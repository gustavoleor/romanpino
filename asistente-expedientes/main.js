'use strict';
const { app, BrowserWindow, ipcMain, dialog, shell, safeStorage, Notification } = require('electron');
const path = require('node:path');
const fs = require('node:fs');
const { AppService } = require('./src/core/service');

let win;
let svc;
let abort = null;

function createService() {
  const encrypt = (s) => {
    if (!safeStorage.isEncryptionAvailable()) {
      throw new Error('Este equipo no ofrece almacenamiento seguro de claves. Definí la variable de entorno ANTHROPIC_API_KEY.');
    }
    return safeStorage.encryptString(s).toString('base64');
  };
  const decrypt = (s) => safeStorage.decryptString(Buffer.from(s, 'base64'));
  return new AppService({ settingsFile: path.join(app.getPath('userData'), 'settings.json'), encrypt, decrypt });
}

function createWindow() {
  win = new BrowserWindow({
    width: 1280,
    height: 860,
    minWidth: 980,
    minHeight: 640,
    title: 'Asistente de Expedientes',
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      contextIsolation: true,
      nodeIntegration: false,
      sandbox: true,
    },
  });
  win.setMenuBarVisibility(false);
  win.loadFile(path.join(__dirname, 'renderer', 'index.html'));
  // Nunca navegar fuera de la app ni abrir ventanas nuevas.
  win.webContents.setWindowOpenHandler(() => ({ action: 'deny' }));
  win.webContents.on('will-navigate', (e) => e.preventDefault());
}

const todayIso = () => {
  const d = new Date();
  return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`;
};

function checkReminders() {
  try {
    const list = svc.reminders(todayIso());
    for (const r of list.slice(0, 5)) {
      const when = r.dias < 0 ? `VENCIDO hace ${-r.dias} día(s)` : r.dias === 0 ? 'vence HOY' : `vence en ${r.dias} día(s)`;
      new Notification({ title: `Plazo: ${r.titulo}`, body: `${r.caratula} — ${when} (${r.fecha})` }).show();
    }
  } catch {}
}

// Envuelve un handler para devolver {ok, data|error} y no filtrar excepciones crudas al renderer.
const handle = (channel, fn) =>
  ipcMain.handle(channel, async (e, ...args) => {
    try {
      return { ok: true, data: await fn(...args) };
    } catch (err) {
      return { ok: false, error: err.message || String(err) };
    }
  });

function inCase(rel) {
  const root = svc.current && svc.current.root;
  if (!root) throw new Error('No hay un expediente abierto.');
  const full = path.resolve(root, rel);
  if (!full.startsWith(root + path.sep)) throw new Error('Ruta fuera del expediente.');
  return full;
}

app.whenReady().then(() => {
  svc = createService();

  handle('settings:get', () => svc.getSettings());
  handle('settings:update', (patch) => svc.updateSettings(patch));
  handle('tasks:list', () => svc.tasks());

  handle('case:pick', async () => {
    const r = await dialog.showOpenDialog(win, { title: 'Elegí la carpeta del expediente', properties: ['openDirectory'] });
    if (r.canceled || !r.filePaths[0]) return null;
    return svc.openCase(r.filePaths[0], (p) => win.webContents.send('case:progress', p));
  });
  handle('case:open', (root) => svc.openCase(root, (p) => win.webContents.send('case:progress', p)));
  handle('case:refresh', () => svc.refresh((p) => win.webContents.send('case:progress', p)));
  handle('case:meta', (patch) => svc.updateMeta(patch));
  handle('case:reveal', () => shell.openPath(svc.current.root));

  handle('doc:page', (doc, n) => svc.getPage(doc, n));
  handle('doc:open', async (doc) => {
    const err = await shell.openPath(inCase(doc));
    if (err) throw new Error(err);
  });
  handle('search', (q) => svc.search(q));

  handle('task:run', async (taskId, params) => {
    abort = new AbortController();
    try {
      return await svc.run(taskId, params, { signal: abort.signal, onText: (t) => win.webContents.send('task:text', t) });
    } finally {
      abort = null;
    }
  });
  handle('task:cancel', () => abort && abort.abort());

  handle('chronology', () => svc.chronology());

  handle('export:docx', async (markdown, suggested) => {
    const r = await dialog.showSaveDialog(win, {
      title: 'Exportar a Word',
      defaultPath: path.join(svc.current ? svc.current.root : app.getPath('documents'), (suggested || 'borrador') + '.docx'),
      filters: [{ name: 'Documento de Word', extensions: ['docx'] }],
    });
    if (r.canceled) return null;
    await svc.exportDocx(markdown, r.filePath);
    shell.showItemInFolder(r.filePath);
    return r.filePath;
  });

  handle('deadlines:list', () => svc.listDeadlines());
  handle('deadlines:calc', (p) => svc.calcDeadline(p));
  handle('deadlines:add', (d) => svc.addDeadline(d));
  handle('deadlines:update', (id, patch) => svc.updateDeadline(id, patch));
  handle('deadlines:remove', (id) => svc.removeDeadline(id));
  handle('deadlines:ics', async () => {
    const r = await dialog.showSaveDialog(win, {
      title: 'Exportar plazos al calendario',
      defaultPath: path.join(app.getPath('documents'), 'plazos.ics'),
      filters: [{ name: 'Calendario (.ics)', extensions: ['ics'] }],
    });
    if (r.canceled) return null;
    fs.writeFileSync(r.filePath, svc.deadlinesIcs());
    return r.filePath;
  });

  createWindow();
  setTimeout(checkReminders, 3000);
  setInterval(checkReminders, 60 * 60 * 1000);
  app.on('activate', () => BrowserWindow.getAllWindows().length === 0 && createWindow());
});

app.on('window-all-closed', () => process.platform !== 'darwin' && app.quit());
