/* ════════════════════════════════════════════════════════════
   build-new-features.js
   6 missing feature pages banata hai docx content se:
   Workout & Diet, POS & Locker, Mobile Apps, Integrations,
   Equipment Inventory, WhatsApp Automation
   + mega menu links update + sitemap update
   Run: node build-new-features.js
════════════════════════════════════════════════════════════ */
const fs = require('fs');
const path = require('path');

const ROOT = __dirname;
const template = fs.readFileSync(path.join(ROOT, 'appointment-and-class/appointment-and-class.html'), 'utf8');

// ── Extract nav + footer from template ──
const navStart = template.indexOf('<body>') + '<body>'.length;
const heroMark = template.indexOf('<!-- HERO -->');
const footerMark = template.indexOf('<!-- FOOTER from Home -->');
const NAV = template.slice(navStart, heroMark);
const FOOTER = template.slice(footerMark, template.lastIndexOf('</body>'));

// ── Shared helpers ──
const IMG = (label, file) => `<div style="background:#f0f4f8; border-radius:16px; overflow:hidden; border:1px solid #e7eaf3; min-height:300px; display:flex; align-items:center; justify-content:center;">
<div style="text-align:center; padding:40px;">
<i class="fa fa-camera" style="font-size:48px; color:#b0c4d8; margin-bottom:16px; display:block;"></i>
<p style="font-size:14px; color:#8899aa; font-weight:600; margin:0;">${label}</p>
<p style="font-size:11px; color:#aab8c5; margin:4px 0 0;">${file}</p>
</div>
</div>`;

const H2C = (pre, accent, post, center = true) => `<h2 style="font-size:clamp(28px,3.2vw,38px); font-weight:800; color:#111; ${center ? 'text-align:center;' : ''} margin-bottom:10px; text-transform:uppercase;">${pre}<span style="color:#028ece;">${accent}</span>${post}</h2>`;
const INTRO = (t) => `<p style="font-size:16px; color:#555; line-height:1.8; max-width:800px; margin:0 auto 36px; text-align:center;">${t}</p>`;

const checkChips = (items, color = '#1565C0', bg = '#f8f9fc') => items.map(t => `<div style="display:flex; align-items:center; gap:12px; padding:14px 18px; background:${bg}; border-radius:10px;"><i class="fa fa-check-circle" style="color:${color}; font-size:16px;"></i><span style="font-size:14px; color:#333;">${t}</span></div>`).join('\n');

const cardIcon = (icon, title, desc) => `<div style="background:#fff; border:1px solid #e5e7eb; border-radius:12px; padding:22px; display:flex; align-items:flex-start; gap:14px;">
<div style="width:40px; height:40px; background:#e8f0fe; border-radius:10px; display:flex; align-items:center; justify-content:center; flex-shrink:0;"><i class="fa ${icon}" style="color:#1565C0; font-size:16px;"></i></div>
<div><h3 style="font-size:15px; font-weight:700; color:#111; margin-bottom:6px;">${title}</h3><p style="font-size:13px; color:#666; margin:0; line-height:1.6;">${desc}</p></div></div>`;

const flowPills = (steps) => steps.map((s, i) => {
  const colors = ['#e8f0fe|#1565C0', '#e6f7ed|#22c55e', '#fef3c7|#f59e0b', '#fce7f3|#ec4899', '#ede9fe|#8b5cf6', '#e0f2fe|#0ea5e9', '#ffedd5|#f97316'];
  const [bg, fg] = colors[i % colors.length].split('|');
  const arrow = i < steps.length - 1 ? `<div style="display:flex; align-items:center; color:#028ece;"><i class="fa fa-arrow-right"></i></div>` : '';
  return `<div style="padding:14px 22px; background:${bg}; border-radius:10px; font-size:14px; font-weight:600; color:${fg}; white-space:nowrap;">${s}</div>${arrow ? '\n' + arrow : ''}`;
}).join('\n');

const flowSection = (bg, pre, accent, post, intro, steps, extra = '') => `<section style="padding:60px 24px; background:${bg};">
<div style="max-width:1200px; margin:0 auto;">
${H2C(pre, accent, post)}
${INTRO(intro)}
<div style="display:flex; justify-content:center; gap:12px; flex-wrap:wrap; max-width:1100px; margin:0 auto;">
${flowPills(steps)}
</div>${extra}
</div>
</section>`;

const chipsSection = (bg, pre, accent, post, intro, chips) => `<section style="padding:60px 24px; background:${bg};">
<div style="max-width:1200px; margin:0 auto;">
${H2C(pre, accent, post)}
${INTRO(intro)}
<div style="display:flex; flex-wrap:wrap; justify-content:center; gap:16px; max-width:1000px; margin:0 auto;">
${checkChips(chips)}
</div>
</div>
</section>`;

const gridSection = (bg, pre, accent, post, intro, cards) => `<section style="padding:60px 24px; background:${bg};">
<div style="max-width:1200px; margin:0 auto;">
${H2C(pre, accent, post)}
${INTRO(intro)}
<div style="display:grid; grid-template-columns:repeat(4,1fr); gap:16px; max-width:1150px; margin:0 auto;" class="nf-grid">
${cards.map(c => cardIcon(c[0], c[1], c[2])).join('\n')}
</div>
</div>
</section>`;

const splitSection = (bg, side, pre, accent, post, para, bodyHtml, imgLabel, imgFile, extraPara = '') => `<section style="padding:60px 24px; background:${bg};">
<div style="max-width:1200px; margin:0 auto; display:grid; grid-template-columns:1fr 1fr; gap:40px; align-items:center;" class="nf-split">
${side === 'left' ? `<div>
${H2C(pre, accent, post, false)}
<p style="font-size:15px; color:#555; line-height:1.8; margin-bottom:20px;">${para}</p>
${extraPara ? `<p style="font-size:15px; color:#555; line-height:1.8; margin-bottom:20px;">${extraPara}</p>` : ''}
${bodyHtml}
</div>
${IMG(imgLabel, imgFile)}` : `${IMG(imgLabel, imgFile)}
<div>
${H2C(pre, accent, post, false)}
<p style="font-size:15px; color:#555; line-height:1.8; margin-bottom:20px;">${para}</p>
${extraPara ? `<p style="font-size:15px; color:#555; line-height:1.8; margin-bottom:20px;">${extraPara}</p>` : ''}
${bodyHtml}
</div>`}
</div>
</section>`;

const chipsWrap = (items, color = '#1565C0', bg = '#f8f9fc') => `<div style="display:grid; grid-template-columns:1fr 1fr; gap:14px;" class="nf-two">${checkChips(items, color, bg)}</div>`;
const cardsGrid = (cards) => `<div style="display:grid; grid-template-columns:repeat(2,1fr); gap:16px;" class="nf-two">${cards.map(c => cardIcon(c[0], c[1], c[2])).join('\n')}</div>`;

const logoChips = (names) => names.map(n => `<div style="padding:16px 22px; background:#fff; border:1px solid #e5e7eb; border-radius:12px; box-shadow:0 2px 8px rgba(0,0,0,.04); font-size:14px; font-weight:700; color:#1a1a2e; white-space:nowrap;">${n}</div>`).join('\n');

const faqSection = (faqs) => `<section style="padding:60px 24px; background:#fff;">
<div style="max-width:800px; margin:0 auto;">
<h2 style="font-size:32px; font-weight:800; color:#111; text-align:center; margin-bottom:36px;">Frequently Asked Questions</h2>
<div style="display:grid; grid-template-columns:repeat(2,1fr); gap:16px; max-width:1100px; margin:0 auto;" class="nf-two">
${faqs.map(f => `<details class="sm-faq-item"><summary>${f[0]}</summary><p>${f[1]}</p></details>`).join('\n')}
</div>
</div>
</section>`;

const ctaSection = (title, sub) => `<section style="padding:60px 24px; background:linear-gradient(135deg,#028ece,#017ab5);">
<div style="max-width:800px; margin:0 auto; text-align:center;">
<h2 style="font-size:28px; font-weight:800; color:#fff; margin-bottom:16px;">${title}</h2>
<p style="font-size:16px; color:rgba(255,255,255,.85); line-height:1.8; margin-bottom:30px;">${sub}</p>
<button class="open-modal-btn" style="display:inline-flex; align-items:center; gap:8px; padding:14px 32px; border-radius:50px; font-weight:700; font-size:14px; cursor:pointer; border:none; background:#f26522; color:#fff; font-family:'Poppins',sans-serif; letter-spacing:.5px;">Get Your Free Demo <i class="fa fa-arrow-up" style="font-size:12px;"></i></button>
</div>
</section>`;

