const fs = require('fs');
const path = require('path');

const file = path.join(__dirname, 'business', 'business.html');
let html = fs.readFileSync(file, 'utf8');

// 1. Remove old broken module script
html = html.replace(/<script type="module" crossorigin src="\.\.\/assets\/bussines-jgohSNfB\.js"><\/script>\s*\n/g, '');

// 2. Remove old broken backdrop + contact-us wrapper (the div.backdrop > div.contact-us)
html = html.replace(/<div class="backdrop">\s*<div class="contact-us"\s*>\s*<span class="loader" id="loader"><\/span>\s*<button class="close-btn" id="close-contact-modal">[\s\S]*?<\/button>\s*/g, '');

// 3. Add open-demo-modal class to all demo buttons in nav
// Nav button with demobutton ID
html = html.replace(
  '<button class="nav__link button " Id="demobutton">',
  '<button class="nav__link button open-demo-modal" Id="demobutton">'
);

// Hero and CTA buttons (mm-btn-orange)
html = html.replace(
  /<button class="mm-btn mm-btn-orange ">/g,
  '<button class="mm-btn mm-btn-orange open-demo-modal">'
);

// Also fix the menu-backdrop demo button
html = html.replace(
  '<button class="button ">\n                          <p class="button__text">GET YOUR FREE DEMO</p>',
  '<button class="button open-demo-modal">\n                          <p class="button__text">GET YOUR FREE DEMO</p>'
);

// 4. Also add trigger for demobutton ID in the inline script
const oldScript = `document.querySelectorAll(".open-demo-modal").forEach(function(btn){\n  btn.addEventListener("click",function(e){e.preventDefault();document.getElementById("demoModal").classList.add("active");});\n});`;

const newScript = `document.querySelectorAll(".open-demo-modal").forEach(function(btn){\n  btn.addEventListener("click",function(e){e.preventDefault();document.getElementById("demoModal").classList.add("active");});\n});\nvar db=document.getElementById("demobutton");\nif(db){db.addEventListener("click",function(e){e.preventDefault();document.getElementById("demoModal").classList.add("active");});}`;

html = html.replace(oldScript, newScript);

fs.writeFileSync(file, html, 'utf8');
console.log('Business page fixed!');
