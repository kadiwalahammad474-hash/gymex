# -*- coding: utf-8 -*-
"""Audit all pages for FA4-only icon class names that don't render in FA6."""
import re, os

# FA4 names with no FA6 equivalent (renamed ones only — partial list of the common ones)
FA4 = [
    'fa-pencil-square-o', 'fa-file-text-o', 'fa-file-o', 'fa-envelope-o', 'fa-bell-o',
    'fa-star-o', 'fa-heart-o', 'fa-comment-o', 'fa-user-o', 'fa-circle-o', 'fa-square-o',
    'fa-check-circle-o', 'fa-times-circle-o', 'fa-question-circle-o', 'fa-plus-square-o',
    'fa-minus-square-o', 'fa-hand-o-up', 'fa-hand-o-down', 'fa-hand-o-right', 'fa-hand-o-left',
    'fa-thumbs-o-up', 'fa-thumbs-o-down', 'fa-clock-o', 'fa-calendar-check-o', 'fa-calendar-minus-o',
    'fa-calendar-plus-o', 'fa-calendar-times-o', 'fa-calendar-o', 'fa-floppy-o', 'fa-trash-o',
    'fa-share-square-o', 'fa-gear', 'fa-gears', 'fa-bar-chart', 'fa-bar-chart-o', 'fa-line-chart',
    'fa-pie-chart', 'fa-area-chart', 'fa-money', 'fa-cc-visa', 'fa-facebook-official',
    'fa-google-plus', 'fa-youtube-play', 'fa-paper-plane-o', 'fa-lightbulb-o', 'fa-folder-o',
    'fa-folder-open-o', 'fa-edit', 'fa-sign-out', 'fa-sign-in', 'fa-mobile', 'fa-mobile-phone',
    'fa-tablet', 'fa-location-arrow', 'fa-angle-double-down',
]

pages = [f for f in os.listdir('.') if f.endswith('.html')]
for d in os.listdir('.'):
    if os.path.isdir(d) and not d.startswith('.'):
        pages += [os.path.join(d, f) for f in os.listdir(d) if f.endswith('.html')]

total = 0
by_icon = {}
for p in sorted(set(pages)):
    s = open(p, encoding='utf-8', errors='ignore').read()
    for icon in FA4:
        n = len(re.findall(r'class="[^"]*\b' + re.escape(icon) + r'\b', s))
        if n:
            by_icon.setdefault(icon, []).append(f'{p}({n})')
            total += n

if not by_icon:
    print('All clean — 0 deprecated FA4 icons across all pages')
else:
    for icon, locs in sorted(by_icon.items()):
        print(f'{icon}: {", ".join(locs)}')
    print(f'\ntotal: {total}')