const heroSection = (eyebrow, h1pre, h1accent, h1post, sub) => `<section style="padding:20px 24px 40px; background:linear-gradient(135deg,#f0f7ff 0%,#e8f4fd 50%,#f5f0ff 100%);" class="nf-hero">
<div style="max-width:1200px; margin:0 auto; display:grid; grid-template-columns:1fr 1fr; gap:60px; align-items:center;" class="nf-hero-grid">
<div>
<div style="display:inline-flex; align-items:center; gap:8px; font-size:13px; font-weight:700; color:#028ece; text-transform:uppercase; letter-spacing:1px; margin-bottom:16px;"><span style="width:10px; height:10px; border-radius:50%; background:#ff4f0d;"></span>${eyebrow}</div>
<h1 style="font-size:clamp(32px,4vw,44px); font-weight:800; line-height:1.15; margin:0 0 16px; text-transform:uppercase;">${h1pre}<span style="color:#028ece;">${h1accent}</span>${h1post}</h1>
<p style="color:#6b7589; font-size:16px; line-height:1.7; max-width:480px; margin-bottom:26px;">${sub}</p>
<div style="display:flex; gap:14px; flex-wrap:wrap;">
<button class="mm-btn mm-btn-orange open-modal-btn">Get Your Free Demo <i class="fa fa-arrow-up"></i></button>
</div>
</div>
</div>
</section>`;

const head = (p) => `<!DOCTYPE html>
<html lang="en">
<head>
<script type="text/javascript">(function(c,l,a,r,i,t,y){c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);})(window, document, "clarity", "script", "n95oax955q");</script>
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer','GTM-KPCRHTFH');</script>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>${p.title}</title>
<meta name="description" content="${p.meta}">
<meta name="keywords" content="${p.keywords}">
<meta property="og:type" content="website">
<meta property="og:title" content="${p.title}">
<meta property="og:description" content="${p.meta}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="icon" type="image/x-icon" href="../assets/gymex-favicon-U7mChGv0.ico">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css">
<link rel="stylesheet" href="../style.css">
<link rel="stylesheet" href="../new-feature-common.css?v=2">
<script src="../javascript.js"></script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
${p.faqs.slice(0, 3).map(f => `    { "@type": "Question", "name": "${f[0].replace(/"/g, '\\"')}", "acceptedAnswer": { "@type": "Answer", "text": "${f[1].replace(/"/g, '\\"')}" } }`).join(',\n')}
  ]
}
</script>
</head>
<body>

`;

// ═══════════ PAGE DEFINITIONS ═══════════

const pages = [];

// ── 1. WORKOUT & DIET PLANNER ──
pages.push({
  dir: 'workout-diet', file: 'workout-diet-planner.html',
  title: 'Gym Workout & Diet Plan Software | Gymex',
  meta: 'Create personalized workout and diet plans for gym members with Gymex. Track body measurements, monitor progress, generate reports, and share plans via WhatsApp.',
  keywords: 'Gym Workout Plan Software, Gym Diet Plan Software, Gym Body Measurement Tracking, Gym Member Progress Tracking',
  build: () => [
    heroSection('Gym Workout & Diet Plan Software', 'Create Personalized ', 'Workout &amp; Diet Plans', ' for Your Members',
      'Make fitness planning more organized with Gymex. Create custom workout and diet plans, track body measurements and member progress, and share individual plans directly with members through WhatsApp.'),
    // Two planners
    `<section style="padding:60px 24px; background:#fff;">
<div style="max-width:1200px; margin:0 auto;">
${H2C('Two Planners. ', 'One Connected Member Experience', '')}
${INTRO('Managing workout routines and diet plans separately can make it harder for trainers to keep member fitness information organized. Gymex brings both together.')}
<div style="display:grid; grid-template-columns:1fr 1fr; gap:20px; max-width:900px; margin:0 auto;" class="nf-two">
<div style="background:#f8f9fc; border:1px solid #e5e7eb; border-radius:16px; padding:30px; text-align:center;"><div style="width:56px; height:56px; background:#e8f0fe; border-radius:14px; display:flex; align-items:center; justify-content:center; margin:0 auto 16px;"><i class="fa fa-dumbbell" style="color:#1565C0; font-size:22px;"></i></div><h3 style="font-size:18px; font-weight:800; color:#111; margin-bottom:10px; text-transform:uppercase;">Workout Planner</h3><p style="font-size:14px; color:#555; line-height:1.7; margin:0;">Build structured workout plans. Create exercises and custom workout plans for individual members while keeping their fitness progress connected to their records.</p></div>
<div style="background:#f8f9fc; border:1px solid #e5e7eb; border-radius:16px; padding:30px; text-align:center;"><div style="width:56px; height:56px; background:#e6f7ed; border-radius:14px; display:flex; align-items:center; justify-content:center; margin:0 auto 16px;"><i class="fa fa-apple-alt" style="color:#22c55e; font-size:22px;"></i></div><h3 style="font-size:18px; font-weight:800; color:#111; margin-bottom:10px; text-transform:uppercase;">Diet Planner</h3><p style="font-size:14px; color:#555; line-height:1.7; margin:0;">Plan around individual fitness goals. Create diet templates and customized diet plans based on different dietary needs, health requirements, and fitness goals.</p></div>
</div>
</div>
</section>`,
    splitSection('#f8f9fc', 'left', 'Create Custom ', 'Workout Plans', ' for Every Member',
      'Every member can have different fitness requirements. Instead of relying on the same routine for everyone, Gymex Gym Workout Plan helps your team create and manage custom workout plans for individual members.',
      chipsWrap(['Create a variety of exercises', 'Build custom workout plans', 'Individual plans for members', 'Keep workout information organized', 'Monitor member workout progress', 'Workout records in one connected system']),
      'Workout Planner Screenshot', 'gym-workout-plan-software-gymex.webp'),
    splitSection('#fff', 'right', 'Create Diet Plans for ', 'Different Goals', ' &amp; Dietary Needs',
      'A structured fitness journey isn\u2019t limited to workouts. Gymex Gym Diet Plan allows your team to create diet templates for different dietary needs and customize individual plans based on a member\u2019s health and fitness goals.',
      chipsWrap(['Create diet plan templates', 'Build customized diet plans', 'Plan for different dietary needs', 'Goal-based diet plans', 'Assign diet plans to members', 'Diet plan information in one place'], '#22c55e', '#f0fdf4'),
      'Diet Plan Screenshot', 'gym-diet-plan-software-gymex.webp'),
    splitSection('#f8f9fc', 'left', 'Track More Than a Plan \u2014 ', 'Body Measurements', ' &amp; BMI',
      'A workout plan becomes more useful when trainers can see how a member is progressing over time. Gymex helps your team capture and monitor member body measurements, including BMI, alongside workout planning.',
      chipsWrap(['BMI tracking', 'Body measurements', 'Member progress records', 'Measurement history']),
      'Body Measurements Screenshot', 'gym-body-measurements-bmi-gymex.webp'),
    splitSection('#fff', 'right', 'Turn Member Progress into ', 'Clear Reports', '',
      'Creating a plan is only the beginning. Trainers also need a way to understand how members are progressing. Gymex helps you track and generate detailed workout and diet reports.',
      cardsGrid([['fa-chart-line', 'Workout Progress', 'Review workout information and use detailed reports to assess how members are progressing.'],
        ['fa-utensils', 'Diet Progress', 'Track member diet progress through reports and keep diet information organized.'],
        ['fa-ruler', 'Body Measurements', 'Use recorded measurements and BMI alongside progress records for a connected view.'],
        ['fa-sync', 'Plan \u2192 Improve', 'Plan, monitor, review and improve each member\u2019s fitness journey.']]),
      'Progress Report Screenshot', 'gym-workout-progress-report-gymex.webp'),
    flowSection('#f8f9fc', 'A Simple ', 'Workflow', ' for Trainers',
      'Gymex keeps the workout and diet planning process simple and connected \u2014 from creating a plan to tracking progress.',
      ['Create Exercises', 'Build Workout Plan', 'Assign to Member', 'Track Measurements', 'Review Progress']),
    splitSection('#fff', 'right', 'Share Individual Plans Directly Through ', 'WhatsApp', '',
      'Once a workout or diet plan is ready, getting it to the member shouldn\u2019t create additional work. Gymex allows your team to send individual workout and diet plans to members through WhatsApp.',
      chipsWrap(['Send workout plans via WhatsApp', 'Share diet plans directly', 'Member receives plan instantly', 'No extra manual work'], '#22c55e', '#f0fdf4', ),
      'WhatsApp Plan Sharing Screenshot', 'gym-whatsapp-plan-sharing-gymex.webp'),
    gridSection('#f8f9fc', 'Why Choose Gymex ', 'Workout & Diet Planner', '?',
      'Everything your trainers need to plan, track and share member fitness journeys \u2014 in one connected system.',
      [['fa-dumbbell', 'Custom Workout Plans', 'Create individual workout plans based on member requirements.'],
        ['fa-list-ol', 'Exercise Planning', 'Create a variety of exercises and organize them into workout plans.'],
        ['fa-apple-alt', 'Personalized Diet Plans', 'Create customized diet plans around different member goals.'],
        ['fa-clone', 'Diet Templates', 'Build diet templates for different dietary needs.'],
        ['fa-ruler', 'Body Measurements & BMI', 'Capture and monitor member measurements, including BMI.'],
        ['fa-chart-line', 'Workout Progress Reports', 'Generate detailed workout reports to assess member progress.'],
        ['fa-utensils', 'Diet Progress Tracking', 'Monitor member diet progress through organized reports.'],
        ['fa-brands fa-whatsapp', 'WhatsApp Plan Sharing', 'Send individual plans directly to members through WhatsApp.']]),
    faqSection([
      ['What is gym workout plan software?', 'Gym workout plan software helps fitness businesses create and manage structured workout plans for members. With Gymex, trainers can create exercises, build custom workout plans, monitor body measurements and BMI, and use workout reports to review member progress.'],
      ['Can I create custom workout plans for individual members?', 'Yes. Gymex allows your team to create custom workout plans for individual members, making it easier to organize workouts according to different member requirements.'],
      ['Can Gymex create customized diet plans?', 'Yes. Gymex allows you to create diet templates for different dietary needs and customize individual diet plans based on a member\u2019s health and fitness goals.'],
      ['Can I track member body measurements?', 'Yes. Gymex allows your team to capture and monitor member body measurements, including BMI, helping trainers maintain progress information alongside workout planning.'],
      ['Can trainers track workout and diet progress?', 'Yes. Gymex provides workout reports that help assess member progress and also allows your team to track diet progress through reports.'],
      ['Can workout and diet plans be shared through WhatsApp?', 'Yes. Individual workout and diet plans created in Gymex can be sent to members through WhatsApp, making it convenient to share their plans directly with them.'],
    ]),
    ctaSection('Make Workout & Diet Planning Easier for Your Team', 'Create personalized workout and diet plans, monitor member measurements, track progress, and keep fitness planning organized with Gymex.'),
  ],
  faqs: [['What is gym workout plan software?', 'Gym workout plan software helps fitness businesses create and manage structured workout plans for members.'], ['Can I create custom workout plans for individual members?', 'Yes. Gymex allows your team to create custom workout plans for individual members.'], ['Can workout and diet plans be shared through WhatsApp?', 'Yes. Individual workout and diet plans created in Gymex can be sent to members through WhatsApp.']]
});

// ── 2. POS & LOCKER MANAGEMENT ──
pages.push({
  dir: 'pos-locker', file: 'pos-locker-management.html',
  title: 'Gym POS & Locker Management Software | Gymex',
  meta: 'Manage gym POS sales, merchandise, stock details, lockers, and spaces with Gymex. Create POS bills, track collections, allocate lockers, and monitor utilization.',
  keywords: 'Gym POS Software, Gym Point of Sale Software, Gym Locker Management Software, Gym Inventory Management Software',
  build: () => [
    heroSection('Gym POS & Locker Management Software', 'Simplify Gym ', 'Sales, Merchandise', ' &amp; Locker Management',
      'Manage POS products, merchandise, billing, stock details, and lockers from one connected platform. Gymex helps simplify front-desk sales while keeping product information and member space allocation organized.'),
    // 3 pillars
    `<section style="padding:60px 24px; background:#fff;">
