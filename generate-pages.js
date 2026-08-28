const fs = require('fs');

// ═══════════════════════════════════════════════════
// COMMON: Header (from home page) + Footer + Modal
// ═══════════════════════════════════════════════════

function getNav() {
  return `<div class="container"><nav class="nav" id="nav">
        <div class="nav__logo-links-container">
          <a class="nav__logo-wrap" href="../index/index.html">
            <img class="logo" src="../assets/Gymex-logo-wit6Qpcs.svg" alt="logo">
          </a>
          <div class="flex-center">
            <div class="nav__list">
              <a class="nav__link" href="../index/index.html">Home</a>
              <div class="dropdown">
                <a class="nav__link" href="../business/business.html">Business Types <i class="fa fa-chevron-down"></i></a>
                <div class="dropdown-content mega-menu">
                  <div class="column"><p class="mega-col-title">Gym &amp; Fitness</p>
                    <div style="display:flex;" class="inside">
                      <div><a href="../business/health-and-fitness-centers.html"><span class="mm-emoji">🏋️</span>Health &amp; Fitness</a><a href="../business/gym-management-software.html"><span class="mm-emoji">💪</span>Gym Management</a></div>
                    </div>
                  </div>
                  <div class="column"><p class="mega-col-title">Studio</p>
                    <div style="display:flex;" class="inside">
                      <div><a href="../business/yoga-studio.html"><span class="mm-emoji">🧘</span>Yoga Studio</a><a href="../business/dance-studio.html"><span class="mm-emoji">💃</span>Dance Studio</a><a href="../business/pilates.html"><span class="mm-emoji">🤸</span>Pilates</a></div>
                    </div>
                  </div>
                  <div class="column"><p class="mega-col-title">Specialty</p>
                    <div style="display:flex;" class="inside">
                      <div><a href="../business/martial-arts-studio.html"><span class="mm-emoji">🥋</span>Martial Arts</a><a href="../business/swim-school.html"><span class="mm-emoji">🏊</span>Swim School</a><a href="../business/sport-academies.html"><span class="mm-emoji">🏅</span>Sports Academy</a><a href="../business/pt-studio.html"><span class="mm-emoji">🎯</span>PT Studio</a><a href="../business/aerobics.html"><span class="mm-emoji">🩰</span>Aerobics</a></div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="dropdown">
                <a class="nav__link" href="#">Features <i class="fa fa-chevron-down"></i></a>
                <div class="dropdown-content mega-menu features-mega">
                  <div class="column"><p class="mega-col-title">Core Operations</p>
                    <div style="display:flex;" class="inside">
                      <div>
                        <a href="../staff-management/staff-management.html"><span class="mm-emoji">👥</span>Staff Management</a>
                        <a href="../lead-management/lead-management.html"><span class="mm-emoji">📈</span>Lead Management</a>
                        <a href="../marketing-management/marketing-management.html"><span class="mm-emoji">📣</span>Marketing Management</a>
                        <a href="../member-management/member-management.html"><span class="mm-emoji">👤</span>Member Management</a>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <a class="nav__link" href="../pricing/pricing.html">Pricing</a>
              <a class="nav__link" href="../blog/blog.html">Blog</a>
              <a class="nav__link" href="../contact/contact.html">Contact Us</a>
            </div>
            <button class="nav__cta open-modal-btn">Get Your Free Demo</button>
          </div>
        </div>
        <button class="menu__icon" id="open-menu">
          <span></span><span></span><span></span>
        </button>
      </nav>
      <div class="mobile-nav-content" id="mobile-nav">
        <a href="../index/index.html">Home</a>
        <div class="dropdown"><a href="#">Business Types <i class="fa fa-chevron-down"></i></a><div class="dropdown-menu"><a href="../business/health-and-fitness-centers.html">Health &amp; Fitness</a><a href="../business/gym-management-software.html">Gym Management</a><a href="../business/yoga-studio.html">Yoga Studio</a><a href="../business/dance-studio.html">Dance Studio</a><a href="../business/pilates.html">Pilates</a><a href="../business/martial-arts-studio.html">Martial Arts</a><a href="../business/swim-school.html">Swim School</a><a href="../business/sport-academies.html">Sports Academy</a></div></div>
        <div class="dropdown"><a href="#">Features <i class="fa fa-chevron-down"></i></a><div class="dropdown-menu"><a href="../staff-management/staff-management.html">Staff Management</a><a href="../lead-management/lead-management.html">Lead Management</a><a href="../marketing-management/marketing-management.html">Marketing Management</a><a href="../member-management/member-management.html">Member Management</a></div></div>
        <a href="../pricing/pricing.html">Pricing</a>
        <a href="../blog/blog.html">Blog</a>
        <a href="../contact/contact.html">Contact Us</a>
        <a class="nav__cta open-modal-btn" style="text-align:center;">Get Your Free Demo</a>
      </div>
    </div>`;
}

function getHead(title, desc, keywords, extraCSS) {
  return `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>${title}</title>
<meta name="description" content="${desc}">
<meta name="keywords" content="${keywords}">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="../assets/gymex-favicon.png" type="image/png">
<link rel="stylesheet" href="../assets/bootstrap/bootstrap.min.css">
<script src="../assets/scripts/jquery.min.js"></script>
<script src="../assets/bootstrap/bootstrap.bundle.min.js"></script>
<link href="../assets/aos/aos.css" rel="stylesheet">
<script src="../assets/aos/aos.js"></script>
<link rel="stylesheet" href="../style.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<script type="text/javascript">(function(c,l,a,r,i,t,y){c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);})(window, document, "clarity", "script", "n95oax955q");</script>
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],d=document.createElement(s);dl=l!='dataLayer'?'&l='+l:'';d.async=true;d.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(d,f);})(window,document,'script','dataLayer','GTM-KPCRHTFH');</script>
<style>
body{font-family:'Inter','Segoe UI',sans-serif;margin:0;color:#1e293b;background:#fff;}
a{text-decoration:none;color:inherit;}
${extraCSS}
</style>
</head>`;
}

function getFooter() {
  return `<div style="background:#0b1a3d; padding:0;">
  <div style="max-width:1200px; margin:0 auto; padding:36px 24px 16px;">
    <div style="display:flex; flex-wrap:wrap; gap:8px 24px; justify-content:center; border-bottom:1px solid rgba(255,255,255,.12); padding-bottom:20px; margin-bottom:24px;">
      <a href="../index/index.html" style="color:rgba(255,255,255,.65); font-size:13px;">Home</a>
      <a href="../about/about.html" style="color:rgba(255,255,255,.65); font-size:13px;">About Us</a>
      <a href="../pricing/pricing.html" style="color:rgba(255,255,255,.65); font-size:13px;">Pricing</a>
      <a href="../blog/blog.html" style="color:rgba(255,255,255,.65); font-size:13px;">Blog</a>
      <a href="../contact/contact.html" style="color:rgba(255,255,255,.65); font-size:13px;">Contact Us</a>
      <a href="../privacy-policy/privacy-policy.html" style="color:rgba(255,255,255,.65); font-size:13px;">Privacy Policy</a>
      <a href="../refund-policy/refund-policy.html" style="color:rgba(255,255,255,.65); font-size:13px;">Refund Policy</a>
    </div>
    <div style="display:grid; grid-template-columns:1.4fr 1fr 0.5fr; gap:40px; margin-bottom:24px;">
      <div><h4 style="color:#fff; font-size:15px; margin:0 0 12px;">About Gymex</h4><p style="color:rgba(255,255,255,.55); font-size:13px; line-height:1.7; margin:0;">Gymex is a powerful cloud-based gym management software built to help fitness businesses manage operations, members, and growth.</p></div>
      <div><h4 style="color:#fff; font-size:15px; margin:0 0 12px;">Contact</h4><p style="color:rgba(255,255,255,.55); font-size:13px; line-height:1.7; margin:0;">Office No. 2, An-Nazir Building, Jogeshwari West, Mumbai – 400102</p><p style="color:rgba(255,255,255,.55); font-size:13px; margin:8px 0 0;">Sales: +91 7710862007</p></div>
      <div><h4 style="color:#fff; font-size:15px; margin:0 0 12px;">Follow Us</h4><div style="display:flex; gap:12px;"><a href="https://www.facebook.com/gymexsoftware" target="_blank" style="color:rgba(255,255,255,.55); font-size:20px;"><i class="fa fa-facebook"></i></a><a href="https://www.instagram.com/gymexclubmanagement" target="_blank" style="color:rgba(255,255,255,.55); font-size:20px;"><i class="fa fa-instagram"></i></a></div><img src="../assets/gymex-logo-wit6Qpcs.svg" alt="Gymex" style="height:28px; margin-top:16px; opacity:.5;"></div>
    </div>
    <div style="border-top:1px solid rgba(255,255,255,.1); padding-top:16px; text-align:center;"><p style="color:rgba(255,255,255,.4); font-size:12px; margin:0;">© 2024 Gymex Club Management Software. All Rights Reserved.</p></div>
  </div>
</div>`;
}

