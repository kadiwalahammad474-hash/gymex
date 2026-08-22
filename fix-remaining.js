const fs = require('fs');
const path = require('path');

const pages = ['features/features.html', 'pricing/pricing.html'];

pages.forEach(p => {
  const file = path.join(__dirname, p);
  let html = fs.readFileSync(file, 'utf8');
  let fixed = 0;

  // Remove old broken module scripts
  html = html.replace(/<script type="module" crossorigin src="\.\.\/assets\/features--nGinleA\.js"><\/script>\s*\r?\n/g, '');
  html = html.replace(/<script type="module" crossorigin src="\.\.\/assets\/pricing-EvGzq6aa\.js"><\/script>\s*\r?\n/g, '');
  
  // Remove old modulepreload links
  html = html.replace(/<link rel="modulepreload"[^>]*>\s*\r?\n/g, '');

  // Add open-demo-modal class to nav demobutton
  if (html.includes('class="nav__link button " Id="demobutton"')) {
    html = html.replace(
      'class="nav__link button " Id="demobutton"',
      'class="nav__link button open-demo-modal" Id="demobutton"'
    );
    fixed++;
  }

  // Add open-demo-modal class to mm-btn-orange buttons
  html = html.replace(
    /<button class="mm-btn mm-btn-orange ">/g,
    '<button class="mm-btn mm-btn-orange open-demo-modal">'
  );

  // Add open-demo-modal class to menu backdrop demo button
  html = html.replace(
    '<button class="button ">\r\n                          <p class="button__text">GET YOUR FREE DEMO</p>',
    '<button class="button open-demo-modal">\r\n                          <p class="button__text">GET YOUR FREE DEMO</p>'
  );
  html = html.replace(
    '<button class="button ">\n                          <p class="button__text">GET YOUR FREE DEMO</p>',
    '<button class="button open-demo-modal">\n                          <p class="button__text">GET YOUR FREE DEMO</p>'
  );

  // Add demobutton ID trigger in inline script if not already present
  if (!html.includes("document.getElementById('demobutton')")) {
    html = html.replace(
      "document.getElementById('demoModal').addEventListener('click'",
      "var db=document.getElementById('demobutton');\nif(db){db.addEventListener('click',function(e){e.preventDefault();document.getElementById('demoModal').classList.add('active');});}\ndocument.getElementById('demoModal').addEventListener('click'"
    );
  }

  fs.writeFileSync(file, html, 'utf8');
  console.log('FIXED: ' + p);
});
