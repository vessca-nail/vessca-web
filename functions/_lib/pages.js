/** Giao diện trang quản trị VESSCA — toàn bộ HTML/CSS của khu vực /admin */

import { keywordLibrary, categories } from '../../site.config.mjs';

const esc = (s = '') =>
  String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;').replace(/'/g, '&#39;');

const CSS = `
:root{--ink:#111;--soft:#6E6E6E;--line:#E4E4E4;--bg:#FAFAFA;--panel:#fff;
 --ok:#157a3f;--warn:#B06A00;--bad:#B3261E;--serif:Georgia,serif;}
*{margin:0;padding:0;box-sizing:border-box;}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
 background:var(--bg);color:var(--ink);line-height:1.6;font-size:15px;}
a{color:inherit;}
.top{background:var(--ink);color:#fff;padding:0 26px;position:sticky;top:0;z-index:30;}
.top-in{max-width:1180px;margin:0 auto;display:flex;align-items:center;
 justify-content:space-between;gap:18px;height:60px;}
.brand{display:flex;align-items:center;gap:10px;font-family:var(--serif);
 font-size:18px;letter-spacing:.18em;}
.brand .dot{width:26px;height:26px;border-radius:50%;background:#fff;color:#111;
 display:grid;place-items:center;font-size:14px;font-family:var(--serif);letter-spacing:0;}
.top nav{display:flex;gap:4px;align-items:center;}
.top nav a{padding:8px 14px;border-radius:7px;font-size:14px;color:#CFCFCF;}
.top nav a:hover{background:rgba(255,255,255,.1);color:#fff;}
.top nav a.on{background:#fff;color:#111;}
.wrap{max-width:1180px;margin:0 auto;padding:30px 26px 70px;}
h1{font-family:var(--serif);font-weight:400;font-size:30px;margin-bottom:6px;}
.lede{color:var(--soft);margin-bottom:26px;}
.card{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:22px;}
.card+.card{margin-top:18px;}
.card h2{font-size:17px;font-weight:600;margin-bottom:4px;}
.card h2+p{color:var(--soft);font-size:14px;margin-bottom:16px;}
label{display:block;font-weight:600;font-size:13.5px;margin-bottom:6px;}
label .hint{font-weight:400;color:var(--soft);font-size:12.5px;}
input[type=text],input[type=password],input[type=url],input[type=date],textarea,select{
 width:100%;padding:11px 13px;border:1px solid var(--line);border-radius:8px;
 font:inherit;font-size:14.5px;background:#fff;color:var(--ink);}
input:focus,textarea:focus,select:focus{outline:2px solid var(--ink);outline-offset:-1px;border-color:var(--ink);}
textarea{resize:vertical;min-height:80px;}
.field{margin-bottom:17px;}
.row{display:grid;grid-template-columns:1fr 1fr;gap:16px;}
.btn{display:inline-flex;align-items:center;gap:8px;padding:11px 20px;border-radius:8px;
 border:1px solid var(--ink);background:var(--ink);color:#fff;font:inherit;font-size:14px;
 font-weight:500;cursor:pointer;transition:.18s;}
.btn:hover{opacity:.84;}
.btn.ghost{background:#fff;color:var(--ink);}
.btn.ghost:hover{background:#F2F2F2;opacity:1;}
.btn.danger{background:#fff;color:var(--bad);border-color:#E7C4C1;}
.btn.danger:hover{background:#FDF3F2;}
.btn:disabled{opacity:.5;cursor:not-allowed;}
.btn.sm{padding:7px 13px;font-size:13px;}
.bar{display:flex;gap:10px;flex-wrap:wrap;align-items:center;}
.muted{color:var(--soft);font-size:13.5px;}
.pill{display:inline-block;padding:3px 10px;border-radius:999px;font-size:12px;font-weight:600;}
.pill.pub{background:#E8F5EC;color:#157a3f;}
.pill.draft{background:#F1F1F1;color:#666;}
.note{padding:13px 15px;border-radius:9px;font-size:14px;margin-bottom:18px;}
.note.err{background:#FDF3F2;border:1px solid #F0D5D2;color:#8E201A;}
.note.ok{background:#EDF7F0;border:1px solid #CCE7D6;color:#13643A;}
.note.warn{background:#FFF8EC;border:1px solid #F3E2C0;color:#7A4B00;}
table{width:100%;border-collapse:collapse;}
th,td{text-align:left;padding:12px 10px;border-bottom:1px solid var(--line);font-size:14px;
 vertical-align:middle;}
th{font-size:12px;text-transform:uppercase;letter-spacing:.07em;color:var(--soft);font-weight:600;}
tr:last-child td{border-bottom:none;}
.empty{text-align:center;padding:50px 20px;color:var(--soft);}

/* ---- trình soạn thảo ---- */
.ed-wrap{border:1px solid var(--line);border-radius:9px;overflow:hidden;background:#fff;}
.ed-bar{display:flex;gap:2px;flex-wrap:wrap;padding:7px;border-bottom:1px solid var(--line);
 background:#FCFCFC;position:sticky;top:60px;z-index:5;}
.ed-bar button{border:none;background:none;padding:7px 10px;border-radius:6px;cursor:pointer;
 font:inherit;font-size:13.5px;color:#333;min-width:34px;}
.ed-bar button:hover{background:#ECECEC;}
.ed-bar .sep{width:1px;background:var(--line);margin:4px 5px;}
.ed{min-height:420px;padding:22px 24px;font-size:16.5px;line-height:1.8;outline:none;}
.ed:empty::before{content:attr(data-ph);color:#AAA;}
.ed h2{font-family:var(--serif);font-size:25px;margin:1.5em 0 .5em;font-weight:400;}
.ed h3{font-family:var(--serif);font-size:20px;margin:1.3em 0 .4em;font-weight:400;}
.ed p{margin:0 0 1em;}
.ed ul,.ed ol{margin:0 0 1em 1.3em;}
.ed blockquote{border-left:3px solid #111;padding-left:16px;margin:1.2em 0;color:#444;font-style:italic;}
.ed img{max-width:100%;height:auto;margin:1.2em 0;border-radius:4px;}
.ed a{color:#0b5ed7;text-decoration:underline;}

/* ---- bảng điều khiển SEO ---- */
.seo-side{position:sticky;top:78px;}
.chk{display:flex;gap:9px;align-items:flex-start;padding:7px 0;font-size:13.5px;
 border-bottom:1px solid #F0F0F0;}
.chk:last-child{border-bottom:none;}
.chk .ic{flex:none;width:17px;height:17px;border-radius:50%;display:grid;place-items:center;
 font-size:10.5px;color:#fff;margin-top:3px;font-weight:700;}
.chk.y .ic{background:#157a3f;}
.chk.n .ic{background:#C9CDD2;}
.score{display:flex;align-items:baseline;gap:9px;margin-bottom:12px;}
.score b{font-size:32px;font-family:var(--serif);font-weight:400;}
.meter{height:6px;background:#EEE;border-radius:99px;overflow:hidden;margin-bottom:16px;}
.meter i{display:block;height:100%;background:#157a3f;transition:width .3s;}
.kw-group{margin-bottom:13px;}
.kw-group h4{font-size:11.5px;text-transform:uppercase;letter-spacing:.06em;
 color:var(--soft);margin-bottom:7px;font-weight:600;}
.kw-list{display:flex;gap:5px;flex-wrap:wrap;}
.kw{border:1px solid var(--line);background:#fff;border-radius:999px;padding:4px 11px;
 font-size:12.5px;cursor:pointer;font-family:inherit;color:#444;}
.kw:hover{border-color:var(--ink);}
.kw.on{background:var(--ink);color:#fff;border-color:var(--ink);}
.chosen{display:flex;gap:6px;flex-wrap:wrap;min-height:30px;}
.chosen span{background:#111;color:#fff;border-radius:999px;padding:4px 10px;font-size:12.5px;
 display:inline-flex;gap:7px;align-items:center;}
.chosen span b{cursor:pointer;font-weight:400;opacity:.65;}
.chosen span b:hover{opacity:1;}
.count{font-size:12px;color:var(--soft);margin-top:5px;}
.count.bad{color:var(--bad);}
.count.good{color:#157a3f;}
.grid2{display:grid;grid-template-columns:1fr 330px;gap:20px;align-items:start;}
.drop{border:2px dashed var(--line);border-radius:10px;padding:30px;text-align:center;
 color:var(--soft);cursor:pointer;background:#fff;}
.drop:hover,.drop.over{border-color:var(--ink);color:var(--ink);background:#FCFCFC;}
.thumb{width:76px;height:56px;object-fit:cover;border-radius:5px;border:1px solid var(--line);}
.saving{position:fixed;left:50%;bottom:26px;transform:translateX(-50%);background:#111;
 color:#fff;padding:11px 22px;border-radius:999px;font-size:14px;z-index:60;
 box-shadow:0 6px 24px rgba(0,0,0,.2);}
@media(max-width:900px){
 .grid2,.row{grid-template-columns:1fr;}
 .seo-side{position:static;}
 .top nav a{padding:8px 10px;font-size:13px;}
 .brand span.nm{display:none;}
}
`;

