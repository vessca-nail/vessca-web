"""Đợt 14/11/2026 — cụm bài GỘI ĐẦU (1/2). Số liệu lấy đúng theo lib/goi-dau.mjs (menu chủ tiệm gửi 12/11).
Ngày đăng ở đây chỉ là tạm; tools/viet-bai/xep-lich.py xếp lại 5 bài/ngày."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *

CAT = 'Gội đầu & Thư giãn'
T = '2026-11-14T12:30:00+07:00'

# ---------- G1. Gội đầu thư giãn ở Bình Thạnh ----------
vi = '''<p>VESSCA ở phường Gia Định (Bình Thạnh cũ) nay có thêm dịch vụ gội đầu thư giãn, bên cạnh nail kiểu Hàn. Có bốn gói từ 30 đến 75 phút, giá từ 99.000₫ đến 469.000₫ tuỳ gói và loại dầu gội bạn chọn. Bài này tóm tắt từng gói để bạn chọn nhanh trước khi đặt lịch.</p>

<h2>Bốn gói gội đầu tại VESSCA</h2>

<table>
<thead><tr><th>Gói</th><th>Thời lượng</th><th>Nguyên Xuân</th><th>Gừng sả</th><th>Unove</th></tr></thead>
<tbody>
<tr><td>01 · Gội sạch thơm</td><td>30 phút</td><td>99.000₫</td><td>129.000₫</td><td>149.000₫</td></tr>
<tr><td>02 · Gội sạch thơm, massage chăm da đầu</td><td>50 phút</td><td>229.000₫</td><td>259.000₫</td><td>279.000₫</td></tr>
<tr><td>03 · Gội sạch thơm, chăm da mặt</td><td>50 phút</td><td>269.000₫</td><td>299.000₫</td><td>319.000₫</td></tr>
<tr><td>04 · Gói thiên đường</td><td>75 phút</td><td>419.000₫</td><td>449.000₫</td><td>469.000₫</td></tr>
</tbody>
</table>

<p>Mỗi gói có ba mức giá vì bạn được chọn một trong ba loại dầu gội xả: Nguyên Xuân, gừng sả thiên nhiên hoặc Unove Hàn Quốc. Menu đầy đủ kèm quy trình từng bước có ở trang <a href="/goi-dau/">menu gội đầu</a>.</p>

<h2>Mỗi gói gồm những gì</h2>

<ul>
<li><strong>Gói 01 (30 phút):</strong> tẩy trang, rửa mặt, gội hai lần, xả, sấy bằng máy sấy ion âm, dầu dưỡng tóc. Hợp ngày bận, cần gọn và sạch.</li>
<li><strong>Gói 02 (50 phút):</strong> thêm tẩy tế bào chết da đầu, đắp mặt nạ mắt, hai lần massage đầu thư giãn và dưỡng da tay.</li>
<li><strong>Gói 03 (50 phút):</strong> thêm tẩy tế bào chết da mặt, đắp mặt nạ Hàn Quốc, massage mặt và chiếu đèn ánh sáng sinh học.</li>
<li><strong>Gói 04 (75 phút):</strong> gộp chăm da đầu và da mặt, thêm massage đầu, cổ vai gáy.</li>
</ul>

<p>Cả bốn gói đều kết thúc bằng nước uống và bánh ngọt.</p>

<h2>Chọn gói theo nhu cầu</h2>

<table>
<thead><tr><th>Bạn cần</th><th>Gói nên xem</th></tr></thead>
<tbody>
<tr><td>Gội nhanh trước buổi hẹn</td><td>Gói 01</td></tr>
<tr><td>Da đầu nhanh bết, muốn được massage đầu</td><td>Gói 02</td></tr>
<tr><td>Muốn chăm da mặt cùng lúc</td><td>Gói 03</td></tr>
<tr><td>Thư giãn trọn buổi, mỏi cổ vai gáy</td><td>Gói 04</td></tr>
</tbody>
</table>

<h2>Thêm dịch vụ lẻ</h2>

<p>Khi đã chọn một gói, bạn có thể thêm dịch vụ lẻ: tẩy tế bào chết da đầu 49.000₫, massage cổ vai gáy 15 phút 89.000₫, massage mặt 15 phút 89.000₫, đắp mặt nạ Hàn Quốc 49.000₫, đắp mặt nạ mắt 19.000₫. Dịch vụ lẻ chỉ áp dụng khi dùng kèm một gói gội đầu.</p>

<h2>Đặt lịch gội đầu</h2>

<p>VESSCA mở cửa 9:00–20:30 mỗi ngày. Bạn đặt ở mục <a href="/#booking">Đặt lịch</a> trên trang chủ và chọn "Gội đầu thư giãn", hoặc "Nail và gội đầu" nếu muốn làm cả hai trong một lần ghé. Tiệm gọi lại để xác nhận giờ. Cách tìm hẻm và chỗ để xe có trong bài <a href="/blog/den-vessca-gui-xe-dat-lich/">đến VESSCA: tìm hẻm, gửi xe và đặt lịch</a>. Nếu bạn ở Phú Nhuận hoặc Gò Vấp, xem thêm bài <a href="/blog/tiem-nail-gan-phu-nhuan-go-vap/">VESSCA gần Phú Nhuận, Gò Vấp</a>.</p>'''
faq = [('Gội đầu ở VESSCA giá bao nhiêu?', 'Từ 99.000₫ (gói 30 phút, dầu gội Nguyên Xuân) đến 469.000₫ (Gói thiên đường 75 phút, dầu gội Unove).'),
       ('VESSCA gội đầu ở đâu?', '251/30 Lê Quang Định, phường Gia Định, TP.HCM (Bình Thạnh cũ), mở cửa 9:00–20:30 mỗi ngày.'),
       ('Có cần đặt lịch gội đầu trước không?', 'Nên đặt trước qua form trên web, điện thoại 0933.528.501 hoặc tin nhắn, vì tiệm phục vụ số khách giới hạn cùng lúc.'),
       ('Có thể gội đầu và làm nail cùng một buổi không?', 'Có. Khi đặt lịch, bạn chọn "Nail và gội đầu" để tiệm sắp xếp.')]
en = '''<p>VESSCA in Binh Thanh now offers a relaxing head spa and hair wash alongside Korean-style nails. There are four packages, 30 to 75 minutes, from 99,000₫ to 469,000₫ depending on the package and the shampoo you choose.</p>
<h2>The four packages</h2>
<table>
<thead><tr><th>Package</th><th>Time</th><th>Price range</th></tr></thead>
<tbody>
<tr><td>01 · Fresh Hair Wash</td><td>30 min</td><td>99,000–149,000₫</td></tr>
<tr><td>02 · Hair Wash & Scalp Therapy</td><td>50 min</td><td>229,000–279,000₫</td></tr>
<tr><td>03 · Hair Wash & Facial Glow Care</td><td>50 min</td><td>269,000–319,000₫</td></tr>
<tr><td>04 · The Paradise Ritual</td><td>75 min</td><td>419,000–469,000₫</td></tr>
</tbody>
</table>
<p>Each package has three prices because you pick one of three shampoos: Nguyen Xuan herbal, natural ginger & lemongrass, or Unove from Korea. The full step-by-step menu is on the <a href="/en/goi-dau/">head spa menu</a>.</p>
<h2>What is included</h2>
<p>Every package starts with make-up removal and a face cleanse, then a double shampoo, conditioner, a blow-dry with a negative-ion dryer and hair oil. Package 02 adds scalp exfoliation and two rounds of head massage; package 03 adds a Korean sheet mask, facial massage and LED light therapy; package 04 combines both with a neck and shoulder massage. All end with a drink and a sweet treat.</p>
<h2>Booking</h2>
<p>Use the <a href="/en/#booking">booking form</a> and choose "Head spa / hair wash", or "Nail and hair wash" to do both in one visit. Staff speak Vietnamese, English and Chinese.</p>'''
ko = '''<p>호치민 빈탄의 VESSCA에서 한국식 네일과 함께 헤드 스파·샴푸 서비스를 시작했습니다. 코스는 네 가지, 30분에서 75분이며 코스와 샴푸 종류에 따라 99,000₫부터 469,000₫까지입니다.</p>
<h2>네 가지 코스</h2>
<table>
<thead><tr><th>코스</th><th>시간</th><th>가격</th></tr></thead>
<tbody>
<tr><td>01 · 프레시 헤어 워시</td><td>30분</td><td>99,000–149,000₫</td></tr>
<tr><td>02 · 헤어 워시 & 두피 테라피</td><td>50분</td><td>229,000–279,000₫</td></tr>
<tr><td>03 · 헤어 워시 & 페이셜 글로우 케어</td><td>50분</td><td>269,000–319,000₫</td></tr>
<tr><td>04 · 파라다이스 리추얼</td><td>75분</td><td>419,000–469,000₫</td></tr>
</tbody>
</table>
<p>샴푸는 응우옌 쑤언 허브, 천연 생강·레몬그라스, 한국 어노브 중에서 고르며 선택에 따라 가격이 달라집니다. 단계별 순서는 <a href="/ko/goi-dau/">헤드 스파 메뉴</a>에서 확인하실 수 있습니다.</p>
<h2>포함 내용</h2>
<p>모든 코스는 클렌징과 세안, 샴푸 2회, 컨디셔너, 음이온 드라이, 헤어 오일로 진행합니다. 02 코스는 두피 스케일링과 두피 마사지 2회, 03 코스는 한국 마스크팩과 페이셜 마사지, LED 케어, 04 코스는 두 가지를 합치고 목·어깨 마사지를 더합니다.</p>
<h2>예약</h2>
<p><a href="/ko/#booking">예약 양식</a>에서 "헤드 스파 · 샴푸" 또는 "네일 + 샴푸"를 선택하세요. 직원은 베트남어, 영어, 중국어로 응대합니다.</p>'''
zh = '''<p>胡志明市平盛郡的 VESSCA 在韩式美甲之外,新增了舒缓洗发与头皮护理服务。共有四种套餐,时长 30 至 75 分钟,价格依套餐和洗发水不同,从 99,000₫ 到 469,000₫。</p>
<h2>四种套餐</h2>
<table>
<thead><tr><th>套餐</th><th>时长</th><th>价格</th></tr></thead>
<tbody>
<tr><td>01 · 清爽洗发</td><td>30 分钟</td><td>99,000–149,000₫</td></tr>
<tr><td>02 · 洗发＋头皮护理</td><td>50 分钟</td><td>229,000–279,000₫</td></tr>
<tr><td>03 · 洗发＋面部护理</td><td>50 分钟</td><td>269,000–319,000₫</td></tr>
<tr><td>04 · 天堂套餐</td><td>75 分钟</td><td>419,000–469,000₫</td></tr>
</tbody>
</table>
<p>每种套餐有三个价格,因为您可以在 Nguyen Xuan 草本、天然姜香茅和韩国 Unove 三款洗发水中任选一款。完整流程请看<a href="/zh/goi-dau/">洗发价目表</a>。</p>
<h2>包含内容</h2>
<p>所有套餐都包含卸妆洁面、洗发两次、护发素、负离子吹风机吹干和护发油。套餐 02 增加头皮去角质和两次头部按摩;套餐 03 增加韩国面膜、面部按摩和 LED 光疗;套餐 04 两者兼有,并加肩颈按摩。</p>
<h2>预约</h2>
<p>在<a href="/zh/#booking">预约表单</a>中选择"头皮舒压洗发"或"美甲＋洗发"即可。店员可用越南语、英语和中文接待。</p>'''
bai('goi-dau-thu-gian-binh-thanh', T, CAT,
 A(('hair wash salon', 'Gội đầu thư giãn tại tiệm', 'A relaxing hair wash at a salon', '샵에서 받는 릴랙싱 샴푸', '在店内享受舒缓洗发'), []),
 ('Gội đầu thư giãn ở Bình Thạnh: bốn gói từ 99.000₫ tại VESSCA', 'VESSCA ở phường Gia Định (Bình Thạnh) có bốn gói gội đầu thư giãn từ 30 đến 75 phút. Bảng giá theo ba loại dầu gội, mỗi gói gồm gì và cách đặt lịch.',
  'Gội đầu thư giãn Bình Thạnh từ 99.000₫ | VESSCA',
  'Gội đầu thư giãn ở Bình Thạnh: 4 gói 30–75 phút, 99.000–469.000₫, chọn dầu gội Nguyên Xuân, gừng sả hoặc Unove. VESSCA, 251/30 Lê Quang Định.',
  ['gội đầu Bình Thạnh', 'gội đầu thư giãn', 'gội đầu Gia Định', 'gội đầu Lê Quang Định', 'gội đầu massage Bình Thạnh'], vi, faq),
 ('Head Spa & Hair Wash in Binh Thanh: Four Packages from 99,000₫', 'VESSCA in Binh Thanh offers four head spa packages from 30 to 75 minutes. Prices by shampoo, what each includes and how to book.',
  'Head Spa in Binh Thanh from 99,000₫ | VESSCA', 'Relaxing hair wash and head spa in Binh Thanh, Saigon: 4 packages, 30–75 min, 99,000–469,000₫, three shampoos to choose from. VESSCA.',
  ['head spa Binh Thanh', 'hair wash Saigon', 'head spa Ho Chi Minh City', 'scalp massage Saigon'], en,
  [('How much is a hair wash at VESSCA?', 'From 99,000₫ for the 30-minute package to 469,000₫ for the 75-minute Paradise Ritual with Unove shampoo.'), ('Do I need to book?', 'Booking ahead is recommended; the salon serves a limited number of guests at a time.'), ('Can I do nails and a hair wash in one visit?', 'Yes. Choose "Nail and hair wash" in the booking form.')]),
 ('호치민 빈탄 헤드 스파·샴푸: 99,000₫부터 네 가지 코스', 'VESSCA 빈탄점의 헤드 스파 코스 네 가지. 샴푸별 가격, 코스 구성, 예약 방법.',
  '호치민 빈탄 헤드 스파 | VESSCA', '호치민 빈탄 헤드 스파·샴푸: 30–75분 4코스, 99,000–469,000₫, 샴푸 3종 선택. VESSCA.',
  ['호치민 헤드스파', '호치민 샴푸', '빈탄 헤드스파', '호치민 두피 마사지'], ko,
  [('샴푸 가격은 얼마인가요?', '30분 코스 99,000₫부터 75분 파라다이스 리추얼 469,000₫까지입니다.'), ('예약이 필요한가요?', '동시에 받는 손님 수가 제한되어 있어 미리 예약하시는 것이 좋습니다.'), ('네일과 샴푸를 같이 받을 수 있나요?', '네, 예약 양식에서 "네일 + 샴푸"를 선택하세요.')]),
 ('胡志明平盛郡舒缓洗发:四种套餐 99,000₫ 起', 'VESSCA 平盛郡店的四种洗发套餐:各洗发水价格、套餐内容与预约方式。',
  '胡志明平盛郡洗发 | VESSCA', '胡志明平盛郡舒缓洗发与头皮护理:4 种套餐,30–75 分钟,99,000–469,000₫,三款洗发水可选。VESSCA。',
  ['胡志明 洗发', '胡志明 头皮护理', '平盛郡 洗发', '胡志明 头部按摩'], zh,
  [('洗发多少钱?', '30 分钟套餐 99,000₫ 起,75 分钟天堂套餐最高 469,000₫。'), ('需要预约吗?', '建议提前预约,店内同时接待的客人数量有限。'), ('可以同时做美甲和洗发吗?', '可以,预约时选择"美甲＋洗发"。')]))

# ---------- G2. Chọn dầu gội: Nguyên Xuân, gừng sả, Unove ----------
vi = '''<p>Mỗi gói gội đầu tại VESSCA đi kèm một lựa chọn: dầu gội xả Nguyên Xuân, gừng sả thiên nhiên hoặc Unove Hàn Quốc. Ba loại khác nhau về thành phần, mùi hương và giá. Chọn theo tình trạng da đầu và tóc là cách đơn giản nhất.</p>

<h2>So sánh ba loại dầu gội</h2>

<table>
<thead><tr><th>Dầu gội</th><th>Đặc điểm</th><th>Hợp với</th><th>Giá gói 01</th></tr></thead>
<tbody>
<tr><td>Nguyên Xuân</td><td>Thảo dược truyền thống, tóc mềm bồng bềnh</td><td>Bản vàng cho da đầu dễ bết, bản xanh lá cho tóc khô, hư tổn</td><td>99.000₫</td></tr>
<tr><td>Gừng sả thiên nhiên</td><td>Nguyên liệu tự nhiên chuẩn spa, hương gừng sả ấm, lưu hương lâu</td><td>Da đầu nhạy cảm</td><td>129.000₫</td></tr>
<tr><td>Unove Hàn Quốc</td><td>Dưỡng chất chuyên sâu, hương nước hoa</td><td>Tóc nhuộm, uốn, hư tổn</td><td>149.000₫</td></tr>
</tbody>
</table>

<p>Chênh lệch giữa ba loại giữ nguyên ở mọi gói: gừng sả cao hơn Nguyên Xuân 30.000₫, Unove cao hơn Nguyên Xuân 50.000₫. Ví dụ Gói 02 là 229.000₫, 259.000₫ và 279.000₫.</p>

<h2>Chọn theo da đầu</h2>

<ul>
<li><strong>Da đầu nhanh bết, nhiều dầu:</strong> Nguyên Xuân bản vàng.</li>
<li><strong>Tóc khô, xơ:</strong> Nguyên Xuân bản xanh lá, hoặc Unove nếu tóc đã qua nhuộm, uốn.</li>
<li><strong>Da đầu nhạy cảm, thích mùi thảo mộc ấm:</strong> gừng sả thiên nhiên.</li>
<li><strong>Thích hương nước hoa lưu trên tóc:</strong> Unove.</li>
</ul>

<p>Nếu chưa chắc, bạn nói tình trạng da đầu và tóc với kỹ thuật viên trước khi gội để được gợi ý.</p>

<h2>Các bước sau khi gội</h2>

<p>Dù chọn loại nào, tóc đều được gội hai lần, xả bằng dầu xả, sấy bằng máy sấy ion âm và thoa dầu dưỡng tóc L'Oréal. VESSCA cam kết dùng sản phẩm chính hãng, nguồn gốc xuất xứ rõ ràng.</p>

<h2>Lưu ý</h2>

<p>Nếu da đầu đang có vết thương hở, viêm hoặc bạn từng dị ứng với mỹ phẩm chăm sóc tóc, hãy báo trước cho kỹ thuật viên. Bài viết chỉ mang tính tham khảo, không thay cho tư vấn của bác sĩ da liễu.</p>

<p>Xem bảng giá đủ bốn gói ở trang <a href="/goi-dau/">menu gội đầu</a> hoặc bài <a href="/blog/goi-dau-thu-gian-binh-thanh/">gội đầu thư giãn ở Bình Thạnh</a>. Muốn kết hợp chăm sóc tay chân, đọc bài <a href="/blog/hand-ritual-foot-ritual-vessca/">Hand Ritual và Foot Ritual</a>.</p>'''
faq = [('Ba loại dầu gội ở VESSCA là gì?', 'Nguyên Xuân (thảo dược), gừng sả thiên nhiên và Unove Hàn Quốc.'),
       ('Dầu gội nào rẻ nhất?', 'Nguyên Xuân. Gừng sả cao hơn 30.000₫ và Unove cao hơn 50.000₫ ở mọi gói.'),
       ('Tóc nhuộm nên chọn loại nào?', 'Menu của tiệm gợi ý Unove cho tóc nhuộm, uốn, hư tổn.'),
       ('Da đầu nhạy cảm nên chọn loại nào?', 'Gừng sả thiên nhiên là loại tiệm gợi ý cho da đầu nhạy cảm. Nếu từng dị ứng mỹ phẩm, hãy báo trước.')]
en = '''<p>Every hair wash package at VESSCA comes with a choice of shampoo: Nguyen Xuan herbal, natural ginger & lemongrass, or Unove from Korea. They differ in ingredients, scent and price.</p>
<h2>The three shampoos</h2>
<table>
<thead><tr><th>Shampoo</th><th>Character</th><th>Suits</th><th>Package 01</th></tr></thead>
<tbody>
<tr><td>Nguyen Xuan</td><td>Traditional Vietnamese herbal formula</td><td>Gold for oily scalps, green for dry or damaged hair</td><td>99,000₫</td></tr>
<tr><td>Ginger & lemongrass</td><td>Natural spa-grade ingredients, warm lasting scent</td><td>Sensitive scalps</td><td>129,000₫</td></tr>
<tr><td>Unove (Korea)</td><td>Deep-nourishing, perfume scent</td><td>Coloured, permed or damaged hair</td><td>149,000₫</td></tr>
</tbody>
</table>
<p>The gap is the same in every package: ginger & lemongrass is 30,000₫ more than Nguyen Xuan, Unove 50,000₫ more.</p>
<h2>After the shampoo</h2>
<p>Whichever you choose, hair is washed twice, conditioned, blow-dried with a negative-ion dryer and finished with L'Oréal hair oil. Tell your technician about any scalp wound or past allergy before starting. See all four packages on the <a href="/en/goi-dau/">head spa menu</a>.</p>'''
ko = '''<p>VESSCA의 모든 샴푸 코스는 샴푸를 고를 수 있습니다. 응우옌 쑤언 허브, 천연 생강·레몬그라스, 한국 어노브 세 가지이며 성분과 향, 가격이 다릅니다.</p>
<h2>세 가지 샴푸</h2>
<table>
<thead><tr><th>샴푸</th><th>특징</th><th>추천</th><th>01 코스</th></tr></thead>
<tbody>
<tr><td>응우옌 쑤언</td><td>베트남 전통 허브</td><td>골드는 지성 두피, 그린은 건조·손상 모발</td><td>99,000₫</td></tr>
<tr><td>생강·레몬그라스</td><td>천연 원료, 따뜻하고 오래가는 향</td><td>민감한 두피</td><td>129,000₫</td></tr>
<tr><td>어노브(한국)</td><td>집중 영양, 향수 향</td><td>염색·펌·손상 모발</td><td>149,000₫</td></tr>
</tbody>
</table>
<p>가격 차이는 모든 코스에서 같습니다. 생강·레몬그라스는 응우옌 쑤언보다 30,000₫, 어노브는 50,000₫ 높습니다.</p>
<h2>샴푸 후 과정</h2>
<p>어떤 샴푸를 골라도 샴푸 2회, 컨디셔너, 음이온 드라이, 로레알 헤어 오일로 마무리합니다. 두피에 상처가 있거나 알레르기 경험이 있으면 미리 알려 주세요. 전체 코스는 <a href="/ko/goi-dau/">헤드 스파 메뉴</a>에서 확인하실 수 있습니다.</p>'''
zh = '''<p>VESSCA 的每种洗发套餐都可以选择洗发水:Nguyen Xuan 草本、天然姜香茅或韩国 Unove。三款在成分、香味和价格上各不相同。</p>
<h2>三款洗发水</h2>
<table>
<thead><tr><th>洗发水</th><th>特点</th><th>适合</th><th>套餐 01</th></tr></thead>
<tbody>
<tr><td>Nguyen Xuan</td><td>越南传统草本配方</td><td>金色款适合易油头皮,绿色款适合干燥受损发质</td><td>99,000₫</td></tr>
<tr><td>姜香茅</td><td>天然原料,香气温暖持久</td><td>敏感头皮</td><td>129,000₫</td></tr>
<tr><td>Unove(韩国)</td><td>深层滋养,香水香调</td><td>染烫、受损发质</td><td>149,000₫</td></tr>
</tbody>
</table>
<p>各套餐的差价相同:姜香茅比 Nguyen Xuan 高 30,000₫,Unove 高 50,000₫。</p>
<h2>洗发之后</h2>
<p>无论选哪一款,都会洗发两次、使用护发素、负离子吹风机吹干,并涂 L'Oréal 护发油。如果头皮有伤口或曾经过敏,请提前告知技师。四种套餐请看<a href="/zh/goi-dau/">洗发价目表</a>。</p>'''
bai('chon-dau-goi-nguyen-xuan-gung-sa-unove', T, CAT,
 A(('shampoo bottles salon', 'Ba loại dầu gội xả để chọn khi gội đầu', 'Three shampoos to choose from', '선택할 수 있는 샴푸 세 가지', '可选择的三款洗发水'), []),
 ('Chọn dầu gội nào khi gội đầu ở tiệm: Nguyên Xuân, gừng sả hay Unove', 'So sánh ba loại dầu gội xả tại VESSCA theo thành phần, mùi hương, loại da đầu phù hợp và mức giá ở từng gói gội đầu.',
  'Nguyên Xuân, gừng sả hay Unove: chọn dầu gội nào | VESSCA',
  'So sánh dầu gội Nguyên Xuân, gừng sả thiên nhiên và Unove Hàn Quốc: hợp da đầu nào, chênh giá 30.000–50.000₫ mỗi gói. VESSCA Bình Thạnh.',
  ['dầu gội Nguyên Xuân', 'dầu gội gừng sả', 'dầu gội Unove', 'gội đầu thư giãn', 'chọn dầu gội theo da đầu'], vi, faq),
 ('Which Shampoo to Choose: Nguyen Xuan, Ginger & Lemongrass or Unove', 'The three shampoos at VESSCA compared by ingredients, scent, scalp type and price.',
  'Nguyen Xuan, Ginger or Unove Shampoo | VESSCA', 'Three shampoos compared for a head spa in Saigon: herbal Nguyen Xuan, ginger & lemongrass, Korean Unove. 30,000–50,000₫ apart. VESSCA.',
  ['Unove shampoo', 'Vietnamese herbal shampoo', 'head spa Saigon', 'hair wash Ho Chi Minh City'], en,
  [('What shampoos does VESSCA use?', 'Nguyen Xuan herbal, natural ginger & lemongrass, and Unove from Korea.'), ('Which is best for coloured hair?', 'The menu suggests Unove for coloured, permed or damaged hair.'), ('How much is the price difference?', 'Ginger & lemongrass is 30,000₫ more than Nguyen Xuan; Unove is 50,000₫ more.')]),
 ('샴푸 고르기: 응우옌 쑤언, 생강·레몬그라스, 어노브', 'VESSCA 샴푸 세 가지를 성분, 향, 두피 타입, 가격으로 비교합니다.',
  '샴푸 3종 비교 | 호치민 VESSCA', '호치민 헤드 스파 샴푸 3종 비교: 베트남 허브, 생강·레몬그라스, 한국 어노브. 코스당 30,000–50,000₫ 차이.',
  ['어노브 샴푸', '베트남 허브 샴푸', '호치민 헤드스파', '호치민 샴푸'], ko,
  [('어떤 샴푸가 있나요?', '응우옌 쑤언 허브, 천연 생강·레몬그라스, 한국 어노브입니다.'), ('염색 모발에는 무엇이 좋나요?', '메뉴에서는 염색·펌·손상 모발에 어노브를 추천합니다.'), ('가격 차이는요?', '생강·레몬그라스는 30,000₫, 어노브는 50,000₫ 더 높습니다.')]),
 ('洗发水怎么选:Nguyen Xuan、姜香茅还是 Unove', '从成分、香味、头皮类型和价格比较 VESSCA 的三款洗发水。',
  '三款洗发水对比 | 胡志明 VESSCA', '胡志明洗发三款洗发水对比:越南草本、姜香茅、韩国 Unove,各套餐相差 30,000–50,000₫。VESSCA。',
  ['Unove 洗发水', '越南草本洗发水', '胡志明 洗发', '胡志明 头皮护理'], zh,
  [('有哪些洗发水?', 'Nguyen Xuan 草本、天然姜香茅和韩国 Unove。'), ('染过的头发选哪款?', '价目表建议染烫、受损发质选 Unove。'), ('差价多少?', '姜香茅比 Nguyen Xuan 高 30,000₫,Unove 高 50,000₫。')]))

# ---------- G3. Gội đầu kèm chăm da mặt (Gói 03) ----------
vi = '''<p>Gói 03 tại VESSCA là gội đầu kèm chăm da mặt trong 50 phút, giá 269.000₫, 299.000₫ hoặc 319.000₫ tuỳ dầu gội. Điểm khác với gói gội thông thường là bốn bước cho da mặt: tẩy tế bào chết, đắp mặt nạ Hàn Quốc, massage mặt và chiếu đèn ánh sáng sinh học.</p>

<h2>Quy trình 11 bước</h2>

<ol>
<li>Tẩy trang Garnier, rửa mặt SVR</li>
<li>Tẩy tế bào chết da mặt</li>
<li>Đắp mặt nạ Hàn Quốc</li>
<li>Gội dầu gội 2 lần</li>
<li>Xả dầu xả</li>
<li>Massage mặt thư giãn, nâng cơ</li>
<li>Chiếu đèn ánh sáng sinh học</li>
<li>Sấy tóc bằng máy sấy ion âm</li>
<li>Dầu dưỡng tóc L'Oréal</li>
<li>Dưỡng da tay</li>
<li>Nước uống, bánh ngọt</li>
</ol>

<h2>Chọn mặt nạ</h2>

<table>
<thead><tr><th>Loại mặt nạ</th><th>Chi phí</th></tr></thead>
<tbody>
<tr><td>Mờ thâm, trắng da</td><td>Đã gồm trong gói</td></tr>
<tr><td>Cấp ẩm, phục hồi</td><td>Đã gồm trong gói</td></tr>
<tr><td>Sáng da, trẻ hoá</td><td>Đã gồm trong gói</td></tr>
<tr><td>Nâng cơ, săn chắc, dưỡng chuyên sâu</td><td>Phụ thu 30.000₫</td></tr>
</tbody>
</table>

<p>Bạn chọn một loại. Da đang khô sau nhiều ngày ngồi máy lạnh thì loại cấp ẩm là lựa chọn dễ hợp. Nếu không chắc, kỹ thuật viên xem da rồi gợi ý.</p>

<h2>Gói 03 hợp với ai</h2>

<ul>
<li>Bạn muốn gội đầu nhưng cũng muốn da mặt được làm sạch và đắp mặt nạ trong cùng một lần ghé.</li>
<li>Bạn sắp có buổi hẹn, buổi chụp hình và cần cả tóc lẫn da gọn gàng.</li>
<li>Bạn không có nhu cầu massage cổ vai gáy. Nếu có, xem Gói thiên đường 75 phút.</li>
</ul>

<h2>So với Gói 02</h2>

<p>Gói 02 và Gói 03 cùng 50 phút. Gói 02 tập trung vào da đầu với tẩy tế bào chết da đầu và hai lần massage đầu. Gói 03 tập trung vào da mặt. Giá Gói 03 cao hơn Gói 02 đúng 40.000₫ ở cả ba loại dầu gội.</p>

<h2>Lưu ý trước khi làm</h2>

<p>Nếu da mặt đang kích ứng, vừa làm thủ thuật thẩm mỹ hoặc đang dùng thuốc trị mụn theo đơn, hãy báo trước để kỹ thuật viên điều chỉnh hoặc bỏ bước không phù hợp. Bài viết chỉ mang tính tham khảo, không thay cho tư vấn của bác sĩ da liễu.</p>

<p>Bảng giá cả bốn gói có ở bài <a href="/blog/goi-dau-thu-gian-binh-thanh/">gội đầu thư giãn ở Bình Thạnh</a>. Cách chọn dầu gội xem bài <a href="/blog/chon-dau-goi-nguyen-xuan-gung-sa-unove/">Nguyên Xuân, gừng sả hay Unove</a>. Đặt lịch ở mục <a href="/#booking">Đặt lịch</a>.</p>'''
faq = [('Gội đầu kèm chăm da mặt giá bao nhiêu?', '269.000₫, 299.000₫ hoặc 319.000₫ tuỳ dầu gội, thời lượng 50 phút.'),
       ('Gói có gồm mặt nạ không?', 'Có, một mặt nạ Hàn Quốc. Loại nâng cơ, săn chắc phụ thu 30.000₫.'),
       ('Gói 03 khác Gói 02 thế nào?', 'Gói 02 chăm da đầu và massage đầu; Gói 03 chăm da mặt với mặt nạ, massage mặt và chiếu đèn.'),
       ('Da đang kích ứng có làm được không?', 'Nên báo trước cho kỹ thuật viên và hỏi ý kiến bác sĩ da liễu nếu da đang điều trị.')]
en = '''<p>Package 03 at VESSCA pairs a hair wash with facial care in 50 minutes, at 269,000₫, 299,000₫ or 319,000₫ depending on the shampoo. What sets it apart is four steps for the face: exfoliation, a Korean sheet mask, a facial massage and LED light therapy.</p>
<h2>The 11 steps</h2>
<ol><li>Garnier make-up removal, SVR cleanse</li><li>Facial exfoliation</li><li>Korean sheet mask</li><li>Double shampoo</li><li>Conditioner</li><li>Relaxing, lifting facial massage</li><li>LED light therapy</li><li>Blow-dry with a negative-ion dryer</li><li>L'Oréal hair oil</li><li>Hand care</li><li>A drink and a sweet treat</li></ol>
<h2>Choosing a mask</h2>
<p>One mask is included: brightening, hydrating & repair, or glow & rejuvenating. The lifting and firming mask is 30,000₫ extra.</p>
<h2>Compared with package 02</h2>
<p>Both take 50 minutes. Package 02 focuses on the scalp; package 03 on the face, and costs 40,000₫ more. Tell your technician first if your skin is irritated or under treatment. Full prices are on the <a href="/en/goi-dau/">head spa menu</a>.</p>'''
ko = '''<p>VESSCA의 03 코스는 샴푸와 페이셜 케어를 50분에 함께 받는 코스입니다. 가격은 샴푸에 따라 269,000₫, 299,000₫, 319,000₫입니다. 얼굴 각질 케어, 한국 마스크팩, 페이셜 마사지, LED 케어가 포함됩니다.</p>
<h2>11단계 순서</h2>
<ol><li>가르니에 클렌징, SVR 세안</li><li>얼굴 각질 케어</li><li>한국 마스크팩</li><li>샴푸 2회</li><li>컨디셔너</li><li>릴랙싱·리프팅 페이셜 마사지</li><li>LED 광테라피</li><li>음이온 드라이</li><li>로레알 헤어 오일</li><li>핸드 케어</li><li>음료와 디저트</li></ol>
<h2>마스크 선택</h2>
<p>미백, 수분·진정, 광채 중 한 가지가 포함됩니다. 리프팅·탄력 마스크는 30,000₫가 추가됩니다.</p>
<h2>02 코스와의 차이</h2>
<p>두 코스 모두 50분입니다. 02 코스는 두피, 03 코스는 얼굴에 집중하며 40,000₫ 더 높습니다. 피부가 예민하거나 치료 중이면 미리 알려 주세요. 전체 가격은 <a href="/ko/goi-dau/">헤드 스파 메뉴</a>에 있습니다.</p>'''
zh = '''<p>VESSCA 的套餐 03 把洗发和面部护理合在 50 分钟内完成,价格依洗发水为 269,000₫、299,000₫ 或 319,000₫。特别之处是四个面部步骤:去角质、韩国面膜、面部按摩和 LED 光疗。</p>
<h2>11 个步骤</h2>
<ol><li>Garnier 卸妆、SVR 洁面</li><li>面部去角质</li><li>韩国面膜</li><li>洗发两次</li><li>护发素</li><li>面部放松提拉按摩</li><li>LED 光疗</li><li>负离子吹风机吹干</li><li>L'Oréal 护发油</li><li>手部护理</li><li>饮品与甜点</li></ol>
<h2>面膜选择</h2>
<p>套餐含一片面膜:淡斑亮白、补水修护或亮肤焕颜任选。提拉紧致款需加 30,000₫。</p>
<h2>与套餐 02 的区别</h2>
<p>两者都是 50 分钟。套餐 02 侧重头皮,套餐 03 侧重面部,价格高 40,000₫。如果皮肤敏感或正在治疗,请提前告知技师。完整价格请看<a href="/zh/goi-dau/">洗发价目表</a>。</p>'''
bai('goi-dau-kem-cham-da-mat', T, CAT,
 A(('facial mask spa', 'Chăm da mặt kết hợp gội đầu', 'Facial care combined with a hair wash', '샴푸와 함께 받는 페이셜 케어', '洗发搭配面部护理'), []),
 ('Gội đầu kèm chăm da mặt: Gói 03 tại VESSCA gồm những gì', 'Gói gội đầu kèm chăm da mặt 50 phút: quy trình 11 bước, bốn loại mặt nạ Hàn Quốc, giá theo dầu gội và khác gì gói massage da đầu.',
  'Gội đầu kèm chăm da mặt 50 phút từ 269.000₫ | VESSCA',
  'Gội đầu kèm chăm da mặt 50 phút: tẩy tế bào chết, mặt nạ Hàn Quốc, massage mặt, chiếu đèn. 269.000–319.000₫. VESSCA Bình Thạnh.',
  ['gội đầu chăm da mặt', 'gội đầu đắp mặt nạ', 'gội đầu thư giãn', 'gội đầu Bình Thạnh', 'gội đầu massage mặt'], vi, faq),
 ('Hair Wash with Facial Care: What Package 03 Includes', 'A 50-minute hair wash with facial care: 11 steps, four Korean masks, prices and how it differs from the scalp package.',
  'Hair Wash & Facial Care, 50 min | VESSCA', 'Hair wash with facial care in Saigon: exfoliation, Korean sheet mask, facial massage, LED. 50 minutes, 269,000–319,000₫. VESSCA Binh Thanh.',
  ['hair wash facial Saigon', 'head spa Ho Chi Minh City', 'Korean sheet mask spa', 'head spa Binh Thanh'], en,
  [('How much is it?', '269,000₫, 299,000₫ or 319,000₫ depending on the shampoo, for 50 minutes.'), ('Is a mask included?', 'Yes, one Korean sheet mask. The lifting and firming mask is 30,000₫ extra.'), ('How is it different from package 02?', 'Package 02 focuses on the scalp; package 03 on the face.')]),
 ('샴푸와 페이셜 케어를 함께: 03 코스 구성', '50분 샴푸·페이셜 코스: 11단계 순서, 마스크팩 4종, 가격, 두피 코스와의 차이.',
  '샴푸 + 페이셜 케어 50분 | VESSCA', '호치민 샴푸·페이셜 케어 50분: 각질 케어, 한국 마스크팩, 페이셜 마사지, LED. 269,000–319,000₫.',
  ['호치민 페이셜', '호치민 헤드스파', '호치민 샴푸', '빈탄 헤드스파'], ko,
  [('가격은 얼마인가요?', '샴푸에 따라 269,000₫, 299,000₫, 319,000₫이며 50분입니다.'), ('마스크팩이 포함되나요?', '네, 한 가지가 포함됩니다. 리프팅·탄력 마스크는 30,000₫ 추가입니다.'), ('02 코스와 무엇이 다른가요?', '02 코스는 두피, 03 코스는 얼굴에 집중합니다.')]),
 ('洗发加面部护理:套餐 03 包含什么', '50 分钟洗发加面部护理:11 个步骤、四款韩国面膜、价格,以及与头皮套餐的区别。',
  '洗发＋面部护理 50 分钟 | VESSCA', '胡志明洗发加面部护理 50 分钟:去角质、韩国面膜、面部按摩、LED 光疗,269,000–319,000₫。VESSCA。',
  ['胡志明 面部护理', '胡志明 洗发', '韩国面膜 护理', '平盛郡 洗发'], zh,
  [('价格是多少?', '依洗发水为 269,000₫、299,000₫ 或 319,000₫,时长 50 分钟。'), ('包含面膜吗?', '包含一片韩国面膜,提拉紧致款加 30,000₫。'), ('和套餐 02 有什么不同?', '套餐 02 侧重头皮,套餐 03 侧重面部。')]))

# ---------- G4. Gói thiên đường 75 phút ----------
vi = '''<p>Gói thiên đường là gói gội đầu dài nhất tại VESSCA: 75 phút, 14 bước, chăm cả da mặt, da đầu và cổ vai gáy. Giá 419.000₫, 449.000₫ hoặc 469.000₫ tuỳ dầu gội. Bài này đi qua từng bước để bạn biết 75 phút đó diễn ra thế nào.</p>

<h2>14 bước của Gói thiên đường</h2>

<ol>
<li>Tẩy trang Garnier, rửa mặt SVR</li>
<li>Tẩy tế bào chết da mặt</li>
<li>Đắp mặt nạ Hàn Quốc</li>
<li>Tẩy tế bào chết da đầu</li>
<li>Gội dầu gội 2 lần</li>
<li>Xả dầu xả</li>
<li>Massage mặt thư giãn, nâng cơ</li>
<li>Chiếu đèn ánh sáng sinh học</li>
<li>Đắp mặt nạ mắt</li>
<li>Massage đầu, cổ vai gáy thư giãn</li>
<li>Sấy tóc bằng máy sấy ion âm</li>
<li>Dầu dưỡng tóc L'Oréal</li>
<li>Dưỡng da tay</li>
<li>Nước uống, bánh ngọt</li>
</ol>

<h2>So với ba gói còn lại</h2>

<table>
<thead><tr><th></th><th>Gói 01</th><th>Gói 02</th><th>Gói 03</th><th>Gói 04</th></tr></thead>
<tbody>
<tr><td>Thời lượng</td><td>30 phút</td><td>50 phút</td><td>50 phút</td><td>75 phút</td></tr>
<tr><td>Tẩy tế bào chết da đầu</td><td>–</td><td>Có</td><td>–</td><td>Có</td></tr>
<tr><td>Mặt nạ Hàn Quốc, massage mặt</td><td>–</td><td>–</td><td>Có</td><td>Có</td></tr>
<tr><td>Massage cổ vai gáy</td><td>–</td><td>–</td><td>–</td><td>Có</td></tr>
<tr><td>Giá từ</td><td>99.000₫</td><td>229.000₫</td><td>269.000₫</td><td>419.000₫</td></tr>
</tbody>
</table>

<h2>Tính thử: gói lớn hay gói nhỏ cộng dịch vụ lẻ</h2>

<p>Lấy dầu gội Nguyên Xuân làm ví dụ. Gói 03 là 269.000₫. Nếu thêm ba dịch vụ lẻ để gần bằng Gói 04: tẩy tế bào chết da đầu 49.000₫, massage đầu và cổ vai gáy 15 phút 89.000₫, đắp mặt nạ mắt 19.000₫, tổng là 269.000 + 49.000 + 89.000 + 19.000 = 426.000₫. Gói thiên đường cùng dầu gội là 419.000₫. Nếu bạn muốn đủ các bước, chọn thẳng Gói 04 gọn hơn.</p>

<h2>Gói này hợp với ai</h2>

<ul>
<li>Bạn ngồi máy tính nhiều, hay mỏi cổ vai gáy.</li>
<li>Bạn muốn một buổi nghỉ trọn vẹn, không phải chọn giữa chăm da đầu và chăm da mặt.</li>
<li>Bạn muốn tặng một buổi thư giãn cho người thân.</li>
</ul>

<h2>Đặt lịch</h2>

<p>Vì gói kéo dài 75 phút, bạn nên đặt trước và đến đúng giờ. VESSCA mở cửa 9:00–20:30 mỗi ngày; để kịp trọn gói, nên bắt đầu trước 19:00. Đặt ở mục <a href="/#booking">Đặt lịch</a>, chọn "Gội đầu thư giãn". Lý do tiệm khuyên đặt trước có trong bài <a href="/blog/vi-sao-vessca-gioi-han-so-khach/">vì sao VESSCA giới hạn số khách</a>. Bảng giá đủ bốn gói: <a href="/blog/goi-dau-thu-gian-binh-thanh/">gội đầu thư giãn ở Bình Thạnh</a>.</p>'''
faq = [('Gói thiên đường giá bao nhiêu?', '419.000₫, 449.000₫ hoặc 469.000₫ tuỳ dầu gội Nguyên Xuân, gừng sả hay Unove.'),
       ('Gói kéo dài bao lâu?', '75 phút, gồm 14 bước.'),
       ('Gói 04 khác Gói 03 thế nào?', 'Gói 04 có thêm tẩy tế bào chết da đầu, đắp mặt nạ mắt và massage đầu, cổ vai gáy.'),
       ('Có chọn được mặt nạ không?', 'Có, chọn một loại mặt nạ Hàn Quốc; loại nâng cơ, săn chắc phụ thu 30.000₫.')]
en = '''<p>The Paradise Ritual is the longest head spa package at VESSCA: 75 minutes and 14 steps for your face, scalp, neck and shoulders. It costs 419,000₫, 449,000₫ or 469,000₫ depending on the shampoo.</p>
<h2>The 14 steps</h2>
<ol><li>Make-up removal and face cleanse</li><li>Facial exfoliation</li><li>Korean sheet mask</li><li>Scalp exfoliation</li><li>Double shampoo</li><li>Conditioner</li><li>Relaxing, lifting facial massage</li><li>LED light therapy</li><li>Eye mask</li><li>Head, neck and shoulder massage</li><li>Blow-dry with a negative-ion dryer</li><li>L'Oréal hair oil</li><li>Hand care</li><li>A drink and a sweet treat</li></ol>
<h2>Package or add-ons?</h2>
<p>With Nguyen Xuan shampoo, package 03 plus scalp exfoliation, a 15-minute head and shoulder massage and an eye mask adds up to 426,000₫; the Paradise Ritual is 419,000₫. If you want every step, the full package is simpler.</p>
<h2>Booking</h2>
<p>Book ahead and arrive on time; starting before 19:00 lets you finish before closing at 20:30. See the <a href="/en/goi-dau/">head spa menu</a>.</p>'''
ko = '''<p>파라다이스 리추얼은 VESSCA에서 가장 긴 헤드 스파 코스입니다. 75분, 14단계로 얼굴, 두피, 목과 어깨를 모두 케어합니다. 가격은 샴푸에 따라 419,000₫, 449,000₫, 469,000₫입니다.</p>
<h2>14단계 순서</h2>
<ol><li>클렌징과 세안</li><li>얼굴 각질 케어</li><li>한국 마스크팩</li><li>두피 스케일링</li><li>샴푸 2회</li><li>컨디셔너</li><li>페이셜 마사지</li><li>LED 광테라피</li><li>아이 마스크</li><li>두피·목·어깨 마사지</li><li>음이온 드라이</li><li>로레알 헤어 오일</li><li>핸드 케어</li><li>음료와 디저트</li></ol>
<h2>코스와 단품 비교</h2>
<p>응우옌 쑤언 샴푸 기준, 03 코스에 두피 스케일링, 15분 두피·어깨 마사지, 아이 마스크를 더하면 426,000₫입니다. 파라다이스 리추얼은 419,000₫이므로 모든 단계를 원하시면 코스가 더 간단합니다.</p>
<h2>예약</h2>
<p>미리 예약하고 시간에 맞춰 오세요. 20:30에 마감하므로 19:00 전에 시작하시는 것이 좋습니다. <a href="/ko/goi-dau/">헤드 스파 메뉴</a>를 참고하세요.</p>'''
zh = '''<p>天堂套餐是 VESSCA 最长的洗发套餐:75 分钟、14 个步骤,同时护理面部、头皮和肩颈。价格依洗发水为 419,000₫、449,000₫ 或 469,000₫。</p>
<h2>14 个步骤</h2>
<ol><li>卸妆洁面</li><li>面部去角质</li><li>韩国面膜</li><li>头皮去角质</li><li>洗发两次</li><li>护发素</li><li>面部按摩</li><li>LED 光疗</li><li>眼膜</li><li>头部及肩颈按摩</li><li>负离子吹风机吹干</li><li>L'Oréal 护发油</li><li>手部护理</li><li>饮品与甜点</li></ol>
<h2>套餐还是单项加购</h2>
<p>以 Nguyen Xuan 洗发水为例,套餐 03 加头皮去角质、15 分钟头部及肩颈按摩和眼膜,合计 426,000₫;天堂套餐为 419,000₫。想要全部步骤,直接选套餐更简单。</p>
<h2>预约</h2>
<p>请提前预约并准时到店。店铺 20:30 关门,建议 19:00 前开始。详见<a href="/zh/goi-dau/">洗发价目表</a>。</p>'''
bai('goi-thien-duong-75-phut', T, CAT,
 A(('head spa massage', 'Massage đầu và cổ vai gáy trong Gói thiên đường', 'Head and neck massage in the Paradise Ritual', '파라다이스 리추얼의 두피·목 마사지', '天堂套餐中的头部与肩颈按摩'), []),
 ('Gói thiên đường 75 phút: gội đầu, chăm da mặt và massage cổ vai gáy', 'Gói gội đầu dài nhất tại VESSCA diễn ra thế nào: 14 bước, so sánh với ba gói còn lại, tính thử so với dịch vụ lẻ và cách đặt lịch.',
  'Gói thiên đường 75 phút: gội đầu, massage | VESSCA',
  'Gói thiên đường 75 phút, 14 bước: gội đầu, mặt nạ Hàn Quốc, massage mặt, massage cổ vai gáy. 419.000–469.000₫. VESSCA Bình Thạnh.',
  ['gội đầu massage cổ vai gáy', 'gói gội đầu 75 phút', 'gội đầu thư giãn', 'gội đầu Bình Thạnh', 'gội đầu chăm da mặt'], vi, faq),
 ('The Paradise Ritual: 75 Minutes of Hair Wash, Facial and Massage', 'How the longest head spa package at VESSCA runs: 14 steps, comparison with add-ons and booking tips.',
  'The Paradise Ritual, 75 min Head Spa | VESSCA', 'A 75-minute, 14-step head spa in Saigon: hair wash, Korean mask, facial massage, neck and shoulder massage. 419,000–469,000₫. VESSCA.',
  ['head spa Saigon', 'head spa Ho Chi Minh City', 'neck shoulder massage Saigon', 'head spa Binh Thanh'], en,
  [('How much is the Paradise Ritual?', '419,000₫, 449,000₫ or 469,000₫ depending on the shampoo.'), ('How long does it take?', '75 minutes, 14 steps.'), ('What does it add to package 03?', 'Scalp exfoliation, an eye mask and a head, neck and shoulder massage.')]),
 ('파라다이스 리추얼 75분: 샴푸, 페이셜, 목·어깨 마사지', 'VESSCA에서 가장 긴 헤드 스파 코스의 14단계와 단품 비교, 예약 팁.',
  '파라다이스 리추얼 75분 | 호치민 VESSCA', '호치민 75분 헤드 스파 14단계: 샴푸, 한국 마스크팩, 페이셜·목·어깨 마사지. 419,000–469,000₫.',
  ['호치민 헤드스파', '호치민 마사지', '호치민 샴푸', '빈탄 헤드스파'], ko,
  [('가격은 얼마인가요?', '샴푸에 따라 419,000₫, 449,000₫, 469,000₫입니다.'), ('얼마나 걸리나요?', '75분, 14단계입니다.'), ('03 코스와 차이는요?', '두피 스케일링, 아이 마스크, 두피·목·어깨 마사지가 더해집니다.')]),
 ('天堂套餐 75 分钟:洗发、面部护理与肩颈按摩', 'VESSCA 最长洗发套餐的 14 个步骤、与单项加购的比较及预约建议。',
  '天堂套餐 75 分钟 | 胡志明 VESSCA', '胡志明 75 分钟洗发套餐 14 步:洗发、韩国面膜、面部按摩、肩颈按摩,419,000–469,000₫。VESSCA。',
  ['胡志明 头皮护理', '胡志明 按摩', '胡志明 洗发', '平盛郡 洗发'], zh,
  [('天堂套餐多少钱?', '依洗发水为 419,000₫、449,000₫ 或 469,000₫。'), ('需要多长时间?', '75 分钟,14 个步骤。'), ('比套餐 03 多了什么?', '头皮去角质、眼膜和头部及肩颈按摩。')]))
