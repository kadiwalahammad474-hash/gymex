# -*- coding: utf-8 -*-
import os, re, io

ROOT = r"C:\Users\Developer4\Desktop\gymexglobalwebsite"
pages = []
for dp, dn, fn in os.walk(ROOT):
    dn[:] = [d for d in dn if d not in (".git", "node_modules", "brochure-view", "assets")]
    for f in fn:
        if f.endswith(".html"):
            pages.append(os.path.join(dp, f))

report = {}
for p in sorted(pages):
    rel = os.path.relpath(p, ROOT)
    try:
        s = io.open(p, encoding="utf-8", errors="ignore").read()
    except Exception as e:
        report[rel] = ["READ ERROR: " + str(e)]
        continue
    issues = []
    # all buttons containing GET YOUR FREE DEMO text
    for m in re.finditer(r'<button[^>]*>(?:(?!</button>).)*?GET YOUR FREE DEMO.*?</button>', s, re.S):
        tag = m.group(0)
        cls = re.search(r'class="([^"]*)"', tag)
        cls = cls.group(1) if cls else ""
        has_modal = "open-modal-btn" in cls
        # nav / mobile / other context
        ctx = "nav" if "nav__link" in cls else ("mobile-menu" if "button" in cls else "other")
        if not has_modal:
            issues.append(f"{ctx} button WITHOUT open-modal-btn: class='{cls[:60]}'")
    # footer ASK FOR DEMO
    if "ASK FOR DEMO" in s:
        for m in re.finditer(r'<a[^>]*>\s*ASK FOR DEMO', s):
            tag = m.group(0)
            if "open-modal-btn" not in tag:
                issues.append("footer ASK FOR DEMO without open-modal-btn")
    # modal present?
    if "GET YOUR FREE DEMO" in s or "ASK FOR DEMO" in s:
        if 'id="divemailpopup"' not in s:
            issues.append("NO MODAL (divemailpopup)")
        if "emailjs" not in s:
            issues.append("NO emailjs script")
    if issues:
        report[rel] = issues

n_ok = 0
for rel in sorted(report):
    print("!!", rel)
    for i in report[rel]:
        print("    -", i)
total = len(pages)
print(f"\n{total} pages scanned, {len(report)} with issues, {total-len(report)} clean")
