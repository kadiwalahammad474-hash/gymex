#!/usr/bin/env python3
"""Rebuild all 3 feature pages with EXACT member management inline style."""

import sys
sys.stdout.reconfigure(encoding='utf-8')

# Read nav from member management
with open("member-management/member-management.html", "r", encoding="utf-8") as f:
    mm = f.read()

nav_start = mm.find("<nav")
nav_end = mm.find("</nav>") + 6
NAV = mm[nav_start:nav_end]

footer_start = mm.find('<div style="background:#0b1a3d; padding:0;">')
footer_end = mm.find("</html>") + 7
FOOTER = mm[footer_start:footer_end]

# Read modal from member management
modal_start = mm.find('<!-- Backdrop')
if modal_start < 0:
    modal_start = mm.find('<div class="backdrop"')
MODAL = mm[modal_start:] if modal_start > 0 else ""

# Common CSS (from member management)
CSS = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<link rel="stylesheet" href="../style.css">
<style>
.sm-faq-item { list-style: none; }
.sm-faq-item summary { cursor: pointer; font-weight: 700; font-size: 15px; color: #111; padding: 16px 20px; background: #f8f9fc; border: 1px solid #e5e7eb; border-radius: 10px; display: flex; justify-content: space-between; align-items: center; }
.sm-faq-item summary::-webkit-details-marker { display: none; }
.sm-faq-item summary::after { content: '\\f078'; font-family: FontAwesome; font-size: 12px; color: #999; transition: transform .2s; }
.sm-faq-item[open] summary::after { transform: rotate(180deg); }
.sm-faq-item p { padding: 16px 20px; font-size: 14px; color: #555; line-height: 1.8; margin: 0; background: #fff; border: 1px solid #e5e7eb; border-top: 0; border-radius: 0 0 10px 10px; }
</style>
"""

def page(title, desc, badge, h1, hero_desc, sections, faqs, cta_h2, cta_p, cta_italic):
    faq_html = ""
    for q, a in faqs:
        faq_html += f'<div><details class="sm-faq-item"><summary>{q}</summary><p>{a}</p></details></div>\n'
    
    sec_html = "\n".join(sections)
    
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
{CSS}
</head>
<body>
{NAV}

<div class="sm">

<!-- HERO -->
<section class="sm-hero">
<div class="sm-hero-grid">
<div>
<div class="sm-label">{badge}</div>
<h1>{h1}</h1>
<p class="sm-desc">{hero_desc}</p>
<div class="sm-hero-cta">
<button class="mm-btn mm-btn-orange magnetic-btn open-modal-btn">Get Your Free Demo <i class="fa fa-arrow-up"></i></button>
</div>
</div>
<div class="sm-hero-img">
<div style="background:linear-gradient(135deg,#e8f0fe,#dbe8ff);border-radius:20px;padding:40px;display:flex;align-items:center;justify-content:center;min-height:320px;">
<div style="text-align:center;"><i class="fa fa-shield" style="font-size:80px;color:var(--blue,#028ece);opacity:0.3;"></i></div>
</div>
</div>
</div>
</section>

{sec_html}

<!-- CTA -->
<section style="padding:60px 24px; background:#1565C0;">
<div style="max-width:800px; margin:0 auto; text-align:center;">
<h2 style="font-size:28px; font-weight:800; color:#fff; margin-bottom:16px;">{cta_h2}</h2>
<p style="font-size:16px; color:rgba(255,255,255,.85); line-height:1.8; margin-bottom:10px;">{cta_p}</p>
<p style="font-size:14px; color:rgba(255,255,255,.6); line-height:1.8; margin-bottom:30px; font-style:italic;">{cta_italic}</p>
<button class="mm-btn mm-btn-orange magnetic-btn open-modal-btn">Get Your Free Demo <i class="fa fa-arrow-up"></i></button>
</div>
</section>

<!-- FAQ -->
<section style="padding:60px 24px; background:#fff;">
<div style="max-width:800px; margin:0 auto;">
<h2 style="font-size:32px; font-weight:800; color:#111; text-align:center; margin-bottom:36px;">Frequently Asked Questions</h2>
<div style="display:flex; flex-direction:column; gap:12px;">
{faq_html}
</div>
</div>
</section>

</div>

{FOOTER}
{MODAL}
<script src="../javascript.js"></script>
<script>
document.querySelectorAll('.open-modal-btn').forEach(function(b){{b.addEventListener('click',function(e){{e.preventDefault();document.getElementById('divemailpopup').classList.add('show');document.body.style.overflow='hidden';}});}});
document.getElementById('close-contact-modal').addEventListener('click',function(){{document.getElementById('divemailpopup').classList.remove('show');document.body.style.overflow='auto';document.getElementById('emailsuccessmsg').style.display='none';document.getElementById('form-body').style.display='block';}});
document.getElementById('divemailpopup').addEventListener('click',function(e){{if(e.target===this){{this.classList.remove('show');document.body.style.overflow='auto';}}}});
document.querySelector('.send-again-btn').addEventListener('click',function(){{document.getElementById('emailsuccessmsg').style.display='none';document.getElementById('form-body').style.display='block';}});
emailjs.init('AmP09sgXBaIgn9Juz');
var pi=document.getElementById('number');
if(pi){{var iti=window.intlTelInput(pi,{{utilsScript:'https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js',separateDialCode:true,initialCountry:'in'}});}}
document.getElementById('contact-form').onsubmit=function(e){{e.preventDefault();document.getElementById('loader').classList.add('show');document.getElementById('divemailpopup').classList.add('show');var fn=iti?iti.getNumber():pi.value;emailjs.send('service_1o6wljl','template_6dewzmp',{{firstname:document.getElementById('first-name').value,lastname:document.getElementById('last-name').value,company:document.getElementById('company').value,email:document.getElementById('email').value,phonenumber:fn,message:this.message.value}}).then(function(){{document.getElementById('loader').classList.remove('show');document.getElementById('form-body').style.display='none';document.getElementById('emailsuccessmsg').style.display='block';}},function(){{document.getElementById('loader').classList.remove('show');alert('Thank you! Your demo request has been submitted.');document.getElementById('divemailpopup').classList.remove('show');document.body.style.overflow='auto';}});}};
</script>
</body>
</html>'''

# Helper: checkmark item
def check(text):
    return f'<div style="display:flex; align-items:center; gap:12px; padding:12px 16px; background:#f8f9fc; border-radius:8px;"><i class="fa fa-check-circle" style="color:#1565C0; font-size:16px;"></i><span style="font-size:14px; color:#333;">{text}</span></div>'

# Helper: icon card
def icon_card(icon, title, desc):
    return f'<div style="background:#fff; border:1px solid #e5e7eb; border-radius:12px; padding:24px; display:flex; align-items:flex-start; gap:14px;"><div style="width:40px; height:40px; background:#e8f0fe; border-radius:10px; display:flex; align-items:center; justify-content:center; flex-shrink:0;"><i class="fa {icon}" style="color:#1565C0; font-size:16px;"></i></div><div><h3 style="font-size:15px; font-weight:700; color:#111; margin-bottom:6px;">{title}</h3><p style="font-size:13px; color:#666; margin:0;">{desc}</p></div></div>'

# Helper: simple card
def simple_card(title, desc):
    return f'<div style="background:#fff; border:1px solid #e5e7eb; border-radius:12px; padding:22px; text-align:center;"><h3 style="font-size:14px; font-weight:700; color:#111; margin-bottom:4px;">{title}</h3><p style="font-size:12px; color:#888; margin:0;">{desc}</p></div>'

# Helper: green check item
def green_check(text):
    return f'<div style="display:flex; align-items:center; gap:10px; padding:12px 20px; background:#f0fdf4; border-radius:10px; border:1px solid #bbf7d0;"><i class="fa fa-check-circle" style="color:#22c55e; font-size:18px;"></i><span style="font-size:14px; color:#333;">{text}</span></div>'

# Helper: section
def sec(bg, title, subtitle, content_html):
    return f'''<section style="padding:60px 24px; background:{bg};">
<div style="max-width:1200px; margin:0 auto;">
<h2 style="font-size:32px; font-weight:800; color:#111; text-align:center; margin-bottom:24px;">{title}</h2>
<p style="font-size:16px; color:#555; line-height:1.8; max-width:800px; margin:0 auto 36px; text-align:center;">{subtitle}</p>
{content_html}
</div>
</section>'''

def grid(items, minmax="260px"):
    return f'<div style="display:grid; grid-template-columns:repeat(auto-fit, minmax({minmax},1fr)); gap:24px; max-width:1000px; margin:0 auto;">{"".join(items)}</div>'

def grid_check(items, minmax="240px"):
    return f'<div style="display:grid; grid-template-columns:repeat(auto-fit, minmax({minmax},1fr)); gap:16px; max-width:900px; margin:0 auto;">{"".join(items)}</div>'

def flex_wrap(items):
    return f'<div style="display:flex; flex-wrap:wrap; gap:14px; max-width:900px; margin:0 auto; justify-content:center;">{"".join(items)}</div>'

# ═══════════════════════════════════════════════════════════════
# 1. BIOMETRIC & ACCESS CONTROL
# ═══════════════════════════════════════════════════════════════
bio_secs = [
    sec("#fff", "Track Attendance with Biometric & RFID", "Manual attendance can slow down check-ins and make member visit records harder to maintain. Gymex Gym Biometric Attendance Software allows you to capture staff and member attendance through biometric and RFID integration.", grid([
        icon_card("fa-fingerprint", "Biometric Check-In", "Capture attendance through fingerprint or face recognition integration."),
        icon_card("fa-id-card", "RFID Check-In", "Allow members and staff to check in using RFID cards."),
        icon_card("fa-qrcode", "QR Code Check-In", "Enable member attendance through QR code scanning from the mobile app."),
        icon_card("fa-clipboard-check", "Manual Check-In", "Allow authorized staff to record attendance manually when required."),
    ])),
    
    sec("#f8f9fc", "Control Gym Access Based on Membership Rules", "Attendance tells you who checked in. Access control helps determine who should be allowed access. Gymex Gym Access Control Software allows you to apply access restrictions based on:", grid([
        icon_card("fa-credit-card", "Membership Type", "Control access according to the membership or plan purchased by the member."),
        icon_card("fa-birthday-cake", "Age", "Apply relevant access restrictions based on member age."),
        icon_card("fa-clock-o", "Time", "Control access based on permitted timings."),
    ], "280px")),
    
    sec("#fff", "Block Access for Defaulting Members", "Access shouldn't continue in the same way when a member no longer meets the required membership or payment conditions. Gymex helps you block defaulting members, giving your team greater control over facility access.", grid([
        icon_card("fa-ban", "Block Defaulting Members", "Restrict access for members who do not meet applicable membership or payment conditions."),
        icon_card("fa-building", "Multi-Floor Integration", "Manage biometric attendance and access across multiple floors for larger facilities."),
        icon_card("fa-code-fork", "Multi-Branch Reciprocity", "Allow members to access eligible branches according to their purchased membership."),
    ], "280px")),
    
    sec("#f8f9fc", "Connect Membership, Access & Attendance", "One of the biggest advantages of using an integrated Gym Biometric Attendance System is that attendance doesn't have to operate separately from member information. Gymex connects the process so your team maintains better control over who enters your facilities.", grid([
        simple_card("Member Profile", "Complete member information in one place"),
        simple_card("Membership Type", "Plan and access level verification"),
        simple_card("Access Rules", "Age, time, and membership-based restrictions"),
        simple_card("Check-In", "Biometric, RFID, QR, or manual"),
        simple_card("Attendance", "Connected attendance records"),
    ], "200px")),
    
    sec("#fff", "Keep Staff & Member Attendance Organized", "Gymex isn't limited to member check-ins. You can also capture staff attendance, helping you maintain attendance information for your team alongside member attendance. A connected Gym Attendance Software process makes it easier to maintain organized attendance records instead of relying on separate registers or disconnected systems.", grid([
        icon_card("fa-users", "Staff Attendance", "Capture staff attendance alongside member attendance in one connected system."),
        icon_card("fa-bar-chart", "Visit History", "View individual member visit history and attendance patterns."),
        icon_card("fa-bell-slash", "Inactive Member Detection", "Identify inactive members early and take action."),
    ], "280px")),
    
    sec("#f8f9fc", "Why Choose Gymex for Biometric & Access Control?", "Gymex brings attendance, member information, and facility access together within your gym management system.", grid([
        simple_card("Biometric Attendance", "Capture attendance through biometric integration"),
        simple_card("RFID Check-In", "Provide RFID-based attendance for convenient check-ins"),
        simple_card("QR Code Attendance", "Allow members to record attendance using QR code scanning"),
        simple_card("Manual Check-In", "Give authorized staff flexibility to record attendance manually"),
        simple_card("Membership-Based Access", "Control facility access according to membership purchased"),
        simple_card("Age & Time Restrictions", "Set access restrictions based on age and permitted timings"),
        simple_card("Defaulting Member Control", "Restrict access for members who don't meet conditions"),
        simple_card("Multi-Floor Integration", "Manage attendance across multiple floors"),
        simple_card("Multi-Branch Reciprocity", "Allow members to access eligible branches"),
    ], "220px")),
]

bio_faqs = [
    ("What is gym biometric attendance software?", "Gym Biometric Attendance Software helps gyms record staff and member attendance using biometric identification. It reduces dependence on manual attendance registers and keeps check-in information more organized."),
    ("Does Gymex support RFID attendance?", "Yes. Gymex supports attendance through RFID and biometric integration, giving gyms multiple options for recording staff and member check-ins."),
    ("Can members check in using a QR code?", "Yes. Gymex supports QR code scanning for member attendance through the mobile app, providing members with a convenient check-in option."),
    ("What is gym access control software?", "Gym Access Control Software helps fitness businesses manage who can access their facilities based on defined rules. Gymex supports access restrictions based on membership type, age, and time."),
    ("Can Gymex restrict access for defaulting members?", "Yes. Gymex provides the ability to block defaulting members, helping fitness businesses maintain better control over facility access."),
    ("Does Gymex support multiple gym branches?", "Gymex supports reciprocity for multi-branch businesses, allowing eligible members to access different branches according to their purchased membership."),
]

bio = page(
    "Gym Biometric Attendance & Access Control Software | Gymex",
    "Automate gym attendance with biometric, RFID and QR check-ins. Control member access by membership, age and time with Gymex biometric and access control software.",
    "BIOMETRIC & ACCESS CONTROL SOFTWARE",
    "Simplify Gym Check-Ins & Control Member Access",
    "Track staff and member attendance with biometric, RFID, QR code, and manual check-ins. Gymex helps you manage facility access based on membership rules while keeping attendance and access control connected in one platform.",
    bio_secs, bio_faqs,
    "Make Every Check-In Smarter",
    "Simplify attendance and maintain better control over facility access with Gymex.",
    "Biometric. RFID. QR Check-In. Smarter Access Control."
)

with open("biometric-access-control/biometric-access-control.html", "w", encoding="utf-8") as f:
    f.write(bio)
print("Done: Biometric page")

# ═══════════════════════════════════════════════════════════════
# 2. DATA ANALYSIS & DASHBOARD
# ═══════════════════════════════════════════════════════════════
da_secs = [
    sec("#fff", "See Your Gym's Performance at a Glance", "Gymex keeps your key business metrics connected in one dashboard so you can quickly understand how your gym is performing.", grid([
        icon_card("fa-inr", "Collections & Balances", "View total payments received, outstanding dues, and overall collection status."),
        icon_card("fa-arrow-up", "Membership Upgrades", "Track membership upgrades and plan changes across your gym."),
        icon_card("fa-file-text", "Daily Billing", "Monitor daily billing activity and revenue trends."),
        icon_card("fa-users", "Live Members", "See current active members and membership status at a glance."),
        icon_card("fa-calendar-times-o", "Membership Expiry", "Track upcoming expiries and manage renewals proactively."),
        icon_card("fa-refresh", "Expected Renewals", "View expected renewals and plan follow-ups accordingly."),
        icon_card("fa-trophy", "Sales Performance", "Monitor lead conversion rates and sales team performance."),
        icon_card("fa-phone", "Follow-up Calls", "Track follow-up call activity and lead engagement."),
        icon_card("fa-check-circle", "Approval Requests", "Monitor pending approval requests and manage workflows."),
    ], "240px")),
    
    sec("#f8f9fc", "Explore 50+ Business Reports", "Gymex provides detailed reports across different areas of your gym business.", grid([
        icon_card("fa-pie-chart", "Financial Reports", "Revenue, collections, payments, dues, GST, and tax-related reports for complete financial visibility."),
        icon_card("fa-users", "Member & Attendance Reports", "Member activity, attendance patterns, visit frequency, and membership status reports."),
        icon_card("fa-bullseye", "Sales & Lead Reports", "Lead conversion, sales performance, follow-up tracking, and pipeline reports."),
        icon_card("fa-percent", "Commission & Staff Reports", "Trainer commissions, staff performance, and payroll-related reports."),
    ])),
    
    sec("#fff", "Track the KPIs That Matter", "Key performance indicators help you understand what's working and where improvements are needed.", grid([
        simple_card("Sales Performance", "Track lead conversion rates and revenue targets"),
        simple_card("Member Activity", "Monitor check-in frequency and engagement levels"),
        simple_card("Renewals", "Track renewal rates and upcoming expiries"),
        simple_card("Collections", "Monitor payment collections and outstanding dues"),
        simple_card("Leads & Follow-Ups", "Track lead pipeline and follow-up activity"),
    ], "200px")),
    
    sec("#f8f9fc", "Monitor Sales Team Performance", "Track your sales team's activity, conversions, and revenue contribution through dedicated reports. Gymex provides detailed sales team reports that help you understand individual and team performance.", grid([
        icon_card("fa-line-chart", "Lead Conversion", "Track how leads move through your sales pipeline."),
        icon_card("fa-tasks", "Follow-up Tracking", "Monitor follow-up activity and engagement with prospects."),
        icon_card("fa-trophy", "Revenue Contribution", "See which team members drive the most revenue."),
    ], "280px")),
    
    sec("#fff", "Why Choose Gymex for Analytics?", "Gymex brings data, reports, and dashboards together within your gym management system.", grid([
        simple_card("50+ Business Reports", "Comprehensive reports across all business areas"),
        simple_card("Real-Time Dashboard", "Live metrics and KPIs at your fingertips"),
        simple_card("Revenue Tracking", "Detailed financial visibility and trends"),
        simple_card("Member Analytics", "Attendance, engagement, and retention insights"),
        simple_card("Sales Reports", "Lead conversion and team performance tracking"),
        simple_card("Data Export", "Export reports for sharing and analysis"),
    ], "220px")),
]

da_faqs = [
    ("What is gym analytics software?", "Gym analytics software helps fitness businesses track performance through dashboards, reports, and key metrics covering revenue, members, attendance, and sales."),
    ("What reports does Gymex provide?", "Gymex provides 50+ business reports including financial, member, attendance, sales, lead, commission, and staff reports."),
    ("Can I track revenue and collections?", "Yes. Gymex provides detailed financial reports covering revenue, collections, outstanding dues, and payment trends."),
    ("Does Gymex track sales team performance?", "Yes. Gymex provides sales team reports covering lead conversion, follow-up activity, and revenue contribution."),
    ("Can I export reports from Gymex?", "Yes. Gymex supports data export for most reports, helping you share insights with your team."),
]

da = page(
    "Gym Analytics Software, Reports & Dashboard | Gymex",
    "Track your gym's performance with 50+ business reports, dashboards, and KPIs. Monitor revenue, members, attendance, and sales with Gymex analytics.",
    "GYM ANALYTICS & REPORTING SOFTWARE",
    "Turn Your Gym Data into Actionable Insights",
    "Track your gym's performance with 50+ business reports, interactive dashboards, and key performance indicators — all in one connected platform.",
    da_secs, da_faqs,
    "Make Data-Driven Decisions",
    "Understand your gym business better with real-time analytics and detailed reports from Gymex.",
    "Track. Analyze. Grow. Succeed."
)

with open("data-analysis-dashboard/data-analysis-dashboard.html", "w", encoding="utf-8") as f:
    f.write(da)
print("Done: Data Analysis page")

# ═══════════════════════════════════════════════════════════════
# 3. INTELLIGENT ALERTS & REMINDERS
# ═══════════════════════════════════════════════════════════════
ia_secs = [
    sec("#fff", "Create Customized Alerts for Members", "Different members may need different updates at the right time. Gymex lets you create customized alerts for members, helping your fitness business keep important communication organized and timely.", grid([
        icon_card("fa-bell", "Customized Alerts", "Create relevant alerts for members and staff based on their needs."),
        icon_card("fa-users", "Member Targeting", "Select specific members or groups to receive relevant notifications."),
        icon_card("fa-paper-plane", "Timely Delivery", "Send alerts at the right time to keep members informed."),
    ], "280px")),
    
    sec("#f8f9fc", "Send Alerts Across Multiple Channels", "Reach members through convenient communication channels. Gymex supports alerts through SMS, email, and app notifications, giving your business multiple ways to communicate important information.", grid([
        icon_card("fa-commenting", "SMS Alerts", "Send important updates directly through SMS to members."),
        icon_card("fa-envelope", "Email Alerts", "Keep members informed through email communication."),
        icon_card("fa-mobile", "App Notifications", "Send notifications through the app for timely updates."),
    ], "280px")),
    
    sec("#fff", "Stay Ahead of Balance & Renewal Payments", "Membership renewals and outstanding balances are important to your gym's day-to-day revenue. Gymex allows you to send balance and renewal payment alerts, helping members stay informed about upcoming or pending payments.", grid([
        simple_card("Payment Due Alerts", "Notify members about upcoming payments"),
        simple_card("Renewal Reminders", "Send reminders before membership expires"),
        simple_card("Outstanding Dues", "Alert members about unpaid balances"),
        simple_card("Confirmation Notifications", "Confirm payments received instantly"),
    ], "220px")),
    
    sec("#f8f9fc", "Class, Billing & Operational Alerts", "Gymex supports alerts for classes, services, billing, and operational activities.", grid([
        icon_card("fa-calendar-check-o", "Class & Service Notifications", "Send push notifications about classes and services to keep members engaged."),
        icon_card("fa-file-text", "Bill Creation Notifications", "Keep members informed when their bills are generated automatically."),
        icon_card("fa-building", "Operational Alerts", "Data export alerts and appointment confirmation alerts for trainers."),
    ], "280px")),
    
    sec("#fff", "Automate Follow-Ups & Reduce Manual Work", "Following up manually with every member or prospect can take up valuable staff time. Gymex helps simplify this process with automated follow-ups, allowing your team to maintain timely communication without depending on repeated manual reminders.", grid_check([
        check("Reduce repetitive follow-up work"),
        check("Maintain timely communication"),
        check("Keep important follow-ups from being missed"),
        check("Improve consistency across member communication"),
        check("Give staff more time to focus on important activities"),
    ])),
    
    sec("#f8f9fc", "One Alert System for Everyday Communication", "Instead of relying on separate reminders and repeated manual communication, Gymex brings important member alerts and reminders together within your gym management system.", grid([
        simple_card("Membership", "Alerts for membership updates"),
        simple_card("Payments", "Payment due and confirmation alerts"),
        simple_card("Billing", "Bill creation notifications"),
        simple_card("Renewals", "Renewal reminder alerts"),
        simple_card("Classes", "Class booking confirmations"),
        simple_card("Appointments", "Appointment confirmation alerts"),
    ], "200px")),
    
    sec("#fff", "Why Choose Gymex for Intelligent Alerts?", "Gymex brings alerts, reminders, and notifications together within your gym management system.", grid([
        simple_card("Customized Alerts", "Create relevant alerts for members and staff"),
        simple_card("SMS Notifications", "Send important updates directly through SMS"),
        simple_card("Email Alerts", "Communicate relevant information through email"),
        simple_card("App Notifications", "Keep users updated through app-based notifications"),
        simple_card("Balance & Renewal Alerts", "Remind members about balances and renewals"),
        simple_card("Bill Creation Notifications", "Send SMS notifications when bills are created"),
        simple_card("Class & Service Updates", "Use push notifications to keep members engaged"),
        simple_card("Data Export Alerts", "Keep relevant staff informed about data export activity"),
        simple_card("Trainer Appointment Alerts", "Send appointment confirmation alerts to trainers"),
    ], "220px")),
]

ia_faqs = [
    ("What is gym reminder software?", "Gym Reminder Software helps fitness businesses manage important alerts and reminders for members and staff. It can reduce repetitive manual communication and help ensure important updates are shared on time."),
    ("What alerts are available in Gymex?", "Gymex supports customized member and staff alerts, balance and renewal payment alerts, bill creation notification SMS, data export alerts, class and service push notifications, and appointment confirmation alerts for trainers."),
    ("Can Gymex send membership renewal reminders?", "Yes. Gymex supports balance and renewal payment alerts to help keep members informed about relevant membership payments."),
    ("Which channels can Gymex use for alerts?", "Gymex supports alerts through SMS, email, and app notifications, depending on the type of communication."),
    ("Can Gymex send alerts to trainers?", "Yes. Gymex supports appointment confirmation alerts for trainers, helping them stay informed about confirmed appointments."),
]

ia = page(
    "Gym Reminder Software & Intelligent Alerts | Gymex",
    "Send customized gym alerts and reminders for members and staff with Gymex. Manage renewal, balance, billing, appointment and class notifications from one platform.",
    "GYM ALERTS & REMINDER SOFTWARE",
    "Keep Members Updated with Intelligent Alerts",
    "Send timely personalized alerts, reminders, and automated follow-ups with Gymex. Keep members informed about renewals, payments, appointments, classes, and other important updates from one connected platform.",
    ia_secs, ia_faqs,
    "Make Every Important Update Count",
    "Keep members engaged and your team informed with intelligent alerts from Gymex.",
    "Customize. Notify. Remind. Engage."
)

with open("intelligent-alerts/intelligent-alerts-reminders.html", "w", encoding="utf-8") as f:
    f.write(ia)
print("Done: Intelligent Alerts page")

print("\nAll 3 pages rebuilt with EXACT member management theme!")