<div style="max-width:1200px; margin:0 auto;">
${H2C('POS, Stocks & Lockers \u2014 ', 'Connected in One System', '')}
${INTRO('Running a gym involves more than memberships. Gymex brings front-desk sales, merchandise, stock and lockers together in one system.')}
<div style="display:grid; grid-template-columns:repeat(3,1fr); gap:20px; max-width:1050px; margin:0 auto;" class="nf-three">
<div style="background:#f8f9fc; border:1px solid #e5e7eb; border-radius:16px; padding:28px; text-align:center;"><div style="width:52px; height:52px; background:#e8f0fe; border-radius:14px; display:flex; align-items:center; justify-content:center; margin:0 auto 14px;"><i class="fa fa-calculator" style="color:#1565C0; font-size:20px;"></i></div><h3 style="font-size:16px; font-weight:800; color:#111; margin-bottom:8px; text-transform:uppercase;">POS Management</h3><p style="font-size:13px; color:#555; line-height:1.7; margin:0;">Create products, generate POS bills, print receipts, manage merchandise, and review product-wise collections.</p></div>
<div style="background:#f8f9fc; border:1px solid #e5e7eb; border-radius:16px; padding:28px; text-align:center;"><div style="width:52px; height:52px; background:#fef3c7; border-radius:14px; display:flex; align-items:center; justify-content:center; margin:0 auto 14px;"><i class="fa fa-boxes" style="color:#f59e0b; font-size:20px;"></i></div><h3 style="font-size:16px; font-weight:800; color:#111; margin-bottom:8px; text-transform:uppercase;">Merchandise & Stock</h3><p style="font-size:13px; color:#555; line-height:1.7; margin:0;">Capture gym merchandise and maintain stock inventory details alongside your POS operations.</p></div>
<div style="background:#f8f9fc; border:1px solid #e5e7eb; border-radius:16px; padding:28px; text-align:center;"><div style="width:52px; height:52px; background:#e6f7ed; border-radius:14px; display:flex; align-items:center; justify-content:center; margin:0 auto 14px;"><i class="fa fa-door-closed" style="color:#22c55e; font-size:20px;"></i></div><h3 style="font-size:16px; font-weight:800; color:#111; margin-bottom:8px; text-transform:uppercase;">Locker & Space</h3><p style="font-size:13px; color:#555; line-height:1.7; margin:0;">Maintain locker and space details, sell lockers to members, manage allocations through a calendar, and review utilization.</p></div>
</div>
</div>
</section>`,
    splitSection('#f8f9fc', 'left', 'Manage Everyday Gym Sales with a ', 'Smarter POS', '',
      'Gyms often sell more than memberships. Gymex Gym POS Software allows your team to create multiple POS products and manage product-related sales through one connected system.',
      chipsWrap(['Create multiple POS products', 'Manage POS product information', 'Capture gym merchandise', 'Create POS bills', 'Maintain organized transaction records', 'Keep product sales connected']),
      'POS Billing Screenshot', 'gym-pos-software-gymex.webp'),
    flowSection('#fff', 'Keep Every ', 'POS Transaction', ' Organized',
      'A clear billing process makes it easier for your team to manage product sales and maintain transaction records.',
      ['Product Selected', 'POS Bill Created', 'Transaction Recorded', 'Receipt Printed']),
    splitSection('#f8f9fc', 'right', 'Keep Gym Merchandise & ', 'Stock Details', ' Organized',
      'When your gym sells products or merchandise, keeping product and stock information organized makes everyday front-desk operations easier.',
      chipsWrap(['Capture gym merchandise', 'Maintain product information', 'View stock inventory details', 'Keep merchandise records organized', 'Manage products alongside POS'], '#f59e0b', '#fef9ec'),
      'Merchandise & Stock Screenshot', 'gym-merchandise-stock-inventory-gymex.webp'),
    splitSection('#fff', 'left', 'Track ', 'Product-Wise Collections', '',
      'Knowing how individual products are contributing to collections gives you better visibility into your POS activity. Gymex provides a Product-wise Collection Report.',
      chipsWrap(['Review product-wise collections', 'Understand collections across products', 'Keep product sales organized', 'Clearer visibility into POS activity']),
      'Product-Wise Collection Report', 'gym-product-wise-collection-report-gymex.webp'),
    splitSection('#f8f9fc', 'right', 'Manage Gym Lockers with Clear ', 'Availability & Status', '',
      'Gymex Gym Locker Management gives your team a clear visual view of locker availability and status, making it easier to manage lockers from one organized system.',
      chipsWrap(['View total lockers at a glance', 'Check available & occupied lockers', 'Track out-of-service lockers', 'View lockers marked not vacant', 'One-screen locker status'], '#22c55e', '#f0fdf4'),
      'Locker Status Screenshot', 'gym-locker-management-software-gymex.webp'),
    splitSection('#fff', 'left', 'Sell & Allocate ', 'Lockers to Members', '',
      'Gymex allows your team to sell lockers to members and maintain their allocation information within the system, creating a structured process for managing member lockers.',
      `<div style="display:flex; justify-content:flex-start; gap:10px; flex-wrap:wrap; margin-bottom:20px;">${flowPills(['Select Locker', 'Allocate to Member', 'Maintain Details', 'Track Utilization'])}</div>`,
      'Locker Allocation Screenshot', 'gym-locker-allocation-gymex.webp'),
    gridSection('#f8f9fc', 'Why Choose Gymex ', 'POS & Locker Management', '?',
      'From front-desk sales to locker allocation \u2014 everything organized in one connected system.',
      [['fa-calculator', 'Multiple POS Products', 'Create and manage multiple products through the Gymex POS module.'],
        ['fa-file-invoice-dollar', 'POS Billing', 'Create POS bills for products sold through your gym.'],
        ['fa-print', 'Printed POS Receipts', 'Generate and print POS-based receipts for product transactions.'],
        ['fa-boxes', 'Merchandise & Stock', 'Capture gym merchandise and maintain stock inventory details.'],
        ['fa-chart-bar', 'Product-Wise Reports', 'Review product-wise collections and get better visibility.'],
        ['fa-door-open', 'Locker Status Visibility', 'Quickly understand locker status from one organized view.'],
        ['fa-th', 'Visual Locker Management', 'Manage multiple lockers through a clear visual interface.'],
        ['fa-user-check', 'Locker Allocation', 'Keep member locker allocations organized and easy to manage.']]),
    faqSection([
      ['What is gym POS software?', 'Gym POS software helps fitness businesses manage product sales and related transactions from the front desk. Gymex allows you to create multiple POS products, generate POS bills, print receipts, capture gym merchandise, maintain stock inventory details, and review product-wise collection reports.'],
      ['Can I manage gym merchandise with Gymex POS?', 'Yes. Gymex allows you to capture gym merchandise and maintain related stock inventory details within the POS management process.'],
      ['Does Gymex provide inventory management with POS?', 'Gymex allows you to maintain stock inventory details alongside POS products and merchandise, keeping product and inventory information organized within your gym management system.'],
      ['Can Gymex generate POS receipts?', 'Yes. Gymex allows your team to create POS bills and print POS-based receipts for product transactions.'],
      ['What is gym locker management software?', 'Gym locker management software helps fitness businesses maintain locker information and organize member locker allocations. Gymex allows your team to maintain locker and space details, sell lockers to members, manage allocations, and review utilization reports.'],
      ['Can lockers be allocated to gym members?', 'Yes. Gymex allows your team to sell lockers to members and maintain their locker allocation information within the system.'],
    ]),
    ctaSection('Simplify POS & Locker Management with Gymex', 'Manage product sales, POS billing, merchandise, stock details, and locker allocations from one connected gym management platform.'),
  ],
  faqs: [['What is gym POS software?', 'Gym POS software helps fitness businesses manage product sales and related transactions from the front desk.'], ['Can Gymex generate POS receipts?', 'Yes. Gymex allows your team to create POS bills and print POS-based receipts for product transactions.'], ['Can lockers be allocated to gym members?', 'Yes. Gymex allows your team to sell lockers to members and maintain their allocation information.']]
});

// ── 3. MOBILE APPS ──
pages.push({
  dir: 'mobile-apps', file: 'mobile-apps.html',
  title: 'Gym Management App for Members & Admins | Gymex',
  meta: 'Manage your gym on the go with Gymex mobile apps. Give members access to classes, appointments, workouts and memberships while admins track key business activities.',
  keywords: 'Gym Management App, Gym Member App, Gym Admin App, Gym Class Booking App, Gym Attendance App',
  build: () => [
    heroSection('Gym Management Mobile App', 'Your Gym, ', 'Connected Wherever You Go', '',
      'Bring members, admins, and prospects closer to your gym operations with dedicated Gymex mobile apps \u2014 built to make everyday activities easier from anywhere.'),
    // Three apps
    `<section style="padding:60px 24px; background:#fff;">