const MARK = `<span class="dot">V</span>`;

export function shell({ title, body, active = '', wide = false }) {
  return `<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>${esc(title)} — Quản trị VESSCA</title>
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<style>${CSS}</style>
</head>
<body>
<header class="top">
  <div class="top-in">
    <a href="/admin/" class="brand">${MARK}<span class="nm">VESSCA</span></a>
    <nav>
      <a href="/admin/" class="${active === 'home' ? 'on' : ''}">Bài viết</a>
      <a href="/admin/new" class="${active === 'new' ? 'on' : ''}">Viết bài</a>
      <a href="/admin/design" class="${active === 'design' ? 'on' : ''}">Giao diện</a>
      <a href="/admin/media" class="${active === 'media' ? 'on' : ''}">Ảnh</a>
      <a href="/admin/bookings" class="${active === 'bookings' ? 'on' : ''}">Đặt lịch</a>
      <a href="/admin/thong-ke" class="${active === 'thongke' ? 'on' : ''}">Thống kê</a>
      <a href="/admin/status" class="${active === 'status' ? 'on' : ''}">Hệ thống</a>
      <a href="/admin/logout">Thoát</a>
    </nav>
  </div>
</header>
<div class="wrap" ${wide ? 'style="max-width:1320px"' : ''}>${body}</div>
<script>try{localStorage.setItem('vsNoTk','1')}catch(e){}</script>
</body>
</html>`;
}

export function loginPage(error = '', setupHint = '') {
  return `<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Đăng nhập — Quản trị VESSCA</title>
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<style>${CSS}
body{display:grid;place-items:center;min-height:100vh;background:#111;}
.box{background:#fff;border-radius:14px;padding:38px 34px;width:min(400px,92vw);}
.box .mk{width:50px;height:50px;border-radius:50%;background:#111;color:#fff;
 display:grid;place-items:center;font-family:var(--serif);font-size:25px;margin:0 auto 18px;}
.box h1{text-align:center;font-size:22px;letter-spacing:.2em;margin-bottom:4px;}
.box .sub{text-align:center;color:var(--soft);font-size:12px;letter-spacing:.14em;
 text-transform:uppercase;margin-bottom:26px;}
</style>
</head>
<body>
<form class="box" method="POST" action="/admin/login">
  <div class="mk">V</div>
  <h1>VESSCA</h1>
  <div class="sub">Khu vực quản trị</div>
  ${error ? `<div class="note err">${esc(error)}</div>` : ''}
  ${setupHint ? `<div class="note warn">${setupHint}</div>` : ''}
  <div class="field">
    <label for="pw">Mật khẩu</label>
    <input type="password" id="pw" name="password" autofocus autocomplete="current-password" required>
  </div>
  <button class="btn" style="width:100%;justify-content:center">Đăng nhập</button>
</form>
</body>
</html>`;
}

