'use strict';
// Utilidades de normalización de texto en español (sin dependencias).

const STOPWORDS = new Set(
  ('de la que el en y a los del se las por un para con no una su al lo como mas pero sus le ya o este si porque esta ' +
    'entre cuando muy sin sobre tambien me hasta hay donde quien desde todo nos durante todos uno les ni contra otros ' +
    'ese eso ante ellos e esto mi antes algunos que unos yo otro otras otra el tanto esa estos mucho quienes nada muchos ' +
    'cual poco ella estar estas algunas algo nosotros es son fue ser ha han').split(' ')
);

// Palabras típicas de una pregunta ("¿qué dijo el perito sobre…?") que no sirven para localizar el pasaje.
const QUERY_STOPWORDS = new Set(
  ('que quien cual cuales como cuando donde dijo dice dijeron manifesto manifiesta expreso afirmo afirma indico indica ' +
    'sobre respecto acerca buscar busca busque todas todos referencias referencia menciones mencion hay existe').split(' ')
);

function fold(s) {
  return String(s)
    .toLowerCase()
    .normalize('NFD')
    .replace(/[̀-ͯ]/g, '')
    .replace(/\s+/g, ' ')
    .trim();
}

// Stemming ligero: recorta sufijos frecuentes para que "incapacidad"/"incapacidades" coincidan.
function stem(w) {
  if (w.length > 5) w = w.replace(/(mente|aciones|acion|idades|idad|ismos|ismo|adores|ador|ando|iendo|ados|adas|ido|ida|es|s)$/, '');
  return w;
}

function tokenize(s, { keepStop = false, query = false } = {}) {
  const out = [];
  for (const raw of fold(s).split(/[^a-z0-9ñ]+/)) {
    if (!raw) continue;
    if (!keepStop && STOPWORDS.has(raw)) continue;
    if (query && QUERY_STOPWORDS.has(raw)) continue;
    out.push(stem(raw));
  }
  return out;
}

module.exports = { fold, tokenize, stem, STOPWORDS };
