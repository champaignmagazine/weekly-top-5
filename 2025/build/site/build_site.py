"""Historical edition site for AI by AI Weekly Top 5: The 2025 Collection.

Inputs
  capture/html/<post_id>.html        posts as captured from the WordPress export, October 22, 2026
  book/volume.json                   annotated master: part metadata, permanent IDs, collection notes, reconstructed weeks
  book/ids_register.csv              register of permanent IDs
  labels/Historical_Edition_Labels_v1.1.csv   labels and review records
  proof/ch/<month>_meta.json         print codes of the concise edition, with the master IDs each draws on

Rules
  - Captured posts are reproduced as stored: the post HTML is kept, apart from making links open in a new tab and
    removing scripts. Nothing in the captured text is corrected.
  - Every annotation (permanent ID, label, review record, collection note, concise-edition link) sits in a box that is
    visually separate from the post text and is never merged into it.
  - The reconstructed weeks (January 1 to February 9) are shown, marked as reconstructed in October 2026, not historical.
"""
import csv, html, json, re, shutil, sys, pathlib
from collections import Counter, defaultdict
from datetime import date, timedelta
from bs4 import BeautifulSoup, Comment

ROOT = pathlib.Path('/home/claude/top5')
OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '/home/claude/weekly-top-5/2025/historical')
sys.path.insert(0, str(ROOT / 'hist'))
import align as A

V = A.V
REG = {r['id']: r for r in csv.DictReader(open(ROOT / 'book/ids_register.csv'))}
LAB = {r['id']: r for r in csv.DictReader(open(ROOT / 'labels/Historical_Edition_Labels_v1.1.csv'))}
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
CODES = defaultdict(list)
for m in MONTHS:
    for code, title, ids, sel in json.load(open(ROOT / f'proof/ch/{m.lower()}_meta.json'))['index']:
        for i in ids: CODES[i].append((code, m))
E = lambda s: html.escape(s or '', quote=True)

FAMILIES = [('Copilot', r'Copilot'), ('ChatGPT / GPT', r'\bChat ?GPT|^GPT|\bGPT-(?!.*Copilot)'), ('Grok', r'Grok'), ('Gemini', r'Gemini'),
            ('DeepSeek', r'DeepSeek'), ('Claude', r'Claude'), ('Kimi', r'Kimi'), ('Perplexity', r'Perplexity'), ('Qwen', r'Qwen'),
            ('Llama', r'Llama'), ('Quark', r'Quark')]
def families(c):
    fs = [f for f, rx in FAMILIES if re.search(rx, c)]
    if 'Copilot' in fs and re.search(r'GPT-5 \(via Copilot|Copilot Smart \(GPT-5', c): fs = ['Copilot']
    return fs or ['unattributed']

def week_dates(n):
    if n == 1: return date(2025, 1, 1), date(2025, 1, 5)
    if n == 53: return date(2025, 12, 29), date(2025, 12, 31)
    s = date(2025, 1, 6) + timedelta(days=7 * (n - 2)); return s, s + timedelta(days=6)
def span(n):
    a, b = week_dates(n)
    return f"{a:%B} {a.day}–{b.day}" if a.month == b.month else f"{a:%B} {a.day}–{b:%B} {b.day}"

LABEL_CLASS = {'outside its week': 'out', 'inaccurate as stated': 'inacc', 'no evidence found': 'noev', 'not an event': 'notev', 'unverified': 'unv'}
URL = re.compile(r'(https?://[^\s<>"\')\]]+[^\s<>"\')\].,;:])')
def linkify(s):
    out, last = [], 0
    for m in URL.finditer(s):
        out.append(E(s[last:m.start()])); u = m.group(1)
        out.append(f'<a href="{E(u)}" target="_blank" rel="noopener nofollow">{E(u)}</a>'); last = m.end()
    out.append(E(s[last:])); return ''.join(out)

def runs_html(rs, en):
    o = []
    for x in rs:
        if 'ref' in x:
            n = x['ref']; it = en[n - 1] if 0 < n <= len(en) else None
            if it: o.append(f'<a class="ref" href="{E(it["url"])}" target="_blank" rel="noopener nofollow" title="{E(it["label"])}">[link]</a>')
            continue
        t = E(re.sub(r'\s?\[C\d+\]', '', x.get('t', '')))
        if x.get('b'): t = f'<strong>{t}</strong>'
        if x.get('i'): t = f'<em>{t}</em>'
        o.append(t)
    return ''.join(o)

