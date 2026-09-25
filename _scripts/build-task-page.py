import re

with open('task-management/nav.txt', 'r', encoding='utf-8') as f:
    nav = f.read()
with open('task-management/footer.txt', 'r', encoding='utf-8') as f:
    footer = f.read()

sections = []

sections.append('''<section class="tm-hero"><div class="tm-hero-grid"><div>
<p class="tm-label">GYM TASK MANAGEMENT SOFTWARE</p>
<h1><span class="tm-dark">Assign, Track & Manage</span><br><span class="tm-accent">Gym Tasks</span> <span class="tm-dark">with Ease</span></h1>
<p class="tm-desc">Create and allocate tasks, set priorities and deadlines, track progress, and keep your team updated with task notifications. Gymex helps you organize daily responsibilities and review staff performance based on task completion.</p>
<div class="tm-hero-cta"><a class="tm-btn" href="#">Get Your Free Demo <i class="fa fa-arrow-up"></i></a></div>
</div><div class="tm-hero-img"><div class="tm-img-placeholder"><i class="fa fa-camera"></i><span>gym-task-management-software-gymex.webp</span></div></div></div></section>''')

sections.append('''<section class="tm-section tm-bg-white"><div class="tm-container"><div class="tm-split">
<div class="tm-split-content">
<h2 class="tm-h2">Create and Assign Tasks to Your Team</h2>
<p class="tm-text">Gymex makes it easy to create tasks and allocate them to the right team members from one connected platform. Managers can clearly define responsibilities so every staff member knows what needs to be done.</p>
<p class="tm-text">Whether it is a member follow-up, administrative work, sales activity, or an operational responsibility, structured gym staff task management helps keep daily work organized.</p>
</div>
<div class="tm-split-image"><div class="tm-img-placeholder"><i class="fa fa-camera"></i><span>gym-staff-task-management-gymex.webp</span></div></div>
</div></div></section>''')

sections.append('''<section class="tm-section tm-bg-light"><div class="tm-container"><div class="tm-split">
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
</div></div></div></div></section>''')

sections.append('''<section class="tm-section tm-bg-white"><div class="tm-container">
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
<span class="tm-flow-item tm-blue"><i class="fa fa-check-circle"></i> Complete</span>
</div></div></section>''')

sections.append('''<section class="tm-section tm-bg-light"><div class="tm-container"><div class="tm-split">
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
</div></div></section>''')

sections.append('''<section class="tm-section tm-bg-white"><div class="tm-container"><div class="tm-split">
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
</div></div></div></div></section>''')

sections.append('''<section class="tm-section tm-bg-light"><div class="tm-container">
<h2 class="tm-h2 tm-text-center">Review Staff Performance Based on Task Completion</h2>
<p class="tm-text tm-text-center tm-mb-32">Task management can provide useful insight into how consistently staff members are completing their responsibilities.</p>
<div class="tm-card-grid">
<div class="tm-card"><div class="tm-card-icon"><i class="fa fa-check-square"></i></div><h4>Review Completed Work</h4><p>See which tasks have been finished and by whom.</p></div>
<div class="tm-card"><div class="tm-card-icon"><i class="fa fa-bar-chart"></i></div><h4>Monitor Consistency</h4><p>Track how reliably staff complete assigned tasks.</p></div>
<div class="tm-card"><div class="tm-card-icon"><i class="fa fa-exclamation-triangle"></i></div><h4>Identify Delays</h4><p>Spot pending or delayed work that needs attention.</p></div>
<div class="tm-card"><div class="tm-card-icon"><i class="fa fa-trophy"></i></div><h4>Recognize Top Performers</h4><p>Acknowledge staff who consistently deliver.</p></div>
</div></div></section>''')

sections.append('''<section class="tm-section tm-bg-white"><div class="tm-container">
<h2 class="tm-h2 tm-text-center">Create a Clear Daily Task Workflow</h2>
<p class="tm-text tm-text-center tm-mb-32">Gymex helps turn everyday responsibilities into a sim