<div style="max-width:1200px; margin:0 auto;">
${H2C('Three Apps. Three Experiences. ', 'One Gymex.', '')}
${INTRO('Gymex doesn\u2019t have just one generic app \u2014 members, admins and prospects each get an experience built for them.')}
<div style="display:grid; grid-template-columns:repeat(3,1fr); gap:20px; max-width:1050px; margin:0 auto;" class="nf-three">
<div style="background:#f8f9fc; border:1px solid #e5e7eb; border-radius:16px; padding:28px; text-align:center;"><div style="width:120px; height:200px; margin:0 auto 18px; background:#fff; border:3px solid #1a1a2e; border-radius:22px; display:flex; align-items:center; justify-content:center;"><i class="fa fa-mobile-screen-button" style="font-size:44px; color:#028ece;"></i></div><h3 style="font-size:16px; font-weight:800; color:#111; margin-bottom:8px; text-transform:uppercase;">Member App</h3><p style="font-size:13px; color:#555; line-height:1.7; margin-bottom:12px;">Everything members need, right in their pocket.</p><div style="display:flex; flex-wrap:wrap; gap:6px; justify-content:center;"><span style="font-size:11px; font-weight:600; background:#e8f0fe; color:#1565C0; padding:5px 10px; border-radius:20px;">Bookings</span><span style="font-size:11px; font-weight:600; background:#e8f0fe; color:#1565C0; padding:5px 10px; border-radius:20px;">Membership</span><span style="font-size:11px; font-weight:600; background:#e8f0fe; color:#1565C0; padding:5px 10px; border-radius:20px;">Workouts</span><span style="font-size:11px; font-weight:600; background:#e8f0fe; color:#1565C0; padding:5px 10px; border-radius:20px;">Attendance</span></div></div>
<div style="background:#f8f9fc; border:1px solid #e5e7eb; border-radius:16px; padding:28px; text-align:center;"><div style="width:120px; height:200px; margin:0 auto 18px; background:#fff; border:3px solid #1a1a2e; border-radius:22px; display:flex; align-items:center; justify-content:center;"><i class="fa fa-chart-pie" style="font-size:44px; color:#f26522;"></i></div><h3 style="font-size:16px; font-weight:800; color:#111; margin-bottom:8px; text-transform:uppercase;">Admin App</h3><p style="font-size:13px; color:#555; line-height:1.7; margin-bottom:12px;">Your gym business, wherever you are.</p><div style="display:flex; flex-wrap:wrap; gap:6px; justify-content:center;"><span style="font-size:11px; font-weight:600; background:#ffedd5; color:#c2410c; padding:5px 10px; border-radius:20px;">Dashboard</span><span style="font-size:11px; font-weight:600; background:#ffedd5; color:#c2410c; padding:5px 10px; border-radius:20px;">Collections</span><span style="font-size:11px; font-weight:600; background:#ffedd5; color:#c2410c; padding:5px 10px; border-radius:20px;">Sales</span><span style="font-size:11px; font-weight:600; background:#ffedd5; color:#c2410c; padding:5px 10px; border-radius:20px;">Expenses</span></div></div>
<div style="background:#f8f9fc; border:1px solid #e5e7eb; border-radius:16px; padding:28px; text-align:center;"><div style="width:200px; height:140px; margin:30px auto 26px; background:#fff; border:3px solid #1a1a2e; border-radius:16px; display:flex; align-items:center; justify-content:center;"><i class="fa fa-tablet-screen-button" style="font-size:44px; color:#22c55e;"></i></div><h3 style="font-size:16px; font-weight:800; color:#111; margin-bottom:8px; text-transform:uppercase;">Prospect App</h3><p style="font-size:13px; color:#555; line-height:1.7; margin-bottom:12px;">Capture opportunities while you\u2019re on the move.</p><div style="display:flex; flex-wrap:wrap; gap:6px; justify-content:center;"><span style="font-size:11px; font-weight:600; background:#f0fdf4; color:#15803d; padding:5px 10px; border-radius:20px;">Prospects</span><span style="font-size:11px; font-weight:600; background:#f0fdf4; color:#15803d; padding:5px 10px; border-radius:20px;">Referrals</span><span style="font-size:11px; font-weight:600; background:#f0fdf4; color:#15803d; padding:5px 10px; border-radius:20px;">E-Signature</span></div></div>
</div>
</div>
</section>`,
    splitSection('#f8f9fc', 'left', 'Member App \u2014 Everything Members Need, ', 'Right in Their Pocket', '',
      'From booking a class to checking attendance and accessing workouts, the Gymex Gym Member App puts everyday gym activities within easy reach.',
      cardsGrid([['fa-calendar-check', 'Bookings', 'Classes & appointments'],
        ['fa-dumbbell', 'Fitness', 'Workout videos & diet plans'],
        ['fa-id-card', 'Membership', 'Membership details & forms'],
        ['fa-chart-line', 'Progress', 'Body measurements & attendance history'],
        ['fa-gift', 'Engagement', 'Referrals & loyalty rewards'],
        ['fa-qrcode', 'Check-In', 'QR attendance & live floor count']]),
      'Member App Screenshot', 'gym-member-app-gymex.webp'),
    flowSection('#fff', 'A Day with the ', 'Gymex Member App', '',
      'One app that stays connected throughout the member journey.',
      ['BOOK', 'CHECK IN', 'TRAIN', 'TRACK', 'ENGAGE']),
    splitSection('#f8f9fc', 'right', 'Admin App \u2014 Run Your Gym from More Than Just the ', 'Front Desk', '',
      'Stay connected to important business information through the Gymex Admin App. Monitor everyday gym activity and performance wherever you are.',
      cardsGrid([['fa-money-bill', 'Collections', 'View collection overview'],
        ['fa-bullseye', 'Sales', 'Targets vs achievement'],
        ['fa-user-check', 'Attendance', 'Monitor attendance activity'],
        ['fa-credit-card', 'Payments', 'Bills & payment overview'],
        ['fa-phone', 'Follow-Ups', 'Check follow-up call status'],
        ['fa-file-invoice-dollar', 'Expenses', 'Review expenses & income vs expense']]),
      'Admin App Screenshot', 'gym-admin-app-gymex.webp'),
    splitSection('#fff', 'left', 'Prospect App \u2014 Turn Every Prospect Interaction into an ', 'Organized Digital Experience', '',
      'Capture and manage prospect information while interacting with potential members using the Gymex Prospect App \u2014 tablet compatible.',
      chipsWrap(['Capture Prospects', 'Digital Signature', 'Referrals', 'Profiles', 'Profile Images', 'Tablet Compatible'], '#22c55e', '#f0fdf4'),
      'Prospect App Screenshot', 'gym-prospect-app-gymex.webp'),
    // comparison table
    `<section style="padding:60px 24px; background:#f8f9fc;">
