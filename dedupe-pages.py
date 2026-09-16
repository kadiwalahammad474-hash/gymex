# -*- coding: utf-8 -*-
"""Deduplicate concatenated HTML documents in business/business.html and
features/features.html. Multiple full <!DOCTYPE html> documents got
concatenated into one file; keep only the LAST copy (most recent edits)
of each, verify it has exactly one nav / one dropdown-menu, then save."""
import os, re

FILES = [
    "business/business.html",
    "features/features.html",
]

for p in FILES:
    s = open(p, encoding="utf-8", errors="ignore").read()
    total_before = len(s)
    # split into complete documents on <!DOCTYPE html>
    starts = [m.start() for m in re.finditer(r'<!DOCTYPE html>', s, re.I)]
    print(f"\n=== {p}: {len(starts)} document copies found ===")
    docs = []
    for i, st in enumerate(starts):
        end = starts[i + 1] if i + 1 < len(starts) else len(s)
        docs.append(s[st:end])
    for i, d in enumerate(docs):
        print(f"  copy {i+1}: {len(d)} bytes, navs={d.count('<nav class=\"nav\"')}, "
              f"bizLinks={d.count('business-types-link')}, "
              f"footers={d.count('<!-- Footer -->')}, closed={'</html>' in d}")
    # keep last copy (most recently edited appended copy)
    keep = docs[-1].rstrip() + "\n"
    # sanity: exactly one of each critical id
    checks = {
        'nav': keep.count('<nav class="nav"'),
        'biz-link': keep.count('id="business-types-link"'),
        'dropdown-menu': keep.count('id="dropdown-menu"'),
        'features-menu': keep.count('id="features-dropdown-menu"'),
        'menu-backdrop': keep.count('id="menu-backdrop"'),
        'open-menu': keep.count('id="open-menu"'),
        '</html>': keep.count('</html>'),
    }
    print("  keeping copy with:", checks)
    bad = [k for k, v in checks.items() if v != 1]
    if bad:
        print(f"  !! LAST COPY ALSO BROKEN ({bad}) — checking earlier copies")
        for i in range(len(docs) - 2, -1, -1):
            c = docs[i]
            ok = all(c.count(f'id="{x}"') == 1 or c.count('<nav class="nav"') == 1 for x in
                     ['business-types-link', 'dropdown-menu', 'features-dropdown-menu', 'menu-backdrop', 'open-menu'])
            n_nav = c.count('<nav class="nav"')
            if n_nav == 1 and all(c.count(f'id="{x}"') == 1 for x in
                                  ['business-types-link', 'dropdown-menu', 'features-dropdown-menu', 'menu-backdrop', 'open-menu']):
                keep = c.rstrip() + "\n"
                print(f"  -> using copy {i+1} instead")
                break
    open(p, "w", encoding="utf-8", newline="").write(keep)
    print(f"  saved: {total_before} -> {len(keep)} bytes")

# final verification across both files
print("\n=== FINAL VERIFY ===")
for p in FILES:
    s = open(p, encoding="utf-8", errors="ignore").read()
    print(f"{p}: doctypes={s.count('<!DOCTYPE html>')} navs={s.count(chr(60)+'nav class=\"nav\"')} "
          f"biz={s.count('business-types-link')} menu={s.count(chr(105)+'d=\"dropdown-menu\"')} "
          f"htmlClose={s.count('</html>')}")
