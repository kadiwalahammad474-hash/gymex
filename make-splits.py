import re

ROOT = "."
SIZE = "1200\u00d7700px (16:9)"

def slot_section(label, filename):
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

def box_from_slot(slot):
    prefix = '<section style="padding:0 24px 30px;"><div style="max-width:1000px;margin:0 auto;">'
    tail = "</div></div></section>"
    inner = slot[len(prefix):-len(tail)]
    # inner = <div box><div icon-col>...content...</div>  -> needs one more close for the box
    return inner.replace("min-height:400px", "min-height:340px") + "</div>"

SPLIT_OPEN = '<div class="fx-split" style="display:grid;grid-template-columns:1.15fr .85fr;gap:36px;align-items:center;margin-bottom:8px;">'
SPLIT_OPEN_REV = '<div class="fx-split" style="display:grid;grid-template-columns:.85fr 1.15fr;gap:36px;align-items:center;margin-bottom:8px;">'

def align_left(h2p):
    h2p = h2p.replace("text-align:center;", "")
    h2p = re.sub(r"margin:0 auto (\d+)px", r"margin:0 0 \1px", h2p)
    h2p = re.sub(r"margin:0 auto;", "margin:0;", h2p)
    return h2p

jobs = {
    "member-management/member-management.html": [
        ("Everything About Every Member, in One Profile", "Member Profile View", "gym-member-profile-software-gymex.webp"),
        ("Track Attendance and Make Check-Ins Easier", "Member Check-In Screen", "gym-member-checkin-software-gymex.webp"),
        ("Make Decisions Using Real Member Data", "Member Analytics Dashboard", "gym-member-analytics-gymex.webp"),
    ],
    "staff-management/staff-management.html": [
        ("Give Every Staff Member the", "Staff Roles &amp; Permissions", "gym-staff-roles-software-gymex.webp"),
        ("Keep Your Team Connected to", "Staff Activity Overview", "gym-staff-activity-software-gymex.webp"),
        ("Manage Staff Across", "Multi-Location Staff View", "gym-multi-location-staff-gymex.webp"),
    ],
    "payroll-commission/payroll-commission.html": [
        ("Manage Different Salary Structures", "Salary Structure Setup", "gym-payroll-software-gymex.webp"),
        ("From Staff Activity to Payroll in One Workflow", "Payroll Workflow", "gym-salary-processing-gymex.webp"),
        ("Everything You Need for Payroll", "Payroll Features Overview", "gym-payroll-features-gymex.webp"),
    ],
    "data-analysis-dashboard/data-analysis-dashboard.html": [
        ("See Your Gym's Performance at a Glance", "Analytics Dashboard", "gym-analytics-dashboard-gymex.webp"),
        ("Explore 50+ Business Reports", "Business Reports Library", "gym-business-reports-gymex.webp"),
        ("Track the KPIs That Matter", "KPI Dashboard", "gym-kpi-dashboard-gymex.webp"),
    ],
    "intelligent-alerts/intelligent-alerts-reminders.html": [
        ("Create Customized Alerts for Members", "Alert Builder", "gym-member-alerts-gymex.webp"),
        ("Send Alerts Across Multiple Channels", "Multi-Channel Alerts", "gym-alert-channels-gymex.webp"),
        ("Class, Billing & Operational Alerts", "Billing &amp; Class Alerts", "gym-billing-alerts-gymex.webp"),
    ],
    "biometric-access-control/biometric-access-control.html": [
        ("Track Attendance with Biometric & RFID", "Biometric Attendance", "gym-biometric-attendance-gymex.webp"),
        ("Control Gym Access Based on Membership Rules", "Access Rules Setup", "gym-access-control-gymex.webp"),
        ("Block Access for Defaulting Members", "Blocked Access View", "gym-rfid-gym-access-gymex.webp"),
    ],
    "marketing-management/marketing-management.html": [
        ("Reach Members", "Campaign Builder", "gym-marketing-campaigns-gymex.webp"),
        ("Automate", "Marketing Automation Flow", "gym-marketing-automation-gymex.webp"),
        ("Understand What", "Marketing Analytics Report", "gym-marketing-analytics-gymex.webp"),
    ],
}

grand = {"ok": 0, "fail": 0}
for page, slots in jobs.items():
    s = open(page, encoding="utf-8").read()
    for idx, (anchor, label, fn) in enumerate(slots):
        slot = slot_section(label, fn)
        if slot not in s:
            print(f"  !! slot not found on {page}: {label}")
            grand["fail"] += 1
            continue
        i = s.find(anchor)
        if i == -1:
            print(f"  !! anchor missing on {page}: {anchor}")
            grand["fail"] += 1
            continue
        sec_start = s.rfind("<section", 0, i)
        sec_close = s.find("</section>", i)
        if sec_start == -1 or sec_close == -1:
            print(f"  !! section bounds fail on {page}: {anchor}")
            grand["fail"] += 1
            continue
        section = s[sec_start:sec_close + len("</section>")]

        # find heading block within section
        m_sm = re.search(r'<div class="sm-heading">.*?<div class="sm-underline"></div></div>', section, re.S)
        box = box_from_slot(slot)
        new_section = None
        if m_sm:
            heading = m_sm.group(0)
            if idx % 2 == 0:
                new_heading = SPLIT_OPEN + "<div>" + heading[len('<div class="sm-heading">'):-len("</div>")] + "</div>" + box + "</div>"
            else:
                new_heading = SPLIT_OPEN_REV + box + "<div>" + heading[len('<div class="sm-heading">'):-len("</div>")] + "</div></div>"
            # re-add sm-heading wrapper around text part: rebuild properly
            if idx % 2 == 0:
                inner_text = heading[len('<div class="sm-heading">'):-len("</div>")]
                new_heading = SPLIT_OPEN + '<div><div class="sm-heading">' + inner_text + "</div></div>" + box + "</div>"
            else:
                inner_text = heading[len('<div class="sm-heading">'):-len("</div>")]
                new_heading = SPLIT_OPEN_REV + box + '<div><div class="sm-heading">' + inner_text + "</div></div></div>"
            new_section = section.replace(heading, new_heading, 1)
        else:
            m_h2 = re.search(r"<h2\b", section)
            if not m_h2:
                print(f"  !! no heading on {page}: {anchor}")
                grand["fail"] += 1
                continue
            h2_start = m_h2.start()
            p_end = section.find("</p>", h2_start)
            if p_end == -1:
                print(f"  !! no intro p on {page}: {anchor}")
                grand["fail"] += 1
                continue
            p_end += len("</p>")
            h2p = section[h2_start:p_end]
            h2p_left = align_left(h2p)
            textcol = "<div>" + h2p_left + "</div>"
            if idx % 2 == 0:
                split = SPLIT_OPEN + textcol + box + "</div>"
            else:
                split = SPLIT_OPEN_REV + box + textcol + "</div>"
            new_section = section[:h2_start] + split + section[p_end:]

        if new_section is None:
            grand["fail"] += 1
            continue
        s = s[:sec_start] + new_section + s[sec_close + len("</section>"):]
        # remove standalone slot section (with optional preceding newline)
        s = s.replace("\n" + slot, "", 1).replace(slot, "", 1)
        grand["ok"] += 1
        print(f"  OK {page}: {label} -> side-by-side ({'img right' if idx % 2 == 0 else 'img left'})")
    with open(page, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(s)

print(f"DONE ok={grand['ok']} fail={grand['fail']}")
