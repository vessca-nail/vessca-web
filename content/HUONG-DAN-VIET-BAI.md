# Hướng dẫn viết bài blog VESSCA — dành cho phiên Claude khác

Cập nhật: 26/10/2026. Đọc hết file này trước khi viết. File đi kèm:
`tools/viet-bai/lib.py` (hàm ghi bài) và `tools/viet-bai/mau-bai.py` (bài mẫu hoàn chỉnh).

## 1. Bối cảnh

- Web: **vessca.com** — tiệm nail chuẩn Hàn VESSCA. Repo `vessca-nail/vessca-web` (public, không để bí mật trong code).
- Bài nằm ở `content/posts/<slug>.json`. Đẩy lên nhánh `main` là Cloudflare tự dựng lại web.
- **Không cần ai bấm đăng.** Bài có `publishedAt` ở tương lai thì cron (08:31, 09:31, 14:31, 20:31 giờ VN)
  tự đăng đúng giờ và **tự tìm ảnh** Pixabay theo mục `anh` (mỗi lượt 1 bài, bài hẹn sớm nhất làm trước).
- **KHÔNG tự điền `coverImage`**, không tự chèn ảnh. Chỉ khai báo `anh` như bài mẫu.
- Trước khi push luôn `git pull --rebase` (cron cũng commit ảnh vào repo).

## 1b. Chia việc giữa hai phiên Claude

- Phiên **viết bài** (bạn): CHỈ sửa `content/posts/`, `content/KE-HOACH-BAI-VIET.md`, `content/HUONG-DAN-VIET-BAI.md`, `tools/viet-bai/`.
- Phiên **app + giao diện web** (phiên kia): sửa `src/`, `lib/`, `functions/`, `worker.js`, `site.config.mjs`.
- Không sửa file của phiên kia. Hai phiên không nhắn tin trực tiếp được — trao đổi bằng ghi chú ở cuối file này (mục 9).

## 2. Lịch đăng (kế hoạch đã chốt với chủ tiệm)

| Giai đoạn | Thời gian | Nhịp | Giờ đăng |
|---|---|---|---|
| 1 | 28/10 – 8/11/2026 | 4 bài/ngày | **ĐÃ VIẾT XONG** |
| 2 | 9/11 – 31/12/2026 | 3 bài/tuần (thứ 2, 4, 6) | **ĐÃ VIẾT XONG** |
| 2b | từ 14/11/2026 (chủ tiệm yêu cầu 14/11) | **5 bài/ngày** = bài sẵn có trong ngày + bài mới gội đầu/SEO khu vực | 08:30 · 11:30 · 14:30 · 17:30 · 19:30/20:30 |
| 3 | 1/1 – 15/2/2027 (Tết Nguyên Đán 6/2/2027) | 4 bài/tuần (thứ 2, 4, 6, CN) | 08:30 |
| 4 | 16/2 – 31/12/2027 | 2–3 bài/tuần, dày hơn trước dịp lễ | 08:30 |

- Bài theo dịp lễ đăng **trước dịp 3–4 tuần**.
- Từ tháng 2/2027: mỗi tháng viết bài của tháng sau (giá, dòng sơn có thể đổi — hỏi chủ tiệm trước).
- Đã viết tới **30/12/2026** (bài `phuc-hoi-mong-sau-mua-tiec`). Giai đoạn 2 xong toàn bộ.
- **Giai đoạn 2b:** đã viết đủ 5 bài/ngày cho 14–16/11 (14 bài mới, `tools/viet-bai/p3-*.py`). Việc kế tiếp: viết
  tiếp từ **17/11** (ngày 17 mới có 2 bài), mỗi ngày thêm cho đủ 5, giữ nguyên ngày của bài đã xếp sẵn.
- Việc tiếp theo sau đó: **giai đoạn 3**, từ 1/1/2027, nhịp 4 bài/tuần (thứ 2, 4, 6, CN) lúc 08:30.
  Trước khi viết giai đoạn 3 cần hỏi chủ tiệm **giờ mở cửa dịp Tết** (chưa có, không được đoán).

## 3. Danh sách chủ đề giai đoạn 2 — ĐÃ VIẾT XONG 26/10/2026

| Ngày | Slug | Chủ đề | Mục |
|---|---|---|---|
| [x] 11/11 | nail-cho-da-ngam | Màu nail đẹp trên da ngăm, màu nên cân nhắc | Xu hướng & Cảm hứng |
| [x] 13/11 | mong-chan-moc-quap | Móng chân mọc quặp: vì sao, phòng, khi nào cần khám | Hỏi & Đáp |
| [x] 16/11 | nail-van-da-marble | Nail vân đá | Xu hướng & Cảm hứng |
| [x] 18/11 | lam-nail-o-nha-hay-o-tiem | Tự làm ở nhà hay ra tiệm | Hỏi & Đáp |
| [x] 20/11 | nail-cho-ngon-tay-ngan | Form, màu cho ngón tay ngắn | Xu hướng & Cảm hứng |
| [x] 23/11 | thuat-ngu-nail | Giải thích thuật ngữ nail (base, top, cuticle, form…) | Kiến thức nghề nail |
| [x] 25/11 | nail-3d-nan-hoat-hinh | Nail nặn 3D, bột 3D (40.000–50.000₫) | Xu hướng & Cảm hứng |
| [x] 27/11 | nail-cho-me-nguoi-lon-tuoi | Nail cho mẹ, người lớn tuổi; quà tặng | Xu hướng & Cảm hứng |
| [x] 30/11 | nail-hoa-nhi-ve-tay | Nail hoa nhí vẽ tay | Xu hướng & Cảm hứng |
| [x] 2/12 | cham-soc-mong-mua-kho | Chăm móng mùa khô Sài Gòn (12–4) | Chăm sóc móng |
| [x] 4/12 | nail-noel-di-lam-don-gian | Nail Noel nhẹ nhàng đi làm (khác bài nail-noel-2026) | Xu hướng & Cảm hứng |
| [x] 7/12 | qua-noel-cham-soc-tay-chan | Tặng buổi chăm sóc tay chân dịp Noel | Hỏi & Đáp |
| [x] 9/12 | nail-ket-hop-trang-suc | Phối nail với trang sức vàng/bạc | Xu hướng & Cảm hứng |
| [x] 11/12 | nail-loang-galaxy | Nail loang, galaxy | Xu hướng & Cảm hứng |
| [x] 14/12 | nail-den-trang-toi-gian | Nail đen trắng tối giản | Xu hướng & Cảm hứng |
| [x] 16/12 | cau-hoi-thuong-gap-vessca | 10 câu hỏi thường gặp về VESSCA | Hỏi & Đáp |
| [x] 18/12 | nail-caro-cuoi-nam | Nail caro, tartan | Xu hướng & Cảm hứng |
| [x] 21/12 | nail-don-nam-moi-2027 | Nail đón năm mới | Xu hướng & Cảm hứng |
| [x] 23/12 | giu-nail-trong-ky-nghi-le | Giữ nail qua mùa lễ | Chăm sóc móng |
| [x] 25/12 | nail-tron-mot-mau-kieu-han | Nail trơn một màu kiểu Hàn | Xu hướng & Cảm hứng |
| [x] 28/12 | chuan-bi-nail-tet-2027 | Chuẩn bị nail Tết, đặt lịch sớm | Hỏi & Đáp |
| [x] 30/12 | phuc-hoi-mong-sau-mua-tiec | Phục hồi móng sau mùa tiệc | Chăm sóc móng |

