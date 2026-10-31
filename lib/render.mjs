/**
 * ============================================================
 *  GIAO DIỆN BLOG VESSCA — BA NGÔN NGỮ
 * ============================================================
 *  Tiếng Việt ở /blog/, tiếng Anh ở /en/blog/, tiếng Trung ở /zh/blog/.
 *  Toàn bộ phần SEO (thẻ Google, hreflang, chia sẻ Facebook, dữ liệu
 *  có cấu trúc) được sinh tự động ở đây.
 */

import { site, languages, langOrder, blogPath, categoryLabel } from '../site.config.mjs';

const FAQ_TITLE = { vi: 'Câu hỏi thường gặp', en: 'Frequently asked questions', ko: '자주 묻는 질문', zh: '常见问题' };
import { esc, formatDate, readingTime, truncate } from './utils.mjs';

export const LOGO_SVG = `<svg viewBox="0 0 643 698" aria-hidden="true" class="logo-mark"><g transform="translate(0,698) scale(0.1,-0.1)"><path d="M3195 6489 c-368 -32 -752 -142 -1093 -313 -306 -153 -554 -337 -807 -597 -477 -490 -765 -1114 -835 -1808 -13 -132 -13 -414 0 -556 65 -687 357 -1322 835 -1814 375 -386 790 -638 1305 -794 1045 -317 2202 -24 2980 753 187 187 399 459 400 512 0 27 -29 46 -50 33 -5 -3 -41 -50 -80 -105 -749 -1057 -2095 -1498 -3324 -1088 -313 104 -641 283 -906 494 -230 183 -507 499 -665 759 -383 629 -514 1381 -369 2110 148 744 598 1417 1234 1844 690 464 1530 613 2337 415 658 -161 1239 -546 1644 -1089 141 -189 132 -179 157 -171 38 12 27 53 -39 146 -108 150 -211 272 -339 400 -503 503 -1163 808 -1885 870 -139 11 -357 11 -500 -1z M1020 4695 l0 -125 75 0 75 0 902 -1805 903 -1805 902 1805 903 1805 80 0 80 0 0 125 0 125 -340 0 -340 0 0 -124 c0 -114 2 -125 19 -128 16 -3 -81 -203 -643 -1326 l-661 -1322 -663 1325 c-621 1243 -660 1325 -637 1325 l25 0 0 125 0 125 -340 0 -340 0 0 -125z" fill="currentColor" stroke="none"/></g></svg>`;

