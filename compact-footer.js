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

// Relative path prefix for each page to root assets
function getPrefix(pagePath) {
  const depth = pagePath.split('/').length - 1;
  return depth === 1 ? '../' : '../'.repeat(depth);
}

// The new compact footer HTML
function footerHTML(pagePath) {
  const p = getPrefix(pagePath);
  return `
<!-- Footer -->
<div style="background:#0b1a3d; padding:0; margin-top:60px;">
  <!-- Top Links Row - Compact Grey Bar -->
  <div style="background:#f5f5f5; padding:12px 0;">
    <div style="max-width:1100px; margin:0 auto; padding:0 20px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px;">
      <div style="display:flex; gap:20px; flex-wrap:wrap; align-items:center;">
        <a href="${p}index/index.html" style="color:#333; font-size:12px; font-weight:600; text-decoration:none; letter-spacing:.3px;">HOME</a>
        <a href="${p}about/about.html" style="color:#333; font-size:12px; font-weight:600; text-decoration:none; letter-spacing:.3px;">ABOUT US</a>
        <a href="${p}pricing/pricing.html" style="color:#333; font-size:12px; font-weight:600; text-decoration:none; letter-spacing:.3px;">PRICING</a>
        <a href="#" style="color:#333; font-size:12px; font-weight:600; text-decoration:none; letter-spacing:.3px;">BLOG</a>
        <a href="${p}contact/contact.html" style="color:#333; font-size:12px; font-weight:600; text-decoration:none; letter-spacing:.3px;">CONTACT US</a>
        <a href="#" style="color:#333; font-size:12px; font-weight:600; text-decoration:none; letter-spacing:.3px;">TERMS &amp; CONDITIONS</a>
        <a href="#" style="color:#333; font-size:12px; font-weight:600; text-decoration:none; letter-spacing:.3px;">PRIVACY POLICY</a>
        <a href="#" style="color:#333; font-size:12px; font-weight:600; text-decoration:none; letter-spacing:.3px;">REFUND POLICY</a>
      </div>
      <a class="open-demo-modal" href="#" style="background:#f26522; color:#fff; padding:8px 22px; border-radius:50px; font-size:11px; font-weight:700; text-decoration:none; white-space:nowrap; letter-spacing:.3px;">ASK FOR DEMO</a>
    </div>
  </div>

  <!-- Dark Navy Content -->
  <div style="max-width:1100px; margin:0 auto; padding:28px 20px 20px; display:flex; justify-content:space-between; gap:30px;">
    <!-- About Us -->
    <div style="flex:1;">
      <h3 style="color:#fff; font-size:14px; font-weight:700; margin:0 0 8px;">About Us</h3>
      <p style="color:rgba(255,255,255,.65); font-size:12px; line-height:1.7; margin:0;">Gymex is a powerful cloud based gym management software built to facilitate to effectively manage gym &amp; fitness related businesses.</p>
    </div>
    <!-- Contact Us -->
    <div style="flex:1.4;">
      <h3 style="color:#fff; font-size:14px; font-weight:700; margin:0 0 8px;">Contact Us</h3>
      <p style="color:rgba(255,255,255,.65); font-size:12px; line-height:1.7; margin:0 0 14px;">GreyBits Technologies Office No. 2, An-Nazir Building, Momin Nagar, Patel Estate Road, Jogeshwari West, Mumbai - 400102</p>
      <div style="display:flex; gap:30px;">
        <div>
          <h4 style="color:#fff; font-size:13px; font-weight:700; margin:0 0 6px;">For Sales</h4>
          <div style="display:flex; align-items:center; gap:6px; margin-bottom:4px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#4da6ff" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
            <a href="tel:+917710862007" style="color:rgba(255,255,255,.65); font-size:12px; text-decoration:none;">+91 7710862007</a>
          </div>
          <div style="display:flex; align-items:center; gap:6px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#4da6ff" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
            <a href="mailto:sales@gymex.online" style="color:rgba(255,255,255,.65); font-size:12px; text-decoration:none;">sales@gymex.online</a>
          </div>
        </div>
        <div>
          <h4 style="color:#fff; font-size:13px; font-weight:700; margin:0 0 6px;">For Support</h4>
          <div style="display:flex; align-items:center; gap:6px; margin-bottom:4px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#4da6ff" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
            <a href="tel:+918291682083" style="color:rgba(255,255,255,.65); font-size:12px; text-decoration:none;">+91 8291682083</a>
          </div>
          <div style="display:flex; align-items:center; gap:6px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#4da6ff" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
            <a href="mailto:support@gymex.online" style="color:rgba(255,255,255,.65); font-size:12px; text-decoration:none;">support@gymex.online</a>
          </div>
        </div>
      </div>
    </div>
    <!-- Follow Us On -->
    <div style="flex:0.5; text-align:right;">
      <h3 style="color:#fff; font-size:14px; font-weight:700; margin:0 0 8px;">Follow Us On</h3>
      <div style="display:flex; gap:10px; justify-content:flex-end;">
        <a href="https://www.facebook.com/gymexsoftware" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24"><circle cx="12" cy="12" r="12" fill="#3b5998"/><path d="M16.67 15.04l.52-3.39h-3.25v-2.2c0-.93.46-1.84 1.92-1.84h1.49V4.12s-1.35-.23-2.64-.23c-2.7 0-4.46 1.63-4.46 4.58v2.62H7.6v3.39h2.65V22h3.35v-6.96h2.36z" fill="white"/></svg></a>
        <a href="https://www.instagram.com/gymexclubmanagement" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24"><defs><radialGradient id="igFc" cx="30%" cy="107%"><stop offset="0%" stop-color="#fdf497"/><stop offset="5%" stop-color="#fdf497"/><stop offset="45%" stop-color="#fd5949"/><stop offset="60%" stop-color="#d6249f"/><stop offset="90%" stop-color="#285AEB"/></radialGradient></defs><circle cx="12" cy="12" r="12" fill="url(#igFc)"/><rect x="5" y="5" width="14" height="14" rx="4" fill="none" stroke="white" stroke-width="1.5"/><circle cx="12" cy="12" r="3.5" fill="none" stroke="white" stroke-width="1.5"/><circle cx="17" cy="7" r="1" fill="white"/></svg></a>
        <a href="https://www.linkedin.com/company/gymex-club-management-software/" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24"><circle cx="12" cy="12" r="12" fill="#0077b5"/><path d="M8 10.5v5.5M8 8v.01M11 16v-3.5c0-1.1.9-2 2-2s2 .9 2 2V16" stroke="white" stroke-width="1.8" fill="none" stroke-linecap="round"/><rect x="5.5" y="10" width="5" height="5.5" rx="0.5" fill="none" stroke="white" stroke-width="1.3"/></svg></a>
      </div>
    </div>
  </div>

  <!-- Copyright -->
  <div style="border-top:1px solid rgba(255,255,255,.08); padding:10px 0;">
    <div style="max-width:1100px; margin:0 auto; padding:0 20px; text-align:center;">
      <p style="color:rgba(255,255,255,.4); font-size:11px; margin:0;">&copy; 2024 Gymex Club Management Software. All Rights Reserved.</p>
    </div>
  </div>
</div>

<!-- Footer Mobile -->
<style>
@media(max-width:768px){
  .footer-wrap,.footer-wrap>[style*="display:flex"]{flex-direction:column!important;gap:14px!important;align-items:flex-start!important}
  .footer-wrap [style*="flex:1"],.footer-wrap [style*="flex:1.4"],.footer-wrap [style*="flex:0.5"]{flex:1 1 100%!important;max-width:100%!important}
  .footer-wrap [style*="flex-wrap:nowrap"]{flex-wrap:wrap!important}
  .footer-wrap [style*="gap:30px"]{gap:12px!important}
}
</style>`;
}