function getModal() {
  return `
<div class="backdrop" id="divemailpopup"><div class="contact-popup"><button id="close-contact-modal" class="close-btn">&times;</button><div id="loader" style="display:none;text-align:center;padding:40px;"><i class="fa fa-spinner fa-spin" style="font-size:32px;color:#1565C0;"></i></div><div id="form-body"><h3>Get Your Free Demo</h3><p>See how Gymex fits your workflow.</p><form id="contact-form"><div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;"><input type="text" id="first-name" placeholder="First Name *" required style="padding:12px;border:1px solid #ddd;border-radius:8px;font-size:14px;"><input type="text" id="last-name" placeholder="Last Name *" required style="padding:12px;border:1px solid #ddd;border-radius:8px;font-size:14px;"></div><input type="text" id="company" placeholder="Gym Name *" required style="width:100%;padding:12px;margin-top:12px;border:1px solid #ddd;border-radius:8px;font-size:14px;box-sizing:border-box;"><input type="email" id="email" placeholder="Email *" required style="width:100%;padding:12px;margin-top:12px;border:1px solid #ddd;border-radius:8px;font-size:14px;box-sizing:border-box;"><input type="tel" id="number" placeholder="Phone *" required style="width:100%;padding:12px;margin-top:12px;border:1px solid #ddd;border-radius:8px;font-size:14px;box-sizing:border-box;"><textarea id="message" placeholder="Message" rows="3" style="width:100%;padding:12px;margin-top:12px;border:1px solid #ddd;border-radius:8px;font-size:14px;box-sizing:border-box;"></textarea><div style="display:flex;align-items:center;gap:10px;margin-top:12px;"><div id="captcha-box" style="background:#fff;border:1px solid #ccc;border-radius:4px;padding:4px 14px;font-size:16px;font-weight:bold;letter-spacing:4px;font-family:monospace;color:#333;"></div><button type="button" onclick="generateCaptcha()" style="background:#fff;border:1px solid #ccc;border-radius:4px;padding:4px 10px;cursor:pointer;">&#8635;</button><input type="text" id="captcha-input" placeholder="Enter CAPTCHA" maxlength="6" style="padding:8px 12px;border:1px solid #ccc;border-radius:4px;font-size:13px;width:120px;"><input type="hidden" id="captcha-value"></div><p id="captcha-error" style="color:red;font-size:12px;margin-top:4px;display:none;"></p><button type="submit" style="width:100%;padding:14px;background:#f26522;color:#fff;border:none;border-radius:8px;font-size:15px;font-weight:700;cursor:pointer;margin-top:16px;">Submit</button></form></div><div id="emailsuccessmsg" style="display:none;text-align:center;padding:40px;"><i class="fa fa-check-circle" style="font-size:48px;color:#16a34a;"></i><h3 style="margin-top:16px;">Thank You!</h3><p style="color:#666;">We'll contact you soon.</p><button class="send-again-btn" style="margin-top:16px;padding:10px 24px;background:#1565C0;color:#fff;border:none;border-radius:8px;cursor:pointer;">Send Another</button></div></div></div>
<script>var cc="";function generateCaptcha(){var c="ABCDEFGHJKLMNPQRSTUVWXYZ23456789",r="";for(var i=0;i<6;i++)r+=c.charAt(Math.floor(Math.random()*c.length));cc=r;var b=document.getElementById('captcha-box');if(b)b.innerText=r;var v=document.getElementById('captcha-value');if(v)v.value=r;var inp=document.getElementById('captcha-input');if(inp)inp.value='';}
window.addEventListener('load',function(){generateCaptcha();});</script>
<script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js"></script>
<script>
document.querySelectorAll('.open-modal-btn').forEach(function(b){b.addEventListener('click',function(e){e.preventDefault();document.getElementById('divemailpopup').classList.add('show');document.body.style.overflow='hidden';});});
document.getElementById('close-contact-modal').addEventListener('click',function(){document.getElementById('divemailpopup').classList.remove('show');document.body.style.overflow='auto';document.getElementById('emailsuccessmsg').style.display='none';document.getElementById('form-body').style.display='block';});
document.getElementById('divemailpopup').addEventListener('click',function(e){if(e.target===this){this.classList.remove('show');document.body.style.overflow='auto';}});
document.querySelector('.send-again-btn').addEventListener('click',function(){document.getElementById('emailsuccessmsg').style.display='none';document.getElementById('form-body').style.display='block';});
emailjs.init('AmP09sgXBaIgn9Juz');
document.getElementById('contact-form').onsubmit=function(e){e.preventDefault();var u=document.getElementById('captcha-input').value.trim();if(u!==cc){document.getElementById('captcha-error').innerHTML='Incorrect CAPTCHA.';document.getElementById('captcha-error').style.display='block';generateCaptcha();return false;}document.getElementById('captcha-error').style.display='none';var l=document.getElementById('loader');l.style.display='block';document.getElementById('form-body').style.display='none';emailjs.send('service_1o6wljl','template_6dewzmp',{firstname:document.getElementById('first-name').value,lastname:document.getElementById('last-name').value,company:document.getElementById('company').value,email:document.getElementById('email').value,phonenumber:document.getElementById('number').value,message:document.getElementById('message').value}).then(function(){l.style.display='none';document.getElementById('emailsuccessmsg').style.display='block';},function(){l.style.display='none';alert('Thank you!');document.getElementById('divemailpopup').classList.remove('show');document.body.style.overflow='auto';});};
document.addEventListener('keydown',function(e){if(e.key==='Escape'){document.getElementById('divemailpopup').classList.remove('show');document.body.style.overflow='auto';}});
</script>`;
}

function getScripts() {
  return `
<div id="menu-backdrop" class="backdrop-menu"></div>
<script src="../javascript.js"></script>
<script src="../assets/scripts/script.js"></script>
</body></html>`;
}

// ═══════════════════════════════════════════════════
// PAGE 1: STAFF MANAGEMENT (Orange/Warm Theme)
// ═══════════════════════════════════════════════════

