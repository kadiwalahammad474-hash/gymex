# -*- coding: utf-8 -*-
"""Fix captcha scripts truncated at top by dedupe — they start mid-function
missing `function validateCaptcha() {` + variable init lines."""
import re, os

HEADER = ('<script>\n'
          'function validateCaptcha() {\n'
          '  var userInput = document.getElementById("captcha-input") ? document.getElementById("captcha-input").value : "";\n'
          '  var currentCaptcha = (typeof window.currentCaptcha !== "undefined") ? window.currentCaptcha : "";\n'
          '  if (userInput !== currentCaptcha) {')

pages = [f for f in os.listdir('.') if f.endswith('.html')]
for d in os.listdir('.'):
    if os.path.isdir(d) and not d.startswith('.'):
        pages += [os.path.join(d, f) for f in os.listdir(d) if f.endswith('.html')]

fixed = []
for p in pages:
    s = open(p, encoding='utf-8', errors='ignore').read()
    orig = s
    # script opening directly into mid-function `if (userInput` — missing header
    s = re.sub(r'<script>\s*\n\s*if \(userInput !== currentCaptcha\) \{', HEADER, s)
    if s != orig:
        open(p, 'w', encoding='utf-8', newline='').write(s)
        fixed.append(p)

print(f'fixed {len(fixed)} pages:')
for p in fixed:
    print(' ', p)

# verify: no page has a script starting mid-function
remaining = 0
for p in pages:
    s = open(p, encoding='utf-8', errors='ignore').read()
    remaining += len(re.findall(r'<script>\s*\n\s*if \(userInput', s))
print('truncated captcha scripts remaining:', remaining)
