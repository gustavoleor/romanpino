'use strict';
// Cálculo de vencimientos y recordatorios. Las fechas se manejan como "YYYY-MM-DD" en UTC
// para evitar corrimientos por huso horario.
//
// IMPORTANTE: el cómputo es una ayuda. Cada jurisdicción tiene reglas propias (días y horas
// hábiles, feria judicial, plazo de gracia, notificación ficta). El usuario define los días
// inhábiles; la app NO los inventa y siempre marca el resultado como "a verificar".

const toDate = (iso) => {
  const m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(iso);
  if (!m) throw new Error(`Fecha inválida: ${iso}`);
  return new Date(Date.UTC(+m[1], +m[2] - 1, +m[3]));
};
const toIso = (d) => d.toISOString().slice(0, 10);
const addDays = (d, n) => new Date(d.getTime() + n * 86400000);

function makeCalendar({ feriados = [], ferias = [] } = {}) {
  const set = new Set(feriados);
  const ranges = ferias.map((f) => [f.desde, f.hasta]);
  return (iso) => {
    const wd = toDate(iso).getUTCDay();
    if (wd === 0 || wd === 6) return false;
    if (set.has(iso)) return false;
    return !ranges.some(([a, b]) => iso >= a && iso <= b);
  };
}

/**
 * Suma `n` días a partir del día siguiente a `startIso` (regla general: no se cuenta el día de la notificación).
 * tipo 'habiles' salta días inhábiles; 'corridos' no. Si el vencimiento cae en día inhábil, se corre al
 * primer día hábil siguiente.
 */
function computeDeadline(startIso, n, { tipo = 'habiles', calendar } = {}) {
  const isBusiness = calendar || makeCalendar();
  let d = toDate(startIso);
  if (tipo === 'corridos') {
    d = addDays(d, n);
  } else {
    let left = n;
    while (left > 0) {
      d = addDays(d, 1);
      if (isBusiness(toIso(d))) left--;
    }
  }
  while (!isBusiness(toIso(d))) d = addDays(d, 1);
  return toIso(d);
}

function daysUntil(iso, todayIso) {
  return Math.round((toDate(iso) - toDate(todayIso)) / 86400000);
}

function dueSoon(deadlines, todayIso, thresholds = [7, 3, 1, 0]) {
  return deadlines
    .filter((d) => !d.hecho)
    .map((d) => ({ ...d, dias: daysUntil(d.fecha, todayIso) }))
    .filter((d) => d.dias < 0 || thresholds.includes(d.dias))
    .sort((a, b) => a.dias - b.dias);
}

function escapeIcs(s) {
  return String(s).replace(/\\/g, '\\\\').replace(/;/g, '\;').replace(/,/g, '\\,').replace(/\r?\n/g, '\\n');
}

/** Genera un .ics con recordatorio 3 días y 1 día antes (importable en Google Calendar / Outlook). */
function toIcs(deadlines, caratula = 'Expediente') {
  const stamp = new Date().toISOString().replace(/[-:]/g, '').replace(/\.\d+/, '');
  const lines = ['BEGIN:VCALENDAR', 'VERSION:2.0', 'PRODID:-//Asistente de Expedientes//ES', 'CALSCALE:GREGORIAN'];
  for (const d of deadlines.filter((x) => !x.hecho)) {
    const day = d.fecha.replace(/-/g, '');
    const next = toIso(addDays(toDate(d.fecha), 1)).replace(/-/g, '');
    lines.push(
      'BEGIN:VEVENT',
      `UID:${d.id}@asistente-expedientes`,
      `DTSTAMP:${stamp}`,
      `DTSTART;VALUE=DATE:${day}`,
      `DTEND;VALUE=DATE:${next}`,
      `SUMMARY:${escapeIcs(`[${caratula}] ${d.titulo}`)}`,
      `DESCRIPTION:${escapeIcs(d.nota || '')}`,
      'BEGIN:VALARM', 'ACTION:DISPLAY', 'DESCRIPTION:Vencimiento en 3 días', 'TRIGGER:-P3D', 'END:VALARM',
      'BEGIN:VALARM', 'ACTION:DISPLAY', 'DESCRIPTION:Vencimiento mañana', 'TRIGGER:-P1D', 'END:VALARM',
      'END:VEVENT'
    );
  }
  lines.push('END:VCALENDAR');
  return lines.join('\r\n') + '\r\n';
}

module.exports = { computeDeadline, makeCalendar, daysUntil, dueSoon, toIcs, toDate, toIso };