<div style="max-width:900px; margin:0 auto;">
${H2C('Which App ', 'Does What', '?')}
${INTRO('A quick comparison so you know exactly which app does what.')}
<div style="background:#fff; border:1px solid #e5e7eb; border-radius:16px; overflow:hidden; box-shadow:0 2px 12px rgba(0,0,0,.05);" class="nf-tablewrap">
<table style="width:100%; border-collapse:collapse; font-size:14px;" class="nf-table">
<thead><tr style="background:#1a1a2e; color:#fff;">${['Capability', 'Member App', 'Admin App', 'Prospect App'].map(h => `<th style="padding:14px 16px; text-align:left; font-weight:700;">${h}</th>`).join('')}</tr></thead>
<tbody>
${[['Class & Appointment Booking', '1', '0', '0'], ['Workout & Diet Access', '1', '0', '0'], ['QR Attendance', '1', '0', '0'], ['Membership Details', '1', '0', '0'], ['Business Dashboard', '0', '1', '0'], ['Collections & Payments', '0', '1', '0'], ['Sales Performance', '0', '1', '0'], ['Expense Overview', '0', '1', '0'], ['Capture Prospects', '0', '0', '1'], ['Digital Signatures', '0', '0', '1'], ['Prospect Profiles', '0', '0', '1']].map((r, i) => `<tr style="background:${i % 2 ? '#f8f9fc' : '#fff'}; border-top:1px solid #eef1f5;"><td style="padding:12px 16px; font-weight:600; color:#111;">${r[0]}</td>${[1, 2, 3].map(c => `<td style="padding:12px 16px;">${r[c] === '1' ? '<i class="fa fa-check-circle" style="color:#22c55e;"></i>' : '<span style="color:#cbd5e1;">\u2014</span>'}</td>`).join('')}</tr>`).join('\n')}
</tbody>
</table>
</div>
</div>
</section>`,
    faqSection([
      ['Does Gymex provide a mobile app for gym members?', 'Yes. The Gymex Member App allows members to access features such as classes, appointments, membership details, attendance history, workout videos, diet plans, trainer profiles, body measurements, referrals, loyalty points, and QR attendance.'],
      ['Can members book classes through the Gymex app?', 'Yes. Members can view relevant classes and make class bookings through the Gymex Member App. They can also view and create appointments.'],
      ['Can members mark attendance from the mobile app?', 'Yes. Gymex supports QR code scanning attendance check-in through the Member App. Members can also view their attendance history.'],
      ['Does Gymex have an app for gym admins?', 'Yes. The Gymex Admin App gives owners and admins access to important information such as the dashboard, collections, sales targets, attendance, bills and payments, follow-up calls, approvals, expenses, and income vs expense details.'],
      ['Can Gymex help manage prospects from mobile?', 'Yes. The Prospect App allows your team to capture prospect details and referrals, manage prospect information, capture digital signatures and profile images, and access relevant profiles.'],
    ]),
    ctaSection('Take Your Gym Beyond the Front Desk', 'Give members convenient mobile access while keeping management connected to important gym activities with Gymex. Members. Management. Prospects. One Connected Mobile Experience.'),
  ],
  faqs: [['Does Gymex provide a mobile app for gym members?', 'Yes. The Gymex Member App allows members to access classes, appointments, membership details, workouts and QR attendance.'], ['Does Gymex have an app for gym admins?', 'Yes. The Gymex Admin App gives owners access to dashboard, collections, sales, attendance and expenses.'], ['Can members book classes through the Gymex app?', 'Yes. Members can view relevant classes and make class bookings through the Gymex Member App.']]
});

// ── 4. INTEGRATIONS ──
pages.push({
  dir: 'integrations', file: 'integrations.html',
  title: 'Gym Management Software Integrations | Gymex',
  meta: 'Connect Gymex with payment gateways, biometric systems, health platforms, calendars, Zoom, and more to keep your gym operations connected.',
  keywords: 'Gym Management Software Integrations, Gym Payment Integrations, Gym Biometric Integration, Gym Zoom Integration, Gym Calendar Integration',
  build: () => [
    heroSection('Gym Software Integrations', 'Connect Gymex with ', 'the Tools Your Business Uses', '',
      'Bring payments, access systems, health platforms, calendars, virtual sessions, and communication tools closer to your gym operations with Gymex integrations.'),
    chipsSection('#fff', 'One Platform. ', 'Multiple Connections', '.',
      'Your fitness business may rely on different tools for payments, attendance, member health data, scheduling, and communication. Gymex integrations help connect supported third-party platforms with your gym management system.',
      ['Payment Gateways', 'Attendance & Access (eSSL)', 'Health & Fitness (InBody, Apple Health+, EGYM)', 'Calendar & Virtual (Google Calendar, Zoom)', 'Communication (CallerDesk)']),
    // Payment grid
    `<section style="padding:60px 24px; background:#f8f9fc;">
<div style="max-width:1200px; margin:0 auto;">
${H2C('Simplify Payments with Multiple ', 'Payment Integrations', '')}
${INTRO('Connect Gymex with supported payment providers to make payment processing part of your gym management workflow.')}
<div style="display:flex; flex-wrap:wrap; justify-content:center; gap:14px; max-width:1000px; margin:0 auto;">
${logoChips(['PayPal', 'Stripe', 'MyFatoorah', 'HyperPay', 'PayTabs', 'Checkout.com', 'Telr', 'Razorpay', 'PayU', 'Tap Payment', 'Network International', 'Payfast'])}
</div>
</div>
</section>`,
    splitSection('#fff', 'left', 'Connect Attendance & Access with ', 'eSSL', '',
      'Gymex integrates with eSSL to support connected attendance and access-related operations within your gym management system. By connecting your supported biometric setup with Gymex, attendance information can remain closer to your overall member and staff management process.',
      `<div style="display:flex; justify-content:flex-start; gap:10px; flex-wrap:wrap; margin-bottom:20px;">${flowPills(['eSSL Device', 'Attendance', 'Gymex'])}</div>
<p style="font-size:14px; color:#555; line-height:1.8;">Want the complete attendance picture? Explore <a href="../biometric-access-control/biometric-access-control.html" style="color:#028ece; font-weight:600;">Gymex Biometric &amp; Access Control</a>.</p>`,
      'eSSL Integration Screenshot', 'gym-essl-biometric-integration-gymex.webp'),
    // Health cards
    `<section style="padding:60px 24px; background:#f8f9fc;">
