/**
 * ============================================================
 *  BUILD — biến bài viết thành trang web tĩnh, ba ngôn ngữ
 * ============================================================
 *  Cloudflare chạy file này mỗi lần bạn đăng bài mới.
 *
 *  Tiếng Việt  →  /blog/
 *  Tiếng Anh   →  /en/blog/
 *  Tiếng Trung →  /zh/blog/
 *
 *  Bài nào chưa có bản dịch thì ngôn ngữ đó bỏ qua bài ấy —
 *  không bao giờ sinh ra trang rỗng hay trang dịch dở.
 *
 *  Bạn KHÔNG cần chạy file này bằng tay.
 */

import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { site, categories, languages, langOrder, blogPath } from './site.config.mjs';
import { renderBlogIndex, renderPost, render404, postView, postLangs } from './lib/render.mjs';
import { escXml, truncate, sanitizeHtml } from './lib/utils.mjs';
import { trangBangGia, BANG_GIA_HREFLANG } from './lib/bang-gia.mjs';
import { trangGoiDau } from './lib/goi-dau.mjs';
import { dungTrangChu, HOME_LANGS, homePath } from './lib/trang-chu-ngon-ngu.mjs';

const ROOT = path.dirname(fileURLToPath(import.meta.url));
const DIST = path.join(ROOT, 'dist');
const SRC = path.join(ROOT, 'src');
const POSTS_DIR = path.join(ROOT, 'content', 'posts');
const MEDIA_DIR = path.join(ROOT, 'content', 'media');

const log = (...a) => console.log('  ', ...a);

async function exists(p) {
  try {
    await fs.access(p);
    return true;
  } catch {
    return false;
  }
}

async function copyDir(from, to) {
  if (!(await exists(from))) return 0;
  await fs.mkdir(to, { recursive: true });
  let count = 0;
  for (const entry of await fs.readdir(from, { withFileTypes: true })) {
    if (entry.name.startsWith('.')) continue;
    const src = path.join(from, entry.name);
    const dst = path.join(to, entry.name);
    if (entry.isDirectory()) count += await copyDir(src, dst);
    else {
      await fs.copyFile(src, dst);
      count++;
    }
  }
  return count;
}

/** Bài đã viết nhưng chưa tới ngày đăng — build in ra cho dễ theo dõi */
const scheduled = [];

/** Đọc toàn bộ bài viết đã lưu */
async function loadPosts() {
  if (!(await exists(POSTS_DIR))) return [];
  const files = (await fs.readdir(POSTS_DIR)).filter((f) => f.endsWith('.json'));
  const posts = [];

  for (const file of files) {
    try {
      const post = JSON.parse(await fs.readFile(path.join(POSTS_DIR, file), 'utf8'));

      if (!post.slug || !post.title) {
        console.warn(`   ⚠  Bỏ qua ${file} — thiếu slug hoặc tiêu đề`);
        continue;
      }
      if (post.status !== 'published') continue;

      // Bài hẹn ngày: publishedAt nằm ở tương lai thì chưa hiện lên web.
      // Mỗi ngày website được dựng lại một lần, tới ngày là bài tự xuất hiện.
      if (post.publishedAt && new Date(post.publishedAt) > new Date()) {
        scheduled.push({ slug: post.slug, at: post.publishedAt, title: post.title });
        continue;
      }

      post.content = sanitizeHtml(post.content || '');
      post.publishedAt = post.publishedAt || new Date().toISOString();
      post.keywords = Array.isArray(post.keywords) ? post.keywords : [];

      // Lọc nội dung các bản dịch y như bản tiếng Việt
      if (post.i18n && typeof post.i18n === 'object') {
        for (const code of Object.keys(post.i18n)) {
          if (!languages[code]) {
            delete post.i18n[code];
            continue;
          }
          post.i18n[code].content = sanitizeHtml(post.i18n[code].content || '');
        }
      }

      posts.push(post);
    } catch (err) {
      console.warn(`   ⚠  Lỗi đọc ${file}: ${err.message}`);
    }
  }

  posts.sort((a, b) => new Date(b.publishedAt) - new Date(a.publishedAt));
  return posts;
}

