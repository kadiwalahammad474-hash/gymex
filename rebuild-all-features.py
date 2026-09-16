#!/usr/bin/env python3
"""Rebuild all 3 feature pages with member management theme."""

import os

# Read nav from member management page
with open("member-management/member-management.html", "r", encoding="utf-8") as f:
    mm_html = f.read()

nav_start = mm_html.find("<nav")
nav_end = mm_html.find("</nav>") + 6
nav_html = mm_html[nav_start:nav_end]

# Read footer from member management page
footer_start = mm_html.find('<div style="background:#0b1a3d; padding:0;">')
footer_end = mm_html.find("</html>") + 7
footer_html = mm_html[footer_start:footer_end]

# Modal HTML
modal_html = '''<script src="../javascript.js"></script>
<script>
document.querySelectorAll('.open-modal-btn').forEach(function(btn) {
  btn.addEventListener('click', function(e) {
    e.preventDefault();
    document.getElementById('divemailpopup').classList.add('show');
    document.body.style.overflow = 'hidden';
  });
});
document.getElementById('close-contact-modal').addEventListener('click', function() {
  document.getElementById('divemailpopup').classList.remove('show');
  document.body.style.overflow = 'auto';
  document.getElementById('emailsuccessmsg').style.display = 'none';
  document.getElementById('form-body').style.display = 'block';
});
document.getElementById('divemailpopup').addEventListener('click', function(e) {
  if (e.target === this) {
    this.classList.remove('show');
    document.body.style.overflow = 'auto';
  }
});
document.querySelector('.send-again-btn').addEventListener('click', function() {
  document.getElementById('emailsuccessmsg').style.display = 'none';
  document.getElementById('form-body').style.display = 'block';
});
emailjs.init('AmP09sgXBaIgn9Juz');
var phoneInput = document.getElementById('number');
if (phoneInput) {
  var iti = window.intlTelInput(phoneInput, {
    utilsScript: 'https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js',
    separateDialCode: true,
    initialCountry: 'in'
  });
}
document.getElementById('contact-form').onsubmit = function(e) {
  e.preventDefault();
  document.getElementById('loader').classList.add('show');
  document.getElementById('divemailpopup').classList.add('show');
  var fullNumber = iti ? iti.getNumber() : phoneInput.value;
  emailjs.send('service_1o6wljl', 'template_6dewzmp', {
    firstname: document.getElementById('first-name').value,
    lastname: document.getElementById('last-name').value,
    company: document.getElementById('company').value,
    email: document.getElementById('email').value,
    phonenumber: fullNumber,
    message: this.message.value
  }).then(function() {
    document.getElementById('loader').classList.remove('show');
    document.getElementById('form-body').style.display = 'none';
    document.getElementById('emailsuccessmsg').style.display = 'block';
  }, function(err) {
    document.getElementById('loader').classList.remove('show');
    alert('Thank you! Your demo request has been submitted.');
    document.getElementById('divemailpopup').classList.remove('show');
    document.body.style.overflow = 'auto';
  });
};
document.addEventListener('keydown', function(e) {
  if (e.key === 'Escape') {
    document.getElementById('divemailpopup').classList.remove('show');
    document.body.style.overflow = 'auto';
  }
});
</script>'''

# Modal backdrop HTML (from member management)
modalBackdrop = old_html = ""
with open("member-management/member-management.html", "r", encoding="utf-8") as f:
    content = f.read()
    backdrop_start = content.find('<div class="backdrop"')
    if backdrop_start > 0:
        backdrop_end = content.find('</div>', backdrop_start) + 6
        # Find the full modal
        backdrop_start2 = content.find('<!-- Backdrop')
        if backdrop_start2 > 0:
            modalBackdrop = content[backdrop_start2:content.find('</html>')]

def build_page(title, meta_desc, badge, h1, h1_accent, desc, sections_html, faqs, cta_title, cta_desc, cta_italic):
    faq_html = ""
    for q, a in faqs:
        faq_html += f'''    <div class="feature-faq" onclick="this.classList.toggle('open')">
      <div class="feature-faq-q">{q} <i class="fa fa-chevron-down"></i></div>
      <div class="feature-faq-a">{a}</div>
    </div>
'''
    
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{meta_desc}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <link rel="stylesheet" href="../style.css">
  <link rel="stylesheet" href="../feature-theme.css">
  <style>
    h1, h2, h3, h4, p, span, li {{ text-transform: none !important; }}
  </style>
</head>
<body class="feature-page">

{nav_html}

<!-- Hero -->
<section class="feature-hero">
  <div class="feature-hero-grid">
    <div>
      <div class="sm-label">{badge}</div>
      <h1>{h1}</h1>
      <p class="sm-desc">{desc}</p>
      <div class="feature-hero-cta">
        <button class="sm-btn sm-btn-primary open-modal-btn">Get Your Free Demo <i class="fa fa-arrow-right"></i></button>
      </div>
    </div>
    <div class="feature-hero-img">
      <div style="background:var(--gray-7,#f5f7fb);border-radius:20px;min-height:320px;display:flex;align-items:center;justify-content:center;">
        <i class="fa fa-shield-halved" style="font-size:80px;color:rgba(2,142,206,.15);"></i>
      </div>
    </div>
  </div>
</section>

{sections_html}

<!-- CTA -->
<section class="feature-cta">
  <div class="feature-wrap">
    <h2>{cta_title}</h2>
    <p>{cta_desc}</p>
    <p style="color:rgba(255,255,255,.6)!important;font-size:14px!important;margin:0 0 28px!important;font-style:italic!important;">{cta_italic}</p>
    <button class="sm-btn sm-btn-primary open-modal-btn" style="background:linear-gradient(135deg,#f26522,#e0450b)!important;">Get Your Free Demo <i class="fa fa-arrow-right"></i></button>
  </div>
</section>

<!-- FAQ -->
<section class="feature-section grey">
  <div class="feature-wrap" style="max-width:800px;">
    <div class="feature-heading">
      <h2>Frequently Asked <span class="accent">Questions</span></h2>
      <div class="sm-underline"></div>
    </div>
{faq_html}
  </div>
