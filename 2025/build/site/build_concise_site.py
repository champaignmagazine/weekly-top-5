"""Online concise edition: the same text as the PDF, from the same sources, as web pages.

Front matter comes from build_proof.build_front (the PDF's own HTML, unwrapped from its print page);
chapters come from proof/ch/<Month>.html (the print chapters). Entries get anchors by print code and links to
the master IDs in the historical edition. Page numbers belong to the PDF and are not shown; the keyword index
is replaced by search.
"""
import html, json, re, shutil, sys, pathlib
ROOT = pathlib.Path('/home/claude/top5'); P = ROOT / 'proof'
OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '/home/claude/weekly-top-5/2025/concise')
PDF = sys.argv[2] if len(sys.argv) > 2 else None
E = lambda s: html.escape(s or '', quote=True)
MONTHS = 'January February March April May June July August September October November December'.split()

src = (P / 'build_proof.py').read_text()
src = src[:src.rindex('main(); build_kw(); main()')]
NS = {'__file__': str(P / 'build_proof.py'), '__name__': 'bp'}
exec(compile(src, 'build_proof.py', 'exec'), NS)

def body_of(doc):
    b = re.search(r'<body>(.*)</body>', doc, re.S).group(1)
    return re.sub(r'\sstyle="[^"]*"', '', b)

FRONT = [('series-preface', 'fm05_series', 'Series Preface'), ('volume-preface', 'fm06_pref', 'Volume Preface'),
         ('introduction-1', 'fm08_intro_gpt', 'AI in 2025: Capability, Access and Consequence'),
         ('introduction-2', 'fm09_outline', '2025 in Outline'), ('how-to-read', 'fm10_howread', 'How to Read This Book'),
         ('how-made', 'fm11_howmade', 'How the Volume Was Made'), ('disclosure', 'fm12_disclosure', 'Disclosure')]

CSS = (ROOT / 'hist/style.css').read_text() + (ROOT / 'hist/concise.css').read_text()
def page(title, body, depth=0, desc=''):
    up = '../' * depth
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{up}assets/style.css"></head><body class="concise">
<header class="site"><div class="wrap"><div class="brand"><a href="{up}../../index.html">AI by AI Weekly Top 5</a><span class="sep">·</span><a class="sub" href="{up}../index.html">The 2025 Collection</a><span class="sep">·</span><a class="sub" href="{up}index.html">Concise Edition</a></div>
<nav><a href="{up}index.html">Contents</a><a href="{up}search.html">Search</a><a href="{up}../historical/index.html">Historical edition</a></nav></div></header>
<main class="wrap">{body}</main>
<footer class="site"><div class="wrap">Concise edition of <em>AI by AI Weekly Top 5: The 2025 Collection</em>, Series Volume 1. Edited by W.H.L., Champaign Magazine, November 2026. Text and data CC BY 4.0; code MIT. <a href="https://github.com/champaignmagazine/weekly-top-5">Source on GitHub</a>.</div></footer>
</body></html>'''

def build():
    if OUT.exists(): shutil.rmtree(OUT)
    (OUT / 'assets').mkdir(parents=True); (OUT / 'data').mkdir()
    (OUT / 'assets/style.css').write_text(CSS); shutil.copy(ROOT / 'hist/concise_search.js', OUT / 'assets/search.js')
    pages = dict(NS['build_front']([]))
    toc_front = []
    order = [f[0] for f in FRONT] + [m.lower() for m in MONTHS] + ['edit-log', 'forecast-register', 'print-codes']
    titles = {f[0]: f[2] for f in FRONT}; titles.update({m.lower(): f'{m} 2025' for m in MONTHS})
    titles.update({'edit-log': 'Appendix A: Edit Log', 'forecast-register': 'Appendix B: Forecast Register', 'print-codes': 'Index of Print Codes'})
    def pn(slug):
        i = order.index(slug)
        a = f'<a href="{order[i-1]}.html">← {E(titles[order[i-1]])}</a>' if i else '<a href="index.html">← Contents</a>'
        b = f'<a href="{order[i+1]}.html">{E(titles[order[i+1]])} →</a>' if i + 1 < len(order) else '<span></span>'
        return f'<nav class="pn">{a}<a href="index.html">Contents</a>{b}</nav>'
    for slug, key, title in FRONT:
        b = body_of(pages[key])
        b = b.replace('<span class="pre">', '<span class="pre kicker">')
        (OUT / f'{slug}.html').write_text(page(title, pn(slug) + f'<div class="fm">{b}</div>' + pn(slug), 0, title))
    entries = []
    for m in MONTHS:
        meta = json.load(open(P / f'ch/{m.lower()}_meta.json'))
        ids = {code: i for code, t, i, s in meta['index']}
        b = body_of((P / f'ch/{m}.html').read_text())
        def art(mo):
            a = mo.group(0); code = re.search(r'class="code">(P-2025-W\d\d-\d\d)', a).group(1)
            links = ', '.join(f'<a href="../historical/weeks/{x[:8]}.html#{x}">{x}</a>' for x in ids.get(code, []) if re.match(r'2025-W\d\d-', x))
            a = a.replace('<article>', f'<article id="{code}">', 1)
            a = a.replace(f'<div class="code">{code}</div>', f'<div class="code"><a href="#{code}">{code}</a></div>', 1)
            a = a.replace('</div></div>\n</article>', f'</div><div class="hist">In the historical edition: {links}</div></div>\n</article>') if links else a
            text = re.sub(r'<sup.*?</sup>', '', a); text = re.sub(r'<[^>]+>', ' ', text); text = html.unescape(re.sub(r'\s+', ' ', text)).strip()
            t = re.search(r'<h3>(.*?)</h3>', a, re.S).group(1); dl = re.search(r'class="dateline">(.*?)</div>', a, re.S).group(1)
            sel = re.search(r'class="sel">(.*?)</div>', a, re.S)
            entries.append({'code': code, 'm': m, 'title': html.unescape(re.sub(r'<[^>]+>', '', t)), 'date': html.unescape(dl),
                            'sel': html.unescape(sel.group(1)).replace('Selected by ', '') if sel else '', 'ids': ids.get(code, []), 'text': text[:1800]})
            return a
        b = re.sub(r'<article>.*?</article>', art, b, flags=re.S)
        b = re.sub(r'<a class="url" href', '<a class="url" target="_blank" rel="noopener" href', b)
        (OUT / f'{m.lower()}.html').write_text(page(f'{m} 2025 · Concise Edition', pn(m.lower()) + f'<div class="chapter">{b}</div>' + pn(m.lower()), 0, f'{m} 2025'))
    # appendices
    el = (ROOT / 'print/Edit_Log_2025_v0.1.md').read_text(); t, bb = NS['strip_head'](el)
    (OUT / 'edit-log.html').write_text(page('Appendix A: Edit Log', pn('edit-log') + f'<div class="fm"><section class="piece"><h1>Appendix A: Edit Log</h1>{NS["md"](bb)}</section></div>' + pn('edit-log')))
    t, bb = NS['strip_head']((P / 'src/Appendix_Forecast_register_back_matter_.md').read_text())
    (OUT / 'forecast-register.html').write_text(page('Appendix B: Forecast Register', pn('forecast-register') + f'<div class="fm"><section class="piece"><h1>Appendix B: Forecast Register</h1>{NS["md"](bb)}</section></div>' + pn('forecast-register')))
    rows = []
    for m in MONTHS:
        rows.append(f'<tr class="grp"><td colspan="4">{m}</td></tr>')
        for e in [x for x in entries if x['m'] == m]:
            hid = ', '.join(f'<a href="../historical/weeks/{x[:8]}.html#{x}">{x}</a>' for x in e['ids'] if re.match(r'2025-W\d\d-', x)) or ', '.join(E(x) for x in e['ids'])
            rows.append(f'<tr><td class="c"><a href="{m.lower()}.html#{e["code"]}">{e["code"]}</a></td><td class="d">{E(e["date"])}</td><td>{E(e["title"])}</td><td class="i">{hid}</td></tr>')
    (OUT / 'print-codes.html').write_text(page('Index of Print Codes', pn('print-codes') + '<h1>Index of Print Codes</h1><p class="small">Every printed entry, with the master IDs in the historical edition that it draws on. ' + str(len(entries)) + ' entries.</p><div class="tscroll"><table class="ix"><thead><tr><th>Code</th><th>Date</th><th>Entry</th><th>Historical edition</th></tr></thead><tbody>' + ''.join(rows) + '</tbody></table></div>' + pn('print-codes')))
    (OUT / 'data/entries.json').write_text(json.dumps(entries, ensure_ascii=False, separators=(',', ':')))
    # contents / home
    pdf_link = f'<a class="btn" href="{E(PDF)}">Download the PDF</a>' if PDF else ''
    def li(slug): return f'<li><a href="{slug}.html">{E(titles[slug])}</a></li>'
    body = f'''<div class="home"><div><p class="kicker">Series Volume 1 · Concise Edition</p><h1>AI by AI Weekly Top 5: The 2025 Collection</h1>
