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
<title>Gym Task Management Software | Assign &amp; Track Staff Tasks | Gymex</title>
<meta name="description" content="Assign, organize, and track gym staff tasks with Gymex. Set priorities, manage deadlines, monitor progress, and keep your team accountable from one platform.">
<meta name="keywords" content="Gym Task Management Software, Gym Task Management, Gym Staff Task Management Software, Task Management Software for Gyms, Gym Task Tracking Software">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="icon" type="image/x-icon" href="../assets/gymex-favicon-U7mChGv0.ico">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<link rel="stylesheet" href="../style.css">
<link rel="stylesheet" href="task-management.css">
<script src="../javascript.js"></script>
</head>
<body>

''' + nav + '''

<!-- HERO -->
<section class="tm-hero">
<div class="tm-hero-inner">
<div>
<p class="tm-hero-label"><i class="fa fa-bolt"></i> GYM TASK MANAGEMENT SOFTWARE</p>
<h1>Assign, Track &amp; <span>Manage Gym Tasks</span> with Ease</h1>
<p>Create and allocate tasks, set priorities and deadlines, track progress, and keep your team updated. Gymex helps you organize daily responsibilities and review staff performance.</p>
<a class="tm-hero-btn" href="#">Get Your Free Demo <i class="fa fa-arrow-up"></i></a>
</div>
<div class="tm-hero-visual">
<div class="tm-float-card"><div class="tm-fc-icon orange"><i class="fa fa-plus"></i></div><div class="tm-fc-text"><h5>New Task Created</h5><p>Follow up with lead</p></div></div>
<div class="tm-float-card"><div class="tm-fc-icon blue"><i class="fa fa-user"></i></div><div class="tm-fc-text"><h5>Assigned to Rahul</h5><p>Sales Team</p></div></div>
<div class="tm-float-card"><div class="tm-fc-icon green"><i class="fa fa-check"></i></div><div class="tm-fc-text"><h5>Task Completed</h5><p>Gym cleaned &amp; checked</p></div></div>
<div class="tm-float-card"><div class="tm-fc-icon purple"><i class="fa fa-flag"></i></div><div class="tm-fc-text"><h5>Priority: High</h5><p>Deadline today</p></div></div>
</div>
</div>
</section>

<!-- KANBAN BOARD -->
<section class="tm-kanban">
<div class="tm-wrap">
<h2 class="tm-kanban-title">Track Every Task from Start to Finish</h2>
<p class="tm-kanban-sub">See exactly where each task stands. From creation to completion, Gymex gives you full visibility into your team's workflow.</p>
<div class="tm-kanban-grid">
<div class="tm-kanban-col">
<div class="tm-kanban-header"><div class="tm-kanban-dot todo"></div><h4>To Do</h4><span>4</span></div>
<div class="tm-kanban-task"><h5>Update membership brochure</h5><p>Design team</p><span class="tm-kanban-tag med">Medium</span></div>
<div class="tm-kanban-task"><h5>Schedule equipment service</h5><p>Maintenance</p><span class="tm-kanban-tag high">High</span></div>
<div class="tm-kanban-task"><h5>Prepare monthly report</h5><p>Manager</p><span class="tm-kanban-tag low">Low</span></div>
</div>
<div class="tm-kanban-col">
<div class="tm-kanban-header"><div class="tm-kanban-dot progress"></div><h4>In Progress</h4><span>3</span></div>
<div class="tm-kanban-task"><h5>Follow up with 12 leads</h5><p>Sales Team</p><span class="tm-kanban-tag high">High</span></div>
<div class="tm-kanban-task"><h5>Clean pool area</h5><p>Maintenance</p><span class="tm-kanban-tag med">Medium</span></div>
<div class="tm-kanban-task"><h5>Renew vendor contract</h5><p>Manager</p><span class="tm-kanban-tag med">Medium</span></div>
</div>
<div class="tm-kanban-col">
<div class="tm-kanban-header"><div class="tm-kanban-dot done"></div><h4>Completed</h4><span>5</span></div>
<div class="tm-kanban-task"><h5>Check-in new member</h5><p>Front Desk</p><span class="tm-kanban-tag low">Done</span></div>
<div class="tm-kanban-task"><h5>Fix treadmill belt</h5><p>Maintenance</p><span class="tm-kanban-tag low">Done</span></div>
<div class="tm-kanban-task"><h5>Send birthday wishes</h5><p>Marketing</p><span class="tm-kanban-tag low">Done</span></div>
</div>
</div>
</div>
</section>

