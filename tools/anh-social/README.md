# Lấy ảnh thật từ Instagram về web

Web đang dùng ảnh kho Pixabay. Ảnh kho có hàng nghìn trang khác dùng cùng tấm
đó nên gần như không có cơ hội lên Google Hình ảnh. Ảnh tay tiệm tự làm là ảnh
độc nhất — đó mới là ảnh có giá cho SEO, và là thứ khách thật sự xem trước khi
đặt lịch.

## Cần làm một lần (khoảng 15 phút, chỉ chủ tiệm làm được)

1. **Instagram** → Settings → Account type → chuyển `vessca.nail` sang
   **Professional** (Business hoặc Creator). API của Meta **không đọc được**
   tài khoản cá nhân.
2. **developers.facebook.com** → Create App → thêm sản phẩm **Instagram** →
   *API setup with Instagram login* → Add account → **Generate token**.
3. Token hiện ra là **long-lived, hạn 60 ngày**.

Với tài khoản của chính mình, Meta chỉ cần **Standard Access**: không App Review,
không Business Verification, không cần liên kết Facebook Page.
Quyền dùng: `instagram_business_basic`.

> **Token là bí mật. Repo này public.**
> Không dán token vào bất kỳ file nào trong repo. Chỗ để token:
> Cloudflare → Workers → vessca-web → Settings → Variables (chỗ đang có
> `PIXABAY_API_KEY`), tên biến `IG_ACCESS_TOKEN`.

## Chạy

```bash
export IG_ACCESS_TOKEN='...'                              # không ghi vào repo
node tools/anh-social/lay-anh-instagram.mjs               # chạy thử, không ghi gì
node tools/anh-social/lay-anh-instagram.mjs --ghi         # tải ảnh về thật
node tools/anh-social/lay-anh-instagram.mjs --ghi --so=5  # giới hạn số ảnh mỗi lượt
```

Ảnh lưu ở `content/media/instagram/`, danh mục ở `_index.json`.
`build.mjs` tự chép cả thư mục `content/media/` ra `dist/media/` (đã kiểm tra),
nên ảnh được phục vụ ở `/media/instagram/<tên>.jpg`. Ảnh đã lấy thì lần sau bỏ
qua theo `id` của Instagram.

## Lấy gì, bỏ gì

| Loại trên IG | Xử lý |
|---|---|
| `IMAGE` | Tải ảnh gốc về, tự lưu |
| `CAROUSEL_ALBUM` | Tải từng ảnh con; con là video thì lấy ảnh bìa |
| `VIDEO` / Reels | Lấy **ảnh bìa** (`thumbnail_url`), **không** tải file video |

Vì sao không tải file video:

- Meta **bỏ trống `media_url`** với video dùng nhạc có bản quyền, và với reels
  khi tắt cho phép tải. Reels nail gần như luôn gắn nhạc trending → phần lớn
  không tải được. Đây là giới hạn của Meta.
- Nhạc trending được cấp phép để phát **trên Instagram**. Mang về host trên web
  thương mại của tiệm là chuyện khác.
- File video nặng; commit vào git sẽ phình kho rất nhanh và làm chậm mọi lần dựng.

Cách làm thay thế: ảnh bìa lưu trên vessca.com (có giá SEO), video phát bằng
link `permalink` về Instagram — đúng chỗ nhạc được cấp phép, và kéo thêm người
theo dõi về kênh.

## Còn phải làm sau khi tải ảnh

1. **Viết `alt` tiếng Việt cho từng ảnh.** Trường `alt` trong `_index.json` để
   rỗng sau khi tải. Đây chính là phần mang giá trị SEO — chú thích IG thường
   nhiều emoji, không dùng làm `alt` được. Phải xem từng ảnh rồi tả đúng thứ
   trong ảnh, có từ khoá chính, đọc lên tự nhiên.
2. **Tỉ lệ ảnh.** Bìa reels là dọc 9:16, ảnh IG thường vuông, còn ảnh bìa blog
   cần **ngang**. Muốn dùng làm ảnh bìa blog thì phải cắt lại.
3. **Tự động hoá.** Khi script đã chạy đúng bằng tay, chuyển logic vào
   `functions/_lib/` để cron Cloudflare (4 lượt/ngày) tự lấy ảnh mới.
   Token hạn 60 ngày nhưng cron chạy hằng ngày nên cho nó tự gia hạn
   (`refresh_access_token`) và lưu token mới vào D1 — chủ tiệm không phải chạm nữa.
   Lưu ý gói miễn phí giới hạn ~50 lần gọi ra ngoài mỗi lượt, nên giới hạn số
   ảnh mỗi lượt và gộp vào MỘT commit, giống `anh-blog.js` đang làm.