# ---------- collection notes: attach each note to the item whose text carries its marker -------------
def note_owner(part):
    owner, cur = {}, None
    for b in part['blocks']:
        if b.get('id'): cur = b['id']
        txt = A.btext(b) + ' '.join(''.join(x.get('t', '') for x in c) for row in b.get('rows', []) for c in row)
        for n in re.findall(r'\[C(\d+)\]', txt): owner.setdefault(int(n), cur)
    return owner

def annotation(iid, notes_for, en):
    r = REG.get(iid, {}); l = LAB.get(iid)
    role = r.get('role', 'list')
    chips = []
    if role != 'list':
        chips.append(f'<span class="chip role">{E(role)}</span>')
    elif l:
        labs = [x.strip() for x in l['labels'].split(';') if x.strip()]
        chips += [f'<span class="chip {LABEL_CLASS.get(x, "")}">{E(x)}</span>' for x in labs] or ['<span class="chip ok">confirmed</span>']
    codes = CODES.get(iid, [])
    if codes:
        chips.append('<span class="chip printed">printed: ' + ', '.join(
            f'<a href="../../concise/{m.lower()}.html#{c}">{c}</a>' for c, m in codes) + '</span>')
    det = []
    if l:
        rows = [('Findings', l['findings']), ('Review source', l['review_source']), ('Reviewer', l['reviewer']), ('Review date', l['review_date'])]
        if l['ext_reviewer']:
            rows += [('External review', f"{l['ext_reviewer']}: {l['ext_verdict']}" + (f" (proposed: {l['ext_label'] or 'confirmed'})" if l['ext_verdict'] == 'disagrees' else '')),
                     ('External source', l['ext_source']), ('External note', l['ext_note'])]
        if l['label_status']: rows.append(('Label status', l['label_status']))
        det = [f'<dt>{E(k)}</dt><dd>{linkify(v)}</dd>' for k, v in rows if v and v.strip()]
    for n in notes_for:
        det.append(f'<dt>Collection note {E(n["id"])}</dt><dd>{runs_html(n["r"], en)}</dd>')
    body = f'<details><summary>Review record</summary><dl>{"".join(det)}</dl></details>' if det else ''
    who = r.get('contributor', '')
    return (f'<aside class="annot" id="{E(iid)}" data-id="{E(iid)}"><div class="ahead"><a class="aid" href="#{E(iid)}">{E(iid)}</a>'
            f'<span class="who">{E(who)}</span>{"".join(chips)}</div>{body}</aside>')

def place(el, box, soup):
    frag = BeautifulSoup(box, 'html.parser')
    if el.name == 'li':
        el.append(frag)
    elif el.name == 'tr':
        n = len(el.find_all(['td', 'th'])) or 1
        tr = soup.new_tag('tr', attrs={'class': 'annot-row'}); td = soup.new_tag('td', attrs={'colspan': str(n)}); td.append(frag); tr.append(td)
        el.insert_after(tr)
    else:
        el.insert_after(frag)

def clean_capture(soup):
    for c in soup.find_all(string=lambda t: isinstance(t, Comment)): c.extract()
    for s in soup.find_all(['script', 'style']): s.decompose()
    for a in soup.find_all('a', href=True):
        a['target'] = '_blank'; a['rel'] = 'noopener nofollow'
    for f in soup.find_all('iframe'):
        src = f.get('src', ''); a = soup.new_tag('a', href=src, target='_blank', rel='noopener nofollow'); a.string = f'[embedded content: {src}]'; f.replace_with(a)
    for img in soup.find_all('img'): img['loading'] = 'lazy'

def render_blocks(blocks, en):
    o, inlist = [], None
    def close():
        nonlocal inlist
        if inlist: o.append(f'</{inlist}>'); inlist = None
    for b in blocks:
        k = b['k']; t = runs_html(b.get('r', []), en)
        if k == 'li':
            tag = 'ol' if b.get('ord') else 'ul'
            if inlist != tag: close(); o.append(f'<{tag}>'); inlist = tag
            o.append(f'<li class="lv{b.get("lv", 0)}" data-bid="{E(b.get("id", ""))}">{t}</li>')
            continue
        close()
        if k == 'h': lv = min(6, max(2, b.get('lv', 3))); o.append(f'<h{lv} data-bid="{E(b.get("id", ""))}">{t}</h{lv}>')
        elif k == 'q': o.append(f'<blockquote>{t}</blockquote>')
        elif k == 'table':
            rows = b['rows']; ids = b.get('row_ids') or []
            h = ''.join(f'<th>{runs_html(c, en)}</th>' for c in rows[0])
            body = ''.join(f'<tr data-bid="{E(ids[i] if i < len(ids) else "")}">' + ''.join(f'<td>{runs_html(c, en)}</td>' for c in r) + '</tr>' for i, r in enumerate(rows[1:]))
            o.append(f'<table><thead><tr>{h}</tr></thead><tbody>{body}</tbody></table>')
        else: o.append(f'<p data-bid="{E(b.get("id", ""))}">{t}</p>')
    close(); return '\n'.join(o)

