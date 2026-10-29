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

module.exports = { createAnthropicLlm, DEFAULT_MODEL };