const STYLES = `
:root{
  --stone:#FFFFFF; --panel:#F5F5F5; --ink:#111111; --ink-soft:#6E6E6E;
  --line:rgba(17,17,17,0.10); --accent:#2A2A2A;
  --serif:'Noto Serif KR',Georgia,serif;
  --sans:'Inter',-apple-system,BlinkMacSystemFont,sans-serif;
}
*{margin:0;padding:0;box-sizing:border-box;}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%;}
body{background:var(--stone);color:var(--ink);font-family:var(--sans);
  font-weight:300;line-height:1.65;-webkit-font-smoothing:antialiased;}
img{display:block;max-width:100%;}
a{color:inherit;text-decoration:none;}
h1,h2,h3,h4{font-family:var(--serif);font-weight:400;letter-spacing:.01em;line-height:1.25;}
.wrap{max-width:1180px;margin:0 auto;padding:0 40px;}
.wrap-narrow{max-width:760px;margin:0 auto;padding:0 40px;}

/* ---------- HEADER ---------- */
.bh{position:sticky;top:0;z-index:50;background:rgba(255,255,255,.92);
  backdrop-filter:blur(14px);border-bottom:1px solid var(--line);}
.bh-row{display:flex;align-items:center;justify-content:space-between;
  gap:20px;padding:16px 40px;max-width:1180px;margin:0 auto;}
.bh-logo{display:flex;align-items:center;gap:13px;}
.logo-mark{width:32px;height:32px;flex:none;}
.bh-logo .n{font-family:var(--sans);font-weight:700;font-size:21px;letter-spacing:.2em;
  text-transform:uppercase;display:block;line-height:1.1;}
.bh-logo .t{font-size:10px;letter-spacing:.18em;color:var(--ink-soft);
  text-transform:uppercase;margin-top:4px;display:block;}
.bh-nav{display:flex;gap:22px;align-items:center;font-size:13.5px;letter-spacing:.02em;}
.bh-nav a{color:var(--ink-soft);transition:color .25s;}
.bh-nav a:hover,.bh-nav a[aria-current]{color:var(--ink);}
.bh-cta{border:1px solid var(--ink);padding:9px 20px;font-size:12.5px;
  letter-spacing:.08em;text-transform:uppercase;transition:.25s;}
.bh-cta:hover{background:var(--ink);color:#fff;}

/* ---------- ĐỔI NGÔN NGỮ ---------- */
.lang{display:flex;gap:2px;align-items:center;}
.lang a{border:1px solid var(--line);padding:4px 9px;font-size:10.5px;
  letter-spacing:.04em;color:var(--ink-soft);transition:.2s;line-height:1.5;}
.lang a:hover{border-color:var(--ink);color:var(--ink);}
.lang a[aria-current]{background:var(--ink);color:#fff;border-color:var(--ink);}

/* ---------- HERO BLOG ---------- */
.b-hero{padding:76px 0 52px;border-bottom:1px solid var(--line);}
.b-hero .eyebrow{font-size:12px;letter-spacing:.2em;text-transform:uppercase;
  color:var(--ink-soft);display:block;margin-bottom:18px;}
.b-hero h1{font-size:clamp(32px,4.6vw,52px);max-width:16ch;margin-bottom:20px;}
.b-hero p{color:var(--ink-soft);font-size:16px;max-width:60ch;}

/* ---------- LỌC DANH MỤC ---------- */
.b-cats{display:flex;gap:10px;flex-wrap:wrap;padding:28px 0;border-bottom:1px solid var(--line);}
.b-cats button{font-family:inherit;font-size:13px;letter-spacing:.02em;
  padding:8px 18px;border:1px solid var(--line);background:none;color:var(--ink-soft);
  cursor:pointer;transition:.22s;border-radius:999px;}
.b-cats button:hover{border-color:var(--ink);color:var(--ink);}
.b-cats button.on{background:var(--ink);color:#fff;border-color:var(--ink);}

/* ---------- LƯỚI BÀI VIẾT ---------- */
.b-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:46px 34px;padding:56px 0 80px;}
.b-card{display:flex;flex-direction:column;}
.b-card-img{aspect-ratio:4/3;overflow:hidden;background:var(--panel);margin-bottom:20px;}
.b-card-img img{width:100%;height:100%;object-fit:cover;
  transition:transform .7s cubic-bezier(.2,.7,.3,1);}
.b-card:hover .b-card-img img{transform:scale(1.045);}
.b-meta{font-size:11.5px;letter-spacing:.12em;text-transform:uppercase;
  color:var(--ink-soft);margin-bottom:11px;display:flex;gap:10px;flex-wrap:wrap;}
.b-meta .dot{opacity:.45;}
.b-card h2{font-size:20px;line-height:1.35;margin-bottom:10px;}
.b-card:hover h2{text-decoration:underline;text-underline-offset:4px;}
.b-card p{font-size:14.5px;color:var(--ink-soft);}
.b-empty{padding:90px 0;text-align:center;color:var(--ink-soft);}

/* ---------- BÀI VIẾT ---------- */
.p-head{padding:64px 0 40px;text-align:center;}
.p-head .cat{font-size:11.5px;letter-spacing:.16em;text-transform:uppercase;
  color:var(--ink-soft);display:block;margin-bottom:20px;}
.p-head h1{font-size:clamp(30px,4.4vw,46px);max-width:20ch;margin:0 auto 22px;}
.p-head .sub{color:var(--ink-soft);font-size:16.5px;max-width:58ch;margin:0 auto 26px;}
.p-head .meta{font-size:12.5px;letter-spacing:.08em;color:var(--ink-soft);
  display:flex;gap:12px;justify-content:center;flex-wrap:wrap;}
.p-cover{max-width:1000px;margin:0 auto 56px;padding:0 40px;}
.p-cover img{width:100%;aspect-ratio:16/9;object-fit:cover;}
.p-credit{font-size:12px;color:var(--ink-soft);text-align:right;margin:6px 0 0;}
.p-credit a{color:inherit;}

.p-body{font-size:17px;line-height:1.85;color:#232323;}
.p-body > *+*{margin-top:1.35em;}
.p-body h2{font-size:27px;margin-top:2.2em;padding-top:.2em;}
.p-body h3{font-size:21px;margin-top:1.9em;}
.p-body h4{font-size:18px;margin-top:1.7em;}
.p-body ul,.p-body ol{padding-left:1.35em;}
.p-body li+li{margin-top:.5em;}
.p-body a{text-decoration:underline;text-underline-offset:3px;text-decoration-thickness:1px;}
.p-body a:hover{color:var(--ink-soft);}
.p-body img{width:100%;margin:2em 0;}
.p-body figure{margin:2em 0;}
.p-faq{margin-top:56px;padding-top:8px;border-top:1px solid var(--line);}
.p-faq h2{margin-top:1.2em;}
.p-faq h3{font-size:19px;}
.p-body figcaption{font-size:13px;color:var(--ink-soft);text-align:center;margin-top:10px;}
.p-body blockquote{border-left:2px solid var(--ink);padding:4px 0 4px 24px;
  font-family:var(--serif);font-size:20px;line-height:1.55;color:var(--accent);}
.p-body hr{border:none;border-top:1px solid var(--line);margin:2.6em 0;}
.p-body table{width:100%;border-collapse:collapse;font-size:15px;}
.p-body th,.p-body td{border:1px solid var(--line);padding:11px 14px;text-align:left;}
.p-body th{background:var(--panel);font-weight:500;}

/* ---------- CTA ĐẶT LỊCH ---------- */
.p-cta{background:var(--panel);padding:46px 40px;margin:68px 0 0;text-align:center;}
.p-cta h3{font-size:25px;margin-bottom:12px;}
.p-cta p{color:var(--ink-soft);font-size:15px;max-width:48ch;margin:0 auto 24px;}
.p-cta .btns{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;}
.p-cta a{border:1px solid var(--ink);padding:13px 30px;font-size:12.5px;
  letter-spacing:.09em;text-transform:uppercase;transition:.25s;}
.p-cta a.solid{background:var(--ink);color:#fff;}
.p-cta a:hover{background:var(--ink);color:#fff;}
.p-cta a.solid:hover{background:transparent;color:var(--ink);}
.p-nap{margin-top:26px;font-size:13.5px;line-height:1.7;color:var(--ink-soft);}
.p-cta .p-nap a.lk{border:none;padding:0;font-size:inherit;letter-spacing:0;text-transform:none;text-decoration:underline;color:var(--ink);background:none;}
.p-cta .p-nap a.lk:hover{background:none;color:var(--ink);}

/* ---------- TỪ KHOÁ ---------- */
.p-tags{padding:40px 0 0;display:flex;gap:9px;flex-wrap:wrap;}
.p-tags span{font-size:12px;color:var(--ink-soft);border:1px solid var(--line);
  padding:6px 14px;border-radius:999px;}

/* ---------- ĐỌC BẢN NGÔN NGỮ KHÁC ---------- */
.p-alt{margin-top:34px;padding:16px 20px;background:var(--panel);
  font-size:13.5px;color:var(--ink-soft);display:flex;gap:10px;
  flex-wrap:wrap;align-items:center;}
.p-alt a{text-decoration:underline;text-underline-offset:3px;color:var(--ink);}

/* ---------- BÀI LIÊN QUAN ---------- */
.p-rel{border-top:1px solid var(--line);margin-top:72px;padding:60px 0 80px;}
.p-rel h3{font-size:14px;letter-spacing:.16em;text-transform:uppercase;
  color:var(--ink-soft);margin-bottom:34px;font-family:var(--sans);font-weight:400;}
.p-rel-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:30px;}

/* ---------- FOOTER ---------- */
.bf{background:var(--ink);color:#DDD;padding:62px 0 34px;}
.bf-grid{display:grid;grid-template-columns:1.4fr 1fr 1fr;gap:44px;
  padding-bottom:40px;border-bottom:1px solid rgba(255,255,255,.14);}
.bf h4{font-size:11.5px;letter-spacing:.18em;text-transform:uppercase;
  color:#9A9A9A;margin-bottom:16px;font-family:var(--sans);font-weight:400;}
.bf p,.bf a{font-size:14px;color:#DDD;line-height:1.8;}
.bf a:hover{color:#fff;text-decoration:underline;}
.bf .bf-brand .n{font-family:var(--sans);font-weight:700;font-size:22px;
  letter-spacing:.2em;color:#fff;text-transform:uppercase;}
.bf .bf-brand .t{font-size:10px;letter-spacing:.18em;color:#9A9A9A;
  text-transform:uppercase;margin:5px 0 16px;}
.bf-bottom{padding-top:26px;display:flex;justify-content:space-between;
  gap:16px;flex-wrap:wrap;font-size:12.5px;color:#8A8A8A;}

/* ---------- MOBILE ---------- */
@media(max-width:900px){
  .b-grid,.p-rel-grid{grid-template-columns:1fr 1fr;gap:36px 26px;}
  .bf-grid{grid-template-columns:1fr 1fr;}
}
@media(max-width:640px){
  .wrap,.wrap-narrow,.bh-row,.p-cover{padding-left:22px;padding-right:22px;}
  .b-grid,.p-rel-grid,.bf-grid{grid-template-columns:1fr;gap:34px;}
  .bh-nav{gap:14px;font-size:13px;}
  .bh-nav .hide-sm{display:none;}
}
@media(max-width:480px){
  .bh-nav .bh-cta{display:none;}
  .bh-logo{gap:10px;}
  .logo-mark{width:26px;height:26px;}
  .bh-logo .n{font-size:17px;letter-spacing:.16em;}
  .bh-logo .t{font-size:8.5px;letter-spacing:.12em;}
  .lang a{padding:3px 7px;font-size:10px;}
  .b-hero{padding:48px 0 36px;}
  .p-body{font-size:16.5px;}
  .p-cta{padding:36px 22px;}
}
@media(max-width:350px){
  .wrap,.wrap-narrow,.bh-row,.p-cover{padding-left:16px;padding-right:16px;}
  .lang a{padding:3px 5px;}
  .bh-logo .t{display:none;}
}
`;

