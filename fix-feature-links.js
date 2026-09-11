/* fix-feature-links.js — remaining placeholder links ko real pages pe point karna (idempotent) */
const fs = require('fs');
const path = require('path');
const ROOT = __dirname;

// name → url (name supports raw & or &amp;)
const LINKS = {
  'WhatsApp Automation': '../whatsapp-automation/whatsapp-automation.html',
  'Workout & Diet Planner': '../workout-diet/workout-diet-planner.html',
  'Diet & Workout Plans': '../workout-diet/workout-diet-planner.html',
  'POS & Locker Management': '../pos-locker/pos-locker-management.html',
  'Mobile Apps': '../mobile-apps/mobile-apps.html',
  'Equipment Inventory': '../equipment-inventory/equipment-inventory.html',
  'Integrations': '../integrations/integrations.html',
};
// mobile-menu label → url
const LABELS = {
  'MOBILE APP': '../mobile-apps/mobile-apps.html',
  'POS MODULE': '../pos-locker/pos-locker-management.html',
  'CLASS SCHEDULING': '../appointment-and-class/appointment-and-class.html',
  'WHATSAPP AUTOMATION': '../whatsapp-automation/whatsapp-automation.html',
};

function esc(s) { return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); }

function fix(html) {
  let out = html;
  // Mega-menu anchors: href=...features/features.html ... class="inside" ... text1 ...>NAME</span>
  for (const [name, url] of Object.entries(LINKS)) {
    const variants = [name, name.replace(/&/g, '&amp;')];
    for (const v of variants) {
      const re = new RegExp('href="(?:\\.\\./)?features/features\\.html"((?:(?!<\\/a>)[\\s\\S])*?class="inside"(?:(?!<\\/a>)[\\s\\S])*?<span class="text1"[^>]*>' + esc(v) + '</span>)', 'g');
      out = out.replace(re, () => 'href="' + url + '"$1');
    }
  }
  // Mobile menu labels
  for (const [label, url] of Object.entries(LABELS)) {
    const re = new RegExp('href="(?:\\.\\./)?features/features\\.html">(' + esc(label) + ')</a>', 'g');
    out = out.replace(re, () => 'href="' + url + '">$1</a>');
  }
  return out;
}

function walk(dir, list = []) {
  for (const f of fs.readdirSync(dir)) {
    if (f === 'node_modules' || f === '.git' || f === '.vercel') continue;
    const fp = path.join(dir, f);
    const st = fs.statSync(fp);
    if (st.isDirectory()) walk(fp, list);
    else if (f.endsWith('.html')) list.push(fp);
  }
  return list;
}

let changed = 0;
for (const f of walk(ROOT)) {
  const src = fs.readFileSync(f, 'utf8');
  const out = fix(src);
  if (out !== src) { fs.writeFileSync(f, out); changed++; console.log('fixed: ' + f); }
}
console.log('Total files fixed: ' + changed);
