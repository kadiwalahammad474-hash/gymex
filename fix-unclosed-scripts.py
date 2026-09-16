# -*- coding: utf-8 -*-
"""Insert missing </script> closes: walk each page tracking inline-script state;
an external <script src=...> tag appearing INSIDE an unclosed inline script
means the previous block is missing its </script>."""
import os, re

pages = [f for f in os.listdir('.') if f.endswith('.html')]
for d in os.listdir('.'):
    if os.path.isdir(d) and not d.startswith('.'):
        pages += [os.path.join(d, f) for f in os.listdir(d) if f.endswith('.html')]

fixed = []
for p in sorted(set(pages)):
    lines = open(p, encoding='utf-8', errors='ignore').read().splitlines(keepends=True)
    out = []
    in_script = False
    changed = False
    for line in lines:
        if in_script and re.search(r'<script\s+src=', line):
            # unclosed inline script — close it before this external tag
            out.append('</script>\n')
            in_script = False
            changed = True
        out.append(line)
        # update state from the line just appended
        stripped = line
        if not in_script:
            m = re.search(r'<script(\s[^>]*)?>', stripped)
            if m:
                attrs = m.group(1) or ''
                if 'src=' not in attrs:
                    in_script = True
                    # inline open+close on same line?
                    if '</script>' in stripped[m.end():]:
                        in_script = False
                # external with close on same line: stays False
        else:
            if '</script>' in stripped:
                in_script = False
    if changed:
        open(p, 'w', encoding='utf-8', newline='').write(''.join(out))
        fixed.append(p)

print(f'fixed {len(fixed)} pages:')
for p in fixed:
    print(' ', p)