# ---------- page shell ------------------------------------------------------------------------------------
CSS = open(ROOT / 'hist/style.css').read()
def page(title, body, depth=0, desc=''):
    up = '../' * depth
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{up}assets/style.css"></head><body>
<header class="site"><div class="wrap"><div class="brand"><a href="{up}../../index.html">AI by AI Weekly Top 5</a><span class="sep">·</span><a class="sub" href="{up}../index.html">The 2025 Collection</a><span class="sep">·</span><a class="sub" href="{up}index.html">Historical Edition</a></div>
<nav><a href="{up}index.html">Weeks</a><a href="{up}search.html">Search</a><a href="{up}register.html">Forecasts</a><a href="{up}about.html">About</a><a href="{up}../concise/index.html">Concise edition</a></nav></div></header>
<main class="wrap">{body}</main>
<footer class="site"><div class="wrap">Historical edition of <em>AI by AI Weekly Top 5: The 2025 Collection</em>, Series Volume 1. Edited by W.H.L., Champaign Magazine. Posts captured from champaignmagazine.com on October 22, 2026. Text and data CC BY 4.0; code MIT. <a href="https://github.com/champaignmagazine/weekly-top-5">Source on GitHub</a>.</div></footer>
</body></html>'''

def build():
    if OUT.exists(): shutil.rmtree(OUT)
    (OUT / 'weeks').mkdir(parents=True); (OUT / 'assets').mkdir(); (OUT / 'data').mkdir()
    (OUT / 'assets/style.css').write_text(CSS)
    shutil.copy(ROOT / 'hist/search.js', OUT / 'assets/search.js')
    weeks, items, problems = [], [], []
    parts = [(c, p) for c in V['chapters'] for p in c['parts']]
    for i, (c, p) in enumerate(parts):
        en = c['endnotes']; wk = int(p['id'][-2:]); a, b = week_dates(wk)
        owners = note_owner(p); notes_by = defaultdict(list); loose = []
        for n in p.get('notes', []):
            o = owners.get(n['n'])
            (notes_by[o] if o else loose).append(n)
        if p['kind'] in ('post', 'dec'):
            pid = p.get('pid') or 14515
            soup = BeautifulSoup(open(ROOT / f"capture/html/{pid}.html").read(), 'html.parser')
            els, res, miss = A.align(p, soup)
            if miss: problems.append((p['id'], miss))
            for iid, t, k in A.id_blocks(p):
                if iid in res: place(els[res[iid]], annotation(iid, notes_by.get(iid, []), en), soup)
            clean_capture(soup)
            content = str(soup)
            if p['kind'] == 'post':
                kind = 'Original post, as captured'
                head = (f'<p class="meta">Published {E(p["label"].split("Published ")[1].split(" ·")[0])} · Covers {E(p.get("covers", ""))} · '
                        f'Post {pid} · <a href="{E(p["url"])}" target="_blank" rel="noopener">live page</a></p>')
                banner = ''
            else:
                kind = 'Post of January 4, 2026, as captured'
                head = ('<p class="meta">Published Jan 4, 2026 · Covers December 29, 2025–January 4, 2026 · Post 14515 · '
                        '<a href="https://champaignmagazine.com/2026/01/04/ai-by-ai-weekly-top-5-december-29-2025-january-4-2026/" target="_blank" rel="noopener">live page</a></p>')
                banner = ('<div class="banner excerpt"><strong>Shared with the 2026 collection.</strong> This post covers December 29, 2025 to January 4, 2026. '
                          'Only its items dated December 29, 30 or 31, 2025, and the fact-checks that address them, belong to this collection; they carry 2025 IDs '
                          'and annotations. The rest of the post belongs to the 2026 collection.</div>')
        else:
            html_ = render_blocks(p['blocks'], en); soup = BeautifulSoup(html_, 'html.parser')
            for el in soup.find_all(attrs={'data-bid': True}):
                iid = el['data-bid']; del el['data-bid']
                if iid: place(el, annotation(iid, notes_by.get(iid, []), en), soup)
            content = str(soup)
            if p['kind'] == 'retro':
                kind = 'Reconstructed week'
                banner = ('<div class="banner recon"><strong>Reconstructed, not historical.</strong> The series began on February 17, 2025. '
                          'This week was reconstructed in October 2026 by four contributors working with the editor, for this volume. '
                          'It is not a post captured from the magazine’s website, and its selections were made with hindsight. '
                          f'{E(p["label"])}</div>')
            else:
                kind = 'Excerpts from the post of January 4, 2026'
                banner = f'<div class="banner excerpt">{E(p["label"])}</div>'
            head = ''
        intro = ''
        if p is c['parts'][0] and c.get('intro') and p['kind'] == 'retro':
            intro = f'<section class="cintro"><h3>{E(c["intro"]["label"])}</h3>{render_blocks(c["intro"]["blocks"], en)}</section>'
        loose_html = ''.join(f'<li id="{E(n["id"])}"><strong>{E(n["id"])}</strong> {runs_html(n["r"], en)}</li>' for n in loose)
        loose_html = f'<section class="cnotes"><h2>Collection notes on the post as a whole</h2><ul>{loose_html}</ul></section>' if loose_html else ''
        prev_ = parts[i - 1][1]['id'] if i else None; next_ = parts[i + 1][1]['id'] if i + 1 < len(parts) else None
        nav = ('<nav class="pn">' + (f'<a href="{prev_}.html">← {prev_}</a>' if prev_ else '<span></span>') +
               f'<a href="../index.html#{c["month"].lower()}">{c["month"]}</a>' + (f'<a href="{next_}.html">{next_} →</a>' if next_ else '<span></span>') + '</nav>')
        body = (f'{nav}<p class="kicker">{E(c["month"])} · Week {wk} · {span(wk)} · {E(kind)}</p><h1>{E(p["title"])}</h1>{head}{banner}{intro}'
                f'<div class="legend">The post is reproduced as captured, without corrections. Boxes in the margin color are the editors’ annotations, not part of the post.</div>'
                f'<article class="post {p["kind"]}">{content}</article>{loose_html}{nav}')
        (OUT / f'weeks/{p["id"]}.html').write_text(page(f'{p["id"]} · {p["title"]}', body, 1, f'{kind}: {p["title"]}'))
        n_items = 0
        for iid, t, k in A.id_blocks(p):
            r = REG.get(iid, {}); l = LAB.get(iid); n_items += 1
            labs = [x.strip() for x in (l['labels'] if l else '').split(';') if x.strip()]
            items.append({'id': iid, 'w': wk, 'm': c['month'], 'from': str(a), 'to': str(b), 'post': p['id'], 'kind': p['kind'],
                          'c': r.get('contributor', ''), 'f': families(r.get('contributor', '')), 'role': r.get('role', 'list'),
                          'title': re.sub(r'\s?\[C\d+\]', '', r.get('title', '')), 'text': re.sub(r'\s?\[C\d+\]', '', A.btext({'r': []}) or ''),
                          'labels': labs if r.get('role', 'list') == 'list' else [], 'codes': [x for x, _ in CODES.get(iid, [])]})
        weeks.append({'id': p['id'], 'w': wk, 'm': c['month'], 'title': p['title'], 'kind': p['kind'], 'span': span(wk), 'items': n_items,
                      'pub': (p['label'].split('Published ')[1].split(' ·')[0] if p['kind'] == 'post' else '')})
    # item text for search: the annotated master's item text, cut at 1,500 characters
    IT = json.load(open(ROOT / 'labels/itemtext.json'))
    for it in items: it['text'] = re.sub(r'\s?\[C\d+\]', '', IT.get(it['id'], ''))[:1500]
    (OUT / 'data/items.json').write_text(json.dumps(items, ensure_ascii=False, separators=(',', ':')))
    return weeks, items, problems

def index_pages(weeks, items):
    cnt = Counter(x for it in items if it['role'] == 'list' for x in (it['labels'] or ['confirmed']))
    sel = sum(1 for it in items if it['role'] == 'list')
    by = defaultdict(list)
    for w in weeks: by[w['m']].append(w)
    rows = []
    for m in MONTHS:
        rows.append(f'<h2 id="{m.lower()}">{m}</h2><ul class="weeks">')
        for w in by[m]:
            tag = {'retro': '<span class="chip recon">reconstructed</span>', 'dec': '<span class="chip excerpt">excerpts</span>'}.get(w['kind'], '')
            pub = f' · published {E(w["pub"])}' if w['pub'] else ''
            rows.append(f'<li><a href="weeks/{w["id"]}.html"><span class="wid">{w["id"]}</span> {E(w["span"])}</a>{tag}<span class="sub">{E(w["title"])}{pub} · {w["items"]} items</span></li>')
        rows.append('</ul>')
    legend = ''.join(f'<li><span class="chip {LABEL_CLASS.get(k, "ok")}">{E(k)}</span> {v}</li>' for k, v in sorted(cnt.items(), key=lambda kv: -kv[1]))
    body = f'''<p class="kicker">Series Volume 1 · Historical Edition</p><h1>AI by AI Weekly Top 5: The 2025 Collection</h1>
