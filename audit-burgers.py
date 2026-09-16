# -*- coding: utf-8 -*-
"""Audit: pages with #open-menu but no burger handler script (dead burger)."""
import re, os

pages = [f for f in os.listdir('.') if f.endswith('.html')]
for d in os.listdir('.'):
    if os.path.isdir(d) and not d.startswith('.'):
        pages += [os.path.join(d, f) for f in os.listdir(d) if f.endswith('.html')]

dead = ok = 0
for p in sorted(set(pages)):
    s = open(p, encoding='utf-8', errors='ignore').read()
    has_burger = 'id="open-menu"' in s
    has_handler = re.search(r"getElementById\(['\"]menu-backdrop['\"]\)", s) and re.search(r"getElementById\(['\"]open-menu['\"]\)", s)
    if has_burger and not has_handler:
        print(f'DEAD BURGER: {p}')
        dead += 1
    elif has_burger:
        ok += 1

print(f'\nburgers OK: {ok}, dead: {dead}')
