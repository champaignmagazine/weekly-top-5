"""Forecast register v2.2: step 6 (source attribution) merged from the two frozen halves, with the cross-check
decisions, GPT-6 Astra's document-access records for Claude's half, and two corrections. Every change is logged.

Inputs (all frozen or returned files, unchanged):
  Forecast_Claims_v2.csv                                v2.1 register
  step6/Attribution_Worksheet_Claude_FROZEN.csv         Claude's half (February-July posts)
  step6/Attribution_Worksheet_GPT_FROZEN.csv            GPT-6 Astra's half (August-December posts)
  ../../../handoff/gpt_step6_return/Claude_163_Document_Access.csv   GPT-6 Astra's access check of Claude's documents
"""
import csv, json, re
from collections import Counter
H = '/home/claude/top5'
V = list(csv.DictReader(open('Forecast_Claims_v2.csv'))); F = list(V[0].keys())
def load(p): return {r['cid']: r for r in csv.DictReader(open(p))}
C = load('step6/Attribution_Worksheet_Claude_FROZEN.csv'); G = load('step6/Attribution_Worksheet_GPT_FROZEN.csv')
ACC = load(f'{H}/handoff/gpt_step6_return/Claude_163_Document_Access.csv')
k = lambda r, i: list(r.values())[13 + i]   # the six step-6 fields, by position
NEW = ['attributed_to', 'attribution_basis', 'supporting_document', 'document_opened', 'document_supports',
       'attribution_note', 'attribution_by', 'attribution_correction']
log = []
def L(cid, field, old, new, why): log.append({'cid': cid, 'field': field, 'old': old, 'new': new, 'reason': why})

# Decisions on the cross-check differences (Claude, November 5; editor may overrule)
DEC = {
 'FR-0038': {'attributed_to': '', 'attribution_basis': 'post source',
             'note': 'Unnamed: X accounts linked in the post (ScooterJMiller; mammenthoms) speculate on an Arm merger. The New York Times is the source of the acquisition report, not of the speculation. Account posts could not be retrieved.'},
 'FR-0102': {'attribution_basis': 'post source', 'note': 'The table sentence says only "report"; the surrounding item names the AI Futures Project.'},
 'FR-0136': {'attributed_to': '', 'attribution_basis': 'none', 'voice': 'attributed',
             'note': 'Unnamed: reports and speculation about DeepSeek-R2; they do not establish that DeepSeek made the forecast.'},
 'FR-0228': {'attributed_to': 'ACLU (as the post states)',
             'correction': 'The Markey release of June 4, 2025 attributes the quoted civil-rights warning to Damon Hewitt of the Lawyers’ Committee for Civil Rights Under Law; ACLU counsel Cody Venzke gives a related but different warning in the same release. The post’s wording is kept as published.'},
 'FR-0313': {'note': 'Inference only: the conferences’ organizers. Not recorded as an attribution because the post names no announcing organization.'},
 'FR-0534': {'note': 'Nature is the cited publication; the feature’s author or quoted experts are not identified, so no forecaster is recorded.'},
}
CORR = {'FR-0738': ('paraphrase', 'OpenAI projected cash burn of about $115 billion through 2029 (as reported in a TechCrunch interview with Karen Hao, September 14, 2025)',
                    'GPT-6 Astra, step 6: the cited interview attributes the projection to OpenAI and describes cash burn through 2029; the earlier paraphrase was too broad. The captured quotation is unchanged.')}

