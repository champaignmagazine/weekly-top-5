"""Assemble the print proof of the 2025 volume: front matter, twelve chapters, back matter.
Continuous pagination (roman front matter, arabic body), recto starts, final index pages."""
import os, re, json, html, asyncio, pathlib, subprocess, markdown
from pypdf import PdfReader, PdfWriter
from playwright.async_api import async_playwright

HERE = pathlib.Path(__file__).parent
SRC, CH, OUT = HERE / 'src', HERE / 'ch', HERE / 'parts'
OUT.mkdir(exist_ok=True)
FONTS = HERE.parent / 'print/node_modules/@fontsource'
import os as _os
RELEASE = _os.environ.get('RELEASE') == '1'
PROOF = '' if RELEASE else 'Print proof 20 · November 4, 2026'
OUTNAME = 'AI_by_AI_Weekly_Top5_2025_Concise_Edition.pdf' if RELEASE else 'AI_by_AI_Weekly_Top5_2025_Print_Proof_20.pdf'
MONTHS = 'January February March April May June July August September October November December'.split()
E = html.escape

def ff(fam, file, weight, style='normal'):
    return f"@font-face{{font-family:'{fam}';src:url('{(FONTS / file).as_uri()}') format('woff2');font-weight:{weight};font-style:{style};}}"
FONTCSS = ''.join([
    ff('Source Serif', 'source-serif-4/files/source-serif-4-latin-400-normal.woff2', 400),
    ff('Source Serif', 'source-serif-4/files/source-serif-4-latin-400-italic.woff2', 400, 'italic'),
    ff('Source Serif', 'source-serif-4/files/source-serif-4-latin-600-normal.woff2', 600),
    ff('Source Serif', 'source-serif-4/files/source-serif-4-latin-700-normal.woff2', 700),
    *[ff('InterP', f'inter/files/inter-latin-{w}-normal.woff2', w) for w in (400, 500, 600, 700, 800)],
    ff('Plex Mono', 'ibm-plex-mono/files/ibm-plex-mono-latin-400-normal.woff2', 400),
    ff('Plex Mono', 'ibm-plex-mono/files/ibm-plex-mono-latin-500-normal.woff2', 500),
])
BASE = '''
:root{--ink:#16232f;--muted:#5d6b78;--accent:#1f6f78;--rule:#d5dbe0;}
@page{size:6in 9in;margin:0.78in 0.62in 0.72in 0.72in;
  @top-left{content:"AI by AI Weekly Top 5";font:500 6.6pt 'Plex Mono';letter-spacing:.06em;color:#7a8794;text-transform:uppercase;vertical-align:bottom;padding-bottom:10pt}
  @top-right{content:"%HEAD%";font:500 6.6pt 'Plex Mono';letter-spacing:.06em;color:#7a8794;text-transform:uppercase;vertical-align:bottom;padding-bottom:10pt}}
@page:first{@top-left{content:none}@top-right{content:none}}
html{font-family:'Source Serif',serif;font-size:10.2pt;line-height:1.45;color:var(--ink);-webkit-print-color-adjust:exact;font-kerning:normal;font-variant-numeric:oldstyle-nums proportional-nums}
body{margin:0}
h1,h2,h3,h4{font-family:'InterP',sans-serif;color:var(--ink);font-variant-numeric:lining-nums;break-after:avoid}
.kicker{font:500 7.4pt 'Plex Mono';letter-spacing:.14em;text-transform:uppercase;color:var(--accent)}
.piece>h1{font-size:21pt;font-weight:800;letter-spacing:-.015em;line-height:1.12;margin:.5in 0 .06in;padding-top:.14in;border-top:1.2pt solid var(--accent)}
.byline{font:500 8pt 'InterP';color:var(--muted);margin:0 0 .26in;font-variant-numeric:lining-nums}
h2{font-size:12.4pt;font-weight:700;margin:.24in 0 .07in}
h3{font-size:10.4pt;font-weight:700;margin:.18in 0 .05in}
p{margin:0 0 .09in;text-align:justify;hyphens:auto;orphans:3;widows:3}
p.note{font-style:italic;color:var(--muted);font-size:9.4pt;text-align:left}
ul,ol{margin:0 0 .1in;padding-left:.22in}li{margin:0 0 .03in}li p{margin:0}
sup{font:600 6.2pt 'InterP';line-height:0;color:var(--accent);font-variant-numeric:lining-nums}
table{border-collapse:collapse;width:100%;margin:.08in 0 .16in;font:400 7.6pt/1.32 'InterP';font-variant-numeric:lining-nums}
th{font-weight:600;text-align:left;border-bottom:.8pt solid var(--ink);padding:3pt 4pt 3pt 0;vertical-align:bottom}
td{border-bottom:.4pt solid var(--rule);padding:3pt 4pt 3pt 0;vertical-align:top}
tr{break-inside:avoid}
a{color:inherit;text-decoration:none}
.sign{text-align:right;font-style:italic;margin-top:.2in}
figure{margin:.12in 0 .16in;break-inside:avoid}figure svg{width:100%;height:auto}
figcaption{font:400 7.4pt/1.4 'InterP';color:var(--muted);margin-top:4pt}
.pre{display:block;font:500 7.6pt 'Plex Mono';letter-spacing:.1em;text-transform:uppercase;color:#1f6f78;margin-bottom:5pt}sup.g{white-space:nowrap}.prop{font:700 9.6pt/1.35 InterP;text-align:left;margin:.14in 0 .05in;break-after:avoid}.sp{height:.16in}.notes ol{font-size:8.2pt;line-height:1.36;padding-left:.2in}.notes li{margin-bottom:4pt;word-break:break-word}
'''