const staffCSS = `
/* Staff Management — Orange/Warm Theme */
.stf{background:#fff;min-height:100vh;}
.stf-hero{background:linear-gradient(135deg,#1a0f00 0%,#7c2d12 40%,#ea580c 100%);padding:80px 24px 90px;position:relative;overflow:hidden;}
.stf-hero::after{content:'';position:absolute;bottom:0;left:0;right:0;height:80px;background:linear-gradient(to top,#fff,transparent);}
.stf-hero-grid{max-width:1200px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:center;position:relative;z-index:2;}
.stf-hero-badge{display:inline-block;background:rgba(255,255,255,.15);color:#fff;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:2.5px;padding:8px 18px;border-radius:6px;margin-bottom:24px;backdrop-filter:blur(4px);}
.stf-hero h1{font-size:42px;font-weight:900;color:#fff;line-height:1.15;margin:0 0 20px;}
.stf-hero h1 .hl{color:#fbbf24;}
.stf-hero p{font-size:17px;color:rgba(255,255,255,.8);line-height:1.75;margin:0 0 32px;}
.stf-hero-mockup{background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.12);border-radius:20px;padding:32px;backdrop-filter:blur(8px);}
.stf-mockup-header{display:flex;align-items:center;gap:10px;margin-bottom:20px;}
.stf-mockup-dot{width:12px;height:12px;border-radius:50%;}
.stf-mockup-row{display:flex;align-items:center;gap:12px;padding:12px 16px;background:rgba(255,255,255,.06);border-radius:10px;margin-bottom:8px;}
.stf-mockup-avatar{width:36px;height:36px;border-radius:50%;background:rgba(255,255,255,.15);display:flex;align-items:center;justify-content:center;color:#fff;font-size:13px;font-weight:700;}
.stf-mockup-text{flex:1;}
.stf-mockup-text span{display:block;font-size:13px;color:rgba(255,255,255,.8);font-weight:600;}
.stf-mockup-text small{font-size:11px;color:rgba(255,255,255,.4);}
.stf-mockup-badge{font-size:10px;padding:4px 10px;border-radius:20px;font-weight:600;}

/* Stats strip */
.stf-stats{background:#fff;border-bottom:1px solid #e5e7eb;padding:36px 24px;}
.stf-stats-grid{max-width:1100px;margin:0 auto;display:grid;grid-template-columns:repeat(4,1fr);gap:24px;text-align:center;}
.stf-stat-num{font-size:36px;font-weight:900;color:#ea580c;}
.stf-stat-label{font-size:13px;color:#6b7280;margin-top:4px;}

/* Feature blocks — alternating left/right with mockup cards */
.stf-feature{padding:80px 24px;}
.stf-feature-grid{max-width:1100px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:center;}
.stf-feature-grid.rev{direction:rtl;}
.stf-feature-grid.rev>*{direction:ltr;}
.stf-tag{font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:2.5px;margin-bottom:12px;display:block;color:#ea580c;}
.stf-title{font-size:30px;font-weight:900;color:#0f172a;line-height:1.2;margin:0 0 16px;}
.stf-desc{font-size:15px;color:#64748b;line-height:1.8;margin:0 0 20px;}
.stf-list{list-style:none;padding:0;margin:0;}
.stf-list li{font-size:14px;color:#475569;padding:8px 0 8px 24px;position:relative;line-height:1.6;}
.stf-list li::before{content:'✓';position:absolute;left:0;top:8px;color:#ea580c;font-weight:700;}
.stf-mockup-card{background:#f8fafc;border:1.5px solid #e2e8f0;border-radius:16px;padding:24px;min-height:240px;}

/* Grid features — 2x3 */
.stf-grid-section{padding:80px 24px;background:#f8fafc;}
.stf-grid-inner{max-width:1100px;margin:0 auto;}
.stf-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;}
.stf-grid-card{background:#fff;border-radius:16px;padding:28px;border:1.5px solid #e2e8f0;transition:all .25s;}
.stf-grid-card:hover{border-color:#ea580c;box-shadow:0 8px 30px rgba(234,88,12,.1);transform:translateY(-4px);}
.stf-grid-card i{font-size:32px;color:#ea580c;margin-bottom:14px;display:block;}
.stf-grid-card h4{font-size:16px;font-weight:700;color:#0f172a;margin:0 0 8px;}
.stf-grid-card p{font-size:13.5px;color:#64748b;line-height:1.7;margin:0;}

/* CTA */
.stf-cta{padding:80px 24px;background:linear-gradient(135deg,#7c2d12,#ea580c);text-align:center;}
.stf-cta h2{font-size:34px;font-weight:900;color:#fff;margin:0 0 16px;}
.stf-cta p{font-size:17px;color:rgba(255,255,255,.85);margin:0 0 32px;line-height:1.7;}

/* FAQ */
.stf-faq{padding:80px 24px;background:#fff;}
.stf-faq-inner{max-width:1100px;margin:0 auto;}
.stf-faq-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px;}
.stf-faq-item{background:#f8fafc;border:1.5px solid #e2e8f0;border-radius:14px;overflow:hidden;transition:border-color .2s;}
.stf-faq-item:hover{border-color:#ea580c;}
.stf-faq-item summary{padding:18px 22px;font-size:15px;font-weight:600;color:#0f172a;cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center;}
.stf-faq-item summary::-webkit-details-marker{display:none;}
.stf-faq-item summary .arr{width:28px;height:28px;background:#fff3e0;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:14px;color:#ea580c;transition:transform .2s;flex-shrink:0;}
.stf-faq-item[open] summary .arr{transform:rotate(45deg);}
.stf-faq-item .fb{padding:0 22px 18px;font-size:14px;color:#64748b;line-height:1.8;}

@media(max-width:992px){.stf-hero-grid,.stf-feature-grid{grid-template-columns:1fr;}.stf-grid{grid-template-columns:1fr 1fr;}.stf-faq-grid{grid-template-columns:1fr;}}
@media(max-width:576px){.stf-hero h1{font-size:28px;}.stf-grid{grid-template-columns:1fr;}.stf-stats-grid{grid-template-columns:1fr 1fr;}}
`;