/** Lấy nội dung bài theo ngôn ngữ. Trả về null nếu bài chưa có bản đó. */
export function postView(post, lang) {
  if (lang === 'vi') return post;
  const t = post.i18n?.[lang];
  if (!t || !t.title || !t.content) return null;
  return {
    ...post,
    title: t.title,
    excerpt: t.excerpt ?? '',
    metaTitle: t.metaTitle ?? '',
    metaDescription: t.metaDescription ?? '',
    keywords: Array.isArray(t.keywords) ? t.keywords : [],
    content: t.content,
    coverAlt: t.coverAlt || post.coverAlt,
    faq: Array.isArray(t.faq) ? t.faq : [],
  };
}

/** Những ngôn ngữ mà bài này đã có bản dịch */
export const postLangs = (post) => langOrder.filter((l) => postView(post, l));

/** Khung HTML chung — nơi đặt toàn bộ thẻ SEO và hreflang */
export function layout({
  lang,
  title,
  description,
  keywords = [],
  canonical,
  ogImage,
  ogType = 'website',
  jsonLd = [],
  content,
  activeNav = '',
  alternates = [],
  langSwitch = [],
}) {
  const L = languages[lang];
  const img = ogImage
    ? (ogImage.startsWith('http') ? ogImage : site.url + ogImage)
    : site.url + site.defaultImage;

  const ld = jsonLd
    .map(
      (obj) =>
        `<script type="application/ld+json">${JSON.stringify(obj).replace(/</g, '\\u003c')}</script>`
    )
    .join('\n');

  // hreflang: nói cho Google biết bản nào dành cho người dùng ngôn ngữ nào
  const hreflangTags = alternates
    .map(
      (a) =>
        `<link rel="alternate" hreflang="${esc(languages[a.lang].hreflang)}" href="${esc(a.url)}">`
    )
    .join('\n');
  const xDefault = alternates.find((a) => a.lang === 'vi');

  const langNav = langSwitch.length
    ? `<div class="lang" role="group" aria-label="${esc(L.ui.otherLangs)}">
        ${langSwitch
          .map(
            (a) =>
              `<a href="${esc(a.url)}" hreflang="${esc(languages[a.lang].hreflang)}"${
                a.lang === lang ? ' aria-current="true"' : ''
              }>${esc(languages[a.lang].short)}</a>`
          )
          .join('')}
      </div>`
    : '';

  return `<!DOCTYPE html>
<html lang="${esc(L.htmlLang)}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>${esc(title)}</title>
<meta name="description" content="${esc(description)}">
${keywords.length ? `<meta name="keywords" content="${esc(keywords.join(', '))}">` : ''}
<link rel="canonical" href="${esc(canonical)}">
${hreflangTags}
${xDefault ? `<link rel="alternate" hreflang="x-default" href="${esc(xDefault.url)}">` : ''}
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<meta name="author" content="${esc(site.name)}">
<meta name="geo.region" content="VN-${esc(site.address.region)}">
<meta name="geo.placename" content="${esc(site.address.district)}, ${esc(site.address.city)}">
<meta name="geo.position" content="${site.address.latitude};${site.address.longitude}">
<meta name="ICBM" content="${site.address.latitude}, ${site.address.longitude}">

<meta property="og:type" content="${esc(ogType)}">
<meta property="og:site_name" content="${esc(site.name)}">
<meta property="og:title" content="${esc(title)}">
<meta property="og:description" content="${esc(description)}">
<meta property="og:url" content="${esc(canonical)}">
<meta property="og:image" content="${esc(img)}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="${esc(L.locale)}">
${alternates
  .filter((a) => a.lang !== lang)
  .map((a) => `<meta property="og:locale:alternate" content="${esc(languages[a.lang].locale)}">`)
  .join('\n')}
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="${esc(title)}">
<meta name="twitter:description" content="${esc(description)}">
<meta name="twitter:image" content="${esc(img)}">

<link rel="alternate" type="application/rss+xml" title="${esc(site.name)} Blog" href="${site.url}/rss.xml">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta name="theme-color" content="#111111">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@400;500;600&family=Inter:wght@300;400;500&display=swap" rel="stylesheet">
<style>${STYLES}</style>
${ld}
</head>
<body>

<header class="bh">
  <div class="bh-row">
    <a href="${esc(languages[lang].base)}/" class="bh-logo" aria-label="VESSCA">
      ${LOGO_SVG}
      <span>
        <span class="n">VESSCA</span>
        <span class="t">${esc(L.ui.tagline)}</span>
      </span>
    </a>
    <nav class="bh-nav">
      <a href="/#about" class="hide-sm">${esc(L.ui.navAbout)}</a>
      <a href="/#services" class="hide-sm">${esc(L.ui.navServices)}</a>
      <a href="${lang === 'vi' ? '' : '/' + lang}/bang-gia/" class="hide-sm">${esc(L.ui.navPrices)}</a>
      <a href="${esc(blogPath(lang))}/"${activeNav === 'blog' ? ' aria-current="page"' : ''}>${esc(L.ui.navBlog)}</a>
      ${langNav}
      <a href="/#booking" class="bh-cta">${esc(L.ui.navBook)}</a>
    </nav>
  </div>
</header>

${content}

<footer class="bf">
  <div class="wrap">
    <div class="bf-grid">
      <div class="bf-brand">
        <div class="n">VESSCA</div>
        <div class="t">${esc(L.ui.tagline)}</div>
        <p>${esc(site.address.street)}<br>${esc(site.address.ward)}, ${esc(site.address.district)}<br>${esc(site.address.city)}</p>
      </div>
      <div>
        <h4>${esc(L.ui.contact)}</h4>
        <p><a href="tel:${esc(site.phoneIntl)}">${esc(site.phone)}</a></p>
        <p><a href="${esc(site.social.instagram)}" target="_blank" rel="noopener">Instagram</a></p>
        <p><a href="${esc(site.social.facebook)}" target="_blank" rel="noopener">Facebook</a></p>
      </div>
      <div>
        <h4>${esc(L.ui.hours)}</h4>
        <p>${esc(L.ui.hoursText)}</p>
        <p style="margin-top:14px"><a href="${esc(blogPath(lang))}/">${L.ui.blogLink}</a></p>
      </div>
    </div>
    <div class="bf-bottom">
      <span>© ${new Date().getFullYear()} ${esc(site.legalName)}</span>
      <span>${esc(site.address.district)}, ${esc(site.address.city)}</span>
    </div>
  </div>
</footer>
<script src="/tk.js" defer></script>
</body>
</html>`;
}

