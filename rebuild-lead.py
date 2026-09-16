# -*- coding: utf-8 -*-
import io

P = r"C:\Users\Developer4\Desktop\gymexglobalwebsite\lead-management\lead-management.html"
s = io.open(P, encoding="utf-8").read()
lines = s.split("\n")

SLOT = ('<div style="background:#f0f4f8;border-radius:16px;border:2px dashed #c3d0e0;min-height:340px;'
        'display:flex;align-items:center;justify-content:center;text-align:center;padding:40px;"><div>'
        '<i class="fa fa-camera" style="font-size:44px;color:#b0c4d8;margin-bottom:14px;display:block;"></i>'
        '<p style="font-size:14px;color:#8899aa;font-weight:700;margin:0 0 4px;">{label}</p>'
        '<p style="font-size:12px;color:#aab8c5;margin:0;">{file} &mdash; 1200&times;700px (16:9)</p></div></div>')

CHECK = ('<div style="display:flex;align-items:center;gap:12px;padding:14px 18px;background:#f0fdf4;border-radius:10px;">'
         '<div style="width:30px;height:30px;background:#22c55e;border-radius:50%;display:flex;align-items:center;'
         'justify-content:center;flex-shrink:0;"><i class="fa fa-check" style="color:#fff;font-size:13px;"></i></div>'
         '<span style="font-size:14px;color:#333;">{t}</span></div>')

RED = ('<div style="display:flex;align-items:center;gap:14px;padding:16px 20px;background:#fef2f2;border-radius:12px;'
       'border-left:4px solid #ef4444;"><span style="font-size:20px;">{ic}</span>'
       '<p style="font-size:14px;color:#555;margin:0;">{t}</p></div>')

def checkitems(items):
    return "\n".join(CHECK.format(t=t) for t in items)

# ---------------- 1. PROBLEM ----------------
problem_items = [
    ("&#128548;", "Searching through WhatsApp messages for an old enquiry"),
    ("&#128203;", "Forgetting which staff member spoke to a prospect"),
    ("&#128221;", "Losing walk-in details in a notebook"),
    ("&#128260;", "Following up with the same person twice"),
    ("&#128269;", "Guessing which marketing channel brings your best members"),
]
reds = "\n".join(RED.format(ic=ic, t=t) for ic, t in problem_items)
s_problem = f'''<section class="sm-section" style="background:#fff;"><div class="sm-wrap"><div style="max-width:1100px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:50px;align-items:center;">
<div><p style="font-size:12px;font-weight:700;color:#ef4444;text-transform:uppercase;letter-spacing:2px;margin-bottom:12px;">The Problem</p>
<h2 style="font-size:clamp(24px,2.8vw,32px);font-weight:800;margin-bottom:16px;">Stop Losing Leads to Missed Follow-Ups</h2>
<p style="color:var(--gray-80,#6b7589);font-size:15px;line-height:1.75;margin-bottom:16px;">A potential member fills in a form, calls the front desk, or walks-in to ask about your plans. What happens next should not depend on someone remembering to call them later.</p>
<p style="color:var(--gray-80,#6b7589);font-size:15px;line-height:1.75;margin-bottom:16px;">With Gymex, every new enquiry is recorded in one place. Your team can track the lead from first contact to trial, membership purchase, or follow-up later.</p>
<p style="color:#111;font-size:15px;line-height:1.75;font-weight:600;">Instead, you get a clear view of every prospect and the next action needed to move them forward.</p></div>
<div><p style="font-size:13px;font-weight:800;color:#ef4444;text-transform:uppercase;letter-spacing:1.5px;margin-bottom:14px;">No more:</p>
<div style="display:flex;flex-direction:column;gap:14px;">
{reds}
</div></div>
</div></div></section>'''

