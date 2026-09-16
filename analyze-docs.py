# -*- coding: utf-8 -*-
"""Analyze concatenated documents: map copy boundaries via <body> tags,
score each copy, and identify which to keep."""
import re

def analyze(p):
    text = open(p, encoding="utf-8", errors="ignore").read()
    lines = text.splitlines(keepends=True)
    bodies = [i for i, l in enumerate(lines) if re.match(r'\s*<body>\s*$', l)]
    print(f"\n=== {p}: {len(lines)} lines, <body> at lines {[b+1 for b in bodies]} ===")
    segs = []
    for i, b in enumerate(bodies):
        start = b
        end = bodies[i+1] if i+1 < len(bodies) else len(lines)
        segs.append((start, end))
    best = None
    for i, (a, b) in enumerate(segs):
        head = "".join(lines[:a]) if i == 0 else ""
        chunk = "".join(lines[a:b])
        navs = chunk.count('<nav class="nav"')
        closes = chunk.count('</html>')
        hero = re.findall(r'<h1[^>]*>(.{0,60})', chunk)
        footers = chunk.count('<!-- Footer -->')
        score = (closes >= 1, footers, len(chunk))
        print(f"  copy {i+1}: lines {a+1}-{b} ({b-a} ln) navs={navs} footers={footers} "
              f"htmlClose={closes} h1={hero[:1]}")
        if best is None or score > best[0]:
            best = (score, i, a, b)
    print(f"  -> best copy: #{best[1]+1} (lines {best[2]+1}-{best[3]})")
    return lines, segs, best

for f in ["business/business.html", "features/features.html"]:
    analyze(f)
