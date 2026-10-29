'use strict';
// Capa de aplicación: independiente de Electron para poder probarla y reutilizarla.

const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const { Case } = require('./casestore');
const { runTask, chronologyMarkdown } = require('./tasks');
const { TASKS } = require('./prompts');
const { createAnthropicLlm, createOllamaLlm, DEFAULT_MODEL } = require('./llm');
const { computeDeadline, makeCalendar, dueSoon, toIcs } = require('./deadlines');
const { markdownToDocxBuffer } = require('./exporter');
const { DEFAULT_BUDGET_CHARS } = require('./context');

const DEFAULT_SETTINGS = {
  provider: 'ollama', // 'ollama' (local, gratis) | 'anthropic' (nube, paga)
  ollamaUrl: 'http://127.0.0.1:11434',
  ollamaModel: 'qwen2.5:7b',
  localBudgetChars: 36000,
  model: DEFAULT_MODEL,
  budgetChars: DEFAULT_BUDGET_CHARS,
  feriados: [], // ["2026-12-08", ...] cargados por el usuario
  ferias: [], // [{desde:"2027-01-01", hasta:"2027-01-31"}, ...]
  recents: [],
  apiKeyEnc: null,
  privacyAccepted: false,
};

class AppService {
  /**
   * @param {{settingsFile:string, encrypt?:(s:string)=>string, decrypt?:(s:string)=>string, llmFactory?:Function}} opts
   */
  constructor({ settingsFile, encrypt = (s) => Buffer.from(s).toString('base64'), decrypt = (s) => Buffer.from(s, 'base64').toString(), llmFactory }) {
    this.settingsFile = settingsFile;
    this.encrypt = encrypt;
    this.decrypt = decrypt;
    this.llmFactory =
      llmFactory ||
      ((s) =>
        s.provider === 'anthropic'
          ? createAnthropicLlm({ apiKey: this.apiKey(), model: s.model })
          : createOllamaLlm({ baseUrl: s.ollamaUrl, model: s.ollamaModel, budgetChars: s.localBudgetChars }));
    this.current = null;
    this.settings = { ...DEFAULT_SETTINGS };
    try {
      this.settings = { ...DEFAULT_SETTINGS, ...JSON.parse(fs.readFileSync(settingsFile, 'utf8')) };
    } catch {}
  }

  // ---------- ajustes ----------
  _saveSettings() {
    fs.mkdirSync(path.dirname(this.settingsFile), { recursive: true });
    fs.writeFileSync(this.settingsFile, JSON.stringify(this.settings, null, 2));
  }
  apiKey() {
    if (process.env.ANTHROPIC_API_KEY) return process.env.ANTHROPIC_API_KEY;
    return this.settings.apiKeyEnc ? this.decrypt(this.settings.apiKeyEnc) : '';
  }
  getSettings() {
    const { apiKeyEnc, ...rest } = this.settings;
    return { ...rest, hasApiKey: !!this.apiKey() };
  }
  updateSettings(patch) {
    const { apiKey, ...rest } = patch;
    if (typeof apiKey === 'string') this.settings.apiKeyEnc = apiKey.trim() ? this.encrypt(apiKey.trim()) : null;
    for (const k of ['provider', 'ollamaUrl', 'ollamaModel', 'localBudgetChars', 'model', 'budgetChars', 'feriados', 'ferias', 'privacyAccepted']) if (k in rest) this.settings[k] = rest[k];
    this._saveSettings();
    return this.getSettings();
  }

  // ---------- caso ----------
  _need() {
    if (!this.current) throw new Error('No hay un expediente abierto.');
    return this.current;
  }
  async openCase(root, onProgress) {
    const c = new Case(root).load();
    this.current = c;
    const r = await c.refresh(onProgress);
    this.settings.recents = [root, ...this.settings.recents.filter((x) => x !== root)].slice(0, 10);
    this._saveSettings();
    return { root: c.root, meta: c.meta, docs: r.docs, errors: r.errors };
  }
  async refresh(onProgress) {
    const c = this._need();
    const r = await c.refresh(onProgress);
    return { docs: r.docs, errors: r.errors };
  }
  updateMeta(patch) {
    const c = this._need();
    for (const k of ['caratula', 'fuero', 'notas']) if (k in patch) c.meta[k] = patch[k];
    c.saveMeta();
    return c.meta;
  }
  tasks() {
    return Object.entries(TASKS).map(([id, t]) => ({ id, label: t.label, hint: t.hint, needs: t.needs || [] }));
  }

