const fs = require('fs');
const path = require('path');

const BASE = 'C:/Users/Developer4/Desktop/gymexglobalwebsite';

const pages = [
  'index/index.html',
  'about/about.html',
  'business/business.html',
  'contact/contact.html',
  'features/features.html',
  'pricing/pricing.html',
  'career/career.html',
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

// 1. Merge First Name + Last Name → Your Name
const firstNameRow = /<div class="form-row" style="margin-bottom:16px;">\s*<div><label>First Name \*<\/label><input type="text" name="firstname" placeholder="John" required><\/div>\s*<div><label>Last Name \*<\/label><input type="text" name="lastname" placeholder="Doe" required><\/div>\s*<\/div>/;

const nameField = '<div style="margin-bottom:16px;"><label>Your Name *</label><input type="text" name="fullname" placeholder="Your Full Name" required></div>';

// 2. Remove Business Type dropdown
const bizTypeBlock = /<div style="margin-bottom:16px;"><label>Business Type<\/label>\s*<select name="business_type"[^>]*>[\s\S]*?<\/select>\s*<\/div>/;

let updated = 0;
let errors = 0;

for (const page of pages) {
  const filePath = path.join(BASE, page);
  try {
    let content = fs.readFileSync(filePath, 'utf8');
    let changed = false;

    // Merge First + Last Name → Your Name
    if (firstNameRow.test(content)) {
      content = content.replace(firstNameRow, nameField);
      changed = true;
    }

    // Remove Business Type
    if (bizTypeBlock.test(content)) {
      content = content.replace(bizTypeBlock, '');
      changed = true;
    }

    if (changed) {
      fs.writeFileSync(filePath, content, 'utf8');
      console.log(`UPDATED: ${page}`);
      updated++;
    } else {
      console.log(`NO CHANGE: ${page}`);
    }
  } catch (e) {
    console.log(`ERROR: ${page} - ${e.message}`);
    errors++;
  }
}

console.log(`\nDone! Updated: ${updated}, Errors: ${errors}`);
