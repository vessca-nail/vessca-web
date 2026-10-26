/**
 * ============================================================
 *  TRANG QUẢN TRỊ VESSCA — /admin
 * ============================================================
 *  Đây là "phòng điều khiển" của website. Từ đây bạn có thể:
 *    • Viết / sửa / xoá bài blog
 *    • Thả file HTML mới để đổi giao diện trang chủ
 *    • Tải ảnh lên
 *    • Quay lui về giao diện cũ nếu lỡ tay
 *
 *  Mọi thay đổi được ghi vào kho GitHub, Cloudflare tự dựng lại web.
 */

import { isLoggedIn, createSession, clearSession, checkPassword, missingConfig, deriveKey } from '../_lib/auth.js';
import * as gh from '../_lib/github.js';
import { chayDinhKy } from '../_lib/anh-blog.js';
import { layThongKe } from '../_lib/thong-ke.js';
import { loginPage, listPage, editorPage, designPage, mediaPage, statusPage, bookingsPage, thongKePage } from '../_lib/pages.js';
import { EDITOR_JS } from '../_lib/editor-js.js';
import { slugify, sanitizeHtml } from '../../lib/utils.mjs';

const POSTS = 'content/posts';
const MEDIA = 'content/media';
const HOMEPAGE = 'src/index.html';

const html = (body, status = 200) =>
  new Response(body, { status, headers: { 'Content-Type': 'text/html; charset=utf-8' } });

const json = (data, status = 200) =>
  new Response(JSON.stringify(data), { status, headers: { 'Content-Type': 'application/json' } });

const text = (msg, status = 400) =>
  new Response(msg, { status, headers: { 'Content-Type': 'text/plain; charset=utf-8' } });

const redirect = (to, headers = {}) =>
  new Response(null, { status: 302, headers: { Location: to, ...headers } });

