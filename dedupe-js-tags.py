# -*- coding: utf-8 -*-
"""Keep only ONE javascript.js script tag per page — duplicates double-attach
burger/dropdown handlers (net effect: nothing works)."""
import re, os

pages = [f for f in os.listdir('.') if f.endswith('.html')]
for d in os.listdir('.'):
    if os.path.isdir(d) and not d.startswith('.'):
        pages += [os.path.join(d, f) for f in os.listdir(d) if f.endswith('.html')]

fixed = []
for p in sorted(set(pages)):
    s = open(p, encoding='utf-8', errors='ignore').read()
    tags = re.findall(r'<script src="[^"]*javascript\.js[^"]*"></script>', s)
    if len(tags) > 1:
        # keep first, remove rest
        seen = 0
        def repl(m):
            global seen
            seen += 1
            return m.group(0) if seen == 1 else ''
        s2 = re.sub(r'<script src="[^"]*javascript\.js[^"]*"></script>', repl, s)
        # also drop now-empty lines left behind
        s2 = re.sub(r'\n\s*\n(\s*\n)+', '\n\n', s2)
        open(p, 'w', encoding='utf-8', newline='').write(s2)
        fixed.append((p, len(tags)))

print(f'fixed {len(fixed)} pages:')
for p, n in fixed:
    print(f'  {p} (had {n}x javascript.js)')

# final verify
bad = 0
for p in sorted(set(pages)):
    s = open(p, encoding='utf-8', errors='ignore').read()
    n = len(re.findall(r'<script src="[^"]*javascript\.js[^"]*"></script>', s))
    if n > 1:
        print('STILL DUPLICATE:', p, n)
        bad += 1
print('pages with duplicates remaining:', bad)
