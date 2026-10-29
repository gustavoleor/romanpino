'use strict';
const $ = (id) => document.getElementById(id);
const api = window.asistente;

const state = { root: null, meta: null, docs: [], tasks: [], task: null, lastMd: '', lastTitle: '', settings: null, viewer: null };

const FIELD_HELP = {
  escrito: 'Ej.: Borrador de alegato para la parte actora. Identificá los hechos controvertidos, analizá cada prueba y señalá qué afirmaciones están respaldadas por el expediente.',
  pregunta: 'Ej.: ¿Qué dijo el perito sobre la incapacidad?',
  libre: 'Ej.: Prepará un recurso de reposición contra la resolución del 2 de octubre…',
};
const OPTIONAL_FOCUS = new Set(['resumen', 'contradicciones', 'comparar']);

function toast(msg, ms = 4000) {
  const t = $('toast');
  t.textContent = msg;
  t.classList.remove('hidden');
  clearTimeout(toast.t);
  toast.t = setTimeout(() => t.classList.add('hidden'), ms);
}
const fail = (e) => toast('⚠ ' + (e && e.message ? e.message : e), 7000);
const show = (el, on = true) => el.classList.toggle('hidden', !on);

// ---------- navegación ----------
function showTab(name) {
  document.querySelectorAll('#tabs button').forEach((b) => b.classList.toggle('active', b.dataset.tab === name));
  document.querySelectorAll('.tab').forEach((s) => show(s, s.id === 'tab-' + name));
  show($('welcome'), false);
  if (name === 'plazos') loadDeadlines();
  if (name === 'cronologia') loadChronology();
  if (name === 'ajustes') fillSettings();
}
document.querySelectorAll('#tabs button').forEach((b) => (b.onclick = () => showTab(b.dataset.tab)));

// ---------- caso ----------
function applyCase(c) {
  if (!c) return;
  state.root = c.root;
  state.meta = c.meta;
  state.docs = c.docs;
  show($('case-info'));
  show($('tabs'));
  $('case-title').textContent = c.meta.caratula || c.root;
  renderDocs();
  $('progress').textContent = '';
  if (c.errors && c.errors.length) toast(`${c.errors.length} archivo(s) no se pudieron leer`);
  showTab('asistente');
}

function renderDocs() {
  const ul = $('docs');
  ul.textContent = '';
  $('doc-count').textContent = `(${state.docs.length})`;
  for (const d of state.docs) {
    const li = document.createElement('li');
    const cb = document.createElement('input');
    cb.type = 'checkbox';
    cb.checked = true;
    cb.dataset.name = d.name;
    const label = document.createElement('label');
    const name = document.createElement('span');
    name.textContent = d.name;
    const meta = document.createElement('span');
    meta.className = 'muted small';
    meta.textContent = ` ${d.pages} ${d.unit === 'pág.' ? 'pág.' : d.pages === 1 ? 'bloque' : 'bloques'}`;
    label.append(cb, name, meta);
    li.append(label);
    if (d.warnings && d.warnings.length) {
      const w = document.createElement('div');
      w.className = 'warn small';
      w.textContent = '⚠ ' + d.warnings.join(' ');
      li.append(w);
    }
    ul.append(li);
  }
  fillDocSelects();
}

function selectedDocs() {
  const all = [...document.querySelectorAll('#docs input[type=checkbox]')];
  const on = all.filter((c) => c.checked).map((c) => c.dataset.name);
  return on.length === all.length ? null : on;
}

async function openFolder() {
  try {
    applyCase(await api.pickCase());
  } catch (e) {
    fail(e);
  }
}
$('btn-open').onclick = $('btn-open2').onclick = openFolder;
$('btn-settings0').onclick = () => {
  show($('tabs'));
  showTab('ajustes');
};
$('btn-refresh').onclick = async () => {
  try {
    const r = await api.refreshCase();
    state.docs = r.docs;
    renderDocs();
    $('progress').textContent = '';
    toast('Documentos actualizados');
  } catch (e) {
    fail(e);
  }
};
$('btn-reveal').onclick = () => api.revealCase().catch(fail);
api.onProgress((p) => ($('progress').textContent = `Leyendo ${p.i}/${p.total}: ${p.name}`));

