# -*- coding: utf-8 -*-
"""Ensure every page with the demo modal (#divemailpopup) has working modal CSS:
check the page's actually-linked stylesheets for a .backdrop rule; if none has it,
inject <link ../css/modal-shared.css> after the last local stylesheet link."""
import re, os

ROOT = '.'

def linked_css_files(page_path, html):
    """Return local CSS files this page links, existing on disk, relative to repo root."""
    links = re.findall(r'<link[^>]+href="([^"]+\.css[^"]*)"', html)
    page_dir = os.path.dirname(page_path)
    out = []
    for href in links:
        href_clean = href.split('?')[0]
        if href_clean.startswith('http'):
            continue
        # resolve relative to page dir
        full = os.path.normpath(os.path.join(page_dir, href_clean)) if page_dir else href_clean
        if os.path.isfile(full):
            out.append(full)
    return out

def has_backdrop_rule(css_path):
    try:
        s = open(css_path, encoding='utf-8', errors='ignore').read()
    except Exception:
        return False
    # .backdrop with display/fixed rule (the modal container)
    return bool(re.search(r'\.backdrop\s*\{[^}]*position\s*:\s*fixed', s, re.S)) or bool(re.search(r'\.backdrop\.show\s*\{', s))

pages = [f for f in os.listdir('.') if f.endswith('.html')]
for d in os.listdir('.'):
    if os.path.isdir(d) and not d.startswith('.'):
        pages += [os.path.join(d, f) for f in os.listdir(d) if f.endswith('.html')]

fixed = []
for p in sorted(set(pages)):
    s = open(p, encoding='utf-8', errors='ignore').read()
    if 'divemailpopup' not in s:
        continue
    # already links modal-shared? then fine
    if 'modal-shared.css' in s:
        continue
    # does any linked css already style the backdrop?
    covered = False
    for css in linked_css_files(p, s):
        if has_backdrop_rule(css):
            covered = True
            break
    if covered:
        continue
    # inject modal-shared link after the last local stylesheet <link>
    links = list(re.finditer(r'<link[^>]+href="[^"]+\.css[^"]*"[^>]*>', s))
    if not links:
        print(f'NO CSS LINKS FOUND: {p} — skipping')
        continue
    last = links[-1]
    # path depth: if page is in subdir, href="../css/modal-shared.css", else "css/modal-shared.css"
    prefix = '../' if os.path.dirname(p) else ''
    inject = f'\n<link rel="stylesheet" href="{prefix}css/modal-shared.css">'
    s = s[:last.end()] + inject + s[last.end():]
    open(p, 'w', encoding='utf-8', newline='').write(s)
    fixed.append(p)

print(f'\ninjected modal-shared.css on {len(fixed)} pages:')
for p in fixed:
    print(' ', p)

# final audit
still = []
for p in sorted(set(pages)):
    s = open(p, encoding='utf-8', errors='ignore').read()
    if 'divemailpopup' not in s:
        continue
    if 'modal-shared.css' in s:
        continue
    covered = any(has_backdrop_rule(c) for c in linked_css_files(p, s))
    if not covered:
        still.append(p)
print('\npages STILL missing modal CSS:', still if still else 'NONE — all covered')
