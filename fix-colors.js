const fs = require('fs');
const path = require('path');
const base = 'C:/Users/Developer4/Desktop/gymexglobalwebsite';

const pages = [
  'lead-management/lead-management.html',
  'marketing-management/marketing-management.html'
];

// Staff management uses: #f8f9fc for alternating sections, #fff for white sections
// Replace non-standard colors with staff-management theme
const replacements = [
  ['#f8fafc', '#f8f9fc'],
  ['#fff5f5', '#fff'],
  ['#f0fdf4', '#fff'],
  ['#dcfce7', '#fff'],
  ['#e0e7ff', '#f8f9fc'],
  ['#fce7f3', '#fff'],
  ['#fee2e2', '#fff'],
  ['#fef3c7', '#fff'],
  ['#f0f8ff', '#f8f9fc'],
  ['#e0e7ff', '#f8f9fc'],
];

for (const page of pages) {
  let content = fs.readFileSync(path.join(base, page), 'utf8');
  let totalChanges = 0;
  
  for (const [from, to] of replacements) {
    while (content.includes(from)) {
      content = content.replace(from, to);
      totalChanges++;
    }
  }
  
  fs.writeFileSync(path.join(base, page), content);
  console.log(page + ': ' + totalChanges + ' color replacements');
  
  // Verify
  const verify = fs.readFileSync(path.join(base, page), 'utf8');
  const remaining = verify.match(/background:#[a-f0-9]{6}/gi) || [];
  const unique = [...new Set(remaining)];
  console.log('  Remaining bg colors:', unique.join(', '));
}
