"""Final keyword index from GPT-6 Astra's curation (Keyword_Index_Curated_GPT_v1.csv),
paginated against a proof's cleaned page text (pages.py).

Rules (Claude's final pass, November 2, 2026):
- Pages are counted from body text only: running heads, folios, "Selected by" contributor
  lines, source notes and selected-source lists are removed before matching.
- Named headings match case-sensitively on whole words; a match does not continue into a
  version suffix (".1", "-0324", "-Codex"), so model versions stay separate.
- A heading collects the pages of the terms GPT merged into it, except where the context
  check below restricts or reallocates them.
- Headings with more than HEAVY pages get subentries by part of the book.
- Thematic headings count front-matter pages, the chapters' opening summaries and entry headlines;
  a theme mentioned on eight pages or fewer counts every page.
- Headings that would cover more than half of the indexed pages are omitted.
"""
import csv, json, re, sys
from collections import OrderedDict

CUR = '../handoff/gpt_index_v1/Keyword_Index_Curated_GPT_v1.csv'
HEAVY = 24

# ---- context-check resolutions -------------------------------------------------------
# Display names follow the book's style.
RENAME = {'NVIDIA': 'Nvidia', 'NVIDIA GPUs': 'Nvidia GPUs', 'Edited edition': 'Concise edition',
          'The New York Times': 'New York Times, The', 'Tulu 3': 'Tülu 3', 'Universal': 'Universal, film studio'}
# Headings dropped after the context check (reason in REPORT).
DROP = {
    'Axios': 'source credit only ("told Axios")',
    'Bloomberg News': 'source credits only', 'Business Insider': 'source credit only',
    'CNN': 'source credits only', 'Financial Times': 'source credits only', 'Fortune': 'source credit only',
    'South China Morning Post': 'source credit only', 'TechCrunch': 'no body-text occurrence; notes only',
    'Wall Street Journal': 'source credits only', 'Washington Post': 'source credits only',
    'Opus': 'allocated to the versioned Claude Opus headings',
    'Deep Think': 'allocated to Gemini 2.5 Deep Think, Gemini 3 Deep Think and Gemini Deep Think',
    'Gemini Flash Thinking': 'merged into Gemini 2.0 Flash Thinking (p. 10 names that model)',
    'Artificial intelligence': 'covers nearly every page', 'The New York Times Company': 'merged into New York Times, The',
}
# Extra search terms (literal unless prefixed re:), beyond GPT's merges.
EXTRA = {
    'UK AI Security Institute': ['AI Security Institute'],          # all four occurrences are the UK institute
    'ChatGPT for Teachers': ['ChatGPT for US teachers'],            # p. xxvii "ChatGPT for purchases" excluded
    'General-Purpose AI Code of Practice': ['Code of Practice'],   # all six are the EU code
    'Gavin Newsom': ['Governor Newsom'],
    'Google I/O Connect India': ['I/O Connect India'],
    'DeepSeek-R1': ['R1', 'DeepSeek R1'],                            # every bare R1 is DeepSeek's
    'Scale AI': [r're:Scale(?=’s|\s(?:appointed|investment))'],     # never bare "Scale"
    'Gemini 2.0 Flash Thinking': ['Gemini Flash Thinking'],
    'New York Times, The': ['The New York Times Company', 'The New York Times'],
    'Universal Music Group': ['Universal Music'],
    'Tülu 3': ['Tülu 3', 'Tulu 3'],
    'Nvidia': ['Nvidia', 'NVIDIA'], 'Nvidia GPUs': ['Nvidia GPUs', 'NVIDIA GPUs'],
}
# Page-level allocations (proof page labels) where a string cannot decide identity.
ONLY = {
    'Reuters': ['xxxii', '111', '120'],          # its investigation of Meta's chatbot rules was itself the story
    'BBC': ['9'],                                 # complainant over Apple's notification summaries
    'Universal, film studio': ['137', '203'],     # the studio's suit against Midjourney
    'Gemini Deep Think': ['xiv', '104'],          # the advanced version at the IMO, July
}
ADD = {'Gemini 3 Deep Think': ['xi', 'xxiv', '184']}  # "Deep Think offering/mode" alongside Gemini 3
NOT = {'Universal Music Group': ['137', '203'], 'Nature': ['156']}  # p. 156 is Nature Microbiology
# Headings printed with one named subentry (GPT-6 Astra, November 4: the METR study of developers).
NAMED_SUBS = {'Productivity': 'software developers'}
# Redirects kept as unpaginated "See" entries.
SEE = {'AGI': 'Artificial general intelligence', 'AWS': 'Amazon Web Services', 'Chatbot Arena': 'LMArena',
       'IMO': 'International Mathematical Olympiad', 'Allen Institute for AI': 'Ai2', 'EU': 'European Union',
       'FDA': 'US Food and Drug Administration', 'FTC': 'US Federal Trade Commission',
       'TII': 'Technology Innovation Institute', 'UAE': 'United Arab Emirates'}

