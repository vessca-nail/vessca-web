/**
 * ============================================================
 *  TRANG BẢNG GIÁ RIÊNG — /bang-gia/ (+ /en/, /ko/, /zh/)
 * ============================================================
 *  Để gửi link cho khách hỏi giá. Lấy giá THẲNG từ phần "Dịch vụ & bảng giá"
 *  trên trang chủ (src/index.html) và chữ từ bảng I18N của trang chủ — nên
 *  chỉ cần sửa giá MỘT chỗ (trang chủ), trang này tự cập nhật khi build.
 *  Không có accordion, không co giãn: mọi nhóm hiện sẵn, có thanh chọn nhóm
 *  để nhảy tới — xem trên điện thoại không bị nhảy trang.
 */

const LANGS = ['vi', 'en', 'ko', 'zh'];
const BASE = { vi: '', en: '/en', ko: '/ko', zh: '/zh' };
const HREFLANG = { vi: 'vi', en: 'en', ko: 'ko', zh: 'zh-Hans' };
const LABEL = { vi: 'VI', en: 'EN', ko: '한국어', zh: '中文' };

const UI = {
  vi: {
    title: 'Bảng giá dịch vụ',
    metaTitle: 'Bảng giá nail VESSCA — tiệm nail Hàn Quốc Bình Thạnh (Gia Định)',
    metaDesc: 'Bảng giá đầy đủ tại VESSCA: chăm sóc móng từ 60.000₫, sơn gel từ 130.000₫, sơn Hàn cao cấp từ 220.000₫, úp móng, đắp gel, nail art. 251/30 Lê Quang Định, Gia Định, TP.HCM.',
    intro: 'Giá niêm yết cho từng dịch vụ. Một bộ nail thường gồm: chăm sóc móng + màu sơn, thêm nối móng hoặc design nếu bạn muốn.',
    example: 'Ví dụ: cắt da tay (60.000₫) + sơn thạch (150.000₫) = <b>210.000₫</b>.',
    quote: 'Kỹ thuật viên báo tổng chi phí trước khi làm.',
    hours: 'Mở cửa 9:00–20:30 mỗi ngày',
    address: '251/30 Lê Quang Định, phường Gia Định, TP.HCM',
    book: 'Đặt lịch', call: 'Gọi', map: 'Chỉ đường', share: 'Chia sẻ', copied: 'Đã chép link',
    home: 'Trang chủ', updated: 'Cập nhật', blog: 'Blog',
    warranty: 'Bảo hành 5 ngày · Dụng cụ tiệt trùng bằng máy sau mỗi khách',
    pre: { from: (p) => `từ ${p}`, each: 'viên', color: 'màu', set: 'bộ' },
  },
  en: {
    title: 'Price list',
    metaTitle: 'VESSCA Price List — Korean Nail Salon, Binh Thanh, Saigon',
    metaDesc: 'Full VESSCA price list: nail care from 60,000₫, gel from 130,000₫, premium Korean gel from 220,000₫, extensions, builder gel, nail art. 251/30 Le Quang Dinh, Gia Dinh ward, Ho Chi Minh City.',
    intro: 'Listed prices for each service. A typical set is nail care + colour, plus extensions or design if you like.',
    example: 'Example: hand cuticle care (60,000₫) + jelly gel (150,000₫) = <b>210,000₫</b>.',
    quote: 'Your technician confirms the total before starting.',
    hours: 'Open 9:00–20:30 daily',
    address: '251/30 Le Quang Dinh, Gia Dinh ward, Ho Chi Minh City',
    book: 'Book', call: 'Call', map: 'Directions', share: 'Share', copied: 'Link copied',
    home: 'Home', updated: 'Updated', blog: 'Blog',
    warranty: '5-day warranty · Tools machine-sterilised after every guest',
    pre: { from: (p) => `from ${p}`, each: 'piece', color: 'colour', set: 'set' },
  },
  ko: {
    title: '가격표',
    metaTitle: 'VESSCA 가격표 — 호치민 빈탄 한국식 네일샵',
    metaDesc: 'VESSCA 전체 가격표: 케어 60,000₫부터, 젤 130,000₫부터, 한국 프리미엄 젤 220,000₫부터, 연장, 젤 연장, 네일 아트. 251/30 Lê Quang Định, 자딘동, 호치민.',
    intro: '서비스별 정가입니다. 기본 세트는 케어 + 컬러이며, 원하시면 연장이나 아트를 더합니다.',
    example: '예: 손 큐티클 케어(60,000₫) + 시럽 젤(150,000₫) = <b>210,000₫</b>.',
    quote: '시작 전에 네일리스트가 총액을 안내합니다.',
    hours: '매일 9:00–20:30 영업',
    address: '251/30 Lê Quang Định, 자딘(Gia Định)동, 호치민시',
    book: '예약', call: '전화', map: '길찾기', share: '공유', copied: '링크 복사됨',
    home: '홈', updated: '업데이트', blog: '블로그',
    warranty: '5일 보증 · 매 손님 후 도구 기계 멸균',
    pre: { from: (p) => `${p}부터`, each: '개', color: '컬러', set: '세트' },
  },
  zh: {
    title: '价目表',
    metaTitle: 'VESSCA 价目表 — 胡志明平盛郡韩式美甲店',
    metaDesc: 'VESSCA 完整价目表:护理 60,000₫ 起,甲油胶 130,000₫ 起,韩国高端甲油胶 220,000₫ 起,延长甲、加固胶、美甲设计。251/30 Lê Quang Định,嘉定坊,胡志明市。',
    intro: '各项服务的标价。一套美甲通常是护理 + 颜色,可另加延长或设计。',
    example: '例如:手部甲缘护理(60,000₫)+ 果冻甲油胶(150,000₫)= <b>210,000₫</b>。',
    quote: '开始前美甲师会告知总价。',
    hours: '每天 9:00–20:30 营业',
    address: '251/30 Lê Quang Định,嘉定(Gia Định)坊,胡志明市',
    book: '预约', call: '致电', map: '导航', share: '分享', copied: '链接已复制',
    home: '首页', updated: '更新', blog: '博客',
    warranty: '5 天保修 · 每位客人后工具机器消毒',
    pre: { from: (p) => `${p} 起`, each: '颗', color: '色', set: '套' },
  },
};

