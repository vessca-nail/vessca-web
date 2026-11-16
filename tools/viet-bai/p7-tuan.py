"""Đợt 16/11/2026 (batch 3) — Noel, cuối năm, gội đầu. Giá theo HUONG-DAN-VIET-BAI.md §6 và lib/goi-dau.mjs."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *

X, G, C, Q = 'Xu hướng & Cảm hứng', 'Gội đầu & Thư giãn', 'Chăm sóc móng', 'Hỏi & Đáp'
T = '2026-11-16T12:00:00+07:00'

# 1. Nail vẽ cây thông
vi = '''<p>Cây thông là hoạ tiết Noel dễ nhận ra nhất, nhưng vẽ nguyên cây lên móng thường chiếm hết chỗ. Cách thường dùng ở tiệm là rút gọn: vài nét mảnh gợi hình cây, hoặc chỉ một cây nhỏ trên một móng.</p>

<h2>Ba cách rút gọn</h2>

<table>
<thead><tr><th>Cách</th><th>Mô tả</th><th>Chi phí tham khảo</th></tr></thead>
<tbody>
<tr><td>Cây nét mảnh</td><td>Vài nét chéo xuống dần, không tô đặc</td><td>Vẽ từ 10.000₫ mỗi móng</td></tr>
<tr><td>Cây nhỏ một móng</td><td>Chín móng một màu, một móng có cây</td><td>130.000₫ + 10.000₫</td></tr>
<tr><td>Cây kết hợp đá</td><td>Một viên đá nhỏ làm ngôi sao trên ngọn</td><td>Thêm đá 10.000₫, Swarovski 20.000₫</td></tr>
</tbody>
</table>

<h2>Nền nào lên đẹp</h2>

<ul>
<li><strong>Nền nude hoặc trắng sữa:</strong> nét vẽ xanh, vàng nổi rõ.</li>
<li><strong>Nền đỏ rượu vang:</strong> vẽ nét trắng hoặc vàng, trông ấm.</li>
<li><strong>Nền thạch trong:</strong> hình như nổi trên móng, nhẹ nhàng.</li>
</ul>

<h2>Lưu ý về độ bền</h2>

<p>Nét vẽ nằm dưới lớp top coat nên bền tương đương lớp sơn. Phần dễ bong nhất là đá đính nổi, nhất là khi bạn hay làm việc nhà. Nếu cần bền, chọn vẽ thay vì đính. Mẫu Noel khác có ở bài <a href="/blog/nail-noel-do-xanh/">nail Noel đỏ xanh</a> và <a href="/blog/nail-noel-trang-tuyet/">nail Noel tông trắng</a>.</p>

<p>Gửi ảnh mẫu trước qua Instagram hoặc Facebook để kỹ thuật viên chuẩn bị, rồi <a href="/#booking">đặt lịch</a> hoặc gọi 0933.528.501. Bảng giá đầy đủ ở trang <a href="/bang-gia/">bảng giá</a>.</p>'''
faq=[('Vẽ cây thông lên móng giá bao nhiêu?','Vẽ từ 10.000₫ mỗi móng, cộng vào giá nền sơn gel 130.000₫.'),
('Nền màu nào vẽ cây thông đẹp?','Nude, trắng sữa, đỏ rượu vang hoặc thạch trong.'),
('Đính đá có bền không?','Đá nổi dễ bong hơn nét vẽ, nhất là khi làm việc nhà nhiều.')]
en='''<p>A Christmas tree is the most recognisable holiday motif, but a full tree usually fills the whole nail. Salons tend to simplify it.</p>
<h2>Three simplified versions</h2>
<ul><li>Fine diagonal lines suggesting a tree (art from 10,000₫ per nail)</li><li>One small tree on a single nail, the rest plain (130,000₫ + 10,000₫)</li><li>A tiny stone as the star on top (stones from 10,000₫, Swarovski 20,000₫)</li></ul>
<h2>Which base</h2>
<p>Nude or milky white makes green and gold lines stand out; burgundy suits white or gold lines; clear jelly makes the shape float.</p>
<h2>Durability</h2>
<p>Painted lines sit under the top coat and last as long as the colour. Raised stones are the first thing to come off, especially with housework.</p>'''
ko='''<p>크리스마스 트리는 가장 알아보기 쉬운 모티프지만, 통째로 그리면 손톱을 다 차지합니다. 샵에서는 보통 단순화해 그립니다.</p>
<h2>단순화한 세 가지</h2>
<ul><li>얇은 사선으로 트리를 암시(아트 손톱당 10,000₫부터)</li><li>한 손톱에만 작은 트리, 나머지는 단색(130,000₫ + 10,000₫)</li><li>꼭대기에 작은 스톤으로 별(스톤 10,000₫부터, 스와로브스키 20,000₫)</li></ul>
<h2>베이스 선택</h2>
<p>누드나 밀키 화이트는 그린·골드 라인이 또렷하고, 버건디에는 화이트나 골드 라인, 클리어 젤리는 그림이 떠 보입니다.</p>
<h2>지속력</h2>
<p>그림은 탑젤 아래에 있어 컬러만큼 오래갑니다. 돌출된 스톤이 가장 먼저 떨어집니다.</p>'''
zh='''<p>圣诞树是最好认的节日图案,但整棵画上去往往占满指甲,所以店里通常会简化。</p>
<h2>三种简化画法</h2>
<ul><li>用细斜线暗示树形(彩绘每指 10,000₫ 起)</li><li>只在一指画小树,其余单色(130,000₫ + 10,000₫)</li><li>树顶放一颗小钻当星星(钻 10,000₫ 起,施华洛世奇 20,000₫)</li></ul>
<h2>选底色</h2>
<p>裸色或奶白能衬出绿金线条;酒红配白或金线条;果冻透明则让图案像浮在指甲上。</p>
<h2>耐用度</h2>
<p>彩绘在封层之下,与颜色同样持久;凸起的水钻最容易先掉。</p>'''
bai('nail-cay-thong-noel',T,X,
 A(('nail art manicure','Nail vẽ hoạ tiết cây thông Noel','Christmas tree nail art','크리스마스 트리 네일 아트','圣诞树美甲彩绘'),[]),
 ('Nail vẽ cây thông: ba cách rút gọn cho vừa móng',
  'Vẽ nguyên cây thông thường chiếm hết móng. Ba cách rút gọn, nền màu nào lên đẹp và lưu ý về độ bền khi đính đá.',
  'Nail vẽ cây thông Noel: 3 cách đơn giản | VESSCA',
  'Nail vẽ cây thông Noel: nét mảnh, cây nhỏ một móng hoặc kết hợp đá làm ngôi sao. Vẽ từ 10.000₫, sơn nền 130.000₫. VESSCA Bình Thạnh.',
  ['nail cây thông','nail vẽ Noel','nail Giáng sinh','vẽ nail Noel','nail Noel đẹp'],vi,faq),
 ('Christmas Tree Nail Art: Three Simplified Versions',
  'How salons simplify a Christmas tree, which base colours work and what lasts.',
  'Christmas Tree Nail Art | VESSCA','Christmas tree nail art in Saigon: fine lines, one accent nail or a stone star. Art from 10,000₫, gel base 130,000₫. VESSCA.',
  ['christmas nail art','christmas tree nails','nail salon Saigon'],en,
  [('How much is the art?','From 10,000₫ per nail, on top of the 130,000₫ gel base.'),('Do stones last?','Less than painted lines, especially with housework.')]),
 ('크리스마스 트리 네일: 단순화한 세 가지',
  '트리를 단순화하는 방법, 베이스 컬러, 지속력.',
  '크리스마스 트리 네일 | 호치민 VESSCA','호치민 크리스마스 트리 네일 아트: 얇은 라인, 포인트 한 손톱, 스톤 별. 아트 10,000₫부터.',
  ['크리스마스 네일','네일 아트','호치민 네일'],ko,
  [('아트 비용은요?','손톱당 10,000₫부터이며 젤 베이스 130,000₫에 더해집니다.'),('스톤은 오래가나요?','그림보다 빨리 떨어집니다.')]),
 ('圣诞树美甲:三种简化画法',
  '店里如何简化圣诞树、底色怎么选、耐久如何。',
  '圣诞树美甲 | 胡志明 VESSCA','胡志明圣诞树美甲:细线条、单指重点或水钻当星星。彩绘 10,000₫ 起,凝胶底 130,000₫。',
  ['圣诞美甲','圣诞树 美甲','胡志明 美甲'],zh,
  [('彩绘多少钱?','每指 10,000₫ 起,另加凝胶底色 130,000₫。'),('水钻耐用吗?','不如彩绘持久。')]))

# 2. Nail nhũ vàng Noel
vi = '''<p>Nhũ vàng là lựa chọn quen thuộc cho mùa lễ vì bắt sáng tốt dưới đèn tiệc và đèn trang trí. Điều quyết định bộ móng nhìn sang hay rối là độ mịn của nhũ và số móng bạn phủ.</p>

<h2>Ba mức nhũ</h2>

<table>
<thead><tr><th>Mức</th><th>Hiệu ứng</th><th>Hợp dịp</th></tr></thead>
<tbody>
<tr><td>Nhũ mịn phủ nhẹ</td><td>Ánh lấp lánh chỉ hiện khi bắt sáng</td><td>Đi làm, đi tiệc đều được</td></tr>
<tr><td>Nhũ phủ đậm một móng</td><td>Một móng nổi, chín móng còn lại trơn</td><td>Tiệc tối</td></tr>
<tr><td>Kim tuyến hạt to</td><td>Lấp lánh rõ, nhìn vui mắt</td><td>Tiệc cuối năm, chụp hình</td></tr>
</tbody>
</table>

<h2>Phối với màu nền</h2>

<ul>
<li><strong>Nền nude:</strong> nhũ vàng trông ấm và nhẹ, dễ mặc mọi bộ đồ.</li>
<li><strong>Nền đỏ rượu vang:</strong> cặp màu cổ điển của mùa lễ.</li>
<li><strong>Nền xanh rêu hoặc navy:</strong> nhũ vàng nổi bật hơn hẳn.</li>
<li><strong>Nền đen:</strong> rõ nhất, nhưng kén dịp.</li>
</ul>

<h2>Giá tham khảo</h2>

<p>Sơn gel trơn 130.000₫, mix thêm màu 10.000₫ mỗi màu. Các dòng sơn nhũ Hàn tiệm mang về như Aurora Queen là 280.000₫. Nếu chỉ muốn nhũ ở một móng, chi phí thường chỉ cộng thêm phần mix màu. Bảng giá đầy đủ ở trang <a href="/bang-gia/">bảng giá</a>.</p>

<h2>Lưu ý khi tháo</h2>

<p>Sơn có kim tuyến hạt to thường lâu tháo hơn sơn trơn vì lớp hạt cản dung dịch. Nếu bạn định đổi mẫu ngay sau mùa lễ, nhớ tính thêm thời gian cho bước phá gel 30.000₫. Vì sao bước này cần thời gian có ở bài <a href="/blog/vi-sao-thao-gel-mat-20-phut/">vì sao tháo gel mất 20 phút</a>.</p>'''
faq=[('Nail nhũ vàng hợp dịp nào?','Nhũ mịn hợp cả đi làm; nhũ đậm hoặc kim tuyến hạt to hợp tiệc tối và chụp hình.'),
('Giá bao nhiêu?','Sơn gel trơn 130.000₫, mix màu thêm 10.000₫; dòng nhũ Hàn Aurora Queen 280.000₫.'),
('Sơn kim tuyến có khó tháo không?','Lâu hơn sơn trơn vì lớp hạt cản dung dịch; phá gel là 30.000₫.')]
en='''<p>Gold shimmer suits the season because it catches party and fairy lights. Whether it reads elegant or busy depends on how fine the shimmer is and how many nails you cover.</p>
<h2>Three levels</h2>
<ul><li>Fine shimmer, light coverage — only shows in the light, fine for the office</li><li>Heavier shimmer on one nail, the rest plain — for the evening</li><li>Chunky glitter — the most festive, best for parties and photos</li></ul>
<h2>Base colours</h2>
<p>Nude feels warm and easy; burgundy is the classic pairing; moss green or navy makes gold pop; black is the strongest contrast.</p>
<h2>Prices and removal</h2>
<p>Gel 130,000₫, extra colours 10,000₫; the Korean Aurora Queen shimmer line 280,000₫. Chunky glitter takes longer to remove than plain colour (removal 30,000₫).</p>'''
ko='''<p>골드 펄은 파티 조명과 장식 불빛을 잘 받아 연말에 잘 어울립니다. 세련돼 보일지 복잡해 보일지는 펄의 입자와 바르는 손톱 수에 달려 있습니다.</p>
<h2>세 가지 강도</h2>
<ul><li>고운 펄을 얇게 — 빛을 받을 때만 반짝여 출근용으로도 좋습니다</li><li>한 손톱만 진한 펄, 나머지는 단색 — 저녁 자리에</li><li>굵은 글리터 — 가장 화려해 파티와 촬영에</li></ul>
<h2>베이스 컬러</h2>
<p>누드는 따뜻하고 무난하며, 버건디는 클래식한 조합, 모스그린이나 네이비는 골드를 돋보이게 하고, 블랙은 대비가 가장 강합니다.</p>
<h2>가격과 제거</h2>
<p>젤 130,000₫, 추가 컬러 10,000₫, 한국 오로라퀸 펄 라인 280,000₫. 굵은 글리터는 제거에 시간이 더 걸립니다(제거 30,000₫).</p>'''
zh='''<p>金色闪粉在派对灯与装饰灯下很出彩,很适合节日季。看起来高级还是杂乱,取决于闪粉的粗细和铺几指。</p>
<h2>三种程度</h2>
<ul><li>细闪粉薄涂——只在光下显现,上班也合适</li><li>仅一指重闪,其余单色——适合晚间</li><li>大颗亮片——最有节日感,适合派对与拍照</li></ul>
<h2>底色搭配</h2>
<p>裸色温柔百搭;酒红是经典组合;苔绿或藏青让金色更跳;黑色对比最强。</p>
<h2>价格与卸除</h2>
<p>凝胶 130,000₫,每增加一色 10,000₫;韩国 Aurora Queen 闪粉系列 280,000₫。大颗亮片比纯色更难卸(卸甲 30,000₫)。</p>'''
bai('nail-noel-nhu-vang',T,X,
 A(('dark glitter nails manicure','Nail nhũ vàng mùa lễ','Gold shimmer nails for the holidays','연말 골드 펄 네일','节日金色闪粉美甲'),[]),
 ('Nail nhũ vàng mùa Noel: ba mức nhũ và cách phối nền',
  'Nhũ vàng bắt sáng rất tốt dưới đèn tiệc. Ba mức nhũ từ nhẹ tới kim tuyến hạt to, cách phối với màu nền, giá và lưu ý khi tháo.',
  'Nail nhũ vàng mùa Noel: 3 mức nhũ | VESSCA',
  'Nail nhũ vàng mùa Noel: nhũ mịn, nhũ đậm một móng hay kim tuyến hạt to. Sơn gel 130.000₫, dòng nhũ Hàn Aurora Queen 280.000₫.',
  ['nail nhũ vàng','nail kim tuyến','nail Noel','nail ánh kim','nail đi tiệc'],vi,faq),
 ('Gold Shimmer Nails for the Holidays: Three Levels',
  'Fine shimmer to chunky glitter, base colours, prices and removal.',
  'Gold Shimmer Nails | VESSCA Saigon','Gold shimmer nails for the holidays in Saigon: fine shimmer, one heavy nail or chunky glitter. Gel 130,000₫, Aurora Queen 280,000₫.',
  ['glitter nails','gold nails','nail salon Saigon'],en,
  [('Which level for the office?','Fine shimmer with light coverage.'),('Is glitter harder to remove?','Yes, it takes longer than plain colour; removal is 30,000₫.')]),
 ('연말 골드 펄 네일: 세 가지 강도',
  '고운 펄부터 굵은 글리터까지, 베이스 컬러와 가격.',
  '골드 펄 네일 | 호치민 VESSCA','호치민 연말 골드 펄 네일: 고운 펄, 포인트 한 손톱, 굵은 글리터. 젤 130,000₫, 오로라퀸 280,000₫.',
  ['글리터 네일','골드 네일','호치민 네일'],ko,
  [('출근용은요?','고운 펄을 얇게 바르는 것이 좋습니다.'),('글리터는 제거가 어렵나요?','단색보다 오래 걸립니다. 제거 30,000₫.')]),
 ('节日金色闪粉美甲:三种程度',
  '从细闪到大颗亮片、底色搭配、价格与卸除。',
  '金色闪粉美甲 | 胡志明 VESSCA','胡志明节日金色闪粉美甲:细闪、单指重闪或大颗亮片。凝胶 130,000₫,Aurora Queen 280,000₫。',
  ['闪粉美甲','金色美甲','胡志明 美甲'],zh,
  [('上班选哪种?','细闪粉薄涂。'),('亮片难卸吗?','比纯色更花时间,卸甲 30,000₫。')]))

# 3. Nail bông tuyết
vi = '''<p>Bông tuyết là hoạ tiết Noel nhẹ nhàng hơn cây thông hay ông già Noel, hợp cả người thích tối giản. Nét vẽ mảnh, màu trắng hoặc bạc, đặt trên nền nhạt là cách phổ biến nhất.</p>

<h2>Ba kiểu bông tuyết</h2>

<table>
<thead><tr><th>Kiểu</th><th>Mô tả</th><th>Chi phí</th></tr></thead>
<tbody>
<tr><td>Một bông trên một móng</td><td>Chín móng trơn, một móng điểm bông tuyết</td><td>130.000₫ + vẽ từ 10.000₫</td></tr>
<tr><td>Bông nhỏ rải vài móng</td><td>Nhiều bông nhỏ, đặt lệch</td><td>130.000₫ + vẽ theo số móng</td></tr>
<tr><td>Bông tuyết tráng gương</td><td>Nét ánh bạc bắt sáng</td><td>Tráng gương từ 15.000₫</td></tr>
</tbody>
</table>

<h2>Nền hợp nhất</h2>

<ul>
<li><strong>Trắng trong như thạch:</strong> bông tuyết nổi mà không gắt.</li>
<li><strong>Xanh navy hoặc xám khói:</strong> giống bầu trời đêm mùa đông.</li>
<li><strong>Nude sữa:</strong> nhẹ nhất, hợp đi làm.</li>
</ul>

<h2>Nếu móng ngắn</h2>

<p>Móng ngắn nên vẽ một bông nhỏ, đặt lệch về một góc thay vì giữa móng, nhìn sẽ gọn hơn. Gợi ý đầy đủ cho móng ngắn có ở bài <a href="/blog/nail-noel-mong-ngan/">nail Noel cho móng ngắn</a>.</p>

<p>Gửi ảnh mẫu trước để kỹ thuật viên chuẩn bị màu, rồi <a href="/#booking">đặt lịch</a> hoặc gọi 0933.528.501. Mẫu tông trắng khác có ở bài <a href="/blog/nail-noel-trang-tuyet/">nail Noel tông trắng</a>.</p>'''
faq=[('Vẽ bông tuyết trên móng giá bao nhiêu?','Vẽ từ 10.000₫ mỗi móng, cộng vào nền sơn gel 130.000₫; nét tráng gương từ 15.000₫.'),
('Nền màu nào hợp bông tuyết?','Trắng trong, xanh navy, xám khói hoặc nude sữa.'),
('Móng ngắn vẽ bông tuyết được không?','Được, nên vẽ một bông nhỏ đặt lệch về một góc.')]
en='''<p>Snowflakes are a gentler holiday motif than trees or Santa, and they suit minimal taste: fine white or silver lines on a pale base.</p>
<h2>Three versions</h2>
<ul><li>One snowflake on a single nail (130,000₫ + from 10,000₫)</li><li>Small snowflakes scattered off-centre across a few nails</li><li>Chrome snowflakes that catch the light (from 15,000₫)</li></ul>
<h2>Best bases</h2>
<p>Clear jelly white, navy or smoky grey like a winter sky, or milky nude for the office.</p>
<h2>Short nails</h2>
<p>One small flake placed towards a corner reads neater than one in the middle.</p>'''
ko='''<p>눈꽃은 트리나 산타보다 은은한 모티프여서 미니멀한 취향에도 잘 맞습니다. 연한 베이스에 화이트나 실버 라인으로 그립니다.</p>
<h2>세 가지 방식</h2>
<ul><li>한 손톱에 눈꽃 하나(130,000₫ + 10,000₫부터)</li><li>작은 눈꽃을 몇 손톱에 치우쳐 배치</li><li>빛을 받는 크롬 눈꽃(15,000₫부터)</li></ul>
<h2>어울리는 베이스</h2>
<p>클리어 젤리 화이트, 겨울 하늘 같은 네이비나 스모키 그레이, 출근용으로는 밀키 누드.</p>
<h2>짧은 손톱</h2>
<p>가운데보다 한쪽 모서리에 작게 그리면 더 단정합니다.</p>'''
zh='''<p>雪花比圣诞树或圣诞老人更柔和,也适合极简风格:在浅色底上用白色或银色细线勾画。</p>
<h2>三种做法</h2>
<ul><li>一指画一片雪花(130,000₫ + 10,000₫ 起)</li><li>几指上零散偏放的小雪花</li><li>会反光的镜面雪花(15,000₫ 起)</li></ul>
<h2>适合的底色</h2>
<p>果冻透白、像冬夜天空的藏青或烟灰,上班可选奶裸色。</p>
<h2>短指甲</h2>
<p>把一片小雪花偏放到一角,比放中间更干净。</p>'''
bai('nail-hoa-tiet-bong-tuyet',T,X,
 A(('nail art manicure','Nail vẽ bông tuyết tông nhạt','Snowflake nail art on a pale base','연한 베이스의 눈꽃 네일','浅色底的雪花美甲'),[]),
 ('Nail bông tuyết: ba kiểu vẽ và nền màu hợp nhất',
  'Bông tuyết là hoạ tiết Noel nhẹ nhàng. Ba kiểu vẽ, nền màu hợp, chi phí và cách đặt hoạ tiết khi móng ngắn.',
  'Nail bông tuyết: 3 kiểu vẽ đẹp | VESSCA',
  'Nail vẽ bông tuyết: một bông một móng, bông nhỏ rải hoặc bông tráng gương. Vẽ từ 10.000₫, nền sơn gel 130.000₫. VESSCA Bình Thạnh.',
  ['nail bông tuyết','nail Noel','nail vẽ','nail Giáng sinh','nail mùa đông'],vi,faq),
 ('Snowflake Nail Art: Three Versions and the Best Bases',
  'A gentler holiday motif: three ways to wear snowflakes, bases and prices.',
  'Snowflake Nail Art | VESSCA Saigon','Snowflake nail art in Saigon: one flake, scattered small flakes or chrome flakes. Art from 10,000₫, gel base 130,000₫.',
  ['snowflake nails','christmas nail art','nail salon Saigon'],en,
  [('How much?','Art from 10,000₫ per nail plus the 130,000₫ gel base; chrome from 15,000₫.'),('Which base?','Clear white, navy, smoky grey or milky nude.')]),
 ('눈꽃 네일: 세 가지 방식과 어울리는 베이스',
  '은은한 연말 모티프, 눈꽃 그리는 세 가지 방법과 가격.',
  '눈꽃 네일 | 호치민 VESSCA','호치민 눈꽃 네일 아트: 한 송이, 작은 눈꽃 배치, 크롬 눈꽃. 아트 10,000₫부터.',
  ['눈꽃 네일','크리스마스 네일','호치민 네일'],ko,
  [('가격은요?','아트 10,000₫부터, 젤 베이스 130,000₫, 크롬 15,000₫부터.'),('어떤 베이스가 좋나요?','클리어 화이트, 네이비, 스모키 그레이, 밀키 누드.')]),
 ('雪花美甲:三种画法与合适底色',
  '更柔和的节日图案:三种雪花画法、底色与价格。',
  '雪花美甲 | 胡志明 VESSCA','胡志明雪花美甲:单片雪花、零散小雪花或镜面雪花。彩绘 10,000₫ 起,凝胶底 130,000₫。',
  ['雪花美甲','圣诞美甲','胡志明 美甲'],zh,
  [('多少钱?','彩绘每指 10,000₫ 起,凝胶底 130,000₫,镜面 15,000₫ 起。'),('配什么底色?','透白、藏青、烟灰或奶裸色。')]))

# 4. Gội đầu cho tóc nhanh bết
vi = '''<p>Tóc vừa gội hôm qua, hôm nay đã bết lại là chuyện nhiều người gặp, nhất là ở Sài Gòn nắng nóng và đi xe máy nhiều. Bài này nói về những nguyên nhân thường gặp, cách chăm ở nhà và gói gội đầu phù hợp.</p>

<h2>Vì sao tóc nhanh bết</h2>

<ul>
<li><strong>Da đầu tiết dầu nhiều:</strong> cơ địa, thời tiết nóng, đội mũ bảo hiểm lâu.</li>
<li><strong>Gội chưa sạch chân tóc:</strong> gội vội, chỉ xoa phần tóc chứ không massage da đầu.</li>
<li><strong>Dầu xả thoa lên da đầu:</strong> dầu xả nên thoa từ giữa thân tóc xuống ngọn.</li>
<li><strong>Sản phẩm tạo kiểu tích lại:</strong> sáp, keo dùng hằng ngày mà không làm sạch kỹ.</li>
<li><strong>Tay chạm tóc nhiều:</strong> vuốt tóc liên tục trong ngày.</li>
</ul>

<h2>Làm gì ở nhà</h2>

<p>Massage nhẹ da đầu bằng đầu ngón tay khi gội, không dùng móng. Xả thật kỹ cho hết dầu gội. Thoa dầu xả từ giữa thân tóc xuống. Giặt vỏ gối thường xuyên và để mũ bảo hiểm khô thoáng. Nếu da đầu ngứa, có mảng đỏ hoặc gàu nhiều kéo dài, nên đi khám bác sĩ da liễu thay vì đổi dầu gội liên tục.</p>

<h2>Gói gội đầu phù hợp</h2>

<table>
<thead><tr><th>Gói</th><th>Vì sao hợp</th><th>Giá</th></tr></thead>
<tbody>
<tr><td>Gói 02 · 50 phút</td><td>Có bước tẩy tế bào chết da đầu, làm sạch sâu hơn trước khi gội</td><td>229.000–279.000₫</td></tr>
<tr><td>Gói 01 · 30 phút</td><td>Gội hai lần, sấy ion âm, nhanh gọn</td><td>99.000–149.000₫</td></tr>
<tr><td>Thêm dịch vụ lẻ</td><td>Tẩy tế bào chết da đầu riêng</td><td>49.000₫</td></tr>
</tbody>
</table>

<p>Menu gợi ý dầu gội Nguyên Xuân bản vàng cho da đầu dễ bết. So sánh ba loại ở bài <a href="/blog/chon-dau-goi-nguyen-xuan-gung-sa-unove/">chọn dầu gội Nguyên Xuân, gừng sả hay Unove</a>, và quy trình Gói 02 ở bài <a href="/blog/goi-dau-massage-da-dau/">gội đầu massage da đầu</a>.</p>

<p>Bài viết chỉ mang tính tham khảo, không thay cho tư vấn của bác sĩ da liễu. Đặt lịch ở mục <a href="/#booking">Đặt lịch</a>.</p>'''
faq=[('Vì sao tóc nhanh bết?','Thường do da đầu tiết dầu nhiều, gội chưa sạch chân tóc, thoa dầu xả lên da đầu hoặc tích sản phẩm tạo kiểu.'),
('Gói gội nào hợp tóc nhanh bết?','Gói 02 có bước tẩy tế bào chết da đầu, 229.000–279.000₫; hoặc thêm dịch vụ lẻ tẩy tế bào chết da đầu 49.000₫.'),
('Dầu gội nào tiệm gợi ý?','Menu gợi ý Nguyên Xuân bản vàng cho da đầu dễ bết.'),
('Khi nào cần đi khám?','Khi da đầu ngứa, đỏ hoặc gàu nhiều kéo dài.')]
en='''<p>Hair that looks oily a day after washing is common, especially in Saigon heat and under a helmet.</p>
<h2>Common reasons</h2>
<ul><li>An oily scalp by nature, heat, or long hours in a helmet</li><li>Washing too quickly without massaging the scalp</li><li>Conditioner applied to the scalp instead of mid-length to ends</li><li>Styling products building up</li><li>Touching the hair throughout the day</li></ul>
<h2>At home</h2>
<p>Massage with fingertips, rinse thoroughly, keep conditioner off the scalp, wash pillowcases often and let the helmet dry out. For a persistently itchy or flaky scalp, see a dermatologist rather than switching shampoos again.</p>
<h2>Which package</h2>
<p>Package 02 (50 min, 229,000–279,000₫) includes scalp exfoliation; package 01 (30 min, from 99,000₫) is a quick deep wash; scalp exfoliation alone is a 49,000₫ add-on. This is general information, not medical advice.</p>'''
ko='''<p>감은 다음 날 바로 기름져 보이는 것은 흔한 일입니다. 호치민의 더위와 헬멧 착용도 영향을 줍니다.</p>
<h2>흔한 원인</h2>
<ul><li>지성 두피, 더위, 오래 쓰는 헬멧</li><li>두피를 마사지하지 않고 급히 감기</li><li>컨디셔너를 두피에 바르는 습관</li><li>스타일링 제품 잔여물</li><li>하루 종일 머리를 만지는 습관</li></ul>
<h2>집에서</h2>
<p>손끝으로 마사지하고 충분히 헹구며, 컨디셔너는 중간 길이부터 바르세요. 베갯잇을 자주 세탁하고 헬멧을 말려 주세요. 가려움이나 각질이 오래가면 피부과 진료를 받으세요.</p>
<h2>추천 코스</h2>
<p>02 코스(50분, 229,000–279,000₫)에 두피 스케일링이 포함됩니다. 01 코스는 30분 99,000₫부터, 두피 스케일링 단품은 49,000₫입니다. 의학적 조언은 아닙니다.</p>'''
zh='''<p>刚洗完第二天就出油很常见,尤其在胡志明的高温和长时间戴头盔的情况下。</p>
<h2>常见原因</h2>
<ul><li>头皮天生出油、天气热、长时间戴头盔</li><li>洗头太快,没有按摩头皮</li><li>护发素涂到头皮,而非中段至发尾</li><li>造型产品堆积</li><li>整天用手拨头发</li></ul>
<h2>在家怎么做</h2>
<p>用指腹按摩、彻底冲洗、护发素避开头皮、常洗枕套、让头盔保持干爽。若头皮持续发痒或头皮屑多,请就医,而不是不断换洗发水。</p>
<h2>合适的套餐</h2>
<p>套餐 02(50 分钟,229,000–279,000₫)含头皮去角质;套餐 01 为 30 分钟 99,000₫ 起;单做头皮去角质 49,000₫。本文仅供参考,不替代医生建议。</p>'''
bai('goi-dau-cho-toc-dau-nhanh-bet',T,G,
 A(('scalp massage','Chăm sóc da đầu cho tóc nhanh bết','Scalp care for hair that gets oily fast','쉽게 기름지는 두피 케어','易出油头皮的护理'),[]),
 ('Tóc nhanh bết: nguyên nhân thường gặp và gói gội đầu phù hợp',
  'Vì sao tóc vừa gội đã bết lại, nên chăm ở nhà thế nào, gói gội đầu nào có bước làm sạch da đầu và khi nào nên đi khám.',
  'Tóc nhanh bết: nguyên nhân và cách chăm | VESSCA',
  'Tóc nhanh bết do đâu, chăm ở nhà thế nào và gói gội đầu nào phù hợp. Gói có tẩy tế bào chết da đầu từ 229.000₫ tại VESSCA Bình Thạnh.',
  ['tóc nhanh bết','tóc bết','gội đầu cho tóc dầu','da đầu nhiều dầu','gội đầu thư giãn'],vi,faq),
 ('Hair That Gets Oily Fast: Common Reasons and What Helps',
  'Why hair looks oily a day after washing, what to do at home and which package helps.',
  'Oily Hair: Reasons and Care | VESSCA','Why hair gets oily fast in Saigon heat, what to change at home and which head spa package includes scalp exfoliation. From 99,000₫.',
  ['oily hair care','scalp care Saigon','head spa Saigon'],en,
  [('Which package helps?','Package 02 with scalp exfoliation, 229,000–279,000₫, or the 49,000₫ scalp exfoliation add-on.'),('When to see a doctor?','If the scalp stays itchy, red or flaky.')]),
 ('쉽게 기름지는 머리: 원인과 관리법',
  '감은 다음 날 기름지는 이유, 집에서 할 일, 어울리는 코스.',
  '지성 두피 관리 | 호치민 VESSCA','호치민의 더위에서 머리가 빨리 기름지는 이유와 집에서의 관리, 두피 스케일링 포함 코스 99,000₫부터.',
  ['지성 두피','호치민 헤드스파','두피 관리'],ko,
  [('어느 코스가 좋나요?','두피 스케일링이 포함된 02 코스 229,000–279,000₫ 또는 단품 49,000₫.'),('언제 병원에 가나요?','가려움, 붉어짐, 각질이 오래갈 때입니다.')]),
 ('头发容易出油:常见原因与护理',
  '为什么洗完第二天就油、在家怎么做、选哪个套餐。',
  '头发易出油怎么办 | 胡志明 VESSCA','胡志明高温下头发为何易出油、在家如何改善,以及含头皮去角质的套餐,99,000₫ 起。',
  ['头发出油','胡志明 头皮护理','胡志明 洗发'],zh,
  [('选哪个套餐?','含头皮去角质的套餐 02,229,000–279,000₫,或单项 49,000₫。'),('什么时候该就医?','头皮持续发痒、发红或头皮屑多时。')]))