<div style="max-width:1200px; margin:0 auto;">
${H2C('Connect Member ', 'Fitness & Health Data', '')}
${INTRO('Gymex connects with supported fitness and health platforms, helping create a more connected digital fitness experience.')}
<div style="display:grid; grid-template-columns:repeat(3,1fr); gap:20px; max-width:1000px; margin:0 auto;" class="nf-three">
<div style="background:#fff; border:1px solid #e5e7eb; border-radius:16px; padding:28px; text-align:center;"><div style="width:52px; height:52px; background:#e8f0fe; border-radius:14px; display:flex; align-items:center; justify-content:center; margin:0 auto 14px;"><i class="fa fa-heart-pulse" style="color:#1565C0; font-size:20px;"></i></div><h3 style="font-size:16px; font-weight:800; color:#111; margin-bottom:8px;">InBody</h3><p style="font-size:13px; color:#555; line-height:1.7; margin:0;">Connect supported body composition information with your fitness management process.</p></div>
<div style="background:#fff; border:1px solid #e5e7eb; border-radius:16px; padding:28px; text-align:center;"><div style="width:52px; height:52px; background:#f1f5f9; border-radius:14px; display:flex; align-items:center; justify-content:center; margin:0 auto 14px;"><i class="fa-brands fa-apple" style="color:#111; font-size:22px;"></i></div><h3 style="font-size:16px; font-weight:800; color:#111; margin-bottom:8px;">Apple Health+</h3><p style="font-size:13px; color:#555; line-height:1.7; margin:0;">Connect supported health and fitness information from the Apple ecosystem.</p></div>
<div style="background:#fff; border:1px solid #e5e7eb; border-radius:16px; padding:28px; text-align:center;"><div style="width:52px; height:52px; background:#e6f7ed; border-radius:14px; display:flex; align-items:center; justify-content:center; margin:0 auto 14px;"><i class="fa fa-dumbbell" style="color:#22c55e; font-size:20px;"></i></div><h3 style="font-size:16px; font-weight:800; color:#111; margin-bottom:8px;">EGYM</h3><p style="font-size:13px; color:#555; line-height:1.7; margin:0;">Extend your connected fitness ecosystem through supported EGYM integration.</p></div>
</div>
</div>
</section>`,
    // Calendar + Zoom
    `<section style="padding:60px 24px; background:#fff;">
