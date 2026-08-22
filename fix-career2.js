const fs = require('fs');
let html = fs.readFileSync('career/career.html', 'utf8');

// Fix hero - add gradient background like other pages
html = html.replace(
  '<header class="mm-hero">',
  '<header class="mm-hero" style="background:radial-gradient(700px 460px at 88% -10%, rgba(2,142,206,.16), transparent 65%), radial-gradient(560px 420px at -8% 30%, rgba(254,79,13,.10), transparent 65%), radial-gradient(500px 380px at 55% 90%, rgba(2,142,206,.08), transparent 70%), var(--BG);">'
);

// Fix hero text alignment
html = html.replace(
  '<h1 class="mm-h1">Let\'s Start<br>Your Career<br><span class="accent">With Gymex</span></h1>',
  '<h1 class="mm-h1" style="font-size:clamp(32px,4vw,48px);">Let\'s Start<br>Your Career<br><span class="accent">With Gymex</span></h1>'
);

// Fix hero description
html = html.replace(
  '<p class="mm-desc">We are hiring talented individuals who are ready to learn, grow, and contribute to our organization. Check our current openings and apply today.</p>',
  '<p class="mm-desc" style="font-size:16px;line-height:1.8;max-width:500px;">We are hiring talented individuals who are ready to learn, grow, and contribute to our organization. Check our current openings and apply today.</p>'
);

// Fix hero image - make it bigger and better
html = html.replace(
  '<div style="width:100%;max-width:400px;height:300px;background:linear-gradient(135deg,var(--blue),var(--orange-100));border-radius:var(--radius);display:flex;align-items:center;justify-content:center;box-shadow:var(--shadow-lg);">',
  '<div style="width:100%;max-width:420px;height:320px;background:linear-gradient(135deg,var(--blue),var(--orange-100));border-radius:24px;display:flex;align-items:center;justify-content:center;box-shadow:0 30px 70px rgba(2,142,206,.28);">'
);

// Fix job card header - add hover effect and better spacing
html = html.replace(
  'class="gx-career-header" style="display:flex;align-items:center;justify-content:space-between;cursor:pointer;flex-wrap:wrap;gap:16px;"',
  'class="gx-career-header" style="display:flex;align-items:center;justify-content:space-between;cursor:pointer;flex-wrap:wrap;gap:20px;padding:8px 0;"'
);

// Fix Apply Now button - make it orange like other pages
html = html.replace(
  /background:var(--blue);color:#fff;padding:10px 24px;border-radius:10px/g,
  'background:linear-gradient(135deg,var(--orange-100),#e0450b);color:#fff;padding:12px 28px;border-radius:100px'
);

// Fix job details section - better styling
html = html.replace(
  'class="gx-career-details" style="display:none;margin-top:16px;padding-top:16px;border-top:1px solid #eef1f8;font-size:13px;color:#555;line-height:1.7;"',
  'class="gx-career-details" style="display:none;margin-top:20px;padding-top:20px;border-top:1px solid #eef1f8;font-size:14px;color:#555;line-height:1.8;"'
);

// Fix section heading
html = html.replace(
  '<h2>Open <span class="accent">Positions</span></h2>',
  '<h2 style="font-size:clamp(28px,3.2vw,38px);font-weight:800;letter-spacing:-0.01em;margin-bottom:10px;">Open <span class="accent">Positions</span></h2>'
);

fs.writeFileSync('career/career.html', html, 'utf8');
console.log('Career page polished!');
