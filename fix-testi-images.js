const fs = require('fs');
let html = fs.readFileSync('index/index.html', 'utf8');

// Replace initials with images for the 3 available
// Kshipra
html = html.replace(
  '<div class="testi-avatar" style="background:#fff3e0;color:#f57c00;">KA</div>',
  '<img class="testi-avatar" src="../assets/kshipra.jpeg" alt="Kshipra">'
);

// Iqbal
html = html.replace(
  '<div class="testi-avatar" style="background:#f3e5f5;color:#7b1fa2;">IS</div>',
  '<img class="testi-avatar" src="../assets/iqbal.jpeg" alt="Iqbal">'
);

// Jabir
html = html.replace(
  '<div class="testi-avatar" style="background:#fce4ec;color:#c62828;">JK</div>',
  '<img class="testi-avatar" src="../assets/jabir.jpeg" alt="Jabir">'
);

fs.writeFileSync('index/index.html', html);
console.log('Testi images updated!');
