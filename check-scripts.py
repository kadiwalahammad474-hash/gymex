# -*- coding: utf-8 -*-
"""Extract all inline scripts from every page and syntax-check each with node."""
import re, os, subprocess, tempfile

pages = [f for f in os.listdir('.') if f.endswith('.html')]
for d in os.listdir('.'):
    if os.path.isdir(d) and not d.startswith('.'):
        pages += [os.path.join(d, f) for f in os.listdir(d) if f.endswith('.html')]

bad = total = 0
for p in sorted(pages):
    s = open(p, encoding='utf-8', errors='ignore').read()
    for i, sc in enumerate(re.findall(r'<script>(.*?)</script>', s, re.S)):
        code = sc.strip()
        if not code:
            continue
        total += 1
        with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False, encoding='utf-8') as f:
            f.write(code)
            tmp = f.name
        r = subprocess.run(['node', '--check', tmp], capture_output=True, text=True)
        os.unlink(tmp)
        if r.returncode != 0:
            bad += 1
            first = r.stderr.strip().splitlines()
            print(f'SYNTAX ERROR {p} script#{i}: {first[-1] if first else "?"}')

print(f'\nchecked {total} inline scripts, {bad} syntax errors')