</section>

{footer_html}

{modalBackdrop}
{modal_html}
</body>
</html>'''

# ═══════════════════════════════════════════════════════════════
# 1. BIOMETRIC & ACCESS CONTROL
# ═══════════════════════════════════════════════════════════════
biometric_sections = '''
<!-- Track Attendance with Biometric & RFID -->
<section class="feature-section grey">
  <div class="feature-heading">
    <h2>Track Attendance with <span class="accent">Biometric & RFID</span></h2>
    <div class="sm-underline"></div>
    <p>Manual attendance can slow down check-ins and make member visit records harder to maintain.</p>
  </div>
  <div class="feature-row">
    <div class="feature-content">
      <p>Gymex Gym Biometric Attendance Software allows you to capture staff and member attendance through biometric and RFID integration, creating a faster and more structured check-in process.</p>
      <p>Once a member checks in, their attendance information stays connected with your Gymex system, helping your team maintain accurate visit records without depending on manual registers.</p>
      <p>This makes everyday gym attendance tracking simpler for both members and staff.</p>
    </div>
    <div class="feature-img">
      <div style="text-align:center;">
        <div style="width:80px;height:80px;margin:0 auto 16px;background:linear-gradient(135deg,#028ECE,#0a5d8f);border-radius:20px;display:flex;align-items:center;justify-content:center;"><i class="fa fa-fingerprint" style="color:#fff;font-size:36px;"></i></div>
        <p style="font-size:14px;color:#6b7589;">Biometric + RFID Integration</p>
      </div>
    </div>
  </div>
  <div class="feature-flow" style="max-width:1180px;margin:32px auto;">
    <div class="feature-flow-step">Member Arrives</div>
    <div class="feature-flow-arrow">&rarr;</div>
    <div class="feature-flow-step">Biometric/RFID Verification</div>
    <div class="feature-flow-arrow">&rarr;</div>
    <div class="feature-flow-step">Check-In</div>
    <div class="feature-flow-arrow">&rarr;</div>
    <div class="feature-flow-step">Attendance Recorded</div>
  </div>
</section>

<!-- Multiple Ways to Check In -->
<section class="feature-section">
  <div class="feature-heading">
    <h2>Multiple Ways to <span class="accent">Check In</span></h2>
    <div class="sm-underline"></div>
    <p>This flexibility makes Gymex more than just biometric gym software — it provides multiple ways to manage attendance based on your gym's operations.</p>
  </div>
  <div class="feature-wrap">
    <div class="feature-cards cols-4">
      <div class="feature-card" style="text-align:center;">
        <div class="feature-card-icon" style="background:linear-gradient(135deg,#f26522,#e0450b);margin:0 auto 16px;"><i class="fa fa-fingerprint" style="color:#fff;"></i></div>
        <h3>Biometric</h3>
        <p>Capture attendance through biometric integration.</p>
      </div>
      <div class="feature-card" style="text-align:center;">
        <div class="feature-card-icon" style="background:linear-gradient(135deg,#028ECE,#0a5d8f);margin:0 auto 16px;"><i class="fa fa-id-card" style="color:#fff;"></i></div>
        <h3>RFID</h3>
        <p>Allow members and staff to check in using RFID.</p>
      </div>
      <div class="feature-card" style="text-align:center;">
        <div class="feature-card-icon" style="background:linear-gradient(135deg,#34A853,#1e7e34);margin:0 auto 16px;"><i class="fa fa-qrcode" style="color:#fff;"></i></div>
        <h3>QR Code</h3>
        <p>Enable member attendance through QR code scanning from the mobile app.</p>
      </div>
      <div class="feature-card" style="text-align:center;">
        <div class="feature-card-icon" style="background:linear-gradient(135deg,#7c3aed,#5b21b6);margin:0 auto 16px;"><i class="fa fa-clipboard-check" style="color:#fff;"></i></div>
        <h3>Manual Check-In</h3>
        <p>Allow authorized staff to record attendance manually when required.</p>
      </div>
    </div>
  </div>
</section>

<!-- Control Gym Access -->
<section class="feature-section grey">
  <div class="feature-heading">
    <h2>Control Gym Access Based on <span class="accent">Membership Rules</span></h2>
    <div class="sm-underline"></div>
    <p>Attendance tells you who checked in. Access control helps determine who should be allowed access.</p>
  </div>
  <div class="feature-wrap">
    <div class="feature-cards cols-3">
      <div class="feature-card" style="text-align:center;">
        <div class="feature-card-icon" style="background:linear-gradient(135deg,#f26522,#e0450b);margin:0 auto 16px;"><i class="fa fa-id-card-clip" style="color:#fff;"></i></div>
        <h3>Membership Type</h3>
        <p>Control access according to the membership or plan purchased by the member.</p>
      </div>
      <div class="feature-card" style="text-align:center;">
        <div class="feature-card-icon" style="background:linear-gradient(135deg,#028ECE,#0a5d8f);margin:0 auto 16px;"><i class="fa fa-cake-candles" style="color:#fff;"></i></div>
        <h3>Age</h3>
        <p>Apply relevant access restrictions based on member age.</p>
      </div>
      <div class="feature-card" style="text-align:center;">
        <div class="feature-card-icon" style="background:linear-gradient(135deg,#34A853,#1e7e34);margin:0 auto 16px;"><i class="fa fa-clock" style="color:#fff;"></i></div>
        <h3>Time</h3>
        <p>Control access based on permitted timings.</p>
      </div>
    </div>
    <div class="feature-flow" style="margin:32px auto;">
      <div class="feature-flow-step">Member</div>
      <div class="feature-flow-arrow">&rarr;</div>
      <div class="feature-flow-step">Membership Verification</div>
      <div class="feature-flow-arrow">&rarr;</div>
      <div class="feature-flow-step">Access Rules</div>
      <div class="feature-flow-arrow">&rarr;</div>
      <div class="feature-flow-step">Entry</div>
    </div>
  </div>
</section>