# ---------------- 2. CAPTURE ----------------
capture_items = [
    "Website enquiry and trial-booking forms",
    "Walk-ins at your gym or studio",
    "Phone calls and WhatsApp enquiries",
    "Social-media campaigns and paid advertisements",
    "Referrals from existing members",
    "Fitness events and promotional campaigns",
    "Imported leads from Excel or another system",
]
s_capture = f'''<section class="sm-section grey"><div class="sm-wrap"><div class="fx-split" style="display:grid;grid-template-columns:1.1fr .9fr;gap:36px;align-items:center;">
<div><div class="sm-heading" style="text-align:left;"><h2>Capture Gym Leads from <span class="accent">Every Important Channel</span></h2><div class="sm-underline"></div></div>
<p style="color:var(--gray-80,#6b7589);font-size:15px;line-height:1.75;margin-bottom:18px;">People discover your gym in different ways. A good lead-management process makes sure every enquiry reaches the same system, regardless of where it came from.</p>
<p style="font-size:13px;font-weight:800;color:#1565C0;text-transform:uppercase;letter-spacing:1.5px;margin-bottom:12px;">Capture and organize leads from:</p>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
{checkitems(capture_items)}
</div></div>
<div>{SLOT.format(label="Lead Capture &amp; Enquiry Form Screenshot", file="gym-lead-capture-form-gymex.webp")}</div>
</div>
<div style="max-width:1100px;margin:24px auto 0;background:#fff;border-radius:16px;padding:22px 28px;box-shadow:0 2px 12px rgba(0,0,0,.06);border-left:4px solid #1565C0;">
<p style="font-size:14px;color:#555;line-height:1.75;margin:0;"><strong style="color:#111;">Each lead profile keeps the details your staff needs:</strong> contact information, enquiry source, interests, notes, follow-up history, assigned team member, and current sales stage.</p></div>
</div></section>'''

# ---------------- 3. PIPELINE ----------------
stages = ["New Enquiry", "Contacted", "Trial Booked", "Trial Attended", "Membership Discussed", "Joined", "Lost or Follow Up Later"]
grads = ["linear-gradient(135deg,#1565C0,#1976d2)","linear-gradient(135deg,#1976d2,#2196f3)","linear-gradient(135deg,#2196f3,#42a5f5)","linear-gradient(135deg,#42a5f5,#26a69a)","linear-gradient(135deg,#26a69a,#66bb6a)","linear-gradient(135deg,#66bb6a,#2e9e44)","linear-gradient(135deg,#8d99ae,#6c7a89)"]
stage_cells = []
for i, (st, g) in enumerate(zip(stages, grads)):
    rad = "12px 0 0 12px;" if i == 0 else ("0 12px 12px 0;" if i == len(stages)-1 else "0;")
    stage_cells.append(f'<div style="flex:1;min-width:110px;background:{g};color:#fff;padding:18px 10px;border-radius:{rad}text-align:center;"><div style="font-size:22px;font-weight:800;margin-bottom:4px;">{i+1:02d}</div><div style="font-size:11px;font-weight:600;text-transform:uppercase;line-height:1.4;">{st}</div></div>')
stages_html = "\n".join(stage_cells)
s_pipeline = f'''<section class="sm-section"><div class="sm-wrap"><div class="fx-split" style="display:grid;grid-template-columns:1.15fr .85fr;gap:36px;align-items:center;">
<div><div class="sm-heading" style="text-align:left;"><h2>See Your Entire <span class="accent">Gym Sales Pipeline</span> at a Glance</h2><div class="sm-underline"></div></div>
<p style="color:var(--gray-80,#6b7589);font-size:15px;line-height:1.75;margin-bottom:12px;">Know exactly where every prospect is in the journey from enquiry to membership.</p>
<p style="color:var(--gray-80,#6b7589);font-size:15px;line-height:1.75;margin-bottom:12px;">Create a sales pipeline that reflects how your gym actually sells. For example:</p>
<p style="font-size:14px;font-weight:700;color:#1565C0;line-height:1.7;background:#e8f0fe;border-radius:10px;padding:14px 18px;margin-bottom:14px;">New Enquiry &rarr; Contacted &rarr; Trial Booked &rarr; Trial Attended &rarr; Membership Discussed &rarr; Joined &rarr; Lost or Follow Up Later</p>
<p style="color:var(--gray-80,#6b7589);font-size:14px;line-height:1.75;">A visual pipeline helps your front-desk and sales teams focus on the right conversations. You can quickly identify fresh enquiries, prospects who have not been contacted, trial members who are ready to join, and leads that need another follow-up.</p></div>
<div>{SLOT.format(label="Sales Pipeline Board Screenshot", file="gym-lead-management-pipeline-gymex.webp")}</div>
</div>
<div style="max-width:1100px;margin:24px auto 0;display:flex;align-items:stretch;justify-content:center;gap:0;flex-wrap:wrap;">
{stages_html}
</div></div></section>'''

