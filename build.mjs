/**
 * ============================================================
 *  BUILD — biến bài viết thành trang web tĩnh
 * ============================================================
 *  Cloudflare chạy file này mỗi lần bạn đăng bài mới.
 *  Nó đọc các bài trong content/posts/ rồi sinh ra trang blog
 *  hoàn chỉnh + sitemap + RSS trong thư mục dist/.
 *
 *  Bạn KHÔNG cần chạy file này bằng tay.
 */

import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { site, categories } from './site.config.mjs';
import { renderBlogIndex, renderPost, render404 } from './lib/render.mjs';
import { escXml, truncate, sanitizeHtml } from './lib/utils.mjs';

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

/** Chép nguyên một thư mục sang chỗ khác */
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

/** Đọc toàn bộ bài viết đã lưu */
async function loadPosts() {
  if (!(await exists(POSTS_DIR))) return [];
  const files = (await fs.readdir(POSTS_DIR)).filter((f) => f.endsWith('.json'));
  const posts = [];

  for (const file of files) {
    try {
      const raw = await fs.readFile(path.join(POSTS_DIR, file), 'utf8');
      const post = JSON.parse(raw);

      if (!post.slug || !post.title) {
        console.warn(`   ⚠  Bỏ qua ${file} — thiếu slug hoặc tiêu đề`);
        continue;
      }
      // Bài nháp không lên web
      if (post.status !== 'published') continue;

      post.content = sanitizeHtml(post.content || '');
      post.publishedAt = post.publishedAt || new Date().toISOString();
      post.keywords = Array.isArray(post.keywords) ? post.keywords : [];
      posts.push(post);
    } catch (err) {
      console.warn(`   ⚠  Lỗi đọc ${file}: ${err.message}`);
    }
  }

  posts.sort((a, b) => new Date(b.publishedAt) - new Date(a.publishedAt));
  return posts;
}

/**
 * Chọn bài liên quan để gắn cuối mỗi bài viết.
 * Ưu tiên bài trùng từ khoá, rồi tới bài cùng danh mục — giúp
 * khách đọc tiếp và giúp Google hiểu các bài liên kết với nhau.
 */
function pickRelated(post, all, limit = 3) {
  return all
    .filter((p) => p.slug !== post.slug)
    .map((p) => {
      const shared = (p.keywords || []).filter((k) =>
        (post.keywords || []).includes(k)
      ).length;
      const sameCat = p.category && p.category === post.category ? 2 : 0;
      return { post: p, score: shared * 3 + sameCat };
    })
    .sort((a, b) => b.score - a.score || new Date(b.post.publishedAt) - new Date(a.post.publishedAt))
    .slice(0, limit)
    .map((x) => x.post);
}

/**
 * Bổ sung cho trang chủ những thứ dễ bị mất khi bạn thả file HTML mới
 * từ trang admin: link tới Blog, link RSS, thẻ canonical.
 * Nếu trang chủ đã có sẵn thì giữ nguyên, không đụng vào.
 */
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
    // Chèn link Blog vào ngay trước nút "Đặt lịch" đầu tiên trong menu
    const before = out;
    out = out.replace(
      /(<a\s[^>]*href=["']#booking["'][^>]*>)/i,
      `<a href="/blog/">Blog</a>\n      $1`
    );
    if (out !== before) added.push('link Blog');
  }

  if (added.length) log(`Bổ sung vào trang chủ: ${added.join(', ')}`);
  return out;
}

