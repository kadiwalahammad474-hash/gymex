# -*- coding: utf-8 -*-
"""Gym Management Software page = Gym Industry Page.docx se 100% align."""
import io, re, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
P = 'gym-management-software/gym-management-software.html'
s = io.open(P, encoding='utf-8', newline='').read()
nl = '\r\n' if '\r\n' in s else '\n'
edits = 0

TITLE = 'Gym Management Software for Gyms &amp; Fitness Clubs | Gymex'
DESC = 'Simplify memberships, leads, attendance, staff, bookings and daily gym operations with Gymex gym management software for single and multi-location gyms.'
KEYS = 'Gym Management Software, Gym Software, Gym CRM Software, Gym Membership Software, Gym Management System, Fitness Club Management Software'

def rep(old, new, cnt=1):
    global s, edits
    old = old.replace('\n', nl); new = new.replace('\n', nl)
    assert old in s, 'NOT FOUND: ' + old[:90]
    s2 = s.replace(old, new, cnt)
    assert s2 != s
    s = s2; edits += 1

# ── 1. SEO head ──
rep('<meta name="title" content="GYMEX">', '<meta name="title" content="%s">' % TITLE)
rep('<meta name="keywords" content="gym">', '<meta name="keywords" content="%s">' % KEYS)
rep('<meta name="description" content="Manage your gym in a Few Simple Clicks">',
    '<meta name="description" content="%s">' % DESC)
rep('<meta property="og:title" content="GYMEX">', '<meta property="og:title" content="%s">' % TITLE)
rep('<meta property="og:description" content="Manage your gym in a Few Simple Clicks">',
    '<meta property="og:description" content="%s">' % DESC)
rep('<meta property="twitter:title" content="GYMEX">', '<meta property="twitter:title" content="%s">' % TITLE)
rep('<meta property="twitter:description" content="Manage your gym in a Few Simple Clicks">',
    '<meta property="twitter:description" content="%s">' % DESC)
rep('<title>Gym Management Software</title>', '<title>%s</title>' % TITLE)
rep('business-types-theme.css?v=1', 'business-types-theme.css?v=2')

# ── 2. Hero H1 + two paragraphs ──
rep('''<h1 class="mm-h1">Gym Management Software</h1>
          <p class="mm-desc">Gyms provide numerous benefits for physical and mental well-being, community support, and disease prevention. Utilizing Gymex Software helps gyms enhance operational efficiency, member engagement, retention, finances, data-driven decisions, and communication effectively.</p>''',
    '''<h1 class="mm-h1">Gym Management Software Built for Everyday Gym Operations</h1>
          <p class="mm-desc" style="margin-bottom:8px;">Running a gym means managing members, enquiries, staff, attendance, bookings, payments and much more every day.</p>
          <p class="mm-desc">Gymex brings your essential gym operations together in one connected platform, helping your team stay organized and reduce repetitive administrative work.</p>''')

# ── 3. Replace old "Everything You Need" (12 cards) with docx's 6 sections ──
m = re.search(r'<section class="mm-section">\s*<div class="mm-heading">\s*<h2>Everything You Need,.*?</section>', s, re.S)
assert m, 'old Everything You Need section not found'

def sec(cls, h2a, h2b, paras, body=''):
    h2 = h2a + (' <span class="accent">' + h2b + '</span>' if h2b else '')
    ps = ''.join(nl.join(['      <p class="mm-sec-p">' + p + '</p>']) for p in paras)
    return ('<section class="%s">' % cls + nl +
            '      <div class="mm-heading"><h2>' + h2 + '</h2></div>' + ps + body + nl +
            '    </section>')

def pills(*links):
    out = nl.join(['      <div class="mm-link-row">'])
    for text, href in links:
        out += nl.join(['\n        <a class="mm-link-pill" href="' + href + '">' + text + ' <i class="fa fa-arrow-up"></i></a>'])
    out += nl.join(['\n      </div>'])
    return out

def card(icon, title, desc):
    return (nl.join(['\n        <div class="mm-feature-card"><div class="mm-feature-icon" style="background:#e9f0ff;color:#1657d6;">'
                     '<i class="fa ' + icon + '"></i></div><h3>' + title + '</h3><p>' + desc + '</p></div>']))

cards6 = nl.join(['\n      <div class="mm-feature-grid">']) + \
    card('fa-users', 'Members', 'Keep memberships and member information organized.') + \
    card('fa-filter', 'Leads', 'Capture enquiries and stay on top of follow-ups.') + \
    card('fa-fingerprint', 'Attendance', 'Manage member and staff attendance efficiently.') + \
    card('fa-calendar-check', 'Bookings', 'Organize appointments, classes and schedules.') + \
    card('fa-user', 'Staff', 'Manage staff activities, payroll and commissions.') + \
    card('fa-comments', 'Communication', 'Keep members informed with automated updates.') + \
    nl.join(['\n      </div>'])