# ---------------- 4. FOLLOW-UP ----------------
follow_items = [
    "Assign each lead to the right staff member",
    "Set follow-up calls, messages, visits, and trial reminders",
    "Add notes after every conversation",
    "View the complete interaction history in one timeline",
    "Flag leads that have not been contacted recently",
    "Keep handovers smooth when staff members change shifts",
]
s_follow = f'''<section class="sm-section grey"><div class="sm-wrap"><div class="fx-split" style="display:grid;grid-template-columns:.85fr 1.15fr;gap:36px;align-items:center;">
<div>{SLOT.format(label="Lead Interaction Timeline Screenshot", file="gym-lead-follow-up-timeline-gymex.webp")}</div>
<div><div class="sm-heading" style="text-align:left;"><h2>Follow Up <span class="accent">Faster</span> and More Consistently</h2><div class="sm-underline"></div></div>
<p style="color:var(--gray-80,#6b7589);font-size:15px;line-height:1.75;margin-bottom:16px;">Fast, thoughtful follow-up builds trust. Gymex helps your team stay on top of every next step with scheduled tasks, reminders, and clear ownership.</p>
<p style="font-size:13px;font-weight:800;color:#1565C0;text-transform:uppercase;letter-spacing:1.5px;margin-bottom:12px;">Use the lead-management module to:</p>
<div style="display:flex;flex-direction:column;gap:10px;">
{checkitems(follow_items)}
</div>
<p style="color:#111;font-size:15px;font-weight:600;margin-top:16px;">Your team always knows who to contact next and why.</p></div>
</div></div></section>'''

# ---------------- 5. AUTOMATION ----------------
auto_items = [
    "An instant acknowledgement when someone submits an enquiry",
    "A reminder to call a new prospect",
    "A confirmation before a gym tour or trial session",
    "A follow-up after a trial class",
    "A membership offer for prospects who are ready to join",
    "A re-engagement message for leads who went quiet",
]
s_auto = f'''<section class="sm-section"><div class="sm-wrap"><div class="fx-split" style="display:grid;grid-template-columns:1.1fr .9fr;gap:36px;align-items:center;">
<div><p style="font-size:12px;font-weight:700;color:#22c55e;text-transform:uppercase;letter-spacing:2px;margin-bottom:12px;">Automation</p>
<h2 style="font-size:clamp(24px,2.8vw,32px);font-weight:800;margin-bottom:16px;">Automate the Routine, Keep the Conversation Personal</h2>
<p style="color:var(--gray-80,#6b7589);font-size:15px;line-height:1.75;margin-bottom:14px;">Manual follow-up is difficult to maintain when your gym is busy. Automate the routine messages so your staff can focus on real conversations and better member experiences.</p>
<p style="font-size:13px;font-weight:800;color:#22c55e;text-transform:uppercase;letter-spacing:1.5px;margin-bottom:12px;">Set up relevant communications such as:</p>
<div style="display:flex;flex-direction:column;gap:10px;">
{checkitems(auto_items)}
</div></div>
<div>{SLOT.format(label="WhatsApp / SMS Follow-up Automation Screenshot", file="gym-lead-automation-whatsapp-gymex.webp")}</div>
</div>
<div style="max-width:1100px;margin:24px auto 0;background:#f0fdf4;border-radius:16px;padding:20px 28px;border-left:4px solid #22c55e;">
<p style="font-size:14px;color:#444;line-height:1.75;margin:0;">Use approved communication channels such as <strong>WhatsApp, SMS, email, or push notifications</strong> according to the features available in your plan. Personalize messages with the prospect&rsquo;s name, preferred programme, enquiry source, or trial date.</p></div>
</div></section>'''

