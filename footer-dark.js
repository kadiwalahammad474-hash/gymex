const fs = require('fs');
const path = require('path');

const DARK_FOOTER = `
<!-- Footer -->
<div class="footer" style="background:#0b1a3d; padding:0;">
  <!-- Links Bar -->
  <div style="padding:18px 0; border-bottom:1px solid rgba(255,255,255,0.1);">
    <div style="max-width:1200px; margin:0 auto; padding:0 24px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px;">
      <div style="display:flex; gap:28px; flex-wrap:wrap; align-items:center;">
        <a href="../index/index.html" style="color:rgba(255,255,255,0.85); font-size:13px; font-weight:600; text-decoration:none; letter-spacing:.5px;">HOME</a>
        <a href="../about/about.html" style="color:rgba(255,255,255,0.85); font-size:13px; font-weight:600; text-decoration:none; letter-spacing:.5px;">ABOUT US</a>
        <a href="../pricing/pricing.html" style="color:rgba(255,255,255,0.85); font-size:13px; font-weight:600; text-decoration:none; letter-spacing:.5px;">PRICING</a>
        <a href="#" style="color:rgba(255,255,255,0.85); font-size:13px; font-weight:600; text-decoration:none; letter-spacing:.5px;">BLOG</a>
        <a href="../contact/contact.html" style="color:rgba(255,255,255,0.85); font-size:13px; font-weight:600; text-decoration:none; letter-spacing:.5px;">CONTACT US</a>
        <a href="#" style="color:rgba(255,255,255,0.85); font-size:13px; font-weight:600; text-decoration:none; letter-spacing:.5px;">TERMS &amp; CONDITIONS</a>
        <a href="#" style="color:rgba(255,255,255,0.85); font-size:13px; font-weight:600; text-decoration:none; letter-spacing:.5px;">PRIVACY POLICY</a>
        <a href="#" style="color:rgba(255,255,255,0.85); font-size:13px; font-weight:600; text-decoration:none; letter-spacing:.5px;">REFUND POLICY</a>
      </div>
      <a class="open-demo-modal" href="#" style="background:#f26522; color:#fff; padding:10px 28px; border-radius:50px; font-size:13px; font-weight:700; text-decoration:none; white-space:nowrap; letter-spacing:.5px;">ASK FOR DEMO</a>
    </div>
  </div>

  <!-- Content -->
  <div style="padding:48px 0 36px;">
    <div style="max-width:1200px; margin:0 auto; padding:0 24px; display:flex; justify-content:space-between; gap:40px;">
      <!-- About Us -->
      <div style="flex:1;">
        <h3 style="color:#fff; font-size:18px; font-weight:700; margin-bottom:14px;">About Us</h3>
        <p style="color:rgba(255,255,255,0.7); font-size:14px; line-height:1.8;">Gymex is a powerful cloud based gym management software built to facilitate to effectively manage gym &amp; fitness related businesses.</p>
      </div>
      <!-- Contact Us -->
      <div style="flex:1.4;">
        <h3 style="color:#fff; font-size:18px; font-weight:700; margin-bottom:14px;">Contact Us</h3>
        <p style="color:rgba(255,255,255,0.7); font-size:14px; line-height:1.8; margin-bottom:24px;">GreyBits Technologies Office No. 2, An-Nazir Building, Momin Nagar, Patel Estate Road, Jogeshwari West, Mumbai - 400102</p>
        <div style="display:flex; gap:40px;">
          <div>
            <h4 style="color:#fff; font-size:15px; font-weight:700; margin-bottom:12px;">For Sales</h4>
            <div style="display:flex; align-items:center; gap:8px; margin-bottom:8px;">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#4da6ff" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
              <a href="tel:+917710862007" style="color:rgba(255,255,255,0.7); font-size:14px; text-decoration:none;">+91 7710862007</a>
            </div>
            <div style="display:flex; align-items:center; gap:8px;">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#4da6ff" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
              <a href="mailto:sales@gymex.online" style="color:rgba(255,255,255,0.7); font-size:14px; text-decoration:none;">sales@gymex.online</a>
            </div>
          </div>
          <div>
            <h4 style="color:#fff; font-size:15px; font-weight:700; margin-bottom:12px;">For Support</h4>
            <div style="display:flex; align-items:center; gap:8px; margin-bottom:8px;">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#4da6ff" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
              <a href="tel:+918291682083" style="color:rgba(255,255,255,0.7); font-size:14px; text-decoration:none;">+91 8291682083</a>
            </div>
            <div style="display:flex; align-items:center; gap:8px;">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#4da6ff" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
              <a href="mailto:support@gymex.online" style="color:rgba(255,255,255,0.7); font-size:14px; text-decoration:none;">support@gymex.online</a>
            </div>
          </div>
        </div>
      </div>
      <!-- Follow Us On -->
      <div style="flex:0.5;">
        <h3 style="color:#fff; font-size:18px; font-weight:700; margin-bottom:14px;">Follow Us On</h3>
        <div style="display:flex; gap:14px; margin-top:4px;">
          <a href="https://www.facebook.com/gymexsoftware" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 24 24"><circle cx="12" cy="12" r="12" fill="#3b5998"/><path d="M16.67 15.04l.52-3.39h-3.25v-2.2c0-.93.46-1.84 1.92-1.84h1.49V4.12s-1.35-.23-2.64-.23c-2.7 0-4.46 1.63-4.46 4.58v2.62H7.6v3.39h2.65V22h3.35v-6.96h2.36z" fill="white"/></svg></a>
          <a href="https://www.instagram.com/gymexclubmanagement" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 24 24"><defs><radialGradient id="igFoot" cx="30%" cy="107%"><stop offset="0%" stop-color="#fdf497"/><stop offset="5%" stop-color="#fdf497"/><stop offset="45%" stop-color="#fd5949"/><stop offset="60%" stop-color="#d6249f"/><stop offset="90%" stop-color="#285AEB"/></radialGradient></defs><circle cx="12" cy="12" r="12" fill="url(#igFoot)"/><rect x="5" y="5" width="14" height="14" rx="4" fill="none" stroke="white" stroke-width="1.5"/><circle cx="12" cy="12" r="3.5" fill="none" stroke="white" stroke-width="1.5"/><circle cx="17" cy="7" r="1" fill="white"/></svg></a>
          <a href="https://www.linkedin.com/company/gymex-club-management-software/" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 24 24"><circle cx="12" cy="12" r="12" fill="#0077b5"/><path d="M8 10.5v5.5M8 8v.01M11 16v-3.5c0-1.1.9-2 2-2s2 .9 2 2V16" stroke="white" stroke-width="1.8" fill="none" stroke-linecap="round"/><rect x="5.5" y="10" width="5" height="5.5" rx="0.5" fill="none" stroke="white" stroke-width="1.3"/></svg></a>
        </div>
      </div>
    </div>
  </div>

  <!-- Copyright -->
  <div style="border-top:1px solid rgba(255,255,255,0.1); padding:18px 0;">
    <div style="max-width:1200px; margin:0 auto; padding:0 24px; text-align:center;">
      <p style="color:rgba(255,255,255,0.5); font-size:13px;">&copy; 2024 Gymex Club Management Software. All Rights Reserved.</p>
    </div>
  </div>
</div>`;

