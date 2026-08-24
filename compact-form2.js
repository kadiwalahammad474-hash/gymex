const fs = require('fs');
const path = require('path');

const BASE = 'C:/Users/Developer4/Desktop/gymexglobalwebsite';

const subpages = [
  'aerobics/aerobics.html',
  'dance-studio/dance-studio.html',
  'gym-management-software/gym-management-software.html',
  'health-and-fitness-centers/health-and-fitness-centers.html',
  'marketing-management/marketing-management.html',
  'martial-arts-studio/martial-arts-studio.html',
  'pilates/pilates.html',
  'pt-studio/pt-studio.html',
  'sport-academies/sport-academies.html',
  'swim-school/swim-school.html',
  'yoga-studio/yoga-studio.html'
];

// Subpages have: <div class="form-row"> (no style attribute)
const firstNameRow = /<div class="form-row">\s*<div><label>First Name \*<\/label><input type="text" name="firstname" placeholder="John" required><\/div>\s*<div><label>Last Name \*<\/label><input type="text" name="lastname" placeholder="Doe" required><\/div>\s*<\/div>/;

const nameField = '<div style="margin-bottom:16px;"><label>Your Name *</label><input type="text" name="fullname" placeholder="Your Full Name" required></div>';

let updated = 0;

for (const page of subpages) {
  const filePath = path.join(BASE, page);
  try {
    let content = fs.readFileSync(filePath, 'utf8');
    if (firstNameRow.test(content)) {
      content = content.replace(firstNameRow, nameField);
      fs.writeFileSync(filePath, content, 'utf8');
      console.log(`UPDATED: ${page}`);
      updated++;
    } else {
      console.log(`NO MATCH: ${page}`);
    }
  } catch (e) {
    console.log(`ERROR: ${page} - ${e.message}`);
  }
}

console.log(`\nDone! Updated: ${updated}`);