// ---------- asistente ----------
function renderTaskGrid() {
  const grid = $('task-grid');
  grid.textContent = '';
  for (const t of state.tasks) {
    const b = document.createElement('button');
    b.className = 'taskcard';
    const h = document.createElement('strong');
    h.textContent = t.label;
    const s = document.createElement('span');
    s.className = 'muted small';
    s.textContent = t.hint;
    b.append(h, s);
    b.onclick = () => selectTask(t);
    grid.append(b);
  }
}

function docSelect(id) {
  const s = document.createElement('select');
  s.id = id;
  return s;
}
function fillDocSelects() {
  for (const id of ['f-docA', 'f-docB', 'f-docBorrador']) {
    const s = $(id);
    if (!s) continue;
    const keep = id === 'f-docBorrador' ? [new Option('— pegar el texto abajo —', '')] : [];
    s.textContent = '';
    for (const o of keep) s.add(o);
    for (const d of state.docs) s.add(new Option(d.name, d.name));
  }
}
function field(label, el) {
  const l = document.createElement('label');
  l.append(document.createTextNode(label), el);
  return l;
}
function textarea(id, ph, rows = 5) {
  const t = document.createElement('textarea');
  t.id = id;
  t.rows = rows;
  t.placeholder = ph || '';
  return t;
}

function selectTask(t) {
  state.task = t;
  document.querySelectorAll('.taskcard').forEach((c) => c.classList.toggle('active', c.firstChild.textContent === t.label));
  $('task-title').textContent = t.label;
  const f = $('task-fields');
  f.textContent = '';
  if (t.id === 'comparar') {
    f.append(field('Documento A', docSelect('f-docA')), field('Documento B', docSelect('f-docB')));
  }
  if (t.id === 'revisar') {
    f.append(field('Borrador que está en la carpeta', docSelect('f-docBorrador')), field('…o pegá el texto del borrador', textarea('f-borrador', '', 10)));
  }
  if (t.needs.includes('pedido') || OPTIONAL_FOCUS.has(t.id) || t.id === 'revisar') {
    const required = t.needs.includes('pedido');
    f.append(field(required ? 'Pedido' : 'Instrucción adicional (opcional)', textarea('f-pedido', FIELD_HELP[t.id] || '', required ? 5 : 2)));
  }
  fillDocSelects();
  if (t.id === 'comparar' && state.docs.length > 1) $('f-docB').selectedIndex = 1;
  show($('task-form'));
  show($('result-card'), false);
}

function params() {
  const p = {};
  const v = (id) => ($(id) ? $(id).value.trim() : '');
  if (v('f-pedido')) p.pedido = v('f-pedido');
  if (v('f-borrador')) p.borrador = v('f-borrador');
  if (v('f-docBorrador')) p.docBorrador = v('f-docBorrador');
  if (v('f-docA')) p.docA = v('f-docA');
  if (v('f-docB')) p.docB = v('f-docB');
  const only = selectedDocs();
  if (only) p.only = only;
  return p;
}

