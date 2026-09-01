import os, re

BASE = os.path.dirname(os.path.abspath(__file__))

# Extract nav from existing page
with open(os.path.join(BASE, "expense-management", "expense-management.html"), "r", encoding="utf-8") as f:
    full = f.read()

# Get nav (from <nav to closing </nav>)
nav_match = re.search(r'(<nav class="nav".*?</nav>)', full, re.DOTALL)
NAV = nav_match.group(1) if nav_match else ""

# Get footer (from <!-- FOOTER to end)
footer_match = re.search(r'(<!-- FOOTER from Home -->.*)', full, re.DOTALL)
FOOTER = footer_match.group(1) if footer_match else ""

# Get the modal HTML
modal_match = re.search(r'(<!-- Modal -->.*?</div>\s*</div>\s*</div>)', full, re.DOTALL)
MODAL = modal_match.group(1) if modal_match else ""

# Get CTA section pattern
cta_match = re.search(r'(<!-- Get Your Free Demo -->.*?</section>)', full, re.DOTALL)
CTA = cta_match.group(1) if cta_match else ""

def build_page(title, meta_desc, meta_keywords, og_title, og_desc, label, hero_title, hero_desc, faqs, content_sections, css_extra="", ld_json=""):
    faq_html = "\n".join([
        f'      <div class="ia-faq-item">\n        <details><summary>{q}</summary><p>{a}</p></details>\n      </div>'
        for q, a in faqs
    ])
    
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<script type="text/javascript">(function(c,l,a,r,i,t,y){{c[a]=c[a]||function(){{(c[a].q=c[a].q||[]).push(arguments)}};t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y)}})(window, document, "clarity", "script", "n95oax955q");</script>
<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&'+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f)}})(window,document,'script','dataLayer','GTM-KPCRHTFH');</script>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title}</title>
<meta name="description" content="{meta_desc}">
<meta name="keywords" content="{meta_keywords}">
<meta property="og:type" content="website">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{og_desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="icon" type="image/x-icon" href="../assets/gymex-favicon-U7mChGv0.ico">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<link rel="stylesheet" href="../style.css">
<link rel="stylesheet" href="../feature-page.css">
<script src="../javascript.js"></script>
{ld_json}
</head>
<body>

{NAV}

<!-- Hero Section -->
<section class="ia-hero">
  <div class="ia-hero-inner">
    <span class="ia-label">{label}</span>
    <h1 class="ia-hero-title">{hero_title}</h1>
    <p class="ia-hero-desc">{hero_desc}</p>
    <a class="ia-cta-btn open-modal-btn" href="#">GET YOUR FREE DEMO</a>
  </div>
</section>

<!-- Content Sections -->
{content_sections}

<!-- FAQ Section -->
<section class="ia-section" style="background:#f8f9fc;">
  <div class="ia-container">
    <h2 class="ia-h2 ia-text-center">Frequently Asked Questions</h2>
    <div class="ia-faq-grid">
{faq_html}
    </div>
  </div>
</section>

<!-- CTA Section -->
<section class="ia-cta-section">
  <div class="ia-container ia-text-center">
    <h2 class="ia-cta-title">Make Every Important Update Count</h2>
    <p class="ia-cta-desc">{hero_desc}</p>
    <a class="ia-cta-btn open-modal-btn" href="#">GET YOUR FREE DEMO</a>
  </div>
</section>

{FOOTER}

{MODAL}

<script src="../javascript.js"></script>
</body>
</html>'''


# ═══════════════════════════════════════════
# PAGE 1: Intelligent Alerts & Reminders
# ═══════════════════════════════════════════

alerts_content = '''
<!-- Multi-Channel Alerts -->
<section class="ia-section">
  <div class="ia-container">
    <h2 class="ia-h2">Send Alerts Across Multiple Channels</h2>
    <p class="ia-desc">Reach members through convenient communication channels. Gymex supports alerts through SMS, email, and app notifications, giving your business multiple ways to communicate important information.</p>
    <div class="ia-3col">
      <div class="ia-card">
        <div class="ia-card-icon"><i class="fa fa-comment"></i></div>
        <h3 class="ia-card-title">SMS Alerts</h3>
        <p class="ia-card-desc">Send important updates directly through SMS to keep members informed about payments, renewals, and appointments.</p>
      </div>
      <div class="ia-card">
        <div class="ia-card-icon"><i class="fa fa-envelope"></i></div>
        <h3 class="ia-card-title">Email Alerts</h3>
        <p class="ia-card-desc">Keep members informed through email communication with detailed updates about their membership and activities.</p>
      </div>
      <div class="ia-card">
        <div class="ia-card-icon"><i class="fa fa-bell"></i></div>
        <h3 class="ia-card-title">App Notifications</h3>
        <p class="ia-card-desc">Send push notifications through the app for timely updates about classes, services, and membership activities.</p>
      </div>
    </div>
  </div>
</section>

<!-- Balance & Renewal -->
<section class="ia-section ia-alt-bg">
  <div class="ia-container ia-row">
    <div class="ia-col-text">
      <h2 class="ia-h2">Stay Ahead of Balance & Renewal Payments</h2>
      <p class="ia-desc">Membership renewals and outstanding balances are important to your gym's day-to-day revenue. Gymex allows you to send balance and renewal payment alerts, helping members stay informed about upcoming or pending payments.</p>
      <div class="ia-workflow">
        <span class="ia-wf-step">Payment Due</span>
        <span class="ia-wf-arrow"><i class="fa fa-arrow-right"></i></span>
        <span class="ia-wf-step">Alert Sent</span>
        <span class="ia-wf-arrow"><i class="fa fa-arrow-right"></i></span>
        <span class="ia-wf-step">Member Informed</span>
        <span class="ia-wf-arrow"><i class="fa fa-arrow-right"></i></span>
        <span class="ia-wf-step">Follow-Up</span>
      </div>
    </div>
    <div class="ia-col-visual">
      <div class="ia-visual-box">
        <div class="ia-stat"><span class="ia-stat-num">100%</span><span class="ia-stat-label">Payment Visibility</span></div>
        <div class="ia-stat"><span class="ia-stat-num">Auto</span><span class="ia-stat-label">Renewal Reminders</span></div>
        <div class="ia-stat"><span class="ia-stat-num">24/7</span><span class="ia-stat-label">Alert System</span></div>
      </div>
    </div>
  </div>
</section>

<!-- Automated Follow-Ups -->
<section class="ia-section">
  <div class="ia-container ia-row ia-row-reverse">
    <div class="ia-col-text">
      <h2 class="ia-h2">Automate Follow-Ups & Reduce Manual Work</h2>
      <p class="ia-desc">Following up manually with every member or prospect can take up valuable staff time. Gymex helps simplify this process with automated follow-ups, allowing your team to maintain timely communication.</p>
      <ul class="ia-feature-list">
        <li><i class="fa fa-check"></i> Reduce repetitive follow-up work</li>
        <li><i class="fa fa-check"></i> Maintain timely communication</li>
        <li><i class="fa fa-check"></i> Keep important follow-ups from being missed</li>
        <li><i class="fa fa-check"></i> Improve consistency across member communication</li>
        <li><i class="fa fa-check"></i> Give staff more time to focus on important activities</li>
      </ul>
    </div>
    <div class="ia-col-visual">
      <div class="ia-visual-box">
        <div class="ia-stat"><span class="ia-stat-num">Auto</span><span class="ia-stat-label">Follow-Up System</span></div>
        <div class="ia-stat"><span class="ia-stat-num">Zero</span><span class="ia-stat-label">Missed Follow-Ups</span></div>
        <div class="ia-stat"><span class="ia-stat-num">Faster</span><span class="ia-stat-label">Member Response</span></div>
      </div>
    </div>
  </div>
</section>

<!-- Class & Service Notifications -->
<section class="ia-section ia-alt-bg">
  <div class="ia-container">
    <h2 class="ia-h2 ia-text-center">Keep Members Engaged with Class & Service Notifications</h2>
    <p class="ia-desc ia-text-center" style="max-width:700px;margin:0 auto 30px;">Communication shouldn't stop after a member joins. Gymex lets you send push notifications about classes and services, helping you keep members informed about relevant activities.</p>
    <div class="ia-3col">
      <div class="ia-card">
        <div class="ia-card-icon"><i class="fa fa-calendar"></i></div>
        <h3 class="ia-card-title">Class Alerts</h3>
        <p class="ia-card-desc">Notify members about upcoming classes, schedule changes, and new class offerings.</p>
      </div>
      <div class="ia-card">
        <div class="ia-card-icon"><i class="fa fa-star"></i></div>
        <h3 class="ia-card-title">Service Updates</h3>
        <p class="ia-card-desc">Inform members about new services, special offers, and membership upgrades available at your gym.</p>
      </div>
      <div class="ia-card">
        <div class="ia-card-icon"><i class="fa fa-users"></i></div>
        <h3 class="ia-card-title">Trainer Alerts</h3>
        <p class="ia-card-desc">Send appointment confirmation alerts to trainers, helping them stay prepared for sessions.</p>
      </div>
    </div>
  </div>
</section>

<!-- Why Choose Gymex -->
<section class="ia-section">
  <div class="ia-container">
    <h2 class="ia-h2 ia-text-center">Why Choose Gymex for Intelligent Alerts?</h2>
    <div class="ia-why-grid">
      <div class="ia-why-item"><i class="fa fa-check-circle"></i><span>Customized Alerts</span></div>
      <div class="ia-why-item"><i class="fa fa-check-circle"></i><span>SMS Notifications</span></div>
      <div class="ia-why-item"><i class="fa fa-check-circle"></i><span>Email Alerts</span></div>
      <div class="ia-why-item"><i class="fa fa-check-circle"></i><span>App Notifications</span></div>
      <div class="ia-why-item"><i class="fa fa-check-circle"></i><span>Balance & Renewal Alerts</span></div>
      <div class="ia-why-item"><i class="fa fa-check-circle"></i><span>Bill Creation Notifications</span></div>
      <div class="ia-why-item"><i class="fa fa-check-circle"></i><span>Class & Service Updates</span></div>
      <div class="ia-why-item"><i class="fa fa-check-circle"></i><span>Automated Follow-Ups</span></div>
      <div class="ia-why-item"><i class="fa fa-check-circle"></i><span>Trainer Appointment Alerts</span></div>
    </div>
  </div>
</section>
'''

alerts_faqs = [
    ("What is gym reminder software?", "Gym Reminder Software helps fitness businesses manage important alerts and reminders for members and staff. It can reduce repetitive manual communication and help ensure important updates are shared on time."),
    ("What alerts are available in Gymex?", "Gymex supports customized member and staff alerts, balance and renewal payment alerts, bill creation notification SMS, data export alerts, class and service push notifications, and appointment confirmation alerts for trainers."),
    ("Can Gymex send membership renewal reminders?", "Yes. Gymex supports balance and renewal payment alerts to help keep members informed about relevant membership payments."),
    ("Which channels can Gymex use for alerts?", "Gymex supports alerts through SMS, email, and app notifications, depending on the type of communication."),
    ("Can Gymex send alerts to trainers?", "Yes. Gymex supports appointment confirmation alerts for trainers, helping them stay informed about confirmed appointments."),
    ("Does Gymex support automated follow-ups?", "Yes. Gymex provides automated follow-ups to help your team maintain timely communication with members and prospects without manual intervention."),
]

# ═══════════════════════════════════════════
# PAGE 2: Biometric & Access Control
# ═══════════════════════════════════════════

biometric_content = '''
<!-- Biometric & RFID -->
<section class="ia-section">
  <div class="ia-container ia-row">
    <div class="ia-col-text">
      <h2 class="ia-h2">Track Attendance with Biometric & RFID</h2>
      <p class="ia-desc">Manual attendance can slow down check-ins and make member visit records harder to maintain. Gymex Gym Biometric Attendance Software allows you to capture staff and member attendance through biometric and RFID integration.</p>
      <div class="ia-workflow">
        <span class="ia-wf-step">Member Arrives</span>
        <span class="ia-wf-arrow"><i class="fa fa-arrow-right"></i></span>
        <span class="ia-wf-step">Verify</span>
        <span class="ia-wf-arrow"><i class="fa fa-arrow-right"></i></span>
        <span class="ia-wf-step">Check-In</span>
        <span class="ia-wf-arrow"><i class="fa fa-arrow-right"></i></span>
        <span class="ia-wf-step">Recorded</span>
      </div>
    </div>
    <div class="ia-col-visual">
      <div class="ia-visual-box">
        <div class="ia-stat"><span class="ia-stat-num"><i class="fa fa-fingerprint"></i></span><span class="ia-stat-label">Biometric Scan</span></div>
        <div class="ia-stat"><span class="ia-stat-num"><i class="fa fa-id-card"></i></span><span class="ia-stat-label">RFID Tap</span></div>
        <div class="ia-stat"><span class="ia-stat-num"><i class="fa fa-check-circle"></i></span><span class="ia-stat-label">Instant Check-In</span></div>
      </div>
    </div>
  </div>
</section>

<!-- Multiple Check-In Methods -->
<section class="ia-section ia-alt-bg">
  <div class="ia-container">
    <h2 class="ia-h2 ia-text-center">Multiple Ways to Check In</h2>
    <p class="ia-desc ia-text-center" style="max-width:700px;margin:0 auto 30px;">Not every member needs to check in through a biometric device. Gymex supports multiple check-in options for a smoother attendance experience.</p>
    <div class="ia-4col">
      <div class="ia-card">
        <div class="ia-card-icon"><i class="fa fa-fingerprint"></i></div>
        <h3 class="ia-card-title">Biometric</h3>
        <p class="ia-card-desc">Capture attendance through biometric integration for secure, fast check-ins.</p>
      </div>
      <div class="ia-card">
        <div class="ia-card-icon"><i class="fa fa-id-card"></i></div>
        <h3 class="ia-card-title">RFID</h3>
        <p class="ia-card-desc">Allow members and staff to check in using RFID cards or bands.</p>
      </div>
      <div class="ia-card">
        <div class="ia-card-icon"><i class="fa fa-qrcode"></i></div>
        <h3 class="ia-card-title">QR Code</h3>
        <p class="ia-card-desc">Enable member attendance through QR code scanning from the mobile app.</p>
      </div>
      <div class="ia-card">
        <div class="ia-card-icon"><i class="fa fa-pencil"></i></div>
        <h3 class="ia-card-title">Manual Check-In</h3>
        <p class="ia-card-desc">Allow authorized staff to record attendance manually when required.</p>
      </div>
    </div>
  </div>
</section>

<!-- Access Control Rules -->
<section class="ia-section">
  <div class="ia-container ia-row ia-row-reverse">
    <div class="ia-col-text">
      <h2 class="ia-h2">Control Gym Access Based on Membership Rules</h2>
      <p class="ia-desc">Attendance tells you who checked in. Access control helps determine who should be allowed access. Gymex supports access restrictions based on membership type, age, and time.</p>
      <div class="ia-3col" style="margin-top:20px;">
        <div class="ia-mini-card">
          <div class="ia-mini-icon"><i class="fa fa-id-card-o"></i></div>
          <h4>Membership Type</h4>
          <p>Control access according to the membership plan purchased.</p>
        </div>
        <div class="ia-mini-card">
          <div class="ia-mini-icon"><i class="fa fa-birthday-cake"></i></div>
          <h4>Age</h4>
          <p>Apply relevant access restrictions based on member age.</p>
        </div>
        <div class="ia-mini-card">
          <div class="ia-mini-icon"><i class="fa fa-clock-o"></i></div>
          <h4>Time</h4>
          <p>Control access based on permitted timings.</p>
        </div>
      </div>
    </div>
    <div class="ia-col-visual">
      <div class="ia-visual-box">
        <div class="ia-stat"><span class="ia-stat-num"><i class="fa fa-shield"></i></span><span class="ia-stat-label">Access Control</span></div>
        <div class="ia-stat"><span class="ia-stat-num"><i class="fa fa-ban"></i></span><span class="ia-stat-label">Block Defaulters</span></div>
        <div class="ia-stat"><span class="ia-stat-num"><i class="fa fa-building"></i></span><span class="ia-stat-label">Multi-Floor</span></div>
      </div>
    </div>
  </div>
</section>

<!-- Multi-Branch & Floor -->
<section class="ia-section ia-alt-bg">
  <div class="ia-container">
    <h2 class="ia-h2 ia-text-center">Manage Access Across Multiple Floors & Branches</h2>
    <div class="ia-2col">
      <div class="ia-card">
        <div class="ia-card-icon"><i class="fa fa-building"></i></div>
        <h3 class="ia-card-title">Multi-Floor Integration</h3>
        <p class="ia-card-desc">For clubs operating across multiple floors, Gymex supports seamless biometric integration across floors. Manage member movement and access more effectively within larger facilities.</p>
      </div>
      <div class="ia-card">
        <div class="ia-card-icon"><i class="fa fa-sitemap"></i></div>
        <h3 class="ia-card-title">Multi-Branch Reciprocity</h3>
        <p class="ia-card-desc">Members may sometimes need access to more than one location. Gymex supports reciprocity, allowing multi-branch access according to the membership purchased.</p>
      </div>
    </div>
  </div>
</section>

<!-- Why Choose -->
<section class="ia-section">
  <div class="ia-container">
    <h2 class="ia-h2 ia-text-center">Why Choose Gymex for Biometric & Access Control?</h2>
    <div class="ia-why-grid">
      <div class="ia-why-item"><i class="fa fa-check-circle"></i><span>Biometric Attendance</span></div>
      <div class="ia-why-item"><i class="fa fa-check-circle"></i><span>RFID Check-In</span></div>
      <div class="ia-why-item"><i class="fa fa-check-circle"></i><span>QR Code Attendance</span></div>
      <div class="ia-why-item"><i class="fa fa-check-circle"></i><span>Manual Check-In</span></div>
      <div class="ia-why-item"><i class="fa fa-check-circle"></i><span>Membership-Based Access</span></div>
      <div class="ia-why-item"><i class="fa fa-check-circle"></i><span>Age & Time Restrictions</span></div>
      <div class="ia-why-item"><i class="fa fa-check-circle"></i><span>Defaulting Member Control</span></div>
      <div class="ia-why-item"><i class="fa fa-check-circle"></i><span>Multi-Floor Integration</span></div>
      <div class="ia-why-item"><i class="fa fa-check-circle"></i><span>Multi-Branch Reciprocity</span></div>
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
    ("Does Gymex support multiple gym branches?", "Gymex supports reciprocity for multi-branch businesses, allowing eligible members to access different branches according to their purchased membership."),
]

