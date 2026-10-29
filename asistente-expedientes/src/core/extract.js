'use strict';
// Extracción de texto por página desde PDF, DOCX y TXT.
// PDF: páginas reales. DOCX/TXT: no tienen paginación fija, se dividen en "bloques" de tamaño similar.

const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');

const SUPPORTED = new Set(['.pdf', '.docx', '.txt']);
const BLOCK_CHARS = 3000;

function isSupported(file) {
  return SUPPORTED.has(path.extname(file).toLowerCase());
}

function splitIntoBlocks(text) {
  const paras = text.split(/\n{2,}|\r\n\r\n/).map((p) => p.trim()).filter(Boolean);
  const blocks = [];
  let cur = '';
  for (const p of paras) {
    if (cur && cur.length + p.length > BLOCK_CHARS) {
      blocks.push(cur);
      cur = '';
    }
    cur += (cur ? '\n\n' : '') + p;
    while (cur.length > BLOCK_CHARS * 2) {
      blocks.push(cur.slice(0, BLOCK_CHARS * 2));
      cur = cur.slice(BLOCK_CHARS * 2);
    }
  }
  if (cur) blocks.push(cur);
  return blocks.length ? blocks : [''];
}

async function extractPdf(buf) {
  const pdfjs = await import('pdfjs-dist/legacy/build/pdf.mjs');
  const doc = await pdfjs.getDocument({
    data: new Uint8Array(buf),
    useSystemFonts: true,
    disableFontFace: true,
    isEvalSupported: false,
    verbosity: 0,
  }).promise;
  const pages = [];
  for (let n = 1; n <= doc.numPages; n++) {
    const page = await doc.getPage(n);
    const content = await page.getTextContent();
    let text = '';
    for (const item of content.items) {
      text += item.str;
      text += item.hasEOL ? '\n' : ' ';
    }
    pages.push({ n, text: text.replace(/[ \t]+\n/g, '\n').replace(/[ \t]{2,}/g, ' ').trim() });
  }
  await doc.destroy();
  return { unit: 'pág.', pages };
}

async function extractDocx(buf) {
  const mammoth = require('mammoth');
  const { value } = await mammoth.extractRawText({ buffer: buf });
  return { unit: 'bloque', pages: splitIntoBlocks(value).map((text, i) => ({ n: i + 1, text })) };
}

function extractTxt(buf) {
  // UTF-8; si hay caracteres de reemplazo se reintenta como latin1 (archivos viejos de Windows).
  let text = buf.toString('utf8');
  if (text.includes('�')) text = buf.toString('latin1');
  return { unit: 'bloque', pages: splitIntoBlocks(text.replace(/\r\n/g, '\n')).map((t, i) => ({ n: i + 1, text: t })) };
}

/**
 * @returns {Promise<{name, ext, hash, unit, pages:[{n,text}], warnings:string[]}>}
 */
async function extractDocument(filePath) {
  const ext = path.extname(filePath).toLowerCase();
  const buf = fs.readFileSync(filePath);
  const hash = crypto.createHash('sha1').update(buf).digest('hex');
  let r;
  if (ext === '.pdf') r = await extractPdf(buf);
  else if (ext === '.docx') r = await extractDocx(buf);
  else if (ext === '.txt') r = extractTxt(buf);
  else throw new Error(`Formato no soportado: ${ext}`);

  const warnings = [];
  const empty = r.pages.filter((p) => p.text.length < 20).length;
  if (ext === '.pdf' && empty > 0) {
    warnings.push(
      empty === r.pages.length
        ? 'El PDF no tiene texto seleccionable (probablemente escaneado). Requiere OCR antes de ser analizado.'
        : `${empty} de ${r.pages.length} páginas no tienen texto seleccionable (posibles imágenes escaneadas).`
    );
  }
  return { name: path.basename(filePath), ext, hash, unit: r.unit, pages: r.pages, warnings };
}

module.exports = { extractDocument, isSupported, splitIntoBlocks, SUPPORTED };