const esc = (s = '') => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
const strip = (s = '') => String(s).replace(/<[^>]+>/g, '').replace(/&amp;/g, '&').trim();

/** Đọc bảng I18N (object literal) trong script của trang chủ */
function docI18N(html) {
  const i = html.indexOf('const I18N = ');
  if (i < 0) return {};
  let j = html.indexOf('{', i), sau = 0;
  for (let k = j; k < html.length; k++) {
    if (html[k] === '{') sau++;
    else if (html[k] === '}') { sau--; if (!sau) { j = [j, k + 1]; break; } }
  }
  try { return Function(`"use strict";return (${html.slice(j[0], j[1])});`)(); } catch { return {}; }
}

/** Đọc các nhóm dịch vụ + từng dòng giá từ accordion trên trang chủ */
function docBangGia(html) {
  const s = html.slice(html.indexOf('id="categoryAccordion"'), html.indexOf('<!-- ---------- COLLECTION'));
  const nhom = [];
  const reItem = /<div class="acc-item[^"]*" data-cat="(\w+)">/g;
  const vt = [];
  let m;
  while ((m = reItem.exec(s))) vt.push({ cat: m[1], at: m.index });
  vt.forEach((v, i) => {
    const doan = s.slice(v.at, i + 1 < vt.length ? vt[i + 1].at : s.length);
    const t = /data-i18n="(svc\.\w+\.title)">([^<]*)</.exec(doan);
    const anh = /<img[^>]+src="([^"]+)"/.exec(doan);
    const pane = doan.slice(doan.indexOf('acc-price-pane'));
    const dong = [];
    const re = /<div class="app-eyebrow app-group" data-i18n="([^"]+)">([^<]*)<\/div>|<div class="app-row"><div class="app-name" data-i18n="([^"]+)">([\s\S]*?)<\/div><div class="app-price">([^<]*)<\/div><\/div>|<p class="app-note" data-i18n="([^"]+)">([^<]*)<\/p>/g;
    let r;
    while ((r = re.exec(pane))) {
      if (r[1]) dong.push({ loai: 'nhom', key: r[1], vi: strip(r[2]) });
      else if (r[3]) {
        const d = /<span class="app-desc" data-i18n="([^"]+)">([^<]*)<\/span>/.exec(r[4]);
        dong.push({ loai: 'gia', key: r[3], vi: strip(r[4].replace(/<span[\s\S]*$/, '')),
          descKey: d && d[1], descVi: d && strip(d[2]), gia: strip(r[5]) });
      } else dong.push({ loai: 'ghichu', key: r[6], vi: strip(r[7]) });
    }
    nhom.push({ cat: v.cat, key: t && t[1], vi: t && strip(t[2]), anh: anh && anh[1], dong });
  });
  return nhom;
}

