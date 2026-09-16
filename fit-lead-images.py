# -*- coding: utf-8 -*-
import io, re

P = r"C:\Users\Developer4\Desktop\gymexglobalwebsite\lead-management\lead-management.html"
s = io.open(P, encoding="utf-8").read()

IMG = ('<img src="{src}" alt="{alt}" loading="lazy" '
       'style="width:100%;border-radius:16px;box-shadow:0 8px 30px rgba(0,0,0,.14);display:block;">')

def slot_re(label):
    return re.compile(
        r'<div style="background:#f0f4f8;border-radius:16px;border:2px dashed #c3d0e0;min-height:340px;'
        r'display:flex;align-items:center;justify-content:center;text-align:center;padding:40px;"><div>'
        r'<i class="fa fa-camera"[^>]*></i><p[^>]*>' + re.escape(label) + r'</p><p[^>]*>[^<]*</p></div></div>')

# ---- 1) FIT: capture slot -> real image ----
pat = slot_re('Lead Capture &amp; Enquiry Form Screenshot')
if pat.search(s):
    s = pat.sub(IMG.format(src="../assets/lead_management_latest_1200x700.png",
                           alt="Gymex gym lead capture and enquiry form software"), s, count=1)
    print("capture: image fitted")
else:
    print("!! capture slot not found")

# ---- 2) FIT: pipeline slot -> real image ----
pat = slot_re('Sales Pipeline Board Screenshot')
if pat.search(s):
    s = pat.sub(IMG.format(src="../assets/gym_sales_pipeline_1200x700.png",
                           alt="Gymex gym sales pipeline board"), s, count=1)
    print("pipeline: image fitted")
else:
    print("!! pipeline slot not found")

# ---- 3) REMOVE: 4 slots ----
for label in ['Lead Interaction Timeline Screenshot',
              'WhatsApp / SMS Follow-up Automation Screenshot',
              'Lead Analytics Report Screenshot',
              'Connected CRM Workflow Diagram']:
    pat = slot_re(label)
    if pat.search(s):
        s = pat.sub('', s, count=1)
        print("removed:", label)
    else:
        print("!! NOT FOUND:", label)

# ---- 4) UNWRAP now-single-child fx-splits (replace opening div with plain container — balance-safe) ----
unwraps = [
    # follow-up: slot was first child; text child now directly after fx-split open
    ('<div class="fx-split" style="display:grid;grid-template-columns:.85fr 1.15fr;gap:36px;align-items:center;">'
     '<div><div class="sm-heading" style="text-align:left;"><h2>Follow Up',
     '<div style="max-width:1100px;margin:0 auto;"><div><div class="sm-heading" style="text-align:left;"><h2>Follow Up'),
    # analytics
    ('<div class="fx-split" style="display:grid;grid-template-columns:1.15fr .85fr;gap:36px;align-items:center;">'
     '<div><div class="sm-heading" style="text-align:left;"><h2>Know Which Marketing',
     '<div style="max-width:1100px;margin:0 auto;"><div><div class="sm-heading" style="text-align:left;"><h2>Know Which Marketing'),
    # crm
    ('<div class="fx-split" style="display:grid;grid-template-columns:1.15fr .85fr;gap:36px;align-items:center;">'
     '<div><div class="sm-heading" style="text-align:left;"><h2>One Connected',
     '<div style="max-width:1100px;margin:0 auto;"><div><div class="sm-heading" style="text-align:left;"><h2>One Connected'),
]
for old, new in unwraps:
    if old in s:
        s = s.replace(old, new, 1)
        print("unwrapped:", new[95:130])
    else:
        print("!! unwrap not found:", old[85:125])

io.open(P, "w", encoding="utf-8", newline="\n").write(s)
print("done")
