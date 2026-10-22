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

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);

    // Gõ /admin thiếu dấu gạch cuối → thêm vào cho đúng
    if (url.pathname === '/admin') {
      return Response.redirect(new URL('/admin/', url).toString(), 302);
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
  },
};