<!-- FEATURES GRID -->
<section class="tm-features">
<div class="tm-wrap">
<h2 class="tm-features-title">Everything You Need to Manage Tasks</h2>
<p class="tm-features-sub">From creation to completion, Gymex gives your team the tools to stay organized and accountable.</p>
<div class="tm-features-grid">
<div class="tm-feat-card blue"><div class="tm-feat-icon"><i class="fa fa-plus-circle"></i></div><h4>Create Tasks</h4><p>Add new tasks with details, deadlines, and priorities in seconds.</p></div>
<div class="tm-feat-card orange"><div class="tm-feat-icon"><i class="fa fa-user-plus"></i></div><h4>Assign Staff</h4><p>Allocate tasks to the right team members based on their role.</p></div>
<div class="tm-feat-card green"><div class="tm-feat-icon"><i class="fa fa-flag"></i></div><h4>Set Priorities</h4><p>Mark tasks as high, medium, or low priority for better focus.</p></div>
<div class="tm-feat-card purple"><div class="tm-feat-icon"><i class="fa fa-clock-o"></i></div><h4>Manage Deadlines</h4><p>Set due dates so your team knows when work needs to be done.</p></div>
<div class="tm-feat-card orange"><div class="tm-feat-icon"><i class="fa fa-bell"></i></div><h4>Get Notifications</h4><p>Automatic alerts keep staff updated on assigned tasks.</p></div>
<div class="tm-feat-card blue"><div class="tm-feat-icon"><i class="fa fa-tasks"></i></div><h4>Track Progress</h4><p>Monitor task status from pending to in-progress to completed.</p></div>
<div class="tm-feat-card green"><div class="tm-feat-icon"><i class="fa fa-bar-chart"></i></div><h4>Review Performance</h4><p>Evaluate staff based on how effectively they complete tasks.</p></div>
<div class="tm-feat-card purple"><div class="tm-feat-icon"><i class="fa fa-users"></i></div><h4>Team Accountability</h4><p>Clear ownership means fewer missed tasks and better results.</p></div>
</div>
</div>
</section>

<!-- TIMELINE -->
<section class="tm-timeline">
<div class="tm-wrap">
<h2 class="tm-timeline-title">Your Daily Task Workflow</h2>
<p class="tm-timeline-sub">A simple, repeatable process that turns scattered instructions into organized work.</p>
<div class="tm-timeline-track">
<div class="tm-tl-step"><div class="tm-tl-num">1</div><h5>Create</h5><p>Add the task that needs to be done.</p></div>
<div class="tm-tl-line"></div>
<div class="tm-tl-step"><div class="tm-tl-num">2</div><h5>Assign</h5><p>Choose the responsible staff member.</p></div>
<div class="tm-tl-line"></div>
<div class="tm-tl-step"><div class="tm-tl-num">3</div><h5>Prioritize</h5><p>Set what needs attention first.</p></div>
<div class="tm-tl-line"></div>
<div class="tm-tl-step"><div class="tm-tl-num">4</div><h5>Track</h5><p>Monitor progress in real-time.</p></div>
<div class="tm-tl-line"></div>
<div class="tm-tl-step"><div class="tm-tl-num">5</div><h5>Complete</h5><p>Mark done and review performance.</p></div>
</div>
</div>
</section>

<!-- METRICS -->
<section class="tm-metrics">
<div class="tm-wrap">
<h2 class="tm-metrics-title">Task Management That Drives Results</h2>
<div class="tm-metrics-grid">
<div class="tm-metric"><div class="tm-metric-num c1">100%</div><h5>Task Visibility</h5></div>
<div class="tm-metric"><div class="tm-metric-num c2">0</div><h5>Missed Deadlines</h5></div>
<div class="tm-metric"><div class="tm-metric-num c3">3x</div><h5>Faster Follow-Ups</h5></div>
<div class="tm-metric"><div class="tm-metric-num c4">24/7</div><h5>Team Updates</h5></div>
</div>
</div>
</section>