# Thematic headings: pattern (case-insensitive) and scope ('fm' = front matter only).
THEME = {
    'Large language models': (r'large language models?|\bLLMs?\b', 'all'),
    'Agents': (r'\bagents?\b', 'all'), 'Agentic AI': (r'\bagentic\b', 'all'),
    'AI evaluation': (r'\bevaluat\w*', 'all'), 'Benchmarks': (r'\bbenchmarks?\b', 'all'), 'AI safety': (r'\bsafety\b', 'all'),
    'AI-generated content': (r'AI-generated|deepfakes?|synthetic (?:media|images?|video)', 'all'),
    'Artificial general intelligence': (r'\bAGI\b|artificial general intelligence', 'all'),
    'Chip export controls': (r'export (?:controls?|rules?|licen[cs]es?)|chip[- ]?export', 'all'),
    'Copyright litigation': (r'(?:copyright|fair use)\W+(?:\w+\W+){0,12}?(?:lawsuit|suit|sued|suing|ruling|ruled|court|judge|settle\w*)|(?:lawsuit|suit|sued|suing|ruling|ruled|judge|settle\w*)\W+(?:\w+\W+){0,12}?(?:copyright|fair use)', 'all'),
    'Data centers': (r'data cent(?:er|re)s?', 'all'),
    'Energy demand': (r'\benergy\b|electricity|power (?:demand|grid|supply)|\bnuclear\b', 'all'),
    'Forecasts': (r'\bforecast\w*|\bpredict\w*', 'all'),
    'Hallucinations': (r'hallucinat\w*|fabricat\w*|unsupported claims?', 'all'),
    'Human oversight': (r'human oversight|human review|human in the loop|humans? in charge', 'all'),
    'Inference': (r'\binference\b', 'all'), 'Licensing': (r'\blicens(?:ing|ed|es?)\b', 'all'),
    'Model weights': (r'\bweights\b', 'all'), 'Open models': (r'open[- ]weights?|open[- ]source|open models?', 'all'),
    'Productivity': (r'productivity|experienced open-source developers|completion time', 'all'), 'Reasoning models': (r'reasoning models?', 'all'),
    'Robotics': (r'\brobot\w*|humanoid', 'all'), 'Training data': (r'training data|pirated|scrap(?:ed|ing)', 'all'),
    'Verification': (r'\bverif\w*', 'all'), 'World models': (r'world models?', 'all'),
    'Independent evaluation': (r'independent(?:ly)? (?:evaluat|verif|test|assess|review|check)\w*|third-party (?:test|evaluat|audit)\w*', 'all'),
    'Introspection': (r'introspect\w*', 'all'), 'Foundation models': (r'foundation models?', 'all'),
    'AI chips': (r'\bchips?\b|\bGPUs?\b|\bTPUs?\b|accelerators?', 'all'),
    'Copyright': (r'\bcopyright\w*', 'all'),
    'Cloud': (r'\bcloud\b', 'all'), 'Commitments': (r'\bcommitments?\b', 'all'), 'Governance': (r'\bgovernance\b', 'all'),
    'Incidents': (r'\bincidents?\b', 'all'), 'Security': (r'\bsecurity\b|cyber\w*', 'all'), 'Trust': (r'\btrust\w*', 'all'),
    'Reconstructed weeks': (r'reconstruct\w*', 'fm'), 'Concise edition': (r'concise edition|edited edition', 'fm'),
    'Historical edition': (r'historical edition', 'fm'), 'Disclosure': (r'\bdisclos\w*', 'fm'),
    'Panel independence': (r'(?:panel|panelists|models)\W+(?:\w+\W+){0,10}?independen\w*|independen\w*\W+(?:\w+\W+){0,10}?(?:panel|panelists)', 'fm'),
    'Model self-reporting': (r'about themselves|self-report\w*|makers of (?:the )?panel models|their own makers', 'fm'),
}

def lit(term):
    return re.compile(r'(?<![\w-])' + re.escape(term) + r'(?![\w]|[.\-][0-9A-Z])')