export async function onRequest(context) {
  const { request, env } = context;
  const url = new URL(request.url);
  const path = url.pathname.replace(/^\/admin\/?/, '').replace(/\/$/, '');
  const method = request.method;

  // ---- Chưa cấu hình xong trên Cloudflare ----
  const missing = missingConfig(env);
  if (missing.length) {
    return html(
      loginPage(
        '',
        `Chưa cấu hình xong. Còn thiếu biến môi trường trong Cloudflare: <b>${missing.join(', ')}</b>.<br>
         Vào Cloudflare → Workers &amp; Pages → dự án này → Settings → Variables and Secrets để thêm.`
      )
    );
  }

  // ---- Đăng nhập / đăng xuất ----
  if (path === 'login' && method === 'POST') {
    const form = await request.formData();
    if (!checkPassword(form.get('password'), env)) {
      return html(loginPage('Mật khẩu không đúng. Thử lại nha.'), 401);
    }
    return redirect('/admin/', { 'Set-Cookie': await createSession(env) });
  }

  if (path === 'logout') {
    return redirect('/admin/', { 'Set-Cookie': clearSession() });
  }

  // ---- Chặn mọi thứ còn lại nếu chưa đăng nhập ----
  if (!(await isLoggedIn(request, env))) {
    if (path.startsWith('api/')) return text('Phiên đăng nhập đã hết hạn. Tải lại trang.', 401);
    return html(loginPage());
  }

  try {
    switch (true) {
      // ---------- Mã JavaScript cho trình soạn bài ----------
      case path === 'editor.js':
        return new Response(EDITOR_JS, {
          headers: {
            'Content-Type': 'application/javascript; charset=utf-8',
            'Cache-Control': 'no-store',
          },
        });

      // ---------- Danh sách bài viết ----------
      case path === '':
        return html(listPage({ posts: await loadPosts(env), flash: url.searchParams.get('msg') }));

      // ---------- Viết bài mới ----------
      case path === 'new':
        return html(editorPage({ post: null, isNew: true }));

      // ---------- Sửa bài ----------
      case path.startsWith('edit/'): {
        const slug = decodeURIComponent(path.slice(5));
        const file = await gh.getFile(env, `${POSTS}/${slug}.json`);
        if (!file) return html(listPage({ posts: await loadPosts(env), flash: 'Không tìm thấy bài viết đó.' }));
        return html(editorPage({ post: JSON.parse(file.text), isNew: false }));
      }

      // ---------- Giao diện trang chủ ----------
      case path === 'design': {
        const [history, current] = await Promise.all([
          gh.fileHistory(env, HOMEPAGE),
          gh.getFile(env, HOMEPAGE).catch(() => null),
        ]);
        return html(
          designPage({
            history,
            flash: url.searchParams.get('msg'),
            error: url.searchParams.get('err'),
            currentSize: current?.size,
          })
        );
      }

      // ---------- Thư viện ảnh ----------
      case path === 'media': {
        const files = (await gh.listDir(env, MEDIA))
          .filter((f) => f.type === 'file' && !f.name.startsWith('.'))
          .sort((a, b) => b.name.localeCompare(a.name));
        return html(mediaPage({ files, flash: url.searchParams.get('msg') }));
      }

      // ---------- Thống kê truy cập ----------
      case path === 'thong-ke': {
        if (!env.BOOKINGS) return html(thongKePage({ soNgay: 7, tu: '', tong: {} }));
        const n = [1, 7, 30, 90, 365].includes(Number(url.searchParams.get('ngay'))) ? Number(url.searchParams.get('ngay')) : 7;
        return html(thongKePage(await layThongKe(env, n)));
      }

      // ---------- Đơn đặt lịch từ website ----------
      case path === 'bookings': {
        if (!env.BOOKINGS) {
          return html(
            bookingsPage({
              bookings: [],
              pollKey: null,
              error:
                'Chưa gắn kho dữ liệu đặt lịch (BOOKINGS). Vào Cloudflare → Workers & Pages → ' +
                'vessca-web → Settings → Bindings để nối tới D1 "vessca-bookings".',
            })
          );
        }
        const { results } = await env.BOOKINGS
          .prepare(
            `SELECT id, created_at, name, phone, service, preferred, note, status
               FROM bookings ORDER BY id DESC LIMIT 200`
          )
          .all();
        const fmt = new Intl.DateTimeFormat('vi-VN', {
          timeZone: 'Asia/Ho_Chi_Minh',
          day: '2-digit', month: '2-digit', year: 'numeric',
          hour: '2-digit', minute: '2-digit', hour12: false,
        });
        return html(
          bookingsPage({
            bookings: (results || []).map((b) => ({
              ...b,
              created_at_vn: fmt.format(new Date(b.created_at)),
            })),
            pollKey: await deriveKey('instore-poll', env),
            flash: url.searchParams.get('msg'),
          })
        );
      }

      // ---------- Đổi trạng thái một đơn đặt lịch ----------
      // ---------- Chạy tay việc định kỳ (ảnh blog + đăng bài tới giờ) ----------
      case path === 'api/chay-dinh-ky' && method === 'POST': {
        const kq = await chayDinhKy(env);
        return json(kq);
      }

      case path === 'api/booking-status' && method === 'POST': {
        if (!env.BOOKINGS) return text('Chưa gắn kho dữ liệu đặt lịch.', 503);
        const { ids, status } = await request.json();
        const list = (Array.isArray(ids) ? ids : [])
          .map(Number)
          .filter((n) => Number.isInteger(n) && n > 0)
          .slice(0, 200);
        if (!list.length) return text('Thiếu mã đơn.');
        if (!['moi', 'da_xem', 'da_xac_nhan', 'huy'].includes(status)) {
          return text('Trạng thái không hợp lệ.');
        }
        await env.BOOKINGS
          .prepare(
            `UPDATE bookings SET status = ?, seen_at = ?
              WHERE id IN (${list.map(() => '?').join(',')})`
          )
          .bind(status, new Date().toISOString(), ...list)
          .run();
        return json({ ok: true });
      }

      // ---------- Kiểm tra hệ thống ----------
      case path === 'status': {
        const access = await gh.checkAccess(env);
        const posts = access.ok ? await loadPosts(env) : [];
        return html(
          statusPage({
            repo: env.GITHUB_REPO,
            checks: [
              { ok: true, label: 'Trang quản trị chạy bình thường' },
              { ok: !!env.ADMIN_PASSWORD, label: 'Đã đặt mật khẩu quản trị' },
              { ok: !!env.SESSION_SECRET, label: 'Đã đặt khoá bảo mật phiên đăng nhập' },
              {
                ok: access.ok,
                label: 'Kết nối GitHub',
                detail: access.ok ? `Kho ${access.repo}, nhánh ${access.branch}` : access.reason,
              },
              {
                ok: posts.length > 0,
                label: 'Đã có bài viết',
                detail: `${posts.length} bài — ${posts.filter((p) => p.status === 'published').length} bài đã đăng`,
              },
            ],
          })
        );
      }

      // ---------- Lưu bài viết ----------
      case path === 'api/save' && method === 'POST':
        return await savePost(request, env);

      // ---------- Xoá bài viết ----------
      case path === 'api/delete' && method === 'POST': {
        const { slug } = await request.json();
        if (!slug) return text('Thiếu mã bài viết.');
        await gh.deleteFile(env, `${POSTS}/${slug}.json`, `Xoá bài: ${slug}`);
        return json({ ok: true });
      }

      // ---------- Đổi giao diện trang chủ ----------
      case path === 'api/design' && method === 'POST': {
        const { html: pageHtml } = await request.json();
        if (!pageHtml || pageHtml.length < 200) return text('Nội dung file quá ngắn, có vẻ không đúng.');
        if (pageHtml.length > 3_000_000) return text('File nặng quá 3 MB.');
        await gh.putFile(
          env,
          HOMEPAGE,
          gh.toBase64(pageHtml),
          `Đổi giao diện trang chủ (từ trang admin)`
        );
        return json({ ok: true });
      }

      // ---------- Quay lui giao diện cũ ----------
      case path === 'api/restore' && method === 'POST': {
        const { sha } = await request.json();
        if (!sha) return text('Thiếu mã phiên bản.');
        const old = await gh.getFileAt(env, HOMEPAGE, sha);
        await gh.putFile(
          env,
          HOMEPAGE,
          gh.toBase64(old),
          `Quay lui giao diện trang chủ về ${sha.slice(0, 7)}`
        );
        return json({ ok: true });
      }

      // ---------- Tải ảnh lên ----------
      case path === 'api/media' && method === 'POST':
        return await uploadMedia(request, env);

      default:
        return html(listPage({ posts: await loadPosts(env), flash: 'Không tìm thấy trang đó.' }), 404);
    }
  } catch (err) {
    const msg = err?.message || String(err);
    if (path.startsWith('api/')) return text(msg, 500);
    return html(
      listPage({ posts: [], flash: `Có lỗi xảy ra: ${msg}` }),
      500
    );
  }
}

