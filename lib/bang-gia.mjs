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

import { LOGO_SVG } from './render.mjs';

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
    const poster = /poster="([^"]+)"/.exec(doan);
    const still = /<img class="avp-still" src="([^"]+)"/.exec(doan);
    const anh = poster || still || /<img[^>]+src="([^"]+)"/.exec(doan);
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
    nhom.push({ cat: v.cat, key: t && t[1], vi: t && strip(t[2]), anh: anh && anh[1], vua: !!still && !poster, dong });
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
  const maps = site.mapsUrl || 'https://maps.app.goo.gl/ic8B2eEiF8PWipZg7';
  const alts = LANGS.map((l) => `<link rel="alternate" hreflang="${HREFLANG[l]}" href="${url(site, l)}">`).join('\n');
  const chips = nhom.map((n, i) => `<a href="#${n.cat}" data-cat="${n.cat}"${i ? '' : ' class="on"'}>${esc(T(n.key, n.vi))}</a>`).join('');
  const src = (a) => (a.startsWith('http') ? a : '/' + a.replace(/^\//, ''));
  const muc = nhom.map((n, i) => {
    const rows = n.dong.map((d) => {
      if (d.loai === 'nhom') return `<div class="grp">${esc(T(d.key, d.vi))}</div>`;
      if (d.loai === 'ghichu') return `<p class="note">${esc(T(d.key, d.vi))}</p>`;
      const desc = d.descKey ? `<small>${esc(T(d.descKey, d.descVi))}</small>` : '';
      return `<div class="row"><span class="nm">${esc(T(d.key, d.vi))}${desc}</span><span class="pr">${esc(dichGia(d.gia, lang))}</span></div>`;
    }).join('');
    const ten = esc(T(n.key, n.vi));
    return `<section class="cat" id="${n.cat}">
  <div class="media${n.vua ? ' contain' : ''}">${n.anh ? `<img src="${esc(src(n.anh))}" alt="${ten}" loading="${i ? 'lazy' : 'eager'}">` : ''}
    <div class="cap"><span>${String(i + 1).padStart(2, '0')}</span><h2>${ten}</h2></div></div>
  <div class="pane"><div class="eyebrow">${esc(T('svc.pricelabel', 'Bảng giá'))}</div>${rows}</div>
</section>`;
  }).join('\n');
  const langLinks = LANGS.map((l) => `<a href="${BASE[l]}/bang-gia/"${l === lang ? ' class="on" aria-current="true"' : ''} lang="${HREFLANG[l]}">${LABEL[l]}</a>`).join('');
  const ld = {
    '@context': 'https://schema.org', '@type': 'WebPage', name: U.metaTitle, url: url(site, lang), inLanguage: HREFLANG[lang],
    about: { '@id': 'https://vessca.com/#business' },
  };
  const ic = {
    cal: '<svg viewBox="0 0 24 24"><path d="M7 3v3M17 3v3M4 9h16M5 5h14a1 1 0 0 1 1 1v13a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1z"/></svg>',
    tel: '<svg viewBox="0 0 24 24"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a1 1 0 0 1-1 1A16 16 0 0 1 4 5a1 1 0 0 1 1-1z"/></svg>',
    map: '<svg viewBox="0 0 24 24"><path d="M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/></svg>',
    share: '<svg viewBox="0 0 24 24"><path d="M12 15V3M8 7l4-4 4 4M5 12v7a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-7"/></svg>',
  };
  return `<!DOCTYPE html>
<html lang="${HREFLANG[lang]}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
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
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@400;500&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<script type="application/ld+json">${JSON.stringify(ld).replace(/</g, '\\u003c')}</script>
<style>
:root{--ink:#111;--soft:#6E6E6E;--line:rgba(17,17,17,.1);--dark:#161616;--dline:rgba(255,255,255,.14);
  --gold:#C7C7C7;--serif:'Noto Serif KR',Georgia,serif;--sans:'Inter',-apple-system,sans-serif;}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:var(--sans);font-weight:300;color:var(--ink);background:#0D0D0D;line-height:1.55;-webkit-font-smoothing:antialiased}
a{color:inherit;text-decoration:none}
img{display:block;width:100%;height:100%;object-fit:cover}
/* ---- thanh trên ---- */
.top{position:sticky;top:0;z-index:30;background:#fff;box-shadow:0 1px 0 var(--line)}
.top-in{max-width:1180px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;gap:12px;padding:12px 18px}
.brand{display:flex;align-items:center;gap:10px}
.brand svg{width:26px;height:28px;color:var(--ink)}
.brand b{display:block;font-weight:600;font-size:16px;letter-spacing:.24em}
.brand small{display:block;font-size:8.5px;letter-spacing:.16em;color:var(--soft);margin-top:1px}
.langs{display:flex;gap:4px}.langs a{font-size:10.5px;border:1px solid var(--line);padding:4px 7px;color:var(--soft)}
.langs a.on{background:var(--ink);color:#fff;border-color:var(--ink)}
.chips{max-width:1180px;margin:0 auto;display:flex;gap:8px;overflow-x:auto;padding:2px 18px 12px;scrollbar-width:none;-webkit-overflow-scrolling:touch}
.chips::-webkit-scrollbar{display:none}
.chips a{flex:none;font-size:13px;border:1px solid var(--line);border-radius:999px;padding:8px 15px;white-space:nowrap;background:#fff;transition:background .2s,color .2s}
.chips a.on{background:var(--ink);color:#fff;border-color:var(--ink)}
/* ---- phần mở đầu ---- */
.hero{position:relative;background:#111;color:#fff;overflow:hidden}
.hero::before{content:"";position:absolute;inset:0;background:url(/images/hero-poster.jpg) center/cover;opacity:.32;filter:saturate(.7)}
.hero::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(17,17,17,.35),rgba(17,17,17,.92))}
.hero-in{position:relative;z-index:1;max-width:1180px;margin:0 auto;padding:44px 18px 30px}
.eyebrow{font-size:11.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--gold)}
.hero h1{font-family:var(--serif);font-weight:400;font-size:clamp(32px,7vw,52px);line-height:1.15;margin:10px 0 12px}
.hero p{color:#CFCFCF;font-size:14.5px;max-width:620px}
.ex{margin-top:16px;display:inline-block;font-size:13.5px;color:#EDEDED;border:1px solid var(--dline);background:rgba(255,255,255,.05);padding:11px 14px}
.ex b{font-weight:500;color:#fff}
.info{display:flex;flex-wrap:wrap;gap:4px 18px;margin-top:16px;font-size:12.5px;color:#A9A9A9}
.acts{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-top:20px;max-width:560px}
.acts a,.acts button{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:5px;min-height:62px;border:1px solid var(--dline);font:inherit;font-size:12px;font-weight:400;letter-spacing:.02em;background:transparent;color:#fff;cursor:pointer}
.acts svg{width:19px;height:19px;fill:none;stroke:currentColor;stroke-width:1.5;stroke-linecap:round;stroke-linejoin:round}
.acts .main{background:#fff;color:var(--ink);border-color:#fff}
/* ---- từng nhóm: ảnh + bảng giá tối, giống bảng giá trang chủ ---- */
.list{max-width:1180px;margin:0 auto;padding:0 0 10px}
.cat{display:flex;flex-direction:column;background:var(--dark);border-top:1px solid #000}
.media{position:relative;aspect-ratio:16/10;background:#000;overflow:hidden}
.media img{filter:saturate(.85) brightness(.82)}
.media.contain{background:#0D0D0D}.media.contain img{object-fit:contain;padding:14px;filter:none}
.media::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 45%,rgba(0,0,0,.78))}
.media.contain::after{background:linear-gradient(180deg,rgba(0,0,0,0) 70%,rgba(0,0,0,.7))}
.cap{position:absolute;left:20px;right:20px;bottom:16px;z-index:1;color:#fff}
.cap span{font-size:11.5px;letter-spacing:.12em;color:var(--gold)}
.cap h2{font-family:var(--serif);font-weight:400;font-size:24px;line-height:1.2;margin-top:2px}
.pane{color:#F0F0F0;padding:22px 20px 26px}
.pane .eyebrow{margin-bottom:6px}
.grp{font-size:11.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--gold);margin-top:22px;padding-top:16px;border-top:1px solid rgba(255,255,255,.18)}
.row{display:flex;justify-content:space-between;align-items:baseline;gap:14px;padding:13px 0;border-bottom:1px dotted rgba(255,255,255,.16)}
.row .nm{font-size:14.5px;min-width:0;overflow-wrap:anywhere}
.row .nm small{display:block;font-size:11.5px;color:#9A9A9A;margin-top:3px}
.row .pr{font-size:14px;color:#D8D8D8;white-space:nowrap}
.note{font-size:12px;line-height:1.6;color:#9A9A9A;margin-top:16px}
.foot{max-width:1180px;margin:0 auto;padding:28px 18px 120px;color:#8A8A8A;font-size:12.5px}
.foot p{margin-bottom:6px}.foot a{color:#CFCFCF;text-decoration:underline}
.bar{position:fixed;left:0;right:0;bottom:0;z-index:40;background:rgba(17,17,17,.94);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);
  border-top:1px solid var(--dline);padding:10px 16px calc(10px + env(safe-area-inset-bottom));display:flex;gap:8px;justify-content:center}
.bar a{flex:1;max-width:280px;display:flex;align-items:center;justify-content:center;min-height:46px;font-size:14px;font-weight:400;letter-spacing:.02em;border:1px solid var(--dline);color:#fff}
.bar a.main{background:#fff;color:var(--ink);border-color:#fff}
.toast{position:fixed;left:50%;bottom:86px;transform:translateX(-50%);background:#fff;color:var(--ink);font-size:13px;padding:8px 14px;border-radius:999px;opacity:0;transition:opacity .2s;pointer-events:none;z-index:50}
.toast.show{opacity:1}
/* máy tính bảng, máy tính: ảnh bên trái, bảng giá bên phải */
@media(min-width:700px){
  .hero-in{padding:64px 28px 40px}
  .chips{padding-left:28px;padding-right:28px}.top-in{padding-left:28px;padding-right:28px}
  .cat{flex-direction:row;align-items:stretch}
  .media{flex:1 1 0;aspect-ratio:auto;min-height:440px}
  .media img{position:absolute;inset:0}
  .pane{flex:1 1 0;padding:34px 30px 34px;border-left:1px solid var(--dline)}
  .cap{left:28px;bottom:24px}.cap h2{font-size:28px}
  .cat:nth-child(even){flex-direction:row-reverse}
  .cat:nth-child(even) .pane{border-left:none;border-right:1px solid var(--dline)}
}
@media(min-width:1024px){.media{flex:1.15 1 0}}
@media print{.top,.bar,.acts,.chips,.hero::before{display:none}.foot{padding-bottom:0}}
</style>
</head>
<body>
<header class="top">
  <div class="top-in">
    <a class="brand" href="/" aria-label="VESSCA">${LOGO_SVG}<span><b>VESSCA</b><small>KOREAN NAIL LOUNGE</small></span></a>
    <nav class="langs" aria-label="Language">${langLinks}</nav>
  </div>
  <nav class="chips" id="chips">${chips}</nav>
</header>
<div class="hero"><div class="hero-in">
  <div class="eyebrow">VESSCA · Korean Nail Lounge</div>
  <h1>${esc(U.title)}</h1>
  <p>${esc(U.intro)} ${esc(U.quote)}</p>
  <div class="ex">${U.example}</div>
  <div class="info"><span>${esc(U.address)}</span><span>${esc(U.hours)}</span><span>0933.528.501</span></div>
  <div class="acts">
    <a class="main" href="/#booking" data-tk="Bảng giá: Đặt lịch">${ic.cal}${esc(U.book)}</a>
    <a href="tel:${tel}">${ic.tel}${esc(U.call)}</a>
    <a href="${maps}" target="_blank" rel="noopener">${ic.map}${esc(U.map)}</a>
    <button type="button" id="shareBtn" data-tk="Bảng giá: Chia sẻ">${ic.share}${esc(U.share)}</button>
  </div>
</div></div>
<main class="list">
${muc}
</main>
<div class="foot">
  <p>${esc(U.warranty)}</p>
  <p>${esc(U.updated)}: ${esc(thang)} · <a href="/">${esc(U.home)}</a> · <a href="${BASE[lang]}/blog/">${esc(U.blog)}</a></p>
</div>
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
    chips.forEach(function(a,i){ var on=i===cur; if(on!==a.classList.contains('on')){ a.classList.toggle('on',on); if(on){ var bar=a.parentNode; bar.scrollTo({left:a.offsetLeft-(bar.clientWidth-a.offsetWidth)/2,behavior:'smooth'}); } } });
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
