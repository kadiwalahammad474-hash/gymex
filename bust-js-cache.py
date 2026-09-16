# -*- coding: utf-8 -*-
"""Add ?v=2 cache-buster to javascript.js script tags so browsers fetch the new burger handler."""
import re, os

pages = [f for f in os.listdir('.') if f.endswith('.html')]
for d in os.listdir('.'):
    if os.path.isdir(d) and not d.startswith('.'):
        pages += [os.path.join(d, f) for f in os.listdir(d) if f.endswith('.html')]

fixed = 0
for p in sorted(set(pages)):
    s = open(p, encoding='utf-8', errors='ignore').read()
    orig = s
    # javascript.js (root-relative or same-dir) without existing query
    s = re.sub(r'src="(\.{0,2}/?)javascript\.js"', r'src="\1javascript.js?v=2"', s)
    if s != orig:
        open(p, 'w', encoding='utf-8', newline='').write(s)
        fixed += 1

print(f'cache-buster added on {fixed} pages')
# verify none without buster
missing = 0
for p in sorted(set(pages)):
    s = open(p, encoding='utf-8', errors='ignore').read()
    missing += len(re.findall(r'src="(\.{0,2}/?)javascript\.js"', s))
print('tags still without buster:', missing)