const staffBody = `
<div class="stf">
<section class="stf-hero">
  <div class="stf-hero-grid">
    <div>
      <span class="stf-hero-badge">STAFF MANAGEMENT SOFTWARE</span>
      <h1>Manage Your Gym <span class="hl">Team</span> from One Place</h1>
      <p>Managing a gym team involves more than keeping staff records. You need to manage roles, schedules, attendance, trainers, and performance — while making sure everyone has access to the right information.</p>
      <button class="mm-btn mm-btn-orange magnetic-btn open-modal-btn">Get Your Free Demo <i class="fa fa-arrow-up"></i></button>
    </div>
    <div class="stf-hero-mockup">
      <div class="stf-mockup-header"><div class="stf-mockup-dot" style="background:#ef4444;"></div><div class="stf-mockup-dot" style="background:#fbbf24;"></div><div class="stf-mockup-dot" style="background:#22c55e;"></div><span style="color:rgba(255,255,255,.5);font-size:12px;margin-left:auto;">Staff Dashboard</span></div>
      <div class="stf-mockup-row"><div class="stf-mockup-avatar">JS</div><div class="stf-mockup-text"><span>John Smith</span><small>Manager · Management</small></div><span class="stf-mockup-badge" style="background:rgba(34,197,94,.2);color:#4ade80;">Active</span></div>
      <div class="stf-mockup-row"><div class="stf-mockup-avatar">PS</div><div class="stf-mockup-text"><span>Priya Sharma</span><small>Trainer · Training</small></div><span class="stf-mockup-badge" style="background:rgba(34,197,94,.2);color:#4ade80;">Active</span></div>
      <div class="stf-mockup-row"><div class="stf-mockup-avatar">RV</div><div class="stf-mockup-text"><span>Rahul Verma</span><small>Fitness Instructor · Training</small></div><span class="stf-mockup-badge" style="background:rgba(34,197,94,.2);color:#4ade80;">Active</span></div>
      <div class="stf-mockup-row"><div class="stf-mockup-avatar">AP</div><div class="stf-mockup-text"><span>Anita Patel</span><small>Sales Executive · Sales</small></div><span class="stf-mockup-badge" style="background:rgba(251,191,36,.2);color:#fbbf24;">On Leave</span></div>
    </div>
  </div>
</section>

<section class="stf-stats">
  <div class="stf-stats-grid">
    <div><div class="stf-stat-num">500+</div><div class="stf-stat-label">Gyms Using Gymex</div></div>
    <div><div class="stf-stat-num">40%</div><div class="stf-stat-label">Less Admin Work</div></div>
    <div><div class="stf-stat-num">100%</div><div class="stf-stat-label">Role-Based Access</div></div>
    <div><div class="stf-stat-num">24/7</div><div class="stf-stat-label">Cloud Access</div></div>
  </div>
</section>

<section class="stf-feature" style="background:#fff;">
  <div class="stf-feature-grid">
    <div>
      <span class="stf-tag">Staff Profiles</span>
      <h2 class="stf-title">Gymex Staff Management Software Brings Everything Together</h2>
      <p class="stf-desc">Gymex Staff Management Software brings these everyday tasks together in one connected platform, helping gym owners and managers organize their teams, reduce manual work, and keep daily operations running smoothly.</p>
      <ul class="stf-list">
        <li>Centralized staff directory with roles and departments</li>
        <li>Qualification and certification tracking</li>
        <li>Contact details and emergency information</li>
        <li>Performance history and notes</li>
      </ul>
    </div>
    <div class="stf-mockup-card" style="background:linear-gradient(135deg,#fff7ed,#ffedd5);border-color:#fed7aa;">
      <div style="display:flex;align-items:center;gap:14px;margin-bottom:18px;"><div style="width:48px;height:48px;background:#ea580c;border-radius:14px;display:flex;align-items:center;justify-content:center;"><i class="fa fa-users" style="color:#fff;font-size:20px;"></i></div><div><h4 style="margin:0;font-size:16px;font-weight:700;">Staff Directory</h4><p style="margin:0;font-size:12px;color:#92400e;">12 active members</p></div></div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
        <div style="background:#fff;border-radius:10px;padding:14px;text-align:center;"><div style="font-size:22px;font-weight:800;color:#ea580c;">8</div><div style="font-size:11px;color:#92400e;">Trainers</div></div>
        <div style="background:#fff;border-radius:10px;padding:14px;text-align:center;"><div style="font-size:22px;font-weight:800;color:#ea580c;">2</div><div style="font-size:11px;color:#92400e;">Sales</div></div>
        <div style="background:#fff;border-radius:10px;padding:14px;text-align:center;"><div style="font-size:22px;font-weight:800;color:#ea580c;">1</div><div style="font-size:11px;color:#92400e;">Front Desk</div></div>
        <div style="background:#fff;border-radius:10px;padding:14px;text-align:center;"><div style="font-size:22px;font-weight:800;color:#ea580c;">1</div><div style="font-size:11px;color:#92400e;">Manager</div></div>
      </div>
    </div>
  </div>
</section>

<section class="stf-feature" style="background:#f8fafc;">
  <div class="stf-feature-grid rev">
    <div>
      <span class="stf-tag">Roles &amp; Permissions</span>
      <h2 class="stf-title">Control Who Sees What</h2>
      <p class="stf-desc">Define roles for trainers, front-desk staff, sales teams, and managers. Each role gets exactly the access it needs — nothing more, nothing less.</p>
      <ul class="stf-list">
        <li>Create custom roles with specific permissions</li>
        <li>Limit access to sensitive financial data</li>
        <li>Allow trainers to view schedules but not invoices</li>
        <li>Audit trail for all permission changes</li>
      </ul>
    </div>
    <div class="stf-mockup-card" style="background:linear-gradient(135deg,#fef2f2,#fee2e2);border-color:#fecaca;">
      <h4 style="font-size:15px;font-weight:700;margin:0 0 14px;">Trainer Permissions</h4>
      <div style="display:flex;flex-direction:column;gap:10px;">
        <div style="display:flex;align-items:center;justify-content:space-between;padding:10px 14px;background:#fff;border-radius:8px;"><span style="font-size:13px;">View Members</span><span style="color:#22c55e;font-size:16px;">✓</span></div>
        <div style="display:flex;align-items:center;justify-content:space-between;padding:10px 14px;background:#fff;border-radius:8px;"><span style="font-size:13px;">Manage Attendance</span><span style="color:#22c55e;font-size:16px;">✓</span></div>
        <div style="display:flex;align-items:center;justify-content:space-between;padding:10px 14px;background:#fff;border-radius:8px;"><span style="font-size:13px;">Create Invoices</span><span style="color:#ef4444;font-size:16px;">✕</span></div>
        <div style="display:flex;align-items:center;justify-content:space-between;padding:10px 14px;background:#fff;border-radius:8px;"><span style="font-size:13px;">View Reports</span><span style="color:#ef4444;font-size:16px;">✕</span></div>
        <div style="display:flex;align-items:center;justify-content:space-between;padding:10px 14px;background:#fff;border-radius:8px;"><span style="font-size:13px;">Manage Staff</span><span style="color:#ef4444;font-size:16px;">✕</span></div>
      </div>
    </div>
  </div>
</section>

<section class="stf-grid-section">
  <div class="stf-grid-inner">
    <span class="stf-tag">Everything You Need</span>
    <h2 class="stf-title" style="margin-bottom:40px;">Built for Performance</h2>
    <div class="stf-grid">
      <div class="stf-grid-card"><i class="fa fa-clock-o"></i><h4>Attendance Tracking</h4><p>Track check-ins, work hours, overtime, and leave with automatic logs.</p></div>
      <div class="stf-grid-card"><i class="fa fa-calendar"></i><h4>Schedule Management</h4><p>Create shift schedules, assign trainers to classes, and manage availability.</p></div>
      <div class="stf-grid-card"><i class="fa fa-money"></i><h4>Payroll &amp; Commission</h4><p>Auto-calculate salaries, bonuses, and trainer commissions from membership sales.</p></div>
      <div class="stf-grid-card"><i class="fa fa-star"></i><h4>Performance Reviews</h4><p>Track member feedback, class ratings, and sales targets per staff member.</p></div>
      <div class="stf-grid-card"><i class="fa fa-bell"></i><h4>Shift Reminders</h4><p>Automatic notifications for upcoming shifts, schedule changes, and pending tasks.</p></div>
      <div class="stf-grid-card"><i class="fa fa-bar-chart"></i><h4>Staff Reports</h4><p>Detailed reports on attendance, performance, hours worked, and commission earned.</p></div>
    </div>
  </div>
</section>

<section class="stf-cta">
  <div style="max-width:800px;margin:0 auto;">
    <h2>Organize Your Team. Grow Your Gym.</h2>
    <p>Your staff is your greatest asset. Give them the tools to perform better while reducing the admin burden on yourself.</p>
    <button class="mm-btn mm-btn-orange magnetic-btn open-modal-btn" style="font-size:16px;padding:18px 40px;">Get Your Free Demo <i class="fa fa-arrow-up" style="font-size:14px;"></i></button>
  </div>
</section>

<section class="stf-faq">
  <div class="stf-faq-inner">
    <h2 class="stf-title" style="text-align:center;margin-bottom:40px;">Frequently Asked Questions</h2>
    <div class="stf-faq-grid">
      <div>
        <details class="stf-faq-item"><summary>What is gym staff management software?<span class="arr">+</span></summary><div class="fb">Gym staff management software helps gym owners organize employee information, roles, schedules, attendance, performance, and payroll from one connected platform.</div></details>
        <details class="stf-faq-item" style="margin-top:12px;"><summary>Can I set different permissions for trainers and admin staff?<span class="arr">+</span></summary><div class="fb">Yes. Gymex lets you create custom roles with specific permissions so each team member sees only what they need.</div></details>
        <details class="stf-faq-item" style="margin-top:12px;"><summary>How does staff scheduling work?<span class="arr">+</span></summary><div class="fb">You can create shift schedules, assign trainers to classes, manage availability, and send automatic reminders for upcoming shifts.</div></details>
      </div>
      <div>
        <details class="stf-faq-item"><summary>Can I track staff attendance automatically?<span class="arr">+</span></summary><div class="fb">Yes. Gymex tracks check-ins, work hours, overtime, and leave with automatic logging and reporting.</div></details>
        <details class="stf-faq-item" style="margin-top:12px;"><summary>Does Gymex handle payroll and commissions?<span class="arr">+</span></summary><div class="fb">Yes. Auto-calculate salaries, bonuses, and trainer commissions from membership sales and class attendance.</div></details>
        <details class="stf-faq-item" style="margin-top:12px;"><summary>Can staff access their schedules from mobile?<span class="arr">+</span></summary><div class="fb">Yes. Staff can view their schedules, attendance, and shift details through the Gymex mobile app.</div></details>
      </div>
    </div>
  </div>
</section>
</div>`;

// ═══════════════════════════════════════════════════
// PAGE 2: MARKETING MANAGEMENT (Green/Emerald Theme)
// ═══════════════════════════════════════════════════

