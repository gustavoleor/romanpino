// Convierte slides_html/*.html en slides_png/*.png (1600x900, escala 2)
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

(async () => {
  const dir = path.join(__dirname, 'slides_html');
  const out = path.join(__dirname, 'slides_png');
  fs.mkdirSync(out, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1600, height: 900 }, deviceScaleFactor: 1.5 });
  const files = fs.readdirSync(dir).filter(f => f.endsWith('.html')).sort();
  for (const f of files) {
    await page.goto('file://' + path.join(dir, f));
    await page.waitForTimeout(150);
    // Detecta desbordes de contenido para corregirlos
    const overflow = await page.evaluate(() => {
      const w = document.querySelector('.wrap');
      return w.scrollHeight > w.clientHeight + 2 ? (w.scrollHeight - w.clientHeight) : 0;
    });
    if (overflow) console.log('DESBORDE', f, overflow + 'px');
    await page.screenshot({ path: path.join(out, f.replace('.html', '.png')) });
  }
  await browser.close();
  console.log('PNG:', files.length);
})();
