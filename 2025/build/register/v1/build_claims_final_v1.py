"""v1 final build step (restored November 5, 2026): claims_v1.json -> Forecast_Claims_v1.csv and Assessable_by_2026_v1.csv.

Inputs: claims_v1.json (from build_claims.py), assess_v1.txt (resolvable propositions by group),
duplicate_groups_v1.txt (candidate overlap groups, assigned by hand), labels v0.8 (item labels as of October 29).
Writes to the directory given as the first argument (default: current), so the frozen files can be compared.
"""
import csv, json, sys, os
out = sys.argv[1] if len(sys.argv) > 1 else '.'
J = json.load(open('claims_v1.json'))
A = {}
for l in open('assess_v1.txt'):
    if l.startswith('#') or not l.strip(): continue
    p = [x.strip() for x in l.split('|')]; A[p[0]] = p[1:5]
D = {}
for l in open('duplicate_groups_v1.txt'):
    if l.startswith('#') or not l.strip(): continue
    c, g = [x.strip() for x in l.split('|')]; D[c] = g
LR = list(csv.DictReader(open('/home/claude/top5/labels/Historical_Edition_Labels_v0.8.csv'))); LAB = {r['id']: r['labels'] for r in LR}
F = ['cid', 'rid', 'split', 'published', 'wp_post', 'item', 'speaker', 'type', 'voice', 'final_code', 'claim_text', 'due_status',
     'assessable_by_2026_12_31', 'group', 'deadline', 'proposition', 'source', 'factual_flag', 'possible_duplicate_group']
rows = []
for j in J:
    r = {k: j[k] for k in F[:11]}
    if j['cid'] in A:
        r['due_status'], r['assessable_by_2026_12_31'] = 'due by end-2026', 'Y'
        r['group'], r['deadline'], r['proposition'], r['source'] = A[j['cid']]
    else:
        r['due_status'], r['assessable_by_2026_12_31'] = ('not yet due (later year)', 'N: later year') if j['later_year'] else ('open-ended / no resolvable deadline', 'N')
        r['group'] = r['deadline'] = r['proposition'] = r['source'] = ''
    lab = LAB.get(j['item'], '')
    r['factual_flag'] = f'item labelled: {lab}' if lab else ''
    r['possible_duplicate_group'] = D.get(j['cid'], '')
    rows.append(r)
with open(os.path.join(out, 'Forecast_Claims_v1.csv'), 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=F); w.writeheader(); w.writerows(rows)
groups = {}
for r in rows:
    if r['group']: groups.setdefault(r['group'], []).append(r)
G = ['group', 'deadline', 'proposition', 'source', 'type', 'voice', 'occurrences', 'claim_ids', 'speakers', 'items', 'first_published', 'factual_flags']
with open(os.path.join(out, 'Assessable_by_2026_v1.csv'), 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=G); w.writeheader()
    for g in sorted(groups):
        rs = groups[g]; first = rs[0]
        u = lambda k: ';'.join(sorted({r[k] for r in rs if r[k]}))
        w.writerow({'group': g, 'deadline': first['deadline'], 'proposition': first['proposition'], 'source': first['source'],
                    'type': first['type'], 'voice': first['voice'], 'occurrences': len(rs), 'claim_ids': ';'.join(r['cid'] for r in rs),
                    'speakers': u('speaker'), 'items': u('item'), 'first_published': min(r['published'] for r in rs),
                    'factual_flags': ';'.join(sorted({r['factual_flag'].replace('item labelled: ', '') for r in rs if r['factual_flag']}))})
