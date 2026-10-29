'use strict';
// Un "caso" es una carpeta del usuario. Todo lo que genera la app se guarda en <carpeta>/.asistente/
// (índice de texto, metadatos, plazos), de modo que el expediente y su análisis viajan juntos y no
// dependen de ninguna base de datos externa.

const fs = require('node:fs');
const path = require('node:path');
const { extractDocument, isSupported } = require('./extract');
const { Index } = require('./search');

const META_DIR = '.asistente';
const INDEX_VERSION = 1;

function listFiles(root) {
  const out = [];
  (function walk(dir) {
    for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
      if (e.name.startsWith('.') || e.name.startsWith('~$')) continue;
      const full = path.join(dir, e.name);
      if (e.isDirectory()) walk(full);
      else if (e.isFile() && isSupported(e.name)) out.push(full);
    }
  })(root);
  return out.sort((a, b) => a.localeCompare(b, 'es'));
}

function readJson(file, fallback) {
  try {
    return JSON.parse(fs.readFileSync(file, 'utf8'));
  } catch {
    return fallback;
  }
}

function writeJson(file, data) {
  fs.mkdirSync(path.dirname(file), { recursive: true });
  const tmp = file + '.tmp';
  fs.writeFileSync(tmp, JSON.stringify(data));
  fs.renameSync(tmp, file);
}

class Case {
  constructor(root) {
    this.root = path.resolve(root);
    this.metaDir = path.join(this.root, META_DIR);
    this.docs = [];
    this.meta = readJson(path.join(this.metaDir, 'case.json'), {
      caratula: path.basename(this.root),
      fuero: '',
      notas: '',
      deadlines: [],
      chronology: null,
      history: [],
    });
    this._index = null;
  }

  /** Indexa/actualiza los documentos. Solo reprocesa los archivos nuevos o modificados. */
  async refresh(onProgress = () => {}) {
    const prev = readJson(path.join(this.metaDir, 'index.json'), { version: 0, docs: [] });
    const prevByName = new Map(prev.version === INDEX_VERSION ? prev.docs.map((d) => [d.name, d]) : []);
    const files = listFiles(this.root);
    const docs = [];
    const errors = [];
    let i = 0;
    for (const file of files) {
      const name = path.relative(this.root, file).split(path.sep).join('/');
      const st = fs.statSync(file);
      const old = prevByName.get(name);
      i++;
      if (old && old.size === st.size && old.mtimeMs === st.mtimeMs) {
        docs.push(old);
        continue;
      }
      onProgress({ i, total: files.length, name });
      try {
        const d = await extractDocument(file);
        docs.push({ name, size: st.size, mtimeMs: st.mtimeMs, hash: d.hash, unit: d.unit, pages: d.pages, warnings: d.warnings });
      } catch (err) {
        errors.push({ name, error: err.message });
        docs.push({ name, size: st.size, mtimeMs: st.mtimeMs, hash: null, unit: 'bloque', pages: [], warnings: [`No se pudo leer: ${err.message}`] });
      }
    }
    this.docs = docs;
    this._index = null;
    writeJson(path.join(this.metaDir, 'index.json'), { version: INDEX_VERSION, docs });
    return { docs: this.summary(), errors };
  }

  load() {
    const idx = readJson(path.join(this.metaDir, 'index.json'), null);
    this.docs = idx && idx.version === INDEX_VERSION ? idx.docs : [];
    return this;
  }

  summary() {
    return this.docs.map((d) => ({
      name: d.name,
      unit: d.unit,
      pages: d.pages.length,
      chars: d.pages.reduce((a, p) => a + p.text.length, 0),
      warnings: d.warnings || [],
    }));
  }

  index() {
    if (!this._index) this._index = new Index(this.docs);
    return this._index;
  }

  getDoc(name) {
    return this.docs.find((d) => d.name === name) || null;
  }

  getPage(name, n) {
    const d = this.getDoc(name);
    return d ? d.pages.find((p) => p.n === n) || null : null;
  }

  saveMeta() {
    writeJson(path.join(this.metaDir, 'case.json'), this.meta);
  }
}

module.exports = { Case, listFiles, META_DIR };