<!-- Block Defaulting + Multi-Floor + Multi-Branch -->
<section class="feature-section">
  <div class="feature-heading">
    <h2>Advanced <span class="accent">Access Control</span></h2>
    <div class="sm-underline"></div>
  </div>
  <div class="feature-wrap">
    <div class="feature-cards cols-3">
      <div class="feature-card">
        <div class="feature-card-icon" style="background:linear-gradient(135deg,#dc2626,#b91c1c);"><i class="fa fa-ban" style="color:#fff;"></i></div>
        <h3>Block Defaulting Members</h3>
        <p>Restrict access for members who do not meet applicable membership or payment conditions.</p>
      </div>
      <div class="feature-card">
        <div class="feature-card-icon" style="background:linear-gradient(135deg,#028ECE,#0a5d8f);"><i class="fa fa-building" style="color:#fff;"></i></div>
        <h3>Multi-Floor Integration</h3>
        <p>Manage biometric attendance and access across multiple floors.</p>
      </div>
      <div class="feature-card">
        <div class="feature-card-icon" style="background:linear-gradient(135deg,#34A853,#1e7e34);"><i class="fa fa-code-branch" style="color:#fff;"></i></div>
        <h3>Multi-Branch Reciprocity</h3>
        <p>Allow members to access eligible branches according to their purchased membership.</p>
      </div>
    </div>
  </div>
</section>

<!-- Connect Membership, Access & Attendance -->
<section class="feature-section grey">
  <div class="feature-heading">
    <h2>Connect <span class="accent">Membership, Access & Attendance</span></h2>
    <div class="sm-underline"></div>
    <p>One of the biggest advantages of using an integrated Gym Biometric Attendance System is that attendance doesn't have to operate separately from member information.</p>
  </div>
  <div class="feature-flow" style="max-width:1180px;margin:32px auto;">
    <div class="feature-flow-step">Member Profile</div>
    <div class="feature-flow-arrow">&rarr;</div>
    <div class="feature-flow-step">Membership Type</div>
    <div class="feature-flow-arrow">&rarr;</div>
    <div class="feature-flow-step">Access Rules</div>
    <div class="feature-flow-arrow">&rarr;</div>
    <div class="feature-flow-step">Check-In</div>
    <div class="feature-flow-arrow">&rarr;</div>
    <div class="feature-flow-step">Attendance</div>
  </div>
</section>

<!-- Why Choose Gymex -->
<section class="feature-section">
  <div class="feature-heading">
    <h2>Why Choose <span class="accent">Gymex</span> for Biometric & Access Control?</h2>
    <div class="sm-underline"></div>
    <p>Gymex brings attendance, member information, and facility access together within your gym management system.</p>
  </div>
  <div class="feature-wrap">
    <div class="feature-cards cols-3">
      <div class="feature-card" style="text-align:center;padding:24px;"><div class="feature-card-icon" style="background:linear-gradient(135deg,#f26522,#e0450b);margin:0 auto 14px;width:44px;height:44px;"><i class="fa fa-fingerprint" style="color:#fff;font-size:18px;"></i></div><h3 style="font-size:15px;">Biometric Attendance</h3><p style="font-size:13px;">Capture staff and member attendance through biometric integration.</p></div>
      <div class="feature-card" style="text-align:center;padding:24px;"><div class="feature-card-icon" style="background:linear-gradient(135deg,#028ECE,#0a5d8f);margin:0 auto 14px;width:44px;height:44px;"><i class="fa fa-id-card" style="color:#fff;font-size:18px;"></i></div><h3 style="font-size:15px;">RFID Check-In</h3><p style="font-size:13px;">Provide RFID-based attendance for convenient check-ins.</p></div>
      <div class="feature-card" style="text-align:center;padding:24px;"><div class="feature-card-icon" style="background:linear-gradient(135deg,#34A853,#1e7e34);margin:0 auto 14px;width:44px;height:44px;"><i class="fa fa-qrcode" style="color:#fff;font-size:18px;"></i></div><h3 style="font-size:15px;">QR Code Attendance</h3><p style="font-size:13px;">Allow members to record attendance using QR code scanning.</p></div>
      <div class="feature-card" style="text-align:center;padding:24px;"><div class="feature-card-icon" style="background:linear-gradient(135deg,#7c3aed,#5b21b6);margin:0 auto 14px;width:44px;height:44px;"><i class="fa fa-clipboard-check" style="color:#fff;font-size:18px;"></i></div><h3 style="font-size:15px;">Manual Check-In</h3><p style="font-size:13px;">Give authorized staff the flexibility to record attendance manually.</p></div>
      <div class="feature-card" style="text-align:center;padding:24px;"><div class="feature-card-icon" style="background:linear-gradient(135deg,#f26522,#e0450b);margin:0 auto 14px;width:44px;height:44px;"><i class="fa fa-id-card-clip" style="color:#fff;font-size:18px;"></i></div><h3 style="font-size:15px;">Membership-Based Access</h3><p style="font-size:13px;">Control facility access according to the membership purchased.</p></div>
      <div class="feature-card" style="text-align:center;padding:24px;"><div class="feature-card-icon" style="background:linear-gradient(135deg,#028ECE,#0a5d8f);margin:0 auto 14px;width:44px;height:44px;"><i class="fa fa-clock" style="color:#fff;font-size:18px;"></i></div><h3 style="font-size:15px;">Age & Time Restrictions</h3><p style="font-size:13px;">Set access restrictions based on member age and permitted timings.</p></div>
      <div class="feature-card" style="text-align:center;padding:24px;"><div class="feature-card-icon" style="background:linear-gradient(135deg,#dc2626,#b91c1c);margin:0 auto 14px;width:44px;height:44px;"><i class="fa fa-ban" style="color:#fff;font-size:18px;"></i></div><h3 style="font-size:15px;">Defaulting Member Control</h3><p style="font-size:13px;">Restrict access for members who do not meet payment conditions.</p></div>
      <div class="feature-card" style="text-align:center;padding:24px;"><div class="feature-card-icon" style="background:linear-gradient(135deg,#34A853,#1e7e34);margin:0 auto 14px;width:44px;height:44px;"><i class="fa fa-building" style="color:#fff;font-size:18px;"></i></div><h3 style="font-size:15px;">Multi-Floor Integration</h3><p style="font-size:13px;">Manage biometric attendance across multiple floors.</p></div>
      <div class="feature-card" style="text-align:center;padding:24px;grid-column:1/-1;max-width:calc(33.33% - 14px);margin:0 auto;"><div class="feature-card-icon" style="background:linear-gradient(135deg,#7c3aed,#5b21b6);margin:0 auto 14px;width:44px;height:44px;"><i class="fa fa-code-branch" style="color:#fff;font-size:18px;"></i></div><h3 style="font-size:15px;">Multi-Branch Reciprocity</h3><p style="font-size:13px;">Allow members to access eligible branches.</p></div>
    </div>
  </div>