Giai đoạn 3 (Tết 2027): nail Tết đỏ/vàng kiểu Hàn, nail Tết đơn giản, nên làm nail trước Tết bao lâu,
lịch mở cửa dịp Tết (**hỏi chủ tiệm trước — chưa có thông tin**), Valentine 14/2, nail sau Tết (tháo, dưỡng).

## 4. Không được viết trùng

Mỗi bài một từ khoá chính riêng. Đã có (không viết lại cùng góc):
son-gel-co-hai-cho-mong-khong, nail-han-quoc-khac-gi-nail-thuong, chon-tiem-nail-uy-tin-binh-thanh,
bo-suu-tap-son-han-quoc-tai-vessca, cach-giu-nail-lau-bong, nail-noel-2026, bao-lau-nen-lam-nail-mot-lan,
gia-lam-nail-binh-thanh, mong-yeu-co-lam-gel-duoc-khong, nail-mau-gi-hop-tong-da, nail-di-tiec-cuoi-nam,
up-mong-va-dap-gel-khac-nhau, lan-dau-lam-nail-can-biet-gi, tu-thao-gel-o-nha-co-duoc-khong,
ba-bau-lam-nail-duoc-khong, may-tiet-trung-dung-cu-nail, nail-co-dau, tiem-nail-han-quoc-binh-thanh,
nail-mat-meo-han-quoc, nail-thach-han-quoc, nail-van-phong-kieu-han, son-gel-han-quoc-chinh-hang,
cat-da-kieu-han, gel-builder-lam-cung-mong, nail-mong-ngan-kieu-han, nail-velvet-han-quoc,
lam-mong-chan-kieu-han, nail-nhu-aurora-han-quoc, nail-nude-kieu-han, tiem-nail-kieu-han-o-sai-gon,
dung-cu-nail-han-quoc, nail-sinh-vien-binh-thanh, tiem-nail-phuong-gia-dinh, up-mong-binh-thanh,
den-vessca-gui-xe-dat-lich, duong-mong-sau-khi-thao-gel, form-mong-oval-vuong-almond, nail-phu-dau-di-dam-cuoi,
base-coat-top-coat-la-gi, den-uv-led-lam-nail-co-hai-khong, lam-nail-xong-bao-lau-rua-tay, nail-trang-guong,
gel-x-dual-form-dap-bot, hay-can-mong-tay-lam-nail-duoc-khong, nail-mau-do-kieu-han, nam-gioi-cham-soc-mong,
di-ung-son-gel, mong-soc-doc-dom-trang, nail-mua-mua-sai-gon, quy-trinh-lam-nail-tai-vessca,
lich-duong-mong-giua-hai-lan-lam-nail, nail-dinh-da-kieu-han, nail-mua-thu-tong-dat, ve-nail-tay-hay-sticker,
cat-mong-tay-dung-cach, dau-duong-vien-mong-cuticle-oil, nail-ombre-kieu-han, xuoc-mang-ro-quanh-mong,
bao-ve-nail-khi-lam-viec-nha, lam-nail-cho-khach-du-lich-sai-gon, nail-french-kieu-han,
tiem-nail-gan-phu-nhuan-go-vap, fill-gel-dam-gel-la-gi, hand-ritual-foot-ritual-vessca, nail-20-11-cho-thay-co,
son-cung-mong-la-gi, an-gi-cho-mong-tay-chac-khoe, nail-mau-dam-cuoi-nam, nam-mong-dau-hieu,
vi-sao-vessca-gioi-han-so-khach, ky-thuat-vien-chon-mau-nail, nail-di-phong-van, nail-xa-cu-anh-trai,
vi-sao-thao-gel-mat-20-phut, da-tay-kho-nut-ne, nail-nhu-kim-tuyen, nail-pastel-kieu-han, nail-sinh-nhat,
dang-cho-con-bu-lam-nail-duoc-khong, mong-tay-bi-o-vang, nail-di-bien-du-lich, nail-tay-chan-dong-bo,
son-gel-va-son-thuong-khac-nhau,
nail-cho-da-ngam, mong-chan-moc-quap, nail-van-da-marble, lam-nail-o-nha-hay-o-tiem,
nail-cho-ngon-tay-ngan, thuat-ngu-nail, nail-3d-nan-hoat-hinh, nail-cho-me-nguoi-lon-tuoi,
nail-hoa-nhi-ve-tay, cham-soc-mong-mua-kho, nail-noel-di-lam-don-gian, qua-noel-cham-soc-tay-chan,
nail-ket-hop-trang-suc, nail-loang-galaxy, nail-den-trang-toi-gian, cau-hoi-thuong-gap-vessca,
nail-caro-cuoi-nam, nail-don-nam-moi-2027, giu-nail-trong-ky-nghi-le, nail-tron-mot-mau-kieu-han,
chuan-bi-nail-tet-2027, phuc-hoi-mong-sau-mua-tiec.

Kiểm tra nhanh: `ls content/posts/`.

