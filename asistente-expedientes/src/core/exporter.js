'use strict';
// Markdown → Word (.docx). Formato sobrio de escrito judicial: Times New Roman 12, interlineado 1,5, justificado.

const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType, Table, TableRow, TableCell, WidthType, BorderStyle,
} = require('docx');

const FONT = 'Times New Roman';
const SIZE = 24; // half-points → 12 pt

function runs(text, base = {}) {
  const out = [];
  const re = /(\*\*[^*]+\*\*|\*[^*\n]+\*|`[^`]+`)/g;
  let last = 0;
  let m;
  while ((m = re.exec(text))) {
    if (m.index > last) out.push(new TextRun({ text: text.slice(last, m.index), font: FONT, size: SIZE, ...base }));
    const tok = m[0];
    if (tok.startsWith('**')) out.push(new TextRun({ text: tok.slice(2, -2), bold: true, font: FONT, size: SIZE, ...base }));
    else if (tok.startsWith('`')) out.push(new TextRun({ text: tok.slice(1, -1), font: 'Courier New', size: SIZE - 2, ...base }));
    else out.push(new TextRun({ text: tok.slice(1, -1), italics: true, font: FONT, size: SIZE, ...base }));
    last = m.index + tok.length;
  }
  if (last < text.length) out.push(new TextRun({ text: text.slice(last), font: FONT, size: SIZE, ...base }));
  return out;
}

const border = { style: BorderStyle.SINGLE, size: 4, color: '999999' };
const borders = { top: border, bottom: border, left: border, right: border };

function splitRow(line) {
  return line.trim().replace(/^\|/, '').replace(/\|$/, '').split(/(?<!\\)\|/).map((c) => c.replace(/\\\|/g, '|').trim());
}

function tableFrom(lines) {
  const rows = lines.filter((l) => !/^\s*\|?\s*:?-{2,}/.test(l)).map(splitRow);
  const cols = Math.max(...rows.map((r) => r.length));
  const width = Math.floor(9000 / cols);
  return new Table({
    width: { size: 9000, type: WidthType.DXA },
    columnWidths: Array(cols).fill(width),
    rows: rows.map(
      (r, ri) =>
        new TableRow({
          tableHeader: ri === 0,
          children: Array.from({ length: cols }, (_, ci) =>
            new TableCell({
              borders,
              width: { size: width, type: WidthType.DXA },
              margins: { top: 40, bottom: 40, left: 80, right: 80 },
              shading: ri === 0 ? { fill: 'E8E8E8' } : undefined,
              children: [new Paragraph({ children: runs(r[ci] || '', { size: 20, bold: ri === 0 }) })],
            })
          ),
        })
    ),
  });
}

function markdownToBlocks(md) {
  const lines = md.replace(/\r\n/g, '\n').split('\n');
  const blocks = [];
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    if (!line.trim()) continue;
    if (/^\s*---+\s*$/.test(line)) continue;
    let m;
    if ((m = /^(#{1,4})\s+(.*)$/.exec(line))) {
      const level = [HeadingLevel.HEADING_1, HeadingLevel.HEADING_2, HeadingLevel.HEADING_3, HeadingLevel.HEADING_4][m[1].length - 1];
      blocks.push(new Paragraph({ heading: level, spacing: { before: 240, after: 120 }, children: runs(m[2], { bold: true }) }));
    } else if (line.trim().startsWith('|')) {
      const tbl = [];
      while (i < lines.length && lines[i].trim().startsWith('|')) tbl.push(lines[i++]);
      i--;
      blocks.push(tableFrom(tbl));
      blocks.push(new Paragraph({ children: [] }));
    } else if ((m = /^\s*[-*]\s+(.*)$/.exec(line))) {
      blocks.push(new Paragraph({ bullet: { level: 0 }, spacing: { after: 80 }, children: runs(m[1]) }));
    } else if ((m = /^\s*(\d+)[.)]\s+(.*)$/.exec(line))) {
      blocks.push(new Paragraph({ spacing: { after: 80 }, indent: { left: 360, hanging: 360 }, children: runs(`${m[1]}. ${m[2]}`) }));
    } else if ((m = /^>\s?(.*)$/.exec(line))) {
      blocks.push(new Paragraph({ indent: { left: 360 }, spacing: { after: 120 }, children: runs(m[1], { italics: true }) }));
    } else {
      blocks.push(new Paragraph({ alignment: AlignmentType.JUSTIFIED, spacing: { after: 160, line: 360 }, children: runs(line) }));
    }
  }
  return blocks;
}

async function markdownToDocxBuffer(md, { title = '' } = {}) {
  const children = [];
  if (title) children.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 240 }, children: runs(title, { bold: true, size: 28 }) }));
  children.push(...markdownToBlocks(md));
  const doc = new Document({
    creator: 'Asistente de Expedientes',
    title: title || 'Borrador',
    styles: { default: { document: { run: { font: FONT, size: SIZE } } } },
    sections: [{ properties: { page: { margin: { top: 1440, bottom: 1440, left: 1700, right: 1440 } } }, children }],
  });
  return Packer.toBuffer(doc);
}

module.exports = { markdownToDocxBuffer, markdownToBlocks };
