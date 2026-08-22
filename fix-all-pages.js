const fs = require('fs');
const path = require('path');

const pages = [
  'aerobics/aerobics.html',
  'dance-studio/dance-studio.html',
  'gym-management-software/gym-management-software.html',
  'health-and-fitness-centers/health-and-fitness-centers.html',
  'martial-arts-studio/martial-arts-studio.html',
  'pilates/pilates.html',
  'pt-studio/pt-studio.html',
  'sport-academies/sport-academies.html',
  'swim-school/swim-school.html',
  'yoga-studio/yoga-studio.html'
];

let fixed = 0;
pages.forEach(p => {
  const file = path.join(__dirname, p);
  if (!fs.existsSync(file)) { console.log('SKIP: ' + p); return; }
  
  let html = fs.readFileSync(file, 'utf8');
  
  // Remove old broken module script
  html = html.replace(/<script type="module" crossorigin src="\.\.\/assets\/bussines-jgohSNfB\.js"><\/script>\s*\n/g, '');
  
  // Add open-demo-modal class to nav demobutton
  html = html.replace(
    '<button class="nav__link button " Id="demobutton">',
    '<button class="nav__link button open-demo-modal" Id="demobutton">'
  );
  
  // Add open-demo-modal class to mm-btn-orange buttons
  html = html.replace(
    /<button class="mm-btn mm-btn-orange ">/g,
    '<button class="mm-btn mm-btn-orange open-demo-modal">'
  );
  
  // Add open-demo-modal class to menu backdrop demo button if present
  html = html.replace(
    '<button class="button ">\n                          <p class="button__text">GET YOUR FREE DEMO</p>',
    '<button class="button open-demo-modal">\n                          <p class="button__text">GET YOUR FREE DEMO</p>'
  );
  
  // Add demobutton ID trigger in inline script
  html = html.replace(
    'document.querySelectorAll(".open-demo-modal").forEach(function(btn){\n  btn.addEventListener("click",function(e){e.preventDefault();document.getElementById("demoModal").classList.add("active");});\n});',
    'document.querySelectorAll(".open-demo-modal").forEach(function(btn){\n  btn.addEventListener("click",function(e){e.preventDefault();document.getElementById("demoModal").classList.add("active");});\n});\nvar db=document.getElementById("demobutton");\nif(db){db.addEventListener("click",function(e){e.preventDefault();document.getElementById("demoModal").classList.add("active");});}'
  );
  
  fs.writeFileSync(file, html, 'utf8');
  fixed++;
  console.log('FIXED: ' + p);
});

console.log('Total fixed: ' + fixed);
