"""Forecast register page for the historical edition: register.html (searchable), scoring-rules.html, data files.
The register is shown as recorded; no outcome is scored or implied."""
import csv, json, html, re, shutil, sys, pathlib
import markdown
ROOT = pathlib.Path('/home/claude/top5'); RG = ROOT / 'forecast/reconcile/v2'
OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '/home/claude/weekly-top-5/2025/historical')
sys.path.insert(0, str(ROOT / 'hist'))
import build_site as B
E = lambda s: html.escape(s or '', quote=True)
V = json.load(open(ROOT / 'book/volume.json'))
PID = {str(p.get('pid')): p['id'] for c in V['chapters'] for p in c['parts'] if p.get('pid')}
PID['14515'] = '2025-W53'
R = list(csv.DictReader(open(RG / 'Forecast_Claims_v2.2.csv')))
rows = []
for r in R:
    post = r['occurrence_id'][:8] if r['occurrence_id'] else PID.get(r['wp_post'], '')
    rows.append({'cid': r['cid'], 'st': r['status'], 'role': r['role'], 'orig': r['original_occurrence'], 'fam': r['family'],
                 'pub': r['published'], 'post': post, 'occ': r['occurrence_id'], 'sp': r['speaker'], 'type': r['type'], 'voice': r['voice'],
                 'q': r['quote'][:1200], 'para': r['paraphrase'], 'mod': r['modality'], 'cond': r['condition'], 'time': r['time_expression'],
                 'dl_basis': r['deadline_basis'], 'horizon': r['horizon_status'], 'meas': r['measurability'],
                 'to': r['attributed_to'] or (r['source_attribution'] if r['family'] else ''), 'basis': r['attribution_basis'],
                 'doc': r['supporting_document'], 'opened': r['document_opened'], 'supports': r['document_supports'],
                 'note': r['attribution_note'], 'corr': r['attribution_correction'], 'flag': r['factual_flag'], 'rnote': r['review_note']})
(OUT / 'data').mkdir(parents=True, exist_ok=True)
(OUT / 'data/forecast_register.json').write_text(json.dumps(rows, ensure_ascii=False, separators=(',', ':')))
for f in ['Forecast_Claims_v2.2.csv', 'Change_log_v2.2.csv', 'Forecast_Claims_2026_post_v2.2.csv']: shutil.copy(RG / f, OUT / 'data' / f)
ret = [r for r in R if r['status'] == 'claim']
cnt = lambda k: {}
types = {t: sum(1 for r in ret if r['type'] == t) for t in ('plan', 'expectation', 'possibility')}
voices = {v: sum(1 for r in ret if r['voice'] == v) for v in ('panel', 'actor (reported)', 'attributed')}
body = f'''<div class="prose"><p class="kicker">Historical edition · Forecast register v2.2</p><h1>What the 2025 panel said about the future</h1>
<p class="lede">A dated record of the forward-looking statements in the 2025 posts: {len(ret)} claims from the 46 posts, each with its exact wording, who said it and when, and any time it gave.</p>
<div class="edn"><strong>No outcomes yet.</strong> This register records what was said, not whether it came true. The claims will be scored in the next volume, against evidence through December 31, 2026, under <a href="scoring-rules.html">rules fixed in advance</a>. Nothing here is a verdict.</div>
<p>Both compilers, Claude Opus 5.5 and GPT-6 Astra, extracted the forward-looking passages independently and reconciled their lists. Each claim records:</p>
<ul>
<li>its <strong>type</strong>: a plan reported for a company or government, an expectation, or a bare possibility (“could”, “may”);</li>
<li>its <strong>voice</strong>: the panel’s own view, an actor’s reported plan, or a third party’s statement;</li>
<li>any <strong>condition and deadline</strong> as the post gave them;</li>
<li>its <strong>source attribution</strong>: who the post says made the claim, on what basis, and whether the document it cites supports that attribution.</li>
</ul>
<p>A name in the attribution does not mean a source supports it; a separate field records that. Some attributions in the posts are wrong. Where a document shows a different originator, a correction is recorded beside the post’s wording, which is kept as published.</p>
<p>The register is separate from the propositions in the volume’s two introductions, which each author wrote independently.</p>
<div class="two"><div class="box"><h3>Claims by type</h3><ul class="legend-list">{''.join(f'<li>{E(k)} <span>{v}</span></li>' for k, v in types.items())}</ul></div>
<div class="box"><h3>By voice</h3><ul class="legend-list">{''.join(f'<li>{E(k)} <span>{v}</span></li>' for k, v in voices.items())}</ul></div></div>
<p class="small">Data: <a href="data/Forecast_Claims_v2.2.csv">register (CSV, v2.2)</a> · <a href="data/Change_log_v2.2.csv">change log</a> · <a href="data/Forecast_Claims_2026_post_v2.2.csv">the January 4, 2026 post’s claim</a> · <a href="scoring-rules.html">scoring rules v1.0</a></p></div>
<h2>Search the register</h2>
<form class="search" onsubmit="return false"><input id="q" type="search" placeholder="Keyword or phrase, e.g. Stargate, “by 2030”, Amodei" autocomplete="off">
<div class="filters"><label>Type<select id="t"><option value="">All</option><option>plan</option><option>expectation</option><option>possibility</option></select></label>
<label>Voice<select id="v"><option value="">All</option><option value="panel">panel’s own view</option><option>actor (reported)</option><option>attributed</option></select></label>
<label>Horizon<select id="h"><option value="">All</option><option>due by end-2026</option><option>not yet due (later year)</option><option>open-ended</option></select></label>
<label>Source document<select id="d"><option value="">All</option><option value="yes">opened</option><option value="supports">supports the attribution</option><option value="no">does not support it</option></select></label>
<label class="cb"><input id="o" type="checkbox" checked> Original occurrences only</label></div></form>
<p id="count" class="small"></p><ol id="res" class="results reg"></ol>
<script src="assets/register.js"></script>'''
(OUT / 'register.html').write_text(B.page('Forecast Register · Historical Edition', body, 0, 'What the 2025 panel said about the future, with attribution and no outcomes.'))
md = (RG / 'Scoring_Conventions_v1.0.md').read_text()
(OUT / 'scoring-rules.html').write_text(B.page('Scoring Rules · Historical Edition', '<div class="prose">' + markdown.markdown(md) + '<p><a href="register.html">← Forecast register</a></p></div>', 0, 'How the 2025 panel’s forecasts will be scored.'))
shutil.copy(ROOT / 'hist/register.js', OUT / 'assets/register.js')
print('register rows', len(rows))
