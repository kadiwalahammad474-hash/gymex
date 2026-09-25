const fs = require('fs');

// CAPTCHA HTML to add before submit button
const captchaHTML = `
      <div class="captcha-section" style="margin:16px 0 8px;">
        <label style="display:block;font-size:13px;font-weight:600;color:var(--gray-100);margin-bottom:6px;">CAPTCHA *</label>
        <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap;">
          <div id="captcha-box" style="background:#fff;border:1.5px solid #e2e8f0;border-radius:10px;padding:8px 16px;font-size:18px;font-weight:bold;letter-spacing:6px;color:var(--gray-100);font-family:'Courier New',monospace;user-select:none;min-width:120px;text-align:center;"></div>
          <button type="button" onclick="generateCaptcha()" title="Refresh CAPTCHA" style="background:#fff;border:1.5px solid #e2e8f0;border-radius:10px;color:var(--gray-100);font-size:16px;padding:6px 12px;cursor:pointer;transition:border-color .2s;">&#8635;</button>
          <input type="text" id="captcha-input" name="captcha_input" placeholder="Enter CAPTCHA" maxlength="6" autocomplete="off" style="background:#fff;border:1.5px solid #e2e8f0;border-radius:10px;color:var(--gray-100);padding:10px 14px;font-size:14px;font-family:'Poppins',sans-serif;width:140px;outline:none;transition:border-color .2s,box-shadow .2s;" onfocus="this.style.borderColor='var(--blue)';this.style.boxShadow='0 0 0 3px rgba(2,142,206,.12)'" onblur="this.style.borderColor='#e2e8f0';this.style.boxShadow='none'">
          <input type="hidden" id="captcha-value" name="captcha_value">
        </div>
        <p id="captcha-error" style="color:#ef4444;font-size:13px;margin-top:6px;display:none;font-weight:600;">Incorrect CAPTCHA. Please try again.</p>
      </div>`;

// CAPTCHA JS
const captchaJS = `
<script>
var currentCaptcha = "";
function generateCaptcha() {
  var chars = "ABCDEFGHJKLMNPQRSTUVWXYZabcdefghjkmnpqrstuvwxyz23456789";
  var captcha = "";
  for (var i = 0; i < 6; i++) {
    captcha += chars.charAt(Math.floor(Math.random() * chars.length));
  }
  currentCaptcha = captcha;
  var box = document.getElementById("captcha-box");
  var val = document.getElementById("captcha-value");
  var inp = document.getElementById("captcha-input");
  if (box) box.innerText = captcha;
  if (val) val.value = captcha;
  if (inp) inp.value = "";
  var err = document.getElementById("captcha-error");
  if (err) err.style.display = "none";
}
function validateCaptcha() {
  var userInput = document.getElementById("captcha-input");
  if (!userInput) return true;
  userInput = userInput.value.trim();
  if (userInput === "") {
    document.getElementById("captcha-error").innerHTML = "CAPTCHA is required.";
    document.getElementById("captcha-error").style.display = "block";
    generateCaptcha();
    return false;
  }
  if (userInput !== currentCaptcha) {
    document.getElementById("captcha-error").innerHTML = "Incorrect CAPTCHA. Please try again.";
    document.getElementById("captcha-error").style.display = "block";
    generateCaptcha();
    return false;
  }
  document.getElementById("captcha-error").style.display = "none";
  return true;
}
document.addEventListener("DOMContentLoaded", function() {
  generateCaptcha();
  var form = document.querySelector(".demo-modal form");
  if (form) {
    form.addEventListener("submit", function(e) {
      if (!validateCaptcha()) e.preventDefault();
    });
  }
});
</script>`;

// All pages to update
const pages = [
  'index/index.html',
  'about/about.html', 
  'business/business.html',
  'contact/contact.html',
  'features/features.html',
  'pricing/pricing.html',
  'career/career.html'
];

for (const page of pages) {
  let c = fs.readFileSync(page, 'utf8');
  let changed = false;

  // Add CAPTCHA before submit button (if not already added)
  if (!c.includes('captcha-box')) {
    c = c.replace(
      /<button type="submit" class="submit-btn">/,
      captchaHTML + '\n      <button type="submit" class="submit-btn">'
    );
    changed = true;
  }

  // Add CAPTCHA JS before </body> (if not already added)
  if (!c.includes('currentCaptcha')) {
    c = c.replace('</body>', captchaJS + '\n</body>');
    changed = true;
  }

  if (changed) {
    fs.writeFileSync(page, c);
    console.log('Updated: ' + page);
  } else {
    console.log('Already has CAPTCHA: ' + page);
  }
}