# ---------------- 6. ANALYTICS ----------------
metrics = [
    ("&#128202;", "New Leads Received", "Total enquiries per day, week, month"),
    ("&#128205;", "Lead Source", "Which channel every lead came from"),
    ("&#9889;", "First-Response Time", "How fast your team responds"),
    ("&#128222;", "Follow-Ups Completed", "Calls, messages &amp; visits done"),
    ("&#127950;", "Tours &amp; Trials Booked", "Fitness center tours and trials"),
    ("&#127942;", "Trial-to-Member Rate", "Trials that become memberships"),
    ("&#127919;", "Lead-to-Member Rate", "Overall enquiry conversion"),
    ("&#128101;", "Staff-wise Performance", "Conversion results per staff member"),
    ("&#128201;", "Lost-Lead Reasons", "Why leads were lost &amp; when to retry"),
    ("&#9201;", "Time to Convert", "Time taken to turn a prospect into a member (Check Report)"),
]
metric_cards = "\n".join(
    f'<div style="background:#fff;border-radius:16px;padding:24px 16px;text-align:center;box-shadow:0 2px 12px rgba(0,0,0,.05);"><div style="font-size:32px;">{ic}</div><h3 style="font-size:14px;font-weight:700;color:#111;margin:10px 0 6px;">{t}</h3><p style="font-size:12px;color:#888;line-height:1.6;">{d}</p></div>'
    for ic, t, d in metrics)
s_analytics = f'''<section class="sm-section grey"><div class="sm-wrap"><div class="fx-split" style="display:grid;grid-template-columns:1.15fr .85fr;gap:36px;align-items:center;">
<div><div class="sm-heading" style="text-align:left;"><h2>Know Which Marketing Efforts <span class="accent">Create Real Memberships</span></h2><div class="sm-underline"></div></div>
<p style="color:var(--gray-80,#6b7589);font-size:15px;line-height:1.75;margin-bottom:12px;">Getting enquiries is useful. Knowing which enquiries become paying members is more useful.</p>
<p style="color:var(--gray-80,#6b7589);font-size:15px;line-height:1.75;margin-bottom:14px;">Gymex helps you record where leads come from, so you can understand whether your strongest prospects are coming from Google, social media, referrals, walk-ins, local partnerships, or your website.</p>
<p style="font-size:13px;font-weight:800;color:#1565C0;text-transform:uppercase;letter-spacing:1.5px;">Track the numbers that matter:</p></div>
<div>{SLOT.format(label="Lead Analytics Report Screenshot", file="gym-lead-analytics-report-gymex.webp")}</div>
</div>
<div style="max-width:1100px;margin:24px auto 0;display:grid;grid-template-columns:repeat(5,1fr);gap:16px;">
{metric_cards}
</div>
<p style="max-width:900px;margin:22px auto 0;color:var(--gray-80,#6b7589);font-size:15px;line-height:1.75;text-align:center;">Use these insights to improve campaigns, coach your sales team, and invest more confidently in the channels that bring the right members to your gym.</p>
</div></section>'''

# ---------------- 7. CONNECTED CRM ----------------
s_crm = f'''<section class="sm-section"><div class="sm-wrap"><div class="fx-split" style="display:grid;grid-template-columns:1.15fr .85fr;gap:36px;align-items:center;">
<div><div class="sm-heading" style="text-align:left;"><h2>One Connected <span class="accent">Gym CRM</span>, Not Another Tool to Manage</h2><div class="sm-underline"></div></div>
<p style="color:var(--gray-80,#6b7589);font-size:15px;line-height:1.75;margin-bottom:14px;">Lead management works best when it is connected to the rest of your gym software.</p>
<p style="color:var(--gray-80,#6b7589);font-size:15px;line-height:1.75;margin-bottom:14px;">When a prospect books a trial, attends a class, makes a payment, or becomes a member, that activity should be visible to your team without duplicate entry. Gymex keeps your lead workflow connected with the wider member journey, helping you move seamlessly from first enquiry to active membership.</p>
<p style="color:var(--gray-80,#6b7589);font-size:15px;line-height:1.75;">That means less switching between tools, fewer data gaps, and a clearer experience for both staff and prospects.</p></div>
<div>{SLOT.format(label="Connected CRM Workflow Diagram", file="gym-connected-crm-workflow-gymex.webp")}</div>
</div></div></section>'''

