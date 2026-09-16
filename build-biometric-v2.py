#!/usr/bin/env python3
"""Build the Biometric & Access Control page with exact docx content."""

import os

# Read nav from existing page for reference
with open("biometric-access-control/biometric-access-control.html", "r", encoding="utf-8") as f:
    old_html = f.read()

# Extract nav section
nav_start = old_html.find("<nav")
nav_end = old_html.find("</nav>") + 6
nav_html = old_html[nav_start:nav_end]

# Extract footer section (from <div style="background:#0b1a3d")
footer_start = old_html.find('<div style="background:#0b1a3d; padding:0;">')
footer_end = old_html.find("</html>") + 7
footer_html = old_html[footer_start:footer_end]

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Gym Biometric Attendance & Access Control Software | Gymex</title>
  <meta name="description" content="Automate gym attendance with biometric, RFID and QR check-ins. Control member access by membership, age and time with Gymex biometric and access control software.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <link rel="stylesheet" href="../style.css">
  <style>
    .ba-h1{{font-family:'Poppins',sans-serif!important;font-size:42px!important;font-weight:800!important;line-height:1.15!important;margin:0 0 16px!important;color:#0b1a3d!important;}}
    .ba-p{{font-family:'Poppins',sans-serif!important;font-size:15.5px!important;line-height:1.7!important;margin:0 0 26px!important;color:#6b7589!important;}}
    .ba-sec{{font-family:'Poppins',sans-serif!important;padding:70px 24px!important;}}
    .ba-wrap{{max-width:1100px!important;margin:0 auto!important;}}
    .ba-h2{{font-size:28px!important;font-weight:700!important;color:#0b1a3d!important;margin:0 0 16px!important;line-height:1.3!important;}}
    .ba-sub{{font-size:15px!important;color:#666!important;line-height:1.75!important;margin:0 0 16px!important;}}
    .ba-grid{{display:grid!important;grid-template-columns:repeat(auto-fit,minmax(260px,1fr))!important;gap:20px!important;margin:32px 0!important;}}
    .ba-card{{background:#fff!important;border-radius:16px!important;padding:28px!important;border:1px solid #e8edf3!important;transition:transform .3s,box-shadow .3s!important;}}
    .ba-card:hover{{transform:translateY(-4px)!important;box-shadow:0 12px 32px rgba(0,0,0,.08)!important;}}
    .ba-card-icon{{width:52px!important;height:52px!important;border-radius:14px!important;display:flex!important;align-items:center!important;justify-content:center!important;font-size:22px!important;color:#fff!important;margin-bottom:18px!important;}}
    .ba-card h3{{font-size:17px!important;font-weight:700!important;color:#0b1a3d!important;margin:0 0 10px!important;}}
    .ba-card p{{font-size:14px!important;color:#666!important;line-height:1.7!important;margin:0!important;}}
    .ba-flow{{display:flex!important;align-items:center!important;justify-content:center!important;flex-wrap:wrap!important;gap:12px!important;margin:32px 0!important;}}
    .ba-flow-step{{background:linear-gradient(135deg,#0b1a3d,#1a3a5c)!important;color:#fff!important;padding:12px 22px!important;border-radius:12px!important;font-size:13px!important;font-weight:600!important;}}
    .ba-flow-arrow{{color:#f26522!important;font-size:18px!important;}}
    .ba-cta{{background:linear-gradient(135deg,#0b1a3d 0%,#1a3a5c 100%)!important;text-align:center!important;padding:60px 24px!important;}}
    .ba-cta h2{{color:#fff!important;font-size:30px!important;font-weight:700!important;margin:0 0 14px!important;}}
    .ba-cta p{{color:rgba(255,255,255,.8)!important;font-size:16px!important;margin:0 0 28px!important;line-height:1.7!important;}}

    .ba-faq{{border:1px solid #e8edf3!important;border-radius:12px!important;margin-bottom:12px!important;overflow:hidden!important;}}
    .ba-faq-q{{padding:18px 24px!important;cursor:pointer!important;font-weight:600!important;font-size:15px!important;color:#0b1a3d!important;background:#f8fafc!important;display:flex!important;justify-content:space-between!important;align-items:center!important;}}
    .ba-faq-q i{{transition:transform .3s!important;}}
    .ba-faq-a{{padding:0 24px 18px!important;font-size:14px!important;color:#666!important;line-height:1.75!important;display:none!important;}}
    .ba-faq.open .ba-faq-a{{display:block!important;}}
    .ba-faq.open .ba-faq-q i{{transform:rotate(180deg)!important;}}

    .backdrop {{ display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.6); z-index: 9999; justify-content: center; align-items: center; }}
    .backdrop.show {{ display: flex; }}
    .contact-us {{ background: #fff; border-radius: 20px; padding: 40px 32px; max-width: 520px; width: 90%; position: relative; max-height: 90vh; overflow-y: auto; }}
    .loader {{ display: none; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 40px; height: 40px; border: 4px solid #e0e0e0; border-top: 4px solid #1565C0; border-radius: 50%; animation: spin 0.8s linear infinite; }}
    .loader.show {{ display: block; }}
    @keyframes spin {{ 0% {{ transform: translate(-50%, -50%) rotate(0deg); }} 100% {{ transform: translate(-50%, -50%) rotate(360deg); }} }}

    .mega-menu .icon {{ width: 24px; height: 24px; min-width: 24px; margin-right: 4px; }}
    .mega-menu:not(.features-mega) .text1 {{ color: var(--gray-100, #525251); }}
    .mega-menu:not(.features-mega) .text1:hover {{ color: var(--blue, #028ECE); }}
    .mega-menu:not(.features-mega) .mega-icon {{ background: rgba(2,142,206,.1); color: #028ece; }}
    .mega-menu:not(.features-mega) .inside:hover {{ background: var(--gray-7, #F3F3F3); }}
    .icon {{ width: 32px; height: 32px; }}
    .nav__cta {{ display: inline-flex; align-items: center; }}

    .sm-label {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: transparent;
      padding: 0;
      border-radius: 0;
      font-family: 'Poppins', sans-serif;
      font-size: 12px;
      font-weight: 700;
      letter-spacing: .18em;
      color: #028ECE;
      text-transform: uppercase;
      margin-bottom: 16px;
    }}
    .sm-label::before {{
      content: "";
      width: 8px; height: 8px;
      border-radius: 50%;
      background: #f26522;
      box-shadow: 0 0 12px #f26522;
    }}

    h1, h2, h3, h4, p, span, li {{
      text-transform: none !important;
    }}
  </style>
</head>
<body>

{nav_html}

<!-- Hero Section -->
<section style="position:relative!important;margin-left:calc(-50vw + 50%)!important;margin-right:calc(-50vw + 50%)!important;width:100vw!important;padding:40px calc(50vw - 50% + 40px) 60px!important;background:var(--BG,#f5f7fb)!important;border-radius:0!important;overflow:hidden!important;">
  <div style="max-width:1180px!important;margin:0 auto!important;padding:0 24px!important;position:relative!important;z-index:1!important;text-align:left!important;">
    <div class="sm-label">BIOMETRIC & ACCESS CONTROL SOFTWARE</div>
    <h1 class="ba-h1">Simplify Gym Check-Ins<br>& Control Member Access</h1>
    <p class="ba-p" style="max-width:560px!important;">Track staff and member attendance with biometric, RFID, QR code, and manual check-ins. Gymex helps you manage facility access based on membership rules while keeping attendance and access control connected in one platform.</p>
    <button class="open-modal-btn" style="display:inline-flex;align-items:center;gap:12px;background:linear-gradient(135deg,#f26522,#e0450b);color:#fff;padding:6px 6px 6px 28px;border:none;border-radius:50px;font-size:14px;font-weight:700;font-family:'Poppins',sans-serif;cursor:pointer;letter-spacing:.5px;transition:all .3s;box-shadow:0 14px 32px rgba(242,101,34,.3);">Get Your Free Demo <span style="display:inline-flex;align-items:center;justify-content:center;width:44px;height:44px;min-width:44px;background:#fff;border-radius:50%;"><svg width="18" height="18" viewBox="0 0 32 32" fill="none"><path d="M9.47576 24.5163L7.59014 22.6307L18.9039 11.317H8.53295V8.63941H23.467V23.5735H20.7895V13.2026L9.47576 24.5163Z" fill="#f26522"/></svg></span></button>
  </div>
</section>

<!-- Track Attendance with Biometric & RFID -->
<section class="ba-sec" style="background:#fff!important;">
  <div class="ba-wrap">
    <h2 class="ba-h2" style="text-align:center!important;">Track Attendance with Biometric & RFID</h2>
    <p class="ba-sub" style="text-align:center!important;max-width:700px;margin:0 auto 24px!important;">Manual attendance can slow down check-ins and make member visit records harder to maintain. Gymex Gym Biometric Attendance Software allows you to capture staff and member attendance through biometric and RFID integration, creating a faster and more structured check-in process.</p>
    <p class="ba-sub" style="text-align:center!important;max-width:700px;margin:0 auto 24px!important;">Once a member checks in, their attendance information stays connected with your Gymex system, helping your team maintain accurate visit records without depending on manual registers.</p>
    <div class="ba-flow" style="margin:32px auto!important;">
      <div class="ba-flow-step">Member Arrives</div>
      <div class="ba-flow-arrow">&rarr;</div>
      <div class="ba-flow-step">Biometric/RFID Verification</div>
      <div class="ba-flow-arrow">&rarr;</div>
      <div class="ba-flow-step">Check-In</div>
      <div class="ba-flow-arrow">&rarr;</div>
      <div class="ba-flow-step">Attendance Recorded</div>
    </div>
    <p class="ba-sub" style="text-align:center!important;max-width:700px;margin:0 auto!important;">This makes everyday gym attendance tracking simpler for both members and staff.</p>
  </div>
</section>

<!-- Give Members an Easy QR Code Check-In -->
<section class="ba-sec" style="background:#f8fafc!important;">
  <div class="ba-wrap" style="display:grid!important;grid-template-columns:1fr 1fr!important;gap:48px!important;align-items:center!important;">
    <div>
      <h2 class="ba-h2">Give Members an Easy QR Code Check-In</h2>
      <p class="ba-sub">Not every member needs to check in through a biometric device. Gymex also supports QR code scanning for member attendance through the mobile app, giving members another convenient way to record their gym visit.</p>
      <p class="ba-sub">With multiple check-in options available, your fitness business can create a smoother attendance experience while maintaining organized member records.</p>
    </div>
    <div style="background:linear-gradient(135deg,#0b1a3d,#1a3a5c)!important;border-radius:20px!important;padding:40px!important;text-align:center!important;">
      <div style="width:80px!important;height:80px!important;margin:0 auto 20px!important;background:rgba(255,255,255,.1)!important;border-radius:20px!important;display:flex!important;align-items:center!important;justify-content:center!important;"><i class="fa fa-qrcode" style="color:#f26522!important;font-size:36px!important;"></i></div>
      <h3 style="color:#fff!important;font-size:20px!important;font-weight:700!important;margin:0 0 12px!important;">QR Code Check-In</h3>
      <p style="color:rgba(255,255,255,.7)!important;font-size:14px!important;line-height:1.7!important;margin:0!important;">Members scan QR code from the mobile app for instant check-in</p>
    </div>
  </div>
</section>

<!-- Multiple Ways to Check In -->
<section class="ba-sec" style="background:#fff!important;">
  <div class="ba-wrap">
    <h2 class="ba-h2" style="text-align:center!important;">Multiple Ways to Check In</h2>
    <p class="ba-sub" style="text-align:center!important;max-width:700px;margin:0 auto 32px!important;">This flexibility makes Gymex more than just biometric gym software &mdash; it provides multiple ways to manage attendance based on your gym's operations.</p>
    <div class="ba-grid" style="grid-template-columns:repeat(4,1fr)!important;">
      <div class="ba-card" style="text-align:center!important;">
        <div class="ba-card-icon" style="background:linear-gradient(135deg,#f26522,#e0450b)!important;margin:0 auto 16px!important;"><i class="fa fa-fingerprint" style="color:#fff!important;"></i></div>
        <h3>Biometric</h3>
        <p>Capture attendance through biometric integration.</p>
      </div>
      <div class="ba-card" style="text-align:center!important;">
        <div class="ba-card-icon" style="background:linear-gradient(135deg,#028ECE,#0a5d8f)!important;margin:0 auto 16px!important;"><i class="fa fa-id-card" style="color:#fff!important;"></i></div>
        <h3>RFID</h3>
        <p>Allow members and staff to check in using RFID.</p>
      </div>
      <div class="ba-card" style="text-align:center!important;">
        <div class="ba-card-icon" style="background:linear-gradient(135deg,#34A853,#1e7e34)!important;margin:0 auto 16px!important;"><i class="fa fa-qrcode" style="color:#fff!important;"></i></div>
        <h3>QR Code</h3>
        <p>Enable member attendance through QR code scanning from the mobile app.</p>
      </div>
      <div class="ba-card" style="text-align:center!important;">
        <div class="ba-card-icon" style="background:linear-gradient(135deg,#7c3aed,#5b21b6)!important;margin:0 auto 16px!important;"><i class="fa fa-clipboard-check" style="color:#fff!important;"></i></div>
        <h3>Manual Check-In</h3>
        <p>Allow authorized staff to record attendance manually when required.</p>
      </div>
    </div>
  </div>
</section>

<!-- Control Gym Access Based on Membership Rules -->
<section class="ba-sec" style="background:#f8fafc!important;">
  <div class="ba-wrap">
    <h2 class="ba-h2" style="text-align:center!important;">Control Gym Access Based on Membership Rules</h2>
    <p class="ba-sub" style="text-align:center!important;max-width:700px;margin:0 auto 16px!important;">Attendance tells you who checked in. Access control helps determine who should be allowed access.</p>
    <p class="ba-sub" style="text-align:center!important;max-width:700px;margin:0 auto 32px!important;">Gymex Gym Access Control Software allows you to apply access restrictions based on:</p>
    <div class="ba-grid" style="grid-template-columns:repeat(3,1fr)!important;max-width:900px!important;margin:0 auto 32px!important;">
      <div class="ba-card" style="text-align:center!important;">
        <div class="ba-card-icon" style="background:linear-gradient(135deg,#f26522,#e0450b)!important;margin:0 auto 16px!important;"><i class="fa fa-id-card-clip" style="color:#fff!important;"></i></div>
        <h3>Membership Type</h3>
        <p>Control access according to the membership or plan purchased by the member.</p>
      </div>
      <div class="ba-card" style="text-align:center!important;">
        <div class="ba-card-icon" style="background:linear-gradient(135deg,#028ECE,#0a5d8f)!important;margin:0 auto 16px!important;"><i class="fa fa-cake-candles" style="color:#fff!important;"></i></div>
        <h3>Age</h3>
        <p>Apply relevant access restrictions based on member age.</p>
      </div>
      <div class="ba-card" style="text-align:center!important;">
        <div class="ba-card-icon" style="background:linear-gradient(135deg,#34A853,#1e7e34)!important;margin:0 auto 16px!important;"><i class="fa fa-clock" style="color:#fff!important;"></i></div>
        <h3>Time</h3>
        <p>Control access based on permitted timings.</p>
      </div>
    </div>
    <p class="ba-sub" style="text-align:center!important;max-width:700px;margin:0 auto 24px!important;">By connecting membership information with access rules, Gymex helps create a more structured gym member access control process.</p>
    <div class="ba-flow" style="margin:24px auto!important;">
      <div class="ba-flow-step">Member</div>
      <div class="ba-flow-arrow">&rarr;</div>
      <div class="ba-flow-step">Membership Verification</div>
      <div class="ba-flow-arrow">&rarr;</div>
      <div class="ba-flow-step">Access Rules</div>
      <div class="ba-flow-arrow">&rarr;</div>
      <div class="ba-flow-step">Entry</div>
    </div>
  </div>
</section>

<!-- Block Access for Defaulting Members -->
<section class="ba-sec" style="background:#fff!important;">
  <div class="ba-wrap" style="display:grid!important;grid-template-columns:1fr 1fr!important;gap:48px!important;align-items:center!important;">
    <div style="background:linear-gradient(135deg,#dc2626,#b91c1c)!important;border-radius:20px!important;padding:40px!important;text-align:center!important;">
      <div style="width:80px!important;height:80px!important;margin:0 auto 20px!important;background:rgba(255,255,255,.15)!important;border-radius:20px!important;display:flex!important;align-items:center!important;justify-content:center!important;"><i class="fa fa-ban" style="color:#fff!important;font-size:36px!important;"></i></div>
      <h3 style="color:#fff!important;font-size:20px!important;font-weight:700!important;margin:0 0 12px!important;">Block Defaulting Members</h3>
      <p style="color:rgba(255,255,255,.8)!important;font-size:14px!important;line-height:1.7!important;margin:0!important;">Restrict access for members who do not meet applicable membership or payment conditions</p>
    </div>
    <div>
      <h2 class="ba-h2">Block Access for Defaulting Members</h2>
      <p class="ba-sub">Access shouldn't continue in the same way when a member no longer meets the required membership or payment conditions.</p>
      <p class="ba-sub">Gymex helps you block defaulting members, giving your team greater control over facility access while reducing the need for staff to manually verify every member at entry.</p>
      <p class="ba-sub">This connects your Gym Access Control System more closely with your member management process and helps ensure access is provided according to applicable membership conditions.</p>
    </div>
  </div>
</section>

<!-- Manage Access Across Multiple Floors -->
<section class="ba-sec" style="background:#f8fafc!important;">
  <div class="ba-wrap" style="display:grid!important;grid-template-columns:1fr 1fr!important;gap:48px!important;align-items:center!important;">
    <div>
      <h2 class="ba-h2">Manage Access Across Multiple Floors</h2>
      <p class="ba-sub">For clubs and fitness facilities operating across multiple floors, Gymex supports seamless biometric integration across multiple floors.</p>
      <p class="ba-sub">This helps businesses manage member movement and access more effectively within larger facilities while keeping attendance and access information connected.</p>
      <p class="ba-sub">It is particularly useful for clubs where different facilities, workout areas, or services are spread across multiple floors.</p>
    </div>
    <div style="background:linear-gradient(135deg,#0b1a3d,#1a3a5c)!important;border-radius:20px!important;padding:40px!important;">
      <div style="display:flex!important;flex-direction:column!important;gap:16px!important;">
        <div style="background:rgba(255,255,255,.1)!important;border-radius:12px!important;padding:16px 20px!important;display:flex!important;align-items:center!important;gap:12px!important;">
          <div style="width:40px!important;height:40px!important;border-radius:10px!important;background:rgba(242,101,34,.2)!important;display:flex!important;align-items:center!important;justify-content:center!important;"><i class="fa fa-building" style="color:#f26522!important;"></i></div>
          <div><p style="color:#fff!important;font-size:14px!important;font-weight:600!important;margin:0!important;">Ground Floor</p><p style="color:rgba(255,255,255,.6)!important;font-size:12px!important;margin:0!important;">Reception & Cardio Zone</p></div>
        </div>
        <div style="background:rgba(255,255,255,.1)!important;border-radius:12px!important;padding:16px 20px!important;display:flex!important;align-items:center!important;gap:12px!important;">
          <div style="width:40px!important;height:40px!important;border-radius:10px!important;background:rgba(2,142,206,.2)!important;display:flex!important;align-items:center!important;justify-content:center!important;"><i class="fa fa-dumbbell" style="color:#028ECE!important;"></i></div>
          <div><p style="color:#fff!important;font-size:14px!important;font-weight:600!important;margin:0!important;">First Floor</p><p style="color:rgba(255,255,255,.6)!important;font-size:12px!important;margin:0!important;">Strength Training Zone</p></div>
        </div>
        <div style="background:rgba(255,255,255,.1)!important;border-radius:12px!important;padding:16px 20px!important;display:flex!important;align-items:center!important;gap:12px!important;">
          <div style="width:40px!important;height:40px!important;border-radius:10px!important;background:rgba(52,168,83,.2)!important;display:flex!important;align-items:center!important;justify-content:center!important;"><i class="fa fa-spa" style="color:#34A853!important;"></i></div>
          <div><p style="color:#fff!important;font-size:14px!important;font-weight:600!important;margin:0!important;">Second Floor</p><p style="color:rgba(255,255,255,.6)!important;font-size:12px!important;margin:0!important;">Yoga & Pilates Studio</p></div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Manage Multi-Branch Member Access -->
<section class="ba-sec" style="background:#fff!important;">
  <div class="ba-wrap" style="display:grid!important;grid-template-columns:1fr 1fr!important;gap:48px!important;align-items:center!important;">
    <div style="background:linear-gradient(135deg,#028ECE,#0a5d8f)!important;border-radius:20px!important;padding:40px!important;text-align:center!important;">
      <div style="width:80px!important;height:80px!important;margin:0 auto 20px!important;background:rgba(255,255,255,.15)!important;border-radius:20px!important;display:flex!important;align-items:center!important;justify-content:center!important;"><i class="fa fa-code-branch" style="color:#fff!important;font-size:36px!important;"></i></div>
      <h3 style="color:#fff!important;font-size:20px!important;font-weight:700!important;margin:0 0 12px!important;">Multi-Branch Access</h3>
      <p style="color:rgba(255,255,255,.8)!important;font-size:14px!important;line-height:1.7!important;margin:0!important;">Allow eligible members to access different branches according to their purchased membership</p>
    </div>
    <div>
      <h2 class="ba-h2">Manage Multi-Branch Member Access</h2>
      <p class="ba-sub">Members may sometimes need access to more than one location within a fitness business.</p>
      <p class="ba-sub">Gymex supports reciprocity, allowing multi-branch access according to the membership purchased by the member. This means access can follow the member's membership privileges rather than requiring each branch to manage access separately.</p>
      <p class="ba-sub">For multi-location fitness businesses, this creates a more consistent member experience while giving management greater control over branch access.</p>
    </div>
  </div>
</section>

<!-- Connect Membership, Access & Attendance -->
<section class="ba-sec" style="background:#f8fafc!important;">
  <div class="ba-wrap">
    <h2 class="ba-h2" style="text-align:center!important;">Connect Membership, Access & Attendance</h2>
    <p class="ba-sub" style="text-align:center!important;max-width:700px;margin:0 auto 32px!important;">One of the biggest advantages of using an integrated Gym Biometric Attendance System is that attendance doesn't have to operate separately from member information.</p>
    <div class="ba-flow" style="margin:32px auto!important;">
      <div class="ba-flow-step">Member Profile</div>
      <div class="ba-flow-arrow">&rarr;</div>
      <div class="ba-flow-step">Membership Type</div>
      <div class="ba-flow-arrow">&rarr;</div>
      <div class="ba-flow-step">Access Rules</div>
      <div class="ba-flow-arrow">&rarr;</div>
      <div class="ba-flow-step">Check-In</div>
      <div class="ba-flow-arrow">&rarr;</div>
      <div class="ba-flow-step">Attendance</div>
    </div>
    <p class="ba-sub" style="text-align:center!important;max-width:700px;margin:0 auto 32px!important;">This helps your team maintain better control over who enters your facilities while keeping relevant attendance information connected with your wider member management process.</p>
    <div style="text-align:center!important;">
      <a href="../member-management/member-management.html" style="display:inline-flex!important;align-items:center!important;gap:10px!important;background:#0b1a3d!important;color:#fff!important;padding:14px 32px!important;border-radius:50px!important;font-size:14px!important;font-weight:700!important;text-decoration:none!important;font-family:'Poppins',sans-serif!important;transition:all .3s!important;">Explore Member Management <i class="fa fa-arrow-right" style="font-size:12px!important;"></i></a>
    </div>
  </div>
</section>

<!-- Keep Staff & Member Attendance Organized -->
<section class="ba-sec" style="background:#fff!important;">
  <div class="ba-wrap">
    <h2 class="ba-h2" style="text-align:center!important;">Keep Staff & Member Attendance Organized</h2>
    <p class="ba-sub" style="text-align:center!important;max-width:700px;margin:0 auto 24px!important;">Gymex isn't limited to member check-ins. You can also capture staff attendance, helping you maintain attendance information for your team alongside member attendance.</p>
    <p class="ba-sub" style="text-align:center!important;max-width:700px;margin:0 auto 24px!important;">A connected Gym Attendance Software process makes it easier to maintain organized attendance records instead of relying on separate registers or disconnected systems.</p>
    <p class="ba-sub" style="text-align:center!important;max-width:700px;margin:0 auto!important;">Whether you're reviewing staff attendance or member visits, relevant attendance information stays easier to manage and access.</p>
  </div>
</section>

<!-- Why Choose Gymex -->
<section class="ba-sec" style="background:#f8fafc!important;">
  <div class="ba-wrap">
    <h2 class="ba-h2" style="text-align:center!important;">Why Choose Gymex for Biometric & Access Control?</h2>
    <p class="ba-sub" style="text-align:center!important;max-width:700px;margin:0 auto 32px!important;">Gymex brings attendance, member information, and facility access together within your gym management system.</p>
    <div class="ba-grid" style="grid-template-columns:repeat(3,1fr)!important;">
      <div class="ba-card" style="text-align:center!important;padding:24px!important;"><div class="ba-card-icon" style="background:linear-gradient(135deg,#f26522,#e0450b)!important;margin:0 auto 14px!important;width:44px!important;height:44px!important;"><i class="fa fa-fingerprint" style="color:#fff!important;font-size:18px!important;"></i></div><h3 style="font-size:15px!important;">Biometric Attendance</h3><p style="font-size:13px!important;">Capture staff and member attendance through biometric integration.</p></div>
      <div class="ba-card" style="text-align:center!important;padding:24px!important;"><div class="ba-card-icon" style="background:linear-gradient(135deg,#028ECE,#0a5d8f)!important;margin:0 auto 14px!important;width:44px!important;height:44px!important;"><i class="fa fa-id-card" style="color:#fff!important;font-size:18px!important;"></i></div><h3 style="font-size:15px!important;">RFID Check-In</h3><p style="font-size:13px!important;">Provide RFID-based attendance for convenient check-ins.</p></div>
      <div class="ba-card" style="text-align:center!important;padding:24px!important;"><div class="ba-card-icon" style="background:linear-gradient(135deg,#34A853,#1e7e34)!important;margin:0 auto 14px!important;width:44px!important;height:44px!important;"><i class="fa fa-qrcode" style="color:#fff!important;font-size:18px!important;"></i></div><h3 style="font-size:15px!important;">QR Code Attendance</h3><p style="font-size:13px!important;">Allow members to record attendance using QR code scanning through the mobile app.</p></div>
      <div class="ba-card" style="text-align:center!important;padding:24px!important;"><div class="ba-card-icon" style="background:linear-gradient(135deg,#7c3aed,#5b21b6)!important;margin:0 auto 14px!important;width:44px!important;height:44px!important;"><i class="fa fa-clipboard-check" style="color:#fff!important;font-size:18px!important;"></i></div><h3 style="font-size:15px!important;">Manual Check-In</h3><p style="font-size:13px!important;">Give authorized staff the flexibility to record attendance manually when needed.</p></div>
      <div class="ba-card" style="text-align:center!important;padding:24px!important;"><div class="ba-card-icon" style="background:linear-gradient(135deg,#f26522,#e0450b)!important;margin:0 auto 14px!important;width:44px!important;height:44px!important;"><i class="fa fa-id-card-clip" style="color:#fff!important;font-size:18px!important;"></i></div><h3 style="font-size:15px!important;">Membership-Based Access</h3><p style="font-size:13px!important;">Control facility access according to the membership purchased.</p></div>
      <div class="ba-card" style="text-align:center!important;padding:24px!important;"><div class="ba-card-icon" style="background:linear-gradient(135deg,#028ECE,#0a5d8f)!important;margin:0 auto 14px!important;width:44px!important;height:44px!important;"><i class="fa fa-clock" style="color:#fff!important;font-size:18px!important;"></i></div><h3 style="font-size:15px!important;">Age & Time Restrictions</h3><p style="font-size:13px!important;">Set access restrictions based on member age and permitted timings.</p></div>
      <div class="ba-card" style="text-align:center!important;padding:24px!important;"><div class="ba-card-icon" style="background:linear-gradient(135deg,#dc2626,#b91c1c)!important;margin:0 auto 14px!important;width:44px!important;height:44px!important;"><i class="fa fa-ban" style="color:#fff!important;font-size:18px!important;"></i></div><h3 style="font-size:15px!important;">Defaulting Member Control</h3><p style="font-size:13px!important;">Restrict access for members who do not meet applicable membership or payment conditions.</p></div>
      <div class="ba-card" style="text-align:center!important;padding:24px!important;"><div class="ba-card-icon" style="background:linear-gradient(135deg,#34A853,#1e7e34)!important;margin:0 auto 14px!important;width:44px!important;height:44px!important;"><i class="fa fa-building" style="color:#fff!important;font-size:18px!important;"></i></div><h3 style="font-size:15px!important;">Multi-Floor Integration</h3><p style="font-size:13px!important;">Manage biometric attendance and access across multiple floors.</p></div>
      <div class="ba-card" style="text-align:center!important;padding:24px!important;grid-column:1/-1;max-width:calc(33.33% - 14px);margin:0 auto!important;"><div class="ba-card-icon" style="background:linear-gradient(135deg,#7c3aed,#5b21b6)!important;margin:0 auto 14px!important;width:44px!important;height:44px!important;"><i class="fa fa-code-branch" style="color:#fff!important;font-size:18px!important;"></i></div><h3 style="font-size:15px!important;">Multi-Branch Reciprocity</h3><p style="font-size:13px!important;">Allow members to access eligible branches according to their purchased membership.</p></div>
    </div>
    <p class="ba-sub" style="text-align:center!important;max-width:700px;margin:32px auto 0!important;">With Gymex Biometric Access Control for Gyms, you get a more connected way to manage check-ins, attendance, and facility access.</p>
  </div>
</section>

<!-- CTA Section -->
<section class="ba-cta">
  <div class="ba-wrap">
    <h2>Make Every Check-In Smarter</h2>
    <p>Simplify attendance and maintain better control over facility access with Gymex.</p>
    <p style="color:rgba(255,255,255,.6)!important;font-size:14px!important;margin:0 0 28px!important;font-style:italic!important;">Biometric. RFID. QR Check-In. Smarter Access Control.</p>
    <button class="open-modal-btn" style="display:inline-flex;align-items:center;gap:12px;background:linear-gradient(135deg,#f26522,#e0450b);color:#fff;padding:6px 6px 6px 28px;border:none;border-radius:50px;font-size:14px;font-weight:700;font-family:'Poppins',sans-serif;cursor:pointer;letter-spacing:.5px;transition:all .3s;box-shadow:0 14px 32px rgba(242,101,34,.3);">Get Your Free Demo <span style="display:inline-flex;align-items:center;justify-content:center;width:44px;height:44px;min-width:44px;background:#fff;border-radius:50%;"><svg width="18" height="18" viewBox="0 0 32 32" fill="none"><path d="M9.47576 24.5163L7.59014 22.6307L18.9039 11.317H8.53295V8.63941H23.467V23.5735H20.7895V13.2026L9.47576 24.5163Z" fill="#f26522"/></svg></span></button>
  </div>
</section>

<!-- FAQ Section -->
<section class="ba-sec" style="background:#fff!important;">
  <div class="ba-wrap" style="max-width:800px!important;">
    <h2 class="ba-h2" style="text-align:center!important;">Frequently Asked Questions</h2>
    <div class="ba-faq" onclick="this.classList.toggle('open')">
      <div style="padding:18px 24px;cursor:pointer;font-weight:600;font-size:15px;color:#0b1a3d;background:#f8fafc;display:flex;justify-content:space-between;align-items:center;font-family:Poppins,sans-serif;">What is gym biometric attendance software? <i class="fa fa-chevron-down"></i></div>
      <div style="padding:0 24px 18px;font-size:14px;color:#666;line-height:1.75;display:none;font-family:Poppins,sans-serif;">Gym Biometric Attendance Software helps gyms record staff and member attendance using biometric identification. It reduces dependence on manual attendance registers and keeps check-in information more organized.</div>
    </div>
    <div class="ba-faq" onclick="this.classList.toggle('open')">
      <div style="padding:18px 24px;cursor:pointer;font-weight:600;font-size:15px;color:#0b1a3d;background:#f8fafc;display:flex;justify-content:space-between;align-items:center;font-family:Poppins,sans-serif;">Does Gymex support RFID attendance? <i class="fa fa-chevron-down"></i></div>
      <div style="padding:0 24px 18px;font-size:14px;color:#666;line-height:1.75;display:none;font-family:Poppins,sans-serif;">Yes. Gymex supports attendance through RFID and biometric integration, giving gyms multiple options for recording staff and member check-ins.</div>
    </div>
    <div class="ba-faq" onclick="this.classList.toggle('open')">
      <div style="padding:18px 24px;cursor:pointer;font-weight:600;font-size:15px;color:#0b1a3d;background:#f8fafc;display:flex;justify-content:space-between;align-items:center;font-family:Poppins,sans-serif;">Can members check in using a QR code? <i class="fa fa-chevron-down"></i></div>
      <div style="padding:0 24px 18px;font-size:14px;color:#666;line-height:1.75;display:none;font-family:Poppins,sans-serif;">Yes. Gymex supports QR code scanning for member attendance through the mobile app, providing members with a convenient check-in option.</div>
    </div>
    <div class="ba-faq" onclick="this.classList.toggle('open')">
      <div style="padding:18px 24px;cursor:pointer;font-weight:600;font-size:15px;color:#0b1a3d;background:#f8fafc;display:flex;justify-content:space-between;align-items:center;font-family:Poppins,sans-serif;">What is gym access control software? <i class="fa fa-chevron-down"></i></div>
      <div style="padding:0 24px 18px;font-size:14px;color:#666;line-height:1.75;display:none;font-family:Poppins,sans-serif;">Gym Access Control Software helps fitness businesses manage who can access their facilities based on defined rules. Gymex supports access restrictions based on membership type, age, and time.</div>
    </div>
    <div class="ba-faq" onclick="this.classList.toggle('open')">
      <div style="padding:18px 24px;cursor:pointer;font-weight:600;font-size:15px;color:#0b1a3d;background:#f8fafc;display:flex;justify-content:space-between;align-items:center;font-family:Poppins,sans-serif;">Can Gymex restrict access for defaulting members? <i class="fa fa-chevron-down"></i></div>
      <div style="padding:0 24px 18px;font-size:14px;color:#666;line-height:1.75;display:none;font-family:Poppins,sans-serif;">Yes. Gymex provides the ability to block defaulting members, helping fitness businesses maintain better control over facility access.</div>
    </div>
    <div class="ba-faq" onclick="this.classList.toggle('open')">
      <div style="padding:18px 24px;cursor:pointer;font-weight:600;font-size:15px;color:#0b1a3d;background:#f8fafc;display:flex;justify-content:space-between;align-items:center;font-family:Poppins,sans-serif;">Can access be controlled according to membership type? <i class="fa fa-chevron-down"></i></div>
      <div style="padding:0 24px 18px;font-size:14px;color:#666;line-height:1.75;display:none;font-family:Poppins,sans-serif;">Yes. Gymex can apply access restrictions according to the membership purchased by the member, along with relevant age and time-based rules.</div>
    </div>
    <div class="ba-faq" onclick="this.classList.toggle('open')">
      <div style="padding:18px 24px;cursor:pointer;font-weight:600;font-size:15px;color:#0b1a3d;background:#f8fafc;display:flex;justify-content:space-between;align-items:center;font-family:Poppins,sans-serif;">Does Gymex support multiple gym branches? <i class="fa fa-chevron-down"></i></div>
      <div style="padding:0 24px 18px;font-size:14px;color:#666;line-height:1.75;display:none;font-family:Poppins,sans-serif;">Gymex supports reciprocity for multi-branch businesses, allowing eligible members to access different branches according to their purchased membership.</div>
    </div>
    <div class="ba-faq" onclick="this.classList.toggle('open')">
      <div style="padding:18px 24px;cursor:pointer;font-weight:600;font-size:15px;color:#0b1a3d;background:#f8fafc;display:flex;justify-content:space-between;align-items:center;font-family:Poppins,sans-serif;">Can Gymex track staff attendance? <i class="fa fa-chevron-down"></i></div>
      <div style="padding:0 24px 18px;font-size:14px;color:#666;line-height:1.75;display:none;font-family:Poppins,sans-serif;">Yes. Gymex can capture staff attendance along with member attendance, helping fitness businesses maintain attendance information in a connected system.</div>
    </div>
  </div>
</section>

{footer_html}

<script src="../javascript.js"></script>
<script>
// Modal
document.querySelectorAll('.open-modal-btn').forEach(function(btn) {{
  btn.addEventListener('click', function(e) {{
    e.preventDefault();
    document.getElementById('divemailpopup').classList.add('show');
    document.body.style.overflow = 'hidden';
  }});
}});
document.getElementById('close-contact-modal').addEventListener('click', function() {{
  document.getElementById('divemailpopup').classList.remove('show');
  document.body.style.overflow = 'auto';
  document.getElementById('emailsuccessmsg').style.display = 'none';
  document.getElementById('form-body').style.display = 'block';
}});
document.getElementById('divemailpopup').addEventListener('click', function(e) {{
  if (e.target === this) {{
    this.classList.remove('show');
    document.body.style.overflow = 'auto';
  }}
}});
document.querySelector('.send-again-btn').addEventListener('click', function() {{
  document.getElementById('emailsuccessmsg').style.display = 'none';
  document.getElementById('form-body').style.display = 'block';
}});
emailjs.init('AmP09sgXBaIgn9Juz');
var phoneInput = document.getElementById('number');
if (phoneInput) {{
  var iti = window.intlTelInput(phoneInput, {{
    utilsScript: 'https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js',
    separateDialCode: true,
    initialCountry: 'in'
  }});
}}
document.getElementById('contact-form').onsubmit = function(e) {{
  e.preventDefault();
  document.getElementById('loader').classList.add('show');
  document.getElementById('divemailpopup').classList.add('show');
  var fullNumber = iti ? iti.getNumber() : phoneInput.value;
  emailjs.send('service_1o6wljl', 'template_6dewzmp', {{
    firstname: document.getElementById('first-name').value,
    lastname: document.getElementById('last-name').value,
    company: document.getElementById('company').value,
    email: document.getElementById('email').value,
    phonenumber: fullNumber,
    message: this.message.value
  }}).then(function() {{
    document.getElementById('loader').classList.remove('show');
    document.getElementById('form-body').style.display = 'none';
    document.getElementById('emailsuccessmsg').style.display = 'block';
  }}, function(err) {{
    document.getElementById('loader').classList.remove('show');
    alert('Thank you! Your demo request has been submitted.');
    document.getElementById('divemailpopup').classList.remove('show');
    document.body.style.overflow = 'auto';
  }});
}};
document.addEventListener('keydown', function(e) {{
  if (e.key === 'Escape') {{
    document.getElementById('divemailpopup').classList.remove('show');
    document.body.style.overflow = 'auto';
  }}
}});
</script>
</body>
</html>'''

# Write the file
with open("biometric-access-control/biometric-access-control.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Done! Biometric & Access Control page rebuilt with exact docx content.")
