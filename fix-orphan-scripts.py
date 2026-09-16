# -*- coding: utf-8 -*-
"""Fix orphan `<script>\\s*<script>` left by dedupe — browser treats inner <script>
as JS text -> SyntaxError -> burger/dropdown handlers never attach."""
import re, os

pages = [f for f in os.listdir('.') if f.endswith('.html')]
for d in os.listdir('.'):
    if os.path.isdir(d) and not d.startswith('.'):
        pages += [os.path.join(d, f) for f in os.listdir(d) if f.endswith('.html')]

fixed = []
for p in pages:
    s = open(p, encoding='utf-8', errors='ignore').read()
    orig = s
    # orphan nested: <script> whitespace <script>  ->  single <script>
    s = re.sub(r'<script>\s*<script>', '<script>', s)
    if s != orig:
        open(p, 'w', encoding='utf-8', newline='').write(s)
        fixed.append(p)

print(f'fixed {len(fixed)} pages:')
for p in fixed:
    print(' ', p)

# verify none remain
remaining = 0
for p in pages:
    s = open(p, encoding='utf-8', errors='ignore').read()
    remaining += len(re.findall(r'<script>\s*<script>', s))
print('orphan-nested remaining:', remaining)