function dichGia(g, lang) {
  const P = UI[lang].pre;
  let s = g.trim();
  if (lang !== 'vi') {
    const unit = (u) => u.replace('viên', P.each).replace('màu', P.color).replace('bộ', P.set);
    let duoi = '';
    const md = /\s*\/\s*(viên|màu|bộ)\s*$/.exec(s);
    if (md) { duoi = ' / ' + unit(md[1]); s = s.slice(0, md.index); }
    if (/^từ\s+/.test(s)) s = P.from(s.replace(/^từ\s+/, ''));
    if (lang === 'en') s = s.replace(/(\d)\.(\d{3})/g, '$1,$2').replace(/(\d)\.(\d{3})/g, '$1,$2');
    if (lang === 'ko' || lang === 'zh') s = s.replace(/(\d)\.(\d{3})/g, '$1,$2').replace(/(\d)\.(\d{3})/g, '$1,$2');
    s += duoi;
  }
  return s;
}

const url = (site, lang) => `${site.url}${BASE[lang]}/bang-gia/`;

function trang(site, lang, nhom, I18N) {
  const U = UI[lang];
  const T = (key, vi) => strip((I18N[lang] && I18N[lang][key]) || vi || '');
  const thang = new Intl.DateTimeFormat('vi-VN', { month: '2-digit', year: 'numeric', timeZone: 'Asia/Ho_Chi_Minh' }).format(new Date());
  const tel = '+84933528501';
  const maps = 'https://maps.google.com/?q=251/30+Le+Quang+Dinh+Gia+Dinh+Ho+Chi+Minh';
  const alts = LANGS.map((l) => `<link rel="alternate" hreflang="${HREFLANG[l]}" href="${url(site, l)}">`).join('\n');
  const chips = nhom.map((n, i) => `<a href="#${n.cat}" data-cat="${n.cat}"${i ? '' : ' class="on"'}>${esc(T(n.key, n.vi))}</a>`).join('');
  const muc = nhom.map((n, i) => {
    const rows = n.dong.map((d) => {
      if (d.loai === 'nhom') return `<h3>${esc(T(d.key, d.vi))}</h3>`;
      if (d.loai === 'ghichu') return `<p class="note">${esc(T(d.key, d.vi))}</p>`;
      const desc = d.descKey ? `<small>${esc(T(d.descKey, d.descVi))}</small>` : '';
      return `<div class="row"><span class="nm">${esc(T(d.key, d.vi))}${desc}</span><span class="pr">${esc(dichGia(d.gia, lang))}</span></div>`;
    }).join('');
    return `<section class="cat" id="${n.cat}">
  <div class="cat-head">${n.anh ? `<img src="${esc(n.anh.startsWith('http') ? n.anh : '/' + n.anh.replace(/^\//, ''))}" alt="" loading="lazy">` : ''}<div><span class="num">${String(i + 1).padStart(2, '0')}</span><h2>${esc(T(n.key, n.vi))}</h2></div></div>
  ${rows}
</section>`;
  }).join('\n');
  const langLinks = LANGS.map((l) => `<a href="${BASE[l]}/bang-gia/"${l === lang ? ' class="on" aria-current="true"' : ''} lang="${HREFLANG[l]}">${LABEL[l]}</a>`).join('');
  const ld = {
    '@context': 'https://schema.org', '@type': 'WebPage', name: U.metaTitle, url: url(site, lang), inLanguage: HREFLANG[lang],
    about: { '@id': 'https://vessca.com/#business' },
  };
  return `<!DOCTYPE html>
<html lang="${HREFLANG[lang]}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${esc(U.metaTitle)}</title>
<meta name="description" content="${esc(U.metaDesc)}">
<link rel="canonical" href="${url(site, lang)}">
${alts}
<link rel="alternate" hreflang="x-default" href="${url(site, 'vi')}">
<meta property="og:type" content="website">
<meta property="og:title" content="${esc(U.metaTitle)}">
<meta property="og:description" content="${esc(U.metaDesc)}">
<meta property="og:url" content="${url(site, lang)}">
<meta property="og:image" content="${site.url}/assets/blog-default.jpg">
<meta property="og:site_name" content="VESSCA">
<meta name="theme-color" content="#111111">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@400;500&family=Inter:wght@300;400;500&display=swap" rel="stylesheet">
<script type="application/ld+json">${JSON.stringify(ld).replace(/</g, '\\u003c')}</script>
<style>
:root{--ink:#111;--soft:#6E6E6E;--line:rgba(17,17,17,.1);--panel:#F5F5F5;--serif:'Noto Serif KR',Georgia,serif;--sans:'Inter',-apple-system,sans-serif;}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-padding-top:120px}
body{font-family:var(--sans);font-weight:300;color:var(--ink);background:#fff;line-height:1.55;-webkit-font-smoothing:antialiased}
a{color:inherit;text-decoration:none}
.top{position:sticky;top:0;z-index:30;background:#fff;border-bottom:1px solid var(--line)}
.top-in{max-width:880px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;gap:12px;padding:12px 16px}
.brand{font-family:var(--serif);letter-spacing:.22em;font-size:17px;font-weight:500}
.brand small{display:block;font-family:var(--sans);font-size:9.5px;letter-spacing:.18em;color:var(--soft);font-weight:400}
.langs{display:flex;gap:4px}.langs a{font-size:11px;border:1px solid var(--line);padding:4px 7px;color:var(--soft)}
.langs a.on{background:var(--ink);color:#fff;border-color:var(--ink)}
.chips{max-width:880px;margin:0 auto;display:flex;gap:8px;overflow-x:auto;padding:0 16px 10px;scrollbar-width:none;-webkit-overflow-scrolling:touch}
.chips::-webkit-scrollbar{display:none}
.chips a{flex:none;font-size:13px;border:1px solid var(--line);border-radius:999px;padding:7px 13px;white-space:nowrap;background:#fff}
.chips a.on{background:var(--ink);color:#fff;border-color:var(--ink)}
.wrap{max-width:880px;margin:0 auto;padding:0 16px}
.hero{padding:30px 0 22px}
.hero h1{font-family:var(--serif);font-weight:400;font-size:clamp(28px,6vw,40px);line-height:1.2;margin-bottom:10px}
.hero p{color:var(--soft);font-size:14.5px;max-width:620px}
.hero .ex{margin-top:10px;color:var(--ink);font-size:14px;background:var(--panel);padding:12px 14px;border-radius:10px}
.info{display:flex;flex-wrap:wrap;gap:6px 16px;margin-top:14px;font-size:13px;color:var(--soft)}
.acts{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-top:18px}
.acts a,.acts button{display:flex;align-items:center;justify-content:center;gap:6px;min-height:44px;border:1px solid var(--ink);border-radius:10px;font:inherit;font-size:13.5px;font-weight:400;background:#fff;color:var(--ink);cursor:pointer}
.acts .main{background:var(--ink);color:#fff}
.cat{padding:26px 0 8px;border-top:1px solid var(--line)}
.cat-head{display:flex;align-items:center;gap:14px;margin-bottom:12px}
.cat-head img{width:64px;height:64px;object-fit:cover;border-radius:12px;flex:none;background:var(--panel)}
.cat-head .num{font-size:11px;color:var(--soft);letter-spacing:.08em}
.cat-head h2{font-family:var(--serif);font-weight:400;font-size:22px;line-height:1.25}
.cat h3{font-size:11.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--soft);font-weight:500;margin:18px 0 4px}
.row{display:flex;justify-content:space-between;align-items:baseline;gap:14px;padding:12px 0;border-bottom:1px dotted rgba(17,17,17,.18)}
.row .nm{font-size:15px;min-width:0;overflow-wrap:anywhere}
.row .nm small{display:block;font-size:12px;color:var(--soft);margin-top:2px}
.row .pr{font-size:14.5px;white-space:nowrap;font-weight:400}
.note{font-size:12.5px;color:var(--soft);margin-top:12px}
.foot{margin:34px 0 0;padding:26px 0 110px;border-top:1px solid var(--line);color:var(--soft);font-size:13px}
.foot p{margin-bottom:6px}.foot a{text-decoration:underline}
.bar{position:fixed;left:0;right:0;bottom:0;z-index:40;background:rgba(255,255,255,.96);border-top:1px solid var(--line);padding:10px 16px calc(10px + env(safe-area-inset-bottom));display:flex;gap:8px;justify-content:center}
.bar a{flex:1;max-width:260px;display:flex;align-items:center;justify-content:center;min-height:46px;border-radius:10px;font-size:14.5px;font-weight:400;border:1px solid var(--ink)}
.bar a.main{background:var(--ink);color:#fff}
.toast{position:fixed;left:50%;bottom:86px;transform:translateX(-50%);background:var(--ink);color:#fff;font-size:13px;padding:8px 14px;border-radius:999px;opacity:0;transition:opacity .2s;pointer-events:none}
.toast.show{opacity:1}
@media(min-width:720px){.cat-head img{width:84px;height:84px}.acts{max-width:560px}}
@media print{.top,.bar,.acts,.chips{display:none}.foot{padding-bottom:0}}
</style>
</head>
<body>
<header class="top">
  <div class="top-in">
    <a class="brand" href="/">VESSCA<small>KOREAN NAIL LOUNGE</small></a>
    <nav class="langs" aria-label="Language">${langLinks}</nav>
  </div>
  <nav class="chips" id="chips">${chips}</nav>
</header>
<main class="wrap">
  <div class="hero">
    <h1>${esc(U.title)}</h1>
    <p>${esc(U.intro)} ${esc(U.quote)}</p>
    <p class="ex">${U.example}</p>
    <div class="info"><span>${esc(U.address)}</span><span>${esc(U.hours)}</span><span>0933.528.501</span></div>
    <div class="acts">
      <a class="main" href="/#booking" data-tk="Bảng giá: Đặt lịch">${esc(U.book)}</a>
      <a href="tel:${tel}">${esc(U.call)}</a>
      <a href="${maps}" target="_blank" rel="noopener">${esc(U.map)}</a>
      <button type="button" id="shareBtn" data-tk="Bảng giá: Chia sẻ">${esc(U.share)}</button>
    </div>
  </div>
${muc}
  <div class="foot">
    <p>${esc(U.warranty)}</p>
    <p>${esc(U.updated)}: ${esc(thang)} · <a href="/">${esc(U.home)}</a> · <a href="${BASE[lang]}/blog/">${esc(U.blog)}</a></p>
  </div>
</main>
<div class="bar"><a href="tel:${tel}">${esc(U.call)} 0933.528.501</a><a class="main" href="/#booking" data-tk="Bảng giá: Đặt lịch">${esc(U.book)}</a></div>
<div class="toast" id="toast">${esc(U.copied)}</div>
<script>
(function(){
  try{ localStorage.setItem('vessca-lang','${lang}'); }catch(e){}
  var b=document.getElementById('shareBtn'), t=document.getElementById('toast');
  b.addEventListener('click',function(){
    var u=location.href.split('#')[0];
    if(navigator.share){ navigator.share({title:document.title,url:u}).catch(function(){}); return; }
    (navigator.clipboard?navigator.clipboard.writeText(u):Promise.reject()).then(function(){
      t.classList.add('show'); setTimeout(function(){t.classList.remove('show');},1600);
    }).catch(function(){ prompt('Link:',u); });
  });
  // Đánh dấu nhóm đang xem trên thanh chọn
  var chips=[].slice.call(document.querySelectorAll('#chips a'));
  var secs=chips.map(function(a){return document.getElementById(a.dataset.cat);});
  var hdr=document.querySelector('.top');
  chips.forEach(function(a){
    a.addEventListener('click',function(e){
      var s=document.getElementById(a.dataset.cat); if(!s) return;
      e.preventDefault();
      window.scrollTo({top:s.getBoundingClientRect().top+window.scrollY-hdr.offsetHeight+1,behavior:'instant'});
      history.replaceState(null,'','#'+a.dataset.cat);
    });
  });
  function mark(){
    var y=window.scrollY+hdr.offsetHeight+12, cur=0;
    secs.forEach(function(s,i){ if(s && s.offsetTop<=y) cur=i; });
    chips.forEach(function(a,i){ var on=i===cur; if(on!==a.classList.contains('on')){ a.classList.toggle('on',on); if(on){ var bar=a.parentNode; bar.scrollLeft=a.offsetLeft-(bar.clientWidth-a.offsetWidth)/2; } } });
  }
  window.addEventListener('scroll',mark,{passive:true}); mark();
})();
</script>
<script src="/tk.js" defer></script>
</body>
</html>`;
}

/** Trả về danh sách trang cần ghi: [{dir, html, loc}] */
export function trangBangGia(site, homepageHtml) {
  const I18N = docI18N(homepageHtml);
  const nhom = docBangGia(homepageHtml);
  if (!nhom.length) return [];
  return LANGS.map((l) => ({
    dir: (BASE[l] + '/bang-gia').replace(/^\//, ''),
    html: trang(site, l, nhom, I18N),
    loc: url(site, l),
    lang: l,
  }));
}

export const BANG_GIA_HREFLANG = HREFLANG;
