# -*- coding: utf-8 -*-
"""Rebuild business.html and features.html keeping head from copy 1 and
body from the newest complete copy; collapse duplicate trailing closes."""
import re

def rebuild(p, head_end, body_start):
    lines = open(p, encoding="utf-8", errors="ignore").read().splitlines(keepends=True)
    final = "".join(lines[:head_end]) + "".join(lines[body_start:])
    # collapse duplicate trailing </body></html>
    final = re.sub(r'(\s*</body>\s*</html>)+\s*$', '\n</body>\n</html>\n', final)
    open(p, "w", encoding="utf-8", newline="").write(final)
    # verify
    s = open(p, encoding="utf-8").read()
    checks = {
        "body": len(re.findall(r'<body>', s)),
        "nav": s.count('<nav class="nav"'),
        "biz-link": s.count('id="business-types-link"'),
        "dropdown-menu": s.count('id="dropdown-menu"'),
        "features-menu": s.count('id="features-dropdown-menu"'),
        "backdrop": s.count('id="menu-backdrop"'),
        "open-menu": s.count('id="open-menu"'),
        "html-close": s.count('</html>'),
        "footer": s.count('<!-- Footer -->'),
    }
    opens = len(re.findall(r'<div\b', s)); closes = s.count('</div>')
    print(f"{p}: {checks} | div balance {opens}/{closes} = {opens == closes}")

rebuild("business/business.html", head_end=49, body_start=471)
rebuild("features/features.html", head_end=59, body_start=1262)
