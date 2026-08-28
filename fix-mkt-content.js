const fs = require('fs');
let c = fs.readFileSync('marketing-management/marketing-management.html', 'utf8');

// Replace title
c = c.replace(/<title>.*?<\/title>/, '<title>Gym Marketing Software | WhatsApp, SMS & Email Campaigns | Gymex</title>');

// Replace meta description
c = c.replace(/<meta name="description" content=".*?">/, '<meta name="description" content="Attract new gym members, run WhatsApp and SMS campaigns, automate follow-ups, and track marketing ROI with Gymex gym marketing software.');

// Replace meta keywords
c = c.replace(/<meta name="keywords" content=".*?">/, '<meta name="keywords" content="Gym marketing software, gym WhatsApp marketing, gym SMS campaigns, gym email marketing, fitness business marketing, gym member acquisition, gym promotions software">');

// Replace OG tags
c = c.replace(/<meta property="og:title" content=".*?">/, '<meta property="og:title" content="Gym Marketing Software That Attracts and Retains Members | Gymex">');
c = c.replace(/<meta property="og:description" content=".*?">/, '<meta property="og:description" content="Run WhatsApp, SMS, and email campaigns, automate follow-ups, and track which marketing efforts bring real members.');

// Replace sm-label
c = c.replace(/>LEAD MANAGEMENT SOFTWARE</, '>MARKETING MANAGEMENT SOFTWARE<');

// Replace H1
c = c.replace(/Gym <span class="accent">Lead Management<\/span> Software That Turns Enquiries into Members/, 'Gym <span class="accent">Marketing</span> Software That Attracts, Engages & Retains Members');

// Replace hero description
c = c.replace(/Every gym enquiry is an opportunity\. Gymex brings your website enquiries, walk-ins, phone leads, referrals, and campaign responses into one simple sales pipeline\./, 'Gym marketing is not just about posting on social media. Gymex helps you run targeted campaigns, send automated reminders, and track which efforts bring real members.');

fs.writeFileSync('marketing-management/marketing-management.html', c);
console.log('✅ Content replaced');

// Verify
const v = fs.readFileSync('marketing-management/marketing-management.html', 'utf8');
console.log('Title:', v.includes('Marketing Software'));
console.log('Label:', v.includes('MARKETING MANAGEMENT SOFTWARE'));
console.log('H1:', v.includes('Attracts, Engages'));
console.log('Has stray n:', v.split('\n').some(l => l.trim() === 'n'));
