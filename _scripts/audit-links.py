import os, re
from urllib.parse import urlparse, unquote

pages = []
existing = set()
for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in ('node_modules', '.git', '.vercel')]
    for f in files:
        p = os.path.normpath(os.path.join(root, f)).replace(os.sep, '/')
        existing.add(p.lower())
        if f.endswith('.html'):
            pages.append(p)

broken = {}
for page in pages:
    base = os.path.dirname(page)
    s = open(page, encoding='utf-8').read()
    hrefs = re.findall(r'(?:href|src)="([^"#]+)"', s)
    page_broken = set()
    for h in hrefs:
        h = h.strip()
        if not h or h.startswith(('http', 'mailto:', 'tel:', 'javascript:', 'data:', '//')):
            continue
        if h.endswith(('.css', '.js', '.ico', '.svg', '.png', '.jpg', '.jpeg', '.webp', '.gif', '.woff', '.woff2', '.json', '.xml', '.txt', '.webmanifest')):
            continue
        path = unquote(urlparse(h.replace('%20', ' ')).path)
        if not path:
            continue
        if path.startswith('/'):
            target = os.path.normpath('.' + path).replace(os.sep, '/')
        else:
            target = os.path.normpath(os.path.join(base, path)).replace(os.sep, '/')
        if target.lower() not in existing:
            page_broken.add(h)
    if page_broken:
        broken[page] = sorted(page_broken)

if broken:
    total = sum(len(v) for v in broken.values())
    print(f'BROKEN LINKS: {total} across {len(broken)} pages\n')
    for p, links in sorted(broken.items()):
        print(p + ':')
        for l in links:
            print('   ' + l)
else:
    print('ALL LINKS OK - koi broken link nahi')
print(f'\nScanned {len(pages)} pages')
