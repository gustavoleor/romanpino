'use strict';
// Cliente de IA. Se inyecta en el resto del código para poder probar sin red.

const DEFAULT_MODEL = 'claude-sonnet-5-5';

function createAnthropicLlm({ apiKey, model = DEFAULT_MODEL, maxTokens = 16000 }) {
  if (!apiKey) throw new Error('Falta la clave de API de Anthropic. Configurala en Ajustes.');
  const Anthropic = require('@anthropic-ai/sdk');
  const client = new (Anthropic.default || Anthropic)({ apiKey });

  return {
    model,
    /**
     * @param {{system:string, context:string, instruction:string, onText?:(t:string)=>void, signal?:AbortSignal}} p
     */
    async complete({ system, context, instruction, onText, signal }) {
      const content = [];
      // El expediente va primero y marcado para caché: las tareas siguientes sobre el mismo caso
      // reutilizan el prefijo y salen más rápido y baratas.
      if (context) content.push({ type: 'text', text: context, cache_control: { type: 'ephemeral' } });
      content.push({ type: 'text', text: instruction });

      const stream = client.messages.stream(
        { model, max_tokens: maxTokens, system, messages: [{ role: 'user', content }] },
        { signal }
      );
      if (onText) stream.on('text', onText);
      const msg = await stream.finalMessage();
      const text = msg.content.filter((b) => b.type === 'text').map((b) => b.text).join('');
      return {
        text,
        truncated: msg.stop_reason === 'max_tokens',
        usage: msg.usage,
      };
    },
  };
}

/**
 * IA local con Ollama (gratis, sin enviar nada a internet). Usa la API nativa para fijar num_ctx:
 * por defecto Ollama trunca el contexto en silencio a 2-4k tokens, lo que arruinaría el análisis.
 */
function createOllamaLlm({ baseUrl = 'http://127.0.0.1:11434', model = 'qwen2.5:7b', budgetChars = 36000 }) {
  const numCtx = Math.min(65536, Math.max(8192, Math.ceil(budgetChars / 3) + 6000));
  return {
    model,
    async complete({ system, context, instruction, onText, signal }) {
      let res;
      try {
        res = await fetch(baseUrl.replace(/\/$/, '') + '/api/chat', {
          method: 'POST',
          headers: { 'content-type': 'application/json' },
          signal,
          body: JSON.stringify({
            model,
            stream: true,
            messages: [
              { role: 'system', content: system },
              { role: 'user', content: (context ? context + '\n\n' : '') + instruction },
            ],
            options: { num_ctx: numCtx, num_predict: 4096, temperature: 0.2 },
          }),
        });
      } catch (e) {
        if (e.name === 'AbortError') throw e;
        throw new Error('No se pudo conectar con Ollama. Verificá que esté instalado y abierto (ícono de la llama junto al reloj).');
      }
      if (!res.ok) {
        const detail = await res.text().catch(() => '');
        if (res.status === 404) throw new Error(`El modelo «${model}» no está descargado. En la terminal ejecutá: ollama pull ${model}`);
        throw new Error(`Ollama respondió ${res.status}: ${detail.slice(0, 200)}`);
      }
      const dec = new TextDecoder();
      let buf = '';
      let text = '';
      let last = {};
      for await (const chunk of res.body) {
        buf += dec.decode(chunk, { stream: true });
        let i;
        while ((i = buf.indexOf('\n')) >= 0) {
          const line = buf.slice(0, i).trim();
          buf = buf.slice(i + 1);
          if (!line) continue;
          const j = JSON.parse(line);
          if (j.error) throw new Error('Ollama: ' + j.error);
          if (j.message && j.message.content) {
            text += j.message.content;
            if (onText) onText(j.message.content);
          }
          if (j.done) last = j;
        }
      }
      return {
        text,
        truncated: last.done_reason === 'length',
        usage: { input_tokens: last.prompt_eval_count, output_tokens: last.eval_count },
      };
    },
  };
}

module.exports = { createAnthropicLlm, createOllamaLlm, DEFAULT_MODEL };