</section>
'''

biometric_faqs = [
    ("What is gym biometric attendance software?", "Gym Biometric Attendance Software helps gyms record staff and member attendance using biometric identification. It reduces dependence on manual attendance registers and keeps check-in information more organized."),
    ("Does Gymex support RFID attendance?", "Yes. Gymex supports attendance through RFID and biometric integration, giving gyms multiple options for recording staff and member check-ins."),
    ("Can members check in using a QR code?", "Yes. Gymex supports QR code scanning for member attendance through the mobile app, providing members with a convenient check-in option."),
    ("What is gym access control software?", "Gym Access Control Software helps fitness businesses manage who can access their facilities based on defined rules. Gymex supports access restrictions based on membership type, age, and time."),
    ("Can Gymex restrict access for defaulting members?", "Yes. Gymex provides the ability to block defaulting members, helping fitness businesses maintain better control over facility access."),
    ("Can access be controlled according to membership type?", "Yes. Gymex can apply access restrictions according to the membership purchased by the member, along with relevant age and time-based rules."),
    ("Does Gymex support multiple gym branches?", "Gymex supports reciprocity for multi-branch businesses, allowing eligible members to access different branches according to their purchased membership."),
    ("Can Gymex track staff attendance?", "Yes. Gymex can capture staff attendance along with member attendance, helping fitness businesses maintain attendance information in a connected system."),
]

biometric_html = build_page(
    title="Gym Biometric Attendance & Access Control Software | Gymex",
    meta_desc="Automate gym attendance with biometric, RFID and QR check-ins. Control member access by membership, age and time with Gymex biometric and access control software.",
    badge="BIOMETRIC & ACCESS CONTROL SOFTWARE",
    h1="Simplify Gym Check-Ins<br>& Control Member Access",
    h1_accent="",
    desc="Track staff and member attendance with biometric, RFID, QR code, and manual check-ins. Gymex helps you manage facility access based on membership rules while keeping attendance and access control connected in one platform.",
    sections_html=biometric_sections,
    faqs=biometric_faqs,
    cta_title="Make Every Check-In Smarter",
    cta_desc="Simplify attendance and maintain better control over facility access with Gymex.",
    cta_italic="Biometric. RFID. QR Check-In. Smarter Access Control."
)

with open("biometric-access-control/biometric-access-control.html", "w", encoding="utf-8") as f:
    f.write(biometric_html)
print("Done: Biometric & Access Control page rebuilt!")

# ═══════════════════════════════════════════════════════════════
# 2. DATA ANALYSIS & DASHBOARD
# ═══════════════════════════════════════════════════════════════
da_sections = '''
<!-- See Performance at a Glance -->
<section class="feature-section grey">
  <div class="feature-heading">
    <h2>See Your Gym's <span class="accent">Performance</span> at a Glance</h2>
    <div class="sm-underline"></div>
    <p>Gymex keeps your key business metrics connected in one dashboard so you can quickly understand how your gym is performing.</p>
  </div>
  <div class="feature-wrap">
    <div class="feature-cards cols-3">
      <div class="feature-card" style="text-align:center;"><div class="feature-card-icon" style="background:linear-gradient(135deg,#f26522,#e0450b);margin:0 auto 14px;"><i class="fa fa-indian-rupee-sign" style="color:#fff;"></i></div><h3>Collections & Balances</h3><p>View total payments received, outstanding dues, and overall collection status.</p></div>
      <div class="feature-card" style="text-align:center;"><div class="feature-card-icon" style="background:linear-gradient(135deg,#028ECE,#0a5d8f);margin:0 auto 14px;"><i class="fa fa-arrow-up-right-dots" style="color:#fff;"></i></div><h3>Membership Upgrades</h3><p>Track membership upgrades and plan changes across your gym.</p></div>
      <div class="feature-card" style="text-align:center;"><div class="feature-card-icon" style="background:linear-gradient(135deg,#34A853,#1e7e34);margin:0 auto 14px;"><i class="fa fa-file-invoice" style="color:#fff;"></i></div><h3>Daily Billing</h3><p>Monitor daily billing activity and revenue trends.</p></div>
      <div class="feature-card" style="text-align:center;"><div class="feature-card-icon" style="background:linear-gradient(135deg,#7c3aed,#5b21b6);margin:0 auto 14px;"><i class="fa fa-users" style="color:#fff;"></i></div><h3>Live Members</h3><p>See current active members and membership status at a glance.</p></div>
      <div class="feature-card" style="text-align:center;"><div class="feature-card-icon" style="background:linear-gradient(135deg,#dc2626,#b91c1c);margin:0 auto 14px;"><i class="fa fa-calendar-xmark" style="color:#fff;"></i></div><h3>Membership Expiry</h3><p>Track upcoming expiries and manage renewals proactively.</p></div>
      <div class="feature-card" style="text-align:center;"><div class="feature-card-icon" style="background:linear-gradient(135deg,#f26522,#e0450b);margin:0 auto 14px;"><i class="fa fa-rotate" style="color:#fff;"></i></div><h3>Expected Renewals</h3><p>View expected renewals and plan follow-ups accordingly.</p></div>
      <div class="feature-card" style="text-align:center;"><div class="feature-card-icon" style="background:linear-gradient(135deg,#028ECE,#0a5d8f);margin:0 auto 14px;"><i class="fa fa-trophy" style="color:#fff;"></i></div><h3>Sales Performance</h3><p>Monitor lead conversion rates and sales team performance.</p></div>
      <div class="feature-card" style="text-align:center;"><div class="feature-card-icon" style="background:linear-gradient(135deg,#34A853,#1e7e34);margin:0 auto 14px;"><i class="fa fa-phone" style="color:#fff;"></i></div><h3>Follow-up Calls</h3><p>Track follow-up call activity and lead engagement.</p></div>
      <div class="feature-card" style="text-align:center;"><div class="feature-card-icon" style="background:linear-gradient(135deg,#7c3aed,#5b21b6);margin:0 auto 14px;"><i class="fa fa-circle-check" style="color:#fff;"></i></div><h3>Approval Requests</h3><p>Monitor pending approval requests and manage workflows.</p></div>
    </div>
  </div>
