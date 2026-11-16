"""Đợt 16/11/2026 (batch 4) — tiệc cuối năm, giao thừa, gội đầu."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
X, G = 'Xu hướng & Cảm hứng', 'Gội đầu & Thư giãn'
T = '2026-11-16T12:00:00+07:00'

# 1. Nail đi tiệc tất niên công ty
vi = '''<p>Tiệc tất niên công ty là dịp hơi khác tiệc bạn bè: vẫn muốn nổi một chút, nhưng hôm sau đi làm vẫn phải hợp. Bài này gợi ý hướng chọn mẫu để dùng được cả hai.</p>

<h2>Nguyên tắc chọn</h2>

<ul>
<li>Chọn màu dùng tiếp được sang tuần sau, thay vì mẫu chỉ hợp một tối.</li>
<li>Độ dài vừa phải để còn gõ phím, cầm giấy tờ.</li>
<li>Hiệu ứng thay cho hoạ tiết: mắt mèo, nhũ mịn, tráng gương nổi dưới đèn mà vẫn gọn.</li>
</ul>

<h2>Bốn mẫu an toàn</h2>

<table>
<thead><tr><th>Mẫu</th><th>Vì sao hợp</th><th>Giá</th></tr></thead>
<tbody>
<tr><td>Mắt mèo đỏ rượu vang</td><td>Bắt đèn, nhưng vẫn kín đáo ban ngày</td><td>170.000₫</td></tr>
<tr><td>Nude sữa, một móng nhũ</td><td>Nhẹ nhất, đi làm vẫn hợp</td><td>130.000₫ + 10.000₫</td></tr>
<tr><td>Xanh navy trơn</td><td>Trầm, sang, ít gặp</td><td>130.000₫</td></tr>
<tr><td>Tráng gương bạc một móng</td><td>Điểm nhấn gọn</td><td>130.000₫ + từ 15.000₫</td></tr>
</tbody>
</table>

<h2>Nếu công ty có quy định</h2>

<p>Một số nơi yêu cầu móng ngắn, màu nhạt. Khi đó chọn nude, be sữa hoặc thạch trong, điểm nhũ mịn là đủ cho buổi tiệc. Gợi ý cho môi trường công sở có ở bài <a href="/blog/nail-cong-so-kin-dao/">nail công sở kín đáo</a>.</p>

<h2>Làm trước tiệc mấy ngày</h2>

<p>Làm trước 1–3 ngày là vừa. Nếu tiệc vào cuối tuần, đặt lịch sớm vì khung tối và cuối tuần thường kín trước. Bảo hành 5 ngày. Mẫu tiệc khác có ở bài <a href="/blog/nail-di-tiec-cuoi-nam/">nail đi tiệc cuối năm</a>. Đặt lịch ở mục <a href="/#booking">Đặt lịch</a> hoặc gọi 0933.528.501.</p>'''
faq=[('Nail đi tiệc tất niên nên chọn gì?','Mắt mèo đỏ rượu vang, nude điểm nhũ, navy trơn hoặc tráng gương một móng.'),
('Công ty yêu cầu móng nhạt thì sao?','Chọn nude, be sữa hoặc thạch trong, điểm nhũ mịn.'),
('Nên làm trước mấy ngày?','1–3 ngày trước tiệc; bảo hành 5 ngày.')]
en='''<p>A company year-end party is not quite a night out with friends: you want a little shine, but it still has to work at the desk on Monday.</p>
<h2>How to choose</h2>
<p>Pick a colour you can keep wearing next week, a workable length, and effects rather than motifs — cat-eye, fine shimmer or chrome read well under party lights and stay tidy by day.</p>
<h2>Four safe looks</h2>
<ul><li>Burgundy cat-eye (170,000₫)</li><li>Milky nude with one shimmer nail (130,000₫ + 10,000₫)</li><li>Plain navy (130,000₫)</li><li>One chrome accent nail (130,000₫ + from 15,000₫)</li></ul>
<p>If your office asks for short, pale nails, nude or clear jelly with fine shimmer is enough. Book 1–3 days ahead; evenings and weekends fill first. Five-day guarantee.</p>'''
ko='''<p>회사 송년회는 친구들과의 모임과 조금 다릅니다. 적당히 화사하면서도 월요일 출근에 무리가 없어야 합니다.</p>
<h2>선택 기준</h2>
<p>다음 주에도 쓸 수 있는 컬러, 일하기 편한 길이, 모티프보다 효과(자석, 고운 펄, 크롬)를 고르면 조명 아래서 예쁘고 낮에도 단정합니다.</p>
<h2>무난한 네 가지</h2>
<ul><li>버건디 자석 네일(170,000₫)</li><li>밀키 누드에 펄 포인트 하나(130,000₫ + 10,000₫)</li><li>네이비 원컬러(130,000₫)</li><li>크롬 포인트 한 손톱(130,000₫ + 15,000₫부터)</li></ul>
<p>회사에서 짧고 연한 네일을 요구한다면 누드나 클리어 젤리에 고운 펄이면 충분합니다. 1–3일 전 예약, 5일 보증.</p>'''
zh='''<p>公司尾牙和朋友聚会不太一样:想亮一点,但周一上班也要合适。</p>
<h2>挑选原则</h2>
<p>选下周还能继续戴的颜色、方便工作的长度,以及效果而非图案——猫眼、细闪或镜面在灯下好看,白天也干净。</p>
<h2>四款稳妥选择</h2>
<ul><li>酒红猫眼(170,000₫)</li><li>奶裸色加一指闪粉(130,000₫ + 10,000₫)</li><li>纯色藏青(130,000₫)</li><li>一指镜面点缀(130,000₫ + 15,000₫ 起)</li></ul>
<p>若公司要求短且浅色,裸色或果冻透明加细闪就够。建议提前 1–3 天预约,保修 5 天。</p>'''
bai('nail-tat-nien-cong-ty',T,X,
 A(('navy gel nails manicure','Nail đi tiệc tất niên công ty','Nails for a company year-end party','회사 송년회 네일','公司尾牙美甲'),[]),
 ('Nail đi tiệc tất niên công ty: bốn mẫu dùng được cả hôm sau',
  'Tiệc tất niên cần nổi vừa đủ mà hôm sau đi làm vẫn hợp. Nguyên tắc chọn, bốn mẫu an toàn kèm giá và cách xử lý khi công ty có quy định.',
  'Nail đi tiệc tất niên công ty: 4 mẫu | VESSCA',
  'Nail đi tiệc tất niên: mắt mèo đỏ rượu vang 170.000₫, nude điểm nhũ, navy trơn, tráng gương một móng. VESSCA Bình Thạnh, bảo hành 5 ngày.',
  ['nail tất niên','nail đi tiệc','nail công sở','nail cuối năm','nail tiệc công ty'],vi,faq),
 ('Nails for a Company Year-End Party: Four Safe Looks',
  'A little shine for the party that still works at the desk on Monday.',
  'Nails for a Year-End Party | VESSCA','Nails for a company year-end party in Saigon: burgundy cat-eye 170,000₫, milky nude with shimmer, navy, a chrome accent. VESSCA.',
  ['party nails Saigon','office nails','nail salon Saigon'],en,
  [('What suits a company party?','Burgundy cat-eye, milky nude with shimmer, plain navy or one chrome nail.'),('When to book?','1–3 days ahead; evenings fill first.')]),
 ('회사 송년회 네일: 무난한 네 가지',
  '파티에도 어울리고 출근에도 무리 없는 선택.',
  '송년회 네일 | 호치민 VESSCA','호치민 회사 송년회 네일: 버건디 자석 170,000₫, 밀키 누드 펄, 네이비, 크롬 포인트.',
  ['송년회 네일','오피스 네일','호치민 네일'],ko,
  [('어떤 디자인이 좋나요?','버건디 자석, 밀키 누드 펄, 네이비, 크롬 포인트입니다.'),('언제 예약하나요?','1–3일 전이 좋습니다.')]),
 ('公司尾牙美甲:四款稳妥选择',
  '派对够亮,周一上班也合适。',
  '尾牙美甲 | 胡志明 VESSCA','胡志明公司尾牙美甲:酒红猫眼 170,000₫、奶裸加闪粉、纯色藏青、一指镜面。VESSCA。',
  ['尾牙 美甲','上班 美甲','胡志明 美甲'],zh,
  [('尾牙适合什么?','酒红猫眼、奶裸加闪粉、纯色藏青或一指镜面。'),('提前多久做?','提前 1–3 天,晚上时段先满。')]))

# 2. Nail đêm giao thừa
vi = '''<p>Đêm 31/12 là dịp nhiều người chịu chơi hơn với móng tay: ánh kim, kim tuyến, hiệu ứng bắt sáng đều hợp khung cảnh pháo hoa và đèn đêm.</p>

<h2>Bốn hướng cho đêm giao thừa</h2>

<table>
<thead><tr><th>Hướng</th><th>Mô tả</th><th>Giá</th></tr></thead>
<tbody>
<tr><td>Kim tuyến phủ</td><td>Lấp lánh rõ, lên ảnh đêm rất bắt</td><td>Từ 130.000₫ tuỳ dòng sơn</td></tr>
<tr><td>Tráng gương bạc</td><td>Mặt móng như gương, phản chiếu đèn</td><td>130.000₫ + từ 15.000₫</td></tr>
<tr><td>Mắt mèo ngân hà</td><td>Dải sáng chạy giữa nền tối</td><td>170.000₫</td></tr>
<tr><td>Xà cừ ánh trai</td><td>Ánh ngọc trai, nhẹ hơn kim tuyến</td><td>280.000₫</td></tr>
</tbody>
</table>

<h2>Chụp ảnh ban đêm thì chọn gì</h2>

<p>Dưới ánh đèn vàng, tông đỏ và vàng kim lên ấm; dưới đèn trắng, bạc và xanh lạnh rõ hơn. Nếu bạn hay chụp cận tay cầm ly, mặt móng bóng và sạch quan trọng hơn hoạ tiết cầu kỳ.</p>

<h2>Tính luôn lịch sau Tết dương</h2>

<p>Nếu đã làm mẫu đậm cho đêm giao thừa, hãy tính trước thời điểm tháo gel (30.000₫) để kịp đổi mẫu nhẹ nhàng hơn cho những tuần sau. Mẫu cho năm mới có ở bài <a href="/blog/nail-don-nam-moi-2027/">nail đón năm mới 2027</a>. Đặt lịch ở mục <a href="/#booking">Đặt lịch</a>; khung tối 30 và 31/12 thường kín rất sớm.</p>'''
faq=[('Nail đêm giao thừa nên làm gì?','Kim tuyến phủ, tráng gương bạc, mắt mèo nền tối hoặc xà cừ ánh trai.'),
('Giá bao nhiêu?','Sơn gel từ 130.000₫, mắt mèo 170.000₫, xà cừ ánh trai 280.000₫, tráng gương từ 15.000₫.'),
('Đặt lịch ngày 30, 31/12 có khó không?','Khung tối hai ngày này thường kín rất sớm, nên đặt trước.')]
en='''<p>New Year's Eve is when people go brighter: metallics, glitter and light-catching effects all suit fireworks and night lights.</p>
<h2>Four directions</h2>
<ul><li>Full glitter — the most festive in night photos (from 130,000₫ depending on the line)</li><li>Silver chrome — a mirror finish (130,000₫ + from 15,000₫)</li><li>Galaxy cat-eye — a bright band over a dark base (170,000₫)</li><li>Mother-of-pearl — softer than glitter (280,000₫)</li></ul>
<h2>For night photos</h2>
<p>Warm lighting flatters red and gold; cool white lighting suits silver and icy blue. For close-ups holding a glass, a clean glossy surface matters more than busy art.</p>
<p>Plan the removal (30,000₫) if you want something lighter in January. The 30th and 31st fill up very early.</p>'''
ko='''<p>12월 31일 밤에는 조금 더 화려하게 가는 분이 많습니다. 메탈릭, 글리터, 빛을 받는 효과가 불꽃놀이와 야경에 잘 어울립니다.</p>
<h2>네 가지 방향</h2>
<ul><li>글리터 풀 — 야경 사진에서 가장 화려(라인에 따라 130,000₫부터)</li><li>실버 크롬 — 거울 같은 마감(130,000₫ + 15,000₫부터)</li><li>갤럭시 자석 — 어두운 베이스 위 빛나는 띠(170,000₫)</li><li>자개 — 글리터보다 은은(280,000₫)</li></ul>
<h2>야간 촬영이라면</h2>
<p>따뜻한 조명에는 레드와 골드, 차가운 조명에는 실버와 블루가 잘 맞습니다. 잔을 든 클로즈업에는 화려한 아트보다 깨끗한 광택이 중요합니다.</p>
<p>1월에 가볍게 바꾸실 거라면 제거(30,000₫) 일정도 함께 생각해 두세요. 12월 30–31일은 매우 일찍 마감됩니다.</p>'''
zh='''<p>跨年夜大家会更放得开:金属色、亮片与反光效果都很配烟花和夜景。</p>
<h2>四种方向</h2>
<ul><li>满版亮片——夜景照片最出彩(依系列 130,000₫ 起)</li><li>银色镜面——镜面质感(130,000₫ + 15,000₫ 起)</li><li>星空猫眼——深色底上的亮带(170,000₫)</li><li>贝壳光——比亮片柔和(280,000₫)</li></ul>
<h2>夜间拍照</h2>
<p>暖光下红与金更好看,冷白光下银与冰蓝更出色。举杯特写时,干净的光泽比复杂图案更重要。</p>
<p>若一月想换清淡款,记得预留卸甲时间(30,000₫)。12 月 30、31 日的时段很早就满。</p>'''
bai('nail-dem-giao-thua',T,X,
 A(('dark glitter nails manicure','Nail ánh kim cho đêm giao thừa','Metallic nails for New Year’s Eve','연말 파티용 메탈릭 네일','跨年夜的金属色美甲'),[]),
 ('Nail đêm giao thừa: bốn hướng bắt sáng cho đêm 31/12',
  'Kim tuyến, tráng gương, mắt mèo ngân hà hay xà cừ: chọn mẫu nào cho đêm giao thừa, lưu ý khi chụp ảnh đêm và lịch tháo gel sau đó.',
  'Nail đêm giao thừa: 4 hướng bắt sáng | VESSCA',
  'Nail đêm giao thừa 31/12: kim tuyến phủ, tráng gương bạc, mắt mèo ngân hà, xà cừ ánh trai. Từ 130.000₫ tại VESSCA Bình Thạnh.',
  ['nail giao thừa','nail đêm 31/12','nail đi tiệc','nail kim tuyến','nail cuối năm'],vi,faq),
 ("New Year's Eve Nails: Four Light-Catching Directions",
  'Glitter, chrome, galaxy cat-eye or mother-of-pearl for 31 December.',
  "New Year's Eve Nails | VESSCA Saigon","New Year's Eve nails in Saigon: full glitter, silver chrome, galaxy cat-eye or mother-of-pearl. From 130,000₫. VESSCA.",
  ['new years eve nails','glitter nails','nail salon Saigon'],en,
  [('What suits the night?','Full glitter, silver chrome, galaxy cat-eye or mother-of-pearl.'),('Is 31 December busy?','Yes, evening slots fill very early.')]),
 ('연말 파티 네일: 빛을 받는 네 가지',
  '글리터, 크롬, 갤럭시 자석, 자개 중 고르기.',
  '연말 파티 네일 | 호치민 VESSCA','호치민 연말 파티 네일: 글리터, 실버 크롬, 갤럭시 자석, 자개. 130,000₫부터.',
  ['연말 네일','글리터 네일','호치민 네일'],ko,
  [('어떤 디자인이 좋나요?','글리터, 실버 크롬, 갤럭시 자석, 자개입니다.'),('12월 31일은 붐비나요?','저녁 시간은 매우 일찍 마감됩니다.')]),
 ('跨年夜美甲:四种会反光的选择',
  '亮片、镜面、星空猫眼或贝壳光。',
  '跨年夜美甲 | 胡志明 VESSCA','胡志明跨年夜美甲:满版亮片、银色镜面、星空猫眼、贝壳光,130,000₫ 起。VESSCA。',
  ['跨年 美甲','亮片美甲','胡志明 美甲'],zh,
  [('跨年适合什么?','满版亮片、银色镜面、星空猫眼或贝壳光。'),('12 月 31 日好约吗?','晚间时段很早就满。')]))

# 3. Gội đầu cho tóc khô xơ
vi = '''<p>Tóc khô, xơ, chẻ ngọn thường là hệ quả của nhiều yếu tố cộng lại: nắng, nhuộm uốn, sấy nhiệt cao, gội bằng nước quá nóng. Bài này nói về cách chăm ở nhà và gói gội đầu phù hợp.</p>

<h2>Những thói quen nên đổi</h2>

<ul>
<li>Gội bằng nước ấm vừa thay vì nước nóng.</li>
<li>Thoa dầu xả từ giữa thân tóc xuống ngọn, để đủ thời gian rồi xả kỹ.</li>
<li>Sấy ở nhiệt vừa, giữ máy cách tóc một khoảng, sấy theo chiều từ chân xuống ngọn.</li>
<li>Che nắng khi ra đường lâu.</li>
<li>Cắt bỏ phần ngọn chẻ thay vì cố dưỡng phần đã hỏng.</li>
</ul>

<h2>Gói gội đầu phù hợp</h2>

<table>
<thead><tr><th>Lựa chọn</th><th>Vì sao</th><th>Giá</th></tr></thead>
<tbody>
<tr><td>Gói 01 với Unove</td><td>Dầu gội xả dưỡng chất chuyên sâu, menu gợi ý cho tóc nhuộm, uốn, hư tổn</td><td>149.000₫</td></tr>
<tr><td>Gói 02 với Nguyên Xuân bản xanh lá</td><td>Menu gợi ý bản xanh lá cho tóc khô, hư tổn, kèm massage da đầu</td><td>229.000₫</td></tr>
<tr><td>Gói 04 · 75 phút</td><td>Chăm kỹ cả da đầu và da mặt, có massage cổ vai gáy</td><td>419.000–469.000₫</td></tr>
</tbody>
</table>

<p>Mọi gói đều kết thúc bằng sấy máy sấy ion âm và thoa dầu dưỡng tóc L'Oréal. So sánh ba loại dầu gội ở bài <a href="/blog/chon-dau-goi-nguyen-xuan-gung-sa-unove/">chọn dầu gội Nguyên Xuân, gừng sả hay Unove</a>.</p>

<h2>Điều một buổi gội không làm được</h2>

<p>Gội đầu ở tiệm giúp tóc sạch, mềm và vào nếp hơn, nhưng không phục hồi được phần tóc đã hư tổn nặng hay chẻ ngọn. Nếu tóc rụng nhiều bất thường hoặc da đầu có vấn đề kéo dài, nên đi khám bác sĩ da liễu. Bài viết chỉ mang tính tham khảo.</p>

<p>Đặt lịch ở mục <a href="/#booking">Đặt lịch</a>, chọn "Gội đầu thư giãn".</p>'''
faq=[('Tóc khô xơ nên chọn dầu gội nào ở tiệm?','Menu gợi ý Unove cho tóc nhuộm, uốn, hư tổn; Nguyên Xuân bản xanh lá cho tóc khô.'),
('Gội đầu ở tiệm có phục hồi được tóc hư tổn không?','Không phục hồi phần đã hỏng; giúp tóc sạch, mềm và vào nếp hơn.'),
('Giá bao nhiêu?','Gói 30 phút với Unove 149.000₫; Gói 50 phút từ 229.000₫; Gói 75 phút từ 419.000₫.')]
en='''<p>Dry, brittle hair usually comes from several things at once: sun, colouring and perms, high heat drying and water that is too hot.</p>
<h2>Habits worth changing</h2>
<p>Wash with warm rather than hot water; keep conditioner to mid-length and ends and rinse well; dry on medium heat at a distance, from roots down; cover hair in strong sun; and trim split ends rather than trying to repair them.</p>
<h2>Which package</h2>
<ul><li>Package 01 with Unove (149,000₫) — the menu suggests it for coloured, permed or damaged hair</li><li>Package 02 with green Nguyen Xuan (229,000₫) — suggested for dry hair, with scalp massage</li><li>Package 04 (419,000–469,000₫) — 75 minutes including neck and shoulder massage</li></ul>
<p>Every package finishes with an ion blow-dry and L'Oréal hair oil. A salon wash cannot repair badly damaged ends; see a dermatologist for unusual hair loss.</p>'''
ko='''<p>건조하고 푸석한 모발은 보통 햇빛, 염색·펌, 높은 온도의 드라이, 너무 뜨거운 물이 겹쳐 생깁니다.</p>
<h2>바꾸면 좋은 습관</h2>
<p>뜨거운 물 대신 미온수로 감기, 컨디셔너는 중간 길이부터 끝까지 바르고 충분히 헹구기, 중간 온도로 거리를 두고 뿌리에서 끝 방향으로 말리기, 강한 햇빛 가리기, 갈라진 끝은 다듬기.</p>
<h2>추천 코스</h2>
<ul><li>어노브 01 코스(149,000₫) — 염색·펌·손상 모발에 추천</li><li>응우옌 쑤언 그린 02 코스(229,000₫) — 건조 모발용, 두피 마사지 포함</li><li>04 코스(419,000–469,000₫) — 75분, 목·어깨 마사지 포함</li></ul>
<p>모든 코스는 음이온 드라이와 로레알 헤어 오일로 마무리합니다. 심하게 손상된 끝은 복구되지 않으며, 탈모가 심하면 진료를 받으세요.</p>'''
zh='''<p>干燥毛躁多半是多种因素叠加:日晒、染烫、高温吹干、水温过热。</p>
<h2>值得调整的习惯</h2>
<p>用温水而非热水;护发素涂中段至发尾并冲洗干净;中温、保持距离、由发根向发尾吹;强日晒时遮挡;分叉的发尾直接剪掉。</p>
<h2>合适的套餐</h2>
<ul><li>Unove 套餐 01(149,000₫)——价目表建议用于染烫、受损发质</li><li>Nguyen Xuan 绿色款套餐 02(229,000₫)——适合干燥发质,含头皮按摩</li><li>套餐 04(419,000–469,000₫)——75 分钟,含肩颈按摩</li></ul>
<p>所有套餐都以负离子吹干与 L'Oréal 护发油收尾。店内洗发无法修复已严重受损的发尾;异常脱发请就医。</p>'''
bai('goi-dau-cho-toc-kho-xo',T,G,
 A(('hair wash salon','Chăm sóc tóc khô xơ tại tiệm','Salon care for dry hair','건조 모발 케어','干燥发质的店内护理'),[]),
 ('Tóc khô xơ: thói quen nên đổi và gói gội đầu phù hợp',
  'Tóc khô, chẻ ngọn do đâu, những thói quen nên đổi ở nhà, gói gội đầu và loại dầu gội menu gợi ý, cùng điều một buổi gội không làm được.',
  'Tóc khô xơ: cách chăm và gói gội đầu | VESSCA',
  'Tóc khô xơ chẻ ngọn: thói quen nên đổi và gói gội đầu phù hợp. Gói 30 phút với Unove 149.000₫, gói 50 phút từ 229.000₫. VESSCA Bình Thạnh.',
  ['tóc khô xơ','chăm sóc tóc hư tổn','gội đầu dưỡng tóc','dầu gội Unove','gội đầu thư giãn'],vi,faq),
 ('Dry, Brittle Hair: What to Change and Which Package Helps',
  'Habits worth changing at home and the salon packages suggested for dry or damaged hair.',
  'Dry Hair Care & Head Spa | VESSCA','Dry, brittle hair: habits to change and which head spa package helps. Unove package 149,000₫, 50-minute packages from 229,000₫. VESSCA.',
  ['dry hair care','damaged hair treatment Saigon','head spa Saigon'],en,
  [('Which shampoo?','The menu suggests Unove for coloured, permed or damaged hair.'),('Can it repair damage?','No; it cleans and softens but cannot repair badly damaged ends.')]),
 ('건조하고 푸석한 모발: 습관과 추천 코스',
  '집에서 바꿀 습관과 건조·손상 모발에 추천하는 코스.',
  '건조 모발 케어 | 호치민 VESSCA','건조하고 푸석한 모발: 바꿀 습관과 추천 코스. 어노브 코스 149,000₫, 50분 코스 229,000₫부터.',
  ['건조 모발','손상모 케어','호치민 헤드스파'],ko,
  [('어떤 샴푸인가요?','염색·펌·손상 모발에는 어노브를 추천합니다.'),('손상이 복구되나요?','아니요, 세정과 결 정리까지입니다.')]),
 ('干燥毛躁发质:该改的习惯与合适套餐',
  '在家可调整的习惯,以及适合干燥受损发质的套餐。',
  '干燥发质护理 | 胡志明 VESSCA','干燥毛躁发质:该改的习惯与合适套餐。Unove 套餐 149,000₫,50 分钟套餐 229,000₫ 起。VESSCA。',
  ['干燥发质','受损发质 护理','胡志明 洗发'],zh,
  [('用哪款洗发水?','价目表建议染烫、受损发质选 Unove。'),('能修复受损吗?','不能,只能清洁与改善顺滑度。')]))

# 4. Bao lâu nên gội đầu ở tiệm
vi = '''<p>Không có con số đúng cho tất cả mọi người. Nhịp đi gội ở tiệm phụ thuộc vào da đầu, kiểu tóc, công việc và cả việc bạn xem đó là chăm sóc hay là một buổi nghỉ ngơi.</p>

<h2>Vài cách tự xác định nhịp</h2>

<table>
<thead><tr><th>Tình huống</th><th>Nhịp nhiều người chọn</th></tr></thead>
<tbody>
<tr><td>Da đầu nhanh bết, đội mũ bảo hiểm nhiều</td><td>Đi khi thấy da đầu bí, thường vài tuần một lần</td></tr>
<tr><td>Tóc nhuộm, uốn</td><td>Đi khi tóc khô rối, kết hợp dưỡng</td></tr>
<tr><td>Chỉ muốn thư giãn</td><td>Sau tuần làm việc dài hoặc khi mỏi cổ vai gáy</td></tr>
<tr><td>Có dịp quan trọng</td><td>Trước tiệc, chụp hình, đám cưới một hai ngày</td></tr>
</tbody>
</table>

<h2>Giữa những lần đi tiệm</h2>

<p>Gội ở nhà vẫn là việc chính. Massage da đầu bằng đầu ngón tay, xả kỹ, thoa dầu xả từ giữa thân tóc xuống và sấy ở nhiệt vừa. Buổi gội ở tiệm bổ sung các bước khó tự làm: tẩy tế bào chết da đầu, massage đầu, massage cổ vai gáy, sấy bằng máy sấy ion âm.</p>

<h2>Chọn gói theo nhịp của bạn</h2>

<ul>
<li>Đi thường xuyên, mỗi lần ngắn: Gói 01, 30 phút, từ 99.000₫.</li>
<li>Thỉnh thoảng, muốn làm kỹ: Gói 02 hoặc 03, 50 phút, từ 229.000₫.</li>
<li>Thưa, mỗi lần trọn vẹn: Gói thiên đường 75 phút, từ 419.000₫.</li>
</ul>

<h2>Khi nào nên đi khám thay vì đi gội</h2>

<p>Nếu da đầu ngứa kéo dài, có mảng đỏ, đau, hoặc tóc rụng nhiều bất thường, nên khám bác sĩ da liễu. Gội đầu ở tiệm là dịch vụ chăm sóc, không phải điều trị. Bảng giá bốn gói có ở bài <a href="/blog/goi-dau-thu-gian-binh-thanh/">gội đầu thư giãn ở Bình Thạnh</a>, đặt lịch ở mục <a href="/#booking">Đặt lịch</a>.</p>'''
faq=[('Bao lâu nên gội đầu ở tiệm một lần?','Không có con số chung; tuỳ da đầu, kiểu tóc và nhu cầu nghỉ ngơi của bạn.'),
('Đi tiệm có thay được gội ở nhà không?','Không. Gội ở nhà vẫn là việc chính; buổi ở tiệm bổ sung các bước khó tự làm.'),
('Nên chọn gói nào nếu đi thường xuyên?','Gói 01 30 phút từ 99.000₫ là lựa chọn gọn nhẹ.')]
en='''<p>There is no single right interval. How often you book a salon wash depends on your scalp, your hair, your work and whether you treat it as care or as a break.</p>
<h2>Rough guides</h2>
<ul><li>Oily scalp or long hours in a helmet: whenever the scalp feels heavy, often every few weeks</li><li>Coloured or permed hair: when it feels dry and tangled</li><li>Purely to relax: after a long week or when neck and shoulders ache</li><li>Before an occasion: a day or two before a party, shoot or wedding</li></ul>
<h2>Between visits</h2>
<p>Washing at home is still the main thing. The salon adds what is hard to do yourself: scalp exfoliation, a proper head massage, neck and shoulder work and an ion blow-dry.</p>
<h2>Picking a package</h2>
<p>Often and short: package 01, 30 minutes from 99,000₫. Occasionally and thorough: 50 minutes from 229,000₫. Rarely but fully: the 75-minute Paradise Ritual from 419,000₫. For a persistently itchy or sore scalp, see a dermatologist.</p>'''
ko='''<p>모두에게 맞는 주기는 없습니다. 두피 상태, 모발, 일, 그리고 휴식으로 생각하는지에 따라 달라집니다.</p>
<h2>대략의 기준</h2>
<ul><li>지성 두피이거나 헬멧을 오래 쓰는 경우: 두피가 답답할 때, 보통 몇 주에 한 번</li><li>염색·펌 모발: 건조하고 엉킬 때</li><li>휴식이 목적: 긴 한 주 뒤나 목·어깨가 뻐근할 때</li><li>중요한 일정 전: 하루이틀 전</li></ul>
<h2>방문 사이에는</h2>
<p>집에서 감는 것이 기본입니다. 샵에서는 두피 스케일링, 제대로 된 두피 마사지, 목·어깨 관리, 음이온 드라이를 더합니다.</p>
<h2>코스 고르기</h2>
<p>자주 짧게: 01 코스 30분 99,000₫부터. 가끔 꼼꼼히: 50분 229,000₫부터. 드물게 충분히: 75분 419,000₫부터. 가려움이나 통증이 오래가면 진료를 받으세요.</p>'''
zh='''<p>没有适用所有人的间隔。去店里洗发的频率取决于头皮状况、发质、工作,以及你把它当护理还是休息。</p>
<h2>大致参考</h2>
<ul><li>头皮易油或常戴头盔:觉得头皮闷时,多为几周一次</li><li>染烫发质:头发干涩打结时</li><li>单纯放松:忙完一周或肩颈酸时</li><li>重要场合前:提前一两天</li></ul>
<h2>两次之间</h2>
<p>在家洗头仍是主要的。店里补上自己难做的部分:头皮去角质、完整的头部按摩、肩颈放松与负离子吹干。</p>
<h2>怎么选套餐</h2>
<p>常来短做:套餐 01,30 分钟 99,000₫ 起。偶尔做细:50 分钟 229,000₫ 起。少来但做足:75 分钟 419,000₫ 起。头皮长期发痒或疼痛请就医。</p>'''
bai('bao-lau-nen-goi-dau-o-tiem',T,G,
 A(('scalp massage','Một buổi gội đầu thư giãn tại tiệm','A relaxing salon hair wash','샵에서의 릴랙싱 샴푸','店内的舒缓洗发'),[]),
 ('Bao lâu nên gội đầu ở tiệm một lần?',
  'Không có con số đúng cho tất cả. Cách tự xác định nhịp theo da đầu và công việc, nên làm gì giữa những lần đi tiệm và khi nào cần đi khám.',
  'Bao lâu nên gội đầu ở tiệm một lần | VESSCA',
  'Bao lâu nên gội đầu ở tiệm: tuỳ da đầu, kiểu tóc và nhu cầu. Gói 30 phút từ 99.000₫, 50 phút từ 229.000₫, 75 phút từ 419.000₫.',
  ['bao lâu gội đầu một lần','gội đầu ở tiệm','gội đầu thư giãn','chăm sóc da đầu','gội đầu Bình Thạnh'],vi,faq),
 ('How Often Should You Book a Salon Hair Wash?',
  'There is no single answer: rough guides by scalp and hair, what to do between visits and when to see a doctor.',
  'How Often to Book a Head Spa | VESSCA','How often to book a salon hair wash: guides by scalp and hair type. Packages 30 min from 99,000₫, 50 min from 229,000₫. VESSCA Saigon.',
  ['how often head spa','salon hair wash','head spa Saigon'],en,
  [('Is there a set interval?','No; it depends on your scalp, hair and needs.'),('Does it replace washing at home?','No, home washing is still the main thing.')]),
 ('샵 샴푸, 얼마나 자주 받는 게 좋을까',
  '정해진 주기는 없습니다. 두피와 모발에 따른 기준과 방문 사이 관리법.',
  '헤드 스파 주기 | 호치민 VESSCA','샵 샴푸 주기: 두피와 모발에 따른 기준. 30분 99,000₫부터, 50분 229,000₫부터. 호치민 VESSCA.',
  ['헤드스파 주기','호치민 헤드스파','두피 관리'],ko,
  [('정해진 주기가 있나요?','없습니다. 두피와 모발, 필요에 따라 다릅니다.'),('집에서 감는 것을 대신하나요?','아니요, 집에서 감는 것이 기본입니다.')]),
 ('多久去店里洗一次头比较好',
  '没有统一答案:按头皮与发质的参考、两次之间怎么做、何时该就医。',
  '多久洗一次头 | 胡志明 VESSCA','多久去店里洗一次头:按头皮与发质参考。30 分钟 99,000₫ 起,50 分钟 229,000₫ 起。VESSCA。',
  ['多久洗一次头','胡志明 洗发','头皮护理'],zh,
  [('有固定间隔吗?','没有,取决于头皮、发质与需求。'),('可以代替在家洗头吗?','不能,在家洗头仍是主要的。')]))