/** Trang danh sách bài viết */
export function listPage({ posts, flash }) {
  const rows = posts.length
    ? posts
        .map(
          (p) => `<tr>
  <td style="width:90px">${
    p.coverImage
      ? `<img class="thumb" src="${esc(p.coverImage)}" alt="">`
      : `<div class="thumb" style="background:#F2F2F2"></div>`
  }</td>
  <td>
    <div style="font-weight:600;margin-bottom:3px">${esc(p.title)}</div>
    <div class="muted">${esc(p.category || '—')} · ${esc((p.publishedAt || '').slice(0, 10))}</div>
  </td>
  <td style="width:110px"><span class="pill ${p.status === 'published' ? 'pub' : 'draft'}">${
            p.status === 'published' ? 'Đã đăng' : 'Bản nháp'
          }</span></td>
  <td style="width:230px">
    <div class="bar">
      <a class="btn ghost sm" href="/admin/edit/${esc(p.slug)}">Sửa</a>
      ${
        p.status === 'published'
          ? `<a class="btn ghost sm" href="/blog/${esc(p.slug)}/" target="_blank">Xem</a>`
          : ''
      }
      <button class="btn danger sm" data-del="${esc(p.slug)}">Xoá</button>
    </div>
  </td>
</tr>`
        )
        .join('')
    : '';

  return shell({
    active: 'home',
    title: 'Bài viết',
    body: `
<h1>Bài viết</h1>
<p class="lede">Mỗi bài đăng thêm là thêm một cánh cửa để khách tìm thấy tiệm trên Google.</p>
${flash ? `<div class="note ok">${esc(flash)}</div>` : ''}
<div class="bar" style="margin-bottom:18px">
  <a class="btn" href="/admin/new">+ Viết bài mới</a>
  <a class="btn ghost" href="/blog" target="_blank">Xem trang blog</a>
</div>
<div class="card" style="padding:6px 16px">
  ${
    rows
      ? `<table><thead><tr><th></th><th>Tiêu đề</th><th>Trạng thái</th><th></th></tr></thead><tbody>${rows}</tbody></table>`
      : `<div class="empty"><p style="margin-bottom:16px">Chưa có bài viết nào.</p>
         <a class="btn" href="/admin/new">Viết bài đầu tiên</a></div>`
  }
</div>
<script>
document.querySelectorAll('[data-del]').forEach(function(b){
  b.addEventListener('click', async function(){
    var slug = b.dataset.del;
    if(!confirm('Xoá bài này? Không khôi phục lại được từ trang admin.')) return;
    b.disabled = true; b.textContent = 'Đang xoá…';
    var r = await fetch('/admin/api/delete', {method:'POST',
      headers:{'Content-Type':'application/json'}, body: JSON.stringify({slug:slug})});
    if(r.ok) location.href = '/admin/?msg=' + encodeURIComponent('Đã xoá bài viết. Web sẽ cập nhật sau khoảng 1 phút.');
    else { alert('Xoá không được: ' + await r.text()); b.disabled=false; b.textContent='Xoá'; }
  });
});
</script>`,
  });
}