/** Đọc toàn bộ bài viết từ GitHub, mới nhất lên đầu */
async function loadPosts(env) {
  const files = (await gh.listDir(env, POSTS)).filter((f) => f.name.endsWith('.json'));
  const posts = await Promise.all(
    files.map(async (f) => {
      try {
        const file = await gh.getFile(env, `${POSTS}/${f.name}`);
        return JSON.parse(file.text);
      } catch {
        return null;
      }
    })
  );
  return posts
    .filter(Boolean)
    .sort((a, b) => new Date(b.publishedAt || 0) - new Date(a.publishedAt || 0));
}

async function savePost(request, env) {
  const body = await request.json();

  const slug = slugify(body.slug || body.title || '');
  if (!slug) return text('Đường dẫn bài viết không hợp lệ.');
  if (!body.title?.trim()) return text('Bài viết chưa có tiêu đề.');

  const content = sanitizeHtml(body.content || '');
  if (!content) return text('Bài viết chưa có nội dung.');

  const now = new Date().toISOString();
  const post = {
    slug,
    title: body.title.trim(),
    category: body.category || '',
    author: 'VESSCA',
    status: body.status === 'published' ? 'published' : 'draft',
    publishedAt: body.publishedAt || now,
    updatedAt: now,
    excerpt: (body.excerpt || '').trim(),
    metaTitle: (body.metaTitle || '').trim(),
    metaDescription: (body.metaDescription || '').trim(),
    keywords: Array.isArray(body.keywords) ? body.keywords.filter(Boolean).slice(0, 25) : [],
    coverImage: body.coverImage || '',
    coverAlt: (body.coverAlt || '').trim(),
    faq: Array.isArray(body.faq)
      ? body.faq.filter((f) => f?.q && f?.a).map((f) => ({ q: String(f.q), a: String(f.a) })).slice(0, 12)
      : [],
    content,
  };

  await gh.putFile(
    env,
    `${POSTS}/${slug}.json`,
    gh.toBase64(JSON.stringify(post, null, 2)),
    `${body.oldSlug ? 'Sửa' : 'Thêm'} bài: ${post.title}`
  );

  // Nếu đổi đường dẫn thì xoá file cũ đi cho khỏi trùng bài
  if (body.oldSlug && body.oldSlug !== slug) {
    await gh.deleteFile(env, `${POSTS}/${body.oldSlug}.json`, `Đổi đường dẫn: ${body.oldSlug} → ${slug}`)
      .catch(() => {});
  }

  return json({ ok: true, slug });
}

const IMAGE_TYPES = {
  'image/jpeg': 'jpg',
  'image/png': 'png',
  'image/webp': 'webp',
  'image/gif': 'gif',
  'image/avif': 'avif',
};

async function uploadMedia(request, env) {
  const form = await request.formData();
  const file = form.get('file');
  if (!file || typeof file === 'string') return text('Không nhận được file ảnh.');

  const ext = IMAGE_TYPES[file.type];
  if (!ext) return text('Chỉ nhận ảnh JPG, PNG, WebP, GIF hoặc AVIF.');

  const bytes = new Uint8Array(await file.arrayBuffer());
  if (bytes.length > 5 * 1024 * 1024) return text('Ảnh nặng quá 5 MB.');

  const base = slugify((file.name || 'anh').replace(/\.[^.]+$/, '')) || 'anh';
  const stamp = new Date().toISOString().slice(0, 10).replace(/-/g, '');
  const name = `${stamp}-${base}-${Math.random().toString(36).slice(2, 7)}.${ext}`;

  await gh.putFile(env, `${MEDIA}/${name}`, gh.bytesToBase64(bytes), `Tải ảnh lên: ${name}`);
  return json({ ok: true, url: `/media/${name}`, name });
}