out, cnt = [], Counter()
for r in V:
    cid = r['cid']; src = C.get(cid) or G.get(cid); half = 'Claude Opus 5.5' if cid in C else ('GPT-6 Astra' if cid in G else '')
    for f in NEW: r[f] = ''
    if src:
        a, b, d, o, s, n = (k(src, i) for i in range(6))
        if half.startswith('Claude') and a.startswith('('):          # convention 1: unnamed sources
            n = ('Unnamed: ' + a.strip('()') + ('. ' + n if n else '')).strip(); L(cid, 'attributed_to', a, '', 'convention: unnamed source moved to the note'); a = ''
        if r['voice'] == 'panel' and b != 'n.a. (panel’s own view)':  # convention 2: panel rows
            L(cid, 'attribution_basis', b, 'n.a. (panel’s own view)', 'convention: panel rows'); b = 'n.a. (panel’s own view)'
        if half.startswith('GPT') and r['voice'] != 'panel' and not a and n and not n.startswith('Unnamed') and re.search(r'[Uu]nspecified|[Nn]o (individual|identifiable)', n):
            n = 'Unnamed: ' + n
        if cid in ACC:                                                # GPT-6 Astra's access check of Claude's documents
            x = ACC[cid]; L(cid, 'document_opened/supports', f'{o}/{s}', f"{x['document_opened']}/{x['document_supports']}", 'GPT-6 Astra access check, November 5')
            o, s = x['document_opened'], x['document_supports']; n = (n + (' ' if n else '') + f"[Access check, GPT-6 Astra: {x['note']}]").strip()
        r.update(attributed_to=a, attribution_basis=b, supporting_document=d, document_opened=o, document_supports=s, attribution_note=n,
                 attribution_by=half + (' (documents: GPT-6 Astra)' if cid in ACC else ''))
        if cid in DEC:
            dd = DEC[cid]
            for f, v in [('attributed_to', dd.get('attributed_to')), ('attribution_basis', dd.get('attribution_basis')), ('voice', dd.get('voice'))]:
                if v is not None and r[f] != v: L(cid, f, r[f], v, 'cross-check decision, November 5'); r[f] = v
            if 'note' in dd: r['attribution_note'] = (dd['note'] + ' ' + r['attribution_note']).strip()
            if 'correction' in dd: r['attribution_correction'] = dd['correction']; L(cid, 'attribution_correction', '', dd['correction'], 'document check, GPT-6 Astra')
        cnt[half] += 1
    elif r['status'] == 'claim' and r['family']:
        r['attribution_by'] = 'story family (v2.1 source_attribution)'
    if cid in CORR:
        f, v, why = CORR[cid]; L(cid, f, r[f], v, why); r[f] = v
    out.append(r)
FF = F + NEW
w = csv.DictWriter(open('Forecast_Claims_v2.2.csv', 'w', newline=''), fieldnames=FF); w.writeheader(); w.writerows(out)
w = csv.DictWriter(open('Change_log_v2.2.csv', 'w', newline=''), fieldnames=['cid', 'field', 'old', 'new', 'reason']); w.writeheader(); w.writerows(log)
ret = [r for r in out if r['status'] == 'claim']
fam = [r for r in ret if r['family']]; nf = [r for r in ret if not r['family']]
st = {
 'records': len(out), 'claims': len(ret), 'in_families': len(fam), 'outside_families': len(nf),
 'outside_families_with_v2_1_source_attribution': sum(1 for r in nf if r['source_attribution'].strip()),
 'outside_families_attributed_in_step6': sum(1 for r in nf if r['attribution_by']),
 'by_half': dict(cnt),
 'voice': dict(Counter(r['voice'] for r in nf)),
 'basis': dict(Counter(r['attribution_basis'] for r in nf)),
 'named_attribution_nonpanel': sum(1 for r in nf if r['voice'] != 'panel' and r['attributed_to']),
 'unnamed_nonpanel': sum(1 for r in nf if r['voice'] != 'panel' and not r['attributed_to']),
 'document_opened': dict(Counter(r['document_opened'] for r in nf)),
 'document_supports_when_opened': dict(Counter(r['document_supports'] for r in nf if r['document_opened'] == 'yes')),
 'by_half_opened': {h: dict(Counter(r['document_opened'] for r in nf if r['attribution_by'].startswith(h))) for h in ('Claude', 'GPT')},
 'changes_logged': len(log),
}
json.dump(st, open('stats_v2.2.json', 'w'), indent=1)
print(json.dumps(st, indent=1))