const marketingCSS = `
/* Marketing Management — Green/Emerald Theme */
.mkt{background:#fff;min-height:100vh;}
.mkt-hero{background:linear-gradient(135deg,#052e16 0%,#166534 45%,#22c55e 100%);padding:80px 24px 90px;position:relative;overflow:hidden;}
.mkt-hero::before{content:'';position:absolute;top:-100px;right:-100px;width:400px;height:400px;background:radial-gradient(circle,rgba(255,255,255,.08),transparent 70%);border-radius:50%;}
.mkt-hero::after{content:'';position:absolute;bottom:0;left:0;right:0;height:80px;background:linear-gradient(to top,#fff,transparent);}
.mkt-hero-grid{max-width:1200px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:center;position:relative;z-index:2;}
.mkt-hero-badge{display:inline-block;background:rgba(255,255,255,.15);color:#fff;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:2.5px;padding:8px 18px;border-radius:6px;margin-bottom:24px;backdrop-filter:blur(4px);}
.mkt-hero h1{font-size:42px;font-weight:900;color:#fff;line-height:1.15;margin:0 0 20px;}
.mkt-hero h1 .hl{color:#fde047;}
.mkt-hero p{font-size:17px;color:rgba(255,255,255,.8);line-height:1.75;margin:0 0 32px;}
.mkt-hero-visual{background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.12);border-radius:20px;padding:40px;text-align:center;backdrop-filter:blur(8px);}
.mkt-hero-visual i{font-size:72px;color:rgba(255,255,255,.25);}
.mkt-hero-visual p{font-size:13px;color:rgba(255,255,255,.45);margin-top:14px;}

/* Stats */
.mkt-stats{background:#fff;border-bottom:1px solid #e5e7eb;padding:36px 24px;}
.mkt-stats-grid{max-width:1100px;margin:0 auto;display:grid;grid-template-columns:repeat(4,1fr);gap:24px;text-align:center;}
.mkt-stat-num{font-size:36px;font-weight:900;color:#16a34a;}
.mkt-stat-label{font-size:13px;color:#6b7280;margin-top:4px;}

/* Problem — Horizontal warning banner cards */
.mkt-problem{padding:80px 24px;background:#f8fafc;}
.mkt-problem-inner{max-width:1100px;margin:0 auto;}
.mkt-tag{font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:2.5px;margin-bottom:12px;display:block;color:#16a34a;}
.mkt-title{font-size:34px;font-weight:900;color:#0f172a;line-height:1.2;margin:0 0 16px;}
.mkt-desc{font-size:16px;color:#64748b;line-height:1.8;max-width:640px;margin:0 0 48px;}
.mkt-banner-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:16px;}
.mkt-banner{display:flex;align-items:center;gap:16px;padding:20px 24px;background:#fff;border:1.5px solid #dcfce7;border-radius:14px;transition:all .2s;}
.mkt-banner:hover{border-color:#16a34a;transform:translateY(-2px);box-shadow:0 6px 20px rgba(22,163,74,.08);}
.mkt-banner-icon{width:44px;height:44px;background:#f0fdf4;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:20px;flex-shrink:0;}
.mkt-banner p{font-size:14px;color:#475569;line-height:1.6;margin:0;}

/* Channels — 2-col with icon rows */
.mkt-channels{padding:80px 24px;background:#fff;}
.mkt-channels-inner{max-width:1100px;margin:0 auto;}
.mkt-channel-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:16px;}
.mkt-channel-card{display:flex;align-items:center;gap:16px;padding:18px 20px;background:#f0fdf4;border:1.5px solid #bbf7d0;border-radius:12px;transition:all .2s;}
.mkt-channel-card:hover{background:#dcfce7;border-color:#16a34a;}
.mkt-channel-card i{font-size:22px;color:#16a34a;width:24px;text-align:center;}
.mkt-channel-card h4{font-size:14px;font-weight:700;color:#0f172a;margin:0;}
.mkt-channel-card p{font-size:12px;color:#64748b;margin:2px 0 0;}

/* Campaign — Timeline */
.mkt-campaign{padding:80px 24px;background:#f8fafc;}
.mkt-campaign-inner{max-width:1100px;margin:0 auto;}
.mkt-timeline{position:relative;max-width:700px;margin:0 auto;}
.mkt-tl-step{display:flex;gap:24px;padding-bottom:36px;position:relative;}
.mkt-tl-step:last-child{padding-bottom:0;}
.mkt-tl-dot{width:48px;height:48px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-size:18px;font-weight:800;flex-shrink:0;position:relative;z-index:2;}
.mkt-tl-dot.g1{background:linear-gradient(135deg,#166534,#22c55e);}
.mkt-tl-dot.g2{background:linear-gradient(135deg,#15803d,#4ade80);}
.mkt-tl-dot.g3{background:linear-gradient(135deg,#16a34a,#86efac);}
.mkt-tl-dot.g4{background:linear-gradient(135deg,#4ade80,#bbf7d0);color:#166534;}
.mkt-tl-content{flex:1;padding-top:8px;}
.mkt-tl-content h4{font-size:17px;font-weight:700;color:#0f172a;margin:0 0 6px;}
.mkt-tl-content p{font-size:14px;color:#64748b;line-height:1.7;margin:0;}
.mkt-tl-line{position:absolute;left:24px;top:48px;width:2px;height:calc(100% - 48px);background:linear-gradient(180deg,#16a34a,#e2e8f0);z-index:1;}
.mkt-tl-step:last-child .mkt-tl-line{display:none;}

/* Analytics — Dark green section with 4 circle metrics */
.mkt-analytics{padding:80px 24px;background:#052e16;color:#fff;}
.mkt-analytics-inner{max-width:1100px;margin:0 auto;}
.mkt-analytics .mkt-tag{color:#4ade80;}
.mkt-analytics .mkt-title{color:#fff;}
.mkt-circle-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;margin-top:40px;}
.mkt-circle{text-align:center;}
.mkt-circle-ring{width:120px;height:120px;border-radius:50%;border:6px solid rgba(255,255,255,.15);display:flex;align-items:center;justify-content:center;margin:0 auto 16px;background:rgba(255,255,255,.05);}
.mkt-circle-ring span{font-size:28px;font-weight:900;color:#4ade80;}
.mkt-circle h4{font-size:14px;font-weight:600;color:#fff;margin:0 0 4px;}
.mkt-circle p{font-size:12px;color:rgba(255,255,255,.5);}

/* CTA */
.mkt-cta{padding:80px 24px;background:linear-gradient(135deg,#166534,#22c55e);text-align:center;}
.mkt-cta h2{font-size:34px;font-weight:900;color:#fff;margin:0 0 16px;}
.mkt-cta p{font-size:17px;color:rgba(255,255,255,.85);margin:0 0 32px;line-height:1.7;}

/* FAQ */
.mkt-faq{padding:80px 24px;background:#fff;}
.mkt-faq-inner{max-width:1100px;margin:0 auto;}
.mkt-faq-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px;}
.mkt-faq-item{background:#f8fafc;border:1.5px solid #e2e8f0;border-radius:14px;overflow:hidden;transition:border-color .2s;}
.mkt-faq-item:hover{border-color:#16a34a;}
.mkt-faq-item summary{padding:18px 22px;font-size:15px;font-weight:600;color:#0f172a;cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center;}
.mkt-faq-item summary::-webkit-details-marker{display:none;}
.mkt-faq-item summary .arr{width:28px;height:28px;background:#f0fdf4;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:14px;color:#16a34a;transition:transform .2s;flex-shrink:0;}
.mkt-faq-item[open] summary .arr{transform:rotate(45deg);}
.mkt-faq-item .fb{padding:0 22px 18px;font-size:14px;color:#64748b;line-height:1.8;}

@media(max-width:992px){.mkt-hero-grid{grid-template-columns:1fr;}.mkt-banner-grid{grid-template-columns:1fr;}.mkt-channel-grid{grid-template-columns:1fr;}.mkt-circle-grid{grid-template-columns:1fr 1fr;}.mkt-faq-grid{grid-template-columns:1fr;}}
@media(max-width:576px){.mkt-hero h1{font-size:28px;}.mkt-stats-grid{grid-template-columns:1fr 1fr;}.mkt-circle-grid{grid-template-columns:1fr;}}
`;