</section>

<!-- Explore 50+ Business Reports -->
<section class="feature-section">
  <div class="feature-heading">
    <h2>Explore <span class="accent">50+ Business Reports</span></h2>
    <div class="sm-underline"></div>
    <p>Gymex provides detailed reports across different areas of your gym business.</p>
  </div>
  <div class="feature-wrap">
    <div class="feature-cards cols-2">
      <div class="feature-card"><div class="feature-card-icon" style="background:linear-gradient(135deg,#f26522,#e0450b);"><i class="fa fa-chart-pie" style="color:#fff;"></i></div><h3>Financial Reports</h3><p>Revenue, collections, payments, dues, GST, and tax-related reports for complete financial visibility.</p></div>
      <div class="feature-card"><div class="feature-card-icon" style="background:linear-gradient(135deg,#028ECE,#0a5d8f);"><i class="fa fa-users" style="color:#fff;"></i></div><h3>Member & Attendance Reports</h3><p>Member activity, attendance patterns, visit frequency, and membership status reports.</p></div>
      <div class="feature-card"><div class="feature-card-icon" style="background:linear-gradient(135deg,#34A853,#1e7e34);"><i class="fa fa-bullseye" style="color:#fff;"></i></div><h3>Sales & Lead Reports</h3><p>Lead conversion, sales performance, follow-up tracking, and pipeline reports.</p></div>
      <div class="feature-card"><div class="feature-card-icon" style="background:linear-gradient(135deg,#7c3aed,#5b21b6);"><i class="fa fa-percent" style="color:#fff;"></i></div><h3>Commission & Staff Reports</h3><p>Trainer commissions, staff performance, and payroll-related reports.</p></div>
    </div>
  </div>
</section>

<!-- Track KPIs That Matter -->
<section class="feature-section grey">
  <div class="feature-heading">
    <h2>Track the <span class="accent">KPIs That Matter</span></h2>
    <div class="sm-underline"></div>
    <p>Key performance indicators help you understand what's working and where improvements are needed.</p>
  </div>
  <div class="feature-wrap">
    <div class="feature-cards cols-3">
      <div class="feature-card" style="text-align:center;"><div class="feature-card-icon" style="background:linear-gradient(135deg,#f26522,#e0450b);margin:0 auto 14px;width:44px;height:44px;"><i class="fa fa-chart-line" style="color:#fff;font-size:18px;"></i></div><h3 style="font-size:15px;">Sales Performance</h3><p style="font-size:13px;">Track lead conversion rates and revenue targets.</p></div>
      <div class="feature-card" style="text-align:center;"><div class="feature-card-icon" style="background:linear-gradient(135deg,#028ECE,#0a5d8f);margin:0 auto 14px;width:44px;height:44px;"><i class="fa fa-user-check" style="color:#fff;font-size:18px;"></i></div><h3 style="font-size:15px;">Member Activity</h3><p style="font-size:13px;">Monitor check-in frequency and engagement levels.</p></div>
      <div class="feature-card" style="text-align:center;"><div class="feature-card-icon" style="background:linear-gradient(135deg,#34A853,#1e7e34);margin:0 auto 14px;width:44px;height:44px;"><i class="fa fa-rotate" style="color:#fff;font-size:18px;"></i></div><h3 style="font-size:15px;">Renewals</h3><p style="font-size:13px;">Track renewal rates and upcoming expiries.</p></div>
      <div class="feature-card" style="text-align:center;"><div class="feature-card-icon" style="background:linear-gradient(135deg,#7c3aed,#5b21b6);margin:0 auto 14px;width:44px;height:44px;"><i class="fa fa-indian-rupee-sign" style="color:#fff;font-size:18px;"></i></div><h3 style="font-size:15px;">Collections</h3><p style="font-size:13px;">Monitor payment collections and outstanding dues.</p></div>
      <div class="feature-card" style="text-align:center;grid-column:1/-1;max-width:calc(33.33% - 14px);margin:0 auto;"><div class="feature-card-icon" style="background:linear-gradient(135deg,#f26522,#e0450b);margin:0 auto 14px;width:44px;height:44px;"><i class="fa fa-phone" style="color:#fff;font-size:18px;"></i></div><h3 style="font-size:15px;">Leads & Follow-Ups</h3><p style="font-size:13px;">Track lead pipeline and follow-up activity.</p></div>
    </div>
  </div>
</section>

<!-- Monitor Sales Team Performance -->
<section class="feature-section">
  <div class="feature-heading">
    <h2>Monitor <span class="accent">Sales Team Performance</span></h2>
    <div class="sm-underline"></div>
    <p>Track your sales team's activity, conversions, and revenue contribution through dedicated reports.</p>
  </div>
  <div class="feature-row">
    <div class="feature-content">
      <p>Gymex provides detailed sales team reports that help you understand individual and team performance.</p>
      <p>Track lead assignments, follow-up activity, conversion rates, and revenue generated by each team member.</p>
      <p>This helps you identify top performers, areas for improvement, and optimize your sales process.</p>
    </div>
    <div class="feature-img">
      <div style="text-align:center;">
        <div style="width:80px;height:80px;margin:0 auto 16px;background:linear-gradient(135deg,#34A853,#1e7e34);border-radius:20px;display:flex;align-items:center;justify-content:center;"><i class="fa fa-chart-bar" style="color:#fff;font-size:36px;"></i></div>
        <p style="font-size:14px;color:#6b7589;">Sales Performance Dashboard</p>
      </div>
    </div>
  </div>