# ═══════════════════════════════════════════
# PAGE 3: Data Analysis & Dashboard
# ═══════════════════════════════════════════

data_content = '''
<!-- Dashboard Overview -->
<section class="ia-section">
  <div class="ia-container ia-row">
    <div class="ia-col-text">
      <h2 class="ia-h2">See Your Gym's Performance at a Glance</h2>
      <p class="ia-desc">Running a gym generates a lot of data, but that data is only useful when you can easily understand what it means. The Gymex Gym Management Dashboard brings important business information together in one clear view.</p>
      <ul class="ia-feature-list">
        <li><i class="fa fa-check"></i> Collections and balances</li>
        <li><i class="fa fa-check"></i> Membership upgrades</li>
        <li><i class="fa fa-check"></i> Daily billing</li>
        <li><i class="fa fa-check"></i> Live members</li>
        <li><i class="fa fa-check"></i> Membership expiry</li>
        <li><i class="fa fa-check"></i> Sales team performance</li>
        <li><i class="fa fa-check"></i> Follow-up calls</li>
      </ul>
    </div>
    <div class="ia-col-visual">
      <div class="ia-visual-box">
        <div class="ia-stat"><span class="ia-stat-num">50+</span><span class="ia-stat-label">Business Reports</span></div>
        <div class="ia-stat"><span class="ia-stat-num"><i class="fa fa-tachometer"></i></span><span class="ia-stat-label">Live Dashboard</span></div>
        <div class="ia-stat"><span class="ia-stat-num"><i class="fa fa-bar-chart"></i></span><span class="ia-stat-label">Real-Time Analytics</span></div>
      </div>
    </div>
  </div>
</section>

<!-- 45+ Reports -->
<section class="ia-section ia-alt-bg">
  <div class="ia-container">
    <h2 class="ia-h2 ia-text-center">Explore 50+ Business Reports</h2>
    <p class="ia-desc ia-text-center" style="max-width:700px;margin:0 auto 30px;">Different areas of your gym require different insights. Gymex provides 50+ business reports to help you track financial activity, members, employees, sales, leads, commissions, and attendance.</p>
    <div class="ia-4col">
      <div class="ia-card">
        <div class="ia-card-icon"><i class="fa fa-inr"></i></div>
        <h3 class="ia-card-title">Financial Reports</h3>
        <p class="ia-card-desc">Bills & payments, expenses, revenue, income vs. expense, collections, balance recovery, write-offs.</p>
      </div>
      <div class="ia-card">
        <div class="ia-card-icon"><i class="fa fa-users"></i></div>
        <h3 class="ia-card-title">Member Reports</h3>
        <p class="ia-card-desc">Live member tracking, irregular members, suspended, membership expiry, expected renewals.</p>
      </div>
      <div class="ia-card">
        <div class="ia-card-icon"><i class="fa fa-line-chart"></i></div>
        <h3 class="ia-card-title">Sales & Lead Reports</h3>
        <p class="ia-card-desc">Sales activities, rep performance, targets vs achievements, channel-wise leads, follow-ups.</p>
      </div>
      <div class="ia-card">
        <div class="ia-card-icon"><i class="fa fa-user-plus"></i></div>
        <h3 class="ia-card-title">Commission Reports</h3>
        <p class="ia-card-desc">Trainer commissions, sales staff commissions, conditional commission, customizable reports.</p>
      </div>
    </div>
  </div>
</section>

<!-- KPI Dashboard -->
<section class="ia-section">
  <div class="ia-container">
    <h2 class="ia-h2 ia-text-center">Track the KPIs That Matter to Your Gym</h2>
    <p class="ia-desc ia-text-center" style="max-width:700px;margin:0 auto 30px;">You shouldn't have to go through dozens of records just to understand whether your gym is moving in the right direction. Gymex brings important performance information into dashboards.</p>
    <div class="ia-4col">
      <div class="ia-card">
        <div class="ia-card-icon"><i class="fa fa-bullseye"></i></div>
        <h3 class="ia-card-title">Sales Performance</h3>
        <p class="ia-card-desc">Compare sales representative targets with achievements and monitor overall sales activity.</p>
      </div>
      <div class="ia-card">
        <div class="ia-card-icon"><i class="fa fa-heartbeat"></i></div>
        <h3 class="ia-card-title">Member Activity</h3>
        <p class="ia-card-desc">Track live, irregular, suspended, expiring, and due-upgrade members at a glance.</p>
      </div>
      <div class="ia-card">
        <div class="ia-card-icon"><i class="fa fa-refresh"></i></div>
        <h3 class="ia-card-title">Renewals</h3>
        <p class="ia-card-desc">Get visibility into upcoming renewals so your team knows which memberships need attention.</p>
      </div>
      <div class="ia-card">
        <div class="ia-card-icon"><i class="fa fa-money"></i></div>
        <h3 class="ia-card-title">Collections</h3>
        <p class="ia-card-desc">Monitor collections, balances, billing, and other relevant financial information.</p>
      </div>
    </div>
  </div>
</section>

<!-- Revenue & Expenses -->
<section class="ia-section ia-alt-bg">
  <div class="ia-container ia-row ia-row-reverse">
    <div class="ia-col-text">
      <h2 class="ia-h2">Understand Revenue, Expenses & Collections</h2>
      <p class="ia-desc">Good business decisions require visibility into both income and spending. Gymex provides reports covering revenue, expenses, petty cash, bills and payments, collections, income vs. expense, and balance recovery.</p>
      <div class="ia-workflow">
        <span class="ia-wf-step">Track</span>
        <span class="ia-wf-arrow"><i class="fa fa-arrow-right"></i></span>
        <span class="ia-wf-step">Analyze</span>
        <span class="ia-wf-arrow"><i class="fa fa-arrow-right"></i></span>
        <span class="ia-wf-step">Identify</span>
        <span class="ia-wf-arrow"><i class="fa fa-arrow-right"></i></span>
        <span class="ia-wf-step">Act</span>
        <span class="ia-wf-arrow"><i class="fa fa-arrow-right"></i></span>
        <span class="ia-wf-step">Improve</span>
      </div>
    </div>
    <div class="ia-col-visual">
      <div class="ia-visual-box">
        <div class="ia-stat"><span class="ia-stat-num"><i class="fa fa-line-chart"></i></span><span class="ia-stat-label">Revenue Tracking</span></div>
        <div class="ia-stat"><span class="ia-stat-num"><i class="fa fa-pie-chart"></i></span><span class="ia-stat-label">Expense Reports</span></div>
        <div class="ia-stat"><span class="ia-stat-num"><i class="fa fa-database"></i></span><span class="ia-stat-label">Collection Data</span></div>
      </div>
    </div>
  </div>
</section>

<!-- Why Choose -->
<section class="ia-section">
  <div class="ia-container">
    <h2 class="ia-h2 ia-text-center">Why Choose Gymex for Reports & Analytics?</h2>
    <div class="ia-why-grid">
      <div class="ia-why-item"><i class="fa fa-check-circle"></i><span>Interactive Dashboards</span></div>
      <div class="ia-why-item"><i class="fa fa-check-circle"></i><span>50+ Business Reports</span></div>
      <div class="ia-why-item"><i class="fa fa-check-circle"></i><span>Sales Performance</span></div>
      <div class="ia-why-item"><i class="fa fa-check-circle"></i><span>Member Insights</span></div>
      <div class="ia-why-item"><i class="fa fa-check-circle"></i><span>Financial Visibility</span></div>
      <div class="ia-why-item"><i class="fa fa-check-circle"></i><span>Lead Analysis</span></div>
      <div class="ia-why-item"><i class="fa fa-check-circle"></i><span>Attendance Reports</span></div>
      <div class="ia-why-item"><i class="fa fa-check-circle"></i><span>Commission Reports</span></div>
    </div>
  </div>
</section>
'''