<!-- ROLES -->
<section class="tm-roles">
<div class="tm-wrap">
<h2 class="tm-roles-title">Assign the Right Task to the Right Person</h2>
<p class="tm-roles-sub">Every role in your gym has different responsibilities. Gymex helps you organize tasks across your entire team.</p>
<div class="tm-roles-row">
<div class="tm-role"><div class="tm-role-icon"><i class="fa fa-desktop"></i></div><h4>Front Desk</h4><p>Member check-ins, admin work, daily ops.</p></div>
<div class="tm-role"><div class="tm-role-icon"><i class="fa fa-line-chart"></i></div><h4>Sales Team</h4><p>Lead follow-ups, enquiries, trials.</p></div>
<div class="tm-role"><div class="tm-role-icon"><i class="fa fa-heartbeat"></i></div><h4>Trainers</h4><p>Training sessions, member follow-ups.</p></div>
<div class="tm-role"><div class="tm-role-icon"><i class="fa fa-wrench"></i></div><h4>Maintenance</h4><p>Equipment checks, repairs, cleaning.</p></div>
<div class="tm-role"><div class="tm-role-icon"><i class="fa fa-briefcase"></i></div><h4>Managers</h4><p>Supervision, admin, business tasks.</p></div>
</div>
</div>
</section>

<!-- CTA -->
<section class="tm-cta">
<div class="tm-wrap">
<h2>Keep Your Team Focused on What Matters</h2>
<p>Bring daily tasks, staff responsibilities, priorities, and progress into one connected platform with Gymex.</p>
<a class="tm-hero-btn" href="#" style="background:#fff;color:#ff4f0d;">Get Your Free Demo <i class="fa fa-arrow-up" style="color:#ff4f0d;"></i></a>
</div>
</section>

<!-- FAQ -->
<section class="tm-faq">
<div class="tm-wrap">
<h2 class="tm-faq-title">Frequently Asked Questions</h2>
<div class="tm-faq-grid">
<div class="tm-faq-item"><details><summary>What is gym task management software?</summary><p>Gym Task Management Software helps gym owners and managers create, assign, organize, and track everyday responsibilities across their teams.</p></details></div>
<div class="tm-faq-item"><details><summary>How does gym staff task management work?</summary><p>Managers can organize responsibilities and assign them to relevant staff members. Tasks can then be tracked through their workflow.</p></details></div>
<div class="tm-faq-item"><details><summary>Can tasks be assigned to different gym staff members?</summary><p>Yes. Gym task management can be used to organize responsibilities across different roles, including front-desk staff, trainers, sales teams, and managers.</p></details></div>
<div class="tm-faq-item"><details><summary>Can task management help with lead follow-ups?</summary><p>Yes. Task management can help teams organize responsibilities related to leads and enquiries so follow-ups are easier to track.</p></details></div>
<div class="tm-faq-item"><details><summary>Can Gymex help manage daily gym tasks?</summary><p>Gymex helps organize everyday staff and operational responsibilities within a structured workflow.</p></details></div>
<div class="tm-faq-item"><details><summary>How can task management improve staff accountability?</summary><p>Assigning clear ownership to responsibilities helps staff understand what they are expected to complete.</p></details></div>
<div class="tm-faq-item"><details><summary>Is task management useful for gym operations?</summary><p>Yes. Tasks can cover administrative responsibilities, member follow-ups, sales activities, equipment-related work, and maintenance.</p></details></div>
<div class="tm-faq-item"><details><summary>Can task management reduce manual follow-ups?</summary><p>Keeping assigned responsibilities and their progress visible can reduce the need for managers to repeatedly contact staff.</p></details></div>
</div>
</div>
</section>

</div>

''' + footer + '''

<script src="../javascript.js"></script>
</body>
</html>'''

with open('task-management/task-management.html', 'w', encoding='utf-8') as f:
    f.write(html)
print(f'Created: {len(html)} chars')
