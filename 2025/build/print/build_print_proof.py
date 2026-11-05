"""Render a print chapter (6 x 9 in) from its content module to HTML and PDF with Chromium."""
import html, re, sys, importlib, pathlib, asyncio
from playwright.async_api import async_playwright

MONTH = sys.argv[1] if len(sys.argv) > 1 else 'september'
VERSION = sys.argv[2] if len(sys.argv) > 2 else '0.2'
DATE = sys.argv[3] if len(sys.argv) > 3 else 'October 26, 2026'
C = importlib.import_module(f'{MONTH}_content')
HERE = pathlib.Path(__file__).parent
FONTS = HERE / 'node_modules/@fontsource'
E = html.escape

order, entries_html = [], []
def smart(t):
    t = re.sub(r"(?<=\w)'(?=\w)", '\u2019', t)            # apostrophes
    t = re.sub(r"(^|[\s(\[])'", '\\1\u2018', t)          # opening single quote
    t = re.sub(r'(^|[\s(\[\u2014/-])"', '\\1\u201c', t)       # opening double quote
    t = t.replace('"', '\u201d')
    return t.replace("'", '\u2019')
def ital(h):
    return re.sub(r'\*([^*]+)\*', r'<em>\1</em>', h)
def cite(text):
    out = ital(E(smart(text), quote=False))
    def rep(m):
        k = m.group(1)
        if k not in order: order.append(k)
        return f'<sup class="n"><a href="#s-{k}">{order.index(k) + 1}</a></sup>'
    out = re.sub(r'\{(\w+)\}', rep, out)
    return re.sub(r'</sup><sup class="n">', '<span class="c">,</span>', out)

body = []
from monthly_intros import INTROS, S as INTRO_HEADS
intro_note, intro_secs = INTROS[MONTH]
title, theme = C.THEME
month_name = MONTH.capitalize()
body.append(f'''<section class="opener">
  <div class="kicker">AI by AI Weekly Top 5 · The 2025 Collection</div>
  <h1>{month_name} 2025</h1>
  <div class="theme">{E(title)}</div>
  {f'<p class="inote">{E(intro_note)}</p>' if intro_note else ''}
  <div class="colophon">
    <p>{C.COVERS}</p>
  </div>
</section>''')
body.append('<section class="intro"><div class="kicker">Introduction</div><h2>' + E(month_name) + ' 2025</h2>' + ''.join(f'<h4>{INTRO_HEADS[i]}</h4>' + ''.join(f'<p>{ital(E(smart(t), quote=False))}</p>' for t in ps) for i, ps in enumerate(intro_secs)) + '</section>')
index_rows = []
for wk, span, pub, items in C.WEEKS:
    body.append(f'<section class="week"><div class="weekhead"><div class="kicker">Week {wk}</div><h2>{E(span)}</h2><div class="pub">{E(smart(pub), quote=False)}</div></div>')
    for i, (t, dl, paras, sel, ids) in enumerate(items, 1):
        code = f'P-2025-W{wk:02d}-{i:02d}'
        index_rows.append((code, t.replace('*', ''), ids, sel))
        body.append(f'''<article>
  <div class="head"><div class="code">{code}</div>
  <h3>{ital(E(smart(t), quote=False))}</h3>
  <div class="dateline">{E(dl)}</div>
  <p>{cite(paras[0])}</p></div>
  <div class="tail"><p class="sig">{cite(paras[1])}</p>
  <div class="sel">Selected by {E(" · ".join(sel))}</div>{f'<p class="ednote"><span>Editor’s note.</span> {cite(paras[2])}</p>' if len(paras) > 2 else ''}</div>
</article>''')
    body.append('</section>')

