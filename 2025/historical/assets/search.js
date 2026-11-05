// Search for the historical edition: loads data/items.json once, filters in the browser.
(function () {
  const $ = id => document.getElementById(id);
  const F = ['q', 'm', 'd1', 'd2', 'f', 'l', 'r', 'x'];
  let items = [];
  const esc = s => String(s || '').replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const fold = s => String(s || '').toLowerCase().normalize('NFKD').replace(/[̀-ͯ]/g, '').replace(/[’‘]/g, "'").replace(/[“”]/g, '"');
  const LC = { 'outside its week': 'out', 'inaccurate as stated': 'inacc', 'no evidence found': 'noev', 'not an event': 'notev', 'unverified': 'unv' };

  function terms(q) {  // "quoted phrases" and single words
    const out = []; q = fold(q);
    q.replace(/"([^"]+)"|(\S+)/g, (_, p, w) => { out.push(p || w); return ''; });
    return out.filter(Boolean);
  }
  function snippet(text, ts) {
    const t = String(text || ''); const ft = fold(t);
    let i = -1; for (const x of ts) { i = ft.indexOf(x); if (i >= 0) break; }
    let s = i < 0 ? t.slice(0, 220) : (i > 80 ? '…' : '') + t.slice(Math.max(0, i - 80), i + 160);
    s = esc(s);
    for (const x of ts) {
      if (x.length < 2) continue;
      s = s.replace(new RegExp('(' + x.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'ig'), '<mark>$1</mark>');
    }
    return s + (t.length > 240 ? '…' : '');
  }
  function run() {
    const v = {}; F.forEach(k => v[k] = k === 'x' ? $(k).checked : $(k).value);
    const ts = terms(v.q);
    const res = items.filter(it => {
      if (!v.x && it.kind === 'retro') return false;
      if (v.r && it.role !== v.r) return false;
      if (v.m && it.m !== v.m) return false;
      if (v.d1 && it.to < v.d1) return false;
      if (v.d2 && it.from > v.d2) return false;
      if (v.f && !it.f.includes(v.f)) return false;
      if (v.l === 'confirmed' && (it.role !== 'list' || it.labels.length)) return false;
      if (v.l === 'labeled' && !it.labels.length) return false;
      if (v.l && v.l !== 'confirmed' && v.l !== 'labeled' && !it.labels.includes(v.l)) return false;
      if (ts.length) {
        const hay = fold([it.id, it.c, it.title, it.text, it.codes.join(' ')].join(' '));
        if (!ts.every(t => hay.includes(t))) return false;
      }
      return true;
    });
    $('count').textContent = res.length + (res.length === 1 ? ' item' : ' items') + (v.x ? '' : ' (reconstructed weeks excluded)');
    $('res').innerHTML = res.slice(0, 300).map(it => {
      const chips = it.role !== 'list' ? `<span class="chip role">${esc(it.role)}</span>` :
        (it.labels.length ? it.labels.map(l => `<span class="chip ${LC[l] || ''}">${esc(l)}</span>`).join('') : '<span class="chip ok">confirmed</span>');
      const rec = it.kind === 'retro' ? '<span class="chip recon">reconstructed</span>' : '';
      const pr = it.codes.length ? ` · printed as ${it.codes.map(esc).join(', ')}` : '';
      return `<li><div class="t"><a href="weeks/${it.post}.html#${it.id}">${esc(it.title || it.id)}</a></div>
        <div class="small"><span class="wid">${esc(it.id)}</span> ${esc(it.m)} · week of ${esc(it.from)} · ${esc(it.c)}${pr}</div>
        <div>${chips}${rec}</div><div class="s">${snippet(it.text, ts)}</div></li>`;
    }).join('') + (res.length > 300 ? '<li class="small">Showing the first 300. Narrow the search to see more.</li>' : '');
    const p = new URLSearchParams(); F.forEach(k => { if (v[k]) p.set(k, k === 'x' ? '1' : v[k]); });
    history.replaceState(null, '', '?' + p.toString());
  }
  const qp = new URLSearchParams(location.search);
  F.forEach(k => { if (qp.has(k)) { if (k === 'x') $(k).checked = true; else $(k).value = qp.get(k); } });
  fetch('data/items.json').then(r => r.json()).then(d => { items = d; run(); });
  F.forEach(k => $(k).addEventListener('input', run));
})();
