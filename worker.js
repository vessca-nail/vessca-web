/**
 * ============================================================
 *  CỬA VÀO CỦA WEBSITE VESSCA
 * ============================================================
 *  Mọi truy cập vào vessca.com đều đi qua file này:
 *    • Đường dẫn /admin...  → giao cho trang quản trị xử lý
 *    • Còn lại              → trả về trang tĩnh trong thư mục dist/
 */

import { onRequest as admin } from './functions/admin/[[path]].js';

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);

    // Gõ /admin thiếu dấu gạch cuối → thêm vào cho đúng
    if (url.pathname === '/admin') {
      return Response.redirect(new URL('/admin/', url).toString(), 302);
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
    return env.ASSETS.fetch(request);
  },
};
