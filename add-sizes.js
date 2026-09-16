/* Add size spec line under each camera placeholder filename on new-style pages */
const fs = require('fs');
const pages = [
  'workout-diet/workout-diet-planner.html',
  'whatsapp-automation/whatsapp-automation.html',
  'pos-locker/pos-locker-management.html',
  'mobile-apps/mobile-apps.html',
  'integrations/integrations.html',
  'equipment-inventory/equipment-inventory.html',
  'appointment-and-class/appointment-and-class.html',
  'lead-management/lead-management.html',
  'task-management/task-management.html',
  'expense-management/expense-management.html',
];
let total = 0;
for (const p of pages) {
  let s = fs.readFileSync(p, 'utf8');
  const before = s;
  // after the filename <p> inside camera placeholders, insert size line
  s = s.replace(
    /(<p style="font-size:11px; color:#aab8c5; margin:4px 0 0;">[^<]+<\/p>)(\s*<\/div>\s*<\/div>)/g,
    (m, p1, p2) => {
      total++;
      return p1 + '\n<p style="font-size:10px; color:#b0c4d8; margin:6px 0 0; letter-spacing:.5px;">SIZE: 1200 &times; 700 px (16:9) &mdash; WebP / PNG</p>' + p2;
    }
  );
  if (s !== before) { fs.writeFileSync(p, s); console.log('OK  ' + p); }
  else console.log('SKIP ' + p + ' (no pattern)');
}
console.log('total size lines added: ' + total);