<div style="max-width:1200px; margin:0 auto;">
${H2C('Connect Scheduling & ', 'Virtual Sessions', '')}
${INTRO('Gymex also connects with tools used for scheduling and virtual communication, helping fitness businesses keep online and offline activities better connected.')}
<div style="display:grid; grid-template-columns:1fr 1fr; gap:20px; max-width:760px; margin:0 auto;" class="nf-two">
<div style="background:#f8f9fc; border:1px solid #e5e7eb; border-radius:16px; padding:28px; display:flex; align-items:flex-start; gap:16px;"><div style="width:48px; height:48px; background:#e8f0fe; border-radius:12px; display:flex; align-items:center; justify-content:center; flex-shrink:0;"><i class="fa-brands fa-google" style="color:#1565C0; font-size:20px;"></i></div><div><h3 style="font-size:16px; font-weight:800; color:#111; margin-bottom:8px;">Google Calendar</h3><p style="font-size:13px; color:#555; line-height:1.7; margin:0;">Connect supported Gymex scheduling activities with Google Calendar for easier schedule visibility.</p></div></div>
<div style="background:#f8f9fc; border:1px solid #e5e7eb; border-radius:16px; padding:28px; display:flex; align-items:flex-start; gap:16px;"><div style="width:48px; height:48px; background:#e8f0fe; border-radius:12px; display:flex; align-items:center; justify-content:center; flex-shrink:0;"><i class="fa fa-video" style="color:#1565C0; font-size:20px;"></i></div><div><h3 style="font-size:16px; font-weight:800; color:#111; margin-bottom:8px;">Zoom</h3><p style="font-size:13px; color:#555; line-height:1.7; margin:0;">Connect virtual sessions with Zoom to support online fitness activities and appointments.</p></div></div>
</div>
</div>
</section>`,
    splitSection('#f8f9fc', 'right', 'Connect Gym Communication with ', 'CallerDesk', '',
      'Gymex supports integration with CallerDesk, helping connect supported calling and communication activities with your gym operations. This gives your team another way to keep member and prospect communication connected with the tools they use for everyday business activities.',
      chipsWrap(['Connected calling activities', 'Member & prospect communication', 'Everyday business tools', 'Centralized communication'], '#8b5cf6', '#f3f0ff'),
      'CallerDesk Integration Screenshot', 'gym-callerdesk-integration-gymex.webp'),
    gridSection('#fff', 'Explore ', 'Gymex Integrations', '',
      'A quick overview of everything Gymex can connect with.',
      [['fa-credit-card', 'Payment', 'PayPal, Stripe, MyFatoorah, HyperPay, PayTabs, Checkout.com, Telr & more'],
        ['fa-fingerprint', 'Attendance & Access', 'eSSL biometric attendance and access integration'],
        ['fa-heart-pulse', 'Health & Fitness', 'InBody, Apple Health+ and EGYM integrations'],
        ['fa-calendar-days', 'Calendar & Virtual', 'Google Calendar and Zoom integrations'],
        ['fa-phone-volume', 'Communication', 'CallerDesk calling integration']]),
    faqSection([
      ['What integrations does Gymex support?', 'Gymex supports integrations across payments, biometric and access systems, health and fitness platforms, scheduling, virtual sessions, and communication. Supported integrations include PayPal, Stripe, MyFatoorah, HyperPay, PayTabs, Checkout.com, Telr, eSSL, InBody, Apple Health+, EGYM, Google Calendar, Zoom, and CallerDesk.'],
      ['Does Gymex support payment gateway integrations?', 'Yes. Gymex supports multiple payment integrations, including PayPal, Stripe, MyFatoorah, HyperPay, PayTabs, Checkout.com, and Telr.'],
      ['Does Gymex integrate with biometric systems?', 'Gymex supports eSSL integration for connected biometric attendance and access-related operations.'],
      ['Can Gymex connect with Google Calendar and Zoom?', 'Yes. Gymex supports Google Calendar and Zoom integrations, helping fitness businesses connect scheduling and virtual fitness activities with their gym operations.'],
      ['Does Gymex support health and fitness integrations?', 'Yes. Gymex supports integrations with platforms including InBody, Apple Health+, and EGYM as part of its connected fitness ecosystem.'],
    ]),
    ctaSection('Connect Your Gym with the Tools That Matter', 'Bring your gym operations closer to the payment, attendance, fitness, scheduling, and communication platforms your business uses with Gymex integrations.'),
  ],
  faqs: [['What integrations does Gymex support?', 'Gymex supports integrations across payments, biometric and access systems, health platforms, scheduling, virtual sessions, and communication.'], ['Does Gymex support payment gateway integrations?', 'Yes. Gymex supports PayPal, Stripe, MyFatoorah, HyperPay, PayTabs, Checkout.com, Telr and more.'], ['Does Gymex integrate with biometric systems?', 'Gymex supports eSSL integration for connected biometric attendance and access operations.']]
});

// ── 5. EQUIPMENT INVENTORY ──
pages.push({
  dir: 'equipment-inventory', file: 'equipment-inventory.html',
  title: 'Gym Equipment Management & Inventory Software | Gymex',
  meta: 'Manage gym equipment records, service and maintenance history, vendors, and equipment reports with Gymex Equipment Inventory Software.',
  keywords: 'Gym Equipment Management Software, Gym Equipment Inventory Software, Gym Equipment Maintenance Software, Gym Equipment Tracking Software',
  build: () => [
    heroSection('Gym Equipment Management Software', 'Keep Your Gym Equipment ', 'Organized & Easy to Track', '',
      'Maintain detailed equipment records, track service and maintenance history, manage vendor information, and review equipment reports from one connected platform with Gymex.'),
    splitSection('#fff', 'left', 'Keep Detailed Records of Your ', 'Gym Equipment', '',
      'Managing multiple gym machines becomes easier when important equipment information is stored in one organized system. Gymex helps you maintain detailed records of equipment purchased for your gym.',
      chipsWrap(['Maintain records of purchased equipment', 'Keep individual equipment details organized', 'Access equipment information when required', 'Reduce dependence on spreadsheets']),
      'Equipment Details Screenshot', 'gym-equipment-management-software-gymex.webp'),
    splitSection('#f8f9fc', 'right', 'Track Equipment ', 'Service & Maintenance', ' Records',
      'Regular servicing is an important part of keeping gym equipment properly maintained. When service information is spread across files or registers, reviewing maintenance history becomes difficult. Gymex keeps it organized.',
      chipsWrap(['Service records for individual equipment', 'Track equipment maintenance records', 'Maintenance info connected to equipment details', 'Review previous service information'], '#f59e0b', '#fef9ec'),
      'Maintenance History Screenshot', 'gym-equipment-maintenance-tracking-gymex.webp'),
    splitSection('#fff', 'left', 'Keep Equipment ', 'Vendor Records', ' Organized',
      'When equipment comes from different vendors, keeping vendor information connected and easy to access can simplify everyday equipment management.',
      chipsWrap(['Maintain equipment vendor records', 'Keep vendor information organized', 'Access vendor details when required', 'Reduce scattered vendor records']),
      'Vendor Records Screenshot', 'gym-equipment-vendor-management-gymex.webp'),
    splitSection('#f8f9fc', 'right', 'Get Better Visibility with ', 'Equipment Reports', '',
      'Equipment information becomes more useful when your team can review it in a structured way. Gymex provides equipment reports that help you review equipment information and gain better visibility.',
      `<div style="display:flex; justify-content:flex-start; gap:10px; flex-wrap:wrap; margin-bottom:8px;">${flowPills(['Equipment Records', 'Service & Maintenance', 'Reports', 'Better Visibility'])}</div>`,
      'Equipment Report Screenshot', 'gym-equipment-reports-gymex.webp'),
    gridSection('#fff', 'Why Choose Gymex ', 'Equipment Inventory', '?',
      'Everything you need to keep your gym equipment organized \u2014 in one connected system.',
      [['fa-list-alt', 'Equipment Records', 'Maintain detailed records of equipment purchased for your gym.'],
        ['fa-wrench', 'Service & Maintenance History', 'Keep service and maintenance records organized for individual equipment.'],
        ['fa-chart-bar', 'Equipment Reports', 'Review equipment information through organized reports for better visibility.'],
        ['fa-truck', 'Vendor Records', 'Maintain records of equipment vendors in one connected system.']]),
    faqSection([
      ['What is gym equipment management software?', 'Gym equipment management software helps fitness businesses maintain organized records of their gym equipment. Gymex allows you to keep equipment purchase details, service and maintenance records, vendor information, and equipment reports in one system.'],
      ['Can I track equipment maintenance records in Gymex?', 'Yes. Gymex allows you to maintain service and maintenance records for individual equipment, helping your team keep equipment maintenance history organized.'],
      ['Can Gymex maintain equipment vendor information?', 'Yes. Gymex allows you to maintain records of equipment vendors, making important vendor information easier to access and manage.'],
      ['Does Gymex provide equipment reports?', 'Yes. Gymex provides equipment reports that help your team review equipment information and gain better visibility into maintained equipment records.'],
    ]),
    ctaSection('Manage Your Gym Equipment with Better Visibility', 'Keep equipment details, maintenance records, vendor information, and reports organized with Gymex Equipment Inventory.'),
  ],
  faqs: [['What is gym equipment management software?', 'Gym equipment management software helps fitness businesses maintain organized records of their gym equipment.'], ['Can I track equipment maintenance records in Gymex?', 'Yes. Gymex allows you to maintain service and maintenance records for individual equipment.'], ['Does Gymex provide equipment reports?', 'Yes. Gymex provides equipment reports for better visibility into equipment records.']]
});

// ── 6. WHATSAPP AUTOMATION ──
pages.push({
  dir: 'whatsapp-automation', file: 'whatsapp-automation.html',
  title: 'Gym WhatsApp Automation Software & Integration | Gymex',
  meta: 'Automate WhatsApp notifications for gym enquiries, appointments, payments, renewals, purchases, classes and more with Gymex WhatsApp integration.',
  keywords: 'Gym WhatsApp Automation Software, WhatsApp Automation for Gyms, Gym WhatsApp Integration, Automated WhatsApp Messages for Gyms',
  build: () => [
    heroSection('Gym WhatsApp Automation Software', 'Automate Everyday ', 'Gym Communication on WhatsApp', '',
      'Keep prospects and members informed without sending every message manually. Gymex automatically sends timely notifications for important activities \u2014 from new enquiries and appointments to payments, renewals, classes, and more.'),
    flowSection('#fff', 'Turn Everyday Gym Activities into ', 'Automated WhatsApp Updates', '',
      'With Gymex WhatsApp Automation, important activities can automatically trigger relevant WhatsApp notifications \u2014 helping your team maintain consistent communication with less manual effort.',
      ['Activity Happens', 'Notification Triggered', 'WhatsApp Message Sent', 'Member Stays Updated']),
    splitSection('#f8f9fc', 'left', 'Automate WhatsApp Notifications Across the ', 'Member Journey', '',
      'Gymex brings WhatsApp communication into different stages of the member journey, so important updates don\u2019t have to depend on someone remembering to send a message.',
      cardsGrid([['fa-user-plus', 'Prospects & Enquiries', 'Timely WhatsApp notifications when new prospects or enquiries enter your sales process.'],
        ['fa-calendar-check', 'Appointments', 'Keep prospects and members updated about relevant appointment activities.'],
        ['fa-credit-card', 'Purchases & Payments', 'Send WhatsApp updates related to purchases and payments.'],
        ['fa-sync', 'Membership Renewals', 'Automated WhatsApp notifications for membership renewal activities.'],
        ['fa-times-circle', 'Cancellations', 'Relevant WhatsApp updates when cancellations take place.'],
        ['fa-bell', 'Classes & Bookings', 'Notifications for class updates and facility bookings.']]),
      'WhatsApp Automation Screenshot', 'gym-whatsapp-automation-gymex.webp'),
    splitSection('#fff', 'right', 'Keep Members Updated About ', 'Classes & Facility Bookings', '',
      'Member communication goes beyond memberships and payments. Gymex can automatically send relevant WhatsApp notifications for class updates and facility bookings, helping members stay informed about activities they have booked or use regularly.',
      chipsWrap(['Class update notifications', 'Facility booking updates', 'Reduced manual communication', 'Smoother member experience'], '#22c55e', '#f0fdf4'),
      'Class & Facility Booking Notifications', 'gym-whatsapp-class-bookings-gymex.webp'),
    splitSection('#f8f9fc', 'left', 'Send Updates for ', 'Gift Vouchers & Wallet Transactions', '',
      'Gymex WhatsApp automation also extends to other member transactions. Relevant notifications can be sent for gift vouchers and wallet transactions, keeping members informed when these activities take place.',
      chipsWrap(['Gift voucher notifications', 'Wallet transaction updates', 'Transactional activity connected', 'Clearer member communication']),
      'Voucher & Wallet Notifications', 'gym-whatsapp-voucher-wallet-gymex.webp'),
    flowSection('#fff', 'From Enquiry to Renewal \u2014 ', 'Keep Communication Connected', '',
      'Different stages of the member journey require different communication. Gymex helps connect those moments through automated WhatsApp notifications.',
      ['Enquiry', 'Appointment', 'Purchase', 'Payment', 'Membership', 'Upgrade', 'Renewal']),
    splitSection('#f8f9fc', 'right', 'Connect Gymex with ', 'Official Meta WhatsApp', '',
      'Gymex WhatsApp Automation works when your fitness business integrates Gymex with official Meta WhatsApp. Once configured, Gymex can use WhatsApp as a connected communication channel for supported automated notifications.',
      `<div style="display:flex; justify-content:flex-start; gap:10px; flex-wrap:wrap; margin-bottom:8px;">${flowPills(['Gymex', 'Official Meta WhatsApp', 'Automated Notifications', 'Prospects & Members'])}</div>`,
      'Meta WhatsApp Integration', 'gym-meta-whatsapp-integration-gymex.webp'),
    splitSection('#fff', 'left', 'Reduce ', 'Routine Manual Follow-Ups', '',
      'With Gym WhatsApp Automation, routine notifications can be triggered automatically when relevant activities occur in Gymex. Your team can focus on conversations that actually require personal attention.',
      chipsWrap(['Reduce repetitive WhatsApp communication', 'Maintain consistent member updates', 'Keep prospects informed', 'Reduce missed routine notifications', 'Save staff time every day'], '#22c55e', '#f0fdf4'),
      'Automated Follow-Ups Screenshot', 'gym-whatsapp-followups-gymex.webp'),
    gridSection('#f8f9fc', 'Why Use Gymex ', 'WhatsApp Automation', '?',
      'Automatically connected communication across every important gym activity.',
      [['fa-bolt', 'Automated Notifications', 'Automatically communicate important Gymex activities through WhatsApp.'],
        ['fa-user-plus', 'Prospect Communication', 'Keep new prospects and enquiries informed with timely updates.'],
        ['fa-credit-card', 'Payment & Purchase Updates', 'Send relevant notifications for payments and purchases.'],
        ['fa-sync', 'Renewal & Upgrade Updates', 'Keep membership communication active around renewals.'],
        ['fa-calendar-check', 'Appointment Notifications', 'Communicate important appointment activities automatically.'],
        ['fa-dumbbell', 'Classes & Facility Bookings', 'Keep members updated about classes and bookings.'],
        ['fa-gift', 'Transaction Updates', 'Notifications for gift vouchers and wallet transactions.'],
        ['fa-clock', 'Less Manual Communication', 'Reduce the need to send repetitive routine messages individually.']]),
    faqSection([
      ['What is gym WhatsApp automation software?', 'Gym WhatsApp Automation Software connects gym management activities with automated WhatsApp communication. When relevant activities take place, supported notifications can be sent automatically instead of staff manually sending every routine message.'],
      ['What WhatsApp notifications can Gymex automate?', 'Gymex can send notifications for various activities, including new prospects and enquiries, appointments, purchases, renewals, membership upgrades, payments, cancellations, class updates, facility bookings, gift vouchers, wallet transactions, and more.'],
      ['Does Gymex WhatsApp Automation require an integration?', 'Yes. To use this functionality, the gym needs to integrate Gymex with official Meta WhatsApp.'],
      ['Can Gymex send WhatsApp notifications for membership renewals?', 'Yes. Gymex supports automated WhatsApp notifications related to membership renewal activities, helping businesses maintain timely renewal communication.'],
      ['Can Gymex automate WhatsApp messages for prospects?', 'Yes. WhatsApp automation can support communication related to new prospects and enquiries, helping your team maintain timely communication during the sales journey.'],
    ]),
    ctaSection('Make WhatsApp Communication Work Automatically', 'Keep prospects and members informed throughout their journey with automated WhatsApp notifications connected to everyday Gymex activities. Enquiries. Appointments. Payments. Renewals. Classes. Transactions. Automatically Connected.'),
  ],
  faqs: [['What is gym WhatsApp automation software?', 'Gym WhatsApp Automation Software connects gym management activities with automated WhatsApp communication.'], ['Does Gymex WhatsApp Automation require an integration?', 'Yes. The gym needs to integrate Gymex with official Meta WhatsApp.'], ['What WhatsApp notifications can Gymex automate?', 'Notifications for enquiries, appointments, payments, renewals, classes, vouchers and more.']]
});

// ═══════════ NAV FIXING ═══════════
const esc = (s) => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
const NAV_LINKS = {
  'WhatsApp Automation': '../whatsapp-automation/whatsapp-automation.html',
  'WhatsApp Automation ': '../whatsapp-automation/whatsapp-automation.html',
  'Workout &amp; Diet Planner': '../workout-diet/workout-diet-planner.html',
  'POS &amp; Locker Management': '../pos-locker/pos-locker-management.html',
  'Mobile Apps': '../mobile-apps/mobile-apps.html',
  'Equipment Inventory': '../equipment-inventory/equipment-inventory.html',
  'Integrations': '../integrations/integrations.html',
};

function fixFeatureLinks(html) {
  let out = html;
  for (const [name, url] of Object.entries(NAV_LINKS)) {
    // mega menu anchors: <a href="...(../)?features/features.html" ...class="inside"...> ... <span class="text1"...>NAME</span>
    const re = new RegExp('href="(?:\\.\\./)?features/features\\.html"((?:(?!<\\/a>)[\\s\\S])*?class="inside"(?:(?!<\\/a>)[\\s\\S])*?<span class="text1"[^>]*>' + esc(name) + '</span>)', 'g');
    out = out.replace(re, () => 'href="' + url + '"$1');
  }
  // mobile menu labels
  const labels = { 'MOBILE APP': '../mobile-apps/mobile-apps.html', 'POS MODULE': '../pos-locker/pos-locker-management.html', 'ALERTS &amp; NOTIFICATIONS': '../intelligent-alerts/intelligent-alerts-reminders.html', 'CLASS SCHEDULING': '../appointment-and-class/appointment-and-class.html', 'WHATSAPP AUTOMATION': '../whatsapp-automation/whatsapp-automation.html' };
  for (const [label, url] of Object.entries(labels)) {
    const re = new RegExp('href="(?:\\.\\./)?features/features\\.html">(' + esc(label) + ')</a>', 'g');
    out = out.replace(re, () => 'href="' + url + '">$1</a>');
  }
  return out;
}

// ═══════════ BUILD PAGES ═══════════
let built = [];
for (const p of pages) {
  const dir = path.join(ROOT, p.dir);
  if (!fs.existsSync(dir)) fs.mkdirSync(dir);
  const nav = fixFeatureLinks(NAV);
  const html = head(p) + nav + '\n' + p.build().join('\n\n') + '\n\n' + FOOTER + '\n\n</body>\n</html>\n';
  fs.writeFileSync(path.join(dir, p.file), html);
  built.push(p.dir + '/' + p.file);
}
console.log('Built pages:\n' + built.join('\n'));

// ═══════════ SHARED CSS ═══════════
fs.writeFileSync(path.join(ROOT, 'new-feature-common.css'), `/* GYMEX \u2014 NEW FEATURE PAGES SHARED STYLES */
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap");

