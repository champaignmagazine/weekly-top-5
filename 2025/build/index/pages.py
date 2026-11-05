"""Clean per-page text of a proof for indexing: drops running heads/folios, contributor lines,
source-note and selected-source sections (to the end of their section), and the back matter."""
import json, re, subprocess, sys
NOTE_HEADS = ('Source notes', 'Selected sources', 'Sources for events outside the chapters')
def clean_pages(pdf, layout):
    L = json.load(open(layout)); lab, st = L['labels'], L['starts']
    last = st['bm01_editlog'] - 1
    from pypdf import PdfReader
    off = len(PdfReader(pdf).pages) - L['total']   # 1 when a front cover precedes the layout
    bounds = sorted(st.values())
    pages, heads, intro, in_notes, pre_entry = {}, {}, {}, False, False
    months = [st[m] for m in ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')]
    for i in range(1, last + 1):
        if i in bounds: in_notes = False
        if i in months: pre_entry = True
        t = subprocess.run(['pdftotext', '-f', str(i + off), '-l', str(i + off), pdf, '-'], capture_output=True, text=True).stdout
        keep, hl, grab = [], [], 0
        for l in t.split('\n'):
            s = l.strip()
            if re.match(r'^(AI BY AI WEEKLY TOP 5|PRINT PROOF|RELEASE CANDIDATE)', s): continue
            if s in ('REFERENCES',) or s.startswith(NOTE_HEADS): in_notes = True
            if in_notes: continue
            if s.startswith('Selected by '): continue
            if re.match(r'^P-2025-W\d\d-\d\d$', s): grab = 1; pre_entry = False; continue
            if grab:
                if s and s.upper() == s and re.search(r'[A-Z]', s): grab = 0
                elif s: hl.append(s)
            keep.append(l)
            if pre_entry and i in range(months[0], last + 1): intro[i] = True
        if not lab[i - 1]: continue
        tx = '\n'.join(keep)
        tx = re.sub(r'-\n(?=[a-z])', '', tx)
        # footnote markers set after a word: "Brookfield.17 The", "oversight.23", "said,”12"
        tx = re.sub(r'(?<=[A-Za-z\)”’%])([.,;:])(\d{1,3}(?:[,–]\s?\d{1,3})*)(?=\s|$)', r'\1', tx)
        tx = re.sub(r'(?<=[\)”’])(\d{1,3}(?:[,–]\s?\d{1,3})*)(?=\s|$)', '', tx)
        pages[i] = re.sub(r'\s+', ' ', tx)
        heads[i] = ' '.join(hl)
    return pages, heads, intro, lab, st
if __name__ == '__main__':
    p, h, it, lab, st = clean_pages(sys.argv[1], sys.argv[2])
    json.dump({'pages': p, 'heads': h, 'intro': sorted(it), 'lab': lab, 'st': st}, open(sys.argv[3], 'w'))
    print(len(p), sum(1 for v in h.values() if v))