// Regex to match old footer (from "<!-- Footer -->" to "<!-- Footer Mobile -->" closing style tag or before "<!-- Demo Modal -->")
const footerRegex = /\n<!-- Footer -->[\s\S]*?<!-- Footer Mobile -->[\s\S]*?<\/style>/;
const footerRegex2 = /\n<!-- Footer -->[\s\S]*?<\/style>\s*(?=\n<!-- |\n<div class="demo)/;

let updated = 0;
let errors = 0;

for (const page of pages) {
  const filePath = path.join(BASE, page);
  try {
    let content = fs.readFileSync(filePath, 'utf8');
    
    // Find footer start
    const footerStart = content.indexOf('<!-- Footer -->');
    if (footerStart === -1) {
      console.log(`SKIP (no footer marker): ${page}`);
      errors++;
      continue;
    }
    
    // Find footer end - look for <!-- Demo Modal --> or <div class="demo-modal
    let footerEnd = content.indexOf('<!-- Demo Modal -->', footerStart);
    if (footerEnd === -1) {
      footerEnd = content.indexOf('<div class="demo-modal-overlay"', footerStart);
    }
    if (footerEnd === -1) {
      // Try <!-- Footer Mobile --> end style tag
      const mobileStyleEnd = content.lastIndexOf('</style>', footerStart + 2000);
      if (mobileStyleEnd > footerStart) {
        footerEnd = mobileStyleEnd + 8;
      }
    }
    if (footerEnd === -1) {
      console.log(`SKIP (no footer end): ${page}`);
      errors++;
      continue;
    }
    
    // Replace
    const before = content.substring(0, footerStart);
    const after = content.substring(footerEnd);
    const newContent = before + footerHTML(page) + after;
    
    fs.writeFileSync(filePath, newContent, 'utf8');
    console.log(`UPDATED: ${page}`);
    updated++;
  } catch (e) {
    console.log(`ERROR: ${page} - ${e.message}`);
    errors++;
  }
}

console.log(`\nDone! Updated: ${updated}, Errors: ${errors}`);
