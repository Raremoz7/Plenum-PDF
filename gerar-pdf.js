const puppeteer = require('puppeteer');
const path = require('path');

async function gerarPDF() {
  const browser = await puppeteer.launch({ headless: 'new' });
  const page = await browser.newPage();

  // Carrega o HTML local
  const filePath = 'file://' + path.resolve(__dirname, 'CRM.html').replace(/\\/g, '/');
  await page.goto(filePath, { waitUntil: 'networkidle0', timeout: 30000 });

  // Aguarda fontes do Google carregarem
  await page.evaluateHandle('document.fonts.ready');

  // Gera o PDF
  await page.pdf({
    path: 'Plenum-CRM.pdf',
    format: 'A4',
    printBackground: true,
    margin: { top: 0, right: 0, bottom: 0, left: 0 },
    preferCSSPageSize: false,
  });

  await browser.close();
  console.log('PDF gerado: Plenum-CRM.pdf');
}

gerarPDF().catch(console.error);