/** Trang viết / sửa bài */
export function editorPage({ post, isNew }) {
  const p = post || {};
  const kwJson = JSON.stringify(keywordLibrary).replace(/</g, '\\u003c');
  const catOpts = categories
    .map((c) => `<option ${p.category === c ? 'selected' : ''}>${esc(c)}</option>`)
    .join('');

  return shell({
    active: isNew ? 'new' : '',
    wide: true,
    title: isNew ? 'Viết bài mới' : 'Sửa bài',
    body: `
<h1>${isNew ? 'Viết bài mới' : 'Sửa bài viết'}</h1>
<p class="lede">Viết xong bấm Lưu. Khoảng 1 phút sau bài sẽ xuất hiện trên web.</p>

<div class="grid2">
  <div>
    <div class="card">
      <div class="field">
        <label for="title">Tiêu đề bài viết</label>
        <input type="text" id="title" value="${esc(p.title || '')}"
          placeholder="VD: Sơn gel có hại cho móng không?">
      </div>

      <div class="row">
        <div class="field">
          <label for="slug">Đường dẫn <span class="hint">— phần sau vessca.com/blog/</span></label>
          <input type="text" id="slug" value="${esc(p.slug || '')}" placeholder="tu-dong-tao">
        </div>
        <div class="field">
          <label for="category">Danh mục</label>
          <select id="category"><option value="">— Chọn —</option>${catOpts}</select>
        </div>
      </div>

      <div class="field">
        <label for="excerpt">Tóm tắt ngắn <span class="hint">— hiện ở trang danh sách blog</span></label>
        <textarea id="excerpt" rows="2" placeholder="1–2 câu gọn gàng về nội dung bài.">${esc(p.excerpt || '')}</textarea>
      </div>
    </div>

    <div class="card">
      <h2>Nội dung</h2>
      <p>Bôi đen chữ rồi bấm nút định dạng. Chèn ảnh bằng nút Ảnh.</p>
      <div class="ed-wrap">
        <div class="ed-bar">
          <button type="button" data-cmd="formatBlock" data-val="h2" title="Tiêu đề lớn"><b>H2</b></button>
          <button type="button" data-cmd="formatBlock" data-val="h3" title="Tiêu đề nhỏ"><b>H3</b></button>
          <button type="button" data-cmd="formatBlock" data-val="p" title="Đoạn thường">¶</button>
          <span class="sep"></span>
          <button type="button" data-cmd="bold" title="In đậm"><b>B</b></button>
          <button type="button" data-cmd="italic" title="In nghiêng"><i>I</i></button>
          <span class="sep"></span>
          <button type="button" data-cmd="insertUnorderedList" title="Danh sách chấm">• —</button>
          <button type="button" data-cmd="insertOrderedList" title="Danh sách số">1. —</button>
          <button type="button" data-cmd="formatBlock" data-val="blockquote" title="Trích dẫn">❝</button>
          <span class="sep"></span>
          <button type="button" id="bLink" title="Chèn link">🔗 Link</button>
          <button type="button" id="bImg" title="Chèn ảnh">🖼 Ảnh</button>
          <button type="button" data-cmd="insertHorizontalRule" title="Đường kẻ ngang">—</button>
          <span class="sep"></span>
          <button type="button" data-cmd="removeFormat" title="Xoá định dạng">Xoá ĐD</button>
        </div>
        <div class="ed" id="ed" contenteditable="true"
          data-ph="Bắt đầu viết ở đây…">${p.content || ''}</div>
      </div>
      <input type="file" id="imgFile" accept="image/*" hidden>
    </div>

    <div class="card">
      <h2>Câu hỏi thường gặp <span class="hint" style="font-weight:400">(không bắt buộc)</span></h2>
      <p>Thêm câu hỏi ở đây thì Google có thể hiện trực tiếp câu trả lời ngay dưới kết quả tìm kiếm — rất đáng làm.</p>
      <div id="faqs"></div>
      <button class="btn ghost sm" type="button" id="addFaq">+ Thêm câu hỏi</button>
    </div>
  </div>

  <div class="seo-side">
    <div class="card">
      <h2>Điểm SEO</h2>
      <div class="score"><b id="scoreNum">0</b><span class="muted">/ 100</span></div>
      <div class="meter"><i id="scoreBar" style="width:0%"></i></div>
      <div id="checks"></div>
    </div>

    <div class="card">
      <h2>Từ khoá</h2>
      <p>Bấm chọn từ khoá khách hay tìm. Từ đầu tiên là từ khoá chính.</p>
      <div class="chosen" id="chosen"></div>
      <div style="margin:14px 0 4px"><input type="text" id="kwAdd" placeholder="Tự nhập từ khoá rồi Enter…"></div>
      <div id="kwLib" style="margin-top:14px"></div>
    </div>

    <div class="card">
      <h2>Hiện trên Google</h2>
      <div class="field">
        <label for="metaTitle">Tiêu đề SEO</label>
        <input type="text" id="metaTitle" value="${esc(p.metaTitle || '')}"
          placeholder="Để trống sẽ dùng tiêu đề bài">
        <div class="count" id="mtCount"></div>
      </div>
      <div class="field">
        <label for="metaDescription">Mô tả SEO</label>
        <textarea id="metaDescription" rows="3"
          placeholder="Câu mô tả hiện dưới tiêu đề trên Google.">${esc(p.metaDescription || '')}</textarea>
        <div class="count" id="mdCount"></div>
      </div>
      <div style="border:1px solid var(--line);border-radius:8px;padding:12px;background:#fff">
        <div style="color:#1a0dab;font-size:16px;line-height:1.3" id="gT">Tiêu đề bài viết</div>
        <div style="color:#006621;font-size:12.5px;margin:2px 0 3px" id="gU">vessca.com › blog</div>
        <div style="color:#545454;font-size:13px" id="gD">Mô tả bài viết sẽ hiện ở đây.</div>
      </div>
    </div>

    <div class="card">
      <h2>Ảnh đại diện</h2>
      <div id="coverBox"></div>
      <input type="file" id="coverFile" accept="image/*" hidden>
      <div class="field" style="margin-top:12px">
        <label for="coverAlt">Mô tả ảnh <span class="hint">— giúp Google hiểu ảnh</span></label>
        <input type="text" id="coverAlt" value="${esc(p.coverAlt || '')}"
          placeholder="VD: Bộ móng gel màu nude tại VESSCA">
      </div>
    </div>

    <div class="card">
      <div class="field">
        <label for="status">Trạng thái</label>
        <select id="status">
          <option value="published" ${p.status === 'published' ? 'selected' : ''}>Đăng công khai</option>
          <option value="draft" ${p.status !== 'published' ? 'selected' : ''}>Bản nháp (chưa hiện)</option>
        </select>
      </div>
      <button class="btn" id="save" style="width:100%;justify-content:center">Lưu bài viết</button>
      <p class="muted" style="margin-top:10px;text-align:center">Web cập nhật sau ~1 phút</p>
    </div>
  </div>
</div>

<script>
window.KW_LIB = ${kwJson};
window.POST = ${JSON.stringify({
      slug: p.slug || '',
      keywords: p.keywords || [],
      coverImage: p.coverImage || '',
      faq: p.faq || [],
      isNew,
      publishedAt: p.publishedAt || '',
    }).replace(/</g, '\\u003c')};
</script>
<script src="/admin/editor.js"></script>`,
  });
}

