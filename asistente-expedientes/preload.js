'use strict';
const { contextBridge, ipcRenderer } = require('electron');

const call = async (channel, ...args) => {
  const r = await ipcRenderer.invoke(channel, ...args);
  if (!r.ok) throw new Error(r.error);
  return r.data;
};
const on = (channel, cb) => {
  const fn = (_e, payload) => cb(payload);
  ipcRenderer.on(channel, fn);
  return () => ipcRenderer.removeListener(channel, fn);
};

contextBridge.exposeInMainWorld('asistente', {
  getSettings: () => call('settings:get'),
  updateSettings: (p) => call('settings:update', p),
  listTasks: () => call('tasks:list'),
  pickCase: () => call('case:pick'),
  openCase: (root) => call('case:open', root),
  refreshCase: () => call('case:refresh'),
  updateMeta: (p) => call('case:meta', p),
  revealCase: () => call('case:reveal'),
  getPage: (doc, n) => call('doc:page', doc, n),
  openDoc: (doc) => call('doc:open', doc),
  search: (q) => call('search', q),
  runTask: (id, params) => call('task:run', id, params),
  cancelTask: () => call('task:cancel'),
  chronology: () => call('chronology'),
  exportDocx: (md, name) => call('export:docx', md, name),
  deadlines: {
    list: () => call('deadlines:list'),
    calc: (p) => call('deadlines:calc', p),
    add: (d) => call('deadlines:add', d),
    update: (id, p) => call('deadlines:update', id, p),
    remove: (id) => call('deadlines:remove', id),
    ics: () => call('deadlines:ics'),
  },
  onText: (cb) => on('task:text', cb),
  onProgress: (cb) => on('case:progress', cb),
});