<p class="lede">Every 2025 post of the <em>AI by AI Weekly Top 5</em> column, as captured from <a href="https://champaignmagazine.com">champaignmagazine.com</a> on October 22, 2026, with each item under its permanent ID and the editors’ labels and review records kept beside the text, never in it.</p>
<div class="edn"><strong>Editorial note.</strong> To keep the posts as they were published, the historical edition does not edit them. Typos, misspellings, grammar, punctuation and capitalization are left as they appear in the captured posts, and so are errors of fact. The editors’ findings appear only in the annotations beside each item.</div>
<div class="two"><div>
<p>The panel’s own words are reproduced as published, including their errors. Where the editors found an item outside its week, inaccurate, without evidence, or not a single event, a dated label says so, with the record of what was checked, by whom and when. Items without a label were confirmed within the scope of the recorded review. The edited, fully checked selections are in the <a href="../concise/index.html">concise edition</a>.</p>
<p>January’s five weeks and the week of February 3–9 were reconstructed in October 2026 for this volume. They are included, marked as reconstructed, and are not historical posts.</p>
<p><a class="btn" href="search.html">Search by keyword, date, model or label</a> <a class="btn ghost" href="about.html">About this edition</a></p>
</div><div class="box"><h3>{sel} selections, labeled</h3><ul class="legend-list">{legend}</ul>
<p class="small">Fact-checks of another model’s list and instructions are kept with their posts but are not selections and carry no label.</p></div></div>
{''.join(rows)}'''
    (OUT / 'index.html').write_text(page('AI by AI Weekly Top 5: The 2025 Collection · Historical Edition', body, 0,
                                         'Every 2025 post as captured, with dated labels and review records kept separate from the text.'))
    fam = sorted({f for it in items for f in it['f']})
    opts_m = ''.join(f'<option>{m}</option>' for m in MONTHS)
    opts_f = ''.join(f'<option>{E(f)}</option>' for f in fam)
    opts_l = ''.join(f'<option value="{E(k)}">{E(k)}</option>' for k in ['confirmed', 'outside its week', 'inaccurate as stated', 'no evidence found', 'not an event', 'unverified'])
    body = f'''<h1>Search the historical edition</h1>
