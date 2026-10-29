'use strict';
const test = require('node:test');
const assert = require('node:assert/strict');
const http = require('node:http');
const { createOllamaLlm } = require('../src/core/llm');

function server(handler) {
  return new Promise((resolve) => {
    const s = http.createServer(handler);
    s.listen(0, '127.0.0.1', () => resolve({ s, url: `http://127.0.0.1:${s.address().port}` }));
  });
}

test('ollama: envía num_ctx, transmite por partes y devuelve uso', async () => {
  let body;
  const { s, url } = await server((req, res) => {
    let b = '';
    req.on('data', (c) => (b += c));
    req.on('end', () => {
      body = JSON.parse(b);
      res.write(JSON.stringify({ message: { content: 'Hola ' } }) + '\n');
      res.write(JSON.stringify({ message: { content: 'mundo' } }).slice(0, 10)); // línea partida entre chunks
      setTimeout(() => {
        res.write(JSON.stringify({ message: { content: 'mundo' } }).slice(10) + '\n');
        res.end(JSON.stringify({ done: true, done_reason: 'stop', prompt_eval_count: 50, eval_count: 7 }) + '\n');
      }, 20);
    });
  });
  const llm = createOllamaLlm({ baseUrl: url, model: 'm', budgetChars: 36000 });
  const parts = [];
  const r = await llm.complete({ system: 'S', context: 'CTX', instruction: 'INS', onText: (t) => parts.push(t) });
  s.close();
  assert.equal(r.text, 'Hola mundo');
  assert.equal(r.usage.output_tokens, 7);
  assert.equal(r.truncated, false);
  assert.ok(body.options.num_ctx >= 18000, 'num_ctx debe cubrir el contexto');
  assert.match(body.messages[1].content, /CTX[\s\S]*INS/);
});

test('ollama: mensajes claros si no está corriendo o falta el modelo', async () => {
  await assert.rejects(() => createOllamaLlm({ baseUrl: 'http://127.0.0.1:1' }).complete({ system: '', instruction: 'x' }), /No se pudo conectar con Ollama/);
  const { s, url } = await server((_, res) => { res.statusCode = 404; res.end('{"error":"model not found"}'); });
  await assert.rejects(() => createOllamaLlm({ baseUrl: url, model: 'zzz' }).complete({ system: '', instruction: 'x' }), /ollama pull zzz/);
  s.close();
});
