# -*- coding: utf-8 -*-
"""Replace FA4 icon names that do NOT render in FA6 (browser-tested) with FA6 equivalents.
Names that render via FA6 aliases (fa-line-chart, fa-bar-chart, fa-mobile, fa-pie-chart,
fa-tablet) are left untouched."""
import re, os

FIX = {
    'fa-calendar-check-o': 'fa-calendar-check',
    'fa-calendar-times-o': 'fa-calendar-xmark',
    'fa-clock-o': 'fa-clock',
    'fa-file-text-o': 'fa-file-lines',
    'fa-money': 'fa-money-bill',
}

pages = [f for f in os.listdir('.') if f.endswith('.html')]
for d in os.listdir('.'):
    if os.path.isdir(d) and not d.startswith('.'):
        pages += [os.path.join(d, f) for f in os.listdir(d) if f.endswith('.html')]

replacements = 0
touched = []
for p in sorted(set(pages)):
    s = open(p, encoding='utf-8', errors='ignore').read()
    orig = s
    for old, new in FIX.items():
        s, n = re.subn(r'\b' + re.escape(old) + r'\b', new, s)
        replacements += n
    if s != orig:
        open(p, 'w', encoding='utf-8', newline='').write(s)
        touched.append(p)

print(f'{replacements} icon names fixed across {len(touched)} pages')
for p in touched:
    print(' ', p)

# verify none remain
left = 0
for p in sorted(set(pages)):
    s = open(p, encoding='utf-8', errors='ignore').read()
    for old in FIX:
        left += len(re.findall(r'\b' + re.escape(old) + r'\b', s))
print('broken names remaining:', left)
