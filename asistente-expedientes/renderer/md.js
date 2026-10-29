// Renderizador Markdown mínimo y seguro (escapa todo el HTML antes de aplicar formato).
(function (root) {
  const esc = (s) => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;').replace(/'/g, '&#39;');

  function cite(inner) {
    return inner
      .split(';')
      .map((part) => {
        const i = part.lastIndexOf(',');
        const doc = (i >= 0 ? part.slice(0, i) : part).trim();
        const loc = i >= 0 ? part.slice(i + 1).trim() : '';
        const m = /(\d+)/.exec(loc);
        if (!doc) return '';
        return `<button class="cite" data-doc="${doc}" data-page="${m ? m[1] : ''}" title="Ver el pasaje en el expediente">${doc}${loc ? ' · ' + loc : ''}</button>`;
      })
      .join(' ');
  }

  function inline(raw) {
    let s = esc(raw);
    s = s.replace(/\[Fuente:\s*([^\]]+)\]/g, (_, inner) => cite(inner));
    s = s.replace(/`([^`]+)`/g, '<code>$1</code>');
    s = s.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
    s = s.replace(/(^|[^*])\*([^*\n]+)\*(?!\*)/g, '$1<em>$2</em>');
    s = s.replace(/(ACREDITADO)/g, '<span class="tag ok">$1</span>')
      .replace(/(CONTROVERTIDO)/g, '<span class="tag warn">$1</span>')
      .replace(/(SIN RESPALDO SUFICIENTE|SIN RESPALDO)/g, '<span class="tag bad">$1</span>')
      .replace(/(\[VERIFICAR NORMA\]|\[Completar:[^\]]*\])/g, '<span class="tag note">$1</span>');
    return s;
  }

  const splitRow = (l) => l.trim().replace(/^\|/, '').replace(/\|$/, '').split(/(?<!\\)\|/).map((c) => c.replace(/\\\|/g, '|').trim());

  function renderMarkdown(md) {
    const lines = String(md).replace(/\r\n/g, '\n').split('\n');
    const out = [];
    for (let i = 0; i < lines.length; i++) {
      const line = lines[i];
      let m;
      if (!line.trim()) continue;
      if (/^\s*---+\s*$/.test(line)) out.push('<hr>');
      else if ((m = /^(#{1,4})\s+(.*)$/.exec(line))) out.push(`<h${m[1].length + 1}>${inline(m[2])}</h${m[1].length + 1}>`);
      else if (line.trim().startsWith('|')) {
        const rows = [];
        while (i < lines.length && lines[i].trim().startsWith('|')) rows.push(lines[i++]);
        i--;
        const body = rows.filter((r) => !/^\s*\|?\s*:?-{2,}/.test(r)).map(splitRow);
        const [head, ...rest] = body;
        out.push(
          '<div class="tablewrap"><table><thead><tr>' + head.map((c) => `<th>${inline(c)}</th>`).join('') + '</tr></thead><tbody>' +
            rest.map((r) => '<tr>' + r.map((c) => `<td>${inline(c)}</td>`).join('') + '</tr>').join('') + '</tbody></table></div>'
        );
      } else if (/^\s*[-*]\s+/.test(line)) {
        const items = [];
        while (i < lines.length && /^\s*[-*]\s+/.test(lines[i])) items.push(lines[i++].replace(/^\s*[-*]\s+/, ''));
        i--;
        out.push('<ul>' + items.map((x) => `<li>${inline(x)}</li>`).join('') + '</ul>');
      } else if (/^\s*\d+[.)]\s+/.test(line)) {
        const items = [];
        while (i < lines.length && /^\s*\d+[.)]\s+/.test(lines[i])) items.push(lines[i++].replace(/^\s*\d+[.)]\s+/, ''));
        i--;
        out.push('<ol>' + items.map((x) => `<li>${inline(x)}</li>`).join('') + '</ol>');
      } else if (/^>\s?/.test(line)) {
        const q = [];
        while (i < lines.length && /^>\s?/.test(lines[i])) q.push(lines[i++].replace(/^>\s?/, ''));
        i--;
        out.push(`<blockquote>${inline(q.join(' '))}</blockquote>`);
      } else {
        const p = [line];
        while (i + 1 < lines.length && lines[i + 1].trim() && !/^(#{1,4}\s|\s*[-*]\s|\s*\d+[.)]\s|>|\||\s*---)/.test(lines[i + 1])) p.push(lines[++i]);
        out.push(`<p>${inline(p.join(' '))}</p>`);
      }
    }
    return out.join('\n');
  }

  if (typeof module !== 'undefined' && module.exports) module.exports = { renderMarkdown, esc };
  else root.renderMarkdown = renderMarkdown;
})(typeof window !== 'undefined' ? window : globalThis);