/** Dữ liệu có cấu trúc mô tả tiệm nail — giúp Google hiện tiệm trên Maps */
export function localBusinessLd() {
  return {
    '@context': 'https://schema.org',
    '@type': 'NailSalon',
    '@id': `${site.url}/#business`,
    name: site.legalName,
    alternateName: site.name,
    description: site.description,
    url: site.url,
    telephone: site.phoneIntl,
    priceRange: site.priceRange,
    image: site.url + site.defaultImage,
    logo: site.url + '/assets/vessca-logo.png',
    address: {
      '@type': 'PostalAddress',
      streetAddress: site.address.street,
      // Phải khớp đúng dạng hồ sơ Google Maps đang ghi ("phường Gia Định,
      // Hồ Chí Minh"). Từ 2025 TP.HCM bỏ cấp quận, nên Bình Thạnh không còn
      // là đơn vị hành chính — để nó trong địa chỉ có cấu trúc làm Google
      // khó đối chiếu website với hồ sơ Maps. Chữ "Bình Thạnh" vẫn giữ
      // nguyên ở phần chữ khách đọc và trong từ khoá, vì người ta vẫn tìm vậy.
      addressLocality: `Phường ${site.address.ward}`,
      addressRegion: site.address.city,
      postalCode: site.address.postalCode,
      addressCountry: site.address.country,
    },
    geo: {
      '@type': 'GeoCoordinates',
      latitude: site.address.latitude,
      longitude: site.address.longitude,
    },
    openingHoursSpecification: {
      '@type': 'OpeningHoursSpecification',
      dayOfWeek: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
      opens: '09:00',
      closes: '20:30',
    },
    knowsLanguage: ['vi', 'en', 'zh'],
    sameAs: Object.values(site.social).filter(Boolean),
  };
}

