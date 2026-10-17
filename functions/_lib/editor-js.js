/**
 * Mã chạy trong trình soạn bài: định dạng chữ, chọn từ khoá,
 * chấm điểm SEO theo thời gian thực và lưu bài lên GitHub.
 * Được phục vụ tại /admin/editor.js
 */

export const EDITOR_JS = String.raw`
(function(){
'use strict';

var $ = function(id){ return document.getElementById(id); };
var ed = $('ed');
var keywords = (window.POST.keywords || []).slice();
var cover = window.POST.coverImage || '';
var faqs = (window.POST.faq || []).slice();

/* ---------- bỏ dấu tiếng Việt để tạo đường dẫn ---------- */
function slugify(s){
  return (s || '').normalize('NFD').replace(/[\u0300-\u036f]/g,'')
    .replace(/đ/g,'d').replace(/Đ/g,'D').toLowerCase()
    .replace(/[^a-z0-9\s-]/g,'').trim().replace(/\s+/g,'-')
    .replace(/-+/g,'-').slice(0,80).replace(/^-|-$/g,'');
}
function textOf(html){
  var d = document.createElement('div'); d.innerHTML = html || '';
  return (d.textContent || '').replace(/\s+/g,' ').trim();
}

/* ---------- thanh công cụ định dạng ---------- */
document.querySelectorAll('.ed-bar [data-cmd]').forEach(function(b){
  b.addEventListener('mousedown', function(e){ e.preventDefault(); });
  b.addEventListener('click', function(){
    ed.focus();
    document.execCommand(b.dataset.cmd, false, b.dataset.val || null);
    scheduleScore();
  });
});

$('bLink').addEventListener('click', function(){
  var sel = window.getSelection().toString();
  var url = prompt('Dán đường dẫn vào đây:' + (sel ? '' : '\n(Bôi đen chữ trước khi bấm sẽ đẹp hơn)'), 'https://');
  if(!url || url === 'https://') return;
  ed.focus();
  document.execCommand('createLink', false, url);
  scheduleScore();
});

/* ---------- chèn ảnh vào bài ---------- */
$('bImg').addEventListener('click', function(){ $('imgFile').click(); });
$('imgFile').addEventListener('change', async function(){
  var f = this.files[0]; if(!f) return;
  if(f.size > 5*1024*1024){ alert('Ảnh nặng quá 5 MB, chọn ảnh nhẹ hơn nha.'); return; }
  toast('Đang tải ảnh lên…');
  var url = await uploadImage(f);
  this.value = '';
  if(!url){ toast('Tải ảnh không được', 2600); return; }
  ed.focus();
  document.execCommand('insertHTML', false,
    '<img src="' + url + '" alt="" loading="lazy"><p><br></p>');
  toast('Đã chèn ảnh', 1600);
  scheduleScore();
});

async function uploadImage(f){
  var fd = new FormData(); fd.append('file', f);
  var r = await fetch('/admin/api/media', { method:'POST', body: fd });
  if(!r.ok){ return null; }
  var j = await r.json();
  return j.url;
}

/* ---------- ảnh đại diện ---------- */
function drawCover(){
  var box = $('coverBox');
  if(cover){
    box.innerHTML = '<img src="' + cover + '" alt="" style="width:100%;border-radius:8px;' +
      'aspect-ratio:16/9;object-fit:cover;border:1px solid var(--line)">' +
      '<div class="bar" style="margin-top:9px">' +
      '<button class="btn ghost sm" id="cChange">Đổi ảnh</button>' +
      '<button class="btn danger sm" id="cClear">Bỏ ảnh</button></div>';
    $('cChange').onclick = function(){ $('coverFile').click(); };
    $('cClear').onclick = function(){ cover=''; drawCover(); scheduleScore(); };
  } else {
    box.innerHTML = '<div class="drop" id="cDrop" style="padding:22px">' +
      '<div style="font-size:22px;margin-bottom:5px">🖼</div>' +
      '<div class="muted">Bấm để chọn ảnh đại diện</div></div>';
    $('cDrop').onclick = function(){ $('coverFile').click(); };
  }
}
$('coverFile').addEventListener('change', async function(){
  var f = this.files[0]; if(!f) return;
  if(f.size > 5*1024*1024){ alert('Ảnh nặng quá 5 MB.'); return; }
  toast('Đang tải ảnh lên…');
  var url = await uploadImage(f);
  this.value = '';
  if(!url){ toast('Tải ảnh không được', 2600); return; }
  cover = url; drawCover(); toast('Đã đặt ảnh đại diện', 1600); scheduleScore();
});
drawCover();

/* ---------- từ khoá ---------- */
function drawKeywords(){
  var box = $('chosen');
  box.innerHTML = keywords.length
    ? keywords.map(function(k,i){
        return '<span>' + (i===0 ? '★ ' : '') + escapeHtml(k) +
               '<b data-rm="' + i + '">×</b></span>';
      }).join('')
    : '<span class="muted" style="background:none;color:#999;padding:4px 0">Chưa chọn từ khoá nào</span>';
  box.querySelectorAll('[data-rm]').forEach(function(b){
    b.onclick = function(){ keywords.splice(+b.dataset.rm,1); drawKeywords(); scheduleScore(); };
  });
  document.querySelectorAll('#kwLib .kw').forEach(function(b){
    b.classList.toggle('on', keywords.indexOf(b.dataset.k) >= 0);
  });
}
function escapeHtml(s){
  return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;')
    .replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}
function toggleKw(k){
  var i = keywords.indexOf(k);
  if(i >= 0) keywords.splice(i,1); else keywords.push(k);
  drawKeywords(); scheduleScore();
}

(function buildLibrary(){
  var html = '';
  Object.keys(window.KW_LIB).forEach(function(group){
    html += '<div class="kw-group"><h4>' + escapeHtml(group) + '</h4><div class="kw-list">' +
      window.KW_LIB[group].map(function(k){
        return '<button type="button" class="kw" data-k="' + escapeHtml(k) + '">' +
               escapeHtml(k) + '</button>';
      }).join('') + '</div></div>';
  });
  $('kwLib').innerHTML = html;
  $('kwLib').querySelectorAll('.kw').forEach(function(b){
    b.onclick = function(){ toggleKw(b.dataset.k); };
  });
})();

$('kwAdd').addEventListener('keydown', function(e){
  if(e.key !== 'Enter') return;
  e.preventDefault();
  var v = this.value.trim();
  if(v && keywords.indexOf(v) < 0){ keywords.push(v); drawKeywords(); scheduleScore(); }
  this.value = '';
});
drawKeywords();

/* ---------- câu hỏi thường gặp ---------- */
function drawFaqs(){
  $('faqs').innerHTML = faqs.map(function(f,i){
    return '<div style="border:1px solid var(--line);border-radius:8px;padding:13px;margin-bottom:11px">' +
      '<div class="field" style="margin-bottom:9px"><label>Câu hỏi ' + (i+1) + '</label>' +
      '<input type="text" data-fq="' + i + '" value="' + escapeHtml(f.q||'') + '"></div>' +
      '<div class="field" style="margin-bottom:9px"><label>Trả lời</label>' +
      '<textarea rows="2" data-fa="' + i + '">' + escapeHtml(f.a||'') + '</textarea></div>' +
      '<button class="btn danger sm" type="button" data-fd="' + i + '">Bỏ câu này</button></div>';
  }).join('');
  $('faqs').querySelectorAll('[data-fq]').forEach(function(el){
    el.oninput = function(){ faqs[+el.dataset.fq].q = el.value; };
  });
  $('faqs').querySelectorAll('[data-fa]').forEach(function(el){
    el.oninput = function(){ faqs[+el.dataset.fa].a = el.value; };
  });
  $('faqs').querySelectorAll('[data-fd]').forEach(function(el){
    el.onclick = function(){ faqs.splice(+el.dataset.fd,1); drawFaqs(); };
  });
}
$('addFaq').addEventListener('click', function(){ faqs.push({q:'',a:''}); drawFaqs(); });
drawFaqs();

/* ---------- tự tạo đường dẫn từ tiêu đề ---------- */
var slugTouched = !window.POST.isNew;
$('slug').addEventListener('input', function(){ slugTouched = true; });
$('title').addEventListener('input', function(){
  if(!slugTouched) $('slug').value = slugify(this.value);
  scheduleScore();
});

/* ---------- chấm điểm SEO ---------- */
var timer = null;
function scheduleScore(){ clearTimeout(timer); timer = setTimeout(score, 260); }
['input','keyup','paste'].forEach(function(e){
  ed.addEventListener(e, scheduleScore);
  $('excerpt').addEventListener(e, scheduleScore);
  $('metaTitle').addEventListener(e, scheduleScore);
  $('metaDescription').addEventListener(e, scheduleScore);
  $('coverAlt').addEventListener(e, scheduleScore);
});

function score(){
  var title = $('title').value.trim();
  var mt = ($('metaTitle').value.trim() || (title ? title + ' — VESSCA' : ''));
  var md = ($('metaDescription').value.trim() || $('excerpt').value.trim());
  var body = textOf(ed.innerHTML);
  var words = body ? body.split(/\s+/).length : 0;
  var main = (keywords[0] || '').toLowerCase();
  var lowBody = body.toLowerCase(), lowTitle = title.toLowerCase();
  var firstPara = lowBody.slice(0, 300);
  var h2s = ed.querySelectorAll('h2').length;

  var density = 0;
  if(main && words){
    var hits = lowBody.split(main).length - 1;
    density = hits / words * 100;
  }

  var checks = [
    { ok: title.length >= 10, label: 'Đã có tiêu đề bài viết' },
    { ok: !!main, label: 'Đã chọn từ khoá chính', detail: main ? '★ ' + main : 'Chọn ít nhất 1 từ khoá bên trên' },
    { ok: !!main && lowTitle.indexOf(main) >= 0, label: 'Từ khoá chính nằm trong tiêu đề',
      detail: main ? 'Google ưu tiên bài có từ khoá ngay ở tiêu đề' : '' },
    { ok: !!main && firstPara.indexOf(main) >= 0, label: 'Từ khoá chính xuất hiện ở đoạn mở đầu' },
    { ok: keywords.length >= 3, label: 'Có từ 3 từ khoá trở lên', detail: 'Đang có ' + keywords.length },
    { ok: mt.length >= 30 && mt.length <= 62, label: 'Tiêu đề SEO dài vừa đủ',
      detail: mt.length + ' ký tự (tốt nhất 30–62)' },
    { ok: md.length >= 110 && md.length <= 160, label: 'Mô tả SEO dài vừa đủ',
      detail: md.length + ' ký tự (tốt nhất 110–160)' },
    { ok: words >= 300, label: 'Bài đủ dài', detail: words + ' từ (nên từ 300 trở lên)' },
    { ok: h2s >= 2, label: 'Có tiêu đề phụ chia đoạn', detail: 'Đang có ' + h2s + ' mục H2' },
    { ok: !!cover, label: 'Đã có ảnh đại diện' },
    { ok: !!cover && $('coverAlt').value.trim().length >= 5, label: 'Ảnh đại diện có mô tả' },
    { ok: !main || (density >= 0.3 && density <= 3),
      label: 'Mật độ từ khoá hợp lý',
      detail: main ? density.toFixed(1) + '% (tốt nhất 0.3–3%)' : 'Chọn từ khoá chính trước' },
    { ok: faqs.filter(function(f){ return f.q && f.a; }).length > 0,
      label: 'Có câu hỏi thường gặp', detail: 'Giúp Google hiện câu trả lời ngay trên kết quả tìm kiếm' }
  ];

  var passed = checks.filter(function(c){ return c.ok; }).length;
  var pct = Math.round(passed / checks.length * 100);
  $('scoreNum').textContent = pct;
  $('scoreBar').style.width = pct + '%';
  $('scoreBar').style.background = pct >= 80 ? '#157a3f' : pct >= 50 ? '#B06A00' : '#B3261E';
  $('checks').innerHTML = checks.map(function(c){
    return '<div class="chk ' + (c.ok ? 'y' : 'n') + '"><span class="ic">' +
      (c.ok ? '✓' : '!') + '</span><span>' + escapeHtml(c.label) +
      (c.detail ? '<br><span class="muted">' + escapeHtml(c.detail) + '</span>' : '') +
      '</span></div>';
  }).join('');

  // đếm ký tự
  setCount('mtCount', mt.length, 30, 62);
  setCount('mdCount', md.length, 110, 160);

  // xem trước trên Google
  $('gT').textContent = mt || 'Tiêu đề bài viết';
  $('gU').textContent = 'vessca.com › blog › ' + ($('slug').value || '…');
  $('gD').textContent = md || 'Mô tả bài viết sẽ hiện ở đây.';
}
function setCount(id, n, lo, hi){
  var el = $(id);
  el.textContent = n + ' ký tự';
  el.className = 'count ' + (n === 0 ? '' : (n >= lo && n <= hi) ? 'good' : 'bad');
}

/* ---------- thông báo nhỏ ---------- */
var toastEl = null, toastT = null;
function toast(msg, ms){
  if(!toastEl){ toastEl = document.createElement('div'); toastEl.className='saving'; document.body.appendChild(toastEl); }
  toastEl.textContent = msg; toastEl.style.display = 'block';
  clearTimeout(toastT);
  if(ms) toastT = setTimeout(function(){ toastEl.style.display='none'; }, ms);
}

/* ---------- lưu nháp tạm trong máy, tránh mất bài ---------- */
var DRAFT = 'vessca_draft_' + (window.POST.slug || 'new');
function saveLocal(){
  try{
    localStorage.setItem(DRAFT, JSON.stringify({
      title:$('title').value, content:ed.innerHTML, excerpt:$('excerpt').value, t:Date.now()
    }));
  }catch(e){}
}
setInterval(saveLocal, 8000);

(function restore(){
  try{
    var raw = localStorage.getItem(DRAFT); if(!raw) return;
    var d = JSON.parse(raw);
    if(Date.now() - d.t > 3*24*3600*1000){ localStorage.removeItem(DRAFT); return; }
    var same = d.title === $('title').value && d.content === ed.innerHTML;
    if(same) return;
    if(confirm('Có bản nháp chưa lưu từ lần trước. Khôi phục lại không?')){
      $('title').value = d.title || ''; ed.innerHTML = d.content || '';
      $('excerpt').value = d.excerpt || '';
    } else localStorage.removeItem(DRAFT);
  }catch(e){}
})();

/* ---------- lưu bài lên GitHub ---------- */
$('save').addEventListener('click', async function(){
  var btn = this;
  var title = $('title').value.trim();
  if(!title){ alert('Nhập tiêu đề bài viết đã nha.'); $('title').focus(); return; }
  var slug = ($('slug').value.trim() || slugify(title));
  if(!slug){ alert('Đường dẫn không hợp lệ, sửa lại giúp tui.'); return; }
  if(!textOf(ed.innerHTML)){ alert('Bài chưa có nội dung.'); ed.focus(); return; }

  var payload = {
    slug: slug,
    oldSlug: window.POST.slug || '',
    title: title,
    category: $('category').value,
    excerpt: $('excerpt').value.trim(),
    metaTitle: $('metaTitle').value.trim(),
    metaDescription: $('metaDescription').value.trim(),
    keywords: keywords,
    coverImage: cover,
    coverAlt: $('coverAlt').value.trim(),
    content: ed.innerHTML,
    status: $('status').value,
    faq: faqs.filter(function(f){ return f.q && f.a; }),
    publishedAt: window.POST.publishedAt || ''
  };

  btn.disabled = true; toast('Đang lưu bài…');
  try{
    var r = await fetch('/admin/api/save', {
      method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(payload)
    });
    if(!r.ok) throw new Error(await r.text());
    try{ localStorage.removeItem(DRAFT); }catch(e){}
    toast('Đã lưu! Web cập nhật sau ~1 phút.', 2500);
    setTimeout(function(){
      location.href = '/admin/?msg=' + encodeURIComponent('Đã lưu "' + title + '". Web sẽ cập nhật sau khoảng 1 phút.');
    }, 800);
  }catch(err){
    toast('Lưu không được', 1);
    alert('Lưu không được:\n' + err.message);
    btn.disabled = false;
  }
});

score();
})();
`;