  // ---------- búsqueda y lectura ----------
  search(query, k = 12) {
    return this._need().index().search(query, { k });
  }
  getPage(doc, n) {
    const c = this._need();
    const d = c.getDoc(doc);
    const p = c.getPage(doc, n);
    return p ? { doc, n, unit: d.unit, total: d.pages.length, text: p.text, fullPath: path.join(c.root, doc) } : null;
  }

  // ---------- IA ----------
  async run(taskId, params, { onText, signal } = {}) {
    const c = this._need();
    const cloud = this.settings.provider === 'anthropic';
    if (cloud && !this.settings.privacyAccepted) throw new Error('Antes de usar la IA debés aceptar el aviso de confidencialidad (Ajustes).');
    const llm = this.llmFactory(this.settings);
    return runTask({ caseObj: c, taskId, params, llm, budget: cloud ? this.settings.budgetChars : this.settings.localBudgetChars, onText, signal });
  }

  async exportDocx(markdown, filePath, title) {
    const buf = await markdownToDocxBuffer(markdown, { title: title || this._need().meta.caratula });
    fs.writeFileSync(filePath, buf);
    return filePath;
  }

  chronology() {
    const ev = this._need().meta.chronology;
    return ev && ev.length ? chronologyMarkdown(ev).md : null;
  }

  // ---------- plazos ----------
  calendar() {
    return makeCalendar({ feriados: this.settings.feriados, ferias: this.settings.ferias });
  }
  listDeadlines() {
    return [...this._need().meta.deadlines].sort((a, b) => a.fecha.localeCompare(b.fecha));
  }
  /** Calcula (sin guardar) el vencimiento a partir de inicio + días. */
  calcDeadline({ inicio, dias, tipo }) {
    return computeDeadline(inicio, Number(dias), { tipo, calendar: this.calendar() });
  }
  addDeadline(d) {
    const c = this._need();
    if (!/^\d{4}-\d{2}-\d{2}$/.test(d.fecha || '')) throw new Error('Fecha de vencimiento inválida.');
    const item = {
      id: crypto.randomUUID(),
      titulo: d.titulo || 'Plazo',
      fecha: d.fecha,
      nota: d.nota || '',
      origen: d.origen || null,
      calculo: d.calculo || null,
      hecho: false,
    };
    c.meta.deadlines.push(item);
    c.saveMeta();
    return item;
  }
  updateDeadline(id, patch) {
    const c = this._need();
    const d = c.meta.deadlines.find((x) => x.id === id);
    if (!d) throw new Error('Plazo inexistente.');
    for (const k of ['titulo', 'fecha', 'nota', 'hecho']) if (k in patch) d[k] = patch[k];
    c.saveMeta();
    return d;
  }
  removeDeadline(id) {
    const c = this._need();
    c.meta.deadlines = c.meta.deadlines.filter((x) => x.id !== id);
    c.saveMeta();
  }
  deadlinesIcs() {
    const c = this._need();
    return toIcs(c.meta.deadlines, c.meta.caratula);
  }
  /** Recordatorios pendientes (para notificaciones de escritorio) de todos los casos recientes. */
  reminders(todayIso) {
    const out = [];
    for (const root of this.settings.recents) {
      try {
        const meta = JSON.parse(fs.readFileSync(path.join(root, '.asistente', 'case.json'), 'utf8'));
        for (const d of dueSoon(meta.deadlines || [], todayIso)) out.push({ ...d, caratula: meta.caratula, root });
      } catch {}
    }
    return out;
  }
}

module.exports = { AppService, DEFAULT_SETTINGS };
