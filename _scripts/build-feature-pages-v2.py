#!/usr/bin/env python3
"""Build 3 feature pages with unique heroes + inline styles."""
import os

# ─── Reusable parts ───
NAV = '''<nav class="nav" id="nav">
        <div class="nav__logo-links-container">
          <a class="nav__logo-wrap" href="../index/index.html">
            <img class="logo" src="../assets/Gymex-logo-wit6Qpcs.svg" alt="logo">
          </a>
          
          <div class="flex-center">
            <div class="nav__list">
              <a class="nav__link" href="../index/index.html">Home</a>

              <div class="dropdown">
                <a class="nav__link" href="../business/business.html">Business Types <i class="fa fa-chevron-down" style="font-size:10px;"></i></a>
                <div class="dropdown-content mega-menu">
                    <div class="column">
                      <p class="mega-col-title">Gym &amp; Fitness</p>
                      <div style="display: flex;" class="inside"><img class="icon" src="data:image/svg+xml,%3csvg%20width='32'%20height='32'%20viewBox='0%200%2032%2032'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cg%20clip-path='url(%23clip0_903_1352)'%3e%3cpath%20fill-rule='evenodd'%20clip-rule='evenodd'%20d='M20.9926%2013.0602C21.4082%2013.1337%2022.0153%2013.3252%2022.3081%2013.8647C22.9495%2015.0465%2022.4197%2016.1699%2021.8513%2016.8684C21.4803%2017.324%2021.0029%2017.7528%2020.4474%2018.0154C20.3314%2018.0708%2020.0953%2018.1736%2019.8231%2018.1736C19.3157%2018.1736%2018.8185%2017.9609%2018.4106%2017.6951C18.3334%2017.9371%2018.2587%2018.2029%2018.1943%2018.4845C18.0669%2019.0249%2017.9979%2019.5755%2017.9882%2020.1284C18.8923%2019.8594%2019.8171%2019.8879%2020.6139%2020.3024C21.2124%2019.8685%2021.9012%2019.5527%2022.6378%2019.3745C23.754%2019.1047%2025.0935%2019.1419%2026.3103%2019.8887C27.1818%2020.4242%2027.8421%2021.4329%2027.9752%2022.5364C28.1143%2023.6866%2027.6807%2024.9444%2026.3695%2025.9111C25.4439%2026.593%2024.0331%2026.8564%2022.7348%2026.9522C21.391%2027.0518%2019.9717%2026.9838%2018.87%2026.8707C16.8281%2026.6618%2015.2602%2026.1366%2014.1646%2025.5947C13.4459%2025.2387%2012.4627%2024.7467%2012.151%2023.9928C11.9407%2023.4817%2011.9956%2022.8615%2012.0471%2022.3299C12.1158%2021.633%2012.2841%2020.7628%2012.5993%2019.8199C13.2278%2017.9379%2014.4582%2015.711%2016.7002%2014.0039C17.3897%2013.4786%2018.5437%2013.1527%2019.5097%2013.0436C20.0077%2012.9874%2020.5315%2012.9795%2020.9926%2013.0602Z'%20fill='%23028ECE'/%3e%3crect%20x='-1.33826'%20y='9.19873'%20width='21.0324'%20height='20.4713'%20rx='10.2356'%20transform='rotate(-30%20-1.33826%209.19873)'%20fill='url(%23paint0_linear_903_1352)'%20fill-opacity='0.5'/%3e%3c/g%3e%3cdefs%3e%3clinearGradient%20id='paint0_linear_903_1352'%20x1='9.17794'%20y1='9.19873'%20x2='9.17794'%20y2='29.67'%20gradientUnits='userSpaceOnUse'%3e%3cstop%20stop-color='%2331AAE1'/%3e%3cstop%20offset='1'%20stop-color='%2331AAE1'%20stop-opacity='0'/%3e%3c/linearGradient%3e%3cclipPath%20id='clip0_903_1352'%3e%3crect%20width='32'%20height='32'%20fill='white'/%3e%3c/clipPath%3e%3c/defs%3e%3c/svg%3e" alt="gym"><a href="../gym-management-software/gym-management-software.html" class="text1">GYM</a><br></div>
                      <div style="display: flex;" class="inside"><img class="icon" src="../assets/yoga-RKEkgKCN.svg" alt="yoga"><a href="../yoga-studio/yoga-studio.html" class="text1">YOGA STUDIO</a><br></div>
                      <div style="display: flex;" class="inside"><img src="../assets/Icons.svg" class="icon"> <a href="../swim-school/swim-school.html" class="text1">SWIM SCHOOL</a><br></div>
                    </div>
                    <div class="column">
                      <p class="mega-col-title">Studios &amp; Specialty</p>
                      <div style="display: flex;" class="inside"><a href="../pilates/pilates.html" class="text1">PILATES</a><br></div>
                      <div style="display: flex;" class="inside"><a href="../aerobics/aerobics.html" class="text1">AEROBICS</a><br></div>
                      <div style="display: flex;" class="inside"><a href="../dance-studio/dance-studio.html" class="text1">DANCE STUDIO</a><br></div>
                    </div>
                </div>
              </div>

<div class="dropdown">
  <a class="nav__link" href="../features/features.html">Features <i class="fa fa-chevron-down"></i></a>
  <div class="dropdown-content mega-menu features-mega">
        <div class="column">
      <p class="mega-col-title">MEMBER MANAGEMENT</p>
      <a href="../marketing-management/marketing-management.html" style="display: flex; gap:6px; align-items:center; text-decoration:none;" class="inside"><div class="mega-icon"><svg viewBox="0 0 24 24"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 0 1-3.46 0"/></svg></div><div><span class="text1" style="color:inherit;">Marketing Management</span><p class="mega-desc">Campaigns, promotions & member engagement</p></div></a>
      <a href="../lead-management/lead-management.html" style="display: flex; gap:6px; align-items:center; text-decoration:none;" class="inside"><div class="mega-icon"><svg viewBox="0 0 24 24"><path d="M22 3H2l8 9.46V19l4 2v-8.54L22 3z"/></svg></div><div><span class="text1" style="color:inherit;">Lead Management</span><p class="mega-desc">Capture leads, follow-ups & conversions</p></div></a>
      <a href="../member-management/member-management.html" style="display: flex; gap:6px; align-items:center; text-decoration:none;" class="inside"><div class="mega-icon"><svg viewBox="0 0 24 24"><path d="M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5c-1.66 0-3 1.34-3 3s1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5C6.34 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"/></svg></div><div><span class="text1" style="color:inherit;">Member Management</span><p class="mega-desc">Profiles, plans, payments & history</p></div></a>
      <a href="../staff-management/staff-management.html" style="display: flex; gap:6px; align-items:center; text-decoration:none;" class="inside"><div class="mega-icon"><svg viewBox="0 0 24 24"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/></svg></div><div><span class="text1" style="color:inherit;">Staff Management</span><p class="mega-desc">Roles, access & staff performance</p></div></a>
      <a href="../expense-management/expense-management.html" style="display: flex; gap:6px; align-items:center; text-decoration:none;" class="inside"><div class="mega-icon"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 6v12"/><path d="M15 9.5c0-1.38-1.34-2.5-3-2.5s-3 1.12-3 2.5 1.34 2.5 3 2.5 3 1.12 3 2.5-1.34 2.5-3 2.5"/></svg></div><div><span class="text1" style="color:inherit;">Expense Management</span><p class="mega-desc">Track costs & business expenses</p></div></a>
      <a href="../task-management/task-management.html" style="display: flex; gap:6px; align-items:center; text-decoration:none;" class="inside"><div class="mega-icon"><svg viewBox="0 0 24 24"><path d="M19 3h-4.18C14.4 1.84 13.3 1 12 1c-1.3 0-2.4.84-2.82 2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-7 0c.55 0 1 .45 1 1s-.45 1-1 1-1-.45-1-1 .45-1 1-1zm-2 14l-4-4 1.41-1.41L10 14.17l6.59-6.59L18 9l-8 8z"/></svg></div><div><span class="text1" style="color:inherit;">Task Management</span><p class="mega-desc">Assign tasks & track progress</p></div></a>
    </div>
    <div class="column">
      <p class="mega-col-title">OPERATIONS</p>
      <a href="../data-analysis-dashboard/data-analysis-dashboard.html" style="display: flex; gap:6px; align-items:center; text-decoration:none;" class="inside"><div class="mega-icon"><svg viewBox="0 0 24 24"><path d="M11 2v20c5.07-.5 9-4.79 9-10s-3.93-9.5-9-10zM2 12c0 4.42 3.13 8.09 7.3 8.94V12H2zm13.7-6.58C17.13 7.52 18 9.66 18 12h-5.7V5.42z"/></svg></div><div><span class="text1" style="color:inherit;">Data Analysis & Dashboard</span><p class="mega-desc">Trends, insights & performance reports</p></div></a>
      <a href="../appointment-and-class/appointment-and-class.html" style="display: flex; gap:6px; align-items:center; text-decoration:none;" class="inside"><div class="mega-icon"><svg viewBox="0 0 24 24"><path d="M19 3h-1V1h-2v2H8V1H6v2H5c-1.11 0-1.99.9-1.99 2L3 19c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V8h14v11zM9 10H7v2h2v-2zm4 0h-2v2h2v-2zm4 0h-2v2h2v-2z"/></svg></div><div><span class="text1" style="color:inherit;">Appointment & Class Booking</span><p class="mega-desc">Appointments, classes & bookings</p></div></a>
      <a href="../biometric-access-control/biometric-access-control.html" style="display: flex; gap:6px; align-items:center; text-decoration:none;" class="inside"><div class="mega-icon"><svg viewBox="0 0 24 24"><path d="M17.81 4.47c-.08 0-.16-.02-.23-.06C15.66 3.42 14 3 12.01 3c-1.98 0-3.86.47-5.57 1.41-.24.13-.54.04-.68-.2-.13-.24-.04-.55.2-.68C7.82 2.52 9.86 2 12.01 2c2.13 0 3.99.47 6.03 1.52.25.13.34.43.21.67-.09.18-.26.28-.44.28z"/></svg></div><div><span class="text1" style="color:inherit;">Biometric & Access Control</span><p class="mega-desc">Biometric attendance & secure access</p></div></a>
      <a href="../intelligent-alerts/intelligent-alerts-reminders.html" style="display: flex; gap:6px; align-items:center; text-decoration:none;" class="inside"><div class="mega-icon"><svg viewBox="0 0 24 24"><path d="M12 22c1.1 0 2-.9 2-2h-4c0 1.1.89 2 2 2zm6-6v-5c0-3.07-1.64-5.64-4.5-6.32V4c0-.83-.67-1.5-1.5-1.5s-1.5.67-1.5 1.5v.68C7.63 5.36 6 7.92 6 11v5l-2 2v1h16v-1l-2-2z"/></svg></div><div><span class="text1" style="color:inherit;">Intelligent Alerts & Reminder</span><p class="mega-desc">Smart alerts, reminders & updates</p></div></a>
      <a href="../features/features.html" style="display: flex; gap:6px; align-items:center; text-decoration:none;" class="inside"><div class="mega-icon"><svg viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z"/><path d="M12 2C6.477 2 2 6.477 2 12c0 1.89.525 3.66 1.438 5.168L2 22l4.832-1.438A9.955 9.955 0 0 0 12 22c5.523 0 10-4.477 10-10S17.523 2 12 2z"/></svg></div><div><span class="text1" style="color:inherit;">WhatsApp Automation</span><p class="mega-desc">WhatsApp campaigns, reminders & auto-replies</p></div></a>
      <a href="../features/features.html" style="display: flex; gap:6px; align-items:center; text-decoration:none;" class="inside"><div class="mega-icon"><svg viewBox="0 0 24 24"><path d="M15.5 14h-.79l-.28-.27A6.471 6.471 0 0 0 16 9.5 6.5 6.5 0 1 0 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/></svg></div><div><span class="text1" style="color:inherit;">Mobile Apps</span><p class="mega-desc">Member, staff & admin mobile apps</p></div></a>
    </div>
    <div class="column">
      <p class="mega-col-title">BILLING & TOOLS</p>
      <a href="../payroll-commission/payroll-commission.html" style="display: flex; gap:6px; align-items:center; text-decoration:none;" class="inside"><div class="mega-icon"><svg viewBox="0 0 24 24"><rect x="2" y="6" width="20" height="12" rx="2"/><circle cx="12" cy="12" r="3"/></svg></div><div><span class="text1" style="color:inherit;">Payroll & Commission</span><p class="mega-desc">Salaries, commissions & staff payouts</p></div></a>
      <a href="../features/features.html" style="display: flex; gap:6px; align-items:center; text-decoration:none;" class="inside"><div class="mega-icon"><svg viewBox="0 0 24 24"><path d="M20.57 14.86L22 13.43l-1.43-1.43L17 15.57 8.43 7 12 3.43 10.57 2 9.14 3.43 7.71 2 5.57 4.14 4.14 2.71 2.71 4.14 1.43 1.43L2 7.71l1.43 1.43L2 10.57 3.43 12 7 8.43l8.57 8.57L12 20.57l1.43 1.43 1.43-1.43L16.29 22l2.14-2.14 1.43 1.43 1.43-1.43-1.43-1.43L22 16.29z"/></svg></div><div><span class="text1" style="color:inherit;">Workout & Diet Planner</span><p class="mega-desc">Personalized workouts & diet plans</p></div></a>
      <a href="../features/features.html" style="display: flex; gap:6px; align-items:center; text-decoration:none;" class="inside"><div class="mega-icon"><svg viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-7 14h-2v-2h2v2zm0-4h-2v-2h2v2zm0-4h-2V7h2v2zm4 8h-2v-2h2v2zm0-4h-2v-2h2v2zm0-4h-2V7h2v2zm-8 8H6v-2h1.5v2zm0-4H6v-2h1.5v2zm0-4H6V7h1.5v2zm8 8h-2v-6h2v6zm4 0h-2V7h2v10z"/></svg></div><div><span class="text1" style="color:inherit;">POS & Locker Management</span><p class="mega-desc">POS sales, transactions & lockers</p></div></a>
      <a href="../features/features.html" style="display: flex; gap:6px; align-items:center; text-decoration:none;" class="inside"><div class="mega-icon"><svg viewBox="0 0 24 24"><path d="M15 11V5l-3-3-3 3v2H3v14h18V11h-6zm-8 8H5v-2h2v2zm0-4H5v-2h2v2zm0-4H5V9h2v2zm6 8h-2v-2h2v2zm0-4h-2v-2h2v2zm0-4h-2V9h2v2zm0-4h-2V5h2v2zm6 12h-2v-2h2v2zm0-4h-2v-2h2v2z"/></svg></div><div><span class="text1" style="color:inherit;">Club Facilities</span><p class="mega-desc">Facilities, services & member access</p></div></a>
      <a href="../features/features.html" style="display: flex; gap:6px; align-items:center; text-decoration:none;" class="inside"><div class="mega-icon"><svg viewBox="0 0 24 24"><path d="M19.14 12.94c.04-.3.06-.61.06-.94 0-.32-.02-.64-.07-.94l2.03-1.58c.18-.14.23-.41.12-.61l-1.92-3.32c-.12-.22-.37-.29-.59-.22l-2.39.96c-.5-.38-1.03-.7-1.62-.94l-.36-2.54c-.04-.24-.24-.41-.48-.41h-3.84c-.24 0-.43.17-.47.41l-.36 2.54c-.59.24-1.13.57-1.62.94l-2.39-.96c-.22-.08-.47 0-.59.22L2.74 8.87c-.12.21-.08.47.12.61l2.03 1.58c-.05.3-.07.62-.07.94s.02.64.07.94l-2.03 1.58c-.18.14-.23.41-.12.61l1.92 3.32c.12.22.37.29.59.22l2.39-.96c.5.38 1.03.7 1.62.94l.36 2.54c.05.24.24.41.48.41h3.84c.24 0 .44-.17.47-.41l.36-2.54c.59-.24 1.13-.56 1.62-.94l2.39.96c.22.08.47 0 .59-.22l1.92-3.32c.12-.22.07-.47-.12-.61l-2.01-1.58zM12 15.6c-1.98 0-3.6-1.62-3.6-3.6s1.62-3.6 3.6-3.6 3.6 1.62 3.6 3.6-1.62 3.6-3.6 3.6z"/></svg></div><div><span class="text1" style="color:inherit;">Equipment Inventory</span><p class="mega-desc">Equipment, stock & maintenance tracking</p></div></a>
    </div>
  </div>
</div>

              <a class="nav__link" href="../pricing/pricing.html">Pricing</a>
              <a class="nav__link" href="../blog/blog.html">Blog</a>
              <a class="nav__link" href="../about/about.html">About</a>
              <a class="nav__link" href="../career/career.html">Career</a>
              <a class="nav__link" href="../contact/contact.html">Contact</a>
            </div>
          </div>
        </div>
        <a class="open-modal-btn nav__cta" href="#">GET YOUR FREE DEMO <span class="arrow-circle"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg></span></a>
      </nav>'''