</section>
'''

da_faqs = [
    ("What is gym analytics software?", "Gym analytics software helps fitness businesses track performance through dashboards, reports, and key metrics covering revenue, members, attendance, and sales."),
    ("What reports does Gymex provide?", "Gymex provides 50+ business reports including financial, member, attendance, sales, lead, commission, and staff reports."),
    ("Can I track revenue and collections?", "Yes. Gymex provides detailed financial reports covering revenue, collections, outstanding dues, and payment trends."),
    ("Does Gymex track sales team performance?", "Yes. Gymex provides sales team reports covering lead conversion, follow-up activity, and revenue contribution."),
    ("Can I export reports from Gymex?", "Yes. Gymex supports data export for most reports, helping you share insights with your team."),
]

da_html = build_page(
    title="Gym Analytics Software, Reports & Dashboard | Gymex",
    meta_desc="Track your gym's performance with 50+ business reports, dashboards, and KPIs. Monitor revenue, members, attendance, and sales with Gymex analytics.",
    badge="GYM ANALYTICS & REPORTING SOFTWARE",
    h1="Turn Your Gym Data into<br>Actionable <span class='accent'>Insights</span>",
    h1_accent="",
    desc="Track your gym's performance with 50+ business reports, interactive dashboards, and key performance indicators — all in one connected platform.",
    sections_html=da_sections,
    faqs=da_faqs,
    cta_title="Make Data-Driven Decisions",
    cta_desc="Understand your gym business better with real-time analytics and detailed reports from Gymex.",
    cta_italic="Track. Analyze. Grow. Succeed."
)

with open("data-analysis-dashboard/data-analysis-dashboard.html", "w", encoding="utf-8") as f:
    f.write(da_html)
print("Done: Data Analysis & Dashboard page rebuilt!")

# ═══════════════════════════════════════════════════════════════
# 3. INTELLIGENT ALERTS & REMINDERS
# ═══════════════════════════════════════════════════════════════
ia_sections = '''
<!-- Create Customized Alerts -->
<section class="feature-section grey">
  <div class="feature-heading">
    <h2>Create <span class="accent">Customized Alerts</span> for Members</h2>
    <div class="sm-underline"></div>
    <p>Different members may need different updates at the right time.</p>
  </div>
  <div class="feature-row">
    <div class="feature-content">
      <p>Gymex lets you create customized alerts for members, helping your fitness business keep important communication organized and timely.</p>
      <p>From membership-related updates to payments, renewals, classes, and other important notifications, Gymex Gym Reminder Software helps reduce repetitive manual communication while keeping members informed.</p>
    </div>
    <div class="feature-img">
      <div style="text-align:center;">
        <div style="width:80px;height:80px;margin:0 auto 16px;background:linear-gradient(135deg,#f26522,#e0450b);border-radius:20px;display:flex;align-items:center;justify-content:center;"><i class="fa fa-bell" style="color:#fff;font-size:36px;"></i></div>
        <p style="font-size:14px;color:#6b7589;">Customized Member Alerts</p>
      </div>
    </div>
  </div>
  <div class="feature-flow" style="max-width:1180px;margin:32px auto;">
    <div class="feature-flow-step">Create Alert</div>
    <div class="feature-flow-arrow">&rarr;</div>
    <div class="feature-flow-step">Select Members</div>
    <div class="feature-flow-arrow">&rarr;</div>
    <div class="feature-flow-step">Send Notification</div>
    <div class="feature-flow-arrow">&rarr;</div>
    <div class="feature-flow-step">Keep Members Updated</div>
  </div>
</section>

<!-- Multiple Channels -->
<section class="feature-section">
  <div class="feature-heading">
    <h2>Send Alerts Across <span class="accent">Multiple Channels</span></h2>
    <div class="sm-underline"></div>
    <p>Reach members through convenient communication channels.</p>
  </div>
  <div class="feature-wrap">
    <div class="feature-cards cols-3">
      <div class="feature-card" style="text-align:center;"><div class="feature-card-icon" style="background:linear-gradient(135deg,#f26522,#e0450b);margin:0 auto 16px;"><i class="fa fa-comment-sms" style="color:#fff;"></i></div><h3>SMS Alerts</h3><p>Send important updates directly through SMS.</p></div>
      <div class="feature-card" style="text-align:center;"><div class="feature-card-icon" style="background:linear-gradient(135deg,#028ECE,#0a5d8f);margin:0 auto 16px;"><i class="fa fa-envelope" style="color:#fff;"></i></div><h3>Email Alerts</h3><p>Keep members informed through email communication.</p></div>
      <div class="feature-card" style="text-align:center;"><div class="feature-card-icon" style="background:linear-gradient(135deg,#34A853,#1e7e34);margin:0 auto 16px;"><i class="fa fa-mobile-screen" style="color:#fff;"></i></div><h3>App Notifications</h3><p>Send notifications through the app for timely updates.</p></div>
    </div>
    <p style="text-align:center;color:#6b7589;font-size:14px;margin-top:16px;">Using multiple channels helps make your gym alerts and notifications process more flexible and organized.</p>
  </div>
</section>

<!-- Balance & Renewal Alerts -->
<section class="feature-section grey">
  <div class="feature-heading">
    <h2>Stay Ahead of <span class="accent">Balance & Renewal</span> Payments</h2>
    <div class="sm-underline"></div>
    <p>Membership renewals and outstanding balances are important to your gym's day-to-day revenue.</p>
  </div>
  <div class="feature-row">
    <div class="feature-content">
      <p>Gymex allows you to send balance and renewal payment alerts, helping members stay informed about upcoming or pending payments while reducing the need for repeated manual reminders from your team.</p>
      <p>With Gym Membership Renewal Reminders, your team can maintain more consistent payment communication and keep important renewal information from being overlooked.</p>
    </div>
    <div class="feature-img">
      <div style="text-align:center;">
        <div style="width:80px;height:80px;margin:0 auto 16px;background:linear-gradient(135deg,#028ECE,#0a5d8f);border-radius:20px;display:flex;align-items:center;justify-content:center;"><i class="fa fa-indian-rupee-sign" style="color:#fff;font-size:36px;"></i></div>
        <p style="font-size:14px;color:#6b7589;">Payment & Renewal Alerts</p>
      </div>
    </div>
  </div>
  <div class="feature-flow" style="max-width:1180px;margin:32px auto;">
    <div class="feature-flow-step">Payment/Renewal Due</div>
    <div class="feature-flow-arrow">&rarr;</div>
    <div class="feature-flow-step">Alert</div>
    <div class="feature-flow-arrow">&rarr;</div>
    <div class="feature-flow-step">Member Informed</div>
    <div class="feature-flow-arrow">&rarr;</div>
    <div class="feature-flow-step">Follow-Up</div>
  </div>
