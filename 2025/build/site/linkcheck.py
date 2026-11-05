import pathlib, re, sys
from urllib.parse import urlparse, unquote
R = pathlib.Path(sys.argv[1]); ids = {}; bad = []; n = 0
for f in R.rglob('*.html'):
    ids[f.resolve()] = set(re.findall(r'\sid="([^"]+)"', f.read_text()))
for f in R.rglob('*.html'):
    for h in re.findall(r'href="([^"]+)"', f.read_text()):
        if re.match(r'(https?:|mailto:)', h) or h.startswith('//'): continue
        n += 1; path, _, frag = h.partition('#')
        t = (f.parent / unquote(path)).resolve() if path else f.resolve()
        if not t.exists(): bad.append((str(f.relative_to(R)), h)); continue
        if frag and t.suffix == '.html' and frag not in ids.get(t.resolve(), set()): bad.append((str(f.relative_to(R)), h))
print('internal links', n, 'broken', len(bad))
from collections import Counter
print(Counter(b[1].split('#')[0].split('/')[-1] for b in bad).most_common(8)); print(bad[:8])
