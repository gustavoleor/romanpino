'use strict';
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const { makeDemo } = require('../scripts/make-demo');
const { Case } = require('../src/core/casestore');
const { verifyCitations, extractCitations } = require('../src/core/citations');
const { computeDeadline, makeCalendar, toIcs, dueSoon } = require('../src/core/deadlines');
const { markdownToDocxBuffer } = require('../src/core/exporter');
const { runTask, parseJsonArray } = require('../src/core/tasks');
const { buildContext } = require('../src/core/context');
const { AppService } = require('../src/core/service');

const tmp = () => fs.mkdtempSync(path.join(os.tmpdir(), 'exp-'));

async function demoCase() {
  const dir = tmp();
  makeDemo(dir);
  const c = new Case(dir);
  await c.refresh();
  return c;
}

test('extrae páginas reales de PDF y bloques de TXT', async () => {
  const c = await demoCase();
  const pericia = c.getDoc('04-pericia-medica.pdf');
  assert.equal(pericia.pages.length, 4);
  assert.equal(pericia.unit, 'pág.');
  assert.match(pericia.pages[3].text, /incapacidad parcial y permanente del 12%/);
  assert.equal(c.getDoc('01-demanda.txt').unit, 'bloque');
  assert.equal(c.summary().length, 5);
});

test('reindexado incremental: no reprocesa archivos sin cambios', async () => {
  const c = await demoCase();
  const before = JSON.stringify(c.docs[0].pages);
  let processed = 0;
  await c.refresh(() => processed++);
  assert.equal(processed, 0);
  assert.equal(JSON.stringify(c.docs[0].pages), before);
  fs.appendFileSync(path.join(c.root, '05-resolucion.txt'), '\n\nNuevo párrafo.');
  await c.refresh(() => processed++);
  assert.equal(processed, 1);
});

test('búsqueda local devuelve la página correcta', async () => {
  const c = await demoCase();
  const hits = c.index().search('¿qué dijo el perito sobre la incapacidad?');
  assert.equal(hits[0].doc, '04-pericia-medica.pdf');
  assert.equal(hits[0].page, 4);
  const fecha = c.index().search('fecha de ingreso del actor');
  assert.ok(fecha.slice(0, 3).some((h) => h.doc === '02-contestacion.txt' || h.doc === '01-demanda.txt'));
});

test('verificación de citas: detecta documento inexistente, página inexistente y cita no literal', async () => {
  const c = await demoCase();
  const md = [
    '«una incapacidad parcial y permanente del 12% de la total obrera» [Fuente: 04-pericia-medica.pdf, p. 4]',
    '«el actor tiene una incapacidad del 40%» [Fuente: 04-pericia-medica.pdf, p. 4]',
    'Hecho sin cita textual [Fuente: 04-pericia-medica.pdf, p. 2]',
    'Página fuera de rango [Fuente: 04-pericia-medica.pdf, p. 9]',
    'Doc inventado [Fuente: informe-inventado.pdf, p. 1]',
    'Sin página [Fuente: 01-demanda.txt]',
  ].join('\n');
  const v = verifyCitations(c, md);
  assert.equal(v.total, 6);
  const st = v.results.map((r) => r.status);
  assert.deepEqual(st, ['ok_textual', 'cita_no_hallada', 'ok_referencia', 'pagina_inexistente', 'doc_inexistente', 'sin_pagina']);
});

test('citas múltiples y rangos de páginas', async () => {
  const c = await demoCase();
  const cites = extractCitations('x [Fuente: 04-pericia-medica.pdf, pp. 2-3; 01-demanda.txt, bloque 1]');
  assert.equal(cites.length, 2);
  assert.deepEqual(cites[0].loc, { from: 2, to: 3 });
  const v = verifyCitations(c, 'x [Fuente: 04-pericia-medica.pdf, pp. 2-3; 01-demanda.txt, bloque 1]');
  assert.equal(v.problemas.length, 0);
});