</section>

<!-- Class & Service + Bill Creation + Operational -->
<section class="feature-section">
  <div class="feature-heading">
    <h2>Class, Billing & <span class="accent">Operational Alerts</span></h2>
    <div class="sm-underline"></div>
  </div>
  <div class="feature-wrap">
    <div class="feature-cards cols-3">
      <div class="feature-card"><div class="feature-card-icon" style="background:linear-gradient(135deg,#34A853,#1e7e34);"><i class="fa fa-calendar-check" style="color:#fff;"></i></div><h3>Class & Service Notifications</h3><p>Send push notifications about classes and services, helping you keep members informed about relevant activities.</p></div>
      <div class="feature-card"><div class="feature-card-icon" style="background:linear-gradient(135deg,#f26522,#e0450b);"><i class="fa fa-file-invoice-dollar" style="color:#fff;"></i></div><h3>Bill Creation Notifications</h3><p>Keep members informed when their bills are generated, allowing relevant billing information to reach members automatically.</p></div>
      <div class="feature-card"><div class="feature-card-icon" style="background:linear-gradient(135deg,#028ECE,#0a5d8f);"><i class="fa fa-building" style="color:#fff;"></i></div><h3>Operational Alerts</h3><p>Data export alerts and appointment confirmation alerts for trainers help keep your team informed about important activities.</p></div>
    </div>
  </div>
</section>

<!-- Automate Follow-Ups -->
<section class="feature-section grey">
  <div class="feature-heading">
    <h2>Automate <span class="accent">Follow-Ups</span> & Reduce Manual Work</h2>
    <div class="sm-underline"></div>
    <p>Following up manually with every member or prospect can take up valuable staff time.</p>
  </div>
  <div class="feature-wrap">
    <p style="color:#6b7589;font-size:15px;line-height:1.7;margin-bottom:20px;">Gymex helps simplify this process with automated follow-ups, allowing your team to maintain timely communication without depending on repeated manual reminders.</p>
    <div class="feature-cards cols-2" style="max-width:700px;margin:0 auto 24px;">
      <div class="feature-card" style="padding:16px 20px;"><p style="margin:0;display:flex;align-items:center;gap:8px;"><span style="width:8px;height:8px;border-radius:50%;background:#f26522;flex-shrink:0;"></span>Reduce repetitive follow-up work</p></div>
      <div class="feature-card" style="padding:16px 20px;"><p style="margin:0;display:flex;align-items:center;gap:8px;"><span style="width:8px;height:8px;border-radius:50%;background:#f26522;flex-shrink:0;"></span>Maintain timely communication</p></div>
      <div class="feature-card" style="padding:16px 20px;"><p style="margin:0;display:flex;align-items:center;gap:8px;"><span style="width:8px;height:8px;border-radius:50%;background:#f26522;flex-shrink:0;"></span>Keep important follow-ups from being missed</p></div>
      <div class="feature-card" style="padding:16px 20px;"><p style="margin:0;display:flex;align-items:center;gap:8px;"><span style="width:8px;height:8px;border-radius:50%;background:#f26522;flex-shrink:0;"></span>Improve consistency across member communication</p></div>
    </div>
    <div class="feature-flow" style="max-width:1180px;margin:32px auto;">
      <div class="feature-flow-step">Alert</div>
      <div class="feature-flow-arrow">&rarr;</div>
      <div class="feature-flow-step">Reminder</div>
      <div class="feature-flow-arrow">&rarr;</div>
      <div class="feature-flow-step">Automated Follow-Up</div>
      <div class="feature-flow-arrow">&rarr;</div>
      <div class="feature-flow-step">Timely Action</div>
    </div>
  </div>
</section>

<!-- One Alert System -->
<section class="feature-section">
  <div class="feature-heading">
    <h2>One Alert System for <span class="accent">Everyday Communication</span></h2>
    <div class="sm-underline"></div>
    <p>Instead of relying on separate reminders and repeated manual communication, Gymex brings important member alerts and reminders together.</p>
  </div>
  <div class="feature-flow" style="max-width:1180px;margin:32px auto;">
    <div class="feature-flow-step">Membership</div>
    <div class="feature-flow-arrow">&rarr;</div>
    <div class="feature-flow-step">Payments</div>
    <div class="feature-flow-arrow">&rarr;</div>
    <div class="feature-flow-step">Billing</div>
    <div class="feature-flow-arrow">&rarr;</div>
    <div class="feature-flow-step">Renewals</div>
    <div class="feature-flow-arrow">&rarr;</div>
    <div class="feature-flow-step">Classes</div>
    <div class="feature-flow-arrow">&rarr;</div>
    <div class="feature-flow-step">Appointments</div>
  </div>
  <p style="text-align:center;color:#6b7589;font-size:14px;max-width:700px;margin:16px auto 0;">With Gym Alerts and Notifications Software, important updates can reach the right members while your team spends less time managing routine communication manually.</p>
</section>