/** Trang đổi giao diện (thả file HTML mới) */
export function designPage({ history, flash, error, currentSize }) {
  const rows = history.length
    ? history
        .map(
          (h) => `<tr>
  <td>${esc(new Date(h.date).toLocaleString('vi-VN', { timeZone: 'Asia/Ho_Chi_Minh' }))}</td>
  <td class="muted">${esc(h.message)}</td>
  <td style="width:130px"><button class="btn ghost sm" data-restore="${esc(h.sha)}">Quay lui bản này</button></td>
</tr>`
        )
        .join('')
    : '<tr><td colspan="3" class="muted" style="padding:18px 10px">Chưa có thay đổi nào.</td></tr>';

  return shell({
    active: 'design',
    title: 'Giao diện',
    body: `
<h1>Giao diện trang chủ</h1>
<p class="lede">Thả file <b>index.html</b> mới vào đây để đổi toàn bộ giao diện trang chủ.</p>

${flash ? `<div class="note ok">${esc(flash)}</div>` : ''}
${error ? `<div class="note err">${esc(error)}</div>` : ''}

<div class="note warn">
  <b>Yên tâm:</b> mỗi lần đổi đều được lưu lại. Nếu file mới bị lỗi, bấm
  <b>Quay lui</b> ở bảng bên dưới là trang chủ trở lại như cũ.
  Phần Blog, logo và thẻ SEO sẽ được tự gắn lại vào file mới — bạn không cần lo.
</div>

<div class="card">
  <h2>Thả file HTML mới</h2>
  <p>Trang chủ hiện tại nặng ${currentSize ? Math.round(currentSize / 1024) + ' KB' : '—'}.</p>
  <div class="drop" id="drop">
    <div style="font-size:26px;margin-bottom:8px">📄</div>
    <div><b>Kéo file index.html vào đây</b></div>
    <div class="muted" style="margin-top:4px">hoặc bấm để chọn file từ máy</div>
  </div>
  <input type="file" id="file" accept=".html,.htm,text/html" hidden>
  <div id="picked" style="margin-top:14px"></div>
</div>

<div class="card">
  <h2>Lịch sử thay đổi</h2>
  <p>15 lần đổi giao diện gần nhất.</p>
  <table><tbody>${rows}</tbody></table>
</div>

<script>
var drop = document.getElementById('drop'), file = document.getElementById('file'),
    picked = document.getElementById('picked');

drop.addEventListener('click', function(){ file.click(); });
['dragenter','dragover'].forEach(function(e){
  drop.addEventListener(e, function(ev){ ev.preventDefault(); drop.classList.add('over'); });
});
['dragleave','drop'].forEach(function(e){
  drop.addEventListener(e, function(ev){ ev.preventDefault(); drop.classList.remove('over'); });
});
drop.addEventListener('drop', function(ev){
  if(ev.dataTransfer.files[0]) handle(ev.dataTransfer.files[0]);
});
file.addEventListener('change', function(){ if(file.files[0]) handle(file.files[0]); });

function handle(f){
  if(!/\\.html?$/i.test(f.name)){ alert('Phải là file .html nha.'); return; }
  var r = new FileReader();
  r.onload = function(){
    var html = r.result;
    if(!/<html[\\s>]/i.test(html) || !/<body[\\s>]/i.test(html)){
      if(!confirm('File này trông không giống một trang HTML hoàn chỉnh. Vẫn dùng?')) return;
    }
    picked.innerHTML = '<div class="note ok">Đã đọc <b>' + f.name + '</b> (' +
      Math.round(f.size/1024) + ' KB). Bấm nút dưới để áp dụng.</div>' +
      '<button class="btn" id="go">Áp dụng giao diện này</button>';
    document.getElementById('go').addEventListener('click', function(){
      send(html, this);
    });
  };
  r.readAsText(f, 'utf-8');
}

async function send(html, btn){
  btn.disabled = true; btn.textContent = 'Đang gửi lên…';
  var r = await fetch('/admin/api/design', {method:'POST',
    headers:{'Content-Type':'application/json'}, body: JSON.stringify({html:html})});
  if(r.ok) location.href = '/admin/design?msg=' +
    encodeURIComponent('Đã đổi giao diện. Trang chủ sẽ cập nhật sau khoảng 1 phút.');
  else { alert('Không gửi được: ' + await r.text()); btn.disabled=false; btn.textContent='Áp dụng giao diện này'; }
}

document.querySelectorAll('[data-restore]').forEach(function(b){
  b.addEventListener('click', async function(){
    if(!confirm('Quay lui trang chủ về bản này?')) return;
    b.disabled = true; b.textContent = 'Đang quay lui…';
    var r = await fetch('/admin/api/restore', {method:'POST',
      headers:{'Content-Type':'application/json'}, body: JSON.stringify({sha:b.dataset.restore})});
    if(r.ok) location.href = '/admin/design?msg=' +
      encodeURIComponent('Đã quay lui giao diện. Cập nhật sau khoảng 1 phút.');
    else { alert('Không quay lui được: ' + await r.text()); b.disabled=false; b.textContent='Quay lui bản này'; }
  });
});
</script>`,
  });
}

