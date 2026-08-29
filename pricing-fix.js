#!/usr/bin/env node
const fs = require('fs');
const path = require('path');

const pricingPath = 'C:/Users/Developer4/Desktop/gymexglobalwebsite/pricing/pricing.html';
let html = fs.readFileSync(pricingPath, 'utf8');

// 1. Remove the DUPLICATE footer that appears after the counter animation script
// The duplicate starts after '</script>\r\n\r\n\r\n  <div style="max-width:1200px;...'
const counterScriptEnd = `})();\r\n</script>\r\n\r\n\r\n  <div style="max-width:1200px; margin:0 auto; padding:20px 24px 16px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">`;
const counterScriptEndLF = `})();\r\n</script>\r\n\r\n\n  <div style="max-width:1200px; margin:0 auto; padding:20px 24px 16px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">`;

// Find the counter script end and everything after it until </body>
const counterPattern = /\(\)\(\);\s*\}\)\(\);\s*<\/script>\s*\r?\n\r?\n\r?\n\s*<div style="max-width:1200px; margin:0 auto; padding:20px 24px 16px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">[\s\S]*?<\/body>/;

const replacement = `})();\r\n</script>\r\n\r\n</body>`;

if (counterPattern.test(html)) {
  html = html.replace(counterPattern, replacement);
  console.log('✅ Removed duplicate footer');
} else {
  console.log('⚠️ Pattern not found, trying alternative...');
  // Alternative: find the second occurrence of the footer navigation links
  const footerNav = `<div style="max-width:1200px; margin:0 auto; padding:20px 24px 16px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">`;
  const firstIdx = html.indexOf(footerNav);
  const secondIdx = html.indexOf(footerNav, firstIdx + 1);
  
  if (secondIdx > 0) {
    // Find </body> after second occurrence
    const bodyEnd = html.indexOf('</body>', secondIdx);
    if (bodyEnd > 0) {
      // Remove from second footerNav to </body> and replace with just </body>
      html = html.substring(0, secondIdx) + '\r\n</body>' + html.substring(bodyEnd + 7);
      console.log('✅ Removed duplicate footer (alternative method)');
    }
  }
}

// 2. Make the "GET YOUR FREE DEMO" orange CTA bar button open the modal
// Replace the mm-cta-banner with one that has open-modal-btn
html = html.replace(
  /<div class="mm-cta-banner">\s*<h2>Ready to see <span class="accent">Gymex<\/span> in action for your gym\?<\/h2>\s*<\/div>/,
  `<div class="mm-cta-banner">\n      <h2>Ready to see <span class="accent">Gymex</span> in action for your gym?</h2>\n      <button class="mm-btn mm-btn-orange open-modal-btn" style="margin-top:16px;">Get Your Free Demo <i class="fa fa-arrow-up"></i></button>\n    </div>`
);

fs.writeFileSync(pricingPath, html, 'utf8');
console.log('✅ Pricing page updated');