<!-- Why Choose Gymex -->
<section class="feature-section grey">
  <div class="feature-heading">
    <h2>Why Choose <span class="accent">Gymex</span> for Intelligent Alerts?</h2>
    <div class="sm-underline"></div>
    <p>Gymex brings attendance, member information, and facility access together within your gym management system.</p>
  </div>
  <div class="feature-wrap">
    <div class="feature-cards cols-3">
      <div class="feature-card" style="text-align:center;padding:24px;"><div class="feature-card-icon" style="background:linear-gradient(135deg,#f26522,#e0450b);margin:0 auto 14px;width:44px;height:44px;"><i class="fa fa-bell" style="color:#fff;font-size:18px;"></i></div><h3 style="font-size:15px;">Customized Alerts</h3><p style="font-size:13px;">Create relevant alerts for members and staff.</p></div>
      <div class="feature-card" style="text-align:center;padding:24px;"><div class="feature-card-icon" style="background:linear-gradient(135deg,#028ECE,#0a5d8f);margin:0 auto 14px;width:44px;height:44px;"><i class="fa fa-comment-sms" style="color:#fff;font-size:18px;"></i></div><h3 style="font-size:15px;">SMS Notifications</h3><p style="font-size:13px;">Send important updates directly through SMS.</p></div>
      <div class="feature-card" style="text-align:center;padding:24px;"><div class="feature-card-icon" style="background:linear-gradient(135deg,#34A853,#1e7e34);margin:0 auto 14px;width:44px;height:44px;"><i class="fa fa-envelope" style="color:#fff;font-size:18px;"></i></div><h3 style="font-size:15px;">Email Alerts</h3><p style="font-size:13px;">Communicate relevant information through email.</p></div>
      <div class="feature-card" style="text-align:center;padding:24px;"><div class="feature-card-icon" style="background:linear-gradient(135deg,#7c3aed,#5b21b6);margin:0 auto 14px;width:44px;height:44px;"><i class="fa fa-mobile-screen" style="color:#fff;font-size:18px;"></i></div><h3 style="font-size:15px;">App Notifications</h3><p style="font-size:13px;">Keep users updated through app-based notifications.</p></div>
      <div class="feature-card" style="text-align:center;padding:24px;"><div class="feature-card-icon" style="background:linear-gradient(135deg,#f26522,#e0450b);margin:0 auto 14px;width:44px;height:44px;"><i class="fa fa-indian-rupee-sign" style="color:#fff;font-size:18px;"></i></div><h3 style="font-size:15px;">Balance & Renewal Alerts</h3><p style="font-size:13px;">Remind members about balances and renewal payments.</p></div>
      <div class="feature-card" style="text-align:center;padding:24px;"><div class="feature-card-icon" style="background:linear-gradient(135deg,#028ECE,#0a5d8f);margin:0 auto 14px;width:44px;height:44px;"><i class="fa fa-file-invoice-dollar" style="color:#fff;font-size:18px;"></i></div><h3 style="font-size:15px;">Bill Creation Notifications</h3><p style="font-size:13px;">Send SMS notifications when bills are created.</p></div>
      <div class="feature-card" style="text-align:center;padding:24px;"><div class="feature-card-icon" style="background:linear-gradient(135deg,#34A853,#1e7e34);margin:0 auto 14px;width:44px;height:44px;"><i class="fa fa-calendar-check" style="color:#fff;font-size:18px;"></i></div><h3 style="font-size:15px;">Class & Service Updates</h3><p style="font-size:13px;">Use push notifications to keep members engaged.</p></div>
      <div class="feature-card" style="text-align:center;padding:24px;"><div class="feature-card-icon" style="background:linear-gradient(135deg,#dc2626,#b91c1c);margin:0 auto 14px;width:44px;height:44px;"><i class="fa fa-download" style="color:#fff;font-size:18px;"></i></div><h3 style="font-size:15px;">Data Export Alerts</h3><p style="font-size:13px;">Keep relevant staff informed about data export activity.</p></div>
      <div class="feature-card" style="text-align:center;padding:24px;grid-column:1/-1;max-width:calc(33.33% - 14px);margin:0 auto;"><div class="feature-card-icon" style="background:linear-gradient(135deg,#7c3aed,#5b21b6);margin:0 auto 14px;width:44px;height:44px;"><i class="fa fa-user" style="color:#fff;font-size:18px;"></i></div><h3 style="font-size:15px;">Trainer Appointment Alerts</h3><p style="font-size:13px;">Send appointment confirmation alerts to trainers.</p></div>
    </div>
  </div>
</section>
'''

ia_faqs = [
    ("What is gym reminder software?", "Gym Reminder Software helps fitness businesses manage important alerts and reminders for members and staff. It can reduce repetitive manual communication and help ensure important updates are shared on time."),
    ("What alerts are available in Gymex?", "Gymex supports customized member and staff alerts, balance and renewal payment alerts, bill creation notification SMS, data export alerts, class and service push notifications, and appointment confirmation alerts for trainers."),
    ("Can Gymex send membership renewal reminders?", "Yes. Gymex supports balance and renewal payment alerts to help keep members informed about relevant membership payments."),
    ("Which channels can Gymex use for alerts?", "Gymex supports alerts through SMS, email, and app notifications, depending on the type of communication."),
    ("Can Gymex send alerts to trainers?", "Yes. Gymex supports appointment confirmation alerts for trainers, helping them stay informed about confirmed appointments."),
]

ia_html = build_page(
    title="Gym Reminder Software & Intelligent Alerts | Gymex",
    meta_desc="Send customized gym alerts and reminders for members and staff with Gymex. Manage renewal, balance, billing, appointment and class notifications from one platform.",
    badge="GYM ALERTS & REMINDER SOFTWARE",
    h1="Keep Members Updated<br>with <span class='accent'>Intelligent Alerts</span>",
    h1_accent="",
    desc="Send timely personalized alerts, reminders, and automated follow-ups with Gymex. Keep members informed about renewals, payments, appointments, classes, and other important updates from one connected platform.",
    sections_html=ia_sections,
    faqs=ia_faqs,
    cta_title="Make Every Important Update Count",
    cta_desc="Keep members engaged and your team informed with intelligent alerts from Gymex.",
    cta_italic="Customize. Notify. Remind. Engage."
)

with open("intelligent-alerts/intelligent-alerts-reminders.html", "w", encoding="utf-8") as f:
    f.write(ia_html)
print("Done: Intelligent Alerts & Reminders page rebuilt!")

print("\nAll 3 feature pages rebuilt with member management theme!")
