const fs = require('fs');
const path = require('path');

const file = path.join(__dirname, 'about', 'about.html');
let html = fs.readFileSync(file, 'utf8');

// 1. Remove old broken module script
html = html.replace(/<script type="module" crossorigin src="\.\.\/assets\/about-nkCRy7Fi\.js"><\/script>\s*\r?\n/g, '');

// 2. Remove old modulepreload links
html = html.replace(/<link rel="modulepreload"[^>]*>\s*\r?\n/g, '');

// 3. Remove old swiper CSS and JS (loaded from assets - broken)
html = html.replace(/<link rel="stylesheet" crossorigin href="\.\.\/assets\/swiper-XvW90xyx\.css">\s*\r?\n/g, '');

// 4. Add open-demo-modal class to nav demobutton
html = html.replace(
  '<button class="nav__link button " Id="demobutton">',
  '<button class="nav__link button open-demo-modal" Id="demobutton">'
);

// 5. Add open-demo-modal class to mm-btn-orange buttons
html = html.replace(
  /<button class="mm-btn mm-btn-orange ">/g,
  '<button class="mm-btn mm-btn-orange open-demo-modal">'
);

// 6. Add open-demo-modal class to menu backdrop demo button
html = html.replace(
  '<button class="button ">\r\n                          <p class="button__text">GET YOUR FREE DEMO</p>',
  '<button class="button open-demo-modal">\r\n                          <p class="button__text">GET YOUR FREE DEMO</p>'
);

// 7. Add demobutton ID trigger in inline script
html = html.replace(
  "document.querySelectorAll('.open-demo-modal').forEach(function(btn) {\r\n    btn.addEventListener('click', function(e) {\r\n        e.preventDefault();\r\n        document.getElementById('demoModal').classList.add('active');\r\n    });\r\n});",
  "document.querySelectorAll('.open-demo-modal').forEach(function(btn) {\r\n    btn.addEventListener('click', function(e) {\r\n        e.preventDefault();\r\n        document.getElementById('demoModal').classList.add('active');\r\n    });\r\n});\r\nvar db=document.getElementById('demobutton');\r\nif(db){db.addEventListener('click',function(e){e.preventDefault();document.getElementById('demoModal').classList.add('active');});}"
);

fs.writeFileSync(file, html, 'utf8');
console.log('About page fixed!');