<form id="sf" class="search" onsubmit="return false"><input id="q" type="search" placeholder="Keyword or phrase, e.g. Stargate, “open weights”, 2025-W36" autocomplete="off">
<div class="filters"><label>Month<select id="m"><option value="">All</option>{opts_m}</select></label>
<label>From<input id="d1" type="date" min="2025-01-01" max="2025-12-31"></label><label>To<input id="d2" type="date" min="2025-01-01" max="2025-12-31"></label>
<label>Model family<select id="f"><option value="">All</option>{opts_f}</select></label>
<label>Label<select id="l"><option value="">All</option>{opts_l}<option value="labeled">any label</option></select></label>
<label>Items<select id="r"><option value="list">Selections</option><option value="">All items</option><option value="fact-check (not a selection)">Fact-checks</option></select></label>
<label class="cb"><input id="x" type="checkbox"> Include reconstructed weeks</label></div></form>
<p id="count" class="small"></p><ol id="res" class="results"></ol>
<script src="assets/search.js"></script>'''
    (OUT / 'search.html').write_text(page('Search · Historical Edition', body, 0, 'Search the 2025 posts by keyword, date, model family and label.'))
    about = open(ROOT / 'hist/about.html').read()
    (OUT / 'about.html').write_text(page('About · Historical Edition', about, 0, 'How the historical edition was made.'))

if __name__ == '__main__':
    weeks, items, problems = build(); index_pages(weeks, items)
    for f in ['Historical_Edition_Labels_v1.1.csv']: shutil.copy(ROOT / 'labels' / f, OUT / 'data' / f)
    shutil.copy(ROOT / 'book/ids_register.csv', OUT / 'data/Item_Register_2025.csv')
    shutil.copy(ROOT / 'top5_2025_captured_posts.zip', OUT / 'data/Captured_Posts_2026-10-22.zip')
    print('weeks', len(weeks), 'items', len(items), 'alignment problems', problems)
