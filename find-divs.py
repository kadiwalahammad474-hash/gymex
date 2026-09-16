# -*- coding: utf-8 -*-
"""Find and fix unbalanced <div> tags: locate unclosed div (stack-based) or stray close."""
import re, io, sys

FILES = [
    "aerobics/aerobics.html", "dance-studio/dance-studio.html", "expense-management/expense-management.html",
    "gym-management-software/gym-management-software.html", "health-and-fitness-centers/health-and-fitness-centers.html",
    "martial-arts-studio/martial-arts-studio.html", "pilates/pilates.html", "pt-studio/pt-studio.html",
    "sport-academies/sport-academies.html", "swim-school/swim-school.html", "task-management/task-management.html",
    "yoga-studio/yoga-studio.html",
]
ROOT = "C:/Users/Developer4/Desktop/gymexglobalwebsite/"

def tokens(s):
    # yield (kind, line) for div open/close; skip <script>/<style>/<pre> content
    out = []
    line = 1
    i = 0
    n = len(s)
    skip_depth = 0
    while i < n:
        c = s[i]
        if c == "\n": line += 1
        if s.startswith("<script", i) or s.startswith("<style", i) or s.startswith("<pre", i):
            end_tag = "</" + s[i+1:s.find(">", i)].split()[0] + ">"
            j = s.find(end_tag, i)
            # count newlines in skipped region
            line += s.count("\n", i, j)
            i = j
            continue
        if s.startswith("<!--", i):
            j = s.find("-->", i)
            line += s.count("\n", i, j)
            i = j
            continue
        if s.startswith("<div", i):
            out.append(("open", line))
            i = s.find(">", i) + 1
            continue
        if s.startswith("</div>", i):
            out.append(("close", line))
            i += 6
            continue
        i += 1
    return out

for rel in FILES:
    p = ROOT + rel
    s = io.open(p, encoding="utf-8").read()
    toks = tokens(s)
    stack = []
    stray = None
    for kind, line in toks:
        if kind == "open":
            stack.append(line)
        else:
            if stack: stack.pop()
            else:
                stray = line
                break
    o = sum(1 for k,_ in toks if k=="open"); c = sum(1 for k,_ in toks if k=="close")
    if o > c:
        # unclosed opens: report the earliest stack line that is likely a wrapper (before footer)
        print(f"{rel}: +{o-c} unclosed; unclosed opens at lines: {stack[:6]}")
    elif c > o:
        print(f"{rel}: {c-o} extra close; first stray close at line {stray}")
    else:
        print(f"{rel}: balanced?!")
