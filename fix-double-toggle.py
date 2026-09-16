# -*- coding: utf-8 -*-
"""Fix double-toggle dropdown bug: pages load javascript.js (which toggles
#business-types-link/#features-link menus at DOMContentLoaded) AND have an
inline IIFE that ALSO toggles '.dropdown > a' — two handlers on the same
element cancel each other out. Remove the inline dropdown-toggle part from
every affected page (keep its backdrop/modal logic), and for pages whose
backdrop toggle also exists twice keep only one."""
import os, re

ROOT = "."
pages = []
for root, dirs, files in os.walk(ROOT):
    if any(x in root for x in [".git", "node_modules"]): continue
    for f in files:
        if f.endswith(".html"):
            pages.append(os.path.join(root, f))

DRIVER = re.compile(
    r"// Mobile dropdown toggle\s*document\.querySelectorAll\('\.dropdown > a'\)\.forEach\(function\(trigger\)\{.*?\}\);\s*\}\);\s*",
    re.S,
)
DRIVER_DQ = re.compile(
    r'// Mobile dropdown toggle\s*document\.querySelectorAll\("\.dropdown > a"\)\.forEach\(function\(trigger\)\{.*?\}\);\s*\}\);\s*',
    re.S,
)

fixed = []
for p in pages:
    s = open(p, encoding="utf-8", errors="ignore").read()
    orig = s
    # does this page load javascript.js (which toggles by id)?
    loads_driver = "javascript.js" in s
    # count dropdown toggle implementations
    has_inline_driver = bool(DRIVER.search(s) or DRIVER_DQ.search(s))
    has_jquery_style = "menu.classList.toggle('show')" in s or 'menu.classList.toggle("show")' in s
    if loads_driver and has_inline_driver:
        s2 = DRIVER.sub("// Mobile dropdown toggle handled by javascript.js (single handler)\n", s)
        s2 = DRIVER_DQ.sub("// Mobile dropdown toggle handled by javascript.js (single handler)\n", s2)
        if s2 != orig:
            open(p, "w", encoding="utf-8", newline="").write(s2)
            fixed.append(p)

print(f"fixed {len(fixed)} pages:")
for p in fixed:
    print(" -", p)

# verify no page still has both
print("\n=== VERIFY: pages with BOTH javascript.js and inline toggle ===")
bad = 0
for p in pages:
    s = open(p, encoding="utf-8", errors="ignore").read()
    if "javascript.js" in s and re.search(r"querySelectorAll\(['\"]\.dropdown > a['\"]\)", s):
        print(" STILL DOUBLE:", p)
        bad += 1
print("none" if bad == 0 else f"{bad} pages still double")