let stream = '';
let offText = null;
async function execute(taskId, p, label, onDone) {
  stream = '';
  const status = $('run-status');
  status.textContent = 'Analizando el expediente…';
  show($('btn-run'), false);
  show($('btn-cancel'), true);
  show($('result-card'));
  $('result').classList.add('streaming');
  $('result').textContent = '';
  if (offText) offText();
  offText = api.onText((t) => {
    stream += t;
    $('result').textContent = stream;
    status.textContent = `Redactando… ${stream.length.toLocaleString('es-AR')} caracteres`;
  });
  try {
    const r = await api.runTask(taskId, p);
    state.lastMd = r.markdown;
    state.lastTitle = label;
    $('result').classList.remove('streaming');
    $('result').innerHTML = window.renderMarkdown(r.markdown);
    const u = r.usage || {};
    status.textContent = u.input_tokens ? `Listo · ${u.input_tokens.toLocaleString('es-AR')} tokens de entrada, ${(u.output_tokens || 0).toLocaleString('es-AR')} de salida` : 'Listo';
    if (onDone) onDone(r);
    return r;
  } catch (e) {
    $('result').classList.remove('streaming');
    $('result').textContent = '';
    status.textContent = '';
    show($('result-card'), false);
    fail(e);
  } finally {
    if (offText) offText();
    offText = null;
    show($('btn-run'), true);
    show($('btn-cancel'), false);
  }
}
$('btn-run').onclick = () => state.task && execute(state.task.id, params(), state.task.label);
$('btn-cancel').onclick = () => api.cancelTask();
$('btn-copy').onclick = () => navigator.clipboard.writeText(state.lastMd).then(() => toast('Copiado'), fail);
$('btn-docx').onclick = () => exportDocx(state.lastMd, state.lastTitle);

async function exportDocx(md, name) {
  if (!md) return toast('No hay nada para exportar');
  try {
    const f = await api.exportDocx(md, (name || 'borrador').replace(/[^\p{L}\p{N} _-]+/gu, '').trim().replace(/ +/g, '-').toLowerCase());
    if (f) toast('Guardado: ' + f, 6000);
  } catch (e) {
    fail(e);
  }
}

// ---------- cronología ----------
async function loadChronology() {
  const md = await api.chronology().catch(() => null);
  $('chron').innerHTML = md ? window.renderMarkdown(md) : '<p class="muted">Todavía no se generó la cronología de este expediente.</p>';
  state.chronMd = md;
}
$('btn-chron-run').onclick = async () => {
  showTab('asistente');
  const t = state.tasks.find((x) => x.id === 'cronologia');
  selectTask(t);
  await execute('cronologia', params(), t.label);
};
$('btn-chron-docx').onclick = () => exportDocx(state.chronMd, 'cronologia');