def build(clean_json, out_json, report_md):
    D = json.load(open(clean_json)); P = {int(k): v for k, v in D['pages'].items()}
    H = {int(k): v for k, v in D['heads'].items()}; lab, st = D['lab'], D['st']; INTRO = set(D['intro'])
    jan = st['January']; fm_skip = set(range(st['fm01_halftitle'], st['fm05_series']))
    month_of = {}
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    for i in P:
        month_of[i] = 'Front matter' if i < jan else [m for m in months if st[m] <= i][-1]
    bylab = {lab[i - 1]: i for i in P}
    R = list(csv.DictReader(open(CUR)))
    heads, merged = OrderedDict(), {}
    for r in R:
        t, keep, into, also = r['term'], r['keep (yes/no)'], r['merge_into'], r['see_also']
        if keep == 'yes':
            heads[RENAME.get(t, t)] = {'src': t, 'also': [RENAME.get(a.strip(), a.strip()) for a in also.split(';') if a.strip()]}
        elif into:
            merged.setdefault(RENAME.get(into, into), []).append(t)
    report = {'dropped': [], 'empty': [], 'broad': [], 'redirects': [], 'subentries': []}
    entries = {}
    for h, d in heads.items():
        if d['src'] in DROP or h in DROP:
            report['dropped'].append((h, DROP.get(d['src'], DROP.get(h)))); continue
        if h in THEME:
            pat, scope = THEME[h]; rx = re.compile(pat, re.I)
            body = {i for i in P if i not in fm_skip and rx.search(P[i]) and (i < jan or scope == 'all')}
            ps = {i for i in body if i < jan or i in INTRO or rx.search(H.get(i, ''))}
            if len(body) <= 8: ps = body   # a rare theme: every substantive mention counts
        else:
            terms = [d['src']] + [v for v in merged.get(h, []) if v not in SEE] + EXTRA.get(h, [])
            # Claude model short forms ("Opus 4.1" for Claude Opus 4.1); DeepSeek short forms ("V3.1")
            m = re.match(r'Claude ((?:Opus|Sonnet|Haiku) [\d.]+)$', h) or re.match(r'DeepSeek-(V[\d.]+(?:-\w+)?|R1(?:-\d+)?)$', h)
            if m: terms.append(m.group(1))
            rxs = [re.compile(t[3:]) if t.startswith('re:') else lit(t) for t in dict.fromkeys(terms)]
            ps = {i for i in P if i not in fm_skip and any(rx.search(P[i]) for rx in rxs)}
        if h in ONLY: ps = {bylab[l] for l in ONLY[h]}
        ps |= {bylab[l] for l in ADD.get(h, [])}; ps -= {bylab[l] for l in NOT.get(h, [])}
        if not ps:
            report['empty'].append(h); continue
        if len(ps) > 0.5 * len(P):
            report['broad'].append((h, len(ps))); continue
        entries[h] = sorted(ps)
    def fmt(ps):
        out, j = [], 0
        while j < len(ps):
            k = j
            while k + 1 < len(ps) and ps[k + 1] == ps[k] + 1: k += 1
            out.append(lab[ps[j] - 1] if k == j else f'{lab[ps[j] - 1]}–{lab[ps[k] - 1]}'); j = k + 1
        return ', '.join(out)
    rows = []
    for h, ps in entries.items():
        also = [a for a in heads[h]['also'] if a in entries and a != h]
        row = {'term': h, 'pages': fmt(ps), 'also': also}
        if h in NAMED_SUBS:
            row['pages'] = ''; row['subs'] = [[NAMED_SUBS[h], fmt(ps)]]
        if len(ps) > HEAVY:
            subs = OrderedDict()
            for i in ps: subs.setdefault(month_of[i], []).append(i)
            row['pages'] = ''; row['subs'] = [[k, fmt(v)] for k, v in subs.items()]
            report['subentries'].append((h, len(ps)))
        rows.append(row)
    for a, tgt in SEE.items():
        tgt = RENAME.get(tgt, tgt)
        if tgt in entries:
            rows.append({'term': a, 'see': tgt}); report['redirects'].append((a, tgt))
        else:
            report['redirects'].append((a, tgt + ' — TARGET MISSING, omitted'))
    key = lambda r: re.sub(r'^[“"]', '', r['term']).lower()
    rows.sort(key=lambda r: (key(r), r['term']))
    # integrity
    names = {r['term'] for r in rows}
    dangling = [(r['term'], x) for r in rows for x in (r.get('also', []) + ([r['see']] if 'see' in r else [])) if x not in names]
    json.dump(rows, open(out_json, 'w'), ensure_ascii=False, indent=0)
    with open(report_md, 'w') as f:
        f.write(f'# Index build report\n\nHeadings printed: {sum(1 for r in rows if "see" not in r)}; redirects: {sum(1 for r in rows if "see" in r)}; with subentries: {len(report["subentries"])}; dangling references: {len(dangling)}\n\n')
        for k, v in report.items():
            f.write(f'## {k} ({len(v)})\n\n' + ''.join(f'- {x}\n' for x in v) + '\n')
        if dangling: f.write('## dangling\n\n' + ''.join(f'- {x}\n' for x in dangling))
    return rows, report, dangling

if __name__ == '__main__':
    rows, rep, dang = build(*sys.argv[1:4])
    print(len(rows), {k: len(v) for k, v in rep.items()}, 'dangling', len(dang))
