# -*- coding: utf-8 -*-
"""Site-wide sweep:
1. Every html: <script src> / <link href> local file exists?
2. javascript.js/nav.js syntax-check via node
3. Duplicate IDs in any page
4. Div balance per page
"""
import io, os, re, glob, subprocess, collections

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

issues = []

# 1. local asset refs
for p in glob.glob('*/*.html') + glob.glob('*.html'):
    base = os.path.dirname(p)
    s = io.open(p, encoding='utf-8', errors='replace').read()
    for m in re.finditer(r'(?:src|href)="([^"#][^"]*)"', s):
        u = m.group(1)
        if u.startswith(('http', '//', 'mailto:', 'tel:', 'data:', 'javascript:')) or u == '':
            continue
        path = u.split('?')[0].split('#')[0]
        if not path:
            continue
        full = os.path.normpath(os.path.join(base, path))
        if not os.path.exists(full):
            issues.append(f'{p}: missing {u}')

# 2. node syntax check
for jsf in ['javascript.js', 'nav.js']:
    r = subprocess.run(['node', '--check', jsf], capture_output=True, text=True)
    if r.returncode != 0:
        issues.append(f'{jsf}: SYNTAX ERROR: {r.stderr[:200]}')

# 3. duplicate ids
for p in glob.glob('*/*.html') + glob.glob('*.html'):
    s = io.open(p, encoding='utf-8', errors='replace').read()
    ids = re.findall(r'id="([^"]+)"', s)
    dups = [i for i, c in collections.Counter(ids).items() if c > 1]
    if dups:
        issues.append(f'{p}: duplicate ids: {dups[:4]}')

# 4. div balance
for p in glob.glob('*/*.html') + glob.glob('*.html'):
    s = io.open(p, encoding='utf-8', errors='replace').read()
    d = len(re.findall(r'<div\b', s)) - s.count('</div>')
    if d != 0:
        issues.append(f'{p}: div balance {d}')

print(f'{len(issues)} issues')
for i in issues[:40]:
    print(' -', i)