// ---------- plazos ----------
const fmtDate = (iso) => iso.split('-').reverse().join('/');
async function loadDeadlines() {
  const list = await api.deadlines.list().catch(fail);
  const box = $('dl-list');
  box.textContent = '';
  if (!list || !list.length) {
    box.innerHTML = '<p class="muted">No hay plazos cargados.</p>';
    return;
  }
  const today = new Date();
  const todayIso = `${today.getFullYear()}-${String(today.getMonth() + 1).padStart(2, '0')}-${String(today.getDate()).padStart(2, '0')}`;
  for (const d of list) {
    const days = Math.round((Date.parse(d.fecha) - Date.parse(todayIso)) / 86400000);
    const row = document.createElement('div');
    row.className = 'dl ' + (d.hecho ? 'done' : days < 0 ? 'late' : days <= 3 ? 'soon' : '');
    const cb = document.createElement('input');
    cb.type = 'checkbox';
    cb.checked = d.hecho;
    cb.title = 'Marcar como cumplido';
    cb.onchange = () => api.deadlines.update(d.id, { hecho: cb.checked }).then(loadDeadlines, fail);
    const main = document.createElement('div');
    main.className = 'grow';
    const t = document.createElement('strong');
    t.textContent = d.titulo;
    const sub = document.createElement('div');
    sub.className = 'muted small';
    const calc = d.calculo ? ` · ${d.calculo.dias} días ${d.calculo.tipo === 'habiles' ? 'hábiles' : 'corridos'} desde ${fmtDate(d.calculo.inicio)}` : '';
    const origen = d.origen ? ` · ${d.origen.doc}${d.origen.pagina ? ', p. ' + d.origen.pagina : ''}` : '';
    sub.textContent = `Vence ${fmtDate(d.fecha)}${calc}${origen}`;
    main.append(t, sub);
    const badge = document.createElement('span');
    badge.className = 'badge';
    badge.textContent = d.hecho ? 'cumplido' : days < 0 ? `vencido hace ${-days} d` : days === 0 ? 'HOY' : `en ${days} d`;
    const del = document.createElement('button');
    del.className = 'ghost small';
    del.textContent = 'Quitar';
    del.onclick = () => api.deadlines.remove(d.id).then(loadDeadlines, fail);
    row.append(cb, main, badge, del);
    box.append(row);
  }
}
$('dl-calc').onclick = async () => {
  try {
    if (!$('dl-inicio').value || !$('dl-dias').value) throw new Error('Completá fecha de notificación y cantidad de días.');
    $('dl-fecha').value = await api.deadlines.calc({ inicio: $('dl-inicio').value, dias: $('dl-dias').value, tipo: $('dl-tipo').value });
    $('dl-msg').textContent = 'Vencimiento calculado (verificalo).';
  } catch (e) {
    fail(e);
  }
};
$('dl-add').onclick = async () => {
  try {
    const calculo = $('dl-inicio').value && $('dl-dias').value ? { inicio: $('dl-inicio').value, dias: Number($('dl-dias').value), tipo: $('dl-tipo').value } : null;
    await api.deadlines.add({ titulo: $('dl-titulo').value.trim() || 'Plazo', fecha: $('dl-fecha').value, calculo, origen: state.dlOrigen || null });
    for (const id of ['dl-titulo', 'dl-inicio', 'dl-dias', 'dl-fecha']) $(id).value = '';
    state.dlOrigen = null;
    $('dl-msg').textContent = '';
    loadDeadlines();
  } catch (e) {
    fail(e);
  }
};
$('dl-ics').onclick = () => api.deadlines.ics().then((f) => f && toast('Calendario guardado: ' + f), fail);
$('dl-detect').onclick = async () => {
  showTab('asistente');
  const t = state.tasks.find((x) => x.id === 'plazos');
  selectTask(t);
  const r = await execute('plazos', params(), t.label);
  if (r && r.data) renderDetected(r.data);
};
function renderDetected(items) {
  // Se muestran en la solapa Plazos para precargar el formulario con un clic.
  showTab('plazos');
  const box = $('dl-detected');
  show(box);
  box.textContent = '';
  const h = document.createElement('h3');
  h.textContent = 'Fechas detectadas (revisalas antes de cargarlas)';
  box.append(h);
  for (const it of items) {
    const row = document.createElement('div');
    row.className = 'dl';
    const main = document.createElement('div');
    main.className = 'grow';
    main.textContent = `${it.fecha ? fmtDate(it.fecha) : 's/f'} — ${it.descripcion}${it.plazo_dias ? ` (plazo: ${it.plazo_dias} días ${it.tipo_dias || 'sin aclarar'})` : ''}`;
    const src = document.createElement('div');
    src.className = 'muted small';
    src.textContent = `${it.doc}, p. ${it.pagina}`;
    main.append(src);
    const use = document.createElement('button');
    use.className = 'ghost small';
    use.textContent = 'Usar en el formulario';
    use.onclick = () => {
      $('dl-titulo').value = it.descripcion;
      $('dl-inicio').value = it.fecha || '';
      $('dl-dias').value = it.plazo_dias || '';
      if (it.tipo_dias) $('dl-tipo').value = it.tipo_dias;
      $('dl-msg').textContent = it.plazo_dias && !it.tipo_dias ? '⚠ El documento no aclara si los días son hábiles o corridos: elegí el tipo según la norma aplicable.' : '';
      state.dlOrigen = { doc: it.doc, pagina: it.pagina };
      $('dl-titulo').scrollIntoView({ behavior: 'smooth' });
    };
    row.append(main, use);
    box.append(row);
  }
}

// ---------- búsqueda ----------
async function doSearch() {
  const q = $('q').value.trim();
  if (!q) return;
  const box = $('hits');
  box.textContent = '';
  try {
    const hits = await api.search(q);
    if (!hits.length) box.innerHTML = '<p class="muted">Sin resultados.</p>';
    for (const h of hits) {
      const card = document.createElement('div');
      card.className = 'hit';
      const b = document.createElement('button');
      b.className = 'cite';
      b.dataset.doc = h.doc;
      b.dataset.page = h.page;
      b.textContent = `${h.doc} · ${h.unit} ${h.page}`;
      const p = document.createElement('p');
      p.textContent = h.snippet;
      card.append(b, p);
      box.append(card);
    }
  } catch (e) {
    fail(e);
  }
}
$('btn-search').onclick = doSearch;
$('q').onkeydown = (e) => e.key === 'Enter' && doSearch();