test('plazos: días hábiles con feriados y feria; vencimiento en día inhábil se corre', () => {
  const cal = makeCalendar({ feriados: ['2025-10-06'], ferias: [] });
  // Notificado jueves 2/10/2025 + 5 hábiles: 3,6(feriado),7,8,9 → jueves... cuenta: vie 3(1), lun 6 feriado, mar 7(2), mié 8(3), jue 9(4), vie 10(5)
  assert.equal(computeDeadline('2025-10-02', 5, { tipo: 'habiles', calendar: cal }), '2025-10-10');
  // Sin feriado
  assert.equal(computeDeadline('2025-10-02', 5, { tipo: 'habiles', calendar: makeCalendar() }), '2025-10-09');
  // Corridos que caen sábado → lunes
  assert.equal(computeDeadline('2025-10-03', 8, { tipo: 'corridos', calendar: makeCalendar() }), '2025-10-13');
  // Feria
  const feria = makeCalendar({ ferias: [{ desde: '2026-07-01', hasta: '2026-07-15' }] });
  assert.equal(computeDeadline('2026-06-30', 1, { tipo: 'habiles', calendar: feria }), '2026-07-16');
});

test('recordatorios e ICS', () => {
  const ds = [
    { id: 'a', titulo: 'Contestar traslado', fecha: '2025-10-10', hecho: false },
    { id: 'b', titulo: 'Hecho', fecha: '2025-10-10', hecho: true },
    { id: 'c', titulo: 'Lejano', fecha: '2025-12-01', hecho: false },
    { id: 'd', titulo: 'Vencido', fecha: '2025-10-01', hecho: false },
  ];
  const due = dueSoon(ds, '2025-10-07');
  assert.deepEqual(due.map((d) => d.id), ['d', 'a']);
  const ics = toIcs(ds, 'Pérez c/ Alfa');
  assert.equal((ics.match(/BEGIN:VEVENT/g) || []).length, 3);
  assert.match(ics, /TRIGGER:-P3D/);
});

test('exporta a .docx válido (zip) con tablas y negritas', async () => {
  const buf = await markdownToDocxBuffer('# Título\n\nTexto con **negrita** y *cursiva*.\n\n| A | B |\n|---|---|\n| 1 | 2 |\n\n- ítem uno\n- ítem dos\n', { title: 'Borrador' });
  assert.equal(buf.slice(0, 2).toString(), 'PK');
  const mammoth = require('mammoth');
  const { value } = await mammoth.extractRawText({ buffer: buf });
  assert.match(value, /Texto con negrita y cursiva/);
  assert.match(value, /ítem dos/);
});

test('JSON del modelo: tolera fences y texto alrededor', () => {
  assert.deepEqual(parseJsonArray('```json\n[{"a":1}]\n```'), [{ a: 1 }]);
  assert.deepEqual(parseJsonArray('Aquí va: [{"a":2}] fin'), [{ a: 2 }]);
  assert.throws(() => parseJsonArray('sin json'));
});

test('contexto: completo si entra en el presupuesto, parcial si no', async () => {
  const c = await demoCase();
  const full = buildContext(c, {});
  assert.equal(full.partial, false);
  assert.match(full.text, /<documento nombre="04-pericia-medica.pdf" unidad="pág." total="4">/);
  const part = buildContext(c, { query: 'incapacidad perito', budget: 1500 });
  assert.equal(part.partial, true);
  assert.match(part.text, /CONTEXTO PARCIAL/);
  assert.match(part.text, /<pagina n="4">/);
});

test('runTask: tarea markdown agrega control de referencias y guarda constancia', async () => {
  const c = await demoCase();
  const llm = {
    async complete({ system, context, instruction }) {
      assert.match(system, /NO inventes|no inventes/i);
      assert.match(context, /<expediente/);
      assert.match(instruction, /incapacidad/);
      return { text: '**ACREDITADO** «incapacidad parcial y permanente del 12%» [Fuente: 04-pericia-medica.pdf, p. 4]. Inventado: «cosa falsa que no figura» [Fuente: 04-pericia-medica.pdf, p. 1]', usage: {} };
    },
  };
  const r = await runTask({ caseObj: c, taskId: 'pregunta', params: { pedido: '¿Qué dijo el perito sobre la incapacidad?' }, llm });
  assert.equal(r.verification.total, 2);
  assert.equal(r.verification.problemas.length, 1);
  assert.match(r.markdown, /Control automático de referencias/);
  assert.match(r.markdown, /no figura literalmente/);
  assert.ok(fs.existsSync(r.savedAs));
  assert.equal(c.meta.history[0].task, 'pregunta');
});

