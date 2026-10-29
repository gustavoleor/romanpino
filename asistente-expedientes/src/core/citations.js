'use strict';
// Las respuestas del modelo citan así:  «texto textual» [Fuente: demanda.pdf, p. 12]
// Este módulo extrae esas citas y comprueba contra el expediente real que (1) el documento exista,
// (2) la página exista y (3) el texto entre comillas figure efectivamente en esa página.

const { fold } = require('./text');

const CITE_RE = /\[Fuente:\s*([^\]]+)\]/g;
const QUOTE_RE = /[«"“]([^«»"“”]{12,}?)[»"”]\s*$/;

function normForQuote(s) {
  return fold(s).replace(/[^a-z0-9ñ ]+/g, ' ').replace(/\s+/g, ' ').trim();
}

function resolveDoc(caseObj, ref) {
  const want = ref.trim();
  const exact = caseObj.docs.find((d) => d.name === want);
  if (exact) return exact;
  const lower = want.toLowerCase();
  const byLower = caseObj.docs.filter((d) => d.name.toLowerCase() === lower || d.name.toLowerCase().endsWith('/' + lower));
  return byLower.length === 1 ? byLower[0] : null;
}

function parseLocator(s) {
  // "p. 12", "pp. 12-14", "pág. 3", "bloque 2", "fs. 45"
  const m = s.match(/(?:pp?\.?|p[áa]gs?\.?|bloque|fs?\.?|fojas?)\s*(\d+)(?:\s*[-–a]\s*(\d+))?/i);
  if (!m) return null;
  const from = +m[1];
  return { from, to: m[2] ? +m[2] : from };
}

/** Extrae todas las citas de un texto en markdown. */
function extractCitations(text) {
  const out = [];
  let m;
  CITE_RE.lastIndex = 0;
  while ((m = CITE_RE.exec(text))) {
    const before = text.slice(Math.max(0, m.index - 600), m.index);
    const q = before.match(QUOTE_RE);
    for (const part of m[1].split(';')) {
      const idx = part.lastIndexOf(',');
      const docRef = idx >= 0 ? part.slice(0, idx) : part;
      const loc = idx >= 0 ? parseLocator(part.slice(idx + 1)) : null;
      out.push({ raw: m[0], index: m.index, docRef: docRef.trim(), loc, quote: q ? q[1] : null });
    }
  }
  return out;
}

function verifyCitations(caseObj, text) {
  const cites = extractCitations(text);
  const results = cites.map((c) => {
    const doc = resolveDoc(caseObj, c.docRef);
    if (!doc) return { ...c, status: 'doc_inexistente', detail: `No existe el documento «${c.docRef}» en el expediente.` };
    if (!c.loc) return { ...c, doc: doc.name, status: 'sin_pagina', detail: 'La cita no indica página.' };
    const pages = doc.pages.filter((p) => p.n >= c.loc.from && p.n <= c.loc.to);
    if (!pages.length) {
      return { ...c, doc: doc.name, status: 'pagina_inexistente', detail: `${doc.name} tiene ${doc.pages.length} ${doc.unit}; se citó ${c.loc.from}.` };
    }
    if (c.quote) {
      const needle = normForQuote(c.quote);
      const hay = pages.map((p) => normForQuote(p.text)).join(' ');
      if (!hay.includes(needle)) {
        return { ...c, doc: doc.name, status: 'cita_no_hallada', detail: 'El texto entre comillas no figura literalmente en la página citada.' };
      }
      return { ...c, doc: doc.name, status: 'ok_textual', detail: 'Texto verificado literalmente.' };
    }
    return { ...c, doc: doc.name, status: 'ok_referencia', detail: 'Documento y página existen (sin cita textual para cotejar).' };
  });

  const count = (s) => results.filter((r) => r.status === s).length;
  const problems = results.filter((r) => !r.status.startsWith('ok'));
  return {
    total: results.length,
    verificadas_textuales: count('ok_textual'),
    verificadas_referencia: count('ok_referencia'),
    problemas: problems,
    results,
  };
}

function renderVerification(v) {
  if (!v.total) {
    return '\n\n---\n**Control automático de referencias:** el texto no contiene citas `[Fuente: …]`. Ninguna afirmación pudo cotejarse con el expediente.\n';
  }
  let md = `\n\n---\n**Control automático de referencias:** ${v.total} citas · ${v.verificadas_textuales} verificadas literalmente · ${v.verificadas_referencia} con documento/página existentes · ${v.problemas.length} con problemas.\n`;
  if (v.problemas.length) {
    md += '\n| Cita | Problema |\n|---|---|\n';
    for (const p of v.problemas) md += `| ${p.raw.replace(/\|/g, '\\|')} | ${p.detail} |\n`;
    md += '\n> ⚠ Revisá manualmente las citas señaladas antes de usar el texto.\n';
  }
  return md;
}

module.exports = { extractCitations, verifyCitations, renderVerification, resolveDoc, parseLocator };