const marketingBody = `
<div class="mkt">
<section class="mkt-hero">
  <div class="mkt-hero-grid">
    <div>
      <span class="mkt-hero-badge">MARKETING MANAGEMENT SOFTWARE</span>
      <h1>Gym <span class="hl">Marketing</span> Software That Attracts &amp; Retains Members</h1>
      <p>Gym marketing is not just about posting on social media. Gymex helps you run targeted campaigns, send automated reminders, and track which efforts bring real members.</p>
      <button class="mm-btn mm-btn-orange magnetic-btn open-modal-btn">Get Your Free Demo <i class="fa fa-arrow-up"></i></button>
    </div>
    <div class="mkt-hero-visual">
      <i class="fa fa-bullhorn"></i>
      <p>Marketing Campaign Dashboard</p>
    </div>
  </div>
</section>

<section class="mkt-stats">
  <div class="mkt-stats-grid">
    <div><div class="mkt-stat-num">3x</div><div class="mkt-stat-label">More Campaign Reach</div></div>
    <div><div class="mkt-stat-num">45%</div><div class="mkt-stat-label">Higher Retention</div></div>
    <div><div class="mkt-stat-num">6+</div><div class="mkt-stat-label">Channels Supported</div></div>
    <div><div class="mkt-stat-num">500+</div><div class="mkt-stat-label">Gyms Growing Faster</div></div>
  </div>
</section>

<section class="mkt-problem">
  <div class="mkt-problem-inner">
    <span class="mkt-tag">The Problem</span>
    <h2 class="mkt-title">Manual Marketing Burns Time and Money</h2>
    <p class="mkt-desc">Posting randomly, sending bulk messages, and hoping something works is not a strategy. You need data-driven marketing that converts.</p>
    <div class="mkt-banner-grid">
      <div class="mkt-banner"><div class="mkt-banner-icon">💸</div><p>Spending on ads without knowing which channel brings actual members</p></div>
      <div class="mkt-banner"><div class="mkt-banner-icon">📱</div><p>Sending the same message to every lead regardless of interest or stage</p></div>
      <div class="mkt-banner"><div class="mkt-banner-icon">😰</div><p>No way to measure campaign ROI or compare channel performance</p></div>
      <div class="mkt-banner"><div class="mkt-banner-icon">📋</div><p>Manually tracking promotions, offers, and member engagement</p></div>
    </div>
  </div>
</section>

<section class="mkt-channels">
  <div class="mkt-channels-inner">
    <span class="mkt-tag">Marketing Channels</span>
    <h2 class="mkt-title">Reach Members Where They Are</h2>
    <p class="mkt-desc">Run campaigns across multiple channels from one platform — and track exactly which ones work.</p>
    <div class="mkt-channel-grid">
      <div class="mkt-channel-card"><i class="fa fa-whatsapp"></i><div><h4>WhatsApp Campaigns</h4><p>Broadcast offers, reminders, and updates to member lists</p></div></div>
      <div class="mkt-channel-card"><i class="fa fa-envelope"></i><div><h4>Email Marketing</h4><p>Targeted newsletters, drip campaigns, and automated sequences</p></div></div>
      <div class="mkt-channel-card"><i class="fa fa-commenting"></i><div><h4>SMS Campaigns</h4><p>Promotional messages, renewal reminders, and event alerts</p></div></div>
      <div class="mkt-channel-card"><i class="fa fa-bullhorn"></i><div><h4>Social Media</h4><p>Track social campaigns and measure engagement and conversions</p></div></div>
      <div class="mkt-channel-card"><i class="fa fa-google"></i><div><h4>Google Ads</h4><p>Connect ad spend to actual lead generation and membership sign-ups</p></div></div>
      <div class="mkt-channel-card"><i class="fa fa-handshake-o"></i><div><h4>Referral Programs</h4><p>Automate member referral rewards and track referral performance</p></div></div>
    </div>
  </div>
</section>

<section class="mkt-campaign">
  <div class="mkt-campaign-inner">
    <span class="mkt-tag">Campaign Flow</span>
    <h2 class="mkt-title">From Idea to Conversion — Step by Step</h2>
    <p class="mkt-desc">Plan, launch, track, and optimize your marketing campaigns with a clear workflow.</p>
    <div class="mkt-timeline">
      <div class="mkt-tl-step"><div class="mkt-tl-dot g1">1</div><div class="mkt-tl-content"><h4>Plan Your Campaign</h4><p>Define your audience, message, channel, and goals before launch.</p></div><div class="mkt-tl-line"></div></div>
      <div class="mkt-tl-step"><div class="mkt-tl-dot g2">2</div><div class="mkt-tl-content"><h4>Launch Across Channels</h4><p>Send your campaign via WhatsApp, email, SMS, or social — all from Gymex.</p></div><div class="mkt-tl-line"></div></div>
      <div class="mkt-tl-step"><div class="mkt-tl-dot g3">3</div><div class="mkt-tl-content"><h4>Track Engagement</h4><p>See who opened, clicked, replied, or visited — in real time.</p></div><div class="mkt-tl-line"></div></div>
      <div class="mkt-tl-step"><div class="mkt-tl-dot g4">4</div><div class="mkt-tl-content"><h4>Convert &amp; Measure ROI</h4><p>Track which campaigns generate actual memberships and optimize spend.</p></div></div>
    </div>
  </div>
</section>

<section class="mkt-analytics">
  <div class="mkt-analytics-inner">
    <span class="mkt-tag">Analytics</span>
    <h2 class="mkt-title">Know What Works, Cut What Doesn't</h2>
    <div class="mkt-circle-grid">
      <div class="mkt-circle"><div class="mkt-circle-ring"><span>ROI</span></div><h4>Campaign ROI</h4><p>Revenue per rupee spent</p></div>
      <div class="mkt-circle"><div class="mkt-circle-ring"><span>CVR</span></div><h4>Conversion Rate</h4><p>Campaign to membership</p></div>
      <div class="mkt-circle"><div class="mkt-circle-ring"><span>ENG</span></div><h4>Engagement</h4><p>Opens, clicks, replies</p></div>
      <div class="mkt-circle"><div class="mkt-circle-ring"><span>RET</span></div><h4>Retention Impact</h4><p>Campaign-driven retention</p></div>
    </div>
  </div>
</section>

<section class="mkt-cta">
  <div style="max-width:800px;margin:0 auto;">
    <h2>Grow Your Gym with Smarter Marketing</h2>
    <p>Stop guessing. Start measuring. Run campaigns that actually bring in new members.</p>
    <button class="mm-btn mm-btn-orange magnetic-btn open-modal-btn" style="font-size:16px;padding:18px 40px;">Get Your Free Demo <i class="fa fa-arrow-up" style="font-size:14px;"></i></button>
  </div>
</section>

<section class="mkt-faq">
  <div class="mkt-faq-inner">
    <h2 class="mkt-title" style="text-align:center;margin-bottom:40px;">Frequently Asked Questions</h2>
    <div class="mkt-faq-grid">
      <div>
        <details class="mkt-faq-item"><summary>What marketing channels does Gymex support?<span class="arr">+</span></summary><div class="fb">Gymex supports WhatsApp, email, SMS, social media campaigns, Google Ads tracking, and referral programs — all from one platform.</div></details>
        <details class="mkt-faq-item" style="margin-top:12px;"><summary>Can I track which campaign brings the most members?<span class="arr">+</span></summary><div class="fb">Yes. Gymex tracks lead sources and their conversion to membership, so you can compare ROI across campaigns and channels.</div></details>
        <details class="mkt-faq-item" style="margin-top:12px;"><summary>How do automated member retention campaigns work?<span class="arr">+</span></summary><div class="fb">Set up automated messages for renewals, birthday offers, inactivity alerts, and membership expiry reminders.</div></details>
      </div>
      <div>
        <details class="mkt-faq-item"><summary>Can I run WhatsApp bulk campaigns?<span class="arr">+</span></summary><div class="fb">Yes. Send promotional offers, event announcements, and renewal reminders to member lists via WhatsApp.</div></details>
        <details class="mkt-faq-item" style="margin-top:12px;"><summary>Do I need separate tools for email and SMS?<span class="arr">+</span></summary><div class="fb">No. Gymex handles WhatsApp, email, and SMS campaigns from one integrated platform.</div></details>
        <details class="mkt-faq-item" style="margin-top:12px;"><summary>Can I segment my audience for targeted campaigns?<span class="arr">+</span></summary><div class="fb">Yes. Segment by membership type, activity level, location, engagement history, or custom tags.</div></details>
      </div>
    </div>
  </div>
</section>
</div>`;

// ═══════════════════════════════════════════════════
// PAGE 3: MEMBER MANAGEMENT (Purple/Violet Theme)
// ═══════════════════════════════════════════════════

