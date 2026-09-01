import re

with open('task-management/nav.txt', 'r', encoding='utf-8') as f:
    nav = f.read()
with open('task-management/footer.txt', 'r', encoding='utf-8') as f:
    footer = f.read()

html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Gym Payroll Software &amp; Trainer Commission Management | Gymex</title>
<meta name="description" content="Simplify gym staff payroll, salaries, and trainer commissions with Gymex. Automate calculations, track payouts, and manage payroll from one connected platform.">
<meta name="keywords" content="Gym Payroll Software, Gym Payroll Management Software, Trainer Commission Software, Gym Commission Management Software, Gym Salary Management Software">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="icon" type="image/x-icon" href="../assets/gymex-favicon-U7mChGv0.ico">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<link rel="stylesheet" href="../style.css">
<link rel="stylesheet" href="payroll-commission.css">
<script src="../javascript.js"></script>
</head>
<body>

''' + nav + '''

<!-- HERO -->
<section class="pm-hero">
<div class="pm-hero-inner">
<div>
<p class="pm-hero-label"><i class="fa fa-inr"></i> GYM PAYROLL SOFTWARE</p>
<h1>Simplify Payroll &amp; <span>Trainer Commissions</span></h1>
<p>Simplify staff salaries, trainer commissions, and payroll management with Gymex. Automate calculations, organize payroll records, and manage staff payouts from one connected platform.</p>
<a class="pm-hero-btn" href="#">Get Your Free Demo <i class="fa fa-arrow-up"></i></a>
</div>
<div class="pm-hero-visual">
<div class="pm-float"><div class="pm-fi green"><i class="fa fa-inr"></i></div><div class="pm-ft"><h5>Salary Processed</h5><p>Rahul - &#8377;45,000</p></div></div>
<div class="pm-float"><div class="pm-fi blue"><i class="fa fa-percent"></i></div><div class="pm-ft"><h5>Commission Calculated</h5><p>Priya - 12% of sales</p></div></div>
<div class="pm-float"><div class="pm-fi orange"><i class="fa fa-check-circle"></i></div><div class="pm-ft"><h5>Payout Completed</h5><p>March payroll done</p></div></div>
<div class="pm-float"><div class="pm-fi purple"><i class="fa fa-users"></i></div><div class="pm-ft"><h5>18 Staff Paid</h5><p>All clearances done</p></div></div>
</div>
</div>
</section>

<!-- SALARY CARDS -->
<section class="pm-salary">
<div class="pm-wrap">
<h2 class="pm-salary-title">Manage Different Salary Structures</h2>
<p class="pm-salary-sub">Not every team member is compensated the same way. Gymex helps you organize different payroll and commission structures.</p>
<div class="pm-salary-grid">
<div class="pm-salary-card">
<div class="pm-sc-head"><div class="pm-sc-icon green"><i class="fa fa-briefcase"></i></div><div><h4>Gym Managers</h4><p>Fixed salary + bonus</p></div></div>
<div class="pm-sc-body">Manage fixed salaries, performance bonuses, and other compensation details for your management team.</div>
</div>
<div class="pm-salary-card">
<div class="pm-sc-head"><div class="pm-sc-icon blue"><i class="fa fa-desktop"></i></div><div><h4>Front Desk &amp; Sales</h4><p>Fixed + incentives</p></div></div>
<div class="pm-sc-body">Track base salary along with sales incentives, lead conversion bonuses, and membership targets.</div>
</div>
<div class="pm-salary-card">
<div class="pm-sc-head"><div class="pm-sc-icon orange"><i class="fa fa-heartbeat"></i></div><div><h4>Trainers &amp; Instructors</h4><p>Base + commission</p></div></div>
<div class="pm-sc-body">Organize commission structures based on sessions, personal training clients, or revenue targets.</div>
</div>
</div>
</div>
</section>

<!-- WORKFLOW -->
<section class="pm-workflow">
<div class="pm-wrap">
<h2 class="pm-workflow-title">From Staff Activity to Payroll in One Workflow</h2>
<p class="pm-workflow-sub">A connected approach that turns scattered payroll tasks into a structured, repeatable process.</p>
<div class="pm-wf-track">
<div class="pm-wf-step"><div class="pm-wf-num">1</div><h5>Set Up</h5><p>Maintain staff salary and commission info.</p></div>
<div class="pm-wf-line"></div>
<div class="pm-wf-step"><div class="pm-wf-num">2</div><h5>Track</h5><p>Keep attendance and compensation records.</p></div>
<div class="pm-wf-line"></div>
<div class="pm-wf-step"><div class="pm-wf-num">3</div><h5>Calculate</h5><p>Simplify salary and commission math.</p></div>
<div class="pm-wf-line"></div>
<div class="pm-wf-step"><div class="pm-wf-num">4</div><h5>Review</h5><p>Check payroll before finalizing.</p></div>
<div class="pm-wf-line"></div>
<div class="pm-wf-step"><div class="pm-wf-num">5</div><h5>Maintain</h5><p>Keep records for future reference.</p></div>
</div>
</div>
</section>

<!-- BEFORE/AFTER -->
<section class="pm-compare">
<div class="pm-wrap">
<h2 class="pm-compare-title">Stop Relying on Spreadsheets</h2>
<div class="pm-compare-grid">
<div class="pm-compare-box before">
<h4><i class="fa fa-times-circle"></i> Without Gymex</h4>
<ul>
<li>Calculating salaries manually every month</li>
<li>Tracking trainer commissions in spreadsheets</li>
<li>Re-entering staff information for payroll</li>
<li>Checking multiple systems for records</li>
<li>Missing commission deadlines</li>
<li>No real-time visibility into payouts</li>
</ul>
</div>
<div class="pm-compare-box after">
<h4><i class="fa fa-check-circle"></i> With Gymex</h4>
<ul>
<li>Automated salary calculations</li>
<li>Commission tracking in one system</li>
<li>Staff info connected with payroll</li>
<li>All records in one platform</li>
<li>Automatic deadline reminders</li>
<li>Real-time payroll visibility</li>
</ul>
</div>
</div>
</div>
</section>

