'use strict';
// Búsqueda BM25 local sobre fragmentos (página + ventana), sin enviar nada a la nube.

const { tokenize, fold } = require('./text');

const CHUNK = 1200;
const OVERLAP = 200;

function chunkPage(text) {
  if (text.length <= CHUNK) return [text];
  const out = [];
  for (let i = 0; i < text.length; i += CHUNK - OVERLAP) {
    out.push(text.slice(i, i + CHUNK));
    if (i + CHUNK >= text.length) break;
  }
  return out;
}

class Index {
  /** @param docs [{name, unit, pages:[{n,text}]}] */
  constructor(docs) {
    this.chunks = [];
    for (const d of docs) {
      for (const p of d.pages) {
        for (const text of chunkPage(p.text)) {
          if (!text.trim()) continue;
          const tokens = tokenize(text);
          this.chunks.push({ doc: d.name, unit: d.unit, page: p.n, text, tokens, len: tokens.length });
        }
      }
    }
    this.df = new Map();
    for (const c of this.chunks) for (const t of new Set(c.tokens)) this.df.set(t, (this.df.get(t) || 0) + 1);
    this.avgLen = this.chunks.reduce((a, c) => a + c.len, 0) / (this.chunks.length || 1);
  }

  search(query, { k = 8, docs = null } = {}) {
    const q = tokenize(query, { query: true });
    if (!q.length) return [];
    const N = this.chunks.length;
    const k1 = 1.4;
    const b = 0.75;
    const scored = [];
    for (const c of this.chunks) {
      if (docs && !docs.includes(c.doc)) continue;
      const tf = new Map();
      for (const t of c.tokens) tf.set(t, (tf.get(t) || 0) + 1);
      let score = 0;
      for (const t of q) {
        const f = tf.get(t);
        if (!f) continue;
        const df = this.df.get(t) || 0;
        const idf = Math.log(1 + (N - df + 0.5) / (df + 0.5));
        score += (idf * f * (k1 + 1)) / (f + k1 * (1 - b + (b * c.len) / this.avgLen));
      }
      if (score > 0) scored.push({ ...c, score });
    }
    scored.sort((a, b2) => b2.score - a.score);
    // Un solo fragmento por (doc,página) para variedad de fuentes.
    const seen = new Set();
    const out = [];
    for (const s of scored) {
      const key = `${s.doc}#${s.page}`;
      if (seen.has(key)) continue;
      seen.add(key);
      out.push({ doc: s.doc, unit: s.unit, page: s.page, score: +s.score.toFixed(3), text: s.text, snippet: snippet(s.text, q) });
      if (out.length >= k) break;
    }
    return out;
  }
}

function snippet(text, qTokens, width = 220) {
  const flat = text.replace(/\s+/g, ' ');
  const folded = fold(flat);
  let pos = -1;
  for (const t of qTokens) {
    const i = folded.indexOf(t);
    if (i >= 0 && (pos < 0 || i < pos)) pos = i;
  }
  const start = Math.max(0, (pos < 0 ? 0 : pos) - 60);
  // fold() puede cambiar la longitud (NFD + trim); como aproximación el desfase es mínimo en español.
  return (start > 0 ? '…' : '') + flat.slice(start, start + width) + (start + width < flat.length ? '…' : '');
}

module.exports = { Index, chunkPage };
