'use strict';
// Arma el texto del expediente que se envía al modelo, con marcas de página
// para que pueda citar con precisión.

const DEFAULT_BUDGET_CHARS = 450000; // ≈ 130k tokens de texto en español

const esc = (s) => s.replace(/<\/(pagina|documento|expediente)>/gi, '<\\/$1>');

function renderDoc(doc, pages) {
  let out = `<documento nombre="${doc.name}" unidad="${doc.unit}" total="${doc.pages.length}">\n`;
  for (const p of pages) out += `<pagina n="${p.n}">\n${esc(p.text)}\n</pagina>\n`;
  return out + '</documento>\n';
}

/**
 * Si el expediente entra en el presupuesto se envía completo. Si no, se seleccionan las páginas más
 * relevantes para la consulta (BM25) y se avisa al modelo (y al usuario) que el contexto es parcial.
 */
function buildContext(caseObj, { query = '', budget = DEFAULT_BUDGET_CHARS, only = null } = {}) {
  const docs = caseObj.docs.filter((d) => !only || only.includes(d.name));
  const total = docs.reduce((a, d) => a + d.pages.reduce((x, p) => x + p.text.length, 0), 0);
  const head = `<expediente caratula="${caseObj.meta.caratula || ''}">\n`;

  if (total <= budget) {
    return {
      text: head + docs.map((d) => renderDoc(d, d.pages)).join('') + '</expediente>',
      partial: false,
      chars: total,
      docs: docs.map((d) => d.name),
    };
  }

  const hits = caseObj.index().search(query || 'hechos prueba demanda contestación', { k: 60, docs: docs.map((d) => d.name) });
  const chosen = new Map(); // doc -> Set(page)
  let used = 0;
  for (const h of hits) {
    const page = caseObj.getPage(h.doc, h.page);
    if (!page || used + page.text.length > budget) continue;
    if (!chosen.has(h.doc)) chosen.set(h.doc, new Set());
    chosen.get(h.doc).add(h.page);
    used += page.text.length;
  }
  let text = head + `<aviso>CONTEXTO PARCIAL: el expediente es demasiado extenso; se incluyen solo las páginas más relevantes para la consulta. No afirmes que algo "no consta" en el expediente: indicá que no surge de las páginas provistas.</aviso>\n`;
  for (const d of docs) {
    const set = chosen.get(d.name);
    if (!set) continue;
    text += renderDoc(d, d.pages.filter((p) => set.has(p.n)));
  }
  const index = docs.map((d) => `${d.name} (${d.pages.length} ${d.unit})`).join('; ');
  text += `<indice_completo>${index}</indice_completo>\n</expediente>`;
  return { text, partial: true, chars: used, totalChars: total, docs: [...chosen.keys()] };
}

module.exports = { buildContext, DEFAULT_BUDGET_CHARS };