data_faqs = [
    ("What is gym analytics software?", "Gym Analytics Software helps gym owners and managers analyze business information such as sales, members, attendance, revenue, collections, renewals, and other operational data through dashboards and reports."),
    ("What reports are available in Gymex?", "Gymex provides 50+ business reports, including bills and payments, expenses, revenue, income vs. expense, trainer and sales staff commissions, collections, attendance, leads, sales activities, balance recovery, and other operational reports."),
    ("What is a gym management dashboard?", "A Gym Management Dashboard provides a visual overview of important business information. Gymex dashboards help management monitor collections, balances, membership activity, sales performance, renewals, billing, and other relevant metrics."),
    ("Can Gymex track sales team performance?", "Yes. Gymex provides visibility into sales representative-wise targets versus achievements, consolidated sales activities, follow-up calls, and other relevant sales information."),
    ("Can Gymex help track membership renewals?", "Yes. Gymex provides expected renewal visibility along with information about today's membership expiries, suspended members, due-upgrade members, irregular members, and live members."),
    ("Does Gymex provide financial reports?", "Yes. Gymex provides reports covering bills and payments, expenses, petty cash, revenue, income versus expense, collections, balance recovery, and other relevant financial information."),
]

# ═══════════════════════════════════════════
# Generate all pages
# ═══════════════════════════════════════════

