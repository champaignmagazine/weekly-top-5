// Search for the concise edition: data/entries.json, filtered in the browser.
(function () {
  const $ = id => document.getElementById(id); let E = [];
  const esc = s => String(s || '').replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const fold = s => String(s || '').toLowerCase().normalize('NFKD').replace(/[̀-ͯ]/g, '').replace(/[’‘]/g, "'").replace(/[“”]/g, '"');
  const terms = q => { const o = []; fold(q).replace(/"([^"]+)"|(\S+)/g, (_, p, w) => { o.push(p || w); return ''; }); return o; };
  function snip(t, ts) {
    const f = fold(t); let i = -1; for (const x of ts) { i = f.indexOf(x); if (i >= 0) break; }
    let s = esc(i < 0 ? t.slice(0, 220) : (i > 80 ? '…' : '') + t.slice(Math.max(0, i - 80), i + 160));
    for (const x of ts) if (x.length > 1) s = s.replace(new RegExp('(' + x.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'ig'), '<mark>$1</mark>');
    return s + '…';
  }
  function run() {
    const ts = terms($('q').value), m = $('m').value, s = fold($('s').value);
    const r = E.filter(e => (!m || e.m === m) && (!s || fold(e.sel).includes(s)) &&
      (!ts.length || ts.every(t => fold([e.code, e.title, e.date, e.sel, e.text, e.ids.join(' ')].join(' ')).includes(t))));
    $('count').textContent = r.length + (r.length === 1 ? ' entry' : ' entries');
    $('res').innerHTML = r.map(e => `<li><div class="t"><a href="${e.m.toLowerCase()}.html#${e.code}">${esc(e.title)}</a></div>
      <div class="small"><span class="wid">${esc(e.code)}</span> ${esc(e.m)} · ${esc(e.date)} · selected by ${esc(e.sel)}</div><div class="s">${snip(e.text, ts)}</div></li>`).join('');
    const p = new URLSearchParams(); if ($('q').value) p.set('q', $('q').value); if (m) p.set('m', m); if ($('s').value) p.set('s', $('s').value);
    history.replaceState(null, '', '?' + p);
  }
  const qp = new URLSearchParams(location.search); ['q', 'm', 's'].forEach(k => { if (qp.has(k)) $(k).value = qp.get(k); });
  fetch('data/entries.json').then(r => r.json()).then(d => { E = d; run(); });
  ['q', 'm', 's'].forEach(k => $(k).addEventListener('input', run));
})();