function breadcrumbLd(trail) {
  return {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: trail.map((t, i) => ({
      '@type': 'ListItem',
      position: i + 1,
      name: t.name,
      item: site.url + t.path,
    })),
  };
}

function cardHtml(post, lang) {
  const v = postView(post, lang);
  const url = `${blogPath(lang)}/${v.slug}/`;
  const img = post.coverImage || site.defaultImage;
  return `<article class="b-card" data-cat="${esc(post.category || '')}">
  <a href="${esc(url)}" aria-label="${esc(v.title)}">
    <div class="b-card-img">
      <img src="${esc(img)}" alt="${esc(v.coverAlt || v.title)}" loading="lazy" width="600" height="450">
    </div>
    <div class="b-meta">
      ${post.category ? `<span>${esc(categoryLabel(post.category, lang))}</span><span class="dot">·</span>` : ''}
      <span>${esc(formatDate(post.publishedAt, lang))}</span>
    </div>
    <h2>${esc(v.title)}</h2>
    <p>${esc(truncate(v.excerpt || v.content, 128))}</p>
  </a>
</article>`;
}

/** Trang danh sách blog của một ngôn ngữ */
export function renderBlogIndex({ lang, posts, categories, alternates, langSwitch }) {
  const L = languages[lang];
  const shown = posts.filter((p) => postView(p, lang));
  const used = categories.filter((c) => shown.some((p) => p.category === c));

  const grid = shown.length
    ? `<div class="b-grid" id="grid">${shown.map((p) => cardHtml(p, lang)).join('\n')}</div>`
    : `<div class="b-empty"><p>${esc(L.ui.empty)}</p></div>`;

  const cats = used.length
    ? `<div class="b-cats">
        <button class="on" data-cat="">${esc(L.ui.all)}</button>
        ${used.map((c) => `<button data-cat="${esc(c)}">${esc(categoryLabel(c, lang))}</button>`).join('')}
      </div>`
    : '';

  const content = `
<main>
  <section class="b-hero">
    <div class="wrap">
      <span class="eyebrow">${esc(L.ui.eyebrow)}</span>
      <h1>${L.blogHeading}</h1>
      <p>${esc(L.blogDescription)}</p>
    </div>
  </section>
  <div class="wrap">
    ${cats}
    ${grid}
  </div>
</main>
${
  used.length
    ? `<script>
document.querySelectorAll('.b-cats button').forEach(function(btn){
  btn.addEventListener('click', function(){
    var cat = btn.dataset.cat;
    document.querySelectorAll('.b-cats button').forEach(function(b){ b.classList.remove('on'); });
    btn.classList.add('on');
    document.querySelectorAll('.b-card').forEach(function(card){
      card.style.display = (!cat || card.dataset.cat === cat) ? '' : 'none';
    });
  });
});
</script>`
    : ''
}`;

  return layout({
    lang,
    title: L.blogTitle,
    description: L.blogDescription,
    keywords: [],
    canonical: `${site.url}${blogPath(lang)}/`,
    ogType: 'website',
    activeNav: 'blog',
    alternates,
    langSwitch,
    jsonLd: [
      localBusinessLd(),
      breadcrumbLd([
        { name: L.ui.home, path: '/' },
        { name: L.ui.navBlog, path: `${blogPath(lang)}/` },
      ]),
      {
        '@context': 'https://schema.org',
        '@type': 'Blog',
        '@id': `${site.url}${blogPath(lang)}/#blog`,
        name: L.blogTitle,
        description: L.blogDescription,
        url: `${site.url}${blogPath(lang)}/`,
        inLanguage: L.hreflang,
        publisher: { '@id': `${site.url}/#business` },
        blogPost: shown.slice(0, 20).map((p) => ({
          '@type': 'BlogPosting',
          headline: postView(p, lang).title,
          url: `${site.url}${blogPath(lang)}/${p.slug}/`,
          datePublished: p.publishedAt,
        })),
      },
    ],
    content,
  });
}