pages = [
    {
        "dir": "intelligent-alerts",
        "file": "intelligent-alerts-reminders.html",
        "title": "Gym Reminder Software & Intelligent Alerts | Gymex",
        "meta_desc": "Send customized gym alerts and reminders for members and staff with Gymex. Manage renewal, balance, billing, appointment and class notifications from one platform.",
        "meta_keywords": "Gym Reminder Software, Gym Alerts and Notifications Software, Gym Membership Reminder Software, Automated Gym Reminders, Gym Payment Reminder Software, Gym Notification Software",
        "og_title": "Gym Reminder Software & Intelligent Alerts | Gymex",
        "og_desc": "Send customized gym alerts and reminders for members and staff with Gymex.",
        "label": "GYM ALERTS & REMINDER SOFTWARE",
        "hero_title": "Keep Members Updated with Intelligent Alerts",
        "hero_desc": "Send timely personalized alerts, reminders, and automated follow-ups with Gymex. Keep members informed about renewals, payments, appointments, classes, and other important updates from one connected platform.",
        "content": alerts_content,
        "faqs": alerts_faqs,
    },
    {
        "dir": "biometric-access-control",
        "file": "biometric-access-control.html",
        "title": "Gym Biometric Attendance & Access Control Software | Gymex",
        "meta_desc": "Automate gym attendance with biometric, RFID and QR check-ins. Control member access by membership, age and time with Gymex biometric and access control software.",
        "meta_keywords": "Gym Biometric Attendance Software, Gym Access Control Software, Biometric Gym Software, Gym Attendance Software, Gym Check-In Software, Gym Attendance Tracking Software",
        "og_title": "Gym Biometric Attendance & Access Control Software | Gymex",
        "og_desc": "Automate gym attendance with biometric, RFID and QR check-ins.",
        "label": "BIOMETRIC & ACCESS CONTROL SOFTWARE",
        "hero_title": "Simplify Gym Check-Ins & Control Member Access",
        "hero_desc": "Track staff and member attendance with biometric, RFID, QR code, and manual check-ins. Gymex helps you manage facility access based on membership rules while keeping attendance and access control connected in one platform.",
        "content": biometric_content,
        "faqs": biometric_faqs,
    },
    {
        "dir": "data-analysis-dashboard",
        "file": "data-analysis-dashboard.html",
        "title": "Gym Analytics Software, Reports & Dashboard | Gymex",
        "meta_desc": "Track gym performance with interactive dashboards and 50+ business reports. Analyze sales, revenue, members, attendance, renewals, expenses and more with Gymex.",
        "meta_keywords": "Gym Analytics Software, Gym Reporting Software, Gym Management Dashboard, Gym Analytics Dashboard, Gym Business Analytics Software, Gym KPI Dashboard",
        "og_title": "Gym Analytics Software, Reports & Dashboard | Gymex",
        "og_desc": "Track gym performance with interactive dashboards and 50+ business reports.",
        "label": "GYM ANALYTICS & REPORTING SOFTWARE",
        "hero_title": "Turn Your Gym Data into Actionable Insights",
        "hero_desc": "Track your gym's performance with interactive dashboards and 50+ business reports. Gymex brings your sales, collections, members, attendance, renewals, expenses, and other key business data together so you can make informed decisions.",
        "content": data_content,
        "faqs": data_faqs,
    },
]

for p in pages:
    html = build_page(
        p["title"], p["meta_desc"], p["meta_keywords"], p["og_title"], p["og_desc"],
        p["label"], p["hero_title"], p["hero_desc"], p["faqs"], p["content"]
    )
    out_dir = os.path.join(BASE, p["dir"])
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, p["file"]), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Created: {p['dir']}/{p['file']}")

print("Done! All 3 pages created.")
