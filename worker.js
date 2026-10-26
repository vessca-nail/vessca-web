/**
 * ============================================================
 *  CỬA VÀO CỦA WEBSITE VESSCA
 * ============================================================
 *  Mọi truy cập vào vessca.com đều đi qua file này:
 *    • Đường dẫn /admin...  → giao cho trang quản trị xử lý
 *    • Còn lại              → trả về trang tĩnh trong thư mục dist/
 */

import { onRequest as admin } from './functions/admin/[[path]].js';
import { onRequest as booking } from './functions/_lib/booking.js';
import { chayDinhKy } from './functions/_lib/anh-blog.js';
import { ghiLuot, donDep } from './functions/_lib/thong-ke.js';

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);

    // Gõ /admin thiếu dấu gạch cuối → thêm vào cho đúng
    if (url.pathname === '/admin') {
      return Response.redirect(new URL('/admin/', url).toString(), 302);
    }

    // Thống kê truy cập (tk.js gửi về). Lỗi gì cũng không được làm phiền khách.
    if (url.pathname === '/api/tk') {
      try { return await ghiLuot(request, env); }
      catch (e) { console.error('Lỗi thống kê:', e?.message || e); return new Response(null, { status: 204 }); }
    }

    // Đặt lịch từ trang chủ + đường cho phần mềm ở tiệm lấy đơn
    if (url.pathname.startsWith('/api/booking')) {
      try {
        return await booking({ request, env, ctx });
      } catch (err) {
        console.error('Lỗi đặt lịch:', err?.stack || err);
        return new Response(
          JSON.stringify({ ok: false, error: 'Máy chủ gặp lỗi khi nhận đơn.' }),
          { status: 500, headers: { 'Content-Type': 'application/json; charset=utf-8' } }
        );
      }
    }

    if (url.pathname.startsWith('/admin/')) {
      try {
        return await admin({ request, env, ctx });
      } catch (err) {
        return new Response(
          `Trang quản trị gặp lỗi: ${err?.message || err}`,
          { status: 500, headers: { 'Content-Type': 'text/plain; charset=utf-8' } }
        );
      }
    }

    // Video: trả từng đoạn theo yêu cầu (HTTP Range / 206). Safari trên iPhone/iPad
    // KHÔNG chạy video nếu máy chủ không hỗ trợ việc này — trước đây kho tĩnh luôn
    // trả nguyên file (200) nên video đầu trang đứng hình trên iPhone.
    if (url.pathname.startsWith('/videos/')) {
      return serveVideo(request, env);
    }

    // Trang chủ, blog, ảnh, video — lấy từ thư mục đã dựng sẵn
    const res = await env.ASSETS.fetch(request);

    // Đường dẫn không tồn tại → trả về trang 404 mang nhận diện VESSCA
    if (res.status === 404) {
      const page = await env.ASSETS.fetch(new URL('/404.html', url).toString());
      return new Response(page.body, {
        status: 404,
        headers: { 'Content-Type': 'text/html; charset=utf-8' },
      });
    }

    return res;
  },

  // Chạy định kỳ (xem "triggers" trong wrangler.jsonc): đăng bài hẹn giờ
  // đúng giờ + lấy ảnh cho bài blog. Chi tiết trong functions/_lib/anh-blog.js
  async scheduled(event, env, ctx) {
    ctx.waitUntil(
      chayDinhKy(env)
        .then((kq) => console.log('Chạy định kỳ:', JSON.stringify(kq)))
        .catch((e) => console.error('Chạy định kỳ lỗi:', e?.stack || e))
    );
    ctx.waitUntil(donDep(env).catch((e) => console.error('Dọn thống kê lỗi:', e?.message || e)));
  },
};

/** Trả video có hỗ trợ Range (206 Partial Content) để Safari phát được. */
async function serveVideo(request, env) {
  const plain = new Request(request.url, { method: 'GET' });
  const res = await env.ASSETS.fetch(plain);
  if (!res.ok) return res;

  const headers = new Headers(res.headers);
  headers.set('Accept-Ranges', 'bytes');
  headers.set('Cache-Control', 'public, max-age=604800');
  headers.delete('Content-Encoding');

  const range = request.headers.get('Range');
  const m = range && /^bytes=(\d*)-(\d*)$/.exec(range.trim());
  if (request.method === 'HEAD' || !m) {
    const body = request.method === 'HEAD' ? null : res.body;
    return new Response(body, { status: 200, headers });
  }

  const buf = await res.arrayBuffer();
  const size = buf.byteLength;
  let start, end;
  if (m[1] === '') {            // bytes=-500 → 500 byte cuối
    const n = Math.min(Number(m[2]), size);
    start = size - n; end = size - 1;
  } else {
    start = Number(m[1]);
    end = m[2] === '' ? size - 1 : Math.min(Number(m[2]), size - 1);
  }
  if (!(start >= 0) || start >= size || end < start) {
    headers.set('Content-Range', `bytes */${size}`);
    return new Response(null, { status: 416, headers });
  }
  headers.set('Content-Range', `bytes ${start}-${end}/${size}`);
  headers.set('Content-Length', String(end - start + 1));
  return new Response(buf.slice(start, end + 1), { status: 206, headers });
}