def md(text):
    out, prev = [], ''
    for line in text.split('\n'):
        line = re.sub(r'^  (\s*)([-*]|\d+\.) ', r'    \1\2 ', line)          # 2-space nesting -> 4
        if re.match(r'^\s*([-*]|\d+\.) ', line) and prev.strip() and not re.match(r'^\s*([-*]|\d+\.) ', prev):
            out.append('')                                                      # list needs a blank line before it
        out.append(line); prev = line
    return markdown.markdown('\n'.join(out), extensions=['tables', 'sane_lists'])

def strip_head(t):
    """Drop the doc title line and any draft-status byline; return (title, body)."""
    lines = t.strip('\n').split('\n')
    title = lines[0].lstrip('# ').strip()
    body = lines[1:]
    while body and (not body[0].strip() or re.match(r'^(\*.*(draft|Draft).*\*|\*Year introduction ·.*\*|\*v\d.*\*|Oct \d+, 2026 ·.*)$', body[0].strip())):
        body.pop(0)
    return title, '\n'.join(body)

async def render(pages):
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for name, doc in pages:
            f = OUT / f'{name}.html'
            f.write_text(doc)
            pg = await b.new_page()
            await pg.goto(f.as_uri())
            await pg.wait_for_timeout(300)
            await pg.pdf(path=str(OUT / f'{name}.pdf'), prefer_css_page_size=True, print_background=True, tagged=True)
            await pg.close()
        await b.close()

