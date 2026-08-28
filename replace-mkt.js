const fs = require('fs');
let lines = fs.readFileSync('marketing-management/marketing-management.html', 'utf8').split('\n');

const newContent = `<!-- Section 1: Problem - Left text + Right visual list -->
<section style="padding:70px 24px; background:#fff;">
  <div style="max-width:1100px; margin:0 auto; display:grid; grid-template-columns:1fr 1fr; gap:60px; align-items:center;">
    <div>
      <p style="font-size:12px; font-weight:700; color:#f26522; text-transform:uppercase; letter-spacing:2px; margin-bottom:12px;">The Problem</p>
      <h2 style="font-size:34px; font-weight:800; color:#111; line-height:1.2; margin-bottom:20px;">Stop Losing Leads to Missed Follow-Ups</h2>
      <p style="font-size:16px; color:#555; line-height:1.8;">A potential member fills in a form, calls the front desk, or walks in. What happens next should not depend on someone remembering to call them later.</p>
    </div>
    <div style="display:flex; flex-direction:column; gap:16px;">
      <div style="display:flex; align-items:center; gap:16px; padding:18px 20px; background:#fef2f2; border-radius:12px; border-left:4px solid #ef4444;"><span style="font-size:22px;">&#128548;</span><p style="font-size:14px; color:#555; margin:0;">Searching through WhatsApp for an old enquiry</p></div>
      <div style="display:flex; align-items:center; gap:16px; padding:18px 20px; background:#fef2f2; border-radius:12px; border-left:4px solid #ef4444;"><span style="font-size:22px;">&#128203;</span><p style="font-size:14px; color:#555; margin:0;">Forgetting which staff member spoke to a prospect</p></div>
      <div style="display:flex; align-items:center; gap:16px; padding:18px 20px; background:#fef2f2; border-radius:12px; border-left:4px solid #ef4444;"><span style="font-size:22px;">&#128221;</span><p style="font-size:14px; color:#555; margin:0;">Losing walk-in details in a notebook</p></div>
      <div style="display:flex; align-items:center; gap:16px; padding:18px 20px; background:#fef2f2; border-radius:12px; border-left:4px solid #ef4444;"><span style="font-size:22px;">&#128260;</span><p style="font-size:14px; color:#555; margin:0;">Following up with the same person twice</p></div>
    </div>
  </div>
</section>

<!-- Section 2: Capture Leads - 3 large cards with colored tops -->
<section style="padding:70px 24px; background:#f8f9fc;">
  <div style="max-width:1100px; margin:0 auto;">
    <p style="font-size:12px; font-weight:700; color:#1565C0; text-transform:uppercase; letter-spacing:2px; text-align:center; margin-bottom:12px;">Lead Capture</p>
    <h2 style="font-size:34px; font-weight:800; color:#111; text-align:center; margin-bottom:16px;">Every Channel, One System</h2>
    <p style="font-size:16px; color:#555; line-height:1.8; max-width:700px; margin:0 auto 48px; text-align:center;">People discover your gym in different ways. Gymex makes sure every enquiry reaches the same pipeline.</p>
    <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:24px;">
      <div style="background:#fff; border-radius:16px; overflow:hidden; box-shadow:0 2px 12px rgba(0,0,0,.06);">
        <div style="height:8px; background:linear-gradient(90deg,#1565C0,#42a5f5);"></div>
        <div style="padding:28px;">
          <div style="width:52px; height:52px; background:#e8f0fe; border-radius:14px; display:flex; align-items:center; justify-content:center; margin-bottom:18px;"><i class="fa fa-globe" style="font-size:22px; color:#1565C0;"></i></div>
          <h3 style="font-size:17px; font-weight:700; color:#111; margin-bottom:10px;">Digital Channels</h3>
          <p style="font-size:14px; color:#666; line-height:1.7;">Website forms, social media, Google Ads, and landing pages - all captured automatically.</p>
        </div>
      </div>
      <div style="background:#fff; border-radius:16px; overflow:hidden; box-shadow:0 2px 12px rgba(0,0,0,.06);">
        <div style="height:8px; background:linear-gradient(90deg,#f26522,#ff8a50);"></div>
        <div style="padding:28px;">
          <div style="width:52px; height:52px; background:#fff3e0; border-radius:14px; display:flex; align-items:center; justify-content:center; margin-bottom:18px;"><i class="fa fa-users" style="font-size:22px; color:#f26522;"></i></div>
          <h3 style="font-size:17px; font-weight:700; color:#111; margin-bottom:10px;">In-Person Visits</h3>
          <p style="font-size:14px; color:#666; line-height:1.7;">Walk-ins, gym tours, trial sessions, and event visitors - logged instantly.</p>
        </div>
      </div>
      <div style="background:#fff; border-radius:16px; overflow:hidden; box-shadow:0 2px 12px rgba(0,0,0,.06);">
        <div style="height:8px; background:linear-gradient(90deg,#22c55e,#4ade80);"></div>
        <div style="padding:28px;">
          <div style="width:52px; height:52px; background:#f0fdf4; border-radius:14px; display:flex; align-items:center; justify-content:center; margin-bottom:18px;"><i class="fa fa-heart" style="font-size:22px; color:#22c55e;"></i></div>
          <h3 style="font-size:17px; font-weight:700; color:#111; margin-bottom:10px;">Referrals</h3>
          <p style="font-size:14px; color:#666; line-height:1.7;">Member referrals, corporate tie-ups, events, and partnerships - tracked in one place.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Section 3: Pipeline - Gradient flow -->
<section style="padding:70px 24px; background:#fff;">
  <div style="max-width:1100px; margin:0 auto;">
    <p style="font-size:12px; font-weight:700; color:#1565C0; text-transform:uppercase; letter-spacing:2px; text-align:center; margin-bottom:12px;">Sales Pipeline</p>
    <h2 style="font-size:34px; font-weight:800; color:#111; text-align:center; margin-bottom:16px;">See Every Prospect Journey</h2>
    <p style="font-size:16px; color:#555; line-height:1.8; max-width:700px; margin:0 auto 48px; text-align:center;">Know exactly where every prospect is - from first enquiry to sign-up.</p>
    <div style="display:flex; align-items:stretch; justify-content:center; gap:0; max-width:1000px; margin:0 auto; flex-wrap:wrap;">
      <div style="flex:1; min-width:140px; background:linear-gradient(135deg,#1565C0,#1976d2); color:#fff; padding:24px 18px; border-radius:12px 0 0 12px; text-align:center;"><div style="font-size:28px; font-weight:800; margin-bottom:6px;">01</div><div style="font-size:13px; font-weight:600; text-transform:uppercase;">New Enquiry</div></div>
      <div style="flex:1; min-width:140px; background:linear-gradient(135deg,#1976d2,#2196f3); color:#fff; padding:24px 18px; text-align:center;"><div style="font-size:28px; font-weight:800; margin-bottom:6px;">02</div><div style="font-size:13px; font-weight:600; text-transform:uppercase;">Contacted</div></div>
      <div style="flex:1; min-width:140px; background:linear-gradient(135deg,#2196f3,#42a5f5); color:#fff; padding:24px 18px; text-align:center;"><div style="font-size:28px; font-weight:800; margin-bottom:6px;">03</div><div style="font-size:13px; font-weight:600; text-transform:uppercase;">Tour Booked</div></div>
      <div style="flex:1; min-width:140px; background:linear-gradient(135deg,#42a5f5,#66bb6a); color:#fff; padding:24px 18px; text-align:center;"><div style="font-size:28px; font-weight:800; margin-bottom:6px;">04</div><div style="font-size:13px; font-weight:600; text-transform:uppercase;">Trial</div></div>
      <div style="flex:1; min-width:140px; background:linear-gradient(135deg,#f26522,#ff6d00); color:#fff; padding:24px 18px; border-radius:0 12px 12px 0; text-align:center;"><div style="font-size:28px; font-weight:800; margin-bottom:6px;">05</div><div style="font-size:13px; font-weight:600; text-transform:uppercase;">Joined!</div></div>
    </div>
  </div>
</section>

<!-- Section 4: Follow Up - Numbered steps -->
<section style="padding:70px 24px; background:#f8f9fc;">
  <div style="max-width:1100px; margin:0 auto;">
    <p style="font-size:12px; font-weight:700; color:#1565C0; text-transform:uppercase; letter-spacing:2px; text-align:center; margin-bottom:12px;">Follow-Up System</p>
    <h2 style="font-size:34p