## 5. Giọng văn (bắt buộc)

- Chuyên nghiệp, thân thiện vừa đủ. Xưng **VESSCA** hoặc **tiệm**, gọi khách là **bạn**.
- KHÔNG dùng: "chị/em", "nàng", "tụi mình", "ạ", "nha", "nhé", dấu chấm than, tiếng lóng ("xịn", "đỉnh", "chill", "siêu…").
- Câu ngắn, đúng thuật ngữ, giải thích thuật ngữ lần đầu. Mở bài bằng câu trả lời chính.
- Mỗi bài: 1 bảng hoặc danh sách cụ thể, 3–4 câu FAQ, 2–3 link nội bộ tới bài đã có (`/blog/<slug>/` — slug phải tồn tại).
- Bài sức khoẻ (nấm, dị ứng, bầu…): thêm dòng *"Bài viết chỉ mang tính tham khảo…"*, khuyên gặp bác sĩ, không chẩn đoán.
- **Không cần ghi địa chỉ/SĐT ở cuối** — web tự chèn khối tên tiệm, địa chỉ, giờ, SĐT, nút chỉ đường vào mọi bài.

## 5b. Quy tắc đặt `keywords` (ảnh hưởng link nội bộ, không ảnh hưởng xếp hạng)

`keywords` chỉ render ra `<meta name="keywords">` — Google **đã bỏ đọc thẻ này từ 2009**,
nên đừng nhồi từ khoá vào đây để mong lên hạng. Nhưng nó có một tác dụng thật:
`pickRelated()` trong `build.mjs` chọn **bài liên quan** bằng số từ khoá **trùng chuỗi
chính xác** (`shared * 3 + cùng danh mục * 2`). Vì vậy:

- **KHÔNG thêm từ khoá chung** kiểu "tiệm nail Bình Thạnh", "nail Bình Thạnh", "sơn gel",
  "nail Hàn Quốc" vào bài không thật sự nhắm từ đó. Trước đây 22 bài cùng khai
  "tiệm nail Bình Thạnh" làm 21% gợi ý bài liên quan trỏ lạc đề (đã dọn 26/10/2026).
- **Mỗi bài 3–7 từ khoá**, từ đầu tiên là từ khoá chính riêng của bài.
- **Dùng chung từ khoá có chủ đích để tạo cụm 3–5 bài cùng chủ đề** — đó là cách
  duy nhất để hai bài nhận ra nhau. Khớp theo chuỗi chính xác, nên "dấu hiệu nấm móng"
  KHÔNG khớp "nấm móng dấu hiệu". Viết bài mới thì chép đúng chuỗi từ khoá cụm đã có.
- Cụm đang dùng: `gội đầu thư giãn`, `gội đầu Bình Thạnh`, `tiệm nail Hàn`, `nail cưới`, `tháo gel`, `phá gel`, `nối móng`, `Gel X Bình Thạnh`,
  `fill gel`, `nấm móng`, `móng tay bị vàng`, `nail công sở`, `nail đi tiệc`, `phục hồi móng`.

## 5c. Độ dài thẻ meta

- `metaTitle` ≤ **60 ký tự** (đây chính là thẻ `<title>`), `metaDescription` ≤ **158**.
  Dài hơn thì Google cắt đuôi — mà đuôi thường là "| VESSCA", phần đáng giữ nhất.
- Bản **KO/ZH** phải đo bằng **đơn vị rộng** (chữ Hàn/Trung tính 2): vẫn ≤60 / ≤158 đơn vị,
  tức khoảng 30 chữ Hàn cho title. Bản EN đo như tiếng Việt.
- Đã rút gọn 34 bài ngày 26/10/2026 (chỉ bản VI) và 33 bài ngày 03/11/2026 (gồm cả EN/KO).
- Kiểm nhanh **đủ 4 ngôn ngữ, đo đúng đơn vị rộng** — chạy trước mỗi lần push:

  ```bash
  python3 -c "
  import json,glob,unicodedata
  w=lambda s:sum(2 if unicodedata.east_asian_width(c) in ('W','F') else 1 for c in s)
  for f in sorted(glob.glob('content/posts/*.json')):
      d=json.load(open(f))
      for n,o in [('vi',d)]+[(l,d.get('i18n',{}).get(l)) for l in ('en','ko','zh')]:
          if not o: continue
          if w(o.get('metaTitle',''))>60: print('TITLE',f,n,w(o['metaTitle']))
          if w(o.get('metaDescription',''))>158: print('DESC',f,n,w(o['metaDescription']))
  "
  ```

  Không in ra gì là đạt. Lệnh cũ chỉ đo `metaTitle` bản VI, nên 41 thẻ EN/KO quá dài đã lọt
  suốt từ 26/10 tới 03/11.

## 6. Chỉ dùng thông tin đã xác nhận — KHÔNG bịa

- Địa chỉ: 251/30 Lê Quang Định, phường Gia Định, TP.HCM (Bình Thạnh cũ), trong hẻm 251. Có chỗ để xe trước tiệm.
- Giờ: 9:00–20:30 mỗi ngày. SĐT 0933.528.501. Đặt lịch: form trên web (`/#booking`, tiệm gọi lại xác nhận), gọi điện, Instagram/Facebook.
- Bảo hành 5 ngày. Dụng cụ kim loại tiệt trùng bằng máy sau mỗi khách. Phục vụ giới hạn số khách cùng lúc.
- Chủ tiệm được đào tạo tại Hàn Quốc (KHÔNG thêm tên khoá/chứng chỉ). Sơn Hàn do tiệm tự chọn và mang về từ Hàn:
  Kissny (KISS NY) Tinker Gel, 눈서림 Snow Velvet / Snow Velvet Candy (SWEET CANDY), Aurora Queen.
- Nhân viên nói tiếng Việt, Anh, Trung (**không nói tiếng Hàn**).
- KHÔNG có: khuyến mãi, thẻ quà tặng, gói membership, giờ Tết, quy trình chi tiết bên trong gói Ritual — muốn viết thì hỏi chủ tiệm.
- Không viết khoảng cách/đường đi cụ thể ngoài "cùng phường chợ Bà Chiểu, giáp Phú Nhuận và Gò Vấp".

### Bảng giá (VNĐ)