notes = []
for n, k in enumerate(order, 1):
    pub, ttl, dt, url = C.SOURCES[k]
    shown = re.sub(r'^https?://', '', url)
    shown = re.sub(r'([/._-])', r'\1<wbr>', E(shown))
    notes.append(f'<li id="s-{k}"><span class="num">{n}</span><div><strong>{E(smart(pub), quote=False)}</strong>. {E(smart(ttl), quote=False)}. {E(smart(dt), quote=False)}.'
                 f'<a class="url" href="{E(url)}">{shown}</a></div></li>')
body.append(f'''<section class="notes"><div class="nh"><div class="kicker">References</div><h2>Source notes</h2>
<p class="pub">Sources checked October 26, 2026. Dates distinguish announcements, reports and later updates.</p></div>
<ol>{''.join(notes)}</ol></section>''')

def ff(fam, file, weight, style='normal'):
    return f"@font-face{{font-family:'{fam}';src:url('{(FONTS / file).as_uri()}') format('woff2');font-weight:{weight};font-style:{style};}}"
fonts = ''.join([
    ff('Source Serif', 'source-serif-4/files/source-serif-4-latin-400-normal.woff2', 400),
    ff('Source Serif', 'source-serif-4/files/source-serif-4-latin-400-italic.woff2', 400, 'italic'),
    ff('Source Serif', 'source-serif-4/files/source-serif-4-latin-600-normal.woff2', 600),
    ff('Source Serif', 'source-serif-4/files/source-serif-4-latin-700-normal.woff2', 700),
    *[ff('InterP', f'inter/files/inter-latin-{w}-normal.woff2', w) for w in (400, 500, 600, 700, 800)],
    ff('Plex Mono', 'ibm-plex-mono/files/ibm-plex-mono-latin-400-normal.woff2', 400),
    ff('Plex Mono', 'ibm-plex-mono/files/ibm-plex-mono-latin-500-normal.woff2', 500),
])
CSS = fonts + '''
:root{--ink:#16232f;--muted:#5d6b78;--accent:#1f6f78;--rule:#d5dbe0;}
@page{size:6in 9in;margin:0.78in 0.62in 0.72in 0.72in;
  @top-left{content:"AI by AI Weekly Top 5: The 2025 Collection";font:500 6.6pt 'Plex Mono';letter-spacing:.06em;color:#7a8794;text-transform:uppercase;vertical-align:bottom;padding-bottom:10pt}
  @top-right{content:"''' + month_name + '''";font:500 6.6pt 'Plex Mono';letter-spacing:.06em;color:#7a8794;text-transform:uppercase;vertical-align:bottom;padding-bottom:10pt}
}
@page:first{@top-left{content:none}@top-right{content:none}}
html{font-family:'Source Serif',serif;font-size:10.2pt;line-height:1.42;color:var(--ink);-webkit-print-color-adjust:exact;font-kerning:normal;font-variant-numeric:oldstyle-nums proportional-nums}
body{margin:0}
.kicker{font:500 7.4pt 'Plex Mono';letter-spacing:.14em;text-transform:uppercase;color:var(--accent)}
h1,h2,h3{font-family:'InterP',sans-serif;color:var(--ink);font-variant-numeric:lining-nums}
.opener{break-after:page;padding-top:.45in;border-top:1.2pt solid var(--accent);display:flex;flex-direction:column;height:7.3in;box-sizing:border-box}
.opener h1{font-size:36pt;font-weight:800;letter-spacing:-.02em;margin:.22in 0 .04in;line-height:1}
.opener .theme{font:400 17pt 'InterP';color:var(--accent);margin-bottom:.32in;letter-spacing:-.01em}
.lede{font-size:10.8pt;line-height:1.48;margin:0 0 .13in;hyphens:auto}
.lede strong{font-weight:700}
.opener .inote{font:italic 400 9.6pt/1.45 'Source Serif';color:var(--muted);margin:0;max-width:4.3in}
.intro{break-after:page}
.intro h2{font-size:20pt;font-weight:800;letter-spacing:-.01em;margin:.06in 0 .16in}
.intro h4{font:700 8.6pt 'InterP';text-transform:uppercase;letter-spacing:.06em;color:var(--accent);margin:.2in 0 .06in;break-after:avoid}
.intro p{font-size:10.4pt;line-height:1.5;margin:0 0 .1in;hyphens:auto;text-align:justify}
.colophon{margin-top:auto;border-top:.5pt solid var(--rule);padding-top:9pt;font:400 7.2pt/1.5 'InterP';color:var(--muted);font-variant-numeric:lining-nums}
.colophon p{margin:4pt 0 0;max-width:4.3in}
.week{break-before:auto;margin-top:.12in}

.week h2{font-size:22pt;font-weight:800;letter-spacing:-.015em;margin:.05in 0 2pt}
.pub{font:400 7.6pt 'InterP';color:var(--muted);margin-bottom:.2in;font-variant-numeric:lining-nums}
article{padding:0 0 10pt;margin:0 0 11pt;border-bottom:.5pt solid var(--rule)}
.head,.tail{break-inside:avoid}
.ednote{font-size:8.4pt;line-height:1.4;font-style:italic;color:#4a5560;margin:4pt 0 0}.ednote span{font-style:normal;font-weight:600}
.weekhead{break-inside:avoid;break-after:avoid}
article:last-child{border-bottom:none}
.code{font:500 6.8pt 'Plex Mono';color:var(--accent);letter-spacing:.06em;margin-bottom:2pt}
h3{font-size:11.6pt;font-weight:700;line-height:1.22;margin:0 0 3pt;letter-spacing:-.005em}
.dateline{font:500 7.2pt 'InterP';color:var(--muted);text-transform:uppercase;letter-spacing:.06em;margin-bottom:5pt;font-variant-numeric:lining-nums}
article p{margin:0 0 5pt;text-align:justify;hyphens:auto;orphans:3;widows:3}
article p.sig{color:#33424f}
.sel{font:400 7.2pt 'InterP';color:var(--muted);margin-top:5pt}
sup.n{font:600 6.2pt 'InterP';line-height:0;vertical-align:super;font-variant-numeric:lining-nums}
sup.n a,.c{color:var(--accent);text-decoration:none}
.c{font:600 6.2pt 'InterP';vertical-align:super;line-height:0}
.notes .nh{break-inside:avoid;padding-bottom:.42in;margin-bottom:-.42in}
.notes{break-before:auto;margin-top:.3in;padding-top:.12in;border-top:1.2pt solid var(--accent)}
.notes h2{font-size:22pt;font-weight:800;margin:.05in 0 2pt}
.notes ol{list-style:none;padding:0;margin:0}
.notes li{display:grid;grid-template-columns:.27in 1fr;margin:0 0 7pt;font-size:8.6pt;line-height:1.38;break-inside:avoid}
.notes .num{font:500 7.6pt 'Plex Mono';color:var(--accent);padding-top:1pt}
.notes strong{font-family:'InterP';font-weight:600;font-size:8.2pt}
.notes .url{display:block;font:400 6.7pt/1.35 'Plex Mono';color:#6b7884;text-decoration:none;margin-top:1.5pt;word-break:normal}
'''
doc = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{month_name} 2025 · Print chapter</title><style>{CSS}</style></head><body>{"".join(body)}</body></html>'
out = HERE.parent / 'proof' / 'ch' / f'{month_name}'
out.with_suffix('.html').write_text(doc)

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page()
        await pg.goto(out.with_suffix('.html').as_uri())
        await pg.wait_for_timeout(400)
        await pg.pdf(path=str(out) + '.pdf', prefer_css_page_size=True, print_background=True, tagged=True, outline=True)
        await b.close()
asyncio.run(main())
import json
json.dump({'index': index_rows, 'sources': order}, open(HERE.parent / 'proof' / 'ch' / f'{MONTH}_meta.json', 'w'), ensure_ascii=False, indent=1)
print('built', out.name, len(index_rows), 'entries', len(order), 'sources')
