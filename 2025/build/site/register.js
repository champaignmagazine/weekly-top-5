// Forecast register search: data/forecast_register.json, filtered in the browser. No outcomes are shown or implied.
(function () {
  const $ = id => document.getElementById(id); let R = [];
  const esc = s => String(s || '').replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const fold = s => String(s || '').toLowerCase().normalize('NFKD').replace(/[̀-ͯ]/g, '').replace(/[’‘]/g, "'").replace(/[“”]/g, '"');
  const terms = q => { const o = []; fold(q).replace(/"([^"]+)"|(\S+)/g, (_, p, w) => { o.push(p || w); return ''; }); return o; };
  const link = u => /^https?:\/\//.test(u) ? `<a href="${esc(u)}" target="_blank" rel="noopener nofollow">${esc(u.length > 70 ? u.slice(0, 70) + '…' : u)}</a>` : esc(u);
  function card(r) {
    const voice = r.voice === 'panel' ? 'panel’s own view' : r.voice;
    const where = r.post ? `<a href="weeks/${esc(r.post)}.html${r.occ ? '#' + esc(r.occ) : ''}">${esc(r.occ || r.post)}</a>` : esc(r.post);
    const det = [['Speaker (panel)', r.sp], ['Attributed to', r.to], ['Basis', r.basis], ['Document in the post', r.doc ? link(r.doc) : ''],
      ['Document opened', r.opened], ['Supports the attribution', r.supports], ['Attribution note', r.note], ['Correction', r.corr],
      ['Condition', r.cond], ['Time expression', r.time], ['Deadline basis', r.dl_basis], ['Horizon', r.horizon], ['Measurability', r.meas],
      ['Item label', r.flag], ['Register note', r.rnote], ['Role', r.role + (r.orig === 'N' ? ' (not an original occurrence)' : '')], ['Story family', r.fam]]
      .filter(([, v]) => v && v !== 'n.a.' && v !== 'not reviewed').map(([k, v]) => `<dt>${esc(k)}</dt><dd>${k === 'Document in the post' ? v : esc(v)}</dd>`).join('');
    return `<li><div class="small"><span class="wid">${esc(r.cid)}</span> ${esc(r.pub)} · ${where} · <span class="chip notev">${esc(r.type)}</span><span class="chip role">${esc(voice)}</span>${r.st !== 'claim' ? '<span class="chip inacc">excluded</span>' : ''}</div>
      <blockquote>${esc(r.q)}</blockquote>${r.para ? `<div class="small">Paraphrase: ${esc(r.para)}</div>` : ''}
      <details><summary>Record</summary><dl>${det}</dl></details></li>`;
  }
  function run() {
    const ts = terms($('q').value), t = $('t').value, v = $('v').value, h = $('h').value, d = $('d').value, o = $('o').checked;
    const res = R.filter(r => (!o || (r.orig === 'Y' && r.st === 'claim')) && (!t || r.type === t) && (!v || r.voice === v) &&
      (!h || r.horizon === h) && (!d || (d === 'yes' ? r.opened === 'yes' : d === 'supports' ? r.supports === 'yes' : r.opened === 'yes' && r.supports === 'no')) &&
      (!ts.length || ts.every(x => fold([r.cid, r.q, r.para, r.sp, r.to, r.note, r.occ].join(' ')).includes(x))));
    $('count').textContent = res.length + (res.length === 1 ? ' claim' : ' claims');
    $('res').innerHTML = res.slice(0, 200).map(card).join('') + (res.length > 200 ? '<li class="small">Showing the first 200. Narrow the search to see more.</li>' : '');
  }
  fetch('data/forecast_register.json').then(r => r.json()).then(d => { R = d; run(); });
  ['q', 't', 'v', 'h', 'd', 'o'].forEach(k => $(k).addEventListener('input', run));
})();
