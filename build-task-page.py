import re, os

# Read expense page to get nav and footer
with open('expense-management/expense-management.html', 'r', encoding='utf-8') as f:
    exp = f.read()

# Extract nav
nav_m = re.search(r'(<nav class="nav".*?</nav>)', exp, re.DOTALL)
nav = nav_m.group(1) if nav_m else ''

# Extract footer
ft_m = re.search(r'(<!-- FOOTER from Home -->.*?</body>)', exp, re.DOTALL)
footer = ft_m.group(1) if ft_m else ''

# Read CSS
with open('task-management/task-management.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Build HTML
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

<section class="tm-hero"><div class="tm-hero-grid"><div>
<p class="tm-label">GYM TASK MANAGEMENT SOFTWARE</p>
<h1><span class="tm-dark">Assign, Track &amp; Manage</span><br><span class="tm-accent">Gym Tasks</span> <span class="tm-dark">with Ease</span></h1>
<p class="tm-desc">Create and allocate tasks, set priorities and deadlines, track progress, and keep your team updated with task notifications. Gymex helps you organize daily responsibilities and review staff performance based on task completion.</p>
<a class="mm-btn-orange" href="#">Get Your Free Demo <i class="fa fa-arrow-up"></i></a>
</div><div class="tm-hero-img"><div class="tm-img-placeholder"><i class="fa fa-camera"></i><span>gym-task-management-software-gymex.webp</span></div></div></div></section>

<section class="tm-section tm-bg-white"><div class="tm-container"><div class="tm-split">
<div class="tm-split-content">
<h2 class="tm-h2">Create and Assign Tasks to Your Team</h2>
<p class="tm-text">Gymex makes it easy to create tasks and allocate them to the right team members from one connected platform. Managers can clearly define responsibilities so every staff member knows what needs to be done.</p>
<p class="tm-text">Whether it is a member follow-up, administrative work, sales activity, or an operational responsibility, structured gym staff task management helps keep daily work organized.</p>
</div>
<div class="tm-split-image"><div class="tm-img-placeholder"><i class="fa fa-camera"></i><span>gym-staff-task-management-gymex.webp</span></div></div>
</div></div></section>

<section class="tm-section tm-bg-light"><div class="tm-container"><div class="tm-split">
<div class="tm-split-image"><div class="tm-img-placeholder"><i class="fa fa-camera"></i><span>gym-daily-task-management-gymex.webp</span></div></div>
<div class="tm-split-content">
<h2 class="tm-h2">Assign the Right Task to the Right Staff Member</h2>
<p class="tm-text">Clear task ownership helps your team understand exactly what they are responsible for.</p>
<p class="tm-sub">Tasks can be assigned based on different responsibilities:</p>
<div class="tm-role-grid">
<div class="tm-role-card"><div class="tm-role-icon"><i class="fa fa-desktop"></i></div><h4>Front Desk</h4><p>Member-related activities, administrative work, and daily operational tasks.</p></div>
<div class="tm-role-card"><div class="tm-role-icon"><i class="fa fa-line-chart"></i></div><h4>Sales Team</h4><p>Lead follow-ups, enquiries, trial follow-ups, and other sales responsibilities.</p></div>
<div class="tm-role-card"><div class="tm-role-icon"><i class="fa fa-heartbeat"></i></div><h4>Trainers</h4><p>Member-related responsibilities, training activities, and assigned follow-ups.</p></div>
<div class="tm-role-card"><div class="tm-role-icon"><i class="fa fa-wrench"></i></div><h4>Maintenance</h4><p>Equipment checks, repairs, facility maintenance, and operational tasks.</p></div>
<div class="tm-role-card"><div class="tm-role-icon"><i class="fa fa-briefcase"></i></div><h4>Managers</h4><p>Team supervision, administrative responsibilities, and business-related activities.</p></div>
</div>
</div></div></div></section>

<section class="tm-section tm-bg-white"><div class="tm-container">
<h2 class="tm-h2 tm-text-center">Prioritize Tasks and Manage Deadlines</h2>
<p class="tm-text tm-text-center tm-mb-32">Not every task requires the same level of attention. Gymex allows you to prioritize tasks based on their importance and deadlines.</p>
<div class="tm-flow-strip">
<span class="tm-flow-item"><i class="fa fa-plus-circle"></i> Create Task</span>
<span class="tm-arrow"><i class="fa fa-arrow-right"></i></span>
<span class="tm-flow-item"><i class="fa fa-user-plus"></i> Assign Staff</span>
<span class="tm-arrow"><i class="fa fa-arrow-right"></i></span>
<span class="tm-flow-item"><i class="fa fa-flag"></i> Set Priority</span>
<span class="tm-arrow"><i class="fa fa-arrow-right"></i></span>
<span class="tm-flow-item"><i class="fa fa-clock-o"></i> Set Deadline</span>
<span class="tm-arrow"><i class="fa fa-arrow-right"></i></span>
<span class="tm-flow-item"><i class="fa fa-tasks"></i> Track Progress</span>
<span class="tm-arrow"><i class="fa fa-arrow-right"></i></span>
<span class="tm-flow-item tm-green"><i class="fa fa-check-circle"></i> Complete</span>
</div></div></section>

<section class="tm-section tm-bg-light"><div class="tm-container"><div class="tm-split">
<div class="tm-split-content">
<h2 class="tm-h2">Keep Your Team Updated with Task Notifications</h2>
<p class="tm-text">Important responsibilities are easier to manage when staff are kept informed.</p>
<p class="tm-text">Gymex provides task notifications to keep team members updated about their assigned tasks and responsibilities.</p>
<div class="tm-check-list">
<div class="tm-check-item"><i class="fa fa-check"></i> Automatic task assignment notifications</div>
<div class="tm-check-item"><i class="fa fa-check"></i> Deadline reminders</div>
<div class="tm-check-item"><i class="fa fa-check"></i> Status update alerts</div>
<div class="tm-check-item"><i class="fa fa-check"></i> Completion confirmations</div>
</div></div>
<div class="tm-split-image"><div class="tm-img-placeholder"><i class="fa fa-camera"></i><span>gym-task-tracking-software-gymex.webp</span></div></div>
</div></div></section>

<section class="tm-section tm-bg-white"><div class="tm-container"><div class="tm-split">
<div class="tm-split-image"><div class="tm-img-placeholder"><i class="fa fa-camera"></i><span>gym-task-tracking-software-gymex.webp</span></div></div>
<div class="tm-split-content">
<h2 class="tm-h2">Track Task Progress from One Place</h2>
<p class="tm-text">Assigning a task is only the beginning. Managers also need to know whether the work is pending, in progress, or completed.</p>
<p class="tm-sub">This makes it easier to:</p>
<div class="tm-check-list">
<div class="tm-check-item"><i class="fa fa-check"></i> Monitor assigned tasks</div>
<div class="tm-check-item"><i class="fa fa-check"></i> Check task status</div>
<div class="tm-check-item"><i class="fa fa-check"></i> Identify work that requires attention</div>
<div class="tm-check-item"><i class="fa fa-check"></i> Keep track of task completion</div>
<div class="tm-check-item"><i class="fa fa-check"></i> Reduce repeated follow-ups</div>
</div></div>
</div></div></section>

<section class="tm-section tm-bg-light"><div class="tm-container">
<h2 class="tm-h2 tm-text-center">Review Staff Performance Based on Task Completion</h2>
<p class="tm-text tm-text-center tm-mb-32">Task management can provide useful insight into how consistently staff members are completing their responsibilities.</p>
<div class="tm-card-grid">
<div class="tm-card"><div class="tm-card-icon"><i class="fa fa-check-square"></i></div><h4>Review Completed Work</h4><p>See which tasks have been finished and by whom.</p></div>
<div class="tm-card"><div class="tm-card-icon"><i class="fa fa-bar-chart"></i></div><h4>Monitor Consistency</h4><p>Track how reliably staff complete assigned tasks.</p></div>
<div class="tm-card"><div class="tm-card-icon"><i class="fa fa-exclamation-triangle"></i></div><h4>Identify Delays</h4><p>Spot pending or delayed work that needs attention.</p></div>
<div class="tm-card"><div class="tm-card-icon"><i class="fa fa-trophy"></i></div><h4>Recognize Top Performers</h4><p>Acknowledge staff who consistently deliver.</p></div>
</div></div></section>

<section class="tm-section tm-bg-white"><div class="tm-container">
<h2 class="tm-h2 tm-text-center">Create a Clear Daily Task Workflow</h2>
<p class="tm-text tm-text-center tm-mb-32">Gymex helps turn everyday responsibilities into a simple, repeatable process.</p>
<div class="tm-process-strip">
<div class="tm-process-step"><div class="tm-process-num">1</div><h5>Create</h5><p>Add the task that needs to be completed.</p></div>
<div class="tm-process-arrow"><i class="fa fa-arrow-right"></i></div>
<div class="tm-process-step"><div class="tm-process-num">2</div><h5>Assign</h5><p>Choose the relevant staff member responsible.</p></div>
<div class="tm-process-arrow"><i class="fa fa-arrow-right"></i></div>
<div class="tm-process-step"><div class="tm-process-num">3</div><h5>Prioritize</h5><p>Define which tasks require attention first.</p></div>
<div class="tm-process-arrow"><i class="fa fa-arrow-right"></i></div>
<div class="tm-process-step"><div class="tm-process-num">4</div><h5>Track</h5><p>Monitor the progress of assigned work.</p></div>
<div class="tm-process-arrow"><i class="fa fa-arrow-right"></i></div>
<div class="tm-process-step"><div class="tm-process-num">5</div><h5>Complete</h5><p>Keep completed work organized.</p></div>
</div></div></section>

<section class="tm-section tm-bg-light"><div class="tm-container">
<h2 class="tm-h2 tm-text-center">Why Choose Gymex for Task Management?</h2>
<p class="tm-text tm-text-center tm-mb-32">From assigning work to reviewing task completion, managers get better visibility while staff stay informed.</p>
<div class="tm-benefit-grid">
<div class="tm-benefit-card"><i class="fa fa-check-circle"></i><h5>Create &amp; Allocate Tasks</h5><p>Create new tasks and assign them to the appropriate team members.</p></div>
<div class="tm-benefit-card"><i class="fa fa-check-circle"></i><h5>Set Priorities</h5><p>Prioritize important responsibilities so staff know what needs attention first.</p></div>
<div class="tm-benefit-card"><i class="fa fa-check-circle"></i><h5>Manage Deadlines</h5><p>Keep time-sensitive tasks organized and easier to track.</p></div>
<div class="tm-benefit-card"><i class="fa fa-check-circle"></i><h5>Task Notifications</h5><p>Keep team members updated about assigned tasks.</p></div>
<div class="tm-benefit-card"><i class="fa fa-check-circle"></i><h5>Monitor Task Status</h5><p>Track the status of tasks without repeatedly asking for updates.</p></div>
<div class="tm-benefit-card"><i class="fa fa-check-circle"></i><h5>Track Completion</h5><p>Maintain visibility into completed and outstanding work.</p></div>
<div class="tm-benefit-card"><i class="fa fa-check-circle"></i><h5>Review Performance</h5><p>Evaluate staff performance based on task completion.</p></div>
<div class="tm-benefit-card"><i class="fa fa-check-circle"></i><h5>Improve Accountability</h5><p>Create clear ownership of responsibilities across your team.</p></div>
</div></div></section>

<section class="tm-cta"><div class="tm-container tm-text-center">
<h2 class="tm-cta-title">Keep Your Team Focused on What Matters</h2>
<p class="tm-cta-desc">Bring daily tasks, staff responsibilities, priorities, and progress into one connected platform with Gymex.</p>
<p class="tm-cta-sub">Assign clearly. Track progress. Get more done.</p>
<a class="mm-btn-orange" href="#">Get Your Free Demo <i class="fa fa-arrow-up"></i></a>
</div></section>

<section class="tm-section tm-bg-white"><div class="tm-container">
<h2 class="tm-h2 tm-text-center">Frequently Asked Questions</h2>
<div class="tm-faq-grid">
<div class="tm-faq-item"><details><summary>What is gym task management software?</summary><p>Gym Task Management Software helps gym owners and managers create, assign, organize, and track everyday responsibilities across their teams.</p></details></div>
<div class="tm-faq-item"><details><summary>How does gym staff task management work?</summary><p>Managers can organize responsibilities and assign them to relevant staff members. Tasks can then be tracked through their workflow.</p></details></div>
<div class="tm-faq-item"><details><summary>Can tasks be assigned to different gym staff members?</summary><p>Yes. Gym task management can be used to organize responsibilities across different roles, including front-desk staff, trainers, sales teams, and managers.</p></details></div>
<div class="tm-faq-item"><details><summary>Can task management help with lead follow-ups?</summary><p>Yes. Task management can help teams organize responsibilities related to leads and enquiries so follow-ups are easier to track.</p></details></div>
<div class="tm-faq-item"><details><summary>Can Gymex help manage daily gym tasks?</summary><p>Gymex helps organize everyday staff and operational responsibilities within a structured workflow.</p></details></div>
<div class="tm-faq-item"><details><summary>How can task management improve staff accountability?</summary><p>Assigning clear ownership to responsibilities helps staff understand what they are expected to complete.</p></details></div>
<div class="tm-faq-item"><details><summary>Is task management useful for gym operations?</summary><p>Yes. Tasks can cover administrative responsibilities, member follow-ups, sales activities, equipment-related work, and maintenance.</p></details></div>
<div class="tm-faq-item"><details><summary>Can task management reduce manual follow-ups?</summary><p>Keeping assigned responsibilities and their progress visible can reduce the need for managers to repeatedly contact staff.</p></details></div>
</div></div></section>

</div>

''' + footer + '''

<script src="../javascript.js"></script>
</body>
</html>'''

with open('task-management/task-management.html', 'w', encoding='utf-8') as f:
    f.write(html)
print(f'Created: {len(html)} chars')