FOOTER = '''<div style="background:#0b1a3d; padding:0;">
  <div style="max-width:1200px; margin:0 auto; padding:20px 24px 16px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">
    <div style="display:flex; gap:28px; flex-wrap:wrap; align-items:center;">
      <a href="../index/index.html" style="color:rgba(255,255,255,.85); font-size:13px; font-weight:600; text-decoration:none; letter-spacing:.5px;">HOME</a>
      <a href="../about/about.html" style="color:rgba(255,255,255,.85); font-size:13px; font-weight:600; text-decoration:none; letter-spacing:.5px;">ABOUT US</a>
      <a href="../pricing/pricing.html" style="color:rgba(255,255,255,.85); font-size:13px; font-weight:600; text-decoration:none; letter-spacing:.5px;">PRICING</a>
      <a href="../blog/blog.html" style="color:rgba(255,255,255,.85); font-size:13px; font-weight:600; text-decoration:none; letter-spacing:.5px;">BLOG</a>
      <a href="../contact/contact.html" style="color:rgba(255,255,255,.85); font-size:13px; font-weight:600; text-decoration:none; letter-spacing:.5px;">CONTACT US</a>
      <a href="#" style="color:rgba(255,255,255,.85); font-size:13px; font-weight:600; text-decoration:none; letter-spacing:.5px;">TERMS &amp; CONDITIONS</a>
      <a href="../privacy-policy/privacy-policy.html" style="color:rgba(255,255,255,.85); font-size:13px; font-weight:600; text-decoration:none; letter-spacing:.5px;">PRIVACY POLICY</a>
      <a href="#" style="color:rgba(255,255,255,.85); font-size:13px; font-weight:600; text-decoration:none; letter-spacing:.5px;">REFUND POLICY</a>
    </div>
    <a class="open-modal-btn" href="#" style="background:#f26522; color:#fff; padding:10px 26px; border-radius:50px; font-size:13px; font-weight:700; text-decoration:none; white-space:nowrap; letter-spacing:.5px;">ASK FOR DEMO</a>
  </div>
  <div style="max-width:1200px; margin:0 auto; padding:40px 24px 36px; display:flex; justify-content:space-between; gap:40px;">
    <div style="flex:1;"><h3 style="color:#fff; font-size:18px; font-weight:700; margin-bottom:14px;">About Us</h3><p style="color:rgba(255,255,255,.7); font-size:14px; line-height:1.8;">Gymex is a powerful cloud based gym management software built to facilitate to effectively manage gym &amp; fitness related businesses.</p></div>
    <div style="flex:1.4;"><h3 style="color:#fff; font-size:18px; font-weight:700; margin-bottom:14px;">Contact Us</h3><p style="color:rgba(255,255,255,.7); font-size:14px; line-height:1.8; margin-bottom:24px;">GreyBits Technologies, Office No. 2, An-Nazir Building, Momin Nagar, Patel&nbsp;Estate&nbsp;Road, Jogeshwari West, Mumbai - 400102</p><div style="display:flex; gap:40px;"><div><h4 style="color:#fff; font-size:15px; font-weight:700; margin-bottom:12px;">For Sales</h4><div style="display:flex; align-items:center; gap:8px; margin-bottom:8px;"><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#4da6ff" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg><a href="tel:+917710862007" style="color:rgba(255,255,255,.7); font-size:14px; text-decoration:none;">+91 7710862007</a></div><div style="display:flex; align-items:center; gap:8px;"><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#4da6ff" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg><a href="mailto:sales@gymex.online" style="color:rgba(255,255,255,.7); font-size:14px; text-decoration:none;">sales@gymex.online</a></div></div><div><h4 style="color:#fff; font-size:15px; font-weight:700; margin-bottom:12px;">For Support</h4><div style="display:flex; align-items:center; gap:8px; margin-bottom:8px;"><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#4da6ff" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg><a href="tel:+918291682083" style="color:rgba(255,255,255,.7); font-size:14px; text-decoration:none;">+91 8291682083</a></div><div style="display:flex; align-items:center; gap:8px;"><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#4da6ff" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg><a href="mailto:support@gymex.online" style="color:rgba(255,255,255,.7); font-size:14px; text-decoration:none;">support@gymex.online</a></div></div></div></div>
    <div style="flex:0.5; text-align:right;"><h3 style="color:#fff; font-size:18px; font-weight:700; margin-bottom:14px;">Follow Us On</h3><div style="display:flex; gap:12px; justify-content:flex-end;"><a href="https://www.facebook.com/gymexsoftware" target="_blank" style="display:flex;align-items:center;justify-content:center;width:38px;height:38px;background:#1877F2;border-radius:50%;transition:transform .2s;text-decoration:none;"><svg width="18" height="18" viewBox="0 0 24 24" fill="white"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg></a><a href="https://www.instagram.com/gymexclubmanagement" target="_blank" style="display:flex;align-items:center;justify-content:center;width:38px;height:38px;border-radius:50%;background:linear-gradient(45deg,#f09433,#e6683c,#dc2743,#cc2366,#bc1888);transition:transform .2s;text-decoration:none;"><svg width="18" height="18" viewBox="0 0 24 24" fill="white"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg></a><a href="https://www.linkedin.com/company/gymex-club-management-software/" target="_blank" style="display:flex;align-items:center;justify-content:center;width:38px;height:38px;background:#0A66C2;border-radius:50%;transition:transform .2s;text-decoration:none;"><svg width="16" height="16" viewBox="0 0 24 24" fill="white"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg></a></div></div>
  </div>
  <div style="border-top:1px solid rgba(255,255,255,.1); padding:16px 0;"><div style="max-width:1200px; margin:0 auto; padding:0 24px; text-align:center;"><p style="color:rgba(255,255,255,.5); font-size:13px;">&copy; 2024 Gymex Club Management Software. All Rights Reserved.</p></div></div>
</div>'''