/**
 * Nhóm bài "ra khách": bài nói về tiệm, giá, địa chỉ, dịch vụ cụ thể ở
 * Bình Thạnh. Đây là chỗ khách đọc rồi mới đặt lịch.
 *
 * Vì sao cần danh sách này: đo liên kết nội bộ trong dist/ ngày 2026-11-02
 * cho thấy hàm chọn bài liên quan đang dồn liên kết vào bài thông tin
 * chung — lich-duong-mong-giua-hai-lan-lam-nail 11 liên kết,
 * nail-mat-meo-han-quoc 10 — còn đúng mấy bài ra khách lại ít nhất:
 * den-vessca-gui-xe-dat-lich 2, up-mong-binh-thanh 3,
 * nail-sinh-vien-binh-thanh 3, tiem-nail-kieu-han-o-sai-gon 3,
 * chon-tiem-nail-uy-tin-binh-thanh 4. Tức là đang chảy ngược: trang
 * đọc cho vui được dẫn nhiều, trang đặt lịch được dẫn ít.
 *
 * Số liệu Search Console 28 ngày tới 2026-10-31 cho thấy mấy bài này
 * xếp hạng tốt nhưng gần như không ai thấy (tiem-nail-phuong-gia-dinh
 * vị trí 4 / 1 hiển thị, den-vessca-gui-xe-dat-lich vị trí 4 / 1 hiển
 * thị), nên việc cần làm là dẫn thêm liên kết vào chúng.
 */
const BAI_RA_KHACH = [
  'tiem-nail-phuong-gia-dinh',
  'gia-lam-nail-binh-thanh',
  'tiem-nail-han-quoc-binh-thanh',
  'up-mong-binh-thanh',
  'chon-tiem-nail-uy-tin-binh-thanh',
  'den-vessca-gui-xe-dat-lich',
  'nail-sinh-vien-binh-thanh',
  'tiem-nail-kieu-han-o-sai-gon',
  'tiem-nail-gan-phu-nhuan-go-vap',
];

/** Điểm giống nhau giữa hai bài: trùng từ khoá nặng hơn cùng danh mục */
function diemGiong(post, p) {
  const shared = (p.keywords || []).filter((k) => (post.keywords || []).includes(k)).length;
  const sameCat = p.category && p.category === post.category ? 2 : 0;
  return shared * 3 + sameCat;
}

/**
 * Bài liên quan — ưu tiên trùng từ khoá, rồi cùng danh mục.
 *
 * Giữ 3 ô như cũ, nhưng để riêng 1 ô cho bài ra khách (xem
 * BAI_RA_KHACH). Bài ra khách tự nó cũng cần bài liên quan nên với
 * chúng thì không giữ ô riêng, tránh mấy bài này chỉ dẫn lẫn nhau.
 */
function pickRelated(post, pool, limit = 3, dem = null) {
  const xep = (arr) =>
    arr
      .map((p) => ({ post: p, score: diemGiong(post, p) }))
      .sort(
        (a, b) =>
          b.score - a.score ||
          new Date(b.post.publishedAt) - new Date(a.post.publishedAt)
      )
      .map((x) => x.post);

  const khac = pool.filter((p) => p.slug !== post.slug);
  if (BAI_RA_KHACH.includes(post.slug)) return xep(khac).slice(0, limit);

  const raKhach = xep(khac.filter((p) => BAI_RA_KHACH.includes(p.slug)));
  const conLai = xep(khac.filter((p) => !BAI_RA_KHACH.includes(p.slug)));

  // Hạn mức: không để một bài ra khách hút hết liên kết. Lần chạy đầu
  // không có hạn mức thì den-vessca-gui-xe-dat-lich nhận 21 liên kết
  // còn up-mong-binh-thanh vẫn 3 — dồn cục như vậy vừa không tự nhiên
  // vừa bỏ sót mấy bài cần đẩy. Chọn bài hợp nhất mà chưa quá hạn mức.
  let chon = [];
  if (raKhach.length) {
    let pick = raKhach[0];
    if (dem) {
      const hanMuc = Math.ceil(pool.length / raKhach.length) + 1;
      pick =
        raKhach.find((p) => (dem.get(p.slug) || 0) < hanMuc) ||
        raKhach.reduce((a, b) =>
          (dem.get(a.slug) || 0) <= (dem.get(b.slug) || 0) ? a : b
        );
      dem.set(pick.slug, (dem.get(pick.slug) || 0) + 1);
    }
    chon.push(pick);
  }
  for (const p of conLai) {
    if (chon.length >= limit) break;
    chon.push(p);
  }
  // Đặt bài ra khách xuống cuối: hai ô đầu vẫn là bài đọc tiếp tự nhiên
  return chon.length > 1 ? [...chon.slice(1), chon[0]] : chon;
}

