# -*- coding: utf-8 -*-
"""Rebuild 'Three Apps' cards on mobile-apps page — content-first design
(no phone mockups since real screenshots are not coming)."""
import re

P = 'mobile-apps/mobile-apps.html'
s = open(P, encoding='utf-8').read()

NEW = '''<section style="padding:60px 24px; background:#fff;">
<div style="max-width:1200px; margin:0 auto;">
<h2 style="font-size:clamp(28px,3.2vw,38px); font-weight:800; color:#111; text-align:center; margin-bottom:10px; text-transform:uppercase;">Three Apps. Three Experiences. <span style="color:#028ece;">One Gymex.</span></h2>
<p style="font-size:16px; color:#555; line-height:1.8; max-width:800px; margin:0 auto 36px; text-align:center;">Gymex doesn\u2019t have just one generic app \u2014 members, admins and prospects each get an experience built for them.</p>
<div style="display:grid; grid-template-columns:repeat(3,1fr); gap:20px; max-width:1050px; margin:0 auto;" class="nf-three">

<div style="background:#fff; border:1px solid #e5e7eb; border-radius:18px; overflow:hidden; display:flex; flex-direction:column; transition:transform .25s ease, box-shadow .25s ease;" onmouseover="this.style.transform='translateY(-6px)';this.style.boxShadow='0 18px 40px rgba(2,142,206,.15)'" onmouseout="this.style.transform='';this.style.boxShadow=''">
<div style="background:linear-gradient(135deg,#028ece,#0369a1); padding:18px 24px; display:flex; align-items:center; gap:12px;">
<div style="width:44px; height:44px; background:rgba(255,255,255,.18); border-radius:12px; display:flex; align-items:center; justify-content:center; flex-shrink:0;"><i class="fa fa-mobile-screen-button" style="font-size:20px; color:#fff;"></i></div>
<div><h3 style="font-size:16px; font-weight:800; color:#fff; margin:0; text-transform:uppercase; letter-spacing:.5px;">Member App</h3><p style="font-size:12px; color:rgba(255,255,255,.85); margin:2px 0 0;">For your gym members</p></div>
</div>
<div style="padding:22px 24px 24px; flex:1; display:flex; flex-direction:column;">
<p style="font-size:13.5px; color:#555; line-height:1.7; margin-bottom:16px;">Everything members need, right in their pocket.</p>
<div style="display:flex; flex-direction:column; gap:10px; margin-bottom:18px;">
<div style="display:flex; align-items:center; gap:10px;"><span style="width:26px; height:26px; background:#e8f0fe; border-radius:8px; display:flex; align-items:center; justify-content:center; flex-shrink:0;"><i class="fa fa-calendar-check" style="font-size:12px; color:#1565C0;"></i></span><span style="font-size:13px; color:#333; font-weight:600;">Class bookings &amp; appointments</span></div>
<div style="display:flex; align-items:center; gap:10px;"><span style="width:26px; height:26px; background:#e8f0fe; border-radius:8px; display:flex; align-items:center; justify-content:center; flex-shrink:0;"><i class="fa fa-id-card" style="font-size:12px; color:#1565C0;"></i></span><span style="font-size:13px; color:#333; font-weight:600;">Membership details &amp; renewals</span></div>
<div style="display:flex; align-items:center; gap:10px;"><span style="width:26px; height:26px; background:#e8f0fe; border-radius:8px; display:flex; align-items:center; justify-content:center; flex-shrink:0;"><i class="fa fa-dumbbell" style="font-size:12px; color:#1565C0;"></i></span><span style="font-size:13px; color:#333; font-weight:600;">Workout plans</span></div>
<div style="display:flex; align-items:center; gap:10px;"><span style="width:26px; height:26px; background:#e8f0fe; border-radius:8px; display:flex; align-items:center; justify-content:center; flex-shrink:0;"><i class="fa fa-qrcode" style="font-size:12px; color:#1565C0;"></i></span><span style="font-size:13px; color:#333; font-weight:600;">QR check-in attendance</span></div>
</div>
<div style="display:flex; flex-wrap:wrap; gap:6px; margin-top:auto;"><span style="font-size:11px; font-weight:600; background:#e8f0fe; color:#1565C0; padding:5px 10px; border-radius:20px;">Bookings</span><span style="font-size:11px; font-weight:600; background:#e8f0fe; color:#1565C0; padding:5px 10px; border-radius:20px;">Membership</span><span style="font-size:11px; font-weight:600; background:#e8f0fe; color:#1565C0; padding:5px 10px; border-radius:20px;">Workouts</span><span style="font-size:11px; font-weight:600; background:#e8f0fe; color:#1565C0; padding:5px 10px; border-radius:20px;">Attendance</span></div>
</div>
</div>

<div style="background:#fff; border:1px solid #e5e7eb; border-radius:18px; overflow:hidden; display:flex; flex-direction:column; transition:transform .25s ease, box-shadow .25s ease;" onmouseover="this.style.transform='translateY(-6px)';this.style.boxShadow='0 18px 40px rgba(242,101,34,.15)'" onmouseout="this.style.transform='';this.style.boxShadow=''">
<div style="background:linear-gradient(135deg,#f26522,#c2410c); padding:18px 24px; display:flex; align-items:center; gap:12px;">
<div style="width:44px; height:44px; background:rgba(255,255,255,.18); border-radius:12px; display:flex; align-items:center; justify-content:center; flex-shrink:0;"><i class="fa fa-chart-pie" style="font-size:20px; color:#fff;"></i></div>
<div><h3 style="font-size:16px; font-weight:800; color:#fff; margin:0; text-transform:uppercase; letter-spacing:.5px;">Admin App</h3><p style="font-size:12px; color:rgba(255,255,255,.85); margin:2px 0 0;">For owners &amp; managers</p></div>
</div>
<div style="padding:22px 24px 24px; flex:1; display:flex; flex-direction:column;">
<p style="font-size:13.5px; color:#555; line-height:1.7; margin-bottom:16px;">Your gym business, wherever you are.</p>
<div style="display:flex; flex-direction:column; gap:10px; margin-bottom:18px;">
<div style="display:flex; align-items:center; gap:10px;"><span style="width:26px; height:26px; background:#ffedd5; border-radius:8px; display:flex; align-items:center; justify-content:center; flex-shrink:0;"><i class="fa fa-gauge-high" style="font-size:12px; color:#c2410c;"></i></span><span style="font-size:13px; color:#333; font-weight:600;">Live business dashboard</span></div>
<div style="display:flex; align-items:center; gap:10px;"><span style="width:26px; height:26px; background:#ffedd5; border-radius:8px; display:flex; align-items:center; justify-content:center; flex-shrink:0;"><i class="fa fa-indian-rupee-sign" style="font-size:12px; color:#c2410c;"></i></span><span style="font-size:13px; color:#333; font-weight:600;">Collections &amp; payment follow-ups</span></div>
<div style="display:flex; align-items:center; gap:10px;"><span style="width:26px; height:26px; background:#ffedd5; border-radius:8px; display:flex; align-items:center; justify-content:center; flex-shrink:0;"><i class="fa fa-arrow-trend-up" style="font-size:12px; color:#c2410c;"></i></span><span style="font-size:13px; color:#333; font-weight:600;">Sales tracking on the go</span></div>
<div style="display:flex; align-items:center; gap:10px;"><span style="width:26px; height:26px; background:#ffedd5; border-radius:8px; display:flex; align-items:center; justify-content:center; flex-shrink:0;"><i class="fa fa-receipt" style="font-size:12px; color:#c2410c;"></i></span><span style="font-size:13px; color:#333; font-weight:600;">Expense entries &amp; approvals</span></div>
</div>
<div style="display:flex; flex-wrap:wrap; gap:6px; margin-top:auto;"><span style="font-size:11px; font-weight:600; background:#ffedd5; color:#c2410c; padding:5px 10px; border-radius:20px;">Dashboard</span><span style="font-size:11px; font-weight:600; background:#ffedd5; color:#c2410c; padding:5px 10px; border-radius:20px;">Collections</span><span style="font-size:11px; font-weight:600; background:#ffedd5; color:#c2410c; padding:5px 10px; border-radius:20px;">Sales</span><span style="font-size:11px; font-weight:600; background:#ffedd5; color:#c2410c; padding:5px 10px; border-radius:20px;">Expenses</span></div>
</div>
</div>

<div style="background:#fff; border:1px solid #e5e7eb; border-radius:18px; overflow:hidden; display:flex; flex-direction:column; transition:transform .25s ease, box-shadow .25s ease;" onmouseover="this.style.transform='translateY(-6px)';this.style.boxShadow='0 18px 40px rgba(34,197,94,.15)'" onmouseout="this.style.transform='';this.style.boxShadow=''">
<div style="background:linear-gradient(135deg,#22c55e,#15803d); padding:18px 24px; display:flex; align-items:center; gap:12px;">
<div style="width:44px; height:44px; background:rgba(255,255,255,.18); border-radius:12px; display:flex; align-items:center; justify-content:center; flex-shrink:0;"><i class="fa fa-user-plus" style="font-size:20px; color:#fff;"></i></div>
<div><h3 style="font-size:16px; font-weight:800; color:#fff; margin:0; text-transform:uppercase; letter-spacing:.5px;">Prospect App</h3><p style="font-size:12px; color:rgba(255,255,255,.85); margin:2px 0 0;">For your sales team</p></div>
</div>
<div style="padding:22px 24px 24px; flex:1; display:flex; flex-direction:column;">
<p style="font-size:13.5px; color:#555; line-height:1.7; margin-bottom:16px;">Capture opportunities while you\u2019re on the move.</p>
<div style="display:flex; flex-direction:column; gap:10px; margin-bottom:18px;">
<div style="display:flex; align-items:center; gap:10px;"><span style="width:26px; height:26px; background:#f0fdf4; border-radius:8px; display:flex; align-items:center; justify-content:center; flex-shrink:0;"><i class="fa fa-user-check" style="font-size:12px; color:#15803d;"></i></span><span style="font-size:13px; color:#333; font-weight:600;">Walk-in prospect capture</span></div>
<div style="display:flex; align-items:center; gap:10px;"><span style="width:26px; height:26px; background:#f0fdf4; border-radius:8px; display:flex; align-items:center; justify-content:center; flex-shrink:0;"><i class="fa fa-share-nodes" style="font-size:12px; color:#15803d;"></i></span><span style="font-size:13px; color:#333; font-weight:600;">Referral tracking</span></div>
<div style="display:flex; align-items:center; gap:10px;"><span style="width:26px; height:26px; background:#f0fdf4; border-radius:8px; display:flex; align-items:center; justify-content:center; flex-shrink:0;"><i class="fa fa-file-signature" style="font-size:12px; color:#15803d;"></i></span><span style="font-size:13px; color:#333; font-weight:600;">E-signature on joining forms</span></div>
</div>
<div style="display:flex; flex-wrap:wrap; gap:6px; margin-top:auto;"><span style="font-size:11px; font-weight:600; background:#f0fdf4; color:#15803d; padding:5px 10px; border-radius:20px;">Prospects</span><span style="font-size:11px; font-weight:600; background:#f0fdf4; color:#15803d; padding:5px 10px; border-radius:20px;">Referrals</span><span style="font-size:11px; font-weight:600; background:#f0fdf4; color:#15803d; padding:5px 10px; border-radius:20px;">E-Signature</span></div>
</div>
</div>

</div>
</div>
</section>'''

# Replace from the section start to its end (the three card divs + section close)
start = s.index('<section style="padding:60px 24px; background:#fff;">\n<div style="max-width:1200px; margin:0 auto;">\n<h2 style="font-size:clamp(28px,3.2vw,38px); font-weight:800; color:#111; text-align:center; margin-bottom:10px; text-transform:uppercase;">Three Apps.')
end_marker = '</section>\n\n<section style="padding:60px 24px; background:#f8f9fc;">'
end = s.index(end_marker, start)
s = s[:start] + NEW + '\n\n' + s[end:]

open(P, 'w', encoding='utf-8', newline='').write(s)
print('Three Apps section rebuilt')
