# VESSCA — website & blog

Website chính thức của **VESSCA Korean Nail Lounge** — chạy trên Cloudflare Pages.

---

## Dùng hằng ngày

Mọi thứ làm ở một chỗ: **https://vessca.com/admin**

| Bạn muốn | Vào mục |
|---|---|
| Viết bài blog mới | **Viết bài** |
| Sửa / xoá bài cũ | **Bài viết** |
| Đổi giao diện trang chủ (thả file HTML mới) | **Giao diện** |
| Quay lui giao diện cũ khi lỡ tay | **Giao diện** → Lịch sử thay đổi |
| Tải ảnh lên dùng cho bài viết | **Ảnh** |
| Kiểm tra web có đang chạy đúng không | **Hệ thống** |

> **Lưu ý:** sau khi bấm Lưu, chờ khoảng **1 phút** rồi tải lại trang web.
> Cloudflare cần chừng đó thời gian để dựng lại trang.

---

## Viết bài sao cho Google tìm thấy

Khi viết bài, cột bên phải có ô **Điểm SEO** chấm điểm theo thời gian thực.
Cứ làm cho các dòng chuyển sang dấu ✓ màu xanh là ổn. Quan trọng nhất:

1. **Chọn từ khoá chính trước khi viết.** Bấm vào các từ khoá gợi ý ở ô
   *Từ khoá*. Từ đầu tiên (có dấu ★) là từ khoá chính.
2. **Đặt từ khoá chính vào tiêu đề** và nhắc lại trong đoạn mở đầu.
3. **Viết ít nhất 300 từ**, chia bằng các tiêu đề phụ (nút **H2**).
4. **Điền Mô tả SEO** khoảng 110–160 ký tự — đây là dòng khách đọc thấy
   trên Google trước khi bấm vào.
5. **Thêm câu hỏi thường gặp** ở cuối trang soạn bài. Google thường hiện
   thẳng câu trả lời này trên kết quả tìm kiếm — rất đáng làm.

Muốn thêm từ khoá mới vào danh sách gợi ý: sửa file `site.config.mjs`,
phần `keywordLibrary`.

---

## Cấu trúc thư mục

```
src/                 Trang chủ và file tĩnh (ảnh, video, logo, favicon)
  index.html         ← trang chủ, đổi được từ trang admin
content/posts/       Bài viết, mỗi bài một file .json
content/media/       Ảnh tải lên từ trang admin
lib/                 Mã sinh giao diện blog
functions/admin/     Trang quản trị
site.config.mjs      Thông tin tiệm + danh sách từ khoá SEO
build.mjs            Script dựng web (Cloudflare tự chạy)
```

---

## Cấu hình trên Cloudflare

Trong Cloudflare → **Workers & Pages** → dự án này → **Settings**:

**Build:**
- Build command: `npm run build`
- Build output directory: `dist`

**Variables and Secrets** (bắt buộc có đủ 5 biến):

| Tên biến | Là gì |
|---|---|
| `ADMIN_PASSWORD` | Mật khẩu đăng nhập trang admin |
| `SESSION_SECRET` | Chuỗi ngẫu nhiên dài, để bảo vệ phiên đăng nhập |
| `GITHUB_TOKEN` | Token GitHub có quyền ghi vào kho này |
| `GITHUB_REPO` | `vessca-nail/vessca-web` |
| `GITHUB_BRANCH` | `main` |

Thiếu biến nào, trang admin sẽ báo rõ tên biến đó khi bạn mở lên.

---

## Cách hệ thống hoạt động

```
Bạn bấm Lưu ở /admin
        ↓
File được ghi vào kho GitHub
        ↓
Cloudflare thấy có thay đổi, tự chạy build.mjs
        ↓
Bài viết thành trang HTML tĩnh + sitemap + RSS
        ↓
vessca.com cập nhật (~1 phút)
```

Vì mọi thay đổi đều đi qua GitHub nên **luôn có lịch sử và quay lui được** —
kể cả khi bạn thả nhầm một file HTML hỏng.

---

## Chạy thử trên máy

```bash
npm install
npm run build        # dựng vào thư mục dist/
npx wrangler pages dev dist   # mở http://localhost:8788
```

Muốn thử cả trang admin ở máy: tạo file `.dev.vars` với 5 biến ở bảng trên.
File này đã được loại khỏi git nên không bị lộ.