/** Các bản ngôn ngữ của một bài, để sinh thẻ hreflang */
const postAlternates = (post) =>
  postLangs(post).map((l) => ({ lang: l, url: `${site.url}${blogPath(l)}/${post.slug}/` }));

/**
 * Nút đổi ngôn ngữ trên trang bài viết: ngôn ngữ nào có bản dịch thì
 * trỏ thẳng tới bài, chưa có thì trỏ về trang blog của ngôn ngữ đó
 * (thà đưa khách tới trang blog còn hơn đưa vào trang 404).
 */
function postLangSwitch(post, activeLangs) {
  const have = new Set(postLangs(post));
  return activeLangs.map((l) => ({
    lang: l,
    url: have.has(l) ? `${blogPath(l)}/${post.slug}/` : `${blogPath(l)}/`,
  }));
}

/** Bổ sung cho trang chủ những thứ dễ mất khi thả file HTML mới từ admin */
function enhanceHomepage(html) {
  let out = html;
  const added = [];

  if (!/rel=["']icon["']/i.test(out)) {
    out = out.replace(
      /<\/head>/i,
      `<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta name="theme-color" content="#111111">
</head>`
    );
    added.push('favicon');
  }
  if (!/rel=["']canonical["']/i.test(out)) {
    out = out.replace(/<\/head>/i, `<link rel="canonical" href="${site.url}/">\n</head>`);
    added.push('canonical');
  }
  if (!/application\/rss\+xml/i.test(out)) {
    out = out.replace(
      /<\/head>/i,
      `<link rel="alternate" type="application/rss+xml" title="Blog ${site.name}" href="${site.url}/rss.xml">\n</head>`
    );
    added.push('RSS');
  }
  if (!/href=["']\/?blog\/?["']/i.test(out)) {
    const before = out;
    out = out.replace(/(<a\s[^>]*href=["']#booking["'][^>]*>)/i, `<a href="/blog/">Blog</a>\n      $1`);
    if (out !== before) added.push('link Blog');
  }

  if (added.length) log(`Bổ sung vào trang chủ: ${added.join(', ')}`);
  return out;
}

/** Sitemap có khai báo hreflang cho từng bản ngôn ngữ */
function buildSitemap(posts) {
  const today = new Date().toISOString().slice(0, 10);
  const entries = [];

  // Trang chủ: bản tiếng Việt ở "/", bản khác ở /en/, /ko/, /zh/ (lib/trang-chu-ngon-ngu.mjs)
  const homeAlts = HOME_LANGS.map((l) => ({ lang: l, url: `${site.url}${homePath(l)}` }));
  for (const { url } of homeAlts) {
    entries.push({ loc: url, lastmod: today, changefreq: 'weekly', priority: '1.0', alts: homeAlts });
  }

  // Trang blog của từng ngôn ngữ
  const active = langOrder.filter((l) => posts.some((p) => postView(p, l)));
  const indexAlts = active.map((l) => ({ lang: l, url: `${site.url}${blogPath(l)}/` }));
  for (const l of active) {
    entries.push({
      loc: `${site.url}${blogPath(l)}/`,
      lastmod: today,
      changefreq: 'daily',
      priority: '0.9',
      alts: indexAlts,
    });
  }

  // Từng bài, từng ngôn ngữ
  for (const p of posts) {
    const alts = postAlternates(p);
    for (const { lang, url } of alts) {
      const v = postView(p, lang);
      entries.push({
        loc: url,
        lastmod: (p.updatedAt || p.publishedAt).slice(0, 10),
        changefreq: 'monthly',
        priority: '0.8',
        alts,
        image: p.coverImage
          ? p.coverImage.startsWith('http')
            ? p.coverImage
            : site.url + p.coverImage
          : null,
        title: v.title,
      });
    }
  }

  return `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml"
        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">
${entries
  .map(
    (u) => `  <url>
    <loc>${escXml(u.loc)}</loc>
    <lastmod>${u.lastmod}</lastmod>
    <changefreq>${u.changefreq}</changefreq>
    <priority>${u.priority}</priority>${u.alts
      .map(
        (a) =>
          `\n    <xhtml:link rel="alternate" hreflang="${escXml(languages[a.lang].hreflang)}" href="${escXml(a.url)}"/>`
      )
      .join('')}${
      u.image
        ? `
    <image:image>
      <image:loc>${escXml(u.image)}</image:loc>
      <image:title>${escXml(u.title)}</image:title>
    </image:image>`
        : ''
    }
  </url>`
  )
  .join('\n')}
</urlset>`;
}

function buildRss(posts, lang) {
  const L = languages[lang];
  const shown = posts.filter((p) => postView(p, lang));
  return `<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
  <title>${escXml(L.blogTitle)}</title>
  <link>${site.url}${blogPath(lang)}/</link>
  <description>${escXml(L.blogDescription)}</description>
  <language>${escXml(L.hreflang)}</language>
  <lastBuildDate>${new Date().toUTCString()}</lastBuildDate>
  <atom:link href="${site.url}${L.base}/rss.xml" rel="self" type="application/rss+xml"/>
${shown
  .slice(0, 30)
  .map((p) => {
    const v = postView(p, lang);
    return `  <item>
    <title>${escXml(v.title)}</title>
    <link>${site.url}${blogPath(lang)}/${p.slug}/</link>
    <guid isPermaLink="true">${site.url}${blogPath(lang)}/${p.slug}/</guid>
    <pubDate>${new Date(p.publishedAt).toUTCString()}</pubDate>
    <description>${escXml(truncate(v.excerpt || v.content, 240))}</description>
  </item>`;
  })
  .join('\n')}
</channel>
</rss>`;
}

function buildRobots() {
  return `User-agent: *
Allow: /
Disallow: /admin
Disallow: /admin/

Sitemap: ${site.url}/sitemap.xml
`;
}

// ============================================================
//  CHẠY BUILD
/** Bài hẹn giờ + bài còn thiếu ảnh — đọc thẳng file gốc, kể cả bài chưa tới giờ */
async function soNoiBo() {
  const out = { dungLuc: new Date().toISOString(), henGio: [], canAnh: [] };
  // Đợt 38: còn ảnh "theo yêu cầu" chưa lấy (content/media/yeu-cau.json) thì báo cho cron biết.
  try {
    const yc = JSON.parse(await fs.readFile(path.join(MEDIA_DIR, 'yeu-cau.json'), 'utf8'));
    out.yeuCauAnh = yc.some((x) => x && x.luu && x.tim && !x.xong && (x.thu || 0) < 3);
  } catch { out.yeuCauAnh = false; }
  if (!(await exists(POSTS_DIR))) return out;
  for (const f of (await fs.readdir(POSTS_DIR)).filter((x) => x.endsWith('.json'))) {
    try {
      const p = JSON.parse(await fs.readFile(path.join(POSTS_DIR, f), 'utf8'));
      if (p.status !== 'published' || !p.slug) continue;
      if (p.publishedAt && new Date(p.publishedAt) > new Date()) {
        out.henGio.push({ slug: p.slug, at: p.publishedAt });
      }
      if (p.anh && !p.anh.xong) out.canAnh.push({ slug: p.slug, file: f, at: p.publishedAt || '' });
    } catch { /* file hỏng đã được báo ở loadPosts */ }
  }
  out.henGio.sort((a, b) => new Date(a.at) - new Date(b.at));
  // Đợt 37: bài ĐÃ LÊN WEB mà thiếu ảnh làm trước (khách đang thấy ô trống),
  // rồi tới bài sắp đăng (sớm nhất trước) — để ảnh có sẵn trước ngày đăng.
  const bayGio = Date.now();
  const sau = (x) => new Date(x.at || 0).getTime() > bayGio;
  out.canAnh.sort((a, b) =>
    sau(a) !== sau(b) ? (sau(a) ? 1 : -1)
      : sau(a) ? String(a.at).localeCompare(String(b.at))
      : String(b.at).localeCompare(String(a.at)));
  return out;
}

// ============================================================
async function main() {
  const t0 = Date.now();
  console.log('\n▸ VESSCA — bắt đầu build\n');

  await fs.rm(DIST, { recursive: true, force: true });
  await fs.mkdir(DIST, { recursive: true });

  const copied = await copyDir(SRC, DIST);
  log(`Chép ${copied} file tĩnh từ src/`);

  const media = await copyDir(MEDIA_DIR, path.join(DIST, 'media'));
  if (media) log(`Chép ${media} ảnh bài viết`);

  const indexPath = path.join(DIST, 'index.html');
  if (await exists(indexPath)) {
    // Ảnh 4 gói gội đầu ở trang chủ: ảnh kho ảnh (content/media/goi-dau) nếu đã về, chưa có thì ảnh cắt từ menu.
    let anhGoi = [];
    try { anhGoi = await fs.readdir(path.join(MEDIA_DIR, 'goi-dau')); } catch { /* chưa có */ }
    const trangChuGoc = (await fs.readFile(indexPath, 'utf8')).replace(/\{\{GOI_IMG_(\d)\}\}/g,
      (_, n) => (anhGoi.includes(`goi-${n}.jpg`) ? '/media' : '/images') + `/goi-dau/goi-${n}.jpg`);
    await fs.writeFile(indexPath, enhanceHomepage(trangChuGoc), 'utf8');
    // Trang chủ riêng cho từng ngôn ngữ, để khách nước ngoài tìm thấy trên Google
    const tc = dungTrangChu(site, await fs.readFile(indexPath, 'utf8'), (w) => console.warn('   ⚠  Trang chủ:', w));
    await fs.writeFile(indexPath, tc.vi, 'utf8');
    const homeDone = [];
    for (const l of HOME_LANGS) {
      if (l === 'vi' || !tc[l]) continue;
      await fs.mkdir(path.join(DIST, l), { recursive: true });
      await fs.writeFile(path.join(DIST, l, 'index.html'), tc[l], 'utf8');
      homeDone.push(homePath(l));
    }
    if (homeDone.length) log(`Sinh trang chủ ngôn ngữ: ${homeDone.join(', ')}`);
  } else {
    console.warn('   ⚠  Không tìm thấy src/index.html — trang chủ sẽ trống');
  }

  const posts = await loadPosts();
  log(`Tìm thấy ${posts.length} bài đã đăng`);

  if (scheduled.length) {
    scheduled.sort((a, b) => new Date(a.at) - new Date(b.at));
    log(`Còn ${scheduled.length} bài hẹn ngày, bài kế tiếp: ${scheduled[0].at.slice(0, 10)} — ${scheduled[0].title}`);
  }


  // Ngôn ngữ nào chưa có bài nào thì không sinh trang — trang blog rỗng
  // bị Google đánh giá là trang mỏng, thà chưa có còn hơn có mà trống.
  const activeLangs = langOrder.filter((l) => posts.some((p) => postView(p, l)));
  const skipped = langOrder.filter((l) => !activeLangs.includes(l));
  if (skipped.length) {
    log(`Bỏ qua (chưa có bài): ${skipped.map((l) => languages[l].label).join(', ')}`);
  }

  const indexAlts = activeLangs.map((l) => ({ lang: l, url: `${site.url}${blogPath(l)}/` }));
  const indexSwitch = activeLangs.map((l) => ({ lang: l, url: `${blogPath(l)}/` }));

  for (const lang of activeLangs) {
    const dir = path.join(DIST, ...blogPath(lang).split('/').filter(Boolean));
    await fs.mkdir(dir, { recursive: true });

    // Đếm riêng từng ngôn ngữ: mỗi bản dịch có số bài khác nhau
    const demRaKhach = new Map();

    await fs.writeFile(
      path.join(dir, 'index.html'),
      renderBlogIndex({
        lang,
        posts,
        categories,
        alternates: indexAlts,
        langSwitch: indexSwitch,
      }),
      'utf8'
    );

    const inLang = posts.filter((p) => postView(p, lang));
    for (const post of inLang) {
      const postDir = path.join(dir, post.slug);
      await fs.mkdir(postDir, { recursive: true });
      await fs.writeFile(
        path.join(postDir, 'index.html'),
        renderPost({
          lang,
          post,
          related: pickRelated(post, inLang, 3, demRaKhach),
          alternates: postAlternates(post),
          langSwitch: postLangSwitch(post, activeLangs),
        }),
        'utf8'
      );
    }

    // RSS riêng cho từng ngôn ngữ
    const rssDir = path.join(DIST, ...languages[lang].base.split('/').filter(Boolean));
    await fs.mkdir(rssDir, { recursive: true });
    await fs.writeFile(path.join(rssDir, 'rss.xml'), buildRss(posts, lang), 'utf8');

    log(`${languages[lang].label.padEnd(10)} ${String(inLang.length).padStart(2)} bài  →  ${blogPath(lang)}/`);
  }

  await fs.writeFile(path.join(DIST, '404.html'), render404('vi'), 'utf8');
  // Trang bảng giá riêng /bang-gia/ (+ en/ko/zh) — lấy giá từ trang chủ
  const bangGia = trangBangGia(site, await fs.readFile(path.join(SRC, 'index.html'), 'utf8'));
  for (const t of bangGia) {
    await fs.mkdir(path.join(DIST, t.dir), { recursive: true });
    await fs.writeFile(path.join(DIST, t.dir, 'index.html'), t.html, 'utf8');
  }
  if (bangGia.length) log(`Sinh ${bangGia.length} trang bảng giá (/bang-gia/)`);
  // Trang bảng giá gội đầu /goi-dau/ (+ en/ko/zh) — đợt 38. Ảnh cron đã tải về thì dùng, chưa có thì dùng ảnh cắt từ menu.
  let coAnhGoi = [];
  try { coAnhGoi = await fs.readdir(path.join(MEDIA_DIR, 'goi-dau')); } catch { /* chưa có ảnh nào */ }
  const goiDau = trangGoiDau(site, new Set(coAnhGoi));
  for (const t of goiDau) {
    await fs.mkdir(path.join(DIST, t.dir), { recursive: true });
    await fs.writeFile(path.join(DIST, t.dir, 'index.html'), t.html, 'utf8');
  }
  log(`Sinh ${goiDau.length} trang gội đầu (/goi-dau/)`);
  let sitemap = buildSitemap(posts);
  for (const nhom of [goiDau]) {
    const homNay = new Date().toISOString().slice(0, 10);
    const altLinks = nhom.map((b) => `\n    <xhtml:link rel="alternate" hreflang="${BANG_GIA_HREFLANG[b.lang]}" href="${b.loc}"/>`).join('');
    const them = nhom.map((b) => `  <url>\n    <loc>${b.loc}</loc>\n    <lastmod>${homNay}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.9</priority>${altLinks}\n  </url>`).join('\n');
    sitemap = sitemap.replace('</urlset>', them + '\n</urlset>');
  }
  if (bangGia.length) {
    const homNay = new Date().toISOString().slice(0, 10);
    const altLinks = bangGia.map((b) => `\n    <xhtml:link rel="alternate" hreflang="${BANG_GIA_HREFLANG[b.lang]}" href="${b.loc}"/>`).join('');
    const them = bangGia.map((b) => `  <url>\n    <loc>${b.loc}</loc>\n    <lastmod>${homNay}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.9</priority>${altLinks}\n  </url>`).join('\n');
    sitemap = sitemap.replace('</urlset>', them + '\n</urlset>');
  }
  await fs.writeFile(path.join(DIST, 'sitemap.xml'), sitemap, 'utf8');
  await fs.writeFile(path.join(DIST, 'robots.txt'), buildRobots(), 'utf8');
  log('Sinh sitemap.xml, rss.xml, robots.txt, 404.html');

  // Sổ nội bộ cho việc chạy định kỳ trên Cloudflare (functions/_lib/anh-blog.js):
  // bài nào đang chờ giờ đăng, bài nào còn thiếu ảnh. Chỉ có slug và giờ —
  // không có gì bí mật, nhưng vẫn để ngoài sitemap.
  await fs.mkdir(path.join(DIST, '_noi-bo'), { recursive: true });
  await fs.writeFile(
    path.join(DIST, '_noi-bo', 'bai-viet.json'),
    JSON.stringify(await soNoiBo(), null, 1),
    'utf8'
  );

  await fs.writeFile(
    path.join(DIST, '_redirects'),
    `/blog.php   /blog/   301
/post.php   /blog/   301
`,
    'utf8'
  );

  console.log(`\n✓ Xong trong ${((Date.now() - t0) / 1000).toFixed(1)}s → dist/\n`);
}

main().catch((err) => {
  console.error('\n✗ Build lỗi:', err);
  process.exit(1);
});