// ---------- visor de páginas ----------
async function openViewer(doc, page) {
  try {
    const d = state.docs.find((x) => x.name === doc);
    const n = Number(page) || 1;
    const p = await api.getPage(doc, n);
    if (!p) throw new Error(`No existe ${doc}${page ? ', p. ' + page : ''} en el expediente.`);
    state.viewer = { doc, n, total: p.total };
    $('viewer-title').textContent = `${doc} — ${p.unit} ${p.n} de ${p.total}`;
    $('viewer-text').textContent = p.text || '(página sin texto extraíble)';
    show($('viewer'));
  } catch (e) {
    fail(e);
  }
}
document.addEventListener('click', (e) => {
  const c = e.target.closest('button.cite');
  if (c) openViewer(c.dataset.doc, c.dataset.page);
});
$('viewer-close').onclick = () => show($('viewer'), false);
$('viewer-prev').onclick = () => state.viewer && state.viewer.n > 1 && openViewer(state.viewer.doc, state.viewer.n - 1);
$('viewer-next').onclick = () => state.viewer && state.viewer.n < state.viewer.total && openViewer(state.viewer.doc, state.viewer.n + 1);
$('viewer-open').onclick = () => state.viewer && api.openDoc(state.viewer.doc).catch(fail);
document.addEventListener('keydown', (e) => e.key === 'Escape' && show($('viewer'), false));

// ---------- ajustes ----------
async function fillSettings() {
  const s = (state.settings = await api.getSettings());
  $('st-privacy').checked = !!s.privacyAccepted;
  $('st-model').value = s.model;
  $('st-budget').value = s.budgetChars;
  $('st-key').value = '';
  $('st-keystate').textContent = s.hasApiKey ? '✓ Hay una clave guardada (no se muestra). Dejá el campo vacío para conservarla.' : 'Todavía no cargaste una clave.';
  $('st-feriados').value = (s.feriados || []).join('\n');
  $('st-ferias').value = (s.ferias || []).map((f) => `${f.desde} ${f.hasta}`).join('\n');
}
$('st-save').onclick = async () => {
  try {
    const lines = (id) => $(id).value.split('\n').map((l) => l.trim()).filter(Boolean);
    const date = /^\d{4}-\d{2}-\d{2}$/;
    const feriados = lines('st-feriados');
    if (feriados.some((f) => !date.test(f))) throw new Error('Los feriados deben tener formato AAAA-MM-DD.');
    const ferias = lines('st-ferias').map((l) => {
      const [desde, hasta] = l.split(/\s+/);
      if (!date.test(desde || '') || !date.test(hasta || '')) throw new Error(`Feria inválida: «${l}». Usá AAAA-MM-DD AAAA-MM-DD.`);
      return { desde, hasta };
    });
    const patch = { privacyAccepted: $('st-privacy').checked, model: $('st-model').value.trim(), budgetChars: Number($('st-budget').value), feriados, ferias };
    if ($('st-key').value.trim()) patch.apiKey = $('st-key').value.trim();
    state.settings = await api.updateSettings(patch);
    $('st-msg').textContent = 'Guardado.';
    fillSettings();
  } catch (e) {
    fail(e);
  }
};

// ---------- inicio ----------
(async function init() {
  try {
    state.tasks = await api.listTasks();
    renderTaskGrid();
    state.settings = await api.getSettings();
    if (!state.settings.privacyAccepted || !state.settings.hasApiKey) toast('Configurá tu clave de API y aceptá el aviso de confidencialidad en Ajustes para usar la IA.', 8000);
  } catch (e) {
    fail(e);
  }
})();