// OLD footer patterns to match and replace
const OLD_FOOTER_PATTERNS = [
  // Pattern 1: <!-- Footer Links Bar --> ... <!-- Footer Copyright --> + closing divs
  /<!-- Footer Links Bar -->[\s\S]*?<!-- Footer Copyright -->[\s\S]*?<\/div>\s*<\/div>\s*<\/div>/,
  // Pattern 2: <div class="footer"> with nested content
  /<div class="footer">\s*<div class="container">[\s\S]*?<\/div>\s*<\/div>\s*<\/div>/,
  // Pattern 3: footer-main
  /<!-- Footer Main -->[\s\S]*?All Rights Reserved\.<\/p>\s*<\/div>\s*<\/div>\s*<\/div>/,
];

// Also remove the separate grey links bar that might exist before footer
const OLD_LINKS_BAR = /<!-- Footer Links Bar -->[\s\S]*?ASK FOR DEMO<\/a>\s*<\/div>\s*<\/div>\s*<\/div>/;

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

let fixed = 0;
for (const page of pages) {
  const filePath = path.join(__dirname, page);
  if (!fs.existsSync(filePath)) {
    console.log(`SKIP: ${page} not found`);
    continue;
  }
  
  let html = fs.readFileSync(filePath, 'utf8');
  
  // Find the footer section - look for <!-- Footer Main --> or <div class="footer"> or <!-- Footer Links Bar -->
  let footerStart = html.indexOf('<!-- Footer Main -->');
  if (footerStart === -1) footerStart = html.indexOf('<!-- Footer Links Bar -->');
  if (footerStart === -1) footerStart = html.indexOf('<div class="footer"');
  
  if (footerStart === -1) {
    console.log(`SKIP: ${page} - no footer found`);
    continue;
  }
  
  // Find the end - look for <!-- Demo Modal --> or </body> or <div class="whatsapp"
  let footerEnd = html.indexOf('<!-- Demo Modal -->', footerStart);
  if (footerEnd === -1) footerEnd = html.indexOf('<div class="whatsapp', footerStart);
  if (footerEnd === -1) footerEnd = html.indexOf('</body>', footerStart);
  
  if (footerEnd === -1) {
    console.log(`SKIP: ${page} - can't find footer end`);
    continue;
  }
  
  // Build new HTML: everything before footer + new footer + everything after
  const before = html.substring(0, footerStart).trimEnd();
  const after = html.substring(footerEnd).trimStart();
  
  // Clean up any stray closing divs between footer end and demo modal
  const newHtml = before + '\n\n' + DARK_FOOTER + '\n\n' + after;
  
  fs.writeFileSync(filePath, newHtml, 'utf8');
  console.log(`DONE: ${page}`);
  fixed++;
}

console.log(`\nTotal fixed: ${fixed} pages`);