/** Trang quản lý ảnh */
export function mediaPage({ files, flash }) {
  const cards = files.length
    ? files
        .map(
          (f) => `<div style="border:1px solid var(--line);border-radius:9px;overflow:hidden;background:#fff">
  <img src="/media/${esc(f.name)}" alt="" style="width:100%;aspect-ratio:4/3;object-fit:cover;display:block">
  <div style="padding:9px 11px">
    <div style="font-size:12.5px;word-break:break-all;margin-bottom:7px">${esc(f.name)}</div>
    <button class="btn ghost sm" data-copy="/media/${esc(f.name)}">Chép đường dẫn</button>
  </div>
</div>`
        )
        .join('')
    : '';

  return shell({
    active: 'media',
    title: 'Ảnh',
    body: `
<h1>Thư viện ảnh</h1>
<p class="lede">Ảnh tải lên đây dùng được cho mọi bài viết.</p>
${flash ? `<div class="note ok">${esc(flash)}</div>` : ''}

<div class="card">
  <div class="drop" id="drop">
    <div style="font-size:26px;margin-bottom:8px">🖼</div>
    <div><b>Kéo ảnh vào đây</b></div>
    <div class="muted" style="margin-top:4px">hoặc bấm để chọn — JPG, PNG, WebP, tối đa 5 MB</div>
  </div>
  <input type="file" id="file" accept="image/*" multiple hidden>
  <div id="prog" style="margin-top:12px"></div>
</div>

<div class="card">
  ${
    cards
      ? `<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(185px,1fr));gap:15px">${cards}</div>`
      : '<div class="empty">Chưa có ảnh nào.</div>'
  }
</div>

<script>
var drop=document.getElementById('drop'), file=document.getElementById('file'), prog=document.getElementById('prog');
drop.addEventListener('click',function(){file.click();});
['dragenter','dragover'].forEach(function(e){drop.addEventListener(e,function(ev){ev.preventDefault();drop.classList.add('over');});});
['dragleave','drop'].forEach(function(e){drop.addEventListener(e,function(ev){ev.preventDefault();drop.classList.remove('over');});});
drop.addEventListener('drop',function(ev){ up(ev.dataTransfer.files); });
file.addEventListener('change',function(){ up(file.files); });

async function up(list){
  var files = Array.from(list).filter(function(f){ return f.type.indexOf('image/')===0; });
  if(!files.length) return;
  for (var i=0;i<files.length;i++){
    var f = files[i];
    prog.innerHTML = '<div class="note ok">Đang tải ' + (i+1) + '/' + files.length + ': ' + f.name + '…</div>';
    if(f.size > 5*1024*1024){ prog.innerHTML = '<div class="note err">' + f.name + ' nặng quá 5 MB.</div>'; continue; }
    var fd = new FormData(); fd.append('file', f);
    var r = await fetch('/admin/api/media', {method:'POST', body: fd});
    if(!r.ok){ prog.innerHTML = '<div class="note err">Lỗi: ' + await r.text() + '</div>'; return; }
  }
  location.href = '/admin/media?msg=' + encodeURIComponent('Đã tải ảnh lên. Ảnh dùng được sau khoảng 1 phút.');
}

document.querySelectorAll('[data-copy]').forEach(function(b){
  b.addEventListener('click',function(){
    navigator.clipboard.writeText(b.dataset.copy);
    var t=b.textContent; b.textContent='Đã chép!'; setTimeout(function(){b.textContent=t;},1400);
  });
});
</script>`,
  });
}

/** Trang kiểm tra hệ thống */
/** Trang xem đơn đặt lịch khách gửi từ website */
export function bookingsPage({ bookings, pollKey, flash, error }) {
  const NHAN = {
    moi: ['Mới', 'draft'],
    da_xem: ['Đã xem', 'draft'],
    da_xac_nhan: ['Đã xác nhận', 'pub'],
    huy: ['Đã huỷ', 'draft'],
  };

  const rows = bookings
    .map((b) => {
      const [nhan, lop] = NHAN[b.status] || ['—', 'draft'];
      const tel = String(b.phone || '').replace(/[^\d+]/g, '');
      return `<tr>
  <td style="width:132px">
    <div style="font-weight:600">${esc(b.created_at_vn)}</div>
    <div class="muted">#${b.id}</div>
  </td>
  <td>
    <div style="font-weight:600;margin-bottom:3px">${esc(b.name)}</div>
    <div class="muted">${esc(b.service || 'Chưa chọn dịch vụ')}${
      b.preferred ? ` · mong muốn: ${esc(b.preferred)}` : ''
    }</div>
    ${b.note ? `<div class="muted" style="margin-top:4px">Ghi chú: ${esc(b.note)}</div>` : ''}
  </td>
  <td style="width:150px"><a href="tel:${esc(tel)}" style="font-weight:600">${esc(b.phone)}</a></td>
  <td style="width:120px"><span class="pill ${lop}">${nhan}</span></td>
  <td style="width:210px">
    <div class="bar">
      ${
        b.status === 'da_xac_nhan'
          ? ''
          : `<button class="btn ghost sm" data-mark="${b.id}" data-to="da_xac_nhan">Đã xác nhận</button>`
      }
      ${
        b.status === 'huy'
          ? ''
          : `<button class="btn danger sm" data-mark="${b.id}" data-to="huy">Huỷ</button>`
      }
    </div>
  </td>
</tr>`;
    })
    .join('');

  const soMoi = bookings.filter((b) => b.status === 'moi').length;

  return shell({
    active: 'bookings',
    wide: true,
    title: 'Đặt lịch',
    body: `
<h1>Đơn đặt lịch</h1>
<p class="lede">Khách gửi từ form ở cuối trang chủ. Mỗi đơn mới đều có email báo về hộp thư của tiệm.</p>
${flash ? `<div class="note ok">${esc(flash)}</div>` : ''}
${error ? `<div class="note err">${esc(error)}</div>` : ''}
${
  soMoi
    ? `<div class="note warn"><b>${soMoi}</b> đơn chưa xử lý. Gọi khách rồi bấm <b>Đã xác nhận</b> để khỏi lẫn.</div>`
    : ''
}

<div class="card" style="padding:6px 16px">
  ${
    rows
      ? `<table><thead><tr><th>Lúc nhận</th><th>Khách</th><th>Điện thoại</th><th>Trạng thái</th><th></th></tr></thead><tbody>${rows}</tbody></table>`
      : `<div class="empty"><p style="margin-bottom:8px">Chưa có đơn nào.</p>
         <p class="muted">Thử gửi một đơn ở <a href="/#booking" target="_blank">form đặt lịch</a> để kiểm tra.</p></div>`
  }
</div>

<div class="card">
  <h2>Chìa khoá cho phần mềm ở tiệm</h2>
  <p>Dán chuỗi này vào phần mềm trong tiệm để nó tự kéo đơn mới về. Giữ kín như mật khẩu —
  ai có chuỗi này là đọc được thông tin khách.</p>
  <p style="margin:10px 0"><code style="display:block;word-break:break-all;background:#F2F2F2;
     padding:10px 12px;border-radius:8px;font-size:13px">${esc(pollKey || '—')}</code></p>
  <p class="muted" style="margin-bottom:0">Đổi <b>SESSION_SECRET</b> trên Cloudflare là chuỗi này
  đổi theo, khoá cũ hết dùng được.</p>
</div>

<script>
document.querySelectorAll('[data-mark]').forEach(function(b){
  b.addEventListener('click', async function(){
    var to = b.dataset.to;
    if(to === 'huy' && !confirm('Huỷ đơn này?')) return;
    b.disabled = true; b.textContent = 'Đang lưu…';
    var r = await fetch('/admin/api/booking-status', {method:'POST',
      headers:{'Content-Type':'application/json'},
      body: JSON.stringify({ids:[Number(b.dataset.mark)], status:to})});
    if(r.ok) location.reload();
    else { alert('Không lưu được: ' + await r.text()); b.disabled=false; }
  });
});
</script>`,
  });
}

export function statusPage({ checks, repo }) {
  return shell({
    active: 'status',
    title: 'Hệ thống',
    body: `
<h1>Tình trạng hệ thống</h1>
<p class="lede">Nếu có dòng nào màu đỏ, đó là chỗ cần sửa trong Cloudflare.</p>

<div class="card">
  ${checks
    .map(
      (c) => `<div class="chk ${c.ok ? 'y' : 'n'}">
      <span class="ic">${c.ok ? '✓' : '!'}</span>
      <span><b>${esc(c.label)}</b>${c.detail ? `<br><span class="muted">${esc(c.detail)}</span>` : ''}</span>
    </div>`
    )
    .join('')}
</div>

<div class="card">
  <h2>Thông tin kết nối</h2>
  <p>Kho mã nguồn: <b>${esc(repo || '—')}</b></p>
  <div class="bar" style="margin-top:12px">
    <a class="btn ghost" href="https://github.com/${esc(repo || '')}" target="_blank">Mở GitHub</a>
    <a class="btn ghost" href="https://dash.cloudflare.com" target="_blank">Mở Cloudflare</a>
    <a class="btn ghost" href="/sitemap.xml" target="_blank">Xem sitemap</a>
  </div>
</div>

<div class="card">
  <h2>Cách hoạt động</h2>
  <p style="margin-bottom:0">Bạn bấm Lưu ở trang admin → file được gửi lên GitHub → Cloudflare
  thấy có file mới và tự dựng lại website → khoảng 1 phút sau thay đổi hiện trên vessca.com.
  Mọi phiên bản cũ đều giữ lại trên GitHub nên luôn quay lui được.</p>
</div>`,
  });
}

/** Trang thống kê truy cập website */
export function thongKePage(tk) {
  const so = (n) => Number(n || 0).toLocaleString('vi-VN');
  const QG = { VN: 'Việt Nam', KR: 'Hàn Quốc', CN: 'Trung Quốc', TW: 'Đài Loan', HK: 'Hồng Kông', US: 'Mỹ', JP: 'Nhật Bản', SG: 'Singapore', AU: 'Úc', TH: 'Thái Lan', MY: 'Malaysia', FR: 'Pháp', DE: 'Đức', GB: 'Anh', CA: 'Canada' };
  const NN = { vi: 'Tiếng Việt', en: 'Tiếng Anh', ko: 'Tiếng Hàn', zh: 'Tiếng Trung', 'zh-Hans': 'Tiếng Trung' };
  const tenTrang = (p) => {
    if (p === '/' ) return 'Trang chủ';
    const m = /^\/(?:(en|ko|zh)\/)?blog\/?(.*?)\/?$/.exec(p);
    if (m) return (m[2] ? m[2] : 'Danh sách blog') + (m[1] ? ` (${m[1].toUpperCase()})` : '');
    if (/^\/(en|ko|zh)\/?$/.test(p)) return `Trang chủ (${p.replace(/\//g, '').toUpperCase()})`;
    return p;
  };
  const bang = (tieuDe, rows, nhan = (k) => k, cotKhach = true, rong = '') => {
    const max = Math.max(1, ...rows.map((r) => r.n));
    return `<div class="card tk-c${rong}"><h2>${tieuDe}</h2>${
      rows.length
        ? `<table class="tk-t">${rows
            .map((r) => `<tr><td class="tk-k">${esc(nhan(r.k))}<span class="tk-b" style="width:${Math.round((r.n / max) * 100)}%"></span></td><td class="tk-n">${so(r.n)}</td>${cotKhach ? `<td class="tk-n muted">${so(r.kh)} người</td>` : ''}</tr>`)
            .join('')}</table>`
        : '<p class="muted">Chưa có dữ liệu.</p>'
    }</div>`;
  };
  const t = tk.tong || {};
  const nut = Object.fromEntries((tk.nut || []).map((r) => [r.k, r.n]));
  const daCo = Object.fromEntries((tk.theoNgay || []).map((d) => [d.ngay, d]));
  const ngay = [];
  if (tk.tu) {
    for (let d = new Date(tk.tu + 'T12:00:00Z'); ngay.length < tk.soNgay; d = new Date(d.getTime() + 86400000)) {
      const k = d.toISOString().slice(0, 10);
      ngay.push(daCo[k] || { ngay: k, xem: 0, khach: 0 });
    }
  }
  const nhanNgay = (i) => tk.soNgay <= 31 || i % Math.ceil(tk.soNgay / 15) === 0;
  const maxN = Math.max(1, ...ngay.map((d) => d.xem));
  const cot = ngay
    .map((d, i) => `<div class="tk-col${tk.soNgay > 31 ? ' sm' : ''}" title="${esc(d.ngay.split('-').reverse().join('/'))}: ${d.xem} lượt xem, ${d.khach} người"><span style="height:${Math.round((d.xem / maxN) * 100)}%"></span><em>${nhanNgay(i) ? `${esc(d.ngay.slice(8))}/${esc(d.ngay.slice(5, 7))}` : ''}</em></div>`)
    .join('');
  const gioMap = Object.fromEntries((tk.theoGio || []).map((r) => [r.k, r.n]));
  const maxG = Math.max(1, ...Object.values(gioMap));
  const gio = Array.from({ length: 24 }, (_, h) => `<div class="tk-col sm" title="${h}h: ${gioMap[h] || 0} lượt"><span style="height:${Math.round(((gioMap[h] || 0) / maxG) * 100)}%"></span><em>${h % 3 === 0 ? h + 'h' : ''}</em></div>`).join('');
  const chon = [1, 7, 30, 90, 365].map((n) => `<a class="btn ${n === tk.soNgay ? '' : 'ghost'} sm" href="/admin/thong-ke?ngay=${n}">${n === 1 ? 'Hôm nay' : n === 365 ? '1 năm' : n + ' ngày'}</a>`).join('');
  const gioFmt = new Intl.DateTimeFormat('vi-VN', { timeZone: 'Asia/Ho_Chi_Minh', day: '2-digit', month: '2-digit', hour: '2-digit', minute: '2-digit', hour12: false });
  const tg = (ts) => {
    try {
      const p = Object.fromEntries(gioFmt.formatToParts(new Date(ts)).map((x) => [x.type, x.value]));
      return `${p.day}/${p.month} ${p.hour}:${p.minute}`;
    } catch { return ''; }
  };
  const khachHtml = (tk.khachGan || []).length ? `<div class="card" style="margin-top:14px"><h2>Hành trình khách gần đây</h2>
<p class="muted" style="margin-bottom:10px">Mỗi dòng là một trình duyệt (mã ẩn danh). Bấm vào để xem khách đã xem trang nào, bấm nút gì, theo thứ tự thời gian.</p>
${tk.khachGan.map((k) => {
  const tong = k.soLan + (k.ngayTruoc || 0);
  const nhanDon = k.don && k.don.length ? `<span class="pill pub">Đã đặt lịch: ${esc(k.don.map((d) => d.name).join(', '))}</span>` : '';
  let phienTruoc = '';
  const buoc = k.buoc.map((b) => {
    const moiPhien = b.phien !== phienTruoc; phienTruoc = b.phien;
    const noi = b.loai === 'bam' ? `<b>Bấm: ${esc(b.nhan)}</b> <span class="muted">(${esc(tenTrang(b.trang))})</span>` : `Xem ${esc(tenTrang(b.trang))}${moiPhien && b.nguon && b.nguon !== 'Trong web' ? ` <span class="muted">· ${b.nguon === 'Vào thẳng' ? 'vào thẳng' : 'đến từ ' + esc(b.nguon)}</span>` : ''}`;
    return `${moiPhien ? '<li class="tk-ph">Lượt vào mới</li>' : ''}<li><span class="muted tk-tm">${esc(tg(b.ts))}</span> ${noi}</li>`;
  }).join('');
  return `<details class="tk-kh"><summary><b>Khách #${esc(k.vid.slice(0, 6))}</b> · ${esc(k.thietBi || '')} · ${esc(k.nguon || '')} · ${esc(k.thanhPho || k.quocGia || '')} · ${tong > 1 ? `vào ${tong} lần` : 'lần đầu'} · <span class="muted">${esc(tg(k.cuoi))}</span> ${nhanDon}</summary><ul class="tk-hj">${buoc}</ul></details>`;
}).join('')}</div>` : '';
  const o = (nhan, gt, phu = '') => `<div class="card tk-o"><div class="muted">${nhan}</div><div class="tk-big">${gt}</div>${phu ? `<div class="muted">${phu}</div>` : ''}</div>`;
  return shell({
    active: 'thongke',
    title: 'Thống kê',
    wide: true,
    body: `
