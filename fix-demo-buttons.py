# -*- coding: utf-8 -*-
"""Standardize all GET YOUR FREE DEMO buttons site-wide:
1. Inject the standard modal + EmailJS block into pages that have demo buttons but no modal
2. Wire the mobile-menu demo button (add open-modal-btn class) everywhere
"""
import os, re, io

ROOT = r"C:\Users\Developer4\Desktop\gymexglobalwebsite"
LM = os.path.join(ROOT, "lead-management", "lead-management.html")

lm = io.open(LM, encoding="utf-8").read()

# ---- extract modal block from lead-management ----
i0 = lm.find('<!-- Backdrop Modal (Imran\'s version) -->')
i1 = lm.find('</div>', lm.find('id="emailsuccessmsg"'))
# find the real end: the modal outer div closes after form-submission-message div
m_end = lm.find('<!-- EmailJS -->', i0)
modal_block = lm[i0:m_end].rstrip()
# strip trailing newlines, keep structure
print("modal block chars:", len(modal_block))

# ---- extract emailjs script block ----
j0 = lm.find('<!-- EmailJS -->')
j1 = lm.find('<script>\n// Reveal on scroll')
if j1 == -1:
    j1 = lm.find("// Reveal on scroll")
    j1 = lm.rfind('<script>', 0, j1)
emailjs_block = lm[j0:j1].rstrip()
print("emailjs block chars:", len(emailjs_block))

# sanity
assert 'id="divemailpopup"' in modal_block
assert 'emailjs.send' in emailjs_block

def fix_page(path, rel):
    s = io.open(path, encoding="utf-8").read()
    changed = False
    msgs = []

    has_demo = ("GET YOUR FREE DEMO" in s) or ("ASK FOR DEMO" in s)
    if not has_demo:
        return msgs

    # 1) wire mobile-menu button: <button class="button "> containing GET YOUR FREE DEMO
    def wire_mobile(m):
        tag = m.group(0)
        if "open-modal-btn" in tag:
            return tag
        nt = tag.replace('class="button "', 'class="button open-modal-btn"')
        nt = nt.replace('class="button"', 'class="button open-modal-btn"')
        return nt
    ns = re.sub(r'<button class="button[^"]*">\s*<p class="button__text">GET YOUR FREE DEMO</p>.*?</button>',
                wire_mobile, s, flags=re.S)
    if ns != s:
        s = ns; changed = True
        msgs.append("mobile button wired")

    # 2) inject modal + emailjs if missing
    if 'id="divemailpopup"' not in s:
        # anchor: insert before </body>
        idx = s.rfind('</body>')
        if idx == -1:
            msgs.append("!! no </body>")
        else:
            inject = "\n" + modal_block + "\n\n" + emailjs_block + "\n\n"
            s = s[:idx] + inject + s[idx:]
            changed = True
            msgs.append("modal+emailjs injected")

    if changed:
        io.open(path, "w", encoding="utf-8", newline="").write(s)
    return msgs

total_msgs = {}
for dp, dn, fn in os.walk(ROOT):
    dn[:] = [d for d in dn if d not in (".git", "node_modules", "brochure-view", "assets")]
    for f in fn:
        if f.endswith(".html"):
            p = os.path.join(dp, f)
            rel = os.path.relpath(p, ROOT)
            try:
                msgs = fix_page(p, rel)
                if msgs:
                    total_msgs[rel] = msgs
            except Exception as e:
                total_msgs[rel] = ["!! ERROR: " + str(e)]

for rel in sorted(total_msgs):
    print(rel, "->", "; ".join(total_msgs[rel]))
print("\ndone:", len(total_msgs), "pages changed")