function buildSitemap(posts) {
  const today = new Date().toISOString().slice(0, 10);
  const urls = [
    { loc: `${site.url}/`, changefreq: 'weekly', priority: '1.0', lastmod: today },
    { loc: `${site.url}${site.blog.path}/`, changefreq: 'daily', priority: '0.9', lastmod: today },
    ...posts.map((p) => ({
      loc: `${site.url}${site.blog.path}/${p.slug}/`,
      changefreq: 'monthly',
      priority: '0.8',
      lastmod: (p.updatedAt || p.publishedAt).slice(0, 10),
      image: p.coverImage
        ? (p.coverImage.startsWith('http') ? p.coverImage : site.url + p.coverImage)
        : null,
      title: p.title,
    })),
  ];

  return `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">
${urls
  .map(
    (u) => `  <url>
    <loc>${escXml(u.loc)}</loc>
    <lastmod>${u.lastmod}</lastmod>
    <changefreq>${u.changefreq}</changefreq>
    <priority>${u.priority}</priority>${
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

function buildRss(posts) {
  return `<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
  <title>${escXml(site.blog.title)}</title>
  <link>${site.url}${site.blog.path}</link>
  <description>${escXml(site.blog.description)}</description>
  <language>vi-VN</language>
  <lastBuildDate>${new Date().toUTCString()}</lastBuildDate>
  <atom:link href="${site.url}/rss.xml" rel="self" type="application/rss+xml"/>
${posts
  .slice(0, 30)
  .map(
    (p) => `  <item>
    <title>${escXml(p.title)}</title>
    <link>${site.url}${site.blog.path}/${p.slug}/</link>
    <guid isPermaLink="true">${site.url}${site.blog.path}/${p.slug}/</guid>
    <pubDate>${new Date(p.publishedAt).toUTCString()}</pubDate>
    <description>${escXml(truncate(p.excerpt || p.content, 240))}</description>${
      p.category ? `\n    <category>${escXml(p.category)}</category>` : ''
    }
  </item>`
  )
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
// ============================================================
async function main() {
  const t0 = Date.now();
  console.log('\n▸ VESSCA — bắt đầu build\n');

  await fs.rm(DIST, { recursive: true, force: true });
  await fs.mkdir(DIST, { recursive: true });

  // 1. Chép toàn bộ file tĩnh (trang chủ, ảnh, video)
  const copied = await copyDir(SRC, DIST);
  log(`Chép ${copied} file tĩnh từ src/`);

  // 2. Chép ảnh bài viết đã upload từ trang admin
  const media = await copyDir(MEDIA_DIR, path.join(DIST, 'media'));
  if (media) log(`Chép ${media} ảnh bài viết`);

  // 3. Bổ sung link Blog / canonical cho trang chủ
  const indexPath = path.join(DIST, 'index.html');
  if (await exists(indexPath)) {
    const html = await fs.readFile(indexPath, 'utf8');
    await fs.writeFile(indexPath, enhanceHomepage(html), 'utf8');
  } else {
    console.warn('   ⚠  Không tìm thấy src/index.html — trang chủ sẽ trống');
  }

  // 4. Sinh trang blog
  const posts = await loadPosts();
  log(`Tìm thấy ${posts.length} bài đã đăng`);

  await fs.mkdir(path.join(DIST, 'blog'), { recursive: true });
  await fs.writeFile(
    path.join(DIST, 'blog', 'index.html'),
    renderBlogIndex({ posts, categories }),
    'utf8'
  );

  for (const post of posts) {
    const dir = path.join(DIST, 'blog', post.slug);
    await fs.mkdir(dir, { recursive: true });
    await fs.writeFile(
      path.join(dir, 'index.html'),
      renderPost({ post, related: pickRelated(post, posts) }),
      'utf8'
    );
  }
  if (posts.length) log(`Sinh ${posts.length} trang bài viết`);

  // Trang 404 cho đường dẫn sai
  await fs.writeFile(path.join(DIST, '404.html'), render404(), 'utf8');

  // 5. Sinh file cho Google
  await fs.writeFile(path.join(DIST, 'sitemap.xml'), buildSitemap(posts), 'utf8');
  await fs.writeFile(path.join(DIST, 'rss.xml'), buildRss(posts), 'utf8');
  await fs.writeFile(path.join(DIST, 'robots.txt'), buildRobots(), 'utf8');
  log('Sinh sitemap.xml, rss.xml, robots.txt');

  // 6. Chuyển hướng /blog.php (link cũ) sang /blog — giữ thứ hạng Google
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