# ---------------- 8. BUILT FOR ----------------
s_built = '''<section class="sm-section grey"><div class="sm-wrap"><div class="sm-heading"><h2>Built for Gyms, Fitness Studios, and <span class="accent">Multi-Location Businesses</span></h2><div class="sm-underline"></div></div>
<p style="max-width:900px;margin:0 auto 14px;color:var(--gray-80,#6b7589);font-size:15px;line-height:1.75;text-align:center;">Whether you manage a neighbourhood gym, a personal-training studio, a Yoga or Pilates studio, a CrossFit box, or a growing fitness chain, the same principle applies: every enquiry deserves a timely response.</p>
<p style="max-width:900px;margin:0 auto 30px;color:var(--gray-80,#6b7589);font-size:15px;line-height:1.75;text-align:center;">Gymex gives your team a practical way to organize sales activity without making the process complicated. Customize stages, assign leads, track performance, and give each branch the visibility it needs.</p>
<div style="max-width:1000px;margin:0 auto;display:grid;grid-template-columns:repeat(4,1fr);gap:20px;">
<div style="background:#fff;border-radius:16px;padding:26px 18px;text-align:center;box-shadow:0 2px 12px rgba(0,0,0,.05);"><div style="width:48px;height:48px;background:#e8f0fe;border-radius:12px;display:flex;align-items:center;justify-content:center;margin:0 auto 14px;"><i class="fa fa-dumbbell" style="font-size:20px;color:#1565C0;"></i></div><h3 style="font-size:15px;font-weight:700;color:#111;margin-bottom:6px;">Gyms</h3><p style="font-size:13px;color:#888;">Neighbourhood gyms &amp; fitness centres</p></div>
<div style="background:#fff;border-radius:16px;padding:26px 18px;text-align:center;box-shadow:0 2px 12px rgba(0,0,0,.05);"><div style="width:48px;height:48px;background:#f0fdf4;border-radius:12px;display:flex;align-items:center;justify-content:center;margin:0 auto 14px;"><i class="fa fa-spa" style="font-size:20px;color:#22c55e;"></i></div><h3 style="font-size:15px;font-weight:700;color:#111;margin-bottom:6px;">Fitness Studios</h3><p style="font-size:13px;color:#888;">PT, Yoga, Pilates &amp; CrossFit boxes</p></div>
<div style="background:#fff;border-radius:16px;padding:26px 18px;text-align:center;box-shadow:0 2px 12px rgba(0,0,0,.05);"><div style="width:48px;height:48px;background:#fff3e0;border-radius:12px;display:flex;align-items:center;justify-content:center;margin:0 auto 14px;"><i class="fa fa-building" style="font-size:20px;color:#f26522;"></i></div><h3 style="font-size:15px;font-weight:700;color:#111;margin-bottom:6px;">Fitness Chains</h3><p style="font-size:13px;color:#888;">Growing multi-location fitness brands</p></div>
<div style="background:#fff;border-radius:16px;padding:26px 18px;text-align:center;box-shadow:0 2px 12px rgba(0,0,0,.05);"><div style="width:48px;height:48px;background:#f3f0ff;border-radius:12px;display:flex;align-items:center;justify-content:center;margin:0 auto 14px;"><i class="fa fa-code-branch" style="font-size:20px;color:#8b5cf6;"></i></div><h3 style="font-size:15px;font-weight:700;color:#111;margin-bottom:6px;">Custom Stages</h3><p style="font-size:13px;color:#888;">Pipeline stages that match your process</p></div>
</div></div></section>'''

# ---------------- 9. CTA ----------------
s_cta = '''<section class="sm-section" style="background:#1565C0;"><div class="sm-wrap" style="text-align:center;"><div style="max-width:800px;margin:0 auto;"><h2 style="font-size:32px;font-weight:800;color:#fff;margin-bottom:16px;">Turn More Interest into Membership Revenue</h2><p style="font-size:16px;color:rgba(255,255,255,.85);line-height:1.8;margin-bottom:10px;">Your next member may already have enquired. Give your team the tools to respond quickly, follow up consistently, and make every prospect feel looked after.</p><button class="mm-btn mm-btn-orange magnetic-btn open-modal-btn" style="font-size:16px;">Book a Personal Demo <i class="fa fa-arrow-up"></i></button><p style="font-size:14px;color:rgba(255,255,255,.75);margin-top:14px;">See how Gymex can fit your current sales process.</p></div></div></section>'''