test('runTask: cronología JSON se ordena por fecha y se verifica', async () => {
  const c = await demoCase();
  const llm = {
    async complete() {
      return {
        text: JSON.stringify([
          { fecha: '2023-03-17', fecha_texto: '17 de marzo de 2023', tipo: 'notificacion', parte: 'actora', descripcion: 'Telegrama', cita: 'intimó fehacientemente por telegrama el 17 de marzo de 2023', doc: '01-demanda.txt', pagina: 1 },
          { fecha: '2018-03-01', fecha_texto: '1 de marzo de 2018', tipo: 'hecho', parte: 'actora', descripcion: 'Ingreso según actor', cita: 'ingresó a trabajar para la demandada el 1 de marzo de 2018', doc: '01-demanda.txt', pagina: 1 },
          { fecha: null, fecha_texto: 'septiembre de 2022', tipo: 'hecho', parte: 'tercero', descripcion: 'Accidente (testigo)', cita: 'Se lastimó la espalda levantando cajas', doc: '03-acta-testimonial.txt', pagina: 1 },
        ]),
        usage: {},
      };
    },
  };
  const r = await runTask({ caseObj: c, taskId: 'cronologia', llm });
  assert.equal(r.data[0].fecha, '2018-03-01');
  assert.equal(r.data[2].fecha, null);
  assert.equal(r.verification.problemas.length, 0, JSON.stringify(r.verification.problemas));
  assert.ok(c.meta.chronology.length === 3);
});

test('runTask: valida parámetros requeridos', async () => {
  const c = await demoCase();
  await assert.rejects(() => runTask({ caseObj: c, taskId: 'escrito', params: {}, llm: {} }), /Falta completar/);
  await assert.rejects(() => runTask({ caseObj: c, taskId: 'revisar', params: {}, llm: {} }), /Falta completar/);
});

test('servicio: exige aceptar confidencialidad, guarda clave cifrada y no la expone', async () => {
  const dir = tmp();
  makeDemo(path.join(dir, 'caso'));
  let called = 0;
  const svc = new AppService({
    settingsFile: path.join(dir, 'cfg', 'settings.json'),
    encrypt: (s) => 'ENC:' + s.split('').reverse().join(''),
    decrypt: (s) => s.slice(4).split('').reverse().join(''),
    llmFactory: () => ({ complete: async () => (called++, { text: 'ok [Fuente: 01-demanda.txt, bloque 1]', usage: {} }) }),
  });
  const opened = await svc.openCase(path.join(dir, 'caso'));
  assert.equal(opened.docs.length, 5);
  await assert.rejects(() => svc.run('resumen', {}), /confidencialidad/);
  svc.updateSettings({ privacyAccepted: true, apiKey: 'sk-ant-secreta' });
  assert.equal(svc.apiKey(), 'sk-ant-secreta');
  const raw = fs.readFileSync(path.join(dir, 'cfg', 'settings.json'), 'utf8');
  assert.ok(!raw.includes('sk-ant-secreta'));
  assert.equal(svc.getSettings().apiKeyEnc, undefined);
  assert.equal(svc.getSettings().hasApiKey, true);
  const r = await svc.run('resumen', {});
  assert.equal(called, 1);
  assert.equal(r.verification.problemas.length, 0);

  // plazos persistentes y recordatorios entre sesiones
  const item = svc.addDeadline({ titulo: 'Contestar traslado', fecha: '2025-10-09', origen: { doc: '05-resolucion.txt', pagina: 1 } });
  assert.equal(svc.listDeadlines().length, 1);
  const svc2 = new AppService({ settingsFile: path.join(dir, 'cfg', 'settings.json') });
  assert.equal(svc2.reminders('2025-10-09')[0].titulo, 'Contestar traslado');
  svc.updateDeadline(item.id, { hecho: true });
  assert.equal(svc2.reminders('2025-10-09').length, 0);
});