const memberCSS = `
/* Member Management — Purple/Violet Theme */
.mem{background:#fff;min-height:100vh;}
.mem-hero{background:linear-gradient(135deg,#1e1033 0%,#581c87 45%,#a855f7 100%);padding:80px 24px 90px;position:relative;overflow:hidden;}
.mem-hero::before{content:'';position:absolute;top:50%;left:-100px;width:300px;height:300px;background:radial-gradient(circle,rgba(168,85,247,.2),transparent 70%);border-radius:50%;}
.mem-hero::after{content:'';position:absolute;bottom:0;left:0;right:0;height:80px;background:linear-gradient(to top,#fff,transparent);}
.mem-hero-grid{max-width:1200px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:center;position:relative;z-index:2;}
.mem-hero-badge{display:inline-block;background:rgba(255,255,255,.15);color:#fff;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:2.5px;padding:8px 18px;border-radius:6px;margin-bottom:24px;backdrop-filter:blur(4px);}
.mem-hero h1{font-size:42px;font-weight:900;color:#fff;line-height:1.15;margin:0 0 20px;}
.mem-hero h1 .hl{color:#c084fc;}
.mem-hero p{font-size:17px;color:rgba(255,255,255,.8);line-height:1.75;margin:0 0 32px;}
.mem-hero-cards{display:flex;flex-direction:column;gap:12px;}
.mem-member-card{background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.12);border-radius:14px;padding:16px 20px;display:flex;align-items:center;gap:14px;backdrop-filter:blur(6px);}
.mem-member-avatar{width:42px;height:42px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:700;color:#fff;flex-shrink:0;}
.mem-member-info{flex:1;}
.mem-member-info span{display:block;font-size:13px;color:rgba(255,255,255,.85);font-weight:600;}
.mem-member-info small{font-size:11px;color:rgba(255,255,255,.4);}
.mem-member-badge{font-size:10px;padding:4px 10px;border-radius:20px;font-weight:600;}

/* Stats */
.mem-stats{background:#fff;border-bottom:1px solid #e5e7eb;padding:36px 24px;}
.mem-stats-grid{max-width:1100px;margin:0 auto;display:grid;grid-template-columns:repeat(4,1fr);gap:24px;text-align:center;}
.mem-stat-num{font-size:36px;font-weight:900;color:#7c3aed;}
.mem-stat-label{font-size:13px;color:#6b7280;margin-top:4px;}

/* Problem — Vertical list with purple accents */
.mem-problem{padding:80px 24px;background:#f8fafc;}
.mem-problem-inner{max-width:1100px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:start;}
.mem-tag{font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:2.5px;margin-bottom:12px;display:block;color:#7c3aed;}
.mem-title{font-size:34px;font-weight:900;color:#0f172a;line-height:1.2;margin:0 0 16px;}
.mem-desc{font-size:16px;color:#64748b;line-height:1.8;max-width:640px;margin:0 0 0;}
.mem-problem-list{display:flex;flex-direction:column;gap:14px;}
.mem-problem-item{display:flex;align-items:flex-start;gap:14px;padding:18px 20px;background:#fff;border:1.5px solid #e9d5ff;border-radius:12px;transition:all .2s;}
.mem-problem-item:hover{border-color:#7c3aed;transform:translateX(4px);}
.mem-problem-item .icon{width:36px;height:36px;background:#f5f3ff;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:16px;flex-shrink:0;}
.mem-problem-item p{font-size:14px;color:#475569;line-height:1.6;margin:0;}

/* Features — Member Journey Cards */
.mem-journey{padding:80px 24px;background:#fff;}
.mem-journey-inner{max-width:1100px;margin:0 auto;}
.mem-journey-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;}
.mem-journey-card{background:#f8fafc;border-radius:16px;padding:28px;border:1.5px solid #e9d5ff;transition:all .25s;position:relative;overflow:hidden;}
.mem-journey-card::before{content:'';position:absolute;top:0;left:0;right:0;height:4px;background:linear-gradient(90deg,#7c3aed,#a855f7);}
.mem-journey-card:hover{border-color:#7c3aed;box-shadow:0 8px 30px rgba(124,58,237,.1);transform:translateY(-4px);}
.mem-journey-card i{font-size:32px;color:#7c3aed;margin-bottom:14px;display:block;}
.mem-journey-card h4{font-size:16px;font-weight:700;color:#0f172a;margin:0 0 8px;}
.mem-journey-card p{font-size:13.5px;color:#64748b;line-height:1.7;margin:0;}

/* Membership Plans — Pricing card style */
.mem-plans{padding:80px 24px;background:#f5f3ff;}
.mem-plans-inner{max-width:1100px;margin:0 auto;}
.mem-plan-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;}
.mem-plan-card{background:#fff;border-radius:16px;padding:28px;text-align:center;border:1.5px solid #e9d5ff;transition:all .25s;}
.mem-plan-card.featured{border-color:#7c3aed;box-shadow:0 8px 30px rgba(124,58,237,.15);}
.mem-plan-card:hover{transform:translateY(-4px);}
.mem-plan-icon{width:56px;height:56px;border-radius:50%;display:flex;align-items:center;justify-content:center;margin:0 auto 16px;font-size:24px;color:#fff;}
.mem-plan-card h4{font-size:17px;font-weight:700;color:#0f172a;margin:0 0 8px;}
.mem-plan-card p{font-size:13px;color:#64748b;line-height:1.6;margin:0;}

/* Analytics — Purple dark section with progress bars */
.mem-analytics{padding:80px 24px;background:#1e1033;color:#fff;}
.mem-analytics-inner{max-width:1100px;margin:0 auto;}
.mem-analytics .mem-tag{color:#c084fc;}
.mem-analytics .mem-title{color:#fff;}
.mem-progress-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:24px;margin-top:40px;}
.mem-progress-item{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:14px;padding:20px 24px;}
.mem-progress-item h4{font-size:14px;font-weight:600;color:#fff;margin:0 0 10px;}
.mem-progress-bar{height:8px;background:rgba(255,255,255,.1);border-radius:4px;overflow:hidden;}
.mem-progress-fill{height:100%;border-radius:4px;transition:width 1.5s ease;}
.mem-progress-label{display:flex;justify-content:space-between;margin-top:6px;}
.mem-progress-label span{font-size:11px;color:rgba(255,255,255,.5);}

/* CTA */
.mem-cta{padding:80px 24px;background:linear-gradient(135deg,#581c87,#a855f7);text-align:center;}
.mem-cta h2{font-size:34px;font-weight:900;color:#fff;margin:0 0 16px;}
.mem-cta p{font-size:17px;color:rgba(255,255,255,.85);margin:0 0 32px;line-height:1.7;}

/* FAQ */
.mem-faq{padding:80px 24px;background:#fff;}
.mem-faq-inner{max-width:1100px;margin:0 auto;}
.mem-faq-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px;}
.mem-faq-item{background:#f8fafc;border:1.5px solid #e2e8f0;border-radius:14px;overflow:hidden;transition:border-color .2s;}
.mem-faq-item:hover{border-color:#7c3aed;}
.mem-faq-item summary{padding:18px 22px;font-size:15px;font-weight:600;color:#0f172a;cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center;}
.mem-faq-item summary::-webkit-details-marker{display:none;}
.mem-faq-item summary .arr{width:28px;height:28px;background:#f5f3ff;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:14px;color:#7c3aed;transition:transform .2s;flex-shrink:0;}
.mem-faq-item[open] summary .arr{transform:rotate(45deg);}
.mem-faq-item .fb{padding:0 22px 18px;font-size:14px;color:#64748b;line-height:1.8;}

@media(max-width:992px){.mem-hero-grid,.mem-problem-inner{grid-template-columns:1fr;}.mem-journey-grid,.mem-plan-grid{grid-template-columns:1fr 1fr;}.mem-faq-grid{grid-template-columns:1fr;}.mem-progress-grid{grid-template-columns:1fr;}}
@media(max-width:576px){.mem-hero h1{font-size:28px;}.mem-journey-grid,.mem-plan-grid{grid-template-columns:1fr;}.mem-stats-grid{grid-template-columns:1fr 1fr;}}
`;