# ---------------- 10. FAQ ----------------
faqs = [
    ("What is gym lead management module?", "Gym lead management module helps gyms capture, organize, track, and follow up with prospective members. It gives staff a single place to manage enquiries from first contact through tours, trials, and membership sign-up."),
    ("How does a gym CRM help increase memberships?", "A gym CRM helps your team respond faster, record every interaction, schedule follow-ups, and identify prospects who are ready to join. It also makes it easier to measure which lead sources and sales activities generate memberships."),
    ("Can I track website, walk-in, and phone enquiries in one place?", "Yes. Gymex is designed to keep enquiries from multiple sources in one lead pipeline, so your team does not need to manage separate spreadsheets, notebooks, or chat threads."),
    ("Can I automate follow-ups for gym leads?", "Yes. Depending on your selected features, you can create automated reminders and follow-up communications through channels such as WhatsApp, SMS, or email. Automated workflows help ensure new enquiries receive a prompt response while staff retain the personal touch."),
    ("What should a gym lead pipeline include?", "Most gyms use stages such as New Enquiry, Contacted, Tour Booked, Trial Booked, Trial Attended, Membership Discussed, Joined, and Lost. The best structure is the one that matches your real sales process and makes it easy for staff to know the next action."),
    ("Can I see which marketing channel brings the best leads?", "Yes. By recording lead sources and tracking their progress to membership, you can compare the quality and conversion rate of leads from your website, social media, referrals, walk-ins, campaigns, and other channels."),
]
faq_cards = "\n".join(
    f'<div style="background:#f8f9fc;border-radius:12px;padding:24px;"><h3 style="font-size:15px;font-weight:700;color:#111;margin-bottom:10px;">{q}</h3><p style="font-size:14px;color:#666;line-height:1.7;">{a}</p></div>'
    for q, a in faqs)
s_faq = f'''<section class="sm-section"><div class="sm-wrap"><div class="sm-heading"><h2>Frequently Asked <span class="accent">Questions</span></h2><div class="sm-underline"></div></div><div style="max-width:1000px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:20px;">
{faq_cards}
</div></div></section>'''

# ---- replace by marker ----
def replace_section(text, marker, contains, new, name):
    for line in text.split("\n"):
        ls = line.strip()
        if ls.startswith(marker) and contains in ls:
            text = text.replace(line, new, 1)
            print("replaced:", name)
            return text
    print("!! NOT FOUND:", name)
    return text

s = replace_section(s, '<section class="sm-section" style="background:#fff;"><div class="sm-wrap"><div style="max-width:1000px', 'Stop Losing Leads', s_problem, "problem")
s = replace_section(s, '<section class="sm-section grey"><div class="sm-wrap"><div class="sm-heading"><h2>Capture Gym Leads', 'Every Channel', s_capture, "capture")
s = replace_section(s, '<section class="sm-section"><div class="sm-wrap"><div class="fx-split"', 'Sales Pipeline', s_pipeline, "pipeline")
s = replace_section(s, '<section class="sm-section grey"><div class="sm-wrap"><div class="fx-split"', 'Follow Up', s_follow, "follow-up")
s = replace_section(s, '<section class="sm-section"><div class="sm-wrap"><div style="max-width:1000px', 'Automate the Routine', s_auto, "automation")
s = replace_section(s, '<section class="sm-section grey"><div class="sm-wrap"><div class="fx-split"', 'Know Which Marketing', s_analytics, "analytics")
s = replace_section(s, '<section class="sm-section"><div class="sm-wrap" style="max-width:800px', 'One Connected', s_crm, "crm")
s = replace_section(s, '<section class="sm-section grey"><div class="sm-wrap"><div class="sm-heading"><h2>Built for Gyms', 'Multi-Location', s_built, "built-for")
s = replace_section(s, '<section class="sm-section" style="background:#1565C0;">', 'Membership Revenue', s_cta, "cta")
s = replace_section(s, '<section class="sm-section"><div class="sm-wrap"><div class="sm-heading"><h2>Frequently Asked', 'Questions', s_faq, "faq")

io.open(P, "w", encoding="utf-8", newline="\n").write(s)
print("done")
