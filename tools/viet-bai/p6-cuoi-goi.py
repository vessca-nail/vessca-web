"""Đợt 16/11/2026 — cụm CƯỚI + GỘI ĐẦU. Giá nail theo HUONG-DAN-VIET-BAI.md §6, giá gội theo lib/goi-dau.mjs."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *

X, G, Q, C = 'Xu hướng & Cảm hứng', 'Gội đầu & Thư giãn', 'Hỏi & Đáp', 'Chăm sóc móng'
T = '2026-11-16T12:00:00+07:00'

# ---------- 1. Nail cô dâu kiểu Hàn ----------
vi = '''<p>Nail cô dâu kiểu Hàn thường đi theo hướng tối giản: móng không quá dài, màu nhạt, chi tiết nhỏ. Lý do đơn giản là trong ảnh cưới, bàn tay luôn xuất hiện cạnh nhẫn và hoa, nên bộ móng cần làm nền chứ không giành phần nhìn.</p>

<h2>Bốn hướng hay được chọn</h2>

<table>
<thead><tr><th>Hướng</th><th>Mô tả</th><th>Giá tham khảo</th></tr></thead>
<tbody>
<tr><td>Nude sữa</td><td>Màu gần với da, tay nhìn sạch trong mọi khung hình</td><td>130.000₫</td></tr>
<tr><td>Thạch trong</td><td>Trong như lớp men mỏng, hợp người thích nhẹ</td><td>150.000₫</td></tr>
<tr><td>Xà cừ ánh trai</td><td>Ánh ngọc trai chuyển theo ánh sáng</td><td>280.000₫</td></tr>
<tr><td>French mảnh</td><td>Viền trắng mỏng ở đầu móng</td><td>130.000₫ + French từ 15.000₫</td></tr>
</tbody>
</table>

<h2>Chi tiết thêm nên dừng ở đâu</h2>

<p>Với nail cưới, một hai móng có chi tiết là vừa. Vài viên đá nhỏ ở chân móng (10.000₫ mỗi viên, Swarovski 20.000₫) hoặc một nét vẽ mảnh (từ 10.000₫) thường lên ảnh đẹp hơn cả bàn tay kín hoạ tiết. Đá quá to dễ vướng khi cầm hoa và khi trao nhẫn.</p>

<h2>Độ dài và form</h2>

<ul>
<li><strong>Form oval hoặc vuông bo góc</strong> an toàn, hợp hầu hết bàn tay.</li>
<li><strong>Độ dài vừa phải</strong> để còn cầm hoa, chỉnh váy, bắt tay khách.</li>
<li>Muốn dài thêm: úp móng 130.000₫, Gel X 190.000₫, đắp gel 250.000₫, dual form 350.000₫.</li>
</ul>

<h2>Làm trước ngày cưới mấy ngày</h2>

<p>Thường 1–3 ngày trước là vừa, móng còn mới mà không sợ lệch lịch. VESSCA bảo hành 5 ngày. Nếu chụp ảnh cưới sớm hơn nhiều, có thể làm một bộ cho buổi chụp rồi làm lại cho ngày cưới. Lịch đầy đủ có ở bài <a href="/blog/nail-va-goi-dau-truoc-ngay-cuoi/">nail và gội đầu trước ngày cưới</a>.</p>

<h2>Đặt lịch</h2>

<p>Nếu đi cùng phù dâu hoặc mẹ, liên hệ sớm qua 0933.528.501 vì tiệm phục vụ số khách giới hạn cùng lúc. Mẫu cho phù dâu có ở bài <a href="/blog/nail-phu-dau-di-dam-cuoi/">nail phù dâu đi đám cưới</a>. Đặt lịch ở mục <a href="/#booking">Đặt lịch</a>.</p>'''
faq = [('Nail cô dâu kiểu Hàn thường màu gì?', 'Nude sữa, thạch trong, xà cừ ánh trai hoặc French mảnh.'),
       ('Nail cưới giá bao nhiêu?', 'Sơn gel trơn 130.000₫, sơn thạch 150.000₫, xà cừ ánh trai 280.000₫, French từ 15.000₫.'),
       ('Nên làm trước ngày cưới mấy ngày?', 'Thường 1–3 ngày trước; VESSCA bảo hành 5 ngày.'),
       ('Đính đá nhiều có ảnh hưởng gì không?', 'Đá to dễ vướng khi cầm hoa và trao nhẫn; nên để vài viên nhỏ ở một hai móng.')]
en = '''<p>Korean-style bridal nails lean minimal: moderate length, soft colour, small details. In wedding photos your hands sit beside the ring and the bouquet, so the nails work best as a backdrop.</p>
<h2>Four directions</h2>
<ul><li>Milky nude — close to skin tone, clean in every frame (130,000₫)</li><li>Clear jelly — like a thin glaze (150,000₫)</li><li>Mother-of-pearl — shifts with the light (280,000₫)</li><li>A thin French line (130,000₫ + from 15,000₫)</li></ul>
<h2>Where to stop</h2>
<p>One or two accent nails is plenty: a few small stones at the base (from 10,000₫, Swarovski 20,000₫) or a fine line (from 10,000₫). Large stones catch on the bouquet and during the ring exchange.</p>
<h2>Timing</h2>
<p>Usually 1–3 days before the wedding; VESSCA offers a 5-day guarantee. For a bridesmaid group, call 0933.528.501 early.</p>'''
ko = '''<p>한국식 브라이덜 네일은 미니멀한 편입니다. 적당한 길이, 은은한 컬러, 작은 디테일. 웨딩 사진에서 손은 늘 반지와 부케 옆에 있기 때문에 네일은 배경 역할을 할 때 가장 예쁩니다.</p>
<h2>네 가지 방향</h2>
<ul><li>밀키 누드 — 피부톤에 가까워 어느 컷에서도 깔끔(130,000₫)</li><li>클리어 젤리 — 얇은 유약 같은 느낌(150,000₫)</li><li>자개 — 빛에 따라 색이 변합니다(280,000₫)</li><li>얇은 프렌치 라인(130,000₫ + 15,000₫부터)</li></ul>
<h2>디테일의 기준</h2>
<p>포인트는 한두 개면 충분합니다. 큐티클 쪽 작은 스톤 몇 개(10,000₫부터, 스와로브스키 20,000₫)나 얇은 라인(10,000₫부터). 큰 스톤은 부케나 반지 교환 때 걸리기 쉽습니다.</p>
<h2>시기</h2>
<p>보통 결혼식 1–3일 전이며 5일 보증을 제공합니다. 들러리 단체는 0933.528.501로 미리 연락해 주세요.</p>'''
zh = '''<p>韩式新娘美甲偏简约:长度适中、颜色柔和、细节小巧。婚礼照片里,手总是与戒指和捧花同框,指甲做陪衬最好看。</p>
<h2>四种方向</h2>
<ul><li>奶裸色——接近肤色,任何画面都干净(130,000₫)</li><li>果冻透明——像一层薄釉(150,000₫)</li><li>贝壳光——随光线变化(280,000₫)</li><li>细法式线条(130,000₫ + 15,000₫ 起)</li></ul>
<h2>细节到哪里为止</h2>
<p>一两指做重点就够:甲根几颗小钻(10,000₫ 起,施华洛世奇 20,000₫)或一道细线(10,000₫ 起)。大颗水钻容易勾到捧花,交换戒指时也不便。</p>
<h2>时间安排</h2>
<p>通常婚礼前 1–3 天,保修 5 天。伴娘团请提前致电 0933.528.501。</p>'''
bai('nail-co-dau-kieu-han', T, X,
 A(('bridal nails', 'Nail cô dâu tông nhạt kiểu Hàn', 'Soft Korean-style bridal nails', '한국식 브라이덜 네일', '韩式新娘美甲'), []),
 ('Nail cô dâu kiểu Hàn: bốn hướng tối giản và nên dừng chi tiết ở đâu',
  'Nail cô dâu kiểu Hàn thiên về tối giản: bốn hướng màu hay chọn, mức độ chi tiết vừa phải, độ dài form móng và nên làm trước ngày cưới mấy ngày.',
  'Nail cô dâu kiểu Hàn: 4 hướng tối giản | VESSCA',
  'Nail cô dâu kiểu Hàn: nude sữa 130.000₫, thạch trong 150.000₫, xà cừ ánh trai 280.000₫, French mảnh. Làm trước cưới 1–3 ngày, bảo hành 5 ngày.',
  ['nail cô dâu', 'nail cưới', 'nail cô dâu kiểu Hàn', 'nail cưới tối giản', 'nail cô dâu Bình Thạnh'], vi, faq),
 ('Korean-Style Bridal Nails: Four Minimal Directions',
  'Four colour directions for Korean-style bridal nails, how much detail to add and when to book.',
  'Korean-Style Bridal Nails | VESSCA', 'Korean-style bridal nails in Saigon: milky nude 130,000₫, jelly 150,000₫, mother-of-pearl 280,000₫, thin French. Book 1–3 days before.',
  ['bridal nails Saigon', 'korean bridal nails', 'wedding nails Ho Chi Minh City'], en,
  [('What colours?', 'Milky nude, clear jelly, mother-of-pearl or a thin French line.'),
   ('When should I book?', 'Usually 1–3 days before the wedding; there is a 5-day guarantee.')]),
 ('한국식 브라이덜 네일: 미니멀한 네 가지',
  '컬러 네 가지, 디테일의 기준, 예약 시기.',
  '한국식 브라이덜 네일 | 호치민 VESSCA', '호치민 한국식 브라이덜 네일: 밀키 누드 130,000₫, 젤리 150,000₫, 자개 280,000₫, 얇은 프렌치.',
  ['호치민 웨딩 네일', '브라이덜 네일', '호치민 네일'], ko,
  [('어떤 컬러인가요?', '밀키 누드, 클리어 젤리, 자개, 얇은 프렌치입니다.'),
   ('언제 하나요?', '보통 결혼식 1–3일 전이며 5일 보증입니다.')]),
 ('韩式新娘美甲:四种简约方向',
  '四种配色方向、细节的分寸,以及预约时间。',
  '韩式新娘美甲 | 胡志明 VESSCA', '胡志明韩式新娘美甲:奶裸 130,000₫、果冻 150,000₫、贝壳光 280,000₫、细法式。婚礼前 1–3 天做。',
  ['胡志明 新娘美甲', '韩式 新娘美甲', '胡志明 婚礼美甲'], zh,
  [('用什么颜色?', '奶裸色、果冻透明、贝壳光或细法式。'),
   ('什么时候做?', '通常婚礼前 1–3 天,保修 5 天。')]))

# ---------- 2. Nail cho mẹ cô dâu, mẹ chú rể ----------
vi = '''<p>Ngày cưới không chỉ có cô dâu lên ảnh. Mẹ cô dâu và mẹ chú rể đứng đón khách, trao quà, chụp ảnh gia đình, nên bàn tay cũng nên gọn gàng. Bài này gợi ý mẫu hợp, ưu tiên nhẹ nhàng và dễ sinh hoạt.</p>

<h2>Mẫu hợp</h2>

<table>
<thead><tr><th>Mẫu</th><th>Vì sao hợp</th><th>Giá</th></tr></thead>
<tbody>
<tr><td>Nude hồng hoặc nude sữa</td><td>Trang nhã, hợp áo dài mọi màu</td><td>130.000₫</td></tr>
<tr><td>Đỏ rượu vang</td><td>Ấm, lên ảnh rõ mà không chói</td><td>130.000₫</td></tr>
<tr><td>Xà cừ ánh trai</td><td>Ánh nhẹ, sang, hợp dịp trang trọng</td><td>280.000₫</td></tr>
<tr><td>Chỉ cắt da, dưỡng viền</td><td>Cho người không quen sơn màu</td><td>Tay 60.000₫, chân 70.000₫</td></tr>
</tbody>
</table>

<h2>Điều nên lưu ý</h2>

<ul>
<li><strong>Độ dài ngắn vừa:</strong> dễ làm việc nhà, bưng bê trong ngày cưới.</li>
<li><strong>Tránh đá to:</strong> dễ vướng khi cầm khay, chỉnh áo dài.</li>
<li><strong>Báo nếu da tay khô:</strong> bước dưỡng viền và dưỡng da tay giúp tay nhìn mềm hơn trong ảnh cận.</li>
<li><strong>Nếu có bệnh lý về móng</strong> như móng dày, đổi màu kéo dài, nên đi khám trước thay vì phủ sơn lên.</li>
</ul>

<h2>Gộp một buổi cho cả nhà</h2>

<p>Nhiều gia đình cho cô dâu, mẹ và phù dâu làm chung một buổi. Tiệm phục vụ số khách giới hạn cùng lúc nên nhóm từ ba người trở lên hãy gọi 0933.528.501 trước vài ngày để sắp xếp. Buổi đó có thể kèm gội đầu thư giãn: gói 30 phút từ 99.000₫, gói 50 phút từ 229.000₫.</p>

<h2>Chăm sóc tay chân trọn gói</h2>

<p>Nếu muốn tay chân mềm mịn cho ngày cưới, Hand Ritual 30 phút là 250.000₫, Foot Ritual 45 phút 350.000₫, Full Ritual 60 phút 550.000₫. Chi tiết từng bước có ở bài <a href="/blog/hand-ritual-foot-ritual-vessca/">Hand Ritual và Foot Ritual</a>. Lịch làm đẹp trước cưới có ở bài <a href="/blog/nail-va-goi-dau-truoc-ngay-cuoi/">nail và gội đầu trước ngày cưới</a>.</p>'''
faq = [('Mẹ cô dâu nên làm nail màu gì?', 'Nude hồng, nude sữa, đỏ rượu vang hoặc xà cừ ánh trai là những lựa chọn trang nhã.'),
       ('Không quen sơn màu thì làm gì?', 'Có thể chỉ cắt da, chỉnh form, dưỡng viền: tay 60.000₫, chân 70.000₫.'),
       ('Cả nhà làm chung một buổi được không?', 'Được, nhóm từ ba người nên gọi 0933.528.501 trước vài ngày.')]
en = '''<p>On a wedding day the mothers are in plenty of photos too. Hands show when greeting guests and in family portraits, so a tidy set helps.</p>
<h2>What suits</h2>
<ul><li>Pink or milky nude — elegant with any ao dai (130,000₫)</li><li>Burgundy — warm, visible in photos without shouting (130,000₫)</li><li>Mother-of-pearl — a soft sheen for formal occasions (280,000₫)</li><li>Cuticle care and shaping only, for anyone who does not wear colour (hands 60,000₫, feet 70,000₫)</li></ul>
<h2>Worth noting</h2>
<p>Keep the length short, skip large stones, and mention dry hands so the care steps can be adjusted. For persistent nail problems, see a doctor rather than covering them with polish.</p>
<h2>Together as a family</h2>
<p>Groups of three or more should call 0933.528.501 a few days ahead. A hair wash can be added: 30 minutes from 99,000₫, 50 minutes from 229,000₫. Hand Ritual 250,000₫, Foot Ritual 350,000₫, Full Ritual 550,000₫.</p>'''
ko = '''<p>결혼식 날에는 어머님들도 사진에 많이 담깁니다. 손님을 맞이하고 가족 사진을 찍을 때 손이 자주 보이니 단정한 네일이 도움이 됩니다.</p>
<h2>어울리는 디자인</h2>
<ul><li>핑크·밀키 누드 — 아오자이 어느 색과도 잘 어울립니다(130,000₫)</li><li>버건디 — 따뜻하고 사진에 잘 나옵니다(130,000₫)</li><li>자개 — 격식 있는 자리에 어울리는 은은한 광(280,000₫)</li><li>컬러가 부담되면 큐티클 케어만(손 60,000₫, 발 70,000₫)</li></ul>
<h2>참고</h2>
<p>길이는 짧게, 큰 스톤은 피하시고, 손이 건조하면 미리 알려 주세요. 손톱 문제가 오래되었다면 덮기보다 진료를 받으시는 것이 좋습니다.</p>
<h2>가족이 함께</h2>
<p>3인 이상은 며칠 전 0933.528.501로 연락 주세요. 샴푸도 함께 가능합니다(30분 99,000₫부터, 50분 229,000₫부터). 핸드 리추얼 250,000₫, 풋 리추얼 350,000₫, 풀 리추얼 550,000₫.</p>'''
zh = '''<p>婚礼当天,母亲们同样常出现在照片里。迎宾、拍全家福时手都很显眼,整洁的指甲会加分。</p>
<h2>适合的款式</h2>
<ul><li>粉裸或奶裸——与各色奥黛都相配(130,000₫)</li><li>酒红——温暖,上镜却不张扬(130,000₫)</li><li>贝壳光——柔和光泽,适合正式场合(280,000₫)</li><li>不习惯上色,可只做修死皮修形(手 60,000₫、脚 70,000₫)</li></ul>
<h2>提醒</h2>
<p>长度宜短,避免大颗水钻;手部干燥请提前告知。指甲问题长期存在,建议就医而非用甲油遮盖。</p>
<h2>全家一起</h2>
<p>三人以上请提前几天致电 0933.528.501。可加洗发(30 分钟 99,000₫ 起,50 分钟 229,000₫ 起)。Hand Ritual 250,000₫、Foot Ritual 350,000₫、Full Ritual 550,000₫。</p>'''
bai('nail-cho-me-co-dau', T, X,
 A(('hand care manicure', 'Chăm sóc tay cho mẹ trước ngày cưới', 'Hand care before a wedding', '결혼식 전 핸드 케어', '婚礼前的手部护理'), []),
 ('Nail cho mẹ cô dâu, mẹ chú rể: mẫu trang nhã và dễ sinh hoạt',
  'Gợi ý mẫu nail cho mẹ trong ngày cưới: màu trang nhã, độ dài vừa, lưu ý khi tay khô, và cách sắp xếp một buổi cho cả nhà cùng làm.',
  'Nail cho mẹ cô dâu: mẫu trang nhã | VESSCA',
  'Nail cho mẹ cô dâu, mẹ chú rể: nude hồng, đỏ rượu vang, xà cừ ánh trai từ 130.000₫; hoặc chỉ cắt da dưỡng viền 60.000₫. VESSCA Bình Thạnh.',
  ['nail cho mẹ', 'nail đám cưới', 'nail cô dâu', 'nail trang nhã', 'làm nail cả nhà'], vi, faq),
 ("Nails for the Mothers of the Bride and Groom",
  'Elegant, practical nail choices for the mothers on a wedding day.',
  'Nails for the Mother of the Bride | VESSCA', 'Nails for the mothers on a wedding day: pink nude, burgundy, mother-of-pearl from 130,000₫, or cuticle care only 60,000₫. VESSCA, Saigon.',
  ['mother of the bride nails', 'wedding nails Saigon', 'nail salon Binh Thanh'], en,
  [('Which colours?', 'Pink or milky nude, burgundy, or mother-of-pearl.'),
   ('Can the family book together?', 'Yes; groups of three or more should call a few days ahead.')]),
 ('혼주 어머님 네일: 단정하고 편한 선택',
  '결혼식 날 어머님께 어울리는 컬러와 길이, 가족 단체 예약.',
  '혼주 어머님 네일 | 호치민 VESSCA', '결혼식 날 어머님 네일: 핑크 누드, 버건디, 자개 130,000₫부터, 큐티클 케어만 60,000₫.',
  ['혼주 네일', '호치민 웨딩 네일', '호치민 네일'], ko,
  [('어떤 컬러가 좋나요?', '핑크·밀키 누드, 버건디, 자개입니다.'),
   ('가족이 함께 예약되나요?', '네, 3인 이상은 며칠 전 연락 주세요.')]),
 ('新娘与新郎母亲的美甲:典雅又好打理',
  '婚礼当天母亲适合的颜色、长度与全家同行预约。',
  '新娘母亲的美甲 | 胡志明 VESSCA', '婚礼当天母亲的美甲:粉裸、酒红、贝壳光 130,000₫ 起,或只做修死皮 60,000₫。VESSCA。',
  ['新娘母亲 美甲', '胡志明 婚礼美甲', '平盛郡 美甲'], zh,
  [('选什么颜色?', '粉裸或奶裸、酒红、贝壳光。'),
   ('可以全家一起预约吗?', '可以,三人以上请提前几天联系。')]))

# ---------- 3. Gội đầu trước tiệc cuối năm ----------
vi = '''<p>Mùa tiệc cuối năm kéo dài từ Noel sang tất niên. Nếu bạn có buổi tiệc vào tối nay hoặc ngày mai, một buổi gội đầu ở tiệm giúp tóc vào nếp và da đầu nhẹ hơn, không cần tự xoay xở ở nhà.</p>

<h2>Chọn gói theo thời gian còn lại</h2>

<table>
<thead><tr><th>Bạn có</th><th>Gói</th><th>Giá</th></tr></thead>
<tbody>
<tr><td>30 phút trước giờ hẹn</td><td>Gói 01: gội 2 lần, xả, sấy ion âm, dầu dưỡng</td><td>99.000–149.000₫</td></tr>
<tr><td>50 phút</td><td>Gói 02: thêm tẩy tế bào chết da đầu, 2 lần massage đầu</td><td>229.000–279.000₫</td></tr>
<tr><td>50 phút, muốn chăm da mặt</td><td>Gói 03: mặt nạ Hàn Quốc, massage mặt, chiếu đèn</td><td>269.000–319.000₫</td></tr>
<tr><td>75 phút</td><td>Gói 04: gộp cả hai, thêm massage cổ vai gáy</td><td>419.000–469.000₫</td></tr>
</tbody>
</table>

<p>Ba mức giá mỗi gói ứng với ba loại dầu gội: Nguyên Xuân, gừng sả thiên nhiên, Unove Hàn Quốc. So sánh ở bài <a href="/blog/chon-dau-goi-nguyen-xuan-gung-sa-unove/">chọn dầu gội Nguyên Xuân, gừng sả hay Unove</a>.</p>

<h2>Lưu ý nếu đi tiệc ngay sau đó</h2>

<ul>
<li>Tiệm gội, xả, sấy khô bằng máy sấy ion âm và thoa dầu dưỡng; tiệm không làm tóc kiểu tiệc.</li>
<li>Nếu sẽ uốn hoặc búi tóc ở chỗ khác, hỏi thợ tóc nên gội trước bao lâu.</li>
<li>Muốn hương lưu lâu, Unove là loại có hương nước hoa; gừng sả cũng lưu hương lâu.</li>
<li>Gói 75 phút nên bắt đầu trước 19:00 vì tiệm đóng cửa 20:30.</li>
</ul>

<h2>Gộp với nail cho gọn một buổi</h2>

<p>Nếu cần cả móng lẫn tóc trước tiệc, chọn "Nail và gội đầu" khi <a href="/#booking">đặt lịch</a> để tiệm xếp liền mạch. Mẫu nail cho tiệc cuối năm có ở bài <a href="/blog/nail-di-tiec-cuoi-nam/">nail đi tiệc cuối năm</a>. Mùa này khung tối kín sớm, nên đặt trước một hai ngày.</p>'''
faq = [('Gội đầu trước tiệc nên chọn gói nào?', 'Có 30 phút thì Gói 01 từ 99.000₫; có 50 phút thì Gói 02 hoặc 03; rảnh hơn thì Gói thiên đường 75 phút.'),
       ('Tiệm có làm tóc kiểu tiệc không?', 'Không. Tiệm gội, xả, sấy bằng máy sấy ion âm và thoa dầu dưỡng tóc.'),
       ('Loại dầu gội nào lưu hương lâu?', 'Unove có hương nước hoa; gừng sả thiên nhiên cũng lưu hương lâu.')]
en = '''<p>Party season runs from Christmas through year-end. A salon hair wash before an evening out leaves hair in shape without the work at home.</p>
<h2>Pick by time</h2>
<ul><li>30 minutes: package 01, double shampoo, conditioner, ion blow-dry, hair oil (99,000–149,000₫)</li><li>50 minutes: package 02 with scalp exfoliation and two head massages (229,000–279,000₫)</li><li>50 minutes with facial care: package 03 (269,000–319,000₫)</li><li>75 minutes: the Paradise Ritual with neck and shoulder massage (419,000–469,000₫)</li></ul>
<h2>Notes</h2>
<p>The salon washes, conditions, blow-dries and oils; it does not do party styling. If someone else is styling your hair, ask them when to wash it. Unove has a perfume scent that lingers. Start the 75-minute package before 19:00; closing is 20:30.</p>
<h2>With nails</h2>
<p>Choose "Nail and hair wash" when booking to do both in one visit.</p>'''
ko = '''<p>연말 파티 시즌은 크리스마스부터 송년회까지 이어집니다. 외출 전 샵에서 머리를 감으면 집에서 따로 손질하지 않아도 모양이 잡힙니다.</p>
<h2>시간에 맞춰 고르기</h2>
<ul><li>30분: 01 코스 — 샴푸 2회, 컨디셔너, 음이온 드라이, 헤어 오일(99,000–149,000₫)</li><li>50분: 02 코스 — 두피 스케일링과 두피 마사지 2회(229,000–279,000₫)</li><li>50분 + 페이셜: 03 코스(269,000–319,000₫)</li><li>75분: 파라다이스 리추얼, 목·어깨 마사지 포함(419,000–469,000₫)</li></ul>
<h2>참고</h2>
<p>샴푸, 컨디셔너, 드라이, 오일까지만 진행하며 파티 스타일링은 하지 않습니다. 다른 곳에서 헤어를 하신다면 언제 감을지 문의해 보세요. 어노브는 향이 오래갑니다. 75분 코스는 20:30 마감 전에 끝나도록 19:00 전에 시작해 주세요.</p>'''
zh = '''<p>年末派对季从圣诞延续到尾牙。出门前在店里洗个头,头发自然成型,省去在家折腾。</p>
<h2>按时间选择</h2>
<ul><li>30 分钟:套餐 01——洗发两次、护发素、负离子吹干、护发油(99,000–149,000₫)</li><li>50 分钟:套餐 02——头皮去角质与两次头部按摩(229,000–279,000₫)</li><li>50 分钟含面部护理:套餐 03(269,000–319,000₫)</li><li>75 分钟:天堂套餐,含肩颈按摩(419,000–469,000₫)</li></ul>
<h2>提醒</h2>
<p>店内只做洗、护、吹干与护发油,不做派对造型。若在别处做造型,请先询问何时洗头。Unove 香气持久。75 分钟套餐建议 19:00 前开始,店里 20:30 关门。</p>'''
bai('goi-dau-truoc-tiec-cuoi-nam', T, G,
 A(('hair wash salon', 'Gội đầu ở tiệm trước buổi tiệc', 'A salon hair wash before a party', '파티 전 샵에서 샴푸', '派对前在店里洗发'), []),
 ('Gội đầu trước tiệc cuối năm: chọn gói theo thời gian bạn có',
  'Mùa tiệc Noel và tất niên: chọn gói gội đầu 30, 50 hay 75 phút, lưu ý nếu làm tóc kiểu ở nơi khác và cách gộp chung với nail.',
  'Gội đầu trước tiệc cuối năm từ 99.000₫ | VESSCA',
  'Gội đầu trước tiệc Noel, tất niên: gói 30 phút từ 99.000₫, 50 phút từ 229.000₫, 75 phút từ 419.000₫. VESSCA Bình Thạnh, mở đến 20:30.',
  ['gội đầu trước tiệc', 'gội đầu cuối năm', 'gội đầu thư giãn', 'gội đầu Bình Thạnh', 'gội đầu Noel'], vi, faq),
 ('A Hair Wash Before a Year-End Party: Pick by Time',
  'Choosing a 30, 50 or 75-minute package before an evening out.',
  'Hair Wash Before a Party | VESSCA', 'A hair wash before Christmas and year-end parties in Saigon: 30 minutes from 99,000₫, 75 minutes from 419,000₫. Open to 20:30.',
  ['head spa Saigon', 'hair wash before party', 'head spa Binh Thanh'], en,
  [('Which package before a party?', '30 minutes: package 01 from 99,000₫; 50 minutes: package 02 or 03; 75 minutes: the Paradise Ritual.'),
   ('Do you do party styling?', 'No — washing, conditioning, blow-drying and hair oil only.')]),
 ('연말 파티 전 샴푸: 시간에 맞춰 고르기',
  '외출 전 30·50·75분 코스 고르기와 참고사항.',
  '파티 전 헤드 스파 | 호치민 VESSCA', '호치민 크리스마스·송년 파티 전 샴푸: 30분 99,000₫부터, 75분 419,000₫부터. 20:30까지 영업.',
  ['호치민 헤드스파', '파티 전 샴푸', '빈탄 헤드스파'], ko,
  [('어느 코스가 좋나요?', '30분이면 01 코스 99,000₫부터, 50분이면 02·03 코스, 75분이면 파라다이스 리추얼.'),
   ('파티 스타일링도 하나요?', '아니요, 샴푸·컨디셔너·드라이·오일까지만 합니다.')]),
 ('年末派对前洗发:按时间选套餐',
  '出门前选择 30、50 或 75 分钟套餐的建议。',
  '派对前洗发 | 胡志明 VESSCA', '胡志明圣诞与尾牙派对前洗发:30 分钟 99,000₫ 起,75 分钟 419,000₫ 起,营业至 20:30。',
  ['胡志明 洗发', '派对前 洗发', '平盛郡 洗发'], zh,
  [('该选哪个套餐?', '30 分钟选套餐 01,99,000₫ 起;50 分钟选 02 或 03;75 分钟选天堂套餐。'),
   ('做派对造型吗?', '不做,只提供洗、护、吹干与护发油。')]))

# ---------- 4. Head spa là gì ----------
vi = '''<p>"Head spa" là cách gọi phổ biến cho dịch vụ chăm sóc da đầu và tóc tại tiệm, thường gồm làm sạch da đầu, gội, massage và sấy. Ở Việt Nam, dịch vụ tương tự hay được gọi là gội đầu dưỡng sinh hoặc gội đầu thư giãn.</p>

<h2>Head spa khác gội đầu thường thế nào</h2>

<table>
<thead><tr><th></th><th>Gội đầu thường</th><th>Head spa tại tiệm</th></tr></thead>
<tbody>
<tr><td>Thời lượng</td><td>10–15 phút</td><td>30–75 phút</td></tr>
<tr><td>Làm sạch da đầu</td><td>Gội là chính</td><td>Có thể thêm bước tẩy tế bào chết da đầu</td></tr>
<tr><td>Massage</td><td>Ngắn</td><td>Massage đầu, có gói thêm cổ vai gáy</td></tr>
<tr><td>Chăm da mặt</td><td>Không</td><td>Tuỳ gói: mặt nạ, massage mặt, chiếu đèn</td></tr>
</tbody>
</table>

<h2>Head spa ở VESSCA gồm bước nào</h2>

<p>Mọi gói đều bắt đầu bằng tẩy trang Garnier và rửa mặt SVR, sau đó gội hai lần, xả, sấy bằng máy sấy ion âm và thoa dầu dưỡng tóc L'Oréal, kết thúc bằng nước uống và bánh ngọt. Tuỳ gói sẽ thêm tẩy tế bào chết da đầu, mặt nạ mắt, mặt nạ Hàn Quốc, massage mặt, chiếu đèn ánh sáng sinh học và massage cổ vai gáy.</p>

<ul>
<li>Gói 01 · 30 phút · 99.000–149.000₫</li>
<li>Gói 02 · 50 phút · 229.000–279.000₫</li>
<li>Gói 03 · 50 phút · 269.000–319.000₫</li>
<li>Gói 04 · 75 phút · 419.000–469.000₫</li>
</ul>

<p>Ba mức giá ứng với ba loại dầu gội bạn chọn. Menu từng bước có ở trang <a href="/goi-dau/">menu gội đầu</a>.</p>

<h2>Điều head spa làm được và không làm được</h2>

<p>Đây là dịch vụ chăm sóc và thư giãn. Sau buổi gội, tóc sạch, vào nếp hơn và nhiều người thấy dễ chịu. Nhưng head spa không phải điều trị y tế: gàu nặng kéo dài, rụng tóc bất thường, da đầu viêm hay đau thì nên đi khám bác sĩ da liễu. Nếu bạn từng dị ứng mỹ phẩm chăm sóc tóc, hãy báo trước cho kỹ thuật viên.</p>

<h2>Bao lâu nên đi một lần</h2>

<p>Tuỳ nhu cầu và tình trạng da đầu, không có con số chung. Nhiều khách đi khi thấy da đầu bí bách hoặc muốn nghỉ ngơi sau tuần làm việc dài. Đặt lịch ở mục <a href="/#booking">Đặt lịch</a>, chọn "Gội đầu thư giãn". Bảng giá bốn gói có ở bài <a href="/blog/goi-dau-thu-gian-binh-thanh/">gội đầu thư giãn ở Bình Thạnh</a>.</p>'''
faq = [('Head spa là gì?', 'Là dịch vụ chăm sóc da đầu và tóc tại tiệm, gồm làm sạch, gội, massage và sấy; ở Việt Nam hay gọi là gội đầu dưỡng sinh.'),
       ('Head spa khác gội đầu thường ra sao?', 'Dài hơn (30–75 phút), có massage kỹ hơn, có thể thêm tẩy tế bào chết da đầu và chăm sóc da mặt.'),
       ('Head spa có trị gàu, rụng tóc không?', 'Không. Đây là dịch vụ chăm sóc; vấn đề kéo dài nên khám bác sĩ da liễu.'),
       ('Giá head spa ở VESSCA bao nhiêu?', 'Từ 99.000₫ cho gói 30 phút đến 469.000₫ cho gói 75 phút.')]
en = '''<p>"Head spa" usually means a salon treatment for the scalp and hair: cleansing, shampoo, massage and blow-dry. In Vietnam the same idea is often called gội đầu dưỡng sinh.</p>
<h2>How it differs from a quick wash</h2>
<p>A normal wash takes 10–15 minutes; a head spa takes 30–75. It can add scalp exfoliation, a longer massage and, depending on the package, facial care.</p>
<h2>At VESSCA</h2>
<p>Every package starts with make-up removal and a cleanse, then a double shampoo, conditioner, an ion blow-dry and hair oil, ending with a drink and a sweet treat. Packages: 30 min 99,000–149,000₫; 50 min 229,000–279,000₫; 50 min with facial care 269,000–319,000₫; 75 min 419,000–469,000₫.</p>
<h2>What it is not</h2>
<p>It is care and relaxation, not medical treatment. For persistent dandruff, unusual hair loss or a sore scalp, see a dermatologist. Mention any cosmetic allergy before starting.</p>'''
ko = '''<p>"헤드 스파"는 보통 두피와 모발을 관리하는 살롱 서비스를 뜻합니다. 클렌징, 샴푸, 마사지, 드라이가 포함되며 베트남에서는 gội đầu dưỡng sinh이라고도 부릅니다.</p>
<h2>일반 샴푸와의 차이</h2>
<p>일반 샴푸는 10–15분, 헤드 스파는 30–75분입니다. 두피 스케일링과 긴 마사지, 코스에 따라 페이셜 케어가 더해집니다.</p>
<h2>VESSCA의 구성</h2>
<p>모든 코스는 클렌징과 세안으로 시작해 샴푸 2회, 컨디셔너, 음이온 드라이, 헤어 오일로 이어지고 음료와 디저트로 마무리합니다. 30분 99,000–149,000₫, 50분 229,000–279,000₫, 페이셜 포함 50분 269,000–319,000₫, 75분 419,000–469,000₫.</p>
<h2>치료는 아닙니다</h2>
<p>케어와 휴식을 위한 서비스입니다. 비듬이 오래가거나 탈모, 두피 통증이 있으면 피부과 진료를 받으세요.</p>'''
zh = '''<p>"头皮 SPA"通常指店内的头皮与头发护理:清洁、洗发、按摩与吹干。在越南,类似服务常被称为"养生洗发"。</p>
<h2>与普通洗头的差别</h2>
<p>普通洗头 10–15 分钟,头皮 SPA 为 30–75 分钟,可加头皮去角质、更长的按摩,部分套餐还含面部护理。</p>
<h2>VESSCA 的流程</h2>
<p>每个套餐都从卸妆洁面开始,接着洗发两次、护发素、负离子吹干、护发油,最后奉上饮品与甜点。30 分钟 99,000–149,000₫;50 分钟 229,000–279,000₫;含面部护理 50 分钟 269,000–319,000₫;75 分钟 419,000–469,000₫。</p>
<h2>它不是治疗</h2>
<p>这是护理与放松服务。头皮屑久治不退、异常脱发或头皮疼痛,请就医。</p>'''
bai('head-spa-la-gi', T, G,
 A(('scalp massage', 'Chăm sóc da đầu tại tiệm', 'Scalp care at a salon', '샵에서 받는 두피 케어', '店内头皮护理'), []),
 ('Head spa là gì, khác gội đầu thường ra sao',
  'Head spa gồm những bước nào, khác gội đầu thường thế nào, bốn gói tại VESSCA và điều dịch vụ này không làm được.',
  'Head spa là gì, khác gội đầu thường ra sao | VESSCA',
  'Head spa là dịch vụ chăm sóc da đầu và tóc 30–75 phút, có massage, tuỳ gói thêm chăm da mặt. Tại VESSCA từ 99.000₫ đến 469.000₫.',
  ['head spa là gì', 'head spa', 'gội đầu dưỡng sinh', 'chăm sóc da đầu', 'gội đầu thư giãn'], vi, faq),
 ('What a Head Spa Is, and How It Differs from a Quick Wash',
  'What a head spa includes, how it differs from a normal wash and what it cannot do.',
  'What Is a Head Spa | VESSCA Saigon', 'A head spa is a 30–75 minute scalp and hair treatment with massage. At VESSCA in Saigon, 99,000–469,000₫.',
  ['what is a head spa', 'head spa Saigon', 'scalp treatment Saigon'], en,
  [('What is a head spa?', 'A salon treatment for scalp and hair: cleansing, shampoo, massage and blow-dry.'),
   ('Does it treat dandruff or hair loss?', 'No. See a dermatologist for persistent problems.')]),
 ('헤드 스파란 무엇이고 일반 샴푸와 어떻게 다른가',
  '헤드 스파의 구성, 일반 샴푸와의 차이, 한계.',
  '헤드 스파란 | 호치민 VESSCA', '헤드 스파는 마사지를 포함한 30–75분 두피·모발 관리입니다. 호치민 VESSCA에서 99,000–469,000₫.',
  ['헤드스파란', '호치민 헤드스파', '두피 관리'], ko,
  [('헤드 스파란?', '클렌징, 샴푸, 마사지, 드라이를 포함한 두피·모발 관리입니다.'),
   ('비듬이나 탈모가 좋아지나요?', '아니요, 오래가면 피부과 진료를 받으세요.')]),
 ('什么是头皮 SPA,与普通洗头有何不同',
  '头皮 SPA 包含什么、与普通洗头的差别,以及它做不到的事。',
  '什么是头皮 SPA | 胡志明 VESSCA', '头皮 SPA 是含按摩的 30–75 分钟头皮与头发护理。胡志明 VESSCA,99,000–469,000₫。',
  ['什么是头皮SPA', '胡志明 头皮护理', '胡志明 洗发'], zh,
  [('什么是头皮 SPA?', '店内的头皮与头发护理:清洁、洗发、按摩与吹干。'),
   ('能治头皮屑或脱发吗?', '不能,问题持续请就医。')]))