def head(title, desc, keywords):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<script type="text/javascript">(function(c,l,a,r,i,t,y){{c[a]=c[a]||function(){{(c[a].q=c[a].q||[]).push(arguments)}};t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y)}})(window, document, "clarity", "script", "n95oax955q");</script>
<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&'+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f)}})(window,document,'script','dataLayer','GTM-KPCRHTFH');</script>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{keywords}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="icon" type="image/x-icon" href="../assets/gymex-favicon-U7mChGv0.ico">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<link rel="stylesheet" href="../style.css">
<script src="../javascript.js"></script>
'''

# ══════════════════════════════════════════════════════════════
# PAGE 1: INTELLIGENT ALERTS & REMINDERS
# ══════════════════════════════════════════════════════════════
def build_intelligent_alerts():
    h = head(
        "Gym Reminder Software & Intelligent Alerts | Gymex",
        "Send customized gym alerts and reminders for members and staff with Gymex. Manage renewal, balance, billing, appointment and class notifications from one platform.",
        "Gym Reminder Software, Gym Alerts and Notifications Software, Gym Membership Reminder Software, Automated Gym Reminders, Gym Payment Reminder Software, Gym Notification Software"
    )
    return h + NAV + '''
<style>
.ia-h1{font-family:'Poppins',sans-serif!important;font-size:36px!important;font-weight:800!important;line-height:1.25!important;margin:0 0 16px!important;color:#fff!important;}
.ia-p{font-family:'Poppins',sans-serif!important;font-size:16px!important;line-height:1.75!important;margin:0 0 24px!important;color:rgba(255,255,255,.85)!important;}
.ia-btn{display:inline-block!important;background:#f26522!important;color:#fff!important;padding:14px 32px!important;border-radius:50px!important;font-size:14px!important;font-weight:700!important;text-decoration:none!important;letter-spacing:.5px!important;transition:all .3s!important;}
.ia-btn:hover{background:#e05a1a!important;transform:translateY(-2px)!important;box-shadow:0 8px 24px rgba(242,101,34,.3)!important;}
.ia-sec{font-family:'Poppins',sans-serif!important;padding:70px 24px!important;}
.ia-wrap{max-width:1100px!important;margin:0 auto!important;}
.ia-h2{font-size:28px!important;font-weight:700!important;color:#0b1a3d!important;margin:0 0 16px!important;line-height:1.3!important;}
.ia-sub{font-size:16px!important;color:#555!important;line-height:1.7!important;margin:0 0 12px!important;}
.ia-chips{display:flex!important;flex-wrap:wrap!important;gap:12px!important;margin:24px 0!important;}
.ia-chip{display:inline-flex!important;align-items:center!important;gap:8px!important;background:#f0f4f8!important;padding:10px 20px!important;border-radius:50px!important;font-size:14px!important;font-weight:600!important;color:#0b1a3d!important;border:1px solid #e2e8f0!important;}
.ia-chip i{color:#f26522!important;}
.ia-grid{display:grid!important;grid-template-columns:repeat(auto-fit,minmax(300px,1fr))!important;gap:24px!important;margin:32px 0!important;}
.ia-card{background:#fff!important;border-radius:16px!important;padding:32px!important;border:1px solid #e8edf3!important;transition:transform .3s,box-shadow .3s!important;}
.ia-card:hover{transform:translateY(-4px)!important;box-shadow:0 12px 32px rgba(0,0,0,.08)!important;}
.ia-card-icon{width:52px!important;height:52px!important;border-radius:14px!important;display:flex!important;align-items:center!important;justify-content:center!important;font-size:22px!important;color:#fff!important;margin-bottom:18px!important;}
.ia-card h3{font-size:18px!important;font-weight:700!important;color:#0b1a3d!important;margin:0 0 10px!important;}
.ia-card p{font-size:14px!important;color:#666!important;line-height:1.7!important;margin:0!important;}
.ia-flow{display:flex!important;align-items:center!important;justify-content:center!important;flex-wrap:wrap!important;gap:12px!important;margin:32px 0!important;}
.ia-flow-step{background:linear-gradient(135deg,#0b1a3d,#1a3a5c)!important;color:#fff!important;padding:12px 22px!important;border-radius:12px!important;font-size:13px!important;font-weight:600!important;}
.ia-flow-arrow{color:#f26522!important;font-size:18px!important;}
.ia-cta{background:linear-gradient(135deg,#0b1a3d 0%,#1a3a5c 100%)!important;text-align:center!important;padding:60px 24px!important;}
.ia-cta h2{color:#fff!important;font-size:30px!important;font-weight:700!important;margin:0 0 14px!important;}
.ia-cta p{color:rgba(255,255,255,.8)!important;font-size:16px!important;margin:0 0 28px!important;line-height:1.7!important;}
.ia-faq{border:1px solid #e8edf3!important;border-radius:12px!important;margin-bottom:12px!important;overflow:hidden!important;}
.ia-faq-q{padding:18px 24px!important;cursor:pointer!important;font-weight:600!important;font-size:15px!important;color:#0b1a3d!important;background:#f8fafc!important;display:flex!important;justify-content:space-between!important;align-items:center!important;}
.ia-faq-q i{transition:transform .3s!important;}
.ia-faq-a{padding:0 24px 18px!important;font-size:14px!important;color:#666!important;line-height:1.75!important;display:none!important;}
.ia-faq.open .ia-faq-a{display:block!important;}
.ia-faq.open .ia-faq-q i{transform:rotate(180deg)!important;}
</style>

<section style="background:linear-gradient(135deg,#0b1a3d 0%,#1a3a5c 50%,#0d2847 100%)!important;padding:90px 24px 70px!important;position:relative!important;overflow:hidden!important;">
  <div style="position:absolute!important;top:-40%!important;right:-15%!important;width:500px!important;height:500px!important;border-radius:50%!important;background:radial-gradient(circle,rgba(242,101,34,.12) 0%,transparent 70%)!important;"></div>
  <div style="position:absolute!important;bottom:-30%!important;left:-10%!important;width:400px!important;height:400px!important;border-radius:50%!important;background:radial-gradient(circle,rgba(49,170,225,.1) 0%,transparent 70%)!important;"></div>
  <div class="ia-wrap" style="position:relative!important;z-index:1!important;">
    <span style="display:inline-block!important;background:rgba(242,101,34,.15)!important;color:#f26522!important;font-size:12px!important;font-weight:700!important;letter-spacing:2px!important;padding:6px 20px!important;border-radius:30px!important;margin-bottom:20px!important;font-family:'Poppins',sans-serif!important;">INTELLIGENT ALERTS & REMINDERS</span>
    <h1 class="ia-h1">Smart Alerts &<br>Automated Reminders<br>for Your Gym</h1>
    <p class="ia-p" style="max-width:600px!important;">Keep members informed and staff updated with automated reminders, renewal alerts, payment notifications, and class schedules — all managed from one connected platform.</p>
    <a class="ia-btn" href="#">Get Your Free Demo <i class="fa fa-arrow-up" style="margin-left:8px!important;"></i></a>
  </div>
</section>

<section class="ia-sec" style="background:#f8fafc!important;">
  <div class="ia-wrap">
    <h2 class="ia-h2" style="text-align:center!important;">Keep Members Informed Before They Even Ask</h2>
    <p class="ia-sub" style="text-align:center!important;max-width:700px;margin:0 auto 24px!important;">Gymex Intelligent Alerts & Reminder Software sends timely notifications to members and staff so nothing falls through the cracks.</p>
    <div class="ia-chips" style="justify-content:center!important;">
      <span class="ia-chip"><i class="fa fa-bell"></i> Membership Renewals</span>
      <span class="ia-chip"><i class="fa fa-credit-card"></i> Payment Due Alerts</span>
      <span class="ia-chip"><i class="fa fa-calendar"></i> Class Schedules</span>
      <span class="ia-chip"><i class="fa fa-user-plus"></i> Appointment Reminders</span>
      <span class="ia-chip"><i class="fa fa-star"></i> Birthday Wishes</span>
      <span class="ia-chip"><i class="fa fa-clock-o"></i> Trial Expiry</span>
    </div>
  </div>
</section>

<section class="ia-sec" style="background:#fff!important;">
  <div class="ia-wrap">
    <h2 class="ia-h2" style="text-align:center!important;">Multi-Channel Notifications That Reach Members Everywhere</h2>
    <p class="ia-sub" style="text-align:center!important;max-width:700px;margin:0 auto 32px!important;">Gymex supports SMS, email, and in-app notifications so you can reach members on the channel that works best for them.</p>
    <div class="ia-grid" style="grid-template-columns:repeat(3,1fr)!important;">
      <div class="ia-card">
        <div class="ia-card-icon" style="background:linear-gradient(135deg,#25D366,#128C7E)!important;"><i class="fa fa-whatsapp"></i></div>
        <h3>SMS & WhatsApp</h3>
        <p>Send renewal reminders, payment confirmations, and class updates via SMS or WhatsApp directly to members.</p>
      </div>
      <div class="ia-card">
        <div class="ia-card-icon" style="background:linear-gradient(135deg,#4285F4,#34A853)!important;"><i class="fa fa-envelope"></i></div>
        <h3>Email Notifications</h3>
        <p>Automated email campaigns for promotional offers, membership updates, and important gym announcements.</p>
      </div>
      <div class="ia-card">
        <div class="ia-card-icon" style="background:linear-gradient(135deg,#f26522,#e05a1a)!important;"><i class="fa fa-mobile"></i></div>
        <h3>In-App Alerts</h3>
        <p>Push notifications through the gym app for real-time alerts on bookings, class changes, and account updates.</p>
      </div>
    </div>
  </div>
</section>

<section class="ia-sec" style="background:#f8fafc!important;">
  <div class="ia-wrap">
    <h2 class="ia-h2" style="text-align:center!important;">Automated Reminder Workflow</h2>
    <p class="ia-sub" style="text-align:center!important;max-width:600px;margin:0 auto!important;">Set it once, and Gymex handles the rest.</p>
    <div class="ia-flow">
      <span class="ia-flow-step"><i class="fa fa-cog"></i> Set Reminder Rule</span>
      <span class="ia-flow-arrow"><i class="fa fa-arrow-right"></i></span>
      <span class="ia-flow-step"><i class="fa fa-database"></i> Member Data Match</span>
      <span class="ia-flow-arrow"><i class="fa fa-arrow-right"></i></span>
      <span class="ia-flow-step"><i class="fa fa-paper-plane"></i> Auto Send Alert</span>
      <span class="ia-flow-arrow"><i class="fa fa-arrow-right"></i></span>
      <span class="ia-flow-step"><i class="fa fa-check-circle"></i> Member Notified</span>
    </div>
  </div>
</section>

<section class="ia-sec" style="background:#fff!important;">
  <div class="ia-wrap">
    <h2 class="ia-h2" style="text-align:center!important;">Types of Alerts & Reminders You Can Send</h2>
    <div class="ia-grid">
      <div class="ia-card"><div class="ia-card-icon" style="background:#f26522!important;"><i class="fa fa-bell"></i></div><h3>Membership Renewal Alerts</h3><p>Automatically notify members before their membership expires so they can renew on time without disruption.</p></div>
      <div class="ia-card"><div class="ia-card-icon" style="background:#028ECE!important;"><i class="fa fa-rupee"></i></div><h3>Payment Due & Overdue Alerts</h3><p>Send payment reminders for pending dues, EMIs, and outstanding balances to improve collection rates.</p></div>
      <div class="ia-card"><div class="ia-card-icon" style="background:#34A853!important;"><i class="fa fa-calendar-check-o"></i></div><h3>Class & Appointment Reminders</h3><p>Remind members about upcoming classes, personal training sessions, and booked appointments.</p></div>
      <div class="ia-card"><div class="ia-card-icon" style="background:#9C27B0!important;"><i class="fa fa-gift"></i></div><h3>Birthday & Anniversary Wishes</h3><p>Send personalized birthday and anniversary messages to make members feel valued and connected.</p></div>
      <div class="ia-card"><div class="ia-card-icon" style="background:#FF5722!important;"><i class="fa fa-hourglass-half"></i></div><h3>Trial Expiry Reminders</h3><p>Alert trial members before their free trial ends and encourage them to convert to a paid membership.</p></div>
      <div class="ia-card"><div class="ia-card-icon" style="background:#607D8B!important;"><i class="fa fa-users"></i></div><h3>Staff Notifications</h3><p>Send shift reminders, schedule changes, and important updates to your gym staff and trainers.</p></div>
    </div>
  </div>
</section>

<section class="ia-cta">
  <div class="ia-wrap">
    <h2>Never Miss a Renewal or Payment Again</h2>
    <p>Automate your gym communication with intelligent alerts and reminders that keep members engaged and payments on track.</p>
    <a class="ia-btn" href="#">Get Your Free Demo</a>
  </div>
</section>

<section class="ia-sec" style="background:#fff!important;">
  <div class="ia-wrap">
    <h2 class="ia-h2" style="text-align:center!important;">Frequently Asked Questions</h2>
    <div class="ia-faq" onclick="this.classList.toggle('open')">
      <div class="ia-faq-q">What types of alerts can I send with Gymex? <i class="fa fa-chevron-down"></i></div>
      <div class="ia-faq-a">Gymex supports membership renewal alerts, payment due reminders, class schedule notifications, appointment reminders, birthday wishes, trial expiry alerts, and custom promotional messages.</div>
    </div>
    <div class="ia-faq" onclick="this.classList.toggle('open')">
      <div class="ia-faq-q">Can I send alerts via SMS and WhatsApp? <i class="fa fa-chevron-down"></i></div>
      <div class="ia-faq-a">Yes. Gymex supports SMS and WhatsApp integration for sending automated alerts to members and staff.</div>
    </div>
    <div class="ia-faq" onclick="this.classList.toggle('open')">
      <div class="ia-faq-q">Are reminders sent automatically? <i class="fa fa-chevron-down"></i></div>
      <div class="ia-faq-a">Yes. Once you set up reminder rules, Gymex automatically sends alerts at the scheduled time without manual intervention.</div>
    </div>
    <div class="ia-faq" onclick="this.classList.toggle('open')">
      <div class="ia-faq-q">Can I customize the alert messages? <i class="fa fa-chevron-down"></i></div>
      <div class="ia-faq-a">Yes. You can fully customize alert templates with member names, membership details, and personalized content.</div>
    </div>
    <div class="ia-faq" onclick="this.classList.toggle('open')">
      <div class="ia-faq-q">Does it send staff notifications too? <i class="fa fa-chevron-down"></i></div>
      <div class="ia-faq-a">Yes. You can send shift reminders, schedule changes, and important announcements to staff and trainers.</div>
    </div>
    <div class="ia-faq" onclick="this.classList.toggle('open')">
      <div class="ia-faq-q">Is there a limit on how many alerts I can send? <i class="fa fa-chevron-down"></i></div>
      <div class="ia-faq-a">Gymex offers generous alert limits based on your plan. Contact our team for details on high-volume messaging.</div>
    </div>
  </div>
</section>

''' + FOOTER + '''
<script src="../javascript.js"></script>
</body>
</html>'''


# ══════════════════════════════════════════════════════════════
# PAGE 2: BIOMETRIC & ACCESS CONTROL
# ══════════════════════════════════════════════════════════════
def build_biometric():
    h = head(
        "Gym Biometric Attendance & Access Control Software | Gymex",
        "Track staff and member attendance with biometric, RFID, QR code, and manual check-ins. Manage facility access based on membership rules with Gymex.",
        "Gym Biometric Software, Gym Access Control Software, Gym Attendance Software, Biometric Attendance System, RFID Gym Access, QR Code Check-in"
    )
    return h + NAV + '''
<style>
.ba-h1{font-family:'Poppins',sans-serif!important;font-size:36px!important;font-weight:800!important;line-height:1.25!important;margin:0 0 16px!important;color:#fff!important;}
.ba-p{font-family:'Poppins',sans-serif!important;font-size:16px!important;line-height:1.75!important;margin:0 0 24px!important;color:rgba(255,255,255,.85)!important;}
.ba-btn{display:inline-block!important;background:#f26522!important;color:#fff!important;padding:14px 32px!important;border-radius:50px!important;font-size:14px!important;font-weight:700!important;text-decoration:none!important;letter-spacing:.5px!important;transition:all .3s!important;}
.ba-btn:hover{background:#e05a1a!important;transform:translateY(-2px)!important;box-shadow:0 8px 24px rgba(242,101,34,.3)!important;}
.ba-sec{font-family:'Poppins',sans-serif!important;padding:70px 24px!important;}
.ba-wrap{max-width:1100px!important;margin:0 auto!important;}
.ba-h2{font-size:28px!important;font-weight:700!important;color:#0b1a3d!important;margin:0 0 16px!important;line-height:1.3!important;}
.ba-sub{font-size:16px!important;color:#555!important;line-height:1.7!important;margin:0 0 12px!important;}
.ba-grid{display:grid!important;grid-template-columns:repeat(auto-fit,minmax(240px,1fr))!important;gap:24px!important;margin:32px 0!important;}
.ba-card{background:#fff!important;border-radius:16px!important;padding:28px!important;border:1px solid #e8edf3!important;text-align:center!important;transition:transform .3s,box-shadow .3s!important;}
.ba-card:hover{transform:translateY(-4px)!important;box-shadow:0 12px 32px rgba(0,0,0,.08)!important;}
.ba-icon{width:60px!important;height:60px!important;border-radius:16px!important;display:flex!important;align-items:center!important;justify-content:center!important;font-size:26px!important;color:#fff!important;margin:0 auto 16px!important;}
.ba-card h3{font-size:17px!important;font-weight:700!important;color:#0b1a3d!important;margin:0 0 8px!important;}
.ba-card p{font-size:14px!important;color:#666!important;line-height:1.65!important;margin:0!important;}
.ba-split{display:grid!important;grid-template-columns:1fr 1fr!important;gap:48px!important;align-items:center!important;margin:32px 0!important;}
.ba-mini{display:flex!important;gap:12px!important;align-items:flex-start!important;margin-bottom:18px!important;}
.ba-mini-icon{width:42px!important;height:42px!important;min-width:42px!important;border-radius:10px!important;display:flex!important;align-items:center!important;justify-content:center!important;font-size:18px!important;color:#fff!important;}
.ba-mini h4{font-size:15px!important;font-weight:700!important;color:#0b1a3d!important;margin:0 0 4px!important;}
.ba-mini p{font-size:13px!important;color:#666!important;line-height:1.6!important;margin:0!important;}
.ba-cta{background:linear-gradient(135deg,#0b1a3d 0%,#1a3a5c 100%)!important;text-align:center!important;padding:60px 24px!important;}
.ba-cta h2{color:#fff!important;font-size:30px!important;font-weight:700!important;margin:0 0 14px!important;}
.ba-cta p{color:rgba(255,255,255,.8)!important;font-size:16px!important;margin:0 0 28px!important;line-height:1.7!important;}
.ba-faq{border:1px solid #e8edf3!important;border-radius:12px!important;margin-bottom:12px!important;overflow:hidden!important;}
.ba-faq-q{padding:18px 24px!important;cursor:pointer!important;font-weight:600!important;font-size:15px!important;color:#0b1a3d!important;background:#f8fafc!important;display:flex!important;justify-content:space-between!important;align-items:center!important;}
.ba-faq-q i{transition:transform .3s!important;}
.ba-faq-a{padding:0 24px 18px!important;font-size:14px!important;color:#666!important;line-height:1.75!important;display:none!important;}
.ba-faq.open .ba-faq-a{display:block!important;}
.ba-faq.open .ba-faq-q i{transform:rotate(180deg)!important;}
</style>

<section style="background:linear-gradient(135deg,#0d2847 0%,#0b1a3d 40%,#162d50 100%)!important;padding:90px 24px 70px!important;position:relative!important;overflow:hidden!important;">
  <div style="position:absolute!important;top:10%!important;left:-8%!important;width:450px!important;height:450px!important;border-radius:50%!important;background:radial-gradient(circle,rgba(49,170,225,.1) 0%,transparent 70%)!important;"></div>
  <div style="position:absolute!important;bottom:-20%!important;right:-5%!important;width:350px!important;height:350px!important;border-radius:50%!important;background:radial-gradient(circle,rgba(242,101,34,.08) 0%,transparent 70%)!important;"></div>
  <div class="ba-wrap" style="position:relative!important;z-index:1!important;">
    <span style="display:inline-block!important;background:rgba(49,170,225,.15)!important;color:#31AAE1!important;font-size:12px!important;font-weight:700!important;letter-spacing:2px!important;padding:6px 20px!important;border-radius:30px!important;margin-bottom:20px!important;font-family:'Poppins',sans-serif!important;">BIOMETRIC & ACCESS CONTROL</span>
    <h1 class="ba-h1">Simplify Gym Check-Ins<br>& Control Member Access</h1>
    <p class="ba-p" style="max-width:600px!important;">Track staff and member attendance with biometric, RFID, QR code, and manual check-ins. Manage facility access based on membership rules — all from one connected platform.</p>
    <a class="ba-btn" href="#">Get Your Free Demo <i class="fa fa-arrow-up" style="margin-left:8px!important;"></i></a>
  </div>
</section>

<section class="ba-sec" style="background:#f8fafc!important;">
  <div class="ba-wrap">
    <h2 class="ba-h2" style="text-align:center!important;">Track Attendance with Biometric & RFID</h2>
    <p class="ba-sub" style="text-align:center!important;max-width:700px;margin:0 auto 24px!important;">Manual attendance can slow down check-ins and make member visit records harder to maintain. Gymex Gym Biometric Attendance Software allows you to capture staff and member attendance through biometric and RFID integration.</p>
    <div style="text-align:center!important;margin-bottom:32px!important;">
      <span style="font-size:15px!important;font-weight:600!important;color:#0b1a3d!important;">Member Arrives &#10132; Verify &#10132; Check-In &#10132; Recorded</span>
    </div>
    <div class="ba-grid" style="grid-template-columns:repeat(3,1fr)!important;">
      <div class="ba-card">
        <div class="ba-icon" style="background:linear-gradient(135deg,#0b1a3d,#1a3a5c)!important;"><i class="fa fa-fingerprint"></i></div>
        <h3>Biometric Scan</h3>
        <p>Fingerprint or facial recognition for secure, unique member identification at check-in.</p>
      </div>
      <div class="ba-card">
        <div class="ba-icon" style="background:linear-gradient(135deg,#028ECE,#0270b0)!important;"><i class="fa fa-credit-card"></i></div>
        <h3>RFID Tap</h3>
        <p>Allow members to check in by tapping their RFID card or band on the reader device.</p>
      </div>
      <div class="ba-card">
        <div class="ba-icon" style="background:linear-gradient(135deg,#34A853,#2d8f47)!important;"><i class="fa fa-check-circle"></i></div>
        <h3>Instant Check-In</h3>
        <p>Fast, frictionless check-in process that takes seconds and updates attendance instantly.</p>
      </div>
    </div>
  </div>
</section>

<section class="ba-sec" style="background:#fff!important;">
  <div class="ba-wrap">
    <h2 class="ba-h2" style="text-align:center!important;">Multiple Ways to Check In</h2>
    <p class="ba-sub" style="text-align:center!important;max-width:700px;margin:0 auto 32px!important;">Not every member needs to check in through a biometric device. Gymex supports multiple check-in options for a smoother attendance experience.</p>
    <div class="ba-grid" style="grid-template-columns:repeat(4,1fr)!important;">
      <div class="ba-card">
        <div class="ba-icon" style="background:#0b1a3d!important;"><i class="fa fa-fingerprint"></i></div>
        <h3>Biometric</h3>
        <p>Capture attendance through biometric integration for secure, fast check-ins.</p>
      </div>
      <div class="ba-card">
        <div class="ba-icon" style="background:#028ECE!important;"><i class="fa fa-credit-card"></i></div>
        <h3>RFID</h3>
        <p>Allow members and staff to check in using RFID cards or bands.</p>
      </div>
      <div class="ba-card">
        <div class="ba-icon" style="background:#34A853!important;"><i class="fa fa-qrcode"></i></div>
        <h3>QR Code</h3>
        <p>Members scan a QR code from the app to mark attendance quickly.</p>
      </div>
      <div class="ba-card">
        <div class="ba-icon" style="background:#f26522!important;"><i class="fa fa-hand-pointer-o"></i></div>
        <h3>Manual</h3>
        <p>Staff can manually mark attendance from the admin panel or staff app.</p>
      </div>
    </div>
  </div>
</section>

<section class="ba-sec" style="background:#f8fafc!important;">
  <div class="ba-wrap">
    <div class="ba-split">
      <div>
        <h2 class="ba-h2">Control Who Enters and When</h2>
        <p class="ba-sub">Set access rules based on membership type, time slots, and branch. Only active members with valid access can enter — expired memberships are blocked automatically.</p>
        <div class="ba-mini">
          <div class="ba-mini-icon" style="background:#0b1a3d!important;"><i class="fa fa-shield"></i></div>
          <div><h4>Membership-Based Access</h4><p>Members can only check in when their membership is active and valid.</p></div>
        </div>
        <div class="ba-mini">
          <div class="ba-mini-icon" style="background:#028ECE!important;"><i class="fa fa-clock-o"></i></div>
          <div><h4>Time-Based Access</h4><p>Restrict entry to specific hours — like ladies-only or peak/off-peak slots.</p></div>
        </div>
        <div class="ba-mini">
          <div class="ba-mini-icon" style="background:#34A853!important;"><i class="fa fa-map-marker"></i></div>
          <div><h4>Branch-Based Access</h4><p>Control which branches a member can access based on their membership plan.</p></div>
        </div>
        <div class="ba-mini">
          <div class="ba-mini-icon" style="background:#f26522!important;"><i class="fa fa-ban"></i></div>
          <div><h4>Auto-Block Expired</h4><p>Members with expired memberships are automatically denied entry.</p></div>
        </div>
      </div>
      <div style="background:linear-gradient(135deg,#0b1a3d,#1a3a5c)!important;border-radius:20px!important;padding:40px!important;color:#fff!important;text-align:center!important;">
        <i class="fa fa-shield" style="font-size:48px!important;color:#31AAE1!important;margin-bottom:20px!important;display:block!important;"></i>
        <h3 style="font-size:22px!important;margin:0 0 12px!important;">Smart Access Rules</h3>
        <p style="font-size:14px!important;color:rgba(255,255,255,.8)!important;line-height:1.7!important;">Set granular access rules for every membership type, time slot, and branch.</p>
      </div>
    </div>
  </div>
</section>

<section class="ba-sec" style="background:#fff!important;">
  <div class="ba-wrap">
    <h2 class="ba-h2" style="text-align:center!important;">Multi-Floor & Multi-Branch Access Control</h2>
    <p class="ba-sub" style="text-align:center!important;max-width:700px;margin:0 auto 32px!important;">Manage access across multiple floors and branches from a single dashboard. Restrict gym floor access based on membership tier.</p>
    <div class="ba-grid" style="grid-template-columns:repeat(3,1fr)!important;">
      <div class="ba-card">
        <div class="ba-icon" style="background:#0b1a3d!important;"><i class="fa fa-building"></i></div>
        <h3>Multi-Branch Control</h3>
        <p>Manage access permissions across all your gym locations from one central dashboard.</p>
      </div>
      <div class="ba-card">
        <div class="ba-icon" style="background:#028ECE!important;"><i class="fa fa-th-large"></i></div>
        <h3>Floor-Level Access</h3>
        <p>Restrict access to specific floors or zones based on membership type and tier.</p>
      </div>
      <div class="ba-card">
        <div class="ba-icon" style="background:#34A853!important;"><i class="fa fa-line-chart"></i></div>
        <h3>Real-Time Reports</h3>
        <p>View live check-in data, peak hours, and occupancy levels across all branches.</p>
      </div>
    </div>
  </div>
</section>

<section class="ba-cta">
  <div class="ba-wrap">
    <h2>Take Control of Your Gym Access Today</h2>
    <p>Replace manual registers and key-based entry with smart biometric and access control — track every check-in and secure every entry.</p>
    <a class="ba-btn" href="#">Get Your Free Demo</a>
  </div>
</section>

<section class="ba-sec" style="background:#fff!important;">
  <div class="ba-wrap">
    <h2 class="ba-h2" style="text-align:center!important;">Frequently Asked Questions</h2>
    <div class="ba-faq" onclick="this.classList.toggle('open')">
      <div class="ba-faq-q">What check-in methods does Gymex support? <i class="fa fa-chevron-down"></i></div>
      <div class="ba-faq-a">Gymex supports biometric (fingerprint/facial), RFID cards/bands, QR code scanning, and manual check-in through the admin or staff app.</div>
    </div>
    <div class="ba-faq" onclick="this.classList.toggle('open')">
      <div class="ba-faq-q">Can I block expired members from entering? <i class="fa fa-chevron-down"></i></div>
      <div class="ba-faq-a">Yes. Gymex automatically denies entry to members with expired memberships based on your access control rules.</div>
    </div>
    <div class="ba-faq" onclick="this.classList.toggle('open')">
      <div class="ba-faq-q">Is multi-branch access control supported? <i class="fa fa-chevron-down"></i></div>
      <div class="ba-faq-a">Yes. You can manage access permissions across multiple branches from a single dashboard, controlling which locations each member can access.</div>
    </div>
    <div class="ba-faq" onclick="this.classList.toggle('open')">
      <div class="ba-faq-q">Can I restrict entry by time slots? <i class="fa fa-chevron-down"></i></div>
      <div class="ba-faq-a">Yes. You can set time-based access rules — for example, ladies-only hours, peak/off-peak slots, or specific booking windows.</div>
    </div>
    <div class="ba-faq" onclick="this.classList.toggle('open')">
      <div class="ba-faq-q">Does Gymex provide real-time check-in reports? <i class="fa fa-chevron-down"></i></div>
      <div class="ba-faq-a">Yes. View live check-in data, daily attendance, peak hours, and occupancy levels from the dashboard in real time.</div>
    </div>
  </div>
</section>

''' + FOOTER + '''
<script src="../javascript.js"></script>
</body>
</html>'''


# ══════════════════════════════════════════════════════════════
# PAGE 3: DATA ANALYSIS & DASHBOARD
# ══════════════════════════════════════════════════════════════
def build_data_analysis():
    h = head(
        "Gym Data Analysis & Dashboard Software | Gymex",
        "Track gym performance with real-time dashboards, revenue reports, member analytics, and staff insights. Gymex helps you make data-driven decisions.",
        "Gym Data Analysis Software, Gym Dashboard Software, Gym Analytics, Gym Revenue Reports, Gym Performance Tracking, Gym Business Intelligence"
    )
    return h + NAV + '''
<style>
.da-h1{font-family:'Poppins',sans-serif!important;font-size:36px!important;font-weight:800!important;line-height:1.25!important;margin:0 0 16px!important;color:#fff!important;}
.da-p{font-family:'Poppins',sans-serif!important;font-size:16px!important;line-height:1.75!important;margin:0 0 24px!important;color:rgba(255,255,255,.85)!important;}
.da-btn{display:inline-block!important;background:#f26522!important;color:#fff!important;padding:14px 32px!important;border-radius:50px!important;font-size:14px!important;font-weight:700!important;text-decoration:none!important;letter-spacing:.5px!important;transition:all .3s!important;}
.da-btn:hover{background:#e05a1a!important;transform:translateY(-2px)!important;box-shadow:0 8px 24px rgba(242,101,34,.3)!important;}
.da-sec{font-family:'Poppins',sans-serif!important;padding:70px 24px!important;}
.da-wrap{max-width:1100px!important;margin:0 auto!important;}
.da-h2{font-size:28px!important;font-weight:700!important;color:#0b1a3d!important;margin:0 0 16px!important;line-height:1.3!important;}
.da-sub{font-size:16px!important;color:#555!important;line-height:1.7!important;margin:0 0 12px!important;}
.da-grid{display:grid!important;grid-template-columns:repeat(auto-fit,minmax(240px,1fr))!important;gap:24px!important;margin:32px 0!important;}
.da-card{background:#fff!important;border-radius:16px!important;padding:28px!important;border:1px solid #e8edf3!important;transition:transform .3s,box-shadow .3s!important;}
.da-card:hover{transform:translateY(-4px)!important;box-shadow:0 12px 32px rgba(0,0,0,.08)!important;}
.da-icon{width:52px!important;height:52px!important;border-radius:14px!important;display:flex!important;align-items:center!important;justify-content:center!important;font-size:22px!important;color:#fff!important;margin-bottom:18px!important;}
.da-card h3{font-size:17px!important;font-weight:700!important;color:#0b1a3d!important;margin:0 0 10px!important;}
.da-card p{font-size:14px!important;color:#666!important;line-height:1.65!important;margin:0!important;}
.da-stats{display:grid!important;grid-template-columns:repeat(4,1fr)!important;gap:20px!important;margin:32px 0!important;}
.da-stat{background:#fff!important;border-radius:14px!important;padding:24px!important;text-align:center!important;border:1px solid #e8edf3!important;}
.da-stat-num{font-size:28px!important;font-weight:800!important;color:#0b1a3d!important;margin-bottom:4px!important;}
.da-stat-label{font-size:13px!important;color:#888!important;font-weight:500!important;}
.da-cta{background:linear-gradient(135deg,#0b1a3d 0%,#1a3a5c 100%)!important;text-align:center!important;padding:60px 24px!important;}
.da-cta h2{color:#fff!important;font-size:30px!important;font-weight:700!important;margin:0 0 14px!important;}
.da-cta p{color:rgba(255,255,255,.8)!important;font-size:16px!important;margin:0 0 28px!important;line-height:1.7!important;}
.da-faq{border:1px solid #e8edf3!important;border-radius:12px!important;margin-bottom:12px!important;overflow:hidden!important;}
.da-faq-q{padding:18px 24px!important;cursor:pointer!important;font-weight:600!important;font-size:15px!important;color:#0b1a3d!important;background:#f8fafc!important;display:flex!important;justify-content:space-between!important;align-items:center!important;}
.da-faq-q i{transition:transform .3s!important;}
.da-faq-a{padding:0 24px 18px!important;font-size:14px!important;color:#666!important;line-height:1.75!important;display:none!important;}
.da-faq.open .da-faq-a{display:block!important;}
.da-faq.open .da-faq-q i{transform:rotate(180deg)!important;}
.da-split{display:grid!important;grid-template-columns:1fr 1fr!important;gap:48px!important;align-items:center!important;margin:32px 0!important;}
.da-mini{display:flex!important;gap:12px!important;align-items:flex-start!important;margin-bottom:18px!important;}
.da-mini-icon{width:42px!important;height:42px!important;min-width:42px!important;border-radius:10px!important;display:flex!important;align-items:center!important;justify-content:center!important;font-size:18px!important;color:#fff!important;}
.da-mini h4{font-size:15px!important;font-weight:700!important;color:#0b1a3d!important;margin:0 0 4px!important;}
.da-mini p{font-size:13px!important;color:#666!important;line-height:1.6!important;margin:0!important;}
</style>

<section style="background:linear-gradient(135deg,#0f3460 0%,#0b1a3d 50%,#1a1a2e 100%)!important;padding:90px 24px 70px!important;position:relative!important;overflow:hidden!important;">
  <div style="position:absolute!important;top:-30%!important;left:10%!important;width:500px!important;height:500px!important;border-radius:50%!important;background:radial-gradient(circle,rgba(52,168,83,.1) 0%,transparent 70%)!important;"></div>
  <div style="position:absolute!important;bottom:-25%!important;right:-10%!important;width:400px!important;height:400px!important;border-radius:50%!important;background:radial-gradient(circle,rgba(242,101,34,.08) 0%,transparent 70%)!important;"></div>
  <div class="da-wrap" style="position:relative!important;z-index:1!important;">
    <span style="display:inline-block!important;background:rgba(52,168,83,.15)!important;color:#34A853!important;font-size:12px!important;font-weight:700!important;letter-spacing:2px!important;padding:6px 20px!important;border-radius:30px!important;margin-bottom:20px!important;font-family:'Poppins',sans-serif!important;">DATA ANALYSIS & DASHBOARD</span>
    <h1 class="da-h1">Understand Your Gym<br>Performance with Real-Time<br>Data & Insights</h1>
    <p class="da-p" style="max-width:600px!important;">Track revenue, membership trends, staff performance, and member engagement through interactive dashboards and detailed reports — all in one place.</p>
    <a class="da-btn" href="#">Get Your Free Demo <i class="fa fa-arrow-up" style="margin-left:8px!important;"></i></a>
  </div>
</section>

<section class="da-sec" style="background:#f8fafc!important;">
  <div class="da-wrap">
    <h2 class="da-h2" style="text-align:center!important;">Key Metrics at Your Fingertips</h2>
    <p class="da-sub" style="text-align:center!important;max-width:700px;margin:0 auto 24px!important;">Gymex dashboard gives you a real-time snapshot of your gym's most important performance metrics.</p>
    <div class="da-stats">
      <div class="da-stat"><div class="da-stat-num" style="color:#0b1a3d!important;">&#8377;12.5L</div><div class="da-stat-label">Monthly Revenue</div></div>
      <div class="da-stat"><div class="da-stat-num" style="color:#34A853!important;">847</div><div class="da-stat-label">Active Members</div></div>
      <div class="da-stat"><div class="da-stat-num" style="color:#028ECE!important;">73%</div><div class="da-stat-label">Retention Rate</div></div>
      <div class="da-stat"><div class="da-stat-num" style="color:#f26522!important;">92%</div><div class="da-stat-label">Attendance Rate</div></div>
    </div>
  </div>
</section>

<section class="da-sec" style="background:#fff!important;">
  <div class="da-wrap">
    <div class="da-split">
      <div>
        <h2 class="da-h2">Revenue Reports That Drive Smarter Decisions</h2>
        <p class="da-sub">See exactly where your revenue is coming from — new memberships, renewals, personal training, POS sales, and more.</p>
        <div class="da-mini">
          <div class="da-mini-icon" style="background:#0b1a3d!important;"><i class="fa fa-line-chart"></i></div>
          <div><h4>Revenue Breakdown</h4><p>Track income by category — membership, PT, products, and services.</p></div>
        </div>
        <div class="da-mini">
          <div class="da-mini-icon" style="background:#34A853!important;"><i class="fa fa-calendar"></i></div>
          <div><h4>Daily / Weekly / Monthly</h4><p>View revenue trends over any time period with interactive charts.</p></div>
        </div>
        <div class="da-mini">
          <div class="da-mini-icon" style="background:#028ECE!important;"><i class="fa fa-building"></i></div>
          <div><h4>Branch-Wise Reports</h4><p>Compare revenue and performance across multiple branches.</p></div>
        </div>
      </div>
      <div style="background:linear-gradient(135deg,#0b1a3d,#1a3a5c)!important;border-radius:20px!important;padding:40px!important;color:#fff!important;">
        <div style="display:grid!important;grid-template-columns:1fr 1fr!important;gap:16px!important;">
          <div style="background:rgba(255,255,255,.1)!important;padding:20px!important;border-radius:12px!important;text-align:center!important;"><div style="font-size:24px!important;font-weight:800!important;color:#34A853!important;">&#8377;4.2L</div><div style="font-size:12px!important;color:rgba(255,255,255,.7)!important;margin-top:4px!important;">New Memberships</div></div>
          <div style="background:rgba(255,255,255,.1)!important;padding:20px!important;border-radius:12px!important;text-align:center!important;"><div style="font-size:24px!important;font-weight:800!important;color:#31AAE1!important;">&#8377;5.8L</div><div style="font-size:12px!important;color:rgba(255,255,255,.7)!important;margin-top:4px!important;">Renewals</div></div>
          <div style="background:rgba(255,255,255,.1)!important;padding:20px!important;border-radius:12px!important;text-align:center!important;"><div style="font-size:24px!important;font-weight:800!important;color:#f26522!important;">&#8377;1.5L</div><div style="font-size:12px!important;color:rgba(255,255,255,.7)!important;margin-top:4px!important;">PT Revenue</div></div>
          <div style="background:rgba(255,255,255,.1)!important;padding:20px!important;border-radius:12px!important;text-align:center!important;"><div style="font-size:24px!important;font-weight:800!important;color:#FF9800!important;">&#8377;1.0L</div><div style="font-size:12px!important;color:rgba(255,255,255,.7)!important;margin-top:4px!important;">POS & Products</div></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="da-sec" style="background:#f8fafc!important;">
  <div class="da-wrap">
    <h2 class="da-h2" style="text-align:center!important;">Analytics That Help You Grow</h2>
    <p class="da-sub" style="text-align:center!important;max-width:700px;margin:0 auto 32px!important;">Go beyond numbers — understand member behavior, staff performance, and business trends with detailed analytics.</p>
    <div class="da-grid">
      <div class="da-card">
        <div class="da-icon" style="background:linear-gradient(135deg,#0b1a3d,#1a3a5c)!important;"><i class="fa fa-users"></i></div>
        <h3>Member Analytics</h3>
        <p>Track new joins, cancellations, retention rates, demographics, and membership trends over time.</p>
      </div>
      <div class="da-card">
        <div class="da-icon" style="background:linear-gradient(135deg,#34A853,#2d8f47)!important;"><i class="fa fa-money"></i></div>
        <h3>Revenue Analytics</h3>
        <p>See income breakdowns by category, payment method, branch, and time period.</p>
      </div>
      <div class="da-card">
        <div class="da-icon" style="background:linear-gradient(135deg,#028ECE,#0270b0)!important;"><i class="fa fa-user"></i></div>
        <h3>Staff Performance</h3>
        <p>Measure trainer productivity, attendance, client satisfaction, and revenue contribution.</p>
      </div>
      <div class="da-card">
        <div class="da-icon" style="background:linear-gradient(135deg,#f26522,#e05a1a)!important;"><i class="fa fa-bullseye"></i></div>
        <h3>Attendance Insights</h3>
        <p>Identify peak hours, low-attendance days, and member visit patterns for better scheduling.</p>
      </div>
    </div>
  </div>
</section>

<section class="da-sec" style="background:#fff!important;">
  <div class="da-wrap">
    <h2 class="da-h2" style="text-align:center!important;">Reports You Can Export and Share</h2>
    <p class="da-sub" style="text-align:center!important;max-width:700px;margin:0 auto 32px!important;">Generate detailed reports and export them as PDF or Excel for meetings, accounting, and business planning.</p>
    <div class="da-grid" style="grid-template-columns:repeat(3,1fr)!important;">
      <div class="da-card">
        <div class="da-icon" style="background:#0b1a3d!important;"><i class="fa fa-file-pdf-o"></i></div>
        <h3>Revenue Reports</h3>
        <p>Detailed income reports by membership type, payment method, and time period.</p>
      </div>
      <div class="da-card">
        <div class="da-icon" style="background:#028ECE!important;"><i class="fa fa-table"></i></div>
        <h3>Member Reports</h3>
        <p>Membership status, renewal tracking, inactive member lists, and demographic breakdowns.</p>
      </div>
      <div class="da-card">
        <div class="da-icon" style="background:#34A853!important;"><i class="fa fa-bar-chart"></i></div>
        <h3>Attendance Reports</h3>
        <p>Daily, weekly, and monthly attendance summaries with peak hour analysis.</p>
      </div>
    </div>
  </div>
</section>

<section class="da-cta">
  <div class="da-wrap">
    <h2>Make Data-Driven Decisions for Your Gym</h2>
    <p>Stop guessing and start knowing. Gymex dashboards and reports give you the insights you need to grow your fitness business.</p>
    <a class="da-btn" href="#">Get Your Free Demo</a>
  </div>
</section>

<section class="da-sec" style="background:#fff!important;">
  <div class="da-wrap">
    <h2 class="da-h2" style="text-align:center!important;">Frequently Asked Questions</h2>
    <div class="da-faq" onclick="this.classList.toggle('open')">
      <div class="da-faq-q">What data can I see on the Gymex dashboard? <i class="fa fa-chevron-down"></i></div>
      <div class="da-faq-a">The Gymex dashboard shows real-time metrics including total revenue, active members, attendance rate, retention rate, upcoming expirations, and daily check-ins.</div>
    </div>
    <div class="da-faq" onclick="this.classList.toggle('open')">
      <div class="da-faq-q">Can I export reports? <i class="fa fa-chevron-down"></i></div>
      <div class="da-faq-a">Yes. Gymex allows you to export revenue, member, and attendance reports in PDF and Excel formats for sharing with your team or accountant.</div>
    </div>
    <div class="da-faq" onclick="this.classList.toggle('open')">
      <div class="da-faq-q">Does it support multi-branch analytics? <i class="fa fa-chevron-down"></i></div>
      <div class="da-faq-a">Yes. You can view branch-wise reports, compare performance across locations, and see consolidated data for all branches.</div>
    </div>
    <div class="da-faq" onclick="this.classList.toggle('open')">
      <div class="da-faq-q">Can I track staff performance? <i class="fa fa-chevron-down"></i></div>
      <div class="da-faq-a">Yes. Gymex tracks trainer productivity, client retention, attendance, and revenue contribution for each staff member.</div>
    </div>
    <div class="da-faq" onclick="this.classList.toggle('open')">
      <div class="da-faq-q">Are the reports updated in real time? <i class="fa fa-chevron-down"></i></div>
      <div class="da-faq-a">Yes. All dashboard metrics and reports update in real time as transactions, check-ins, and membership changes occur.</div>
    </div>
  </div>
</section>

''' + FOOTER + '''
<script src="../javascript.js"></script>
</body>
</html>'''


# ══════════════════════════════════════════════════════════════
# BUILD ALL 3 PAGES
# ══════════════════════════════════════════════════════════════
pages = {
    'intelligent-alerts/intelligent-alerts-reminders.html': build_intelligent_alerts(),
    'biometric-access-control/biometric-access-control.html': build_biometric(),
    'data-analysis-dashboard/data-analysis-dashboard.html': build_data_analysis(),
}

for path, html in pages.items():
    full = os.path.join('.', path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"OK Written: {path} ({len(html)} bytes)")

print("\nAll 3 pages built successfully!")
