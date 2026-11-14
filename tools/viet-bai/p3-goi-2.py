"""Đợt 14/11/2026 — cụm bài GỘI ĐẦU (2/2). Số liệu theo lib/goi-dau.mjs."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *

CAT = 'Gội đầu & Thư giãn'
T = '2026-11-14T12:30:00+07:00'

# ---------- G5. Nail và gội đầu cùng một buổi ----------
vi = '''<p>Từ khi VESSCA có thêm gội đầu thư giãn, nhiều khách hỏi có làm được nail và gội đầu trong cùng một lần ghé không. Câu trả lời là có. Bài này giải thích cách đặt lịch, vài cách kết hợp phổ biến và chi phí tham khảo.</p>

<h2>Đặt lịch một lần cho cả hai</h2>

<p>Ở mục <a href="/#booking">Đặt lịch</a> trên trang chủ, bạn chọn dịch vụ "Nail và gội đầu", chọn ngày giờ và ghi chú nếu đã biết muốn làm gì. Tiệm gọi lại để xác nhận và sắp xếp thứ tự hai dịch vụ cho bạn đỡ phải chờ. Nếu đặt qua điện thoại 0933.528.501, Instagram hoặc Facebook, bạn nói rõ là làm cả hai.</p>

<h2>Vài cách kết hợp và chi phí tham khảo</h2>

<table>
<thead><tr><th>Kết hợp</th><th>Cách tính</th><th>Tổng</th></tr></thead>
<tbody>
<tr><td>Sơn gel trơn + gội sạch thơm (Nguyên Xuân)</td><td>130.000 + 99.000</td><td>229.000₫</td></tr>
<tr><td>Sơn thạch + gội massage chăm da đầu (Nguyên Xuân)</td><td>150.000 + 229.000</td><td>379.000₫</td></tr>
<tr><td>Hand Ritual + gội kèm chăm da mặt (gừng sả)</td><td>250.000 + 299.000</td><td>549.000₫</td></tr>
<tr><td>Full Ritual + Gói thiên đường (Unove)</td><td>550.000 + 469.000</td><td>1.019.000₫</td></tr>
</tbody>
</table>

<p>Giá nail chưa gồm phá gel cũ (30.000₫), vẽ, đính đá hay mix màu nếu bạn chọn thêm. Bảng giá nail đầy đủ có ở trang <a href="/bang-gia/">bảng giá</a>, bấm "Gội đầu" ở đầu trang để xem giá gội.</p>

<h2>Khi nào nên làm cả hai</h2>

<ul>
<li>Trước một buổi tiệc, buổi chụp hình hoặc chuyến đi, cần tay và tóc cùng gọn gàng.</li>
<li>Ngày nghỉ muốn dành trọn một buổi chăm sóc bản thân.</li>
<li>Bạn ở xa, muốn tận dụng một lần đi.</li>
</ul>

<h2>Mẹo để buổi hẹn trôi chảy</h2>

<ul>
<li>Nếu đã có mẫu nail, gửi ảnh trước qua tin nhắn để kỹ thuật viên chuẩn bị màu.</li>
<li>Báo trước nếu bạn có dị ứng mỹ phẩm hay da đầu nhạy cảm.</li>
<li>Chọn giờ còn dư thời gian: một bộ nail cộng Gói thiên đường 75 phút có thể mất gần cả buổi chiều.</li>
</ul>

<p>Muốn hiểu thêm từng gói gội, đọc bài <a href="/blog/goi-dau-thu-gian-binh-thanh/">gội đầu thư giãn ở Bình Thạnh</a>. Các bước của một bộ nail tại tiệm có ở bài <a href="/blog/quy-trinh-lam-nail-tai-vessca/">quy trình làm nail tại VESSCA</a>.</p>'''
faq = [('Có làm nail và gội đầu cùng một lần được không?', 'Được. Khi đặt lịch, bạn chọn "Nail và gội đầu" để tiệm sắp xếp.'),
       ('Làm cả nail và gội đầu tốn bao nhiêu?', 'Tuỳ dịch vụ. Ví dụ sơn gel trơn 130.000₫ cộng gói gội 30 phút 99.000₫ là 229.000₫.'),
       ('Nên làm nail trước hay gội đầu trước?', 'Tiệm sẽ sắp xếp thứ tự khi xác nhận lịch để bạn ít phải chờ nhất.')]
en = '''<p>Since VESSCA added a head spa menu, many guests ask whether they can have their nails done and a hair wash in one visit. Yes: choose "Nail and hair wash" in the <a href="/en/#booking">booking form</a> and the salon arranges the order so you wait as little as possible.</p>
<h2>Sample combinations</h2>
<table>
<thead><tr><th>Combination</th><th>Total</th></tr></thead>
<tbody>
<tr><td>Plain gel (130,000₫) + Fresh Hair Wash, Nguyen Xuan (99,000₫)</td><td>229,000₫</td></tr>
<tr><td>Jelly gel (150,000₫) + Scalp Therapy, Nguyen Xuan (229,000₫)</td><td>379,000₫</td></tr>
<tr><td>Hand Ritual (250,000₫) + Facial Glow Care, ginger (299,000₫)</td><td>549,000₫</td></tr>
<tr><td>Full Ritual (550,000₫) + Paradise Ritual, Unove (469,000₫)</td><td>1,019,000₫</td></tr>
</tbody>
</table>
<p>Nail prices do not include gel removal (30,000₫) or nail art. Send your nail reference photo ahead and mention any allergies. A full set plus the 75-minute Paradise Ritual can take most of an afternoon.</p>'''
ko = '''<p>VESSCA에 헤드 스파 메뉴가 생긴 뒤로 네일과 샴푸를 한 번에 받을 수 있는지 묻는 분이 많습니다. 가능합니다. <a href="/ko/#booking">예약 양식</a>에서 "네일 + 샴푸"를 선택하시면 기다리는 시간이 적도록 순서를 맞춰 드립니다.</p>
<h2>조합 예시</h2>
<table>
<thead><tr><th>조합</th><th>합계</th></tr></thead>
<tbody>
<tr><td>원컬러 젤(130,000₫) + 프레시 헤어 워시(99,000₫)</td><td>229,000₫</td></tr>
<tr><td>시럽 젤(150,000₫) + 두피 테라피(229,000₫)</td><td>379,000₫</td></tr>
<tr><td>핸드 리추얼(250,000₫) + 페이셜 글로우 케어, 생강(299,000₫)</td><td>549,000₫</td></tr>
<tr><td>풀 리추얼(550,000₫) + 파라다이스 리추얼, 어노브(469,000₫)</td><td>1,019,000₫</td></tr>
</tbody>
</table>
<p>네일 가격에는 젤 제거(30,000₫)와 아트가 포함되지 않습니다. 원하는 디자인 사진을 미리 보내 주시고 알레르기가 있으면 알려 주세요.</p>'''
zh = '''<p>VESSCA 推出洗发服务后,不少客人问能否一次同时做美甲和洗发。可以:在<a href="/zh/#booking">预约表单</a>中选择"美甲＋洗发",店里会安排顺序,尽量减少您的等待。</p>
<h2>组合参考</h2>
<table>
<thead><tr><th>组合</th><th>合计</th></tr></thead>
<tbody>
<tr><td>纯色凝胶(130,000₫)＋清爽洗发(99,000₫)</td><td>229,000₫</td></tr>
<tr><td>果冻凝胶(150,000₫)＋洗发头皮护理(229,000₫)</td><td>379,000₫</td></tr>
<tr><td>Hand Ritual(250,000₫)＋洗发面部护理,姜香茅(299,000₫)</td><td>549,000₫</td></tr>
<tr><td>Full Ritual(550,000₫)＋天堂套餐,Unove(469,000₫)</td><td>1,019,000₫</td></tr>
</tbody>
</table>
<p>美甲价格不含卸甲(30,000₫)和彩绘。可提前发送款式图片,如有过敏请告知。</p>'''
bai('nail-va-goi-dau-cung-mot-buoi', T, CAT,
 A(('manicure salon relax', 'Làm nail và gội đầu trong cùng một buổi', 'Nails and a hair wash in one visit', '한 번에 받는 네일과 샴푸', '一次完成美甲与洗发'), []),
 ('Làm nail và gội đầu cùng một buổi: cách đặt lịch và chi phí', 'Đặt một lịch cho cả nail và gội đầu tại VESSCA: cách chọn dịch vụ, bốn cách kết hợp kèm tổng chi phí và mẹo để buổi hẹn trôi chảy.',
  'Làm nail và gội đầu cùng một buổi | VESSCA Bình Thạnh',
  'Làm nail và gội đầu trong một lần ghé VESSCA: chọn "Nail và gội đầu" khi đặt lịch, kết hợp từ 229.000₫. 251/30 Lê Quang Định, Bình Thạnh.',
  ['nail và gội đầu', 'làm nail gội đầu', 'gội đầu thư giãn', 'gội đầu Bình Thạnh'], vi, faq),
 ('Nails and a Hair Wash in One Visit: Booking and Prices', 'How to book nails and a head spa together at VESSCA, four sample combinations with totals, and tips.',
  'Nails & Hair Wash in One Visit | VESSCA', 'Book nails and a head spa together at VESSCA in Binh Thanh, Saigon. Combinations from 229,000₫, one booking.',
  ['nail salon head spa Saigon', 'head spa Binh Thanh', 'nail salon Binh Thanh'], en,
  [('Can I do both in one visit?', 'Yes. Choose "Nail and hair wash" when you book.'), ('How much does it cost?', 'It depends on the services; for example plain gel plus a 30-minute hair wash is 229,000₫.')]),
 ('네일과 샴푸를 한 번에: 예약 방법과 가격', 'VESSCA에서 네일과 헤드 스파를 함께 예약하는 방법, 조합 네 가지와 합계.',
  '네일 + 샴푸 한 번에 | 호치민 VESSCA', '호치민 빈탄 VESSCA에서 네일과 헤드 스파를 한 번에. 조합 229,000₫부터.',
  ['호치민 네일', '호치민 헤드스파', '빈탄 네일'], ko,
  [('한 번에 받을 수 있나요?', '네, 예약 시 "네일 + 샴푸"를 선택하세요.'), ('가격은요?', '서비스에 따라 다르며 원컬러 젤과 30분 샴푸는 229,000₫입니다.')]),
 ('美甲和洗发一次完成:预约方式与价格', '在 VESSCA 同时预约美甲与洗发的方法、四种组合及合计价格。',
  '美甲＋洗发一次完成 | 胡志明 VESSCA', '在胡志明平盛郡 VESSCA 一次完成美甲与洗发,组合 229,000₫ 起。',
  ['胡志明 美甲', '胡志明 洗发', '平盛郡 美甲'], zh,
  [('可以一次做两项吗?', '可以,预约时选择"美甲＋洗发"。'), ('多少钱?', '视项目而定,例如纯色凝胶加 30 分钟洗发为 229,000₫。')]))

# ---------- G6. Gội đầu massage da đầu (Gói 02) ----------
vi = '''<p>Gói 02 tại VESSCA là gội đầu kèm massage và chăm sóc da đầu, kéo dài 50 phút, giá 229.000₫, 259.000₫ hoặc 279.000₫ tuỳ dầu gội. So với gói gội nhanh 30 phút, gói này thêm tẩy tế bào chết da đầu, đắp mặt nạ mắt, hai lần massage đầu và dưỡng da tay.</p>

<h2>Quy trình 11 bước</h2>

<ol>
<li>Tẩy trang Garnier, rửa mặt SVR</li>
<li>Tẩy tế bào chết da đầu</li>
<li>Đắp mặt nạ mắt</li>
<li>Massage đầu thư giãn lần 1</li>
<li>Gội dầu gội 2 lần</li>
<li>Xả dầu xả siêu mượt</li>
<li>Massage đầu thư giãn lần 2</li>
<li>Sấy bảo vệ tóc bằng máy sấy ion âm</li>
<li>Dầu dưỡng tóc L'Oréal</li>
<li>Dưỡng da tay</li>
<li>Nước uống, bánh ngọt</li>
</ol>

<h2>Vì sao có bước tẩy tế bào chết da đầu</h2>

<p>Dầu, bụi và cặn sản phẩm tạo kiểu tích lại trên da đầu sau nhiều ngày. Gội thường làm sạch tóc nhưng không phải lúc nào cũng lấy hết lớp cặn sát chân tóc. Bước tẩy tế bào chết giúp làm sạch kỹ hơn trước khi gội, nhờ đó da đầu nhẹ hơn sau buổi gội. Hiệu quả thực tế khác nhau ở mỗi người và phụ thuộc thói quen chăm tóc ở nhà.</p>

<h2>Gói 02 hợp với ai</h2>

<ul>
<li>Da đầu nhanh bết, hay dùng keo, sáp vuốt tóc.</li>
<li>Thích cảm giác được massage đầu sau ngày dài làm việc.</li>
<li>Muốn thêm chút chăm sóc cho mắt và tay mà không cần đến gói chăm da mặt.</li>
</ul>

<p>Nếu da đầu dễ bết, bạn có thể chọn dầu gội Nguyên Xuân bản vàng; da đầu nhạy cảm thì cân nhắc gừng sả thiên nhiên. So sánh chi tiết ở bài <a href="/blog/chon-dau-goi-nguyen-xuan-gung-sa-unove/">chọn dầu gội Nguyên Xuân, gừng sả hay Unove</a>.</p>

<h2>Muốn massage lâu hơn</h2>

<p>Bạn có thể thêm dịch vụ lẻ massage đầu và cổ vai gáy 15 phút (89.000₫). Nếu muốn chăm cả da mặt, Gói thiên đường 75 phút gộp đủ các bước, xem bài <a href="/blog/goi-thien-duong-75-phut/">Gói thiên đường 75 phút</a>.</p>

<h2>Lưu ý</h2>

<p>Nếu da đầu đang có vết thương, viêm, gàu nặng kéo dài hoặc rụng tóc bất thường, nên đi khám bác sĩ da liễu. Gội đầu thư giãn là dịch vụ chăm sóc, không phải điều trị.</p>'''
faq = [('Gội đầu massage da đầu ở VESSCA giá bao nhiêu?', '229.000₫, 259.000₫ hoặc 279.000₫ tuỳ dầu gội, thời lượng 50 phút.'),
       ('Gói 02 có mấy lần massage đầu?', 'Hai lần: một lần trước khi gội và một lần sau khi xả.'),
       ('Có thêm massage cổ vai gáy được không?', 'Được, dịch vụ lẻ massage đầu và cổ vai gáy 15 phút giá 89.000₫.'),
       ('Gội đầu có chữa được gàu hay rụng tóc không?', 'Không. Đây là dịch vụ chăm sóc thư giãn; vấn đề da đầu kéo dài nên đi khám bác sĩ da liễu.')]
en = '''<p>Package 02 at VESSCA is a hair wash with scalp therapy: 50 minutes, 229,000₫, 259,000₫ or 279,000₫ depending on the shampoo. Compared with the 30-minute wash, it adds scalp exfoliation, an eye mask, two rounds of head massage and hand care.</p>
<h2>The 11 steps</h2>
<ol><li>Make-up removal, face cleanse</li><li>Scalp exfoliation</li><li>Eye mask</li><li>Head massage, round 1</li><li>Double shampoo</li><li>Silky conditioner</li><li>Head massage, round 2</li><li>Negative-ion blow-dry</li><li>L'Oréal hair oil</li><li>Hand care</li><li>A drink and a sweet treat</li></ol>
<h2>Who it suits</h2>
<p>Oily scalps, people who use styling products, and anyone who wants a proper head massage after a long day. Add a 15-minute head, neck and shoulder massage for 89,000₫. A hair wash is care, not treatment: see a dermatologist for persistent scalp problems.</p>'''
ko = '''<p>VESSCA의 02 코스는 두피 마사지와 케어가 포함된 샴푸 코스입니다. 50분, 샴푸에 따라 229,000₫, 259,000₫, 279,000₫이며 두피 스케일링, 아이 마스크, 두피 마사지 2회, 핸드 케어가 더해집니다.</p>
<h2>11단계 순서</h2>
<ol><li>클렌징, 세안</li><li>두피 스케일링</li><li>아이 마스크</li><li>두피 마사지 1차</li><li>샴푸 2회</li><li>실키 컨디셔너</li><li>두피 마사지 2차</li><li>음이온 드라이</li><li>로레알 헤어 오일</li><li>핸드 케어</li><li>음료와 디저트</li></ol>
<h2>추천 대상</h2>
<p>두피가 쉽게 기름지는 분, 스타일링 제품을 자주 쓰시는 분께 맞습니다. 15분 두피·목·어깨 마사지(89,000₫)를 추가할 수 있습니다. 두피 문제가 오래가면 피부과 진료를 받으세요.</p>'''
zh = '''<p>VESSCA 的套餐 02 是含头皮按摩与护理的洗发套餐:50 分钟,依洗发水为 229,000₫、259,000₫ 或 279,000₫。比 30 分钟洗发多了头皮去角质、眼膜、两次头部按摩和手部护理。</p>
<h2>11 个步骤</h2>
<ol><li>卸妆洁面</li><li>头皮去角质</li><li>眼膜</li><li>头部按摩(第一次)</li><li>洗发两次</li><li>柔顺护发素</li><li>头部按摩(第二次)</li><li>负离子吹干</li><li>L'Oréal 护发油</li><li>手部护理</li><li>饮品与甜点</li></ol>
<h2>适合谁</h2>
<p>头皮易油、常用造型产品的人。可加 15 分钟头部及肩颈按摩(89,000₫)。头皮问题持续请就医。</p>'''
bai('goi-dau-massage-da-dau', T, CAT,
 A(('scalp massage', 'Massage da đầu khi gội đầu', 'A scalp massage during a hair wash', '샴푸 중 두피 마사지', '洗发时的头皮按摩'), []),
 ('Gội đầu massage da đầu 50 phút: quy trình và giá tại VESSCA', 'Gói gội đầu kèm massage, tẩy tế bào chết da đầu tại VESSCA: 11 bước, giá theo dầu gội, hợp với ai và lưu ý khi da đầu có vấn đề.',
  'Gội đầu massage da đầu 50 phút từ 229.000₫ | VESSCA',
  'Gội đầu massage da đầu 50 phút: tẩy tế bào chết da đầu, 2 lần massage đầu, mặt nạ mắt. 229.000–279.000₫. VESSCA Bình Thạnh.',
  ['gội đầu massage', 'massage da đầu', 'gội đầu massage da đầu', 'gội đầu thư giãn', 'gội đầu Bình Thạnh'], vi, faq),
 ('Hair Wash with Scalp Massage: 50 Minutes at VESSCA', 'The VESSCA scalp therapy package: 11 steps, prices by shampoo and who it suits.',
  'Scalp Massage Hair Wash, 50 min | VESSCA', 'A 50-minute hair wash with scalp exfoliation and two head massages in Binh Thanh, Saigon. 229,000–279,000₫. VESSCA.',
  ['scalp massage Saigon', 'head spa Saigon', 'head spa Binh Thanh'], en,
  [('How much is it?', '229,000₫, 259,000₫ or 279,000₫ depending on the shampoo.'), ('How many head massages?', 'Two: before the shampoo and after the conditioner.')]),
 ('두피 마사지 샴푸 50분: 순서와 가격', 'VESSCA 두피 테라피 코스의 11단계, 샴푸별 가격, 추천 대상.',
  '두피 마사지 샴푸 50분 | 호치민 VESSCA', '호치민 빈탄 50분 두피 스케일링·두피 마사지 2회 샴푸 코스. 229,000–279,000₫.',
  ['호치민 두피 마사지', '호치민 헤드스파', '빈탄 헤드스파'], ko,
  [('가격은요?', '샴푸에 따라 229,000₫, 259,000₫, 279,000₫입니다.'), ('마사지는 몇 번인가요?', '샴푸 전과 컨디셔너 후 두 번입니다.')]),
 ('头皮按摩洗发 50 分钟:流程与价格', 'VESSCA 洗发头皮护理套餐的 11 个步骤、价格与适合人群。',
  '头皮按摩洗发 50 分钟 | 胡志明 VESSCA', '胡志明平盛郡 50 分钟洗发:头皮去角质、两次头部按摩,229,000–279,000₫。VESSCA。',
  ['胡志明 头皮按摩', '胡志明 洗发', '平盛郡 洗发'], zh,
  [('多少钱?', '依洗发水为 229,000₫、259,000₫ 或 279,000₫。'), ('按摩几次?', '两次:洗发前和护发素后。')]))

# ---------- G7. Gội đầu gần Phú Nhuận, Gò Vấp ----------
vi = '''<p>Nếu bạn ở Phú Nhuận hoặc Gò Vấp và đang tìm chỗ gội đầu thư giãn, VESSCA ở 251/30 Lê Quang Định, phường Gia Định (Bình Thạnh cũ), cùng phường chợ Bà Chiểu và giáp ranh hai khu này. Tiệm vốn làm nail kiểu Hàn, nay có thêm bốn gói gội đầu từ 99.000₫.</p>

<h2>Thông tin nhanh</h2>

<table>
<thead><tr><th>Mục</th><th>Chi tiết</th></tr></thead>
<tbody>
<tr><td>Địa chỉ</td><td>251/30 Lê Quang Định, phường Gia Định, TP.HCM (trong hẻm 251)</td></tr>
<tr><td>Giờ mở cửa</td><td>9:00–20:30 mỗi ngày</td></tr>
<tr><td>Gói gội</td><td>30, 50 hoặc 75 phút</td></tr>
<tr><td>Giá</td><td>99.000₫ – 469.000₫</td></tr>
<tr><td>Để xe</td><td>Có chỗ để xe trước tiệm</td></tr>
<tr><td>Đặt lịch</td><td>Form trên web, điện thoại 0933.528.501, Instagram, Facebook</td></tr>
</tbody>
</table>

<h2>Chọn gói theo thời gian bạn có</h2>

<ul>
<li><strong>Giờ nghỉ trưa hoặc trước buổi hẹn:</strong> Gói 01, 30 phút, gội sạch, sấy và dưỡng tóc.</li>
<li><strong>Sau giờ làm:</strong> Gói 02 (massage chăm da đầu) hoặc Gói 03 (chăm da mặt), mỗi gói 50 phút.</li>
<li><strong>Ngày nghỉ:</strong> Gói thiên đường 75 phút, có massage cổ vai gáy.</li>
</ul>

<p>Bảng giá chi tiết theo từng loại dầu gội có ở bài <a href="/blog/goi-dau-thu-gian-binh-thanh/">gội đầu thư giãn ở Bình Thạnh</a>.</p>

<h2>Vì sao nên đặt trước</h2>

<p>VESSCA phục vụ số khách giới hạn cùng lúc để không gian yên tĩnh và mỗi khách được làm kỹ. Đặt trước giúp bạn có giờ chắc chắn, nhất là buổi tối và cuối tuần. Lý do tiệm chọn cách này có ở bài <a href="/blog/vi-sao-vessca-gioi-han-so-khach/">vì sao VESSCA giới hạn số khách</a>.</p>

<h2>Kết hợp với nail</h2>

<p>Nhiều khách ở xa chọn làm nail và gội đầu trong một lần ghé. Khi đặt lịch, chọn "Nail và gội đầu". Xem thêm bài <a href="/blog/tiem-nail-gan-phu-nhuan-go-vap/">tiệm nail gần Phú Nhuận, Gò Vấp</a> và cách tìm hẻm ở bài <a href="/blog/den-vessca-gui-xe-dat-lich/">đến VESSCA: tìm hẻm, gửi xe</a>.</p>'''
faq = [('Có chỗ gội đầu thư giãn nào gần Phú Nhuận, Gò Vấp?', 'VESSCA ở 251/30 Lê Quang Định, phường Gia Định, cùng phường chợ Bà Chiểu, giáp Phú Nhuận và Gò Vấp.'),
       ('Gội đầu ở VESSCA mở cửa đến mấy giờ?', 'Tiệm mở cửa 9:00–20:30 mỗi ngày.'),
       ('Có chỗ để xe không?', 'Có chỗ để xe trước tiệm.')]
en = '''<p>Looking for a relaxing hair wash near Phu Nhuan or Go Vap? VESSCA is at 251/30 Le Quang Dinh, Gia Dinh ward (formerly Binh Thanh), in the same ward as Ba Chieu market and bordering both areas. The salon does Korean-style nails and now four head spa packages from 99,000₫.</p>
<h2>Quick facts</h2>
<ul><li>Open 9:00–20:30 daily</li><li>Packages of 30, 50 or 75 minutes, 99,000–469,000₫</li><li>Parking in front of the salon</li><li>Book online, by phone (0933.528.501), Instagram or Facebook</li></ul>
<p>The salon serves a limited number of guests at a time, so booking ahead is recommended, especially evenings and weekends. Choose "Nail and hair wash" to combine both.</p>'''
ko = '''<p>푸뉴언이나 고밥 근처에서 헤드 스파를 찾으신다면, VESSCA는 251/30 Le Quang Dinh, 자딘 동(옛 빈탄)에 있으며 벤짜이 시장과 같은 동이고 두 지역과 맞닿아 있습니다. 한국식 네일과 함께 99,000₫부터 헤드 스파 코스 네 가지를 운영합니다.</p>
<h2>기본 정보</h2>
<ul><li>매일 9:00–20:30 영업</li><li>30·50·75분 코스, 99,000–469,000₫</li><li>샵 앞 주차 가능</li><li>웹, 전화(0933.528.501), 인스타그램, 페이스북 예약</li></ul>
<p>동시에 받는 손님 수를 제한하므로 저녁과 주말에는 미리 예약하시는 것이 좋습니다.</p>'''
zh = '''<p>在富润郡或鹅邑郡附近找舒缓洗发?VESSCA 位于 251/30 Le Quang Dinh,嘉定坊(原平盛郡),与 Ba Chieu 市场同坊,紧邻这两个区。店里提供韩式美甲,以及 99,000₫ 起的四种洗发套餐。</p>
<h2>基本信息</h2>
<ul><li>每天 9:00–20:30 营业</li><li>30、50 或 75 分钟套餐,99,000–469,000₫</li><li>店门前可停车</li><li>可通过网站、电话(0933.528.501)、Instagram、Facebook 预约</li></ul>
<p>店内同时接待人数有限,晚上和周末建议提前预约。</p>'''
bai('goi-dau-gan-phu-nhuan-go-vap', T, CAT,
 A(('hair salon wash', 'Gội đầu thư giãn gần Phú Nhuận, Gò Vấp', 'A hair wash near Phu Nhuan and Go Vap', '푸뉴언·고밥 근처 헤드 스파', '富润郡、鹅邑郡附近的洗发'), []),
 ('Gội đầu thư giãn gần Phú Nhuận, Gò Vấp: VESSCA ở Gia Định', 'Tìm chỗ gội đầu thư giãn gần Phú Nhuận, Gò Vấp: địa chỉ, giờ mở cửa, chọn gói theo thời gian và vì sao nên đặt lịch trước.',
  'Gội đầu gần Phú Nhuận, Gò Vấp từ 99.000₫ | VESSCA',
  'Gội đầu thư giãn gần Phú Nhuận, Gò Vấp: VESSCA, 251/30 Lê Quang Định, phường Gia Định. Gói 30–75 phút, 99.000–469.000₫, mở 9:00–20:30.',
  ['gội đầu Phú Nhuận', 'gội đầu Gò Vấp', 'gội đầu gần đây', 'gội đầu thư giãn', 'gội đầu Bình Thạnh'], vi, faq),
 ('Head Spa near Phu Nhuan and Go Vap: VESSCA in Gia Dinh', 'A relaxing hair wash near Phu Nhuan and Go Vap: address, hours, packages and booking.',
  'Head Spa near Phu Nhuan & Go Vap | VESSCA', 'Relaxing hair wash near Phu Nhuan and Go Vap, Saigon: VESSCA, 251/30 Le Quang Dinh. 30–75 min, from 99,000₫, open 9:00–20:30.',
  ['head spa Phu Nhuan', 'head spa Go Vap', 'head spa Saigon'], en,
  [('Where is it?', '251/30 Le Quang Dinh, Gia Dinh ward, bordering Phu Nhuan and Go Vap.'), ('Opening hours?', '9:00–20:30 every day.')]),
 ('푸뉴언·고밥 근처 헤드 스파: 자딘 동 VESSCA', '푸뉴언·고밥 근처 헤드 스파: 주소, 영업시간, 코스와 예약.',
  '푸뉴언·고밥 근처 헤드 스파 | VESSCA', '호치민 푸뉴언·고밥 근처 헤드 스파 VESSCA. 30–75분 코스 99,000₫부터, 매일 9:00–20:30.',
  ['푸뉴언 헤드스파', '고밥 헤드스파', '호치민 헤드스파'], ko,
  [('어디에 있나요?', '251/30 Le Quang Dinh, 자딘 동이며 푸뉴언·고밥과 맞닿아 있습니다.'), ('영업시간은요?', '매일 9:00–20:30입니다.')]),
 ('富润郡、鹅邑郡附近的舒缓洗发:嘉定坊 VESSCA', '富润郡、鹅邑郡附近的洗发店:地址、营业时间、套餐与预约。',
  '富润郡·鹅邑郡附近洗发 | VESSCA', '胡志明富润郡、鹅邑郡附近舒缓洗发 VESSCA,30–75 分钟套餐 99,000₫ 起,每天 9:00–20:30。',
  ['富润郡 洗发', '鹅邑郡 洗发', '胡志明 洗发'], zh,
  [('在哪里?', '251/30 Le Quang Dinh,嘉定坊,紧邻富润郡和鹅邑郡。'), ('营业时间?', '每天 9:00–20:30。')]))

# ---------- G8. Dịch vụ lẻ khi gội đầu ----------
vi = '''<p>Ngoài bốn gói gội đầu, VESSCA có danh sách dịch vụ lẻ để bạn thêm vào gói đã chọn: massage cổ vai gáy, đắp mặt nạ, chiếu đèn ánh sáng sinh học và vài bước chăm da khác. Dịch vụ lẻ chỉ áp dụng khi dùng kèm một gói gội đầu.</p>

<h2>Bảng giá dịch vụ lẻ</h2>

<table>
<thead><tr><th>Nhóm</th><th>Dịch vụ</th><th>Giá</th></tr></thead>
<tbody>
<tr><td rowspan="3">Chăm sóc da đầu</td><td>Tẩy tế bào chết da đầu</td><td>49.000₫</td></tr>
<tr><td>Massage đầu và cổ vai gáy (15 phút)</td><td>89.000₫</td></tr>
<tr><td>Massage cổ vai gáy (15 phút)</td><td>89.000₫</td></tr>
<tr><td rowspan="6">Chăm sóc da mặt</td><td>Tẩy trang Garnier, rửa mặt SVR</td><td>49.000₫</td></tr>
<tr><td>Tẩy tế bào chết da mặt</td><td>29.000₫</td></tr>
<tr><td>Đắp mặt nạ Hàn Quốc</td><td>49.000₫</td></tr>
<tr><td>Massage mặt (15 phút)</td><td>89.000₫</td></tr>
<tr><td>Chiếu đèn ánh sáng sinh học</td><td>49.000₫</td></tr>
<tr><td>Đắp mặt nạ mắt</td><td>19.000₫</td></tr>
</tbody>
</table>

<p>Với mặt nạ Hàn Quốc, loại nâng cơ, săn chắc phụ thu 30.000₫. Ba loại còn lại (mờ thâm trắng da, cấp ẩm phục hồi, sáng da trẻ hoá) không phụ thu.</p>

<h2>Thêm gì vào gói nào</h2>

<ul>
<li><strong>Gói 01 (30 phút):</strong> thêm tẩy tế bào chết da đầu nếu da đầu nhanh bết, hoặc đắp mặt nạ mắt khi mắt mỏi.</li>
<li><strong>Gói 02 (massage da đầu):</strong> thêm massage cổ vai gáy 15 phút nếu hay ngồi máy tính.</li>
<li><strong>Gói 03 (chăm da mặt):</strong> thêm massage đầu và cổ vai gáy nếu muốn thư giãn cả phần đầu.</li>
</ul>

<h2>Khi nào chọn thẳng gói lớn hơn</h2>

<p>Nếu cộng nhiều dịch vụ lẻ, hãy so với gói lớn hơn. Ví dụ Gói 03 (Nguyên Xuân, 269.000₫) thêm tẩy tế bào chết da đầu, massage đầu và cổ vai gáy, mặt nạ mắt là 426.000₫, trong khi Gói thiên đường cùng dầu gội là 419.000₫ và đã gồm các bước đó. Chi tiết ở bài <a href="/blog/goi-thien-duong-75-phut/">Gói thiên đường 75 phút</a>.</p>

<p>Nói với kỹ thuật viên dịch vụ lẻ bạn muốn thêm khi đến tiệm, hoặc ghi chú lúc <a href="/#booking">đặt lịch</a> để tiệm sắp xếp thời gian. Menu đầy đủ ở trang <a href="/goi-dau/">menu gội đầu</a>.</p>'''
faq = [('Dịch vụ lẻ gội đầu có làm riêng được không?', 'Không. Dịch vụ lẻ áp dụng khi dùng kèm một gói gội đầu.'),
       ('Massage cổ vai gáy giá bao nhiêu?', '89.000₫ cho 15 phút.'),
       ('Mặt nạ nâng cơ có phụ thu không?', 'Có, loại nâng cơ, săn chắc phụ thu 30.000₫.')]
en = '''<p>Besides the four head spa packages, VESSCA has add-ons you can put on top of any package. Add-ons are only available with a package.</p>
<h2>Add-on prices</h2>
<table>
<thead><tr><th>Add-on</th><th>Price</th></tr></thead>
<tbody>
<tr><td>Scalp exfoliation</td><td>49,000₫</td></tr>
<tr><td>Head, neck & shoulder massage (15 min)</td><td>89,000₫</td></tr>
<tr><td>Neck & shoulder massage (15 min)</td><td>89,000₫</td></tr>
<tr><td>Make-up removal & face cleanse</td><td>49,000₫</td></tr>
<tr><td>Facial exfoliation</td><td>29,000₫</td></tr>
<tr><td>Korean sheet mask (lifting type +30,000₫)</td><td>49,000₫</td></tr>
<tr><td>Facial massage (15 min)</td><td>89,000₫</td></tr>
<tr><td>LED light therapy</td><td>49,000₫</td></tr>
<tr><td>Eye mask</td><td>19,000₫</td></tr>
</tbody>
</table>
<p>If you add several, compare with a bigger package: package 03 with three add-ons can cost more than the 75-minute Paradise Ritual, which already includes them.</p>'''
ko = '''<p>VESSCA에는 헤드 스파 코스 네 가지 외에 코스에 추가할 수 있는 단품 메뉴가 있습니다. 단품은 코스와 함께일 때만 이용할 수 있습니다.</p>
<h2>단품 가격</h2>
<table>
<thead><tr><th>단품</th><th>가격</th></tr></thead>
<tbody>
<tr><td>두피 스케일링</td><td>49,000₫</td></tr>
<tr><td>두피·목·어깨 마사지(15분)</td><td>89,000₫</td></tr>
<tr><td>목·어깨 마사지(15분)</td><td>89,000₫</td></tr>
<tr><td>클렌징·세안</td><td>49,000₫</td></tr>
<tr><td>얼굴 각질 케어</td><td>29,000₫</td></tr>
<tr><td>한국 마스크팩(리프팅 +30,000₫)</td><td>49,000₫</td></tr>
<tr><td>페이셜 마사지(15분)</td><td>89,000₫</td></tr>
<tr><td>LED 광테라피</td><td>49,000₫</td></tr>
<tr><td>아이 마스크</td><td>19,000₫</td></tr>
</tbody>
</table>
<p>여러 개를 추가하신다면 상위 코스와 비교해 보세요.</p>'''
zh = '''<p>除了四种洗发套餐,VESSCA 还有可加在套餐上的单项服务。单项服务需搭配套餐使用。</p>
<h2>单项价格</h2>
<table>
<thead><tr><th>项目</th><th>价格</th></tr></thead>
<tbody>
<tr><td>头皮去角质</td><td>49,000₫</td></tr>
<tr><td>头部及肩颈按摩(15 分钟)</td><td>89,000₫</td></tr>
<tr><td>肩颈按摩(15 分钟)</td><td>89,000₫</td></tr>
<tr><td>卸妆洁面</td><td>49,000₫</td></tr>
<tr><td>面部去角质</td><td>29,000₫</td></tr>
<tr><td>韩国面膜(提拉款 +30,000₫)</td><td>49,000₫</td></tr>
<tr><td>面部按摩(15 分钟)</td><td>89,000₫</td></tr>
<tr><td>LED 光疗</td><td>49,000₫</td></tr>
<tr><td>眼膜</td><td>19,000₫</td></tr>
</tbody>
</table>
<p>加购多项时,可以和更高一级的套餐比较。</p>'''
bai('dich-vu-le-goi-dau-massage-mat-na', T, CAT,
 A(('neck shoulder massage', 'Massage cổ vai gáy, dịch vụ lẻ khi gội đầu', 'Neck and shoulder massage add-on', '목·어깨 마사지 단품', '肩颈按摩单项'), []),
 ('Dịch vụ lẻ khi gội đầu: massage cổ vai gáy, mặt nạ, chiếu đèn', 'Bảng giá dịch vụ lẻ đi kèm gói gội đầu tại VESSCA, nên thêm gì vào gói nào và khi nào chọn thẳng gói lớn hơn sẽ hợp lý hơn.',
  'Dịch vụ lẻ gội đầu: massage cổ vai gáy, mặt nạ | VESSCA',
  'Dịch vụ lẻ kèm gói gội đầu tại VESSCA: massage cổ vai gáy 15 phút 89.000₫, mặt nạ Hàn Quốc 49.000₫, mặt nạ mắt 19.000₫, chiếu đèn 49.000₫.',
  ['massage cổ vai gáy', 'gội đầu đắp mặt nạ', 'dịch vụ lẻ gội đầu', 'gội đầu thư giãn', 'gội đầu massage'], vi, faq),
 ('Head Spa Add-ons: Neck Massage, Masks and LED', 'VESSCA head spa add-on prices and when a bigger package makes more sense.',
  'Head Spa Add-ons: Massage, Masks | VESSCA', 'Head spa add-ons at VESSCA, Saigon: 15-min neck and shoulder massage 89,000₫, Korean mask 49,000₫, eye mask 19,000₫, LED 49,000₫.',
  ['neck shoulder massage Saigon', 'head spa Saigon', 'Korean sheet mask spa'], en,
  [('Can I book an add-on alone?', 'No, add-ons are only available with a head spa package.'), ('How much is the neck massage?', '89,000₫ for 15 minutes.')]),
 ('헤드 스파 단품: 목·어깨 마사지, 마스크팩, LED', 'VESSCA 헤드 스파 단품 가격과 상위 코스가 나은 경우.',
  '헤드 스파 단품 가격 | 호치민 VESSCA', '호치민 VESSCA 헤드 스파 단품: 15분 목·어깨 마사지 89,000₫, 마스크팩 49,000₫, 아이 마스크 19,000₫.',
  ['호치민 마사지', '호치민 헤드스파', '호치민 마스크팩'], ko,
  [('단품만 받을 수 있나요?', '아니요, 코스와 함께일 때만 가능합니다.'), ('목·어깨 마사지 가격은요?', '15분 89,000₫입니다.')]),
 ('洗发单项服务:肩颈按摩、面膜、LED', 'VESSCA 洗发单项价格,以及何时直接选更大的套餐更划算。',
  '洗发单项价格 | 胡志明 VESSCA', '胡志明 VESSCA 洗发单项:15 分钟肩颈按摩 89,000₫、韩国面膜 49,000₫、眼膜 19,000₫、LED 49,000₫。',
  ['胡志明 肩颈按摩', '胡志明 洗发', '韩国面膜 护理'], zh,
  [('可以只做单项吗?', '不可以,单项需搭配洗发套餐。'), ('肩颈按摩多少钱?', '15 分钟 89,000₫。')]))