/** Trang chi tiết một bài viết */
export function renderPost({ lang, post, related, alternates, langSwitch }) {
  const L = languages[lang];
  const v = postView(post, lang);
  const url = `${site.url}${blogPath(lang)}/${post.slug}/`;
  const desc = v.metaDescription || truncate(v.excerpt || v.content, 158);
  const mins = readingTime(v.content);
  const img = post.coverImage || site.defaultImage;

  // Mời đọc bản ngôn ngữ khác của chính bài này
  const others = alternates.filter((a) => a.lang !== lang);
  const altBox = others.length
    ? `<div class="p-alt"><span>${esc(L.ui.otherLangs)}:</span>${others
        .map(
          (a) =>
            `<a href="${esc(a.url)}" hreflang="${esc(languages[a.lang].hreflang)}">${esc(languages[a.lang].label)}</a>`
        )
        .join('')}</div>`
    : '';

  const content = `
<main>
  <article>
    <header class="p-head">
      <div class="wrap-narrow">
        ${post.category ? `<span class="cat">${esc(categoryLabel(post.category, lang))}</span>` : ''}
        <h1>${esc(v.title)}</h1>
        ${v.excerpt ? `<p class="sub">${esc(v.excerpt)}</p>` : ''}
        <div class="meta">
          <span>${esc(post.author || site.name)}</span>
          <span>·</span>
          <time datetime="${esc(post.publishedAt)}">${esc(formatDate(post.publishedAt, lang))}</time>
          <span>·</span>
          <span>${mins} ${esc(L.ui.readTime)}</span>
        </div>
      </div>
    </header>

    ${
      post.coverImage
        ? `<div class="p-cover"><img src="${esc(post.coverImage)}" alt="${esc(v.coverAlt || v.title)}" width="1000" height="563">${
            post.coverCredit && post.coverCredit.ten
              ? `<p class="p-credit">Ảnh: <a href="${esc(post.coverCredit.link || '#')}" target="_blank" rel="noopener nofollow">${esc(post.coverCredit.ten)} / ${esc(post.coverCredit.nguon || 'Pexels')}</a></p>`
              : ''
          }</div>`
        : ''
    }

    <div class="wrap-narrow">
      <div class="p-body">${v.content}</div>

      ${
        // FAQ phải hiện ra cho người đọc thì Google mới tính — trước đây chỉ nằm trong JSON-LD
        v.faq?.length
          ? `<section class="p-body p-faq" aria-labelledby="faq-h">
        <h2 id="faq-h">${esc(FAQ_TITLE[lang] || FAQ_TITLE.vi)}</h2>
        ${v.faq.map((f) => `<h3>${esc(f.q)}</h3>\n        <p>${esc(f.a)}</p>`).join('\n        ')}
      </section>`
          : ''
      }

      ${
        v.keywords?.length
          ? `<div class="p-tags">${v.keywords.map((k) => `<span>${esc(k)}</span>`).join('')}</div>`
          : ''
      }

      ${altBox}

      <aside class="p-cta">
        <h3>${esc(L.ui.ctaTitle)}</h3>
        <p>${esc(L.ui.ctaText)}</p>
        <div class="btns">
          <a href="/#booking" class="solid">${esc(L.ui.ctaBook)}</a>
          <a href="tel:${esc(site.phoneIntl)}">${esc(site.phone)}</a>
        </div>
        <div class="p-nap">
          <b>VESSCA Korean Nail Lounge</b> — ${esc(L.ui.napAddress)}<br>
          ${esc(L.ui.hoursText)} · <a class="lk" href="tel:${esc(site.phoneIntl)}">${esc(site.phone)}</a> ·
          <a class="lk" href="${esc(site.mapsUrl)}" target="_blank" rel="noopener">${esc(L.ui.napDirections)}</a>
        </div>
      </aside>
    </div>

    ${
      related.length
        ? `<div class="wrap">
      <section class="p-rel">
        <h3>${esc(L.ui.related)}</h3>
        <div class="p-rel-grid">${related.map((p) => cardHtml(p, lang)).join('\n')}</div>
      </section>
    </div>`
        : ''
    }
  </article>
</main>`;

  return layout({
    lang,
    title: v.metaTitle || `${v.title} — ${site.name}`,
    description: desc,
    keywords: v.keywords || [],
    canonical: url,
    ogImage: img,
    ogType: 'article',
    activeNav: 'blog',
    alternates,
    langSwitch,
    jsonLd: [
      {
        '@context': 'https://schema.org',
        '@type': 'BlogPosting',
        '@id': `${url}#article`,
        headline: v.title,
        description: desc,
        image: [img.startsWith('http') ? img : site.url + img],
        datePublished: post.publishedAt,
        dateModified: post.updatedAt || post.publishedAt,
        inLanguage: L.hreflang,
        wordCount: v.content.split(/\s+/).length,
        keywords: (v.keywords || []).join(', '),
        articleSection: categoryLabel(post.category || 'Blog', lang),
        author: { '@type': 'Organization', name: post.author || site.name, url: site.url },
        publisher: { '@id': `${site.url}/#business` },
        mainEntityOfPage: { '@type': 'WebPage', '@id': url },
      },
      localBusinessLd(),
      breadcrumbLd([
        { name: L.ui.home, path: '/' },
        { name: L.ui.navBlog, path: `${blogPath(lang)}/` },
        { name: v.title, path: `${blogPath(lang)}/${post.slug}/` },
      ]),
      ...(v.faq?.length
        ? [
            {
              '@context': 'https://schema.org',
              '@type': 'FAQPage',
              inLanguage: L.hreflang,
              mainEntity: v.faq.map((f) => ({
                '@type': 'Question',
                name: f.q,
                acceptedAnswer: { '@type': 'Answer', text: f.a },
              })),
            },
          ]
        : []),
    ],
    content,
  });
}

