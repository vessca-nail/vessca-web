"""Đợt 16/11/2026 — cụm NOEL (nail + gội đầu). Giá lấy đúng bảng giá đã xác nhận ở HUONG-DAN-VIET-BAI.md §6.
Lịch đăng do xep-lich gán lại; ở đây để tạm 2026-11-16T12:00."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *

X, G, C = 'Xu hướng & Cảm hứng', 'Gội đầu & Thư giãn', 'Chăm sóc móng'
T = '2026-11-16T12:00:00+07:00'

# ---------- 1. Nail Noel đỏ xanh ----------
vi = '''<p>Đỏ và xanh lá là cặp màu gắn liền với Noel, nhưng để trên móng tay không bị giống đồ trang trí thì cách phối quan trọng hơn bản thân hai màu. Bài này gợi ý vài cách dùng đỏ xanh nhẹ tay, kèm chi phí tham khảo tại VESSCA.</p>

<h2>Bốn cách phối đỏ xanh</h2>

<table>
<thead><tr><th>Cách phối</th><th>Mô tả</th><th>Chi phí tham khảo</th></tr></thead>
<tbody>
<tr><td>Một màu chủ đạo</td><td>Tám móng đỏ, hai móng xanh lá đậm làm điểm nhấn</td><td>Sơn gel trơn 130.000₫ + mix màu 10.000₫/màu</td></tr>
<tr><td>Nền nude, điểm đỏ xanh</td><td>Nền nude cho cả bàn tay, chỉ vẽ chi tiết nhỏ đỏ xanh ở một hai móng</td><td>130.000₫ + vẽ từ 10.000₫/móng</td></tr>
<tr><td>French đổi màu</td><td>Viền French màu đỏ hoặc xanh lá thay cho trắng</td><td>130.000₫ + French từ 15.000₫</td></tr>
<tr><td>Đỏ rượu vang thay đỏ tươi</td><td>Tông trầm hơn, ít chói, hợp đi làm</td><td>Sơn gel trơn 130.000₫</td></tr>
</tbody>
</table>

<h2>Chọn sắc đỏ và sắc xanh</h2>

<ul>
<li><strong>Đỏ tươi:</strong> rõ không khí Noel nhất, nổi trên mọi tông da. Nếu sợ chói, chọn móng ngắn.</li>
<li><strong>Đỏ rượu vang:</strong> trầm, sang, dễ mặc đồ công sở trong mùa lễ.</li>
<li><strong>Xanh lá đậm:</strong> hợp làm màu phụ hơn là phủ cả mười móng.</li>
<li><strong>Xanh rêu:</strong> nhẹ hơn xanh lá tươi, phối với nude rất dịu.</li>
</ul>

<h2>Thêm chi tiết mà không quá đà</h2>

<p>Một hai móng có chi tiết là đủ. Nhũ nhẹ, một viên đá nhỏ ở chân móng hoặc vài nét vẽ mảnh thường đẹp hơn cả bàn tay kín hoạ tiết. Giá tham khảo: đá thường 10.000₫ mỗi viên, đá Swarovski 20.000₫, charm 5.000₫, vẽ từ 10.000₫ mỗi móng. Bảng giá đầy đủ ở trang <a href="/bang-gia/">bảng giá</a>.</p>

<h2>Giữ được bao lâu qua mùa lễ</h2>

<p>Sơn gel thường giữ được qua kỳ nghỉ nếu bạn làm trong khoảng một tuần trước Noel. Nếu định làm mẫu khác cho năm mới, nên tính luôn lịch tháo gel (30.000₫) để không phải chờ. Mẫu cho dịp cuối năm có ở bài <a href="/blog/nail-di-tiec-cuoi-nam/">nail đi tiệc cuối năm</a>, còn mẫu đi làm vẫn hợp không khí Noel có ở bài <a href="/blog/nail-noel-di-lam-don-gian/">nail Noel đi làm đơn giản</a>.</p>

<h2>Đặt lịch</h2>

<p>Tuần trước Noel thường kín sớm vì tiệm phục vụ số khách giới hạn cùng lúc. Gửi ảnh mẫu trước qua Instagram hoặc Facebook để kỹ thuật viên chuẩn bị màu, rồi đặt ở mục <a href="/#booking">Đặt lịch</a> hoặc gọi 0933.528.501.</p>'''
faq = [('Nail Noel đỏ xanh làm sao cho không bị rối?', 'Chọn một màu chủ đạo, màu còn lại chỉ dùng cho một hai móng hoặc chi tiết nhỏ.'),
       ('Giá làm nail Noel đỏ xanh bao nhiêu?', 'Sơn gel trơn 130.000₫, mix màu thêm 10.000₫ mỗi màu, vẽ từ 10.000₫ mỗi móng, đá từ 10.000₫ mỗi viên.'),
       ('Nên làm trước Noel bao lâu?', 'Khoảng một tuần trước là vừa, bộ móng còn đẹp trọn kỳ nghỉ.')]
en = '''<p>Red and green say Christmas, but on nails the way you combine them matters more than the colours themselves.</p>
<h2>Four combinations</h2>
<ul><li>One dominant colour: eight red nails, two deep green as accents (gel 130,000₫ + 10,000₫ per extra colour)</li><li>Nude base with small red and green details on one or two nails (from 10,000₫ per painted nail)</li><li>A French line in red or green instead of white (from 15,000₫)</li><li>Burgundy instead of bright red — softer, easy for the office</li></ul>
<h2>Keep details light</h2>
<p>One or two accent nails is usually enough: fine lines, light shimmer, or a single stone at the base (stones from 10,000₫, Swarovski 20,000₫, charms 5,000₫).</p>
<h2>Booking</h2>
<p>The week before Christmas fills up early. Send a reference photo ahead and book through the <a href="/en/#booking">booking form</a> or call 0933.528.501.</p>'''
ko = '''<p>레드와 그린은 크리스마스의 색이지만, 네일에서는 두 색을 어떻게 조합하는지가 더 중요합니다.</p>
<h2>네 가지 조합</h2>
<ul><li>한 가지를 메인으로: 레드 8개, 딥그린 2개 포인트(젤 130,000₫ + 추가 컬러당 10,000₫)</li><li>누드 베이스에 한두 개만 레드·그린 디테일(아트 손톱당 10,000₫부터)</li><li>화이트 대신 레드·그린 프렌치 라인(15,000₫부터)</li><li>밝은 레드 대신 버건디 — 차분해서 출근용으로 좋습니다</li></ul>
<h2>디테일은 가볍게</h2>
<p>포인트는 한두 개면 충분합니다. 얇은 라인, 은은한 펄, 큐티클 쪽 스톤 하나(스톤 10,000₫부터, 스와로브스키 20,000₫, 참 5,000₫).</p>
<h2>예약</h2>
<p>크리스마스 전 주는 일찍 찹니다. 원하는 디자인 사진을 미리 보내 주시고 <a href="/ko/#booking">예약 양식</a> 또는 0933.528.501로 예약하세요.</p>'''
zh = '''<p>红配绿是圣诞的颜色,但在指甲上,怎么搭配比颜色本身更重要。</p>
<h2>四种搭配</h2>
<ul><li>以一色为主:八指红色,两指深绿点缀(凝胶 130,000₫ + 每增加一色 10,000₫)</li><li>裸色打底,仅一两指加红绿小细节(彩绘每指 10,000₫ 起)</li><li>法式线条用红或绿取代白色(15,000₫ 起)</li><li>以酒红代替正红——更沉稳,适合上班</li></ul>
<h2>细节点到为止</h2>
<p>一两指做重点就够:细线条、淡淡闪粉,或甲根一颗小钻(钻 10,000₫ 起,施华洛世奇 20,000₫,挂饰 5,000₫)。</p>
<h2>预约</h2>
<p>圣诞前一周很快约满。可先发送款式图片,再用<a href="/zh/#booking">预约表单</a>或致电 0933.528.501。</p>'''
bai('nail-noel-do-xanh', T, X,
 A(('red nails manicure', 'Nail Noel phối đỏ và xanh lá', 'Christmas nails in red and green', '레드 그린 크리스마스 네일', '红绿配色的圣诞美甲'), []),
 ('Nail Noel đỏ xanh: bốn cách phối không bị rối mắt',
  'Đỏ và xanh lá trên móng tay dễ thành rối nếu dùng ngang nhau. Bốn cách phối nhẹ tay, cách chọn sắc đỏ sắc xanh và chi phí tham khảo.',
  'Nail Noel đỏ xanh: 4 cách phối đẹp | VESSCA',
  'Nail Noel đỏ xanh: chọn một màu chủ đạo, nền nude điểm chi tiết, French đổi màu hay đỏ rượu vang. Giá từ 130.000₫ tại VESSCA Bình Thạnh.',
  ['nail Noel', 'nail Noel đỏ xanh', 'nail Giáng sinh', 'mẫu nail Noel', 'nail Noel đẹp'], vi, faq),
 ('Red and Green Christmas Nails: Four Ways to Combine Them',
  'Four light-handed ways to wear red and green nails, with prices.',
  'Red & Green Christmas Nails | VESSCA', 'Red and green Christmas nails without the clutter: four combinations, colour choices and prices from 130,000₫. VESSCA, Saigon.',
  ['christmas nails', 'red green nails', 'nail salon Saigon'], en,
  [('How do I keep red and green from clashing?', 'Pick one dominant colour and use the other only on one or two nails.'),
   ('How much?', 'Plain gel 130,000₫, extra colours 10,000₫ each, art from 10,000₫ per nail.')]),
 ('레드 그린 크리스마스 네일, 네 가지 조합',
  '레드와 그린을 가볍게 쓰는 네 가지 방법과 가격.',
  '크리스마스 네일 레드 그린 | VESSCA', '호치민 크리스마스 네일 레드 그린: 네 가지 조합과 컬러 선택, 130,000₫부터. VESSCA.',
  ['크리스마스 네일', '호치민 네일', '레드 네일'], ko,
  [('어떻게 하면 안 촌스러운가요?', '한 색을 메인으로 하고 다른 색은 한두 개만 쓰세요.'),
   ('가격은요?', '원컬러 젤 130,000₫, 추가 컬러 10,000₫, 아트 손톱당 10,000₫부터.')]),
 ('红绿圣诞美甲:四种不显杂乱的搭配',
  '红配绿的四种轻盈搭配方式与价格。',
  '红绿圣诞美甲 | 胡志明 VESSCA', '胡志明红绿圣诞美甲:四种搭配、配色建议,130,000₫ 起。VESSCA。',
  ['圣诞美甲', '胡志明 美甲', '红色美甲'], zh,
  [('怎么搭才不杂乱?', '以一色为主,另一色只用在一两指。'),
   ('多少钱?', '纯色凝胶 130,000₫,每增加一色 10,000₫,彩绘每指 10,000₫ 起。')]))

# ---------- 2. Nail Noel trắng tuyết ----------
vi = '''<p>Không phải ai cũng muốn móng tay đỏ rực vào tháng 12. Tông trắng, sữa, bạc là hướng nhẹ nhàng hơn mà vẫn đúng không khí mùa lễ, lại dễ mặc với mọi bộ đồ.</p>

<h2>Ba tông trắng khác nhau</h2>

<table>
<thead><tr><th>Tông</th><th>Cảm giác</th><th>Hợp với</th></tr></thead>
<tbody>
<tr><td>Trắng sữa đục</td><td>Mềm, ấm, trông tay sạch sẽ</td><td>Móng ngắn, đi làm</td></tr>
<tr><td>Trắng trong như thạch</td><td>Trong, nhẹ, nhìn như lớp men mỏng</td><td>Người thích tối giản</td></tr>
<tr><td>Trắng ánh bạc</td><td>Lấp lánh khi bắt sáng</td><td>Tiệc tối, chụp hình</td></tr>
</tbody>
</table>

<p>Sơn gel trơn 130.000₫, sơn thạch 150.000₫. Nếu muốn ánh xà cừ sâu hơn, dòng xà cừ ánh trai là 280.000₫.</p>

<h2>Thêm chút tuyết</h2>

<ul>
<li><strong>Nhũ mịn rắc nhẹ ở chân móng:</strong> giống tuyết đọng, kín đáo.</li>
<li><strong>Một móng vẽ bông tuyết mảnh:</strong> vẽ từ 10.000₫ mỗi móng.</li>
<li><strong>Vài viên đá nhỏ rải không đều:</strong> đá 10.000₫, Swarovski 20.000₫.</li>
<li><strong>Tráng gương bạc một móng:</strong> từ 15.000₫, bắt sáng rất rõ.</li>
</ul>

<h2>Lưu ý khi làm móng tông trắng</h2>

<p>Trắng đục cần sơn đều tay nên thường phải nhiều lớp mỏng, bộ móng vì vậy lâu hơn một chút. Màu trắng cũng dễ lộ phần móng mọc ra hơn màu nude, nên nếu bạn ít có thời gian quay lại, cân nhắc trắng trong hoặc nude sữa. Cách móng mọc ảnh hưởng tới mẫu nail có ở bài <a href="/blog/bao-lau-nen-lam-nail-mot-lan/">bao lâu nên làm nail một lần</a>.</p>

<h2>Đặt lịch trước mùa lễ</h2>

<p>Tiệm phục vụ số khách giới hạn cùng lúc, tuần giữa tháng 12 thường kín trước. Đặt ở mục <a href="/#booking">Đặt lịch</a> hoặc gọi 0933.528.501. Mẫu Noel khác có ở bài <a href="/blog/nail-noel-do-xanh/">nail Noel đỏ xanh</a>.</p>'''
faq = [('Nail Noel tông trắng có những kiểu nào?', 'Trắng sữa đục, trắng trong như thạch và trắng ánh bạc, thêm nhũ hoặc vẽ bông tuyết tuỳ thích.'),
       ('Giá bao nhiêu?', 'Sơn gel trơn 130.000₫, sơn thạch 150.000₫, dòng xà cừ ánh trai 280.000₫.'),
       ('Màu trắng có nhanh lộ móng mọc không?', 'Dễ lộ hơn màu nude. Nếu ít thời gian quay lại, chọn trắng trong hoặc nude sữa.')]
en = '''<p>Not everyone wants bright red in December. White, milky and silver tones feel festive in a quieter way and go with anything.</p>
<h2>Three kinds of white</h2>
<ul><li>Milky opaque white — soft and warm, good on short nails</li><li>Clear jelly white — minimal, like a thin glaze</li><li>Silvery white — catches the light, good for evening</li></ul>
<p>Plain gel 130,000₫, jelly 150,000₫; the mother-of-pearl line is 280,000₫.</p>
<h2>A little snow</h2>
<p>Fine shimmer at the base, a thin snowflake on one nail (art from 10,000₫), scattered small stones (from 10,000₫) or a chrome accent nail (from 15,000₫).</p>
<h2>Note</h2>
<p>Opaque white needs even, thin layers and shows regrowth sooner than nude. Book ahead: mid-December fills early.</p>'''
ko = '''<p>12월이라고 꼭 붉은색일 필요는 없습니다. 화이트, 밀키, 실버 톤은 은은하게 겨울 분위기를 내고 어떤 옷에도 어울립니다.</p>
<h2>세 가지 화이트</h2>
<ul><li>밀키 화이트 — 부드럽고 따뜻하며 짧은 손톱에 잘 어울립니다</li><li>클리어 젤리 화이트 — 얇은 유약 같은 미니멀한 느낌</li><li>실버 화이트 — 빛을 받아 반짝여 저녁 자리에 좋습니다</li></ul>
<p>원컬러 젤 130,000₫, 시럽 150,000₫, 자개 라인 280,000₫.</p>
<h2>눈 내린 느낌</h2>
<p>큐티클 쪽 고운 펄, 한 손톱에 얇은 눈꽃(아트 10,000₫부터), 작은 스톤(10,000₫부터), 크롬 포인트(15,000₫부터).</p>
<h2>참고</h2>
<p>불투명 화이트는 얇게 여러 번 발라야 하고 누드보다 자란 부분이 빨리 보입니다. 12월 중순은 일찍 차니 미리 예약해 주세요.</p>'''
zh = '''<p>十二月不一定要大红。白色、奶白与银色同样有节日感,而且百搭。</p>
<h2>三种白</h2>
<ul><li>奶白不透明——柔和温暖,适合短指甲</li><li>果冻透白——极简,像一层薄釉</li><li>银白——会反光,适合晚间场合</li></ul>
<p>纯色凝胶 130,000₫,果冻 150,000₫,贝壳光系列 280,000₫。</p>
<h2>加一点"雪"</h2>
<p>甲根细闪粉、一指细雪花(彩绘 10,000₫ 起)、零星小钻(10,000₫ 起)或一指镜面银(15,000₫ 起)。</p>
<h2>提醒</h2>
<p>不透明白色需薄涂多层,且比裸色更快看出新长出的指甲。十二月中旬很快约满,建议提前预约。</p>'''
bai('nail-noel-trang-tuyet', T, X,
 A(('milky white nails manicure', 'Nail Noel tông trắng tuyết', 'Snowy white Christmas nails', '화이트 크리스마스 네일', '雪白色圣诞美甲'), []),
 ('Nail Noel tông trắng: ba sắc trắng và cách thêm chút tuyết',
  'Tông trắng, sữa, bạc cho mùa Noel: ba sắc trắng khác nhau, cách thêm nhũ và bông tuyết, giá tham khảo và lưu ý khi làm móng màu trắng.',
  'Nail Noel tông trắng tuyết: 3 sắc trắng | VESSCA',
  'Nail Noel tông trắng: trắng sữa, trắng trong, trắng ánh bạc, thêm nhũ hoặc bông tuyết. Sơn gel từ 130.000₫ tại VESSCA Bình Thạnh.',
  ['nail Noel trắng', 'nail trắng sữa', 'nail Giáng sinh', 'nail bông tuyết', 'mẫu nail Noel'], vi, faq),
 ('White Christmas Nails: Three Whites and a Little Snow',
  'Milky, clear and silvery white for December, with art ideas and prices.',
  'White Christmas Nails | VESSCA', 'White Christmas nails in Saigon: milky, jelly and silvery white, shimmer and snowflake art. Gel from 130,000₫. VESSCA.',
  ['white christmas nails', 'milky white nails', 'nail salon Saigon'], en,
  [('Which whites are there?', 'Milky opaque, clear jelly and silvery white.'),
   ('Does white show regrowth?', 'Sooner than nude. Choose clear white or milky nude if you cannot return soon.')]),
 ('화이트 크리스마스 네일: 세 가지 화이트',
  '밀키·클리어·실버 화이트와 눈꽃 아트, 가격.',
  '화이트 크리스마스 네일 | 호치민 VESSCA', '호치민 화이트 크리스마스 네일: 밀키·젤리·실버 화이트, 펄과 눈꽃 아트. 젤 130,000₫부터.',
  ['크리스마스 네일', '화이트 네일', '호치민 네일'], ko,
  [('어떤 화이트가 있나요?', '밀키, 클리어 젤리, 실버 화이트입니다.'),
   ('자란 부분이 티 나나요?', '누드보다 빨리 보입니다.')]),
 ('雪白圣诞美甲:三种白与一点雪',
  '奶白、透白与银白,以及雪花彩绘和价格。',
  '雪白圣诞美甲 | 胡志明 VESSCA', '胡志明雪白圣诞美甲:奶白、果冻白、银白,闪粉与雪花彩绘,凝胶 130,000₫ 起。VESSCA。',
  ['圣诞美甲', '白色美甲', '胡志明 美甲'], zh,
  [('有哪几种白?', '奶白、果冻透白与银白。'),
   ('白色容易看出新长的指甲吗?', '比裸色更明显。')]))

# ---------- 3. Nail Noel cho móng ngắn ----------
vi = '''<p>Móng ngắn vẫn làm được mẫu Noel đẹp, chỉ cần chọn hoạ tiết vừa với diện tích móng. Bài này gợi ý mẫu hợp móng ngắn và cách chọn để tay nhìn gọn gàng.</p>

<h2>Nguyên tắc chung</h2>

<ul>
<li>Hoạ tiết nhỏ và ít, đặt lệch về chân móng hoặc một góc, không phủ kín.</li>
<li>Một hoặc hai móng làm điểm nhấn, tám móng còn lại một màu.</li>
<li>Tông trầm hoặc nude làm nền giúp móng ngắn trông dài hơn tông sáng chói.</li>
<li>Form vuông bo góc hoặc oval nhẹ thường gọn hơn form nhọn khi móng ngắn.</li>
</ul>

<h2>Năm mẫu hợp móng ngắn</h2>

<table>
<thead><tr><th>Mẫu</th><th>Cách làm</th><th>Chi phí tham khảo</th></tr></thead>
<tbody>
<tr><td>Đỏ rượu vang trơn</td><td>Một màu cho cả mười móng</td><td>130.000₫</td></tr>
<tr><td>Nude sữa, một móng nhũ bạc</td><td>Nền nude, một móng phủ nhũ</td><td>130.000₫ + mix 10.000₫</td></tr>
<tr><td>Mắt mèo tông xanh rêu</td><td>Ánh từ tính chạy giữa móng</td><td>170.000₫</td></tr>
<tr><td>French viền đỏ mảnh</td><td>Viền mảnh ở đầu móng</td><td>130.000₫ + French từ 15.000₫</td></tr>
<tr><td>Một bông tuyết nhỏ</td><td>Vẽ ở một móng, nền trắng trong</td><td>130.000₫ + vẽ từ 10.000₫</td></tr>
</tbody>
</table>

<h2>Nếu móng bạn đang yếu</h2>

<p>Móng ngắn do hay gãy thì nên chăm trước khi làm mẫu cầu kỳ. Sơn cứng móng là 40.000₫; cắt da, chỉnh form, dưỡng viền tay 60.000₫. Nguyên nhân móng giòn dễ gãy có ở bài <a href="/blog/mong-tay-yeu-de-gay/">móng tay yếu dễ gãy</a>.</p>

<h2>Muốn dài hơn một chút</h2>

<p>Nếu muốn thêm độ dài cho dịp lễ, úp móng là 130.000₫, Gel X 190.000₫, đắp gel 250.000₫. Cân nhắc công việc hằng ngày trước khi chọn độ dài. Bảng giá đầy đủ ở trang <a href="/bang-gia/">bảng giá</a>, đặt lịch ở mục <a href="/#booking">Đặt lịch</a>.</p>'''
faq = [('Móng ngắn làm nail Noel được không?', 'Được. Chọn hoạ tiết nhỏ, đặt lệch, và chỉ làm điểm nhấn ở một hai móng.'),
       ('Mẫu nào hợp móng ngắn nhất?', 'Đỏ rượu vang trơn, nude sữa điểm nhũ, mắt mèo tông trầm, French viền mảnh.'),
       ('Muốn dài thêm cho dịp lễ thì làm gì?', 'Úp móng 130.000₫, Gel X 190.000₫ hoặc đắp gel 250.000₫.')]
en = '''<p>Short nails can carry a Christmas look; the trick is scaling the art to the nail.</p>
<h2>Rules of thumb</h2>
<ul><li>Small, few details, placed off-centre rather than covering the nail</li><li>One or two accent nails, the rest a single colour</li><li>Deeper or nude bases make short nails look longer than bright shades do</li><li>Squoval or soft oval reads neater than a pointed shape</li></ul>
<h2>Five looks</h2>
<p>Burgundy (130,000₫); milky nude with one shimmer nail (130,000₫ + 10,000₫); moss-green cat-eye (170,000₫); a thin red French line (130,000₫ + from 15,000₫); a single snowflake (130,000₫ + from 10,000₫).</p>
<h2>Want more length</h2>
<p>Tips 130,000₫, Gel X 190,000₫, builder gel 250,000₫. A nail hardener is 40,000₫ if your nails break easily.</p>'''
ko = '''<p>짧은 손톱도 크리스마스 네일이 잘 어울립니다. 손톱 크기에 맞게 아트를 줄이는 것이 요령입니다.</p>
<h2>기본 원칙</h2>
<ul><li>작고 적은 디테일을 한쪽으로 치우쳐 배치</li><li>포인트는 한두 개, 나머지는 한 가지 컬러</li><li>딥한 톤이나 누드가 밝은 색보다 손톱을 길어 보이게 합니다</li><li>스퀘어오프나 부드러운 오벌이 뾰족한 형보다 단정합니다</li></ul>
<h2>다섯 가지 디자인</h2>
<p>버건디(130,000₫), 밀키 누드에 펄 포인트 하나(130,000₫ + 10,000₫), 모스그린 자석(170,000₫), 얇은 레드 프렌치(130,000₫ + 15,000₫부터), 눈꽃 하나(130,000₫ + 10,000₫부터).</p>
<h2>길이를 더하고 싶다면</h2>
<p>팁 130,000₫, 젤엑스 190,000₫, 젤 연장 250,000₫. 잘 부러지는 손톱에는 강화제 40,000₫.</p>'''
zh = '''<p>短指甲同样能做圣诞款,关键是把图案缩到合适的比例。</p>
<h2>基本原则</h2>
<ul><li>细节少而小,偏放一侧,不要铺满</li><li>一两指做重点,其余单色</li><li>深色或裸色比亮色更显指甲修长</li><li>方圆形或柔和椭圆比尖形更干净</li></ul>
<h2>五款推荐</h2>
<p>酒红纯色(130,000₫);奶裸色加一指闪粉(130,000₫ + 10,000₫);苔绿猫眼(170,000₫);细红法式(130,000₫ + 15,000₫ 起);一片雪花(130,000₫ + 10,000₫ 起)。</p>
<h2>想要长一点</h2>
<p>甲片 130,000₫、Gel X 190,000₫、延长凝胶 250,000₫。指甲易断可做强甲油 40,000₫。</p>'''
bai('nail-noel-mong-ngan', T, X,
 A(('short nails manicure', 'Mẫu nail Noel cho móng ngắn', 'Christmas nails on short nails', '짧은 손톱 크리스마스 네일', '短指甲的圣诞美甲'), []),
 ('Nail Noel cho móng ngắn: năm mẫu vừa vặn, không rườm rà',
  'Móng ngắn vẫn làm được mẫu Noel đẹp: nguyên tắc chọn hoạ tiết, năm mẫu cụ thể kèm chi phí và cách xử lý khi móng đang yếu.',
  'Nail Noel cho móng ngắn: 5 mẫu gọn đẹp | VESSCA',
  'Nail Noel cho móng ngắn: đỏ rượu vang, nude điểm nhũ, mắt mèo xanh rêu, French mảnh, bông tuyết nhỏ. Từ 130.000₫ tại VESSCA.',
  ['nail Noel móng ngắn', 'nail móng ngắn', 'nail Noel', 'mẫu nail Giáng sinh', 'nail đẹp móng ngắn'], vi, faq),
 ('Christmas Nails for Short Nails: Five Looks That Fit',
  'Scaling Christmas nail art to short nails, with five looks and prices.',
  'Christmas Nails for Short Nails | VESSCA', 'Christmas nails for short nails in Saigon: burgundy, milky nude, cat-eye, thin French, a single snowflake. From 130,000₫.',
  ['short nails christmas', 'christmas nails', 'nail salon Saigon'], en,
  [('Can short nails do Christmas art?', 'Yes, with small details placed off-centre and one or two accent nails.'),
   ('How to add length?', 'Tips 130,000₫, Gel X 190,000₫ or builder gel 250,000₫.')]),
 ('짧은 손톱 크리스마스 네일 다섯 가지',
  '짧은 손톱에 맞춘 아트 비율과 다섯 가지 디자인, 가격.',
  '짧은 손톱 크리스마스 네일 | VESSCA', '호치민 짧은 손톱 크리스마스 네일: 버건디, 밀키 누드, 자석, 얇은 프렌치, 눈꽃. 130,000₫부터.',
  ['짧은 손톱 네일', '크리스마스 네일', '호치민 네일'], ko,
  [('짧아도 되나요?', '네, 작은 디테일을 한쪽에 두고 포인트는 한두 개만 하세요.'),
   ('길이를 더하려면?', '팁 130,000₫, 젤엑스 190,000₫, 젤 연장 250,000₫.')]),
 ('短指甲的圣诞美甲:五款刚刚好',
  '短指甲的图案比例与五款设计、价格。',
  '短指甲圣诞美甲 | 胡志明 VESSCA', '胡志明短指甲圣诞美甲:酒红、奶裸、猫眼、细法式、小雪花,130,000₫ 起。VESSCA。',
  ['短指甲 美甲', '圣诞美甲', '胡志明 美甲'], zh,
  [('短指甲能做吗?', '可以,细节小且偏放,一两指做重点。'),
   ('怎么加长?', '甲片 130,000₫、Gel X 190,000₫ 或延长凝胶 250,000₫。')]))

# ---------- 4. Nail mắt mèo mùa Noel ----------
vi = '''<p>Sơn mắt mèo có hạt từ tính, khi đưa nam châm lại gần sẽ gom thành một dải sáng chạy trên móng. Vào mùa lễ, hiệu ứng này hợp với các tông đỏ, xanh rêu và xám khói, cho bàn tay nổi mà không cần vẽ gì thêm.</p>

<h2>Mắt mèo hoạt động thế nào</h2>

<p>Trong sơn có hạt kim loại nhỏ. Kỹ thuật viên đưa nam châm lại gần lúc sơn còn ướt, hạt gom lại thành dải sáng, rồi hơ đèn để cố định. Dải sáng nằm ở đâu là do hướng đặt nam châm, nên bạn có thể nói trước mình muốn dải chạy ngang, dọc hay chéo.</p>

<h2>Tông hợp mùa Noel</h2>

<table>
<thead><tr><th>Tông</th><th>Cảm giác</th></tr></thead>
<tbody>
<tr><td>Đỏ rượu vang</td><td>Sâu, ánh đỏ chuyển khi nghiêng tay</td></tr>
<tr><td>Xanh rêu</td><td>Trầm, ít gặp, hợp người không thích đỏ</td></tr>
<tr><td>Xám khói ánh bạc</td><td>Lạnh, giống ánh băng</td></tr>
<tr><td>Tím mận</td><td>Giữa đỏ và tím, dễ phối đồ tối màu</td></tr>
</tbody>
</table>

<h2>Giá và dòng sơn</h2>

<p>Sơn mắt mèo thường là 170.000₫. Dòng mắt mèo KISS NY (Kissny) tiệm tự chọn và mang về từ Hàn là 280.000₫. Mix thêm màu cộng 10.000₫ mỗi màu. Các dòng sơn Hàn tiệm đang dùng có ở bài <a href="/blog/bo-suu-tap-son-han-quoc-tai-vessca/">bộ sưu tập sơn Hàn Quốc tại VESSCA</a>.</p>

<h2>Làm sao giữ dải sáng đẹp</h2>

<ul>
<li>Nói rõ hướng dải sáng bạn muốn trước khi kỹ thuật viên hơ đèn.</li>
<li>Mắt mèo lên đẹp nhất trên nền tối; nền sáng thì hiệu ứng mờ hơn.</li>
<li>Móng ngắn vẫn làm được, dải sáng sẽ ngắn và gọn hơn.</li>
</ul>

<p>Cách sơn mắt mèo hoạt động nói kỹ hơn ở bài <a href="/blog/son-mat-meo-la-gi/">sơn mắt mèo là gì</a>. Đặt lịch ở mục <a href="/#booking">Đặt lịch</a> hoặc gọi 0933.528.501.</p>'''
faq = [('Sơn mắt mèo giá bao nhiêu?', 'Mắt mèo thường 170.000₫; dòng mắt mèo KISS NY mang về từ Hàn là 280.000₫.'),
       ('Mắt mèo có chọn hướng dải sáng được không?', 'Được, nói với kỹ thuật viên trước khi hơ đèn để đặt nam châm theo hướng bạn muốn.'),
       ('Tông nào hợp mùa Noel?', 'Đỏ rượu vang, xanh rêu, xám khói ánh bạc và tím mận.')]
en = '''<p>Cat-eye gel holds tiny magnetic particles. A magnet held near the wet polish draws them into a bright band, which is then cured. For the holidays it works beautifully in burgundy, moss green and smoky grey.</p>
<h2>Shades for December</h2>
<ul><li>Burgundy — deep, shifts as the hand moves</li><li>Moss green — muted, for anyone avoiding red</li><li>Smoky silver grey — cool, icy</li><li>Plum — between red and purple</li></ul>
<h2>Prices</h2>
<p>Cat-eye gel 170,000₫; the KISS NY cat-eye line the salon brings from Korea is 280,000₫; extra colours 10,000₫ each.</p>
<h2>Tips</h2>
<p>Say which direction you want the band before curing. The effect is strongest over a dark base, and works on short nails too.</p>'''
ko = '''<p>자석 젤에는 미세한 자성 입자가 들어 있습니다. 젤이 마르기 전 자석을 가까이 대면 입자가 모여 빛나는 띠를 만들고, 그 상태로 큐어링합니다. 연말에는 버건디, 모스그린, 스모키 그레이가 특히 잘 어울립니다.</p>
<h2>12월에 어울리는 컬러</h2>
<ul><li>버건디 — 깊고, 손을 움직일 때 색이 변합니다</li><li>모스그린 — 차분해서 레드가 부담스러운 분께</li><li>스모키 실버 그레이 — 차갑고 얼음 같은 느낌</li><li>플럼 — 레드와 퍼플 사이</li></ul>
<h2>가격</h2>
<p>자석 젤 170,000₫, 샵이 한국에서 가져온 KISS NY 자석 라인 280,000₫, 추가 컬러 10,000₫.</p>
<h2>팁</h2>
<p>큐어링 전에 원하는 띠 방향을 말씀해 주세요. 어두운 베이스에서 가장 또렷하며 짧은 손톱에도 가능합니다.</p>'''
zh = '''<p>猫眼凝胶内含细小磁性颗粒。趁未干时靠近磁铁,颗粒聚成一道亮带,再照灯定型。节日季里,酒红、苔绿和烟灰都很合适。</p>
<h2>适合十二月的色调</h2>
<ul><li>酒红——深邃,转动手时有色泽变化</li><li>苔绿——低调,适合不想用红色的人</li><li>烟灰银——冷调,像冰</li><li>梅子紫——介于红与紫之间</li></ul>
<h2>价格</h2>
<p>猫眼凝胶 170,000₫;店里从韩国带回的 KISS NY 猫眼系列 280,000₫;每增加一色 10,000₫。</p>
<h2>小提示</h2>
<p>照灯前先说明想要的光带方向。深色打底效果最明显,短指甲同样可做。</p>'''
bai('nail-noel-mat-meo', T, X,
 A(('dark glitter nails manicure', 'Nail mắt mèo tông tối mùa lễ', 'Cat-eye nails in deep holiday shades', '연말 분위기의 자석 네일', '节日色调的猫眼美甲'), []),
 ('Nail mắt mèo mùa Noel: bốn tông đẹp và cách chọn hướng dải sáng',
  'Sơn mắt mèo hoạt động thế nào, bốn tông hợp mùa lễ, giá từng dòng và cách nói với kỹ thuật viên để dải sáng nằm đúng ý.',
  'Nail mắt mèo mùa Noel: 4 tông đẹp | VESSCA',
  'Nail mắt mèo mùa Noel: đỏ rượu vang, xanh rêu, xám khói, tím mận. Mắt mèo 170.000₫, dòng KISS NY 280.000₫ tại VESSCA Bình Thạnh.',
  ['nail mắt mèo', 'nail mắt mèo Noel', 'sơn mắt mèo', 'nail Giáng sinh', 'mắt mèo đỏ'], vi, faq),
 ('Cat-Eye Nails for the Holidays: Four Shades',
  'How cat-eye gel works, four festive shades and prices.',
  'Cat-Eye Nails for the Holidays | VESSCA', 'Cat-eye nails for the holidays in Saigon: burgundy, moss green, smoky grey, plum. 170,000₫, KISS NY line 280,000₫.',
  ['cat eye nails', 'magnetic gel nails', 'nail salon Saigon'], en,
  [('How much?', 'Cat-eye gel 170,000₫; the KISS NY line 280,000₫.'),
   ('Can I choose the band direction?', 'Yes, tell your technician before curing.')]),
 ('연말 자석 네일: 어울리는 네 가지 컬러',
  '자석 젤의 원리, 연말 컬러 네 가지, 가격.',
  '연말 자석 네일 | 호치민 VESSCA', '호치민 연말 자석 네일: 버건디, 모스그린, 스모키 그레이, 플럼. 170,000₫, KISS NY 라인 280,000₫.',
  ['자석 네일', '호치민 네일', '크리스마스 네일'], ko,
  [('가격은요?', '자석 젤 170,000₫, KISS NY 라인 280,000₫.'),
   ('띠 방향을 고를 수 있나요?', '네, 큐어링 전에 말씀해 주세요.')]),
 ('节日猫眼美甲:四种好看的色调',
  '猫眼凝胶的原理、四种节日色与价格。',
  '节日猫眼美甲 | 胡志明 VESSCA', '胡志明节日猫眼美甲:酒红、苔绿、烟灰、梅子紫。170,000₫,KISS NY 系列 280,000₫。',
  ['猫眼美甲', '胡志明 美甲', '圣诞美甲'], zh,
  [('多少钱?', '猫眼凝胶 170,000₫,KISS NY 系列 280,000₫。'),
   ('可以选光带方向吗?', '可以,照灯前告知技师。')]))
