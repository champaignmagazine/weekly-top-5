"""Align permanent item IDs (from the annotated master, book/volume.json) to elements of the captured post HTML."""
import json, re, sys
from bs4 import BeautifulSoup
V = json.load(open('/home/claude/top5/book/volume.json'))
def norm(s):
    s = re.sub(r'\[C\d+\]', '', s)
    return re.sub(r'[^a-z]', '', s.lower())
def btext(b): return ''.join(x.get('t', '') for x in b.get('r', []))
def id_blocks(part):
    out = []
    for b in part['blocks']:
        if b.get('id'): out.append((b['id'], btext(b), b['k']))
        if b.get('row_ids'):
            for i, row in zip(b['row_ids'], b['rows'][1:]):
                out.append((i, ' '.join(''.join(x.get('t', '') for x in c) for c in row), 'tr'))
    return out
def align(part, soup):
    els = [e for e in soup.find_all(['h1','h2','h3','h4','h5','h6','li','tr','p'])]
    keys = [norm(e.get_text(' ')) for e in els]
    res, j, miss = {}, 0, []
    for iid, t, k in id_blocks(part):
        n = norm(t)
        probe = n[:40] if len(n) >= 12 else n
        found = None
        for jj in range(j, len(els)):
            if probe and probe in keys[jj]:
                # prefer the innermost element: skip if a child li/p also contains it
                found = jj; break
        if found is None:
            for L in (25, 15):  # looser probe
                p2 = n[:L]
                for jj in range(j, len(els)):
                    if p2 and p2 in keys[jj]: found = jj; break
                if found is not None: break
        if found is None: miss.append(iid); continue
        res[iid] = found; j = found + 1
    return els, res, miss
if __name__ == '__main__':
    tot = mis = 0
    for c in V['chapters']:
        for p in c['parts']:
            if p['kind'] != 'post': continue
            soup = BeautifulSoup(open(f"/home/claude/top5/capture/html/{p['pid']}.html").read(), 'html.parser')
            els, res, miss = align(p, soup)
            n = len(id_blocks(p)); tot += n; mis += len(miss)
            if miss: print(p['id'], p['pid'], len(miss), '/', n, miss[:4])
    print('total', tot, 'missed', mis)