<p class="lede">The year’s AI developments as a panel of leading AI models chose them, week by week: 354 entries, each checked against sources, dated to its week and credited to the models that chose it.</p>
<p class="small">Edited by W.H.L., with Claude Opus 5.5 and GPT-6 Astra. Champaign Magazine, November 2026.</p>
<p>{pdf_link} <a class="btn ghost" href="search.html">Search the entries</a> <a class="btn ghost" href="../historical/index.html">Historical edition</a></p></div>
<img class="cover" src="assets/cover.png" alt="Cover of AI by AI Weekly Top 5: The 2025 Collection, Series Volume 1, Concise Edition"></div>
<div class="toc2"><div><h2>Front matter</h2><ul>{''.join(li(f[0]) for f in FRONT)}</ul>
<h2>Back matter</h2><ul>{li('edit-log')}{li('forecast-register')}{li('print-codes')}<li><a href="search.html">Search (in place of the printed Index)</a></li></ul></div>
<div><h2>Monthly chapters</h2><ul>{''.join(li(m.lower()) for m in MONTHS)}</ul></div></div>'''
    (OUT / 'index.html').write_text(page('AI by AI Weekly Top 5: The 2025 Collection · Concise Edition', body, 0, 'The concise edition: 354 checked entries, by month.'))
    shutil.copy(P / 'cover/Cover_2025_Concise_v2.png', OUT / 'assets/cover.png')
    opts = ''.join(f'<option>{m}</option>' for m in MONTHS)
    body = f'''<h1>Search the concise edition</h1><form class="search" onsubmit="return false"><input id="q" type="search" placeholder="Keyword or phrase, e.g. Nvidia, “open weights”, P-2025-W36-01" autocomplete="off">
<div class="filters"><label>Month<select id="m"><option value="">All</option>{opts}</select></label><label>Selected by<input id="s" type="text" placeholder="e.g. Grok"></label></div></form>
<p id="count" class="small"></p><ol id="res" class="results"></ol><script src="assets/search.js"></script>'''
    (OUT / 'search.html').write_text(page('Search · Concise Edition', body, 0, 'Search the 354 entries.'))
    return entries

if __name__ == '__main__':
    e = build(); print('entries', len(e))
