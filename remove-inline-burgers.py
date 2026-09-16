# -*- coding: utf-8 -*-
"""Remove inline burger IIFEs from pages (canonical handler moves to javascript.js)."""
import re, os

pages = [f for f in os.listdir('.') if f.endswith('.html')]
for d in os.listdir('.'):
    if os.path.isdir(d) and not d.startswith('.'):
        pages += [os.path.join(d, f) for f in os.listdir(d) if f.endswith('.html')]

# Match the whole standalone burger IIFE (non-greedy to its own closing })();
PAT = re.compile(
    r"\(function\(\)\{\s*var T=document\.getElementById\('menu-backdrop'\),b=document\.getElementById\('open-menu'\);.*?\}\)\(\);",
    re.S)

fixed = []
for p in sorted(set(pages)):
    s = open(p, encoding='utf-8', errors='ignore').read()
    orig = s
    s = PAT.sub('/* burger handled by javascript.js (canonical) */', s)
    # clean now-empty script blocks left behind
    s = re.sub(r'<script>\s*/\* burger handled by javascript\.js \(canonical\) \*/\s*</script>', '', s)
    if s != orig:
        open(p, 'w', encoding='utf-8', newline='').write(s)
        fixed.append(p)

print(f'inline burger removed from {len(fixed)} pages:')
for p in fixed:
    print(' ', p)

# verify
remaining = 0
for p in sorted(set(pages)):
    s = open(p, encoding='utf-8', errors='ignore').read()
    remaining += len(PAT.findall(s))
print('inline burger handlers remaining:', remaining)