new_block = nl.join([
    sec('mm-section grey', 'Keep Your Gym', 'Operations Connected', [
        'As your gym grows, managing different activities through spreadsheets, registers and separate tools can make everyday work complicated.',
        'Gymex keeps important operations connected, giving your team an easier way to manage your gym from one place.',
    ], cards6),

    sec('mm-section', 'From New Enquiries', 'to Active Members', [
        "A member's journey often starts long before they purchase a membership. Gymex helps your team keep enquiries organized, manage follow-ups and continue managing members after they join.",
        'Keep prospect details together, follow up on opportunities and maintain important membership information without switching between disconnected records.',
    ], pills(('Explore Lead Management', '../lead-management/lead-management.html'),
             ('Explore Member Management', '../member-management/member-management.html'))),

    sec('mm-section grey', 'Make Everyday Member Visits', 'Easier to Manage', [
        'Busy gym hours require quick and organized processes.',
        'Gymex helps manage member attendance through Biometric, Face, RFID, QR Code and manual check-ins. Your team can also manage appointments and classes while keeping track of member activity from one connected system.',
    ], pills(('Explore Biometric &amp; Access Control', '../biometric-access-control/biometric-access-control.html'),
             ('Explore Appointment &amp; Class Booking', '../appointment-and-class/appointment-and-class.html'))),

    sec('mm-section', 'Give Your Team', 'More Time for Members', [
        'Routine administrative work can take valuable time away from your members.',
        'Gymex helps organize staff activities, tasks, payroll and trainer commissions while automating important member alerts and follow-ups. This reduces repetitive work and helps your team focus more on everyday member experience.',
    ], pills(('Staff Management', '../staff-management/staff-management.html'),
             ('Task Management', '../task-management/task-management.html'),
             ('Payroll &amp; Commission', '../payroll-commission/payroll-commission.html'),
             ('Intelligent Alerts &amp; Reminder', '../intelligent-alerts/intelligent-alerts-reminders.html'))),

    sec('mm-section grey', 'Know What Is Happening', 'Across Your Gym', [
        'Gym owners need visibility without checking multiple records every day.',
        'Gymex brings important business information together through dashboards and reports, helping you review memberships, collections, attendance, leads and other key gym activities.',
        'For businesses with multiple locations, Gymex also helps keep branch operations connected as the business grows.',
    ], pills(('Explore Data Analysis &amp; Dashboard', '../data-analysis-dashboard/data-analysis-dashboard.html'))),

    sec('mm-section', 'Manage Your Gym', 'Beyond the Front Desk', [
        'Gymex mobile apps help members, prospects and gym administrators stay connected beyond the desktop.',
        'Members can access relevant gym services through the Member App, while Admin and Prospect Apps support different parts of gym management and prospect handling.',
    ], pills(('Explore Gymex Mobile Apps', '../mobile-apps/mobile-apps.html'))),
])
s = s.replace(m.group(0), new_block, 1); edits += 1

# ── 4. FAQ -> docx exact 5 ──
m = re.search(r'<div class="mm-faq">.*?</div>\s*</section>', s, re.S)
assert m, 'faq block not found'
faqs = [
    ('What is gym management software?',
     'Gym management software helps fitness businesses manage memberships, leads, attendance, staff, bookings, payments and other everyday operations from one system.'),
    ('Is Gymex suitable for a single gym?',
     'Yes. Gymex can be used by independent gyms as well as businesses managing multiple gym locations.'),
    ('Can Gymex manage gym attendance?',
     'Yes. Gymex supports Biometric, Face, RFID, QR Code and manual attendance options along with access-control functionality.'),
    ('Can members book classes and appointments with Gymex?',
     'Yes. Gymex supports class and appointment booking, helping members and gym teams manage schedules and bookings more efficiently.'),
    ('Does Gymex provide mobile apps?',
     'Yes. Gymex provides dedicated Member, Prospect and Admin apps for different gym-management requirements.'),
]
faq_html = nl.join([
    '      <div class="mm-faq">',
    ''.join(nl.join(['\n          <details class="mm-faq-item"><summary>' + q + '</summary><p>' + a + '</p></details>']) for q, a in faqs),
    nl.join(['\n      </div>']),
    '    </section>',
])
s = s.replace(m.group(0), faq_html, 1); edits += 1

# ── 5. Final CTA ──
rep('''<div class="mm-cta-banner">
      <h2>Ready to see <span class="accent">Gymex</span> in action for your business?</h2>
      <button class="mm-btn mm-btn-orange open-modal-btn">Get Your Free Demo <i class="fa fa-arrow-up"></i></button>
    </div>''',
    '''<div class="mm-cta-banner">
      <h2>Bring Your Gym <span class="accent">Operations Together</span></h2>
      <p style="color:#cfe0f5; font-size:15px; margin:12px auto 22px; max-width:640px; line-height:1.7;">Manage your members, team and daily activities through one connected gym management platform.</p>
      <button class="mm-btn mm-btn-orange open-modal-btn">Get Your Free Demo <i class="fa fa-arrow-up"></i></button>
    </div>''')

io.open(P, 'w', encoding='utf-8', newline='').write(s)
print('OK edits:', edits)

# ── 6. bump theme css version on all 10 pages ──
import glob
for p in glob.glob('*/*.html'):
    t = io.open(p, encoding='utf-8', newline='').read()
    if 'business-types-theme.css?v=1' in t:
        io.open(p, 'w', encoding='utf-8', newline='').write(
            t.replace('business-types-theme.css?v=1', 'business-types-theme.css?v=2'))
        print('bumped:', p)
