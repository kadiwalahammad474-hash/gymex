# -*- coding: utf-8 -*-
"""Remove the duplicate hamburger/backdrop toggle from script block 1 in
business/business.html. Block 1's demo-modal handlers target #demoModal
which does not exist on this page (page uses #divemailpopup), so the whole
conflicting block is dead code except its duplicate hamburger toggle that
breaks the menu. Script block 2 already handles backdrop + dropdowns."""
import re

p = "business/business.html"
s = open(p, encoding="utf-8").read()

# The conflicting block: <script> (function(){ var T=document.getElementById("menu-backdrop") ... })();
pattern = re.compile(
    r'<script>\s*\(function\(\)\{\s*var T=document\.getElementById\("menu-backdrop"\).*?\}\)\(\);\s*</script>',
    re.S,
)
m = pattern.search(s)
print("block found:", bool(m))
if m:
    s2 = s[:m.start()] + s[m.end():]
    open(p, "w", encoding="utf-8", newline="").write(s2)
    print(f"removed {m.end()-m.start()} bytes of duplicate/conflicting script")
# verify
s = open(p, encoding="utf-8").read()
print("backdrop scripts remaining:", s.count("var T=document.getElementById"))
print("dropdown toggle present:", s.count("menu.classList.toggle('show')"))
print("divemailpopup modal present:", s.count('id="divemailpopup"'))