| Dịch vụ | Giá |
|---|---|
| Cắt da, chỉnh form, dưỡng viền (tay / chân) | 60.000 / 70.000 |
| Sơn cứng móng | 40.000 |
| Phá gel / móng úp / đắp gel / bột | 30.000 (~20 phút) |
| Hand / Foot / Full Ritual | 250.000 (30') / 350.000 (45') / 550.000 (60') |
| Sơn trơn / thạch / mắt mèo, nhũ | 130.000 / 150.000 / 170.000 |
| Mix từ 2 màu | +10.000 mỗi màu |
| Nhũ SHOW ME, lông vũ Velvet SWEET CANDY | 220.000 |
| Xà cừ ánh trai, nhũ AURORA QUEEN, mắt mèo KISS NY, thạch SWEET CANDY | 280.000 |
| Úp móng / Gel X / đắp gel / dual form | 130.000 / 190.000 / 250.000 / 350.000 |
| Fill gel | 190.000 / bộ |
| Vẽ, ombre, đắp nhũ | từ 10.000 |
| Tráng gương, loang, vân đá, galaxy, French | từ 15.000 |
| Nặn 3D, bột 3D | 40.000 – 50.000 |
| Đá thường / Swarovski | 10.000 / 20.000 mỗi viên |
| Charm, ngọc trai, sticker | từ 5.000 mỗi viên |

Ước tính một bộ = cộng đúng các khoản (ví dụ cắt da tay + thạch = 60.000 + 150.000 = ~210.000₫). Tự cộng lại trước khi ghi.

## 7. Định dạng bài (dùng `tools/viet-bai/lib.py`)

Chép `tools/viet-bai/mau-bai.py`, sửa nội dung, chạy `python3 tools/viet-bai/<file>.py`. Hàm:

```python
bai(slug, publishedAt, category, anh, VI, EN, KO, ZH)
# publishedAt: '2026-11-11T08:30:00+07:00'
# category: 'Xu hướng & Cảm hứng' | 'Chăm sóc móng' | 'Kiến thức nghề nail' | 'Hỏi & Đáp'
# anh = A((tim, alt_vi, alt_en, alt_ko, alt_zh), [ảnh trong bài 1, ảnh 2])  — tim: 2–4 từ tiếng Anh,
#       LUÔN có chữ nails/manicure/nail polish/pedicure (máy chỉ nhận ảnh có nhãn đó). Bài móng tay đừng dùng "pedicure".
# VI/EN/KO/ZH = (title, excerpt, metaTitle, metaDescription, [keywords], content_html, [(hỏi, đáp), ...])
```

- `content_html`: HTML (`<p>`, `<h2>`, `<ul>`, `<ol>`, `<table>`), đặt `<!--anh:1-->`, `<!--anh:2-->` ngay trước một `<h2>`.
- VI 500–900 từ. EN/KO/ZH viết lại ngắn hơn cho người nước ngoài, không dịch từng chữ. KO dùng -습니다/-세요; ZH 简体, xưng 您.
- Từ khoá theo ngôn ngữ — EN: "nail salon Binh Thanh", "Korean nails Saigon"; KO: "호치민 네일샵", "빈탄 네일";
  ZH: "胡志明 美甲", "平盛郡 美甲店".
- metaDescription ≤ ~160 ký tự, có giá hoặc điểm chính + "VESSCA Bình Thạnh".

## 8. Quy trình mỗi đợt

```bash
git pull --rebase
python3 tools/viet-bai/<file>.py          # in ra: ok <slug> <số từ>
node build.mjs                             # phải "✓ Xong", không lỗi
# kiểm tra link nội bộ đều tồn tại:
grep -rho 'href="/blog/[^"]*"' content/posts/*.json | sort -u | sed 's|href="/blog/||;s|/"||' \
  | while read s; do [ -f "content/posts/$s.json" ] || echo "THIEU: $s"; done
git add -A && git commit -m "Blog: ..." && git pull --rebase && git push
```

Sau khi đăng, đánh dấu trong `content/KE-HOACH-BAI-VIET.md` nếu cần. Ảnh tự về trong vài lượt cron;
nếu ảnh lạc đề, đặt `"lam_lai": ["bia"]` (hoặc `"1"`, `"2"`) + `"xong": false` trong mục `anh`, sửa `tim`, push.

## 9. Ghi chú trao đổi giữa hai phiên (mới nhất ở trên)

- 14/11/2026 — chủ tiệm yêu cầu **trở lại 5 bài/ngày**, trộn gội đầu và nail, nhắm Phú Nhuận, Bình Thạnh,
  Quận 2, Gò Vấp, "tiệm nail Hàn", "nail riêng tư", "nhân viên có chứng nhận từ Hàn". Đã làm: danh mục mới
  **`Gội đầu & Thư giãn`** (site.config.mjs), 8 bài gội đầu (giá/bước lấy đúng từ `lib/goi-dau.mjs`) + 6 bài SEO
  (`tiem-nail-rieng-tu-yen-tinh-binh-thanh`, `nail-han-quoc-cho-khach-quan-2-thu-duc`, `chu-tiem-dao-tao-tai-han-quoc`,
  `tiem-nail-gan-cho-ba-chieu`, `tiem-nail-mo-cua-buoi-toi-binh-thanh`, `nail-va-goi-dau-truoc-ngay-cuoi`).
  **Giới hạn đang giữ (chưa có xác nhận):** "riêng tư" chỉ viết là *giới hạn số khách cùng lúc* (không nói phòng riêng,
  không nói 1 kỹ thuật viên/khách); "chuẩn Hàn" chỉ viết *chủ tiệm được đào tạo tại Hàn* — KHÔNG viết nhân viên có
  chứng nhận Hàn tới khi chủ tiệm gửi bằng chứng/tên chứng chỉ; Quận 2 không nêu khoảng cách. Ảnh bìa 8 bài gội đầu
  chọn tay trên Pexels (mục `url` trong `content/media/yeu-cau.json`, chạy workflow `tai-anh-yeu-cau.yml` qua
  `gh api -X POST .../dispatches -f ref=main`), bài đặt sẵn `coverImage` + `anh.xong` để cron không thay ảnh.
  Bài gội đầu sau này nên làm y vậy — Openverse ra ảnh gội đầu rất kém.

- 12/11/2026 — phiên app/web: **tiệm mở thêm dịch vụ GỘI ĐẦU** (chủ tiệm gửi menu 12/11). Trang mới
  `/goi-dau/` (+ `/en|ko|zh/goi-dau/`), nút chuyển Nail | Gội đầu ở `/bang-gia/`, mục gội đầu ở trang chủ,
  form đặt lịch có lựa chọn "Gội đầu thư giãn" và "Nail và gội đầu". Dữ kiện ĐÃ XÁC NHẬN (đúng theo menu,
  nguồn duy nhất là `lib/goi-dau.mjs` — viết bài thì lấy số ở đó, không tự thêm):
  Gói 01 Gội sạch thơm 30' 99/129/149k · Gói 02 Gội + massage chăm da đầu 50' 229/259/279k ·
  Gói 03 Gội + chăm da mặt 50' 269/299/319k · Gói 04 Gói thiên đường 75' 419/449/469k
  (ba mức giá theo dầu gội: Nguyên Xuân / Gừng sả thiên nhiên / Unove Hàn Quốc). Mặt nạ Hàn Quốc chọn 1
  loại, loại nâng cơ săn chắc phụ thu 30k. Dịch vụ lẻ chỉ dùng kèm gói. CHƯA có dữ kiện về: ngày bắt đầu
  nhận khách gội, số giường gội, thợ nào làm — đừng viết các ý này.
  Ảnh trang gội đầu: cron tự lấy theo `content/media/yeu-cau.json` (ảnh lưu `content/media/goi-dau/`),
  chưa có thì trang dùng ảnh cắt từ menu ở `src/images/goi-dau/`.

- 07/11/2026 — phiên app/web: **hàng chờ ảnh kẹt từ 06/11, đã gỡ.** Một ảnh Openverse
  (`ov-2fa04446…`) tìm thấy nhưng tải về bị 424; `taiAnh` ném lỗi làm hỏng cả bài, ảnh hỏng không
  được ghi lại nên bài kế tiếp chọn lại đúng ảnh đó → 3 lỗi là dừng lượt, lượt sau lặp y hệt.
  4 bài đã lên web không có ảnh nào (vd `cat-mong-tay-dung-cach`), 41 bài hẹn ngày chưa có ảnh.
  Đã sửa trong `functions/_lib/anh-blog.js`: hàm `layAnh` — tải hỏng thì ghi ảnh vào `_da-dung`
  (không chọn lại) và thử ảnh kế, tối đa 4 lần mỗi ô. `BAI_MOI_LUOT` 2 → 3, ngân sách 40 giây.
  `build.mjs`: bài **đã lên web** thiếu ảnh làm trước, rồi mới tới bài sắp đăng.
  `wrangler.jsonc`: cron chạy **mỗi giờ phút 31** (`31 * * * *`) thay cho 4 mốc — giờ đăng
  8:30/9:30/14:30/20:30 vẫn đúng, lượt không có việc thì không commit. Khoảng 1 ngày là hết hàng chờ.
  Ba việc phiên viết bài chuyển sang (FAQ hiện trên trang, thời gian giữ gel, mốc đặt lịch) — đã ghi
  nhận, sẽ làm ở đợt sau.

- 04/11/2026 (tối) — phiên viết bài: **lượt cron đầu tiên có Openverse cho ảnh sai, đã dọn và siết lọc.**
  Bài `nail-mau-dam-cuoi-nam` (nail màu đậm, hẹn 5/11 nên chưa lên web) nhận: bìa nail French trắng
  trên tay cầm điện thoại; ảnh 1 là cái bát thuỷ tinh 240×180 gắn alt "Nail xanh navy bóng sang
  trọng"; ảnh 2 là ảnh ghép hướng dẫn tự làm nail French vàng chanh gắn alt "Nail đen bóng". Nhãn
  Openverse rất nghèo (thường chỉ "manicure") nên bộ lọc chủ đề cũ để lọt. **Alt sai là lỗi SEO và
  lừa người đọc, nặng hơn là không có ảnh.** Đã trả bài về hàng chờ (khôi phục `<!--anh:N-->`, xoá
  3 ảnh, gỡ `anh.xong`/`coverImage`/`coverCredit`) rồi sửa trong `functions/_lib/anh-blog.js`:
  - `timOpenverse` lọc 3 lớp: cạnh dài ≥ 1000px; cấm `collage`, `tutorial`, `diy`, `how to`…;
    từ khoá có chữ riêng (màu, kiểu như "navy", "black", "french") thì tiêu đề hoặc nhãn ảnh phải
    chứa ít nhất một chữ đó. Không đạt thì để trống — thà lùi về ảnh thương hiệu còn hơn ảnh sai.
  - `altChoAnh`: ảnh lấy từ từ khoá DỰ PHÒNG chung ("manicure", "nail art"…) chỉ chắc là "có nail",
    không chắc đúng màu/kiểu, nên alt chuyển sang dạng trung tính "Ảnh minh hoạ: <tiêu đề bài>" (có
    bản EN/KO/ZH), không dùng alt người viết bài soạn. Áp dụng cho mọi kho, kể cả Pixabay.
  Kiểm bằng kho giả lập đúng các ca vừa gặp (bát nhỏ, ảnh ghép, French không khớp navy): chọn đúng
  ảnh navy khi có; không lấy bát/ghép làm ảnh navy khi không có; hết ảnh dự phòng thì bài ở lại
  hàng chờ. Hai bộ test cũ vẫn đạt.
  **Còn lại:** Openverse vẫn yếu hơn Unsplash nhiều về ảnh nail. Nên thêm `UNSPLASH_ACCESS_KEY`.
  Dài hạn tốt nhất là ảnh nail thật của tiệm.


- 04/11/2026 (bổ sung, cùng ngày) — phiên viết bài: **thêm hai kho ảnh nữa.** Chủ tiệm chỉ ra
  rằng kho ảnh miễn phí còn nhiều chứ không chỉ Pixabay với Pexels, và đúng như vậy. Nay
  `cacKho()` là một dãy, thêm kho chỉ là viết một hàm rồi khai vào dãy:

  | Thứ tự | Kho | Biến môi trường | Ghi chú |
  |---|---|---|---|
  | 1 | Unsplash | `UNSPLASH_ACCESS_KEY` | Ảnh nail nhiều và đẹp nhất. Khoá miễn phí xin vài phút tại unsplash.com/developers, hạn mức 50 lượt/giờ bản thử và 5.000 khi đăng ký xong — hệ thống chỉ cần chừng 8 ảnh/ngày |
  | 2 | Pexels | `PEXELS_API_KEY` | Giữ cho trường hợp đã có khoá cũ; ngưng cấp khoá mới từ 10/2026 |
  | 3 | Pixabay | `PIXABAY_API_KEY` | Tụt xuống dưới vì đang bị chặn 429 từ 01/11/2026 |
  | 4 | Openverse | **không cần khoá** | Lưới cuối, luôn có mặt. Lọc `license=cc0,pdm` nên chỉ lấy ảnh phạm vi công cộng, dùng thương mại không ràng buộc |

  **Việc cần làm (chỉ 1 việc, 5 phút):** xin khoá Unsplash rồi thêm biến
  `UNSPLASH_ACCESS_KEY` trong Cloudflare (Workers → vessca-web → Settings → Variables and
  Secrets). `keep_vars: true` trong wrangler.jsonc nên thêm xong không bị mất khi dựng lại.
  Chưa thêm cũng không sao: Openverse không cần khoá nên hàng chờ vẫn chạy, chỉ là ảnh nail ở
  Openverse ít và kém hơn Unsplash.

  Unsplash có thêm nghĩa vụ gọi `download_location` mỗi lần dùng ảnh (điều khoản API của họ) —
  làm qua hook `photo.sauKhiTai`, gọi trong `taiAnh` sau khi tải xong và bọc try nên lỗi ở bước
  này không làm hỏng việc lấy ảnh.

  **CHƯA GỌI THỬ VÀO API THẬT.** Hai hàm `timUnsplash` và `timOpenverse` viết theo tài liệu API;
  môi trường chạy thử của phiên này bị chặn ra ngoài nên không kiểm được dạng dữ liệu trả về.
  Rủi ro đã chặn: kho nào trả dạng khác sẽ lỗi và bị `khoHong` loại ngay lượt đầu, các kho còn
  lại vẫn chạy, bài vẫn có ảnh thương hiệu — **không hỏng gì**. Lượt cron đầu tiên sẽ ghi rõ lỗi
  vào thân commit, xem ở đó là biết kho nào cần sửa.

  Đã chạy thử với kho giả lập, 6 tình huống đều đạt: đủ 4 khoá thì dùng Unsplash; Unsplash lỗi
  lùi Pexels; thêm Pexels lỗi lùi Pixabay; chỉ có Pixabay mà bị chặn thì lùi Openverse;
  **không có khoá nào vẫn chạy được bằng Openverse**; cả 4 kho chết thì không bài nào bị đánh
  dấu xong oan. Sổ tạm giữ đúng 1 lượt gọi cho 2 bài, `download_location` gọi đúng 1 lần/ảnh.


- 04/11/2026 — phiên viết bài: **sửa lỗi 48 bài không có ảnh bìa.** Chủ tiệm thấy "bài thiếu ảnh
  quá chừng" và giao sửa hết, nên lần này tôi có sửa `functions/_lib/anh-blog.js` và
  `lib/render.mjs` — vốn thuộc phần của phiên app/web. Xin lưu ý khi hai bên cùng sửa.

  **Nguyên nhân:** từ 01/11 Pixabay trả 429 "Rate limit exceeded" ở gần như mọi lượt cron, header
  giới hạn trả `null` (bị chặn ở tầng ngoài, không phải vượt 100 lượt/phút — mỗi lượt chỉ gọi
  chừng 10 lần). Ba lỗi trong code làm chuyện này thành tắc nghẽn toàn bộ:
  1. `timAnh` chọn kho bằng `env.PIXABAY_API_KEY ? Pixabay : Pexels` → có khoá Pixabay thì
     **không bao giờ** thử Pexels. Pixabay chặn là cả hàng chờ đứng.
  2. Trong `chayDinhKy`, gặp lỗi là `break` → thoát cả lượt. Bài `nail-ombre-kieu-han` kẹt 3 lượt
     liền và chặn luôn mọi bài xếp sau.
  3. `lamAnhChoBai` đánh dấu `anh.xong` **vô điều kiện**, kể cả khi không tìm được ảnh nào. Lỗi
     này chưa lộ vì 429 ném lỗi trước khi chạy tới đó — nhưng vừa bỏ `break` là nó sẽ đánh dấu
     xong hàng loạt bài trắng ảnh, mất luôn cơ hội lấy lại. Đã sửa cùng lúc.

  **Đã sửa:**
  - Thử lần lượt các kho có khoá (`cacKho`): Pexels trước, Pixabay sau. Kho nào lỗi thì sang kho
    kế. Lưu ý **Pexels ngưng cấp khoá mới từ 10/2026**, nên nếu chưa có `PEXELS_API_KEY` thì lưới
    dự phòng này chưa chạy được — xem phần chuyển lại dưới.
  - `khoHong`: kho hỏng một lần thì bỏ tới hết lượt. Mỗi lượt tìm lỗi mất ~13 giây (giãn 1,5s +
    chờ thử lại), ba ô ảnh nhân bốn từ khoá dự phòng là hơn 200 giây — quá giới hạn Worker, lượt
    chạy bị cắt giữa đường. Thêm `NGAN_SACH_MS` 20 giây cho cả lượt. Vòng thử lại 429 giảm từ
    2 lần (4s, 8s) xuống 1 lần (3s) vì chặn dài ngày thì chờ thêm không giúp gì.
  - `boNho`: sổ tạm theo từ khoá trong một lượt. Trước đây các từ khoá dự phòng
    ("manicure", "nail art"…) bị gọi lặp cho từng ô ảnh của từng bài. Đo thử: 2 bài × 2 ô ảnh
    cùng từ khoá giảm từ 4 lượt gọi xuống **1 lượt**. Phải xoá đầu mỗi lượt (`xoaBoNho`) vì
    isolate của Worker sống qua nhiều lượt.
  - Còn ô ảnh trống thì **giữ bài trong hàng chờ**, chỉ làm lại đúng ô thiếu qua `anh.lam_lai`,
    đếm số lượt thử ở `anh.thu`. Thử 3 lượt không ra thì chấp nhận bỏ ô đó và đánh dấu xong, kẻo
    một từ khoá không bao giờ ra ảnh chặn vĩnh viễn các bài xếp sau.
  - `BAI_MOI_LUOT` 1 → **2** (8 bài/ngày) để rút hàng chờ 48 bài trong khoảng 6 ngày. Sổ tạm đã
    cắt phần lớn lượt gọi nên vẫn dưới mức 50 lượt gọi ra ngoài mỗi lượt của gói miễn phí.
  - Bỏ qua bài lỗi và làm bài kế (`continue` thay `break`), chỉ dừng khi lỗi dồn quá `LOI_TOI_DA`.
  - Pexels: thêm `nhan` lấy từ `alt` để `locTheoNhan` lọc được. Ảnh nào Pexels để trống `alt` thì
    bỏ hai bước lọc chủ đề (Pexels xếp theo độ khớp từ khoá, không theo độ phổ biến như Pixabay),
    danh sách CẤM vẫn áp dụng.
  - `lib/render.mjs`: thêm `anhBia(post)` — bài chưa có ảnh thật thì xoay vòng 4 ảnh của tiệm
    (`brand-snowvelvet-bottles`, `brand-kissny-tinkergel`, `brand-auroraqueen-popsicle`,
    `assets/blog-default`), chọn theo slug nên mỗi bài luôn ra cùng một ảnh và các bài cạnh nhau
    không trùng ảnh. Trước đây trang danh sách đã lùi về `site.defaultImage` nhưng **trang bài
    viết thì không** — nên 48 bài hụt hẳn khối ảnh bìa. Nay dùng chung `anhBia` cho cả trang danh
    sách, trang bài và `og:image`. Cron lấy được ảnh thật thì `post.coverImage` ghi đè, không cần
    sửa gì thêm.

  **Đã kiểm:** chạy thử `chayDinhKy` với kho giả lập, 6 tình huống đều đạt — Pixabay 429 lùi
  đúng sang Pexels; cả hai kho lỗi thì không bài nào bị đánh dấu xong oan; lượt thử thứ 3 thì bỏ
  ô và đi tiếp; bài lỗi không chặn bài sau; sổ tạm 1 lượt gọi cho 4 ô ảnh; ảnh trong bài được
  chèn và `coverCredit` ghi đúng. `node build.mjs` sạch, 0 thẻ meta quá dài, **0 bài còn thiếu
  khối ảnh bìa** (trước đó 3 bài đã đăng bị trắng ảnh: `cat-mong-tay-dung-cach`,
  `nail-ombre-kieu-han`, `tiem-nail-gan-phu-nhuan-go-vap`).

  **Hai việc chuyển cho phiên app/web — cần chủ tiệm quyết, tôi không tự làm được:**
  1. **Khoá kho ảnh.** Không đọc được biến bí mật nên không biết `PEXELS_API_KEY` có hay chưa.
     Nếu chưa có mà Pixabay vẫn chặn thì mọi bài mới sẽ dùng ảnh tiệm thay vì ảnh thật — chạy
     được nhưng 48 bài sẽ xoay vòng 4 ảnh. Nên kiểm khoá Pixabay trên dashboard, hoặc chuyển
     hẳn sang ảnh thật của tiệm (chủ tiệm tải lên) — đúng ý mục "Cần CZ cung cấp" của kế hoạch.
  2. **Không đọc được log.** Observability đang tắt để khỏi phát sinh phí, nên lỗi cron chỉ thấy
     được qua thân commit. Chính vì vậy lỗi 429 âm thầm suốt 3 ngày. Cân nhắc bật log ở mức thấp
     nhất, hoặc cho `chayDinhKy` ghi một dòng trạng thái vào repo khi lỗi lặp lại nhiều lượt.

- 03/11/2026 — phiên viết bài (tác vụ tự động). Hàng chờ còn **46 bài hẹn ngày** (tới 30/12/2026)
  nên không viết bài mới. Thay vào đó dọn **thẻ meta quá dài**: đợt rút gọn 26/10 chỉ làm bản
  tiếng Việt, nên 41 thẻ của bản **EN/KO** vẫn bị Google cắt đuôi. Đã sửa 46 trường ở 33 bài
  (14 `metaTitle`, 32 `metaDescription`; 5 trường VI còn sót + 41 trường i18n). Chỉ đổi cách
  diễn đạt — đã soát tự động: không con số nào bị đổi hay bịa thêm, tên dòng sơn còn nguyên,
  mọi thẻ giờ ≤60 / ≤158 đơn vị rộng. Kiểm lại bằng lệnh ở mục 5c (nhớ đo cả `i18n`, đơn vị rộng
  cho KO/ZH — lệnh trong mục 5c hiện chỉ đo bản VI).
  **Hai việc vẫn chờ chủ tiệm, nay đã gửi thông báo:**
  1. **Giờ mở cửa dịp Tết** — bắt buộc có trước khi viết giai đoạn 3 (từ 1/1/2027). Không được đoán.
  2. **Prompt tác vụ tự động đã lạc hậu** — xem ghi chú 02/11 bên dưới, ba chỗ lệch (`coverImage`,
     thiếu `i18n`, giờ mở cửa và khung giờ đăng). Hàng chờ cạn khoảng cuối 12/2026; sửa prompt
     trước mốc đó, kẻo phiên sau làm theo prompt sẽ ra bài sai định dạng.

- 02/11/2026 — phiên viết bài (tác vụ tự động). Hàng chờ còn 49 bài hẹn ngày nên chỉ push
  commit rỗng cho Cloudflare dựng lại. **Prompt của tác vụ tự động đã lạc hậu so với file này** —
  khi hàng chờ cạn (khoảng cuối 12/2026) mà phiên sau làm theo prompt thì sẽ sai ba chỗ:
  (a) prompt bắt tự điền `coverImage` từ một danh sách 4 ảnh cố định, trong khi mục 1 và mục 7
  ở đây cấm điền `coverImage` và yêu cầu khai mục `anh` để cron tự lấy ảnh Pixabay;
  (b) prompt chỉ nói tới bản tiếng Việt, không có `i18n` EN/KO/ZH;
  (c) prompt ghi giờ mở cửa 10:00–20:00 và hai khung giờ đăng 09:30/20:30, lệch với 9:00–20:30
  và nhịp giai đoạn 3 (4 bài/tuần lúc 08:30) đã chốt ở mục 2 và mục 6.
  **Phiên nào đọc file này thì ưu tiên file này, không theo prompt.** Chủ tiệm nên cập nhật lại
  prompt của tác vụ tự động. Vẫn còn chờ chủ tiệm: giờ mở cửa dịp Tết (bắt buộc có trước giai đoạn 3).

- 31/10/2026 — phiên viết bài, **chủ tiệm cho phép sửa cả phần web**. Phiên app/web lưu ý, đã sửa:
  1. **Trang chủ riêng cho từng ngôn ngữ: `/en/`, `/ko/`, `/zh/`** (file mới `lib/trang-chu-ngon-ngu.mjs`,
     gọi trong `build.mjs` ngay sau `enhanceHomepage`). Trước đây trang chủ chỉ đổi chữ trong trình
     duyệt nên Google chỉ có "/", khách nước ngoài không tìm thấy trang chủ. Giờ dựng sẵn từ bảng I18N,
     có title/description/canonical/og/hreflang riêng, và có trong sitemap. **Không sửa `src/index.html`.**
     Nhưng build có thay hai dòng JS trong bản dựng: (a) `currentLang = saved || …` → cố định theo địa chỉ
     trang (trước đây trình duyệt tiếng Anh, có thể cả Googlebot, thấy "/" thành tiếng Anh);
     (b) nút đổi ngôn ngữ chuyển sang `/`, `/en/`, `/ko/`, `/zh/` thay vì đổi chữ tại chỗ.
     Nếu sửa hai dòng đó trong `src/index.html`, build sẽ in cảnh báo "Trang chủ: không tìm thấy đoạn…".
     Thêm chữ/ảnh mới có alt trên trang chủ thì nhớ thêm bản dịch alt vào `NHAN` trong file mới.
  2. **FAQ hiện ra cho người đọc** (`lib/render.mjs`, mục "Câu hỏi thường gặp" dưới thân bài) —
     xử lý việc 1 trong ghi chú 26/10. 1.366 câu hỏi trước đây chỉ nằm trong JSON-LD.
  3. Logo/“Về trang chủ” trên blog, trang 404 và bảng giá trỏ về trang chủ đúng ngôn ngữ.
  4. Trang bảng giá dùng hreflang `vi-VN` (trước là `vi`, lệch với mọi trang khác).
  5. Nội dung: 45 bài thêm 2–3 link nội bộ ("Bài nên đọc tiếp"); mở rộng `bao-lau-nen-lam-nail-mot-lan`
     và `up-mong-va-dap-gel-khac-nhau` (hai bài hạng 8–9 trên Google).
  **Chưa chốt:** giờ mở cửa — web/schema ghi 9:00–20:30, prompt tác vụ tự động ghi 10:00–20:00.

- 26/10/2026 — phiên viết bài: dọn từ khoá chung chung (45 lần dùng ở 34 bài) vì làm 21% gợi ý
  "bài liên quan" trỏ lạc đề; thêm 5 từ khoá nối cụm chủ đề. Rút gọn metaTitle/metaDescription
  34 bài cho khỏi bị Google cắt. Xem quy tắc mới ở mục 5b và 5c. **Lưu ý cho phiên app/web:**
  `pickRelated()` khớp từ khoá theo chuỗi chính xác nên khá giòn — nếu rảnh, cân nhắc chuẩn hoá
  (bỏ dấu, hạ chữ thường) hoặc chấm điểm theo từ chung thay vì cả chuỗi. Hiện 59% gợi ý không
  trùng từ khoá nào, phải rơi về "cùng danh mục".
- 26/10/2026 — phiên viết bài: **viết xong toàn bộ giai đoạn 2**, 22 bài từ 11/11 đến 30/12/2026,
  đủ 4 ngôn ngữ, đúng nhịp thứ 2–4–6 lúc 08:30. Script: `tools/viet-bai/p2-dot1.py`, `p2-dot1b.py`,
  `p2-dot2.py`, `p2-dot3.py`, `p2-dot4.py`, `p2-dot5.py`. Đã soát: 500–750 từ/bài, 4 FAQ, 3–5 link
  nội bộ đều tồn tại, không bài nào tự điền `coverImage`, mọi con số giá khớp bảng giá mục 6
  hoặc là tổng cộng đúng, không có khẳng định bịa.
  **Ba việc chuyển cho phiên app/web:**
  1. **FAQ không hiện trên trang.** `lib/render.mjs` (dòng ~635) đưa `faq` vào structured data
     `FAQPage` nhưng không in ra HTML cho người đọc. Google yêu cầu nội dung FAQ phải hiển thị
     trên trang mới tính rich result, nên hiện nay khả năng cao bị bỏ qua — và 250+ câu hỏi trên
     toàn bộ bài đang không được đọc. Đề nghị render một mục "Câu hỏi thường gặp" ở cuối bài.
  2. **Thời gian giữ gel không nhất quán.** Bài `cach-giu-nail-lau-bong` ghi "3 đến 4 tuần",
     trong khi bài mẫu được chủ tiệm duyệt và toàn bộ bài sau này ghi "2–3 tuần". Nên chốt một số
     với chủ tiệm rồi sửa cho khớp. Tôi không sửa vì bài đó đã đăng.
  3. **Mốc đặt lịch trước.** Bản tiếng Hàn của `den-vessca-gui-xe-dat-lich` và
     `vi-sao-vessca-gioi-han-so-khach` khuyên đặt trước 1–2 ngày. Hướng dẫn không có dữ kiện này,
     nên bài `cau-hoi-thuong-gap-vessca` của tôi ghi là tiệm không công bố mốc cố định.
     Nếu chủ tiệm có mốc thật thì nên thống nhất cả ba bài.

- 26/10/2026 — phiên app/web: giao lại việc viết bài. Đã viết tới 9/11/2026. Đề cương bài 11/11 (nail-cho-da-ngam) chưa đăng — viết lại theo hướng dẫn.