<!-- FEATURES -->
<section class="pm-features">
<div class="pm-wrap">
<h2 class="pm-features-title">Everything You Need for Payroll</h2>
<p class="pm-features-sub">From salary management to commission tracking, Gymex gives you the tools to handle payroll efficiently.</p>
<div class="pm-feat-grid">
<div class="pm-feat g"><div class="pm-feat-icon"><i class="fa fa-inr"></i></div><h4>Manage Salaries</h4><p>Maintain staff salary and compensation details in one place.</p></div>
<div class="pm-feat b"><div class="pm-feat-icon"><i class="fa fa-calculator"></i></div><h4>Auto Calculations</h4><p>Reduce manual payroll math with automated calculations.</p></div>
<div class="pm-feat o"><div class="pm-feat-icon"><i class="fa fa-percent"></i></div><h4>Trainer Commissions</h4><p>Organize commission structures and track trainer earnings.</p></div>
<div class="pm-feat p"><div class="pm-feat-icon"><i class="fa fa-clock-o"></i></div><h4>Attendance Link</h4><p>Connect attendance records with payroll calculations.</p></div>
<div class="pm-feat g"><div class="pm-feat-icon"><i class="fa fa-users"></i></div><h4>Staff Connected</h4><p>Keep payroll linked with your staff management records.</p></div>
<div class="pm-feat b"><div class="pm-feat-icon"><i class="fa fa-file-text"></i></div><h4>Payroll Records</h4><p>Maintain organized payroll history for review.</p></div>
<div class="pm-feat o"><div class="pm-feat-icon"><i class="fa fa-eye"></i></div><h4>Full Visibility</h4><p>Review payroll and commission information anytime.</p></div>
<div class="pm-feat p"><div class="pm-feat-icon"><i class="fa fa-bar-chart"></i></div><h4>Reports</h4><p>Get insights into staff compensation costs.</p></div>
</div>
</div>
</section>

<!-- METRICS -->
<section class="pm-metrics">
<div class="pm-wrap">
<h2 class="pm-metrics-title">Payroll That Works for Your Business</h2>
<div class="pm-metrics-grid">
<div class="pm-metric"><div class="pm-metric-num c1">0</div><h5>Manual Errors</h5></div>
<div class="pm-metric"><div class="pm-metric-num c2">100%</div><h5>Transparency</h5></div>
<div class="pm-metric"><div class="pm-metric-num c3">5min</div><h5>Payroll Processing</h5></div>
<div class="pm-metric"><div class="pm-metric-num c4">24/7</div><h5>Access Records</h5></div>
</div>
</div>
</section>

<!-- CTA -->
<section class="pm-cta">
<div class="pm-wrap">
<h2>Make Gym Payroll Easier to Manage</h2>
<p>From staff salaries and payroll records to trainer commissions and compensation tracking, Gymex helps bring your payroll process together.</p>
<a class="pm-hero-btn" href="#" style="background:#fff;color:#27ae60;">Get Your Free Demo <i class="fa fa-arrow-up" style="color:#27ae60;"></i></a>
</div>
</section>

<!-- FAQ -->
<section class="pm-faq">
<div class="pm-wrap">
<h2 class="pm-faq-title">Frequently Asked Questions</h2>
<div class="pm-faq-grid">
<div class="pm-faq-item"><details><summary>What is gym payroll software?</summary><p>Gym payroll software helps fitness businesses organize and manage staff salaries, trainer commissions, compensation records, and other payroll-related information from a centralized system.</p></details></div>
<div class="pm-faq-item"><details><summary>Why do gyms need payroll management software?</summary><p>Gyms often have different types of employees with different compensation structures. Gym payroll management software helps organize these requirements and reduce dependence on manual spreadsheets.</p></details></div>
<div class="pm-faq-item"><details><summary>What is trainer commission software?</summary><p>Trainer commission software helps gyms calculate, organize, and track commission-related earnings for personal trainers and fitness instructors.</p></details></div>
<div class="pm-faq-item"><details><summary>Can Gymex manage personal trainer commissions?</summary><p>Yes. Gymex helps fitness businesses organize trainer commission information and connect it with wider payroll and staff management processes.</p></details></div>
<div class="pm-faq-item"><details><summary>Can payroll be connected with staff attendance?</summary><p>Yes. Attendance information can support payroll calculations where compensation depends on staff attendance, working patterns, or sessions.</p></details></div>
<div class="pm-faq-item"><details><summary>Can Gymex manage both salaries and commissions?</summary><p>Yes. Gymex is designed to help gyms organize both staff payroll and trainer commission-related information within the wider gym management platform.</p></details></div>
<div class="pm-faq-item"><details><summary>Can gym payroll software reduce manual calculations?</summary><p>Yes. Payroll automation can reduce repetitive calculations and manual data entry by keeping relevant staff and compensation information within a structured workflow.</p></details></div>
<div class="pm-faq-item"><details><summary>Is Gymex suitable for fitness staff payroll?</summary><p>Yes. Gymex connects payroll with other gym operations, making it suitable for fitness businesses that want to manage staff information, compensation, and commissions from a connected platform.</p></details></div>
</div>
</div>
</section>

</div>

''' + footer + '''

<script src="../javascript.js"></script>
</body>
</html>'''

with open('payroll-commission/payroll-commission.html', 'w', encoding='utf-8') as f:
    f.write(html)
print(f'Created: {len(html)} chars')
