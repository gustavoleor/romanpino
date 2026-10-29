'use strict';
const test = require('node:test');
const assert = require('node:assert/strict');
const { renderMarkdown } = require('../renderer/md');

test('markdown: escapa HTML (no hay XSS desde documentos o respuestas del modelo)', () => {
  const html = renderMarkdown('<img src=x onerror=alert(1)> **ok** [Fuente: <b>a.pdf</b>, p. 1]\n\n| <script>x</script> | b |\n|---|---|\n| 1 | 2 |');
  assert.ok(!/<img|<script|<b>/.test(html));
  assert.match(html, /&lt;img/);
  assert.match(html, /<strong>ok<\/strong>/);
});

test('markdown: citas se vuelven botones con documento y página', () => {
  const html = renderMarkdown('Dato «x» [Fuente: sub/pericia.pdf, p. 4; demanda.txt, bloque 2]');
  assert.match(html, /data-doc="sub\/pericia.pdf" data-page="4"/);
  assert.match(html, /data-doc="demanda.txt" data-page="2"/);
});

test('markdown: tablas, listas y etiquetas de estado', () => {
  const html = renderMarkdown('| H | E |\n|---|---|\n| hecho | ACREDITADO |\n\n- uno\n- dos');
  assert.match(html, /<th>H<\/th>/);
  assert.match(html, /class="tag ok">ACREDITADO/);
  assert.match(html, /<li>dos<\/li>/);
});
