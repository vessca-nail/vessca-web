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
| 3 | 1/1 – 15/2/2027 (Tết Nguyên Đán 6/2/2027) | 4 bài/tuần (thứ 2, 4, 6, CN) | 08:30 |
| 4 | 16/2 – 31/12/2027 | 2–3 bài/tuần, dày hơn trước dịp lễ | 08:30 |

- Bài theo dịp lễ đăng **trước dịp 3–4 tuần**.
- Từ tháng 2/2027: mỗi tháng viết bài của tháng sau (giá, dòng sơn có thể đổi — hỏi chủ tiệm trước).
- Đã viết tới **30/12/2026** (bài `phuc-hoi-mong-sau-mua-tiec`). Giai đoạn 2 xong toàn bộ.
- Việc tiếp theo: **giai đoạn 3**, từ 1/1/2027, nhịp 4 bài/tuần (thứ 2, 4, 6, CN) lúc 08:30.
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
