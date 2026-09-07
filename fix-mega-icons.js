/* ════════════════════════════════════════════════════════════
   fix-mega-icons.js
   Features mega-menu icons ko exact Font Awesome 6 icons se
   replace karta hai (target: Feature Mega Menu Bar design).

   - FA 4.x / other FA link (agar hai) → FA 6.7.2 upgrade
   - FA link nahi hai → <head> me add
   - Har feature item ke inline <svg> ko FA <i> icon se replace
   Run: node fix-mega-icons.js
════════════════════════════════════════════════════════════ */

const fs = require('fs');
const path = require('path');

const FA_LINK = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css">';

/* Label (jaise HTML me likha hai, &amp; use hota hai) → exact FA icon */
const ICONS = {
  'Marketing Management':            '<i class="fa-solid fa-bullhorn"></i>',
  'Lead Management':                 '<i class="fa-solid fa-filter"></i>',
  'Member Management':               '<i class="fa-solid fa-users"></i>',
  'Staff Management':                '<i class="fa-solid fa-user"></i>',
  'Expense Management':              '<i class="fa-solid fa-file-invoice-dollar"></i>',
  'Task Management':                 '<i class="fa-solid fa-clipboard-check"></i>',
  'Data Analysis &amp; Dashboard':   '<i class="fa-solid fa-chart-pie"></i>',
  'Payroll &amp; Commission':        '<i class="fa-solid fa-wallet"></i>',
  'Workout &amp; Diet Planner':      '<svg viewBox="0 0 24 24"><rect x="4" y="4" width="16" height="18" rx="2"/><rect x="9" y="2" width="6" height="3.5" rx="1.2"/><g fill="#eef4fd"><rect x="7.5" y="12.4" width="9" height="1.2" rx="0.6"/><rect x="6.2" y="10.2" width="1.8" height="5.6" rx="0.9"/><rect x="16" y="10.2" width="1.8" height="5.6" rx="0.9"/></g></svg>',
  'Intelligent Alerts &amp; Reminder': '<span class="bell-wrap"><i class="fa-solid fa-bell"></i><span class="bell-dot"></span></span>',
  'Appointment &amp; Class Booking': '<i class="fa-solid fa-calendar-days"></i>',
  'Biometric &amp; Access Control':  '<i class="fa-solid fa-fingerprint"></i>',
  'POS &amp; Locker Management':     '<i class="fa-solid fa-calculator"></i>',
  'Club Facilities':                 '<i class="fa-solid fa-building"></i>',
  'Equipment Inventory':             '<i class="fa-solid fa-dumbbell"></i>',
  'WhatsApp Automation':             '<i class="fa-brands fa-whatsapp"></i>',
  'Mobile Apps':                     '<i class="fa-solid fa-mobile-screen-button"></i>',
  'Integrations':                    '<i class="fa-solid fa-puzzle-piece"></i>',
  /* features.html / business.html ke long mega menu ke extra items */
  'Biometric Attendance':            '<i class="fa-solid fa-fingerprint"></i>',
  'Class Scheduling':                '<i class="fa-solid fa-calendar-days"></i>',
  'Diet &amp; Workout Plans':        '<svg viewBox="0 0 24 24"><rect x="4" y="4" width="16" height="18" rx="2"/><rect x="9" y="2" width="6" height="3.5" rx="1.2"/><g fill="#eef4fd"><rect x="7.5" y="12.4" width="9" height="1.2" rx="0.6"/><rect x="6.2" y="10.2" width="1.8" height="5.6" rx="0.9"/><rect x="16" y="10.2" width="1.8" height="5.6" rx="0.9"/></g></svg>',
  'Member App &amp; Portal':         '<i class="fa-solid fa-mobile-screen-button"></i>',
  'Member Self-Serve':               '<i class="fa-solid fa-user-check"></i>',
  'Payment Gateway':                 '<i class="fa-solid fa-credit-card"></i>',
  'Payment Integration':             '<i class="fa-solid fa-money-bill-transfer"></i>',
  'WhatsApp Marketing':              '<i class="fa-brands fa-whatsapp"></i>'
};

function walk(dir, out) {
  out = out || [];
  let entries;
  try { entries = fs.readdirSync(dir, { withFileTypes: true }); } catch (e) { return out; }
  for (const e of entries) {
    if (e.name === 'node_modules' || e.name === '.git' || e.name === '__MACOSX' || e.name === '.vercel') continue;
    const p = path.join(dir, e.name);
    if (e.isDirectory()) walk(p, out);
    else if (e.name.endsWith('.html')) out.push(p);
  }
  return out;
}

const files = walk(process.cwd());
let updated = 0, scanned = 0;

for (const file of files) {
  let html;
  try { html = fs.readFileSync(file, 'utf8'); } catch (e) { continue; }
  if (!html.includes('mega-desc')) continue;
  scanned++;
  const orig = html;

  /* ── 1. Font Awesome 6 CSS ensure karo ── */
  const faLinkRe = /<link[^>]*(font-awesome|fontawesome)[^>]*>/i;
  if (faLinkRe.test(html)) {
    html = html.replace(faLinkRe, FA_LINK);
  } else if (!html.includes('font-awesome/6.')) {
    if (html.includes('</title>')) {
      html = html.replace('</title>', '</title>\n    ' + FA_LINK);
    } else if (/<meta[^>]*charset[^>]*>/i.test(html)) {
      html = html.replace(/(<meta[^>]*charset[^>]*>)/i, '$1\n    ' + FA_LINK);
    }
  }

  /* ── 2. Har feature item ka svg → FA icon (SAB occurrences) ── */
  for (const [label, iconHtml] of Object.entries(ICONS)) {
    /* HTML me kuch files raw & use karti hain, kuch &amp; — dono markers */
    const markers = ['>' + label, '>' + label.replace('&amp;', '&')];
    let replaced = 0;
    for (const marker of markers) {
      let from = 0;
      for (;;) {
        const idx = html.indexOf(marker, from);
        if (idx === -1) break;
        from = idx + marker.length;

        const around = html.slice(idx, idx + 400);
        if (!around.includes('mega-desc')) continue; /* mobile menu / plain link — skip */

        const iconStart = html.lastIndexOf('<div class="mega-icon">', idx);
        if (iconStart === -1) continue;

        const END = '</svg></div>';
        const svgEnd = html.indexOf(END, iconStart);
        if (svgEnd === -1 || svgEnd > idx) continue;

        html = html.slice(0, iconStart) + '<div class="mega-icon">' + iconHtml + '</div>' + html.slice(svgEnd + END.length);
        replaced++;
      }
    }
    if (replaced === 0) console.log('  MISS  ', path.relative(process.cwd(), file), '→', label);
  }

  if (html !== orig) {
    fs.writeFileSync(file, html);
    updated++;
    console.log('UPDATED', path.relative(process.cwd(), file));
  }
}

console.log('\nDone → ' + updated + ' files updated, ' + scanned + ' mega-menu pages scanned.');