<style>
.tk-g .card,.tk-g2 .card{margin:0!important}.tk-o{padding:16px 18px}.tk-big{font-size:30px;font-weight:700;line-height:1.2;margin:4px 0}
.tk-g{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin:14px 0 18px}
.tk-g2{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(320px,100%),1fr));gap:14px}
.tk-c{margin:0}.tk-t{width:100%;border-collapse:collapse}.tk-t td{padding:6px 4px;border-bottom:1px solid var(--line);font-size:14px;vertical-align:middle}
.tk-k{position:relative;word-break:break-word}.tk-b{display:block;height:4px;background:#111;border-radius:2px;margin-top:4px;opacity:.75}
.tk-n{text-align:right;white-space:nowrap;width:1%;padding-left:12px!important}
.tk-chart{display:flex;align-items:flex-end;gap:3px;height:170px;padding-top:10px;overflow-x:auto}
.tk-col{flex:1;min-width:14px;height:100%;display:flex;flex-direction:column;justify-content:flex-end;align-items:center}
.tk-col span{display:block;width:100%;background:#111;border-radius:3px 3px 0 0;min-height:1px}
.tk-col em{font-style:normal;font-size:10px;color:var(--soft);margin-top:4px;white-space:nowrap;height:14px}
.tk-col.sm{min-width:4px}
.tk-kh{border-top:1px solid var(--line);padding:9px 2px}.tk-kh summary{cursor:pointer;font-size:14px;line-height:1.6}
.tk-hj{margin:8px 0 4px 4px;font-size:13.5px;list-style:none}.tk-hj li{margin:2px 0}.tk-hj .tk-ph{list-style:none;margin:8px 0 2px 0;font-size:12px;color:var(--soft);text-transform:uppercase;letter-spacing:.05em}
.tk-tm{display:inline-block;min-width:92px}.tk-chart.full{justify-content:space-between}
</style>
<h1>Thống kê truy cập</h1>
<p class="lede">Từ ${esc(tk.tu.split('-').reverse().join('/'))} đến nay. Không tính lượt của trang quản trị và máy dò tìm (bot). Mỗi "người" là một thiết bị khác nhau trong một ngày.</p>
<div class="bar">${chon}</div>
<div class="tk-g">
  ${o('Lượt xem trang', so(t.xem))}
  ${o('Người truy cập', so(t.khach), 'tính theo thiết bị mỗi ngày')}
  ${o('Khách mới', so(tk.khachMoi), 'lần đầu vào web')}
  ${o('Khách quay lại', so(tk.khachQuayLai), 'vào từ 2 lần trở lên')}
  ${o('Bấm gọi điện', so(nut['Gọi điện']))}
  ${o('Bấm chỉ đường', so(nut['Chỉ đường']))}
  ${o('Đơn đặt lịch gửi', tk.donDatLich == null ? '—' : so(tk.donDatLich))}
</div>
<div class="card" style="margin-bottom:14px"><h2>Lượt xem theo ngày</h2>${ngay.length ? `<div class="tk-chart">${cot}</div>` : '<p class="muted">Chưa có dữ liệu.</p>'}</div>
<div class="tk-g2">
  ${bang('Thiết bị', tk.thietBi)}
  ${bang('Khách đến từ đâu', tk.nguon)}
  ${bang('Nút được bấm', tk.nut, (k) => k, true)}
  ${bang('Trang được xem nhiều', tk.trang, tenTrang)}
  ${bang('Quốc gia', tk.quocGia, (k) => QG[k] || k)}
  ${bang('Thành phố', tk.thanhPho)}
  ${bang('Ngôn ngữ đang xem', tk.ngonNgu, (k) => NN[k] || k)}
  ${bang('Trình duyệt / ứng dụng', tk.trinhDuyet)}
</div>
<div class="card" style="margin-top:14px"><h2>Giờ khách vào web (giờ Việt Nam)</h2><div class="tk-chart">${gio}</div></div>
${khachHtml}
<p class="muted" style="margin-top:14px">Từ khoá khách gõ trên Google không có ở đây — xem trong Google Search Console. Dữ liệu được giữ 400 ngày.</p>`,
  });
}
