# -*- coding: utf-8 -*-
"""Show full error for the 4 broken inline scripts."""
import re, subprocess, tempfile

for p, idx in [('lead-management/lead-management.html', 5),
               ('marketing-management/marketing-management.html', 5),
               ('staff-management/staff-management.html', 8),
               ('thankyou.html', 1)]:
    s = open(p, encoding='utf-8', errors='ignore').read()
    sc = [x for x in re.findall(r'<script>(.*?)</script>', s, re.S) if x.strip()][idx]
    code = sc.strip()
    with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False, encoding='utf-8') as f:
        f.write(code)
        tmp = f.name
    r = subprocess.run(['node', '--check', tmp], capture_output=True, text=True)
    os_removed = False
    print(f'=== {p} script#{idx} ===')
    print(r.stderr[:600])
    print('first 120 chars:', code[:120])
    print()