def page(name, head, body, extra=''):
    css = FONTCSS + BASE.replace('%HEAD%', head) + extra
    return (name, f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{E(name)}</title><style>{css}</style></head><body>{body}</body></html>')

def piece(title, byline, body_html, cls=''):
    b = f'<div class="byline">{byline}</div>' if byline else ''
    return f'<section class="piece {cls}"><h1>{title}</h1>{b}{body_html}</section>'

# ---------- charts for "2025 in Outline" (redrawn for print from the doc's widgets) ----------
def chart_types():
    data = {'Releases': [39, 30, 31, 42], 'Deals and investments': [11, 10, 22, 25],
            'Research and evaluations': [7, 7, 13, 18], 'Government action': [12, 10, 9, 10]}
    n = [78, 76, 95, 105]
    L, R, T, B = 46, 330, 14, 196
    x = lambda i: L + i * (R - L) / 3
    y = lambda v: B - v / 50 * (B - T)
    s = [f'<svg viewBox="0 0 470 222" font-family="InterP" font-size="9">']
    for v in range(0, 51, 10):
        s.append(f'<line x1="{L}" x2="{R}" y1="{y(v):.1f}" y2="{y(v):.1f}" stroke="{"#16232f" if v == 0 else "#dde2e6"}" stroke-width=".6"/><text x="{L-6}" y="{y(v)+3:.1f}" text-anchor="end" fill="#5d6b78">{v}%</text>')
    for i, q in enumerate(['Q1', 'Q2', 'Q3', 'Q4']):
        s.append(f'<text x="{x(i):.1f}" y="{B+14}" text-anchor="middle" fill="#5d6b78">{q} ({n[i]})</text>')
    shades = {'Releases': '#16232f', 'Deals and investments': '#1f6f78', 'Research and evaluations': '#7a8794', 'Government action': '#a9b3bc'}
    labels_y = {}
    for k, vals in data.items():
        pct = [100 * c / n[i] for i, c in enumerate(vals)]
        pts = ' '.join(f'{x(i):.1f},{y(p):.1f}' for i, p in enumerate(pct))
        w = 2.4 if k.startswith('Deals') else 1.4
        s.append(f'<polyline points="{pts}" fill="none" stroke="{shades[k]}" stroke-width="{w}"/>')
        s += [f'<circle cx="{x(i):.1f}" cy="{y(p):.1f}" r="2.6" fill="{shades[k]}"/>' for i, p in enumerate(pct)]
        labels_y[k] = y(pct[-1])
    # keep end labels apart
    ordered = sorted(labels_y.items(), key=lambda kv: kv[1])
    last = -99
    for k, ly in ordered:
        ly = max(ly, last + 11); last = ly
        p = round(100 * data[k][-1] / n[-1])
        s.append(f'<text x="{R+8}" y="{ly+3:.1f}" fill="{shades[k]}" font-weight="{600 if k.startswith("Deals") else 400}">{k} {p}%</text>')
    s.append('</svg>')
    return ('<figure>' + ''.join(s) + '<figcaption>Share of printed entries by story type, by quarter of 2025 (354 entries; adjudicated coding v2, October 29, 2026; quarters by collection week, entries per quarter in brackets). Separate codings by Claude Opus 5.5 and GPT-6 Astra, disagreements settled by rules the editor set and reviewed by both.</figcaption></figure>')

def chart_releases():
    rel = [(0, 'DeepSeek-R1 · o3-mini'), (1, 'Grok 3 · Claude 3.7 Sonnet · GPT-4.5'), (2, 'Gemini 2.5 Pro'), (3, 'o3 · o4-mini'),
           (4, 'Claude Opus 4 · Sonnet 4'), (6, 'Grok 4'), (7, 'GPT-5 · Claude Opus 4.1'), (10, 'GPT-5.1 · Grok 4.1 · Gemini 3 Pro · Claude Opus 4.5'),
           (11, 'GPT-5.2 · Gemini 3 Flash')]
    mon = 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split()
    band = {0: 'Wave 1: reasoning', 3: 'Wave 2: tools and routing', 10: 'Wave 3: new generation'}
    row = 16
    s = ['<svg viewBox="0 0 470 214" font-family="InterP" font-size="8.6">']
    for i, m in enumerate(mon):
        yy = 10 + i * row
        s.append(f'<text x="0" y="{yy+4}" fill="#5d6b78" font-family="Plex Mono" font-size="8">{m}</text><line x1="30" x2="40" y1="{yy}" y2="{yy}" stroke="#d5dbe0"/>')
    spans = [(0, 2, '#16232f'), (3, 7, '#1f6f78'), (10, 11, '#7a8794')]
    for a, z, c in spans:
        s.append(f'<rect x="32" y="{10+a*row-5}" width="5" height="{(z-a)*row+10}" fill="{c}"/>')
    for i, t in rel:
        yy = 10 + i * row
        s.append(f'<circle cx="46" cy="{yy}" r="2.4" fill="#1f6f78"/><text x="54" y="{yy+3}" fill="#16232f">{E(t)}</text>')
    for i, t in band.items():
        s.append(f'<text x="470" y="{10+i*row+3}" text-anchor="end" fill="#5d6b78" font-style="italic">{t}</text>')
    s.append('</svg>')
    return ('<figure>' + ''.join(s) + '<figcaption>Frontier model releases named in this outline, January–December 2025, by month of release. Bars mark the three waves described above.</figcaption></figure>')

def notes_refs(t):
    def grp(m):
        ns = [int(x) for x in re.findall(r'\[\^(\d+)\]', m.group(0))]
        out, j = [], 0
        while j < len(ns):
            k = j
            while k + 1 < len(ns) and ns[k + 1] == ns[k] + 1: k += 1
            out.append(str(ns[j]) if k - j < 2 else f'{ns[j]}–{ns[k]}')
            if 0 < k - j < 2: out.append(str(ns[k]))
            j = k + 1
        return f'<sup class="g">{", ".join(out)}</sup>'
    head, sep, notes = t.partition('## Source notes')
    head = re.sub(r'(?:\[\^\d+\])+', grp, head)
    head = re.sub(r'\\\[([\d, ]+)\\\]', lambda m: f'<sup class="g">{m.group(1)}</sup>', head)
    head = re.sub(r'^\*\*(GPT-2025-P\d\.[^*]+)\*\*[ \t]*\n?', r'<p class="prop">\1</p>\n\n', head, flags=re.M)
    notes = re.sub(r'^\[\^(\d+)\]: ', r'\1. ', notes, flags=re.M)
    notes = re.sub(r'\n\n(?=\d+\. )', '\n', notes)
    return head + sep + notes

# ---------- pieces ----------
def build_front(contents_rows):
    pages = []
    ttl = 'AI by AI Weekly Top 5 2025'
    pages.append(page('fm01_halftitle', '', '<div style="padding-top:2.3in"><div style="font:800 22pt/1.15 InterP;letter-spacing:-.015em">AI by AI Weekly Top 5<br>The 2025 Collection</div></div>'))
    pages.append(page('fm02_title', '', f'''<div style="padding-top:1.5in;text-align:center;height:7.2in;box-sizing:border-box;display:flex;flex-direction:column">
<div style="font:800 30pt/1.05 InterP;letter-spacing:-.02em;margin:.25in 0 .3in">AI by AI<br>Weekly Top 5</div>
<div style="font:700 17pt InterP;color:#1f6f78;margin:-.12in 0 .12in">The 2025 Collection</div>
<div style="font:500 10pt InterP;color:#5d6b78;margin:0 0 .3in">Series Volume 1 · Concise Edition</div>
<div style="font:500 11pt InterP">Edited by W.H.L.</div>
<div style="font:400 10pt 'Source Serif';font-style:italic;color:#5d6b78;margin-top:4pt">with Claude Opus 5.5 and GPT-6 Astra</div>
<div style="margin-top:auto;font:italic 400 11pt 'Source Serif'">Champaign Magazine</div></div>'''))
    tp = (SRC / 'Title_page.md').read_text().split('## Copyright page')[1]
    tp = tp.replace('\\[month\\]', '[month]')
    pages.append(page('fm03_copyright', '', f'<div style="padding-top:3.6in;font-size:8.4pt;line-height:1.5" class="copy">{md(tp)}</div>', 'p{text-align:left}'))
    rows = ''.join(
        (f'<tr class="grp"><td colspan="3">{E(g)}</td></tr>' if g else '') +
        f'<tr><td class="t">{E(t)}</td><td class="a">{E(a)}</td><td class="p">{p}</td></tr>'
        for g, t, a, p in contents_rows)
    pages.append(page('fm04_contents', '', piece('Contents', '', f'<table class="toc">{rows}</table>'),
        '.toc{font:400 8.6pt/1.3 "Source Serif";font-variant-numeric:oldstyle-nums}.toc td{border:none;padding:2.4pt 0}.toc .a{color:#5d6b78;font-style:italic;padding:2.4pt 8pt;white-space:nowrap}.toc .p{text-align:right;font-family:"Plex Mono";font-size:7.6pt;width:.4in}.toc .grp td{font:600 7pt "Plex Mono";letter-spacing:.12em;text-transform:uppercase;color:#1f6f78;padding-top:9pt}'))
    # series preface
    t, b = strip_head((SRC / 'Series_preface.md').read_text())
    pages.append(page('fm05_series', 'Series preface', piece('Series Preface', '', '<div class="sp"></div>' + md(b)), 'p{font-size:9.9pt;line-height:1.42}.sign{margin-top:.1in}'))
    t, b = strip_head((SRC / 'Preface_GPT_6_Astra.md').read_text())
    def signed(h, name):
        i = h.rstrip().rfind('<p>')
        return h[:i] + f'<div style="break-inside:avoid">{h[i:]}<p class="sign">{name}</p></div>'
    g = signed(md(b), 'GPT-6 Astra') + '<div class="sep">· · ·</div>'
    t, b = strip_head((SRC / 'AI_by_AI_2025_Year_Volume_Preface_Claude_.md').read_text())
    b = b.replace('— Claude Opus 5.5', '')
    pages.append(page('fm06_pref', 'Volume preface', piece('Volume Preface: 2025', '', '<div class="sp"></div>' + g + signed(md(b), 'Claude Opus 5.5')), '.sep{text-align:center;color:#7a8794;margin:.16in 0 .1in;letter-spacing:.3em}'))
    t, b = strip_head((SRC / 'Year_introduction_GPT_6_Astra.md').read_text())
    b = notes_refs(b)
    main, notes = b.split('## Source notes')
    html_main = md(main).replace('<p><em>Written retro', '<p class="note"><em>Written retro').replace('<p><em>GPT-6 Astra also', '<p class="note"><em>GPT-6 Astra also')
    pages.append(page('fm08_intro_gpt', 'AI in 2025 · GPT-6 Astra', piece('<span class="pre">2025 Collection Introduction, I</span>' + E(t), 'GPT-6 Astra', html_main + '<div class="notes"><h2>Source notes</h2>' + md(notes) + '</div>')))
    t, b = strip_head((SRC / 'AI_by_AI_2025_Yearly_Introduction_The_Year_in_AI.md').read_text())
    b = re.sub(r'^&#91;embedded content: frontier.*$', '%%REL%%', b, flags=re.M)
    b = re.sub(r'^&#91;embedded content: Adjudicated.*$', '%%TYPES%%', b, flags=re.M)
    h = md(b).replace('<p>%%REL%%</p>', chart_releases()).replace('<p>%%TYPES%%</p>', chart_types())
    h = h.replace('<p><em>Written retro', '<p class="note"><em>Written retro').replace('<p><em>Sources for events', '<p class="note"><em>Sources for events')
    pages.append(page('fm09_outline', '2025 in Outline · Claude Opus 5.5', piece('<span class="pre">2025 Collection Introduction, II</span>2025 in Outline', 'Claude Opus 5.5', h)))
    for n, f, head in [('fm10_howread', 'How_to_read_this_book.md', 'How to read this book'),
                       ('fm11_howmade', 'How_the_volume_was_made.md', 'How the volume was made'),
                       ('fm12_disclosure', 'AI_authorship_disclosure.md', 'Disclosure')]:
        t, b = strip_head((SRC / f).read_text())
        pages.append(page(n, head, piece(E(head.title().replace(' To ', ' to ').replace(' The ', ' the ').replace('Ai ', 'AI ')), '', md(b))))
    return pages

def build_back(chapter_start, pagemap):
    pages = []
    el = (HERE.parent / 'print/Edit_Log_2025_v0.1.md').read_text()
    t, b = strip_head(el)
    pages.append(page('bm01_editlog', 'Appendix A · Edit log', piece('Appendix A: Edit Log', '', md(b))))
    t, b = strip_head((SRC / 'Appendix_Forecast_register_back_matter_.md').read_text())
    pages.append(page('bm02_forecast', 'Appendix B · Forecast register', piece('Appendix B: Forecast Register', '', md(b)),
        'table{font-size:6.5pt}td,th{padding:2.2pt 3pt 2.2pt 0}'))
    import sys, importlib
    sys.path.insert(0, str(HERE.parent / 'print'))
    rows = []
    for m in MONTHS:
        meta = json.load(open(CH / f'{m.lower()}_meta.json'))
        C = importlib.import_module(f'{m.lower()}_content')
        dls = {f'P-2025-W{wk:02d}-{i:02d}': it[1] for wk, _, _, items in C.WEEKS for i, it in enumerate(items, 1)}
        rows.append(f'<tr class="grp"><td colspan="5">{m}</td></tr>')
        for code, title, ids, sel in meta['index']:
            pg = chapter_start[m] + pagemap[m]['codes'][code] - 1
            t = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', E(title))
            rows.append(f'<tr><td class="c">{code}</td><td class="d">{E(dls[code])}</td><td>{t}</td><td class="p">{pg}</td><td class="i">{E(", ".join(ids))}</td></tr>')
    intro = ('<p class="note">Print codes (P-2025-W36-01) give year, collection week and entry. Dates are the entry’s dateline; pages are the page on which the entry begins. Names and terms are indexed separately in the Index that follows. '
             'Master IDs (2025-W36-L1-1: year, week, list, item) locate each source item in the annotated master and the historical edition; supplemental IDs cover gaps in the supplied register. 354 entries.</p>')
    pages.append(page('bm03_index', 'Index of print codes', piece('Index of Print Codes', '', intro + '<table class="ix"><tr><th>Code</th><th>Date</th><th>Entry</th><th class="p">Page</th><th>Master IDs</th></tr>' + ''.join(rows) + '</table>'),
        '.ix{font-size:6.6pt;line-height:1.28}.ix td{padding:1.6pt 3pt 1.6pt 0}.ix .c{font-family:"Plex Mono";white-space:nowrap;color:#1f6f78}.ix .p{text-align:right;padding-right:6pt}.ix .i{font-family:"Plex Mono";font-size:5.6pt;color:#5d6b78;width:1.35in}.ix .d{width:.8in;color:#5d6b78;font-size:5.8pt;padding-right:5pt}.ix .c{width:.62in}.ix .grp td{font:600 7.4pt InterP;padding-top:7pt;border-bottom:.8pt solid #16232f}'))
    kw = HERE / 'kw.json'
    terms = json.load(open(kw)) if kw.exists() else [['(placeholder)', '1']]
    body, cur = [], ''
    for r in terms:
        if isinstance(r, list): r = {'term': r[0], 'pages': r[1]}
        t = r['term']; L = t.lstrip('“"')[0].upper(); L = L if L.isalpha() else '#'
        if L != cur:
            cur = L; body.append(f'<div class="L">{L}</div>')
        if 'see' in r:
            body.append(f'<div class="k">{E(t)}. <em>See</em> {E(r["see"])}</div>'); continue
        also = f' <em>See also</em> {E("; ".join(r["also"]))}.' if r.get('also') else ''
        if r.get('subs'):
            body.append(f'<div class="k">{E(t)}</div>' + ''.join(f'<div class="k s">{E(a)} <span>{pp}</span></div>' for a, pp in r['subs']) + (f'<div class="k s">{also.strip()}</div>' if also else ''))
        else:
            body.append(f'<div class="k">{E(t)} <span>{r["pages"]}</span>{"." if also else ""}{also}</div>')
    note = ('<p class="note">Organizations, people, models, products, places, laws and principal topics in the front matter and the twelve chapters. '
            'Source notes and contributor lines are not indexed. Each model version has its own heading; topics point to the introductions, the chapters’ opening summaries and entry headlines. '
            'Dates are indexed in the Index of Print Codes. The online editions will add full-text search by date, keyword and phrase.</p>')
    pages.append(page('bm04_keyword', 'Index', piece('Index', '', note + '<div class="cols">' + ''.join(body) + '</div>'),
        '.cols{columns:2;column-gap:.22in;font:400 7pt/1.3 "Source Serif"}.k{padding-left:.12in;text-indent:-.12in;break-inside:avoid}.k span{font-family:"Plex Mono";font-size:6.2pt;color:#5d6b78}.k.s{padding-left:.26in;text-indent:-.12in}.k em{font-style:italic}.L{font:700 8.4pt InterP;color:#1f6f78;margin:6pt 0 2pt;break-after:avoid}'))
    return pages

def npages(f):
    return len(PdfReader(str(f)).pages)

def layout(front_names, back_names):
    """Return the ordered page plan [(kind, src, srcpage or None, label)] and section start pages."""
    plan, starts = [], {}
    def add(src, label_fn, recto=True, number=True):
        if False:
            plan.append(('blank', None, None, None))
        first = len(plan) + 1
        for i in range(npages(src)):
            plan.append(('pdf', src, i, label_fn if number else None))
        return first
    # front matter: roman, title pages unnumbered
    for n in front_names:
        src = OUT / f'{n}.pdf'
        unnumbered = n in ('fm01_halftitle', 'fm02_title', 'fm03_copyright')
        recto = n != 'fm03_copyright'
        starts[n] = add(src, 'roman', recto=recto, number=not unnumbered)
    body0 = len(plan)
    for m in MONTHS:
        starts[m] = add(CH / f'{m}.pdf', 'arabic')
    for n in back_names:
        starts[n] = add(OUT / f'{n}.pdf', 'arabic')
    return plan, starts, body0

def roman(n):
    out = ''
    for v, s in [(50, 'l'), (40, 'xl'), (10, 'x'), (9, 'ix'), (5, 'v'), (4, 'iv'), (1, 'i')]:
        while n >= v: out += s; n -= v
    return out

def labels(plan, body0):
    lab = []
    for i, (k, src, sp, fn) in enumerate(plan, 1):
        if fn == 'roman': lab.append(roman(i))
        elif fn == 'arabic': lab.append(str(i - body0))
        else: lab.append('')
    # chapter openers: no number on the opener page itself (matches chapter style: first page has no running head)
    return lab

FRONT = ['fm01_halftitle', 'fm02_title', 'fm03_copyright', 'fm04_contents', 'fm05_series', 'fm06_pref',
         'fm08_intro_gpt', 'fm09_outline', 'fm10_howread', 'fm11_howmade', 'fm12_disclosure']
BACK = ['bm01_editlog', 'bm02_forecast', 'bm03_index', 'bm04_keyword']
TOC = [('fm05_series', 'Series Preface', ''), ('fm06_pref', 'Volume Preface', ''), ('fm08_intro_gpt', 'Volume Introduction', ''),
       ('fm10_howread', 'How to Read This Book', ''), ('fm11_howmade', 'How the Volume Was Made', ''), ('fm12_disclosure', 'Disclosure', '')]

def main():
    pagemap = json.load(open(CH / 'pagemap.json'))
    # pass 1 with placeholder contents to measure
    toc_rows = lambda st, lab: ([(('Front matter' if i == 0 else ''), t, a, lab[st[k]-1] if st else '') for i, (k, t, a) in enumerate(TOC)] +
        [(('Monthly Chapters' if i == 0 else ''), f'{m} 2025', '', lab[st[m]-1] if st else '') for i, m in enumerate(MONTHS)] +
        [('Back matter', 'Appendix A: Edit Log', '', lab[st['bm01_editlog']-1] if st else ''),
         ('', 'Appendix B: Forecast Register', '', lab[st['bm02_forecast']-1] if st else ''),
         ('', 'Index of Print Codes', '', lab[st['bm03_index']-1] if st else ''),
         ('', 'Index', '', lab[st['bm04_keyword']-1] if st else '')])
    fake_start = {m: 1 for m in MONTHS}
    asyncio.run(render(build_front(toc_rows(None, None)) + build_back(fake_start, pagemap)))
    for _ in range(2):
        plan, st, body0 = layout(FRONT, BACK)
        lab = labels(plan, body0)
        chap = {m: st[m] - body0 for m in MONTHS}
        asyncio.run(render([p for p in build_front(toc_rows(st, lab)) if p[0] == 'fm04_contents'] + [p for p in build_back(chap, pagemap) if p[0] in ('bm03_index', 'bm04_keyword')]))
    plan2, st2, b2 = layout(FRONT, BACK)
    assert st2 == st, 'layout moved after re-render'
    # number overlay
    ov = ''.join(f'<div class="pg">{f"<span class=n>{l}</span>" if l else ""}{"<span class=l>" + PROOF + "</span>" if l and PROOF else ""}</div>' for l in lab)
    css = FONTCSS + '@page{size:6in 9in;margin:0}body{margin:0}.pg{width:6in;height:9in;position:relative;break-after:page}.n{position:absolute;right:.62in;bottom:.4in;font:500 7.5pt "Plex Mono";color:#5d6b78}.l{position:absolute;left:.72in;bottom:.4in;font:400 6.4pt "Plex Mono";color:#9aa5af;letter-spacing:.05em;text-transform:uppercase}'
    asyncio.run(render([('overlay', f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{ov}</body></html>')]))
    over = PdfReader(str(OUT / 'overlay.pdf'))
    w = PdfWriter()
    readers = {}
    for i, (k, src, sp, fn) in enumerate(plan):
        if k == 'blank':
            w.add_blank_page(432, 648)
        else:
            r = readers.setdefault(src, PdfReader(str(src)))
            w.add_page(r.pages[sp])
        if lab[i]:
            w.pages[-1].merge_page(over.pages[i])
    # outline (bookmarks)
    names = dict((k, t + (f' — {a}' if a else '')) for k, t, a in TOC)
    names.update({m: f'{m} 2025' for m in MONTHS}, bm01_editlog='Appendix A: Edit Log', bm02_forecast='Appendix B: Forecast Register', bm03_index='Index of Print Codes', bm04_keyword='Index', fm02_title='Title page', fm04_contents='Contents')
    for k, v in sorted(st.items(), key=lambda kv: kv[1]):
        if k in names: w.add_outline_item(names[k], v - 1)
    w.add_metadata({'/Title': 'AI by AI Weekly Top 5: The 2025 Collection' + ('' if RELEASE else ' — print proof 20'), '/Author': 'W.H.L., editor; Claude Opus 5.5; GPT-6 Astra', '/Subject': 'Series Volume 1, Concise Edition. Champaign Magazine, November 2026.', '/Keywords': 'artificial intelligence; AI news; 2025; Champaign Magazine; AI by AI Weekly Top 5'})
    dst = HERE / OUTNAME
    cov = HERE / 'cover' / 'Cover_2025_Concise_v2.png'
    if cov.exists():
        # front cover as page 1, full bleed at the 6 x 9 in trim size
        from PIL import Image
        cpdf = HERE / 'cover' / 'cover.pdf'
        im = Image.open(cov).convert('RGB'); im.save(cpdf, 'PDF', resolution=im.size[0] / 6)
        w.insert_page(PdfReader(str(cpdf)).pages[0], 0)
        w.pages[0].mediabox.upper_right = (432, 648)
    w.write(str(dst))
    json.dump({'starts': st, 'labels': lab, 'body0': body0, 'total': len(plan)}, open(HERE / 'proof_layout.json', 'w'), indent=1)
    print('pages', len(plan), 'body starts after', body0, {k: lab[v-1] for k, v in st.items()})

STOP = set('The A An In On At For By And With As After Before From To Of Its It This That These Those Its Their His Her Our We I He She They Both Each Every Some Many Most More Other Another Two Three Four Five One New First Second Third Last Next Early Late Later Week Weeks Month Selected Editor Editor’s Reported Background Research Introduction Major Patterns Long-term Source Sources References Print Date Dates Entry Entries Page Pages Index Chapter Chapters Appendix However When While Where What Why How Which Who If Not No Yes But Or So Also Only Even Still Then Than Although Because Since Under Over Through Across Within Without Among Between Against Toward About Around Into During Until Once Twice Here There Such Much Few Several Any All Monday Tuesday Wednesday Thursday Friday Saturday Sunday January February March April May June July August September October November December Q1 Q2 Q3 Q4 H1 H2 Significance Feedback Context Note Notes Part Table Figure Mr Ms Dr St Capability Access Consequence Written Based Apart Read Across'.split())
def extract_terms():
    import sys, importlib
    sys.path.insert(0, str(HERE.parent / 'print'))
    tok = r"[A-Z][A-Za-z0-9’'&.\-]*[A-Za-z0-9]|[A-Z]"
    seq = re.compile(rf"(?:{tok})(?:\s(?:{tok}|\d[\d.]*[A-Za-z]*|(?:of|de|for|and|the)\s(?:{tok})))*")
    texts = []
    for m in MONTHS:
        C = importlib.import_module(f'{m.lower()}_content')
        for wk, span, pub, items in C.WEEKS:
            for t, dl, paras, sel, ids in items:
                texts.append((t.replace('*', ''), True)); texts += [(p.replace('*', ''), False) for p in paras]
    for f in ['Year_introduction_GPT_6_Astra.md', 'AI_by_AI_2025_Yearly_Introduction_The_Year_in_AI.md', 'AI_by_AI_2025_Year_Volume_Preface_Claude_.md', 'Preface_GPT_6_Astra.md']:
        texts += [(p, False) for p in (SRC / f).read_text().split('## Source notes')[0].split('\n') if p and not p.startswith(('#', '|', '- ['))]
    cnt, intitle, mid = {}, set(), set()
    seq = re.compile(rf"(?:{tok})(?:\s(?:{tok}|\d+(?:\.\d+)*[A-Za-z]*|(?:of|de|for)\s(?:{tok})))*")
    for text, is_title in texts:
        text = re.sub(r'\{\w+\}', '', text)
        for mt in seq.finditer(text):
            pre = text[:mt.start()].rstrip()
            initial = not pre or pre.endswith(('.', ':', '?', '!', '“', '"', '—', '(')) or is_title
            for part in re.split(r"[’']s\s", mt.group(0) + ' '):
                words = re.sub(r"[’']s$", '', part.strip()).rstrip('.,').split(' ')
                while words and words[0] in STOP: words.pop(0)
                while words and (words[-1] in ('of', 'de', 'for') or words[-1] in STOP): words.pop()
                if not words: continue
                term = ' '.join(words)
                if len(term) < 2 or term.isdigit() or (len(words) == 1 and term in STOP): continue
                cnt[term] = cnt.get(term, 0) + 1
                if is_title: intitle.add(term)
                if not initial: mid.add(term)
    junk = set('API APIs GPU GPUs TPU TPUs CPU CPUs AI State States Information Transparency Max Instant Pro Mini Flash Turbo Thinking Fast Lite Plus Preview Experimental Ultra Edge Labs Lab Studio Search Agent Agents Mode Deep Act Law Rule Plan Order Bill Court House Senate Congress Commission Department Ministry Government Council Office Foundation Institute University Prize Award Summit Day Times Information'.split())
    keep = [t for t, c in cnt.items() if t not in junk and not t.endswith(('-based', '-style', '-like')) and (len(t.split()) > 1 or t in mid or (t in intitle and c >= 2))]
    return keep

def build_kw():
    """Index from GPT-6 Astra's curation, paginated on the current layout (../index/build_index.py)."""
    import sys
    sys.path.insert(0, str(HERE.parent / 'index'))
    import pages as IP, build_index as BI
    pdf = str(HERE / OUTNAME)
    p, h, it, lab, st = IP.clean_pages(pdf, str(HERE / 'proof_layout.json'))
    cj = HERE.parent / 'index' / 'clean_current.json'
    json.dump({'pages': p, 'heads': h, 'intro': sorted(it), 'lab': lab, 'st': st}, open(cj, 'w'))
    cwd = os.getcwd(); os.chdir(HERE.parent / 'index')
    try: rows, rep, dang = BI.build(str(cj), str(HERE / 'kw.json'), str(HERE.parent / 'index' / 'Index_Build_Report.md'))
    finally: os.chdir(cwd)
    print('index entries', len(rows), 'dangling', len(dang))

main(); build_kw(); main()
