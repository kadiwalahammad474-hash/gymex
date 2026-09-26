# -*- coding: utf-8 -*-
"""Swap order: CTA section ABOVE FAQ section (was FAQ -> CTA, now CTA -> FAQ)."""
import io, glob

CTA_MARKER = '<section class="sm-section" style="background:#1565C0;'
FAQ_TEXT = 'Frequently Asked Questions'

changed, skipped = [], []
for p in sorted(glob.glob('*/*.html')):
    s = io.open(p, encoding='utf-8', newline='').read()
    if FAQ_TEXT not in s or CTA_MARKER not in s:
        continue
    lines = s.split('\n')

    # CTA line index (single-line section)
    cta_idx = next((i for i, l in enumerate(lines) if CTA_MARKER in l), None)
    # FAQ section start: line containing '<section' whose block contains FAQ_TEXT before '</section>'
    faq_start = faq_end = None
    for i, l in enumerate(lines):
        if l.strip().startswith('<section') and FAQ_TEXT in '\n'.join(lines[i:i+3]):
            faq_start = i
            for j in range(i + 1, len(lines)):
                if '</section>' in lines[j]:
                    faq_end = j
                    break
            break
    if cta_idx is None or faq_start is None or faq_end is None:
        skipped.append((p, 'block not found'))
        continue
    if cta_idx < faq_end:
        skipped.append((p, 'CTA already above FAQ'))
        continue

    faq_block = lines[faq_start:faq_end + 1]
    cta_block = [lines[cta_idx]]
    new_lines = lines[:faq_start] + cta_block + [''] + faq_block + lines[cta_idx + 1:]

    io.open(p, 'w', encoding='utf-8', newline='').write('\n'.join(new_lines))
    changed.append(p)

print('SWAPPED (%d):' % len(changed))
for p in changed: print('  ', p)
print('SKIPPED:', skipped if skipped else 'none')
