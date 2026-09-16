import re, sys

ROOT = r"C:/Users/Developer4/Desktop/gymexglobalwebsite"
SIZE = "1200\u00d7700px (16:9)"

def read(p):
    return open(p, encoding="utf-8").read()

def write(p, s):
    open(p, "w", encoding="utf-8", newline="\n").write(s)

def placeholder(label, filename):
    return (
        '<section style="padding:0 24px 30px;">'
        '<div style="max-width:1000px;margin:0 auto;">'
        '<div style="background:#f0f4f8;border-radius:16px;border:2px dashed #c3d0e0;'
        'min-height:400px;display:flex;align-items:center;justify-content:center;text-align:center;padding:40px;">'
        '<div><i class="fa fa-camera" style="font-size:44px;color:#b0c4d8;margin-bottom:14px;display:block;"></i>'
        f'<p style="font-size:14px;color:#8899aa;font-weight:700;margin:0 0 4px;">{label} Screenshot</p>'
        f'<p style="font-size:12px;color:#aab8c5;margin:0;">{filename} \u2014 {SIZE}</p>'
        "</div></div></div></section>"
    )

def insert_after_section(html, anchor_text, slot, page):
    """Insert slot right after the </section> that contains anchor_text."""
    i = html.find(anchor_text)
    if i == -1:
        print(f"  !! anchor not found: {anchor_text[:50]!r} on {page}")
        return html, False
    j = html.find("</section>", i)
    if j == -1:
        print(f"  !! no section close after anchor on {page}")
        return html, False
    end = j + len("</section>")
    return html[:end] + "\n" + slot + html[end:], True

jobs = {
    "intelligent-alerts/intelligent-alerts-reminders.html": [
        ("Create Customized Alerts for Members", "Alert Builder", "gym-member-alerts-gymex.webp"),
        ("Send Alerts Across Multiple Channels", "Multi-Channel Alerts", "gym-alert-channels-gymex.webp"),
        ("Class, Billing &amp; Operational Alerts", "Billing &amp; Class Alerts", "gym-billing-alerts-gymex.webp"),
    ],
    "biometric-access-control/biometric-access-control.html": [
        ("Track Attendance with Biometric &amp; RFID", "Biometric Attendance", "gym-biometric-attendance-gymex.webp"),
        ("Control Gym Access Based on Membership Rules", "Access Rules Setup", "gym-access-control-gymex.webp"),
        ("Block Access for Defaulting Members", "Blocked Access View", "gym-rfid-gym-access-gymex.webp"),
    ],
    "marketing-management/marketing-management.html": [
        ("Reach Members", "Campaign Builder", "gym-marketing-campaigns-gymex.webp"),
        ("Automate", "Marketing Automation Flow", "gym-marketing-automation-gymex.webp"),
        ("Understand What", "Marketing Analytics Report", "gym-marketing-analytics-gymex.webp"),
    ],
}

print("=== 1) Old pages: insert image slots ===")
total = 0
for page, slots in jobs.items():
    p = f"{ROOT}/{page}"
    html = read(p)
    ok = 0
    for anchor, label, fn in slots:
        html, done = insert_after_section(html, anchor, placeholder(label, fn), page)
        if done:
            ok += 1
            total += 1
    if ok:
        write(p, html)
    print(f"  {page}: {ok}/{len(slots)} slots")

print("=== 2) task/expense: add size inside placeholder spans ===")
for page in ["task-management/task-management.html", "expense-management/expense-management.html"]:
    p = f"{ROOT}/{page}"
    s = read(p)
    s2, n = re.subn(
        r'(<i class="fa fa-camera"></i>\s*<span>)([^<]+)(</span>)',
        lambda m: m.group(1) + m.group(2) + f" \u2014 {SIZE}" + m.group(3),
        s,
    )
    write(p, s2)
    print(f"  {page}: {n} spans sized")
    total += n

print(f"TOTAL: {total} image slots now carry size specs")