const memberBody = `
<div class="mem">
<section class="mem-hero">
  <div class="mem-hero-grid">
    <div>
      <span class="mem-hero-badge">MEMBER MANAGEMENT SOFTWARE</span>
      <h1>Everything About <span class="hl">Every Member</span> — in One Place</h1>
      <p>Stop relying on spreadsheets and separate tools. Gymex gives you a centralized system to organize member information, manage plans, track attendance, and build stronger relationships.</p>
      <button class="mm-btn mm-btn-orange magnetic-btn open-modal-btn">Get Your Free Demo <i class="fa fa-arrow-up"></i></button>
    </div>
    <div class="mem-hero-cards">
      <div class="mem-member-card"><div class="mem-member-avatar" style="background:linear-gradient(135deg,#7c3aed,#a855f7);">AK</div><div class="mem-member-info"><span>Amit Kumar</span><small>Gold Plan · Active since Jan 2024</small></div><span class="mem-member-badge" style="background:rgba(34,197,94,.2);color:#4ade80;">Active</span></div>
      <div class="mem-member-card"><div class="mem-member-avatar" style="background:linear-gradient(135deg,#2563eb,#60a5fa);">SP</div><div class="mem-member-info"><span>Sara Patel</span><small>Platinum Plan · Active since Mar 2024</small></div><span class="mem-member-badge" style="background:rgba(34,197,94,.2);color:#4ade80;">Active</span></div>
      <div class="mem-member-card"><div class="mem-member-avatar" style="background:linear-gradient(135deg,#dc2626,#f87171);">RJ</div><div class="mem-member-info"><span>Raj Joshi</span><small>Silver Plan · Expires in 5 days</small></div><span class="mem-member-badge" style="background:rgba(234,179,8,.2);color:#fbbf24;">Expiring</span></div>
      <div class="mem-member-card"><div class="mem-member-avatar" style="background:linear-gradient(135deg,#059669,#34d399);">NM</div><div class="mem-member-info"><span>Neha Mehta</span><small>Gold Plan · Last visit 12 days ago</small></div><span class="mem-member-badge" style="background:rgba(239,68,68,.2);color:#f87171;">At Risk</span></div>
    </div>
  </div>
</section>

<section class="mem-stats">
  <div class="mem-stats-grid">
    <div><div class="mem-stat-num">500+</div><div class="mem-stat-label">Gyms Managing Members</div></div>
    <div><div class="mem-stat-num">95%</div><div class="mem-stat-label">Renewal Reminders Sent</div></div>
    <div><div class="mem-stat-num">30%</div><div class="mem-stat-label">Better Retention Rates</div></div>
    <div><div class="mem-stat-num">100%</div><div class="mem-stat-label">Member Data Secure</div></div>
  </div>
</section>

<section class="mem-problem">
  <div class="mem-problem-inner">
    <div>
      <span class="mem-tag">The Challenge</span>
      <h2 class="mem-title">Managing Members Shouldn't Be This Hard</h2>
      <p class="mem-desc">Whether you run a single gym or multiple locations, keeping track of memberships, payments, attendance, and engagement across hundreds of members is overwhelming without the right system.</p>
    </div>
    <div class="mem-problem-list">
      <div class="mem-problem-item"><div class="icon">😰</div><p>Juggling spreadsheets, paper forms, and WhatsApp chats to track member details</p></div>
      <div class="mem-problem-item"><div class="icon">⏰</div><p>Missing renewal deadlines and losing members who forget to renew</p></div>
      <div class="mem-problem-item"><div class="icon">📊</div><p>No visibility into which members are at risk of leaving</p></div>
      <div class="mem-problem-item"><div class="icon">🔄</div><p>Duplicating member data across billing, attendance, and communication tools</p></div>
    </div>
  </div>
</section>

<section class="mem-journey">
  <div class="mem-journey-inner">
    <span class="mem-tag">Features</span>
    <h2 class="mem-title" style="margin-bottom:40px;">Everything You Need to Manage Every Member</h2>
    <div class="mem-journey-grid">
      <div class="mem-journey-card"><i class="fa fa-user-plus"></i><h4>Simple Sign-Up</h4><p>Fast digital registration with document upload, plan selection, and instant payment.</p></div>
      <div class="mem-journey-card"><i class="fa fa-id-card"></i><h4>Member Profiles</h4><p>Complete profiles with contact info, fitness goals, medical notes, and visit history.</p></div>
      <div class="mem-journey-card"><i class="fa fa-credit-card"></i><h4>Payment Tracking</h4><p>Track dues, renewals, auto-debit status, and payment history per member.</p></div>
      <div class="mem-journey-card"><i class="fa fa-check-square-o"></i><h4>Attendance &amp; Check-In</h4><p>Biometric, QR, or manual check-in with real-time attendance tracking.</p></div>
      <div class="mem-journey-card"><i class="fa fa-comments"></i><h4>Communication</h4><p>Send personalized messages, renewal reminders, and engagement nudges.</p></div>
      <div class="mem-journey-card"><i class="fa fa-heartbeat"></i><h4>At-Risk Alerts</h4><p>Automatic alerts for inactive members so you can intervene before they leave.</p></div>
    </div>
  </div>
</section>

<section class="mem-plans">
  <div class="mem-plans-inner">
    <span class="mem-tag">Membership Plans</span>
    <h2 class="mem-title">Manage Plans Your Way</h2>
    <p class="mem-desc" style="margin-bottom:40px;">Create, customize, and manage membership plans that fit your business model.</p>
    <div class="mem-plan-grid">
      <div class="mem-plan-card"><div class="mem-plan-icon" style="background:linear-gradient(135deg,#7c3aed,#a855f7);"><i class="fa fa-star"></i></div><h4>Flexible Plans</h4><p>Monthly, quarterly, yearly, or custom durations with auto-renewal options.</p></div>
      <div class="mem-plan-card featured"><div class="mem-plan-icon" style="background:linear-gradient(135deg,#2563eb,#60a5fa);"><i class="fa fa-users"></i></div><h4>Group &amp; Family</h4><p>Group discounts, family plans, corporate packages, and couples offers.</p></div>
      <div class="mem-plan-card"><div class="mem-plan-icon" style="background:linear-gradient(135deg,#dc2626,#f87171);"><i class="fa fa-exchange"></i></div><h4>Plan Upgrades</h4><p>Seamless plan changes with pro-rata billing and automatic adjustments.</p></div>
    </div>
  </div>
</section>

<section class="mem-analytics">
  <div class="mem-analytics-inner">
    <span class="mem-tag">Member Insights</span>
    <h2 class="mem-title">Make Decisions Using Real Member Data</h2>
    <div class="mem-progress-grid">
      <div class="mem-progress-item"><h4>Membership Renewal Rate</h4><div class="mem-progress-bar"><div class="mem-progress-fill" style="width:78%;background:linear-gradient(90deg,#7c3aed,#a855f7);"></div></div><div class="mem-progress-label"><span>78%</span><span>Target: 85%</span></div></div>
      <div class="mem-progress-item"><h4>Attendance Consistency</h4><div class="mem-progress-bar"><div class="mem-progress-fill" style="width:65%;background:linear-gradient(90deg,#2563eb,#60a5fa);"></div></div><div class="mem-progress-label"><span>65%</span><span>Target: 75%</span></div></div>
      <div class="mem-progress-item"><h4>Payment Collection Rate</h4><div class="mem-progress-bar"><div class="mem-progress-fill" style="width:92%;background:linear-gradient(90deg,#059669,#34d399);"></div></div><div class="mem-progress-label"><span>92%</span><span>Target: 95%</span></div></div>
      <div class="mem-progress-item"><h4>Member Satisfaction Score</h4><div class="mem-progress-bar"><div class="mem-progress-fill" style="width:85%;background:linear-gradient(90deg,#ea580c,#fb923c);"></div></div><div class="mem-progress-label"><span>8.5/10</span><span>Target: 9/10</span></div></div>
    </div>
  </div>
</section>

<section class="mem-cta">
  <div style="max-width:800px;margin:0 auto;">
    <h2>Build Stronger Member Relationships</h2>
    <p>Every member is unique. Give your team the tools to understand, engage, and retain every single one.</p>
    <button class="mm-btn mm-btn-orange magnetic-btn open-modal-btn" style="font-size:16px;padding:18px 40px;">Get Your Free Demo <i class="fa fa-arrow-up" style="font-size:14px;"></i></button>
  </div>
</section>

<section class="mem-faq">
  <div class="mem-faq-inner">
    <h2 class="mem-title" style="text-align:center;margin-bottom:40px;">Frequently Asked Questions</h2>
    <div class="mem-faq-grid">
      <div>
        <details class="mem-faq-item"><summary>What is gym member management software?<span class="arr">+</span></summary><div class="fb">Gym member management software helps gyms organize member profiles, track memberships, manage payments, monitor attendance, and improve retention — all from one platform.</div></details>
        <details class="mem-faq-item" style="margin-top:12px;"><summary>Can I track member attendance automatically?<span class="arr">+</span></summary><div class="fb">Yes. Gymex supports biometric, QR code, and manual check-in methods with real-time attendance tracking and reporting.</div></details>
        <details class="mem-faq-item" style="margin-top:12px;"><summary>How does Gymex help with member retention?<span class="arr">+</span></summary><div class="fb">Gymex flags at-risk members based on inactivity patterns and sends automated re-engagement messages to help bring them back.</div></details>
      </div>
      <div>
        <details class="mem-faq-item"><summary>Can I manage different membership plans?<span class="arr">+</span></summary><div class="fb">Yes. Create monthly, quarterly, yearly, group, family, and custom plans with auto-renewal and pro-rata billing.</div></details>
        <details class="mem-faq-item" style="margin-top:12px;"><summary>Can members access their own data through an app?<span class="arr">+</span></summary><div class="fb">Yes. The Gymex Member App lets members view their profile, check attendance, track payments, and book classes.</div></details>
        <details class="mem-faq-item" style="margin-top:12px;"><summary>Is member data secure in Gymex?<span class="arr">+</span></summary><div class="fb">Yes. All member data is encrypted with AES-256-GCM, stored in HIPAA-compliant infrastructure, and access is controlled by role-based permissions.</div></details>
      </div>
    </div>
  </div>
</section>
</div>`;

// ═══════════════════════════════════════════════════
// GENERATE ALL 3 PAGES
// ═══════════════════════════════════════════════════

const pages = [
  {
    dir: 'staff-management',
    file: 'staff-management/staff-management.html',
    title: 'Gym Staff Management Software | Manage Staff & Trainers | Gymex',
    desc: 'Manage gym staff, trainers, roles, attendance, schedules, performance, and payroll from one connected platform with Gymex Staff Management Software.',
    kw: 'Gym Staff Management Software, Gym Staff Management System, Staff Management Software for Gyms, Gym Employee Management Software, Gym Trainer Management Software',
    css: staffCSS,
    body: staffBody
  },
  {
    dir: 'marketing-management',
    file: 'marketing-management/marketing-management.html',
    title: 'Gym Marketing Software | WhatsApp, SMS & Email Campaigns | Gymex',
    desc: 'Run targeted gym marketing campaigns via WhatsApp, SMS, email, and social media. Track ROI and convert more leads into members with Gymex.',
    kw: 'Gym Marketing Software, Gym Marketing Management, Gym WhatsApp Marketing, Gym SMS Campaigns, Gym Email Marketing, Fitness Marketing Software',
    css: marketingCSS,
    body: marketingBody
  },
  {
    dir: 'member-management',
    file: 'member-management/member-management.html',
    title: 'Gym Member Management Software | Profiles, Plans & Attendance | Gymex',
    desc: 'Manage gym member profiles, memberships, payments, attendance, and retention from one connected platform with Gymex Member Management Software.',
    kw: 'Gym Member Management Software, Gym Membership Management, Gym Member Tracking, Fitness Member Management, Gym Attendance Software',
    css: memberCSS,
    body: memberBody
  }
];

pages.forEach(p => {
  const html = getHead(p.title, p.desc, p.kw, p.css)
    + '<body>\n'
    + getNav()
    + p.body
    + getFooter()
    + getModal()
    + getScripts();
  
  fs.writeFileSync(p.file, html);
  
  // Verify
  const opens = (html.match(/<div[\s>]/g)||[]).length;
  const closes = (html.match(/<\/div>/g)||[]).length;
  const lines = html.split('\n');
  let depth = 0;
  for(let i=0;i<lines.length;i++){
    depth += (lines[i].match(/<div[\s>]/g)||[]).length - (lines[i].match(/<\/div>/g)||[]).length;
  }
  console.log(p.dir + ': opens=' + opens + ' closes=' + closes + ' depth=' + depth + ' ' + (depth===0?'✅':'❌'));
});

console.log('\nAll 3 pages generated!');