/* FAQ accordion */
.sm-faq-item {
  background: #f8f9fc;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  padding: 0;
  overflow: hidden;
}
.sm-faq-item summary {
  padding: 18px 24px;
  font-size: 15px;
  font-weight: 600;
  color: #111;
  cursor: pointer;
  list-style: none;
  display: flex;
  align-items: center;
  justify-content: space-between;
  transition: background 0.2s;
}
.sm-faq-item summary::-webkit-details-marker { display: none; }
.sm-faq-item summary::after {
  content: "+";
  font-size: 20px;
  font-weight: 700;
  color: #028ece;
  transition: transform 0.2s;
}
.sm-faq-item[open] summary::after { content: "\u2212"; }
.sm-faq-item summary:hover { background: #f0f7ff; }
.sm-faq-item p {
  padding: 0 24px 18px;
  font-size: 14px;
  color: #555;
  line-height: 1.7;
  margin: 0;
}

/* CTA buttons (match appointment page) */
.mm-btn {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 14px 30px;
  border-radius: 50px;
  font-weight: 700;
  font-size: 14px;
  cursor: pointer;
  border: none;
  font-family: "Poppins", sans-serif;
  letter-spacing: .5px;
}
.mm-btn-orange { background: #f26522; color: #fff; }
.mm-btn-orange:hover { background: #e05510; }

/* Responsive grids */
@media (max-width: 991px) {
  .nf-grid { grid-template-columns: repeat(2, 1fr) !important; }
  .nf-three { grid-template-columns: 1fr !important; }
}
@media (max-width: 767px) {
  .nf-split { grid-template-columns: 1fr !important; }
  .nf-hero-grid { grid-template-columns: 1fr !important; }
  .nf-two { grid-template-columns: 1fr !important; }
  .nf-grid { grid-template-columns: 1fr !important; }
  .nf-table { font-size: 12px; }
  .nf-table th, .nf-table td { padding: 8px 10px !important; }
}
`);
console.log('new-feature-common.css written');

// ═══════════ UPDATE EXISTING PAGES ═══════════
function walk(dir, ext, list = []) {
  for (const f of fs.readdirSync(dir)) {
    if (f === 'node_modules' || f === '.git' || f === '.vercel') continue;
    const fp = path.join(dir, f);
    const st = fs.statSync(fp);
    if (st.isDirectory()) walk(fp, ext, list);
    else if (f.endsWith(ext)) list.push(fp);
  }
  return list;
}
const htmlFiles = walk(ROOT, '.html');
let updated = 0;
for (const f of htmlFiles) {
  if (built.some(b => f.replace(/\\/g, '/').endsWith(b))) continue;
  const src = fs.readFileSync(f, 'utf8');
  const out = fixFeatureLinks(src);
  if (out !== src) { fs.writeFileSync(f, out); updated++; }
}
console.log('Updated existing pages: ' + updated);

// ═══════════ SITEMAP ═══════════
const smPath = path.join(ROOT, 'sitemap.xml');
let sm = fs.readFileSync(smPath, 'utf8');
const base = (sm.match(/<loc>(https?:\/\/[^<]+?)\/?<\/loc>/) || [null, 'https://gymex.online'])[1].replace(/\/features\/features\.html$/, '');
const today = new Date().toISOString().slice(0, 10);
const add = pages.map(p => `
  <url>
    <loc>${base}/${p.dir}/${p.file}</loc>
    <lastmod>${today}</lastmod>
    <priority>0.8</priority>
  </url>`).join('');
if (!sm.includes('whatsapp-automation/whatsapp-automation.html')) {
  sm = sm.replace('</urlset>', add + '\n</urlset>');
  fs.writeFileSync(smPath, sm);
  console.log('sitemap.xml updated with ' + pages.length + ' new URLs');
} else {
  console.log('sitemap already has new pages');
}
console.log('DONE');
