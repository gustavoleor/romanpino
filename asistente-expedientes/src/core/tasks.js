'use strict';
const fs = require('node:fs');
const path = require('node:path');
const { SYSTEM, TASKS } = require('./prompts');
const { buildContext } = require('./context');
const { verifyCitations, renderVerification } = require('./citations');

function parseJsonArray(text) {
  let s = text.trim().replace(/^```(?:json)?\s*/i, '').replace(/```\s*$/, '');
  const a = s.indexOf('[');
  const b = s.lastIndexOf(']');
  if (a < 0 || b < a) throw new Error('El modelo no devolvió un arreglo JSON.');
  return JSON.parse(s.slice(a, b + 1));
}

const cell = (s) => String(s ?? '').replace(/\|/g, '\\|').replace(/\s*\n\s*/g, ' ');

function chronologyMarkdown(events) {
  const sorted = [...events].sort((a, b) => {
    if (a.fecha && b.fecha) return a.fecha.localeCompare(b.fecha);
    if (a.fecha) return -1;
    if (b.fecha) return 1;
    return 0;
  });
  let md = '## Cronología\n\n| Fecha | Tipo | Parte | Hecho / actuación | Respaldo |\n|---|---|---|---|---|\n';
  for (const e of sorted) {
    const fecha = e.fecha || (e.fecha_texto ? `${e.fecha_texto} *(fecha a precisar)*` : 's/f');
    const quote = e.cita ? `«${cell(e.cita)}» ` : '';
    md += `| ${cell(fecha)} | ${cell(e.tipo)} | ${cell(e.parte || '')} | ${cell(e.descripcion)} | ${quote}[Fuente: ${cell(e.doc)}, p. ${e.pagina}] |\n`;
  }
  return { md, sorted };
}

function deadlinesMarkdown(items) {
  let md = '## Fechas y plazos detectados\n\n| Fecha | Tipo | Descripción | Plazo | Respaldo |\n|---|---|---|---|---|\n';
  for (const e of items) {
    const plazo = e.plazo_dias ? `${e.plazo_dias} días ${e.tipo_dias || '(no aclara si hábiles o corridos)'}` : '';
    const quote = e.cita ? `«${cell(e.cita)}» ` : '';
    md += `| ${cell(e.fecha || 's/f')} | ${cell(e.tipo)} | ${cell(e.descripcion)} | ${plazo} | ${quote}[Fuente: ${cell(e.doc)}, p. ${e.pagina}] |\n`;
  }
  return md + '\n> Los vencimientos no se calculan acá: confirmá fecha de inicio y plazo en la solapa **Plazos** y verificalos contra el código procesal y el calendario judicial.\n';
}

/**
 * Ejecuta una tarea sobre el expediente.
 * @returns {{markdown, data, verification, context:{partial,chars}, usage, truncated, savedAs}}
 */
async function runTask({ caseObj, taskId, params = {}, llm, budget, onText, signal }) {
  const task = TASKS[taskId];
  if (!task) throw new Error(`Tarea desconocida: ${taskId}`);
  if (!caseObj.docs.length) throw new Error('El expediente no tiene documentos indexados.');

  const missing = (task.needs || []).filter((n) => !n.split('|').some((alt) => params[alt] && String(params[alt]).trim()));
  if (missing.length) throw new Error(`Falta completar: ${missing.join(', ')}`);

  const query = [params.pedido, params.borrador && params.borrador.slice(0, 2000), params.docA, params.docB].filter(Boolean).join(' ');
  const only = params.only && params.only.length ? params.only : null;
  const ctx = buildContext(caseObj, { query, budget, only });
  const instruction = task.build(params);

  const res = await llm.complete({ system: SYSTEM, context: ctx.text, instruction, onText, signal });

  let markdown = res.text.trim();
  let data = null;
  if (task.json) {
    data = parseJsonArray(markdown);
    markdown = taskId === 'cronologia' ? chronologyMarkdown(data).md : deadlinesMarkdown(data);
    if (taskId === 'cronologia') {
      data = chronologyMarkdown(data).sorted;
      caseObj.meta.chronology = data;
    }
  }

  const verification = verifyCitations(caseObj, markdown);
  let full = markdown + renderVerification(verification);
  if (ctx.partial) {
    full += `\n> ℹ Contexto parcial: el expediente supera el límite de una consulta, se analizaron ${ctx.docs.length} documento(s) con las páginas más relevantes. Los resultados pueden no ser exhaustivos.\n`;
  }
  if (res.truncated) full += '\n> ⚠ La respuesta fue cortada por límite de longitud. Pedí continuar o dividí la tarea.\n';

  // Constancia de lo generado (auditable y reutilizable)
  const dir = path.join(caseObj.metaDir, 'outputs');
  fs.mkdirSync(dir, { recursive: true });
  const stamp = new Date().toISOString().replace(/[:.]/g, '-');
  const savedAs = path.join(dir, `${stamp}-${taskId}.md`);
  fs.writeFileSync(savedAs, full);
  caseObj.meta.history = [{ at: new Date().toISOString(), task: taskId, file: path.basename(savedAs), title: task.label }, ...(caseObj.meta.history || [])].slice(0, 100);
  caseObj.saveMeta();

  return { markdown: full, data, verification, context: { partial: ctx.partial, chars: ctx.chars }, usage: res.usage, truncated: !!res.truncated, savedAs };
}

module.exports = { runTask, parseJsonArray, chronologyMarkdown };