/** Trang báo "không tìm thấy" */
export function render404(lang = 'vi') {
  const L = languages[lang];
  return layout({
    lang,
    title: `${L.ui.notFound} — ${site.name}`,
    description: L.ui.notFoundText,
    canonical: `${site.url}/404`,
    content: `
<main>
  <section class="b-hero" style="border-bottom:none;padding:110px 0 90px;text-align:center">
    <div class="wrap">
      <span class="eyebrow" style="display:block">404</span>
      <h1 style="max-width:none;margin:0 auto 18px">${esc(L.ui.notFound)}</h1>
      <p style="margin:0 auto 32px">${esc(L.ui.notFoundText)}</p>
      <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap">
        <a href="${esc(languages[lang].base)}/" style="border:1px solid var(--ink);background:var(--ink);color:#fff;padding:13px 30px;font-size:12.5px;letter-spacing:.09em;text-transform:uppercase">${esc(L.ui.backHome)}</a>
        <a href="${esc(blogPath(lang))}/" style="border:1px solid var(--ink);padding:13px 30px;font-size:12.5px;letter-spacing:.09em;text-transform:uppercase">${esc(L.ui.seeBlog)}</a>
      </div>
    </div>
  </section>
</main>`,
  }).replace(
    '<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">',
    '<meta name="robots" content="noindex, follow">'
  );
}
