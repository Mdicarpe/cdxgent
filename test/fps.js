const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
  const browser = await puppeteer.launch({args: ['--no-sandbox'], headless: true});
  const page = await browser.newPage();
  await page.setViewport({width:1280, height:720});
  await page.goto('file://' + path.resolve(__dirname, '../index.html'));
  await page.waitForFunction('window.frameTimes && window.frameTimes.length >= 60', {timeout: 10000});
  const avg = await page.evaluate('window.frameTimes.reduce((a,b)=>a+b)/window.frameTimes.length');
  console.log('Average frame time:', avg);
  await browser.close();
  if (avg >= 30) {
    console.error('Average frame time too high:', avg);
    process.exit(1);
  }
  console.log('Performance OK');
})();
