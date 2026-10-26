# -*- coding: utf-8 -*-
"""Giai đoạn 2 — đợt 1: 11/11, 13/11, 16/11, 18/11."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *

# ---------- 11/11 — Nail cho da ngăm ----------
vi='''<p>Da ngăm ăn được nhiều màu hơn da sáng, nhưng chọn sai thì tay trông xỉn đi. Nguyên tắc gọn: lấy màu có độ tương phản rõ với màu da, hoặc màu cùng tông ấm với da. Bài này liệt kê màu nên chọn, màu nên cân nhắc và lý do.</p>

<h2>Hai thứ quyết định màu có đẹp trên tay bạn</h2>

<p><strong>Độ tương phản</strong> là mức chênh sáng tối giữa màu sơn và màu da. Chênh rõ thì móng nổi, chênh ít thì móng lẫn vào tay. <strong>Tông nền</strong> (undertone) là sắc ngả ấm hay lạnh của da: da ngăm ở Việt Nam phần lớn ngả vàng hoặc ngả olive, tức tông ấm.</p>

<p>Da ngăm có sẵn độ sâu, nên màu đậm không làm tay tối thêm như nhiều người lo. Ngược lại, màu nhạt sát đúng tông da là nhóm dễ hỏng nhất, vì không đủ chênh để móng tách khỏi nền.</p>

<!--anh:1-->
<h2>Nhóm màu nổi trên da ngăm</h2>

<table>
<thead><tr><th>Nhóm màu</th><th>Vì sao hợp</th></tr></thead>
<tbody>
<tr><td>Đỏ gạch, đỏ rượu, đỏ cam</td><td>Cùng tông ấm với da, độ đậm cao nên tương phản rõ</td></tr>
<tr><td>Cam đất, nâu caramel, terracotta</td><td>Ngả vàng giống tông nền, tay trông ấm và đều màu</td></tr>
<tr><td>Xanh lá đậm, xanh rêu, xanh cổ vịt</td><td>Màu lạnh đậm đặt cạnh da ấm cho tương phản mạnh</td></tr>
<tr><td>Tím mận, tím nho</td><td>Đậm và ngả đỏ, ăn với tông da ngả vàng</td></tr>
<tr><td>Trắng sữa, trắng ngà</td><td>Tương phản sáng tối cao nhất, làm ngón trông dài hơn</td></tr>
<tr><td>Nhũ vàng đồng, xà cừ ánh trai</td><td>Ánh kim ấm bắt sáng, tôn nền da ngăm</td></tr>
</tbody>
</table>

<h2>Nhóm màu nên cân nhắc</h2>

<ul>
<li><strong>Nude hồng nhạt sát tông da.</strong> Đây là lỗi hay gặp nhất. Móng gần như biến mất, tay trông thiếu sức sống. Nếu thích nude, chọn nude đậm hơn da một bậc, ngả nâu hoặc ngả cam thay vì ngả hồng. Xem thêm <a href="/blog/nail-nude-kieu-han/">nail nude kiểu Hàn</a>.</li>
<li><strong>Pastel lạnh nhạt</strong> như xanh baby, tím lavender nhạt. Tông lạnh nhạt đặt trên da ấm dễ cho cảm giác bạc màu. Muốn pastel thì lấy bản đục sữa, độ đậm cao hơn.</li>
<li><strong>Xám tro nhạt, be xám.</strong> Thiếu cả tương phản lẫn độ ấm, thường làm tay trông xám.</li>
</ul>

<p>Đây là gợi ý chung, không phải luật. Nếu bạn thích một màu trong nhóm cân nhắc, kỹ thuật viên có thể xử lý bằng cách tăng độ đậm, thêm lớp nhũ mảnh, hoặc chỉ dùng màu đó cho một hai ngón nhấn.</p>

<!--anh:2-->
<h2>Cách thử trước khi quyết</h2>

<p>Đặt chai sơn hoặc tấm màu mẫu áp sát mu bàn tay, dưới ánh sáng tự nhiên cạnh cửa sổ, không phải dưới đèn vàng. Nhìn vào mức chênh giữa màu và da: thấy ranh giới rõ là đủ tương phản. So hai ba màu cạnh nhau sẽ dễ thấy hơn so từng màu một.</p>

<p>Tại VESSCA, bạn có thể đề nghị kỹ thuật viên áp tấm màu lên tay trước khi sơn, và đổi màu nếu thấy chưa hợp. Cách kỹ thuật viên cân màu cho từng khách được nói kỹ hơn trong bài <a href="/blog/ky-thuat-vien-chon-mau-nail/">kỹ thuật viên chọn màu nail dựa trên gì</a>. Nếu muốn so sánh theo tông da nói chung, đọc <a href="/blog/nail-mau-gi-hop-tong-da/">nail màu gì hợp tông da</a>.</p>

<p>Giá sơn gel trơn tại tiệm 130.000₫, mix từ hai màu cộng thêm 10.000₫ mỗi màu, xà cừ ánh trai và nhũ AURORA QUEEN 280.000₫.</p>'''
faq=[('Da ngăm nên sơn màu gì?','Đỏ gạch, đỏ rượu, cam đất, nâu caramel, xanh lá đậm, tím mận, trắng sữa và nhũ vàng đồng đều nổi trên da ngăm.'),
 ('Da ngăm sơn màu nude được không?','Được, nhưng nên chọn nude đậm hơn da một bậc và ngả nâu hoặc ngả cam, tránh nude hồng nhạt sát tông da.'),
 ('Vì sao màu pastel nhạt trông xỉn trên da ngăm?','Pastel lạnh nhạt thiếu độ tương phản với da tông ấm, nên móng dễ cho cảm giác bạc màu. Bản pastel đục sữa đậm hơn sẽ hợp hơn.'),
 ('Thử màu thế nào cho chắc?','Áp tấm màu lên mu bàn tay dưới ánh sáng tự nhiên và so hai ba màu cạnh nhau, không thử dưới đèn vàng.')]
en='''<p>Deeper skin tones carry more colours than fair skin, but the wrong shade makes hands look dull. The rule: pick a colour with clear contrast against your skin, or one that shares its warm undertone.</p>
<h2>What decides it</h2>
<p>Contrast is the lightness gap between polish and skin. Undertone is whether skin leans warm or cool — most deeper Vietnamese skin leans yellow or olive, so warm.</p>
<!--anh:1-->
<h2>Shades that work</h2>
<table>
<thead><tr><th>Family</th><th>Why</th></tr></thead>
<tbody>
<tr><td>Brick red, wine, red-orange</td><td>Warm and deep, strong contrast</td></tr>
<tr><td>Terracotta, caramel brown</td><td>Shares the yellow undertone</td></tr>
<tr><td>Deep green, teal</td><td>Cool and dark against warm skin</td></tr>
<tr><td>Plum, grape purple</td><td>Deep with a red lean</td></tr>
<tr><td>Milky white, ivory</td><td>Highest contrast, lengthens fingers</td></tr>
<tr><td>Bronze shimmer, pearl</td><td>Warm metallics catch light</td></tr>
</tbody>
</table>
<h2>Shades to reconsider</h2>
<p>Pale pink nudes that match your skin exactly make nails disappear — go one shade deeper and lean brown or peach. Cool pastels and pale grey-beige often read washed out; milky, denser versions work better.</p>
<!--anh:2-->
<h2>How to test</h2>
<p>Hold the colour against the back of your hand in daylight, not under warm lamps, and compare two or three shades side by side. At VESSCA you can ask your technician to test swatches before applying. Plain gel is 130,000₫, mixing two colours adds 10,000₫ per colour, pearl and AURORA QUEEN shimmer 280,000₫.</p>'''
ko='''<p>어두운 톤의 피부는 밝은 피부보다 소화하는 색이 많지만, 잘못 고르면 손이 탁해 보입니다. 기준은 피부와 명도 차가 분명한 색, 또는 피부와 같은 웜톤 색입니다.</p>
<h2>무엇이 결정하나</h2>
<p>명도 차는 컬러와 피부의 밝기 차이입니다. 언더톤은 피부가 웜인지 쿨인지이며, 베트남의 어두운 톤 피부는 대부분 노란빛 또는 올리브빛 웜톤입니다.</p>
<!--anh:1-->
<h2>잘 어울리는 색</h2>
<table>
<thead><tr><th>계열</th><th>이유</th></tr></thead>
<tbody>
<tr><td>브릭 레드, 와인, 레드오렌지</td><td>웜하고 진해 명도 차가 큼</td></tr>
<tr><td>테라코타, 카라멜 브라운</td><td>노란 언더톤과 같은 계열</td></tr>
<tr><td>딥그린, 틸</td><td>웜톤 피부에 쿨한 어두운 색이 대비됨</td></tr>
<tr><td>플럼, 그레이프 퍼플</td><td>붉은 기가 있는 진한 색</td></tr>
<tr><td>밀키 화이트, 아이보리</td><td>대비가 가장 크고 손가락이 길어 보임</td></tr>
<tr><td>브론즈 펄, 자개</td><td>웜한 메탈이 빛을 받음</td></tr>
</tbody>
</table>
<h2>다시 생각할 색</h2>
<p>피부색과 똑같은 연한 핑크 누드는 손톱이 사라져 보입니다. 한 톤 진하게, 브라운이나 피치 쪽으로 고르세요. 쿨한 파스텔과 연한 그레이 베이지는 색이 빠져 보이기 쉬우니 밀키한 버전이 낫습니다.</p>
<!--anh:2-->
<h2>테스트 방법</h2>
<p>자연광에서 손등에 컬러를 대고 두세 가지를 나란히 비교하세요. VESSCA에서는 시술 전 컬러칩 테스트를 요청할 수 있습니다. 단색 젤 130,000₫, 두 색 믹스는 색당 10,000₫ 추가, 자개와 AURORA QUEEN 펄 280,000₫.</p>'''
zh='''<p>深肤色比浅肤色能驾驭更多颜色,但选错会让手显得暗沉。原则是:挑与肤色明度差明显的颜色,或与肤色同为暖调的颜色。</p>
<h2>两个决定因素</h2>
<p>明度差是甲油与皮肤的亮暗差距。底调是皮肤偏暖还是偏冷,越南的深肤色多偏黄或偏橄榄,属暖调。</p>
<!--anh:1-->
<h2>显白的色系</h2>
<table>
<thead><tr><th>色系</th><th>原因</th></tr></thead>
<tbody>
<tr><td>砖红、酒红、橘红</td><td>暖而深,明度差大</td></tr>
<tr><td>陶土色、焦糖棕</td><td>与偏黄底调一致</td></tr>
<tr><td>墨绿、蓝绿</td><td>冷调深色与暖调皮肤形成对比</td></tr>
<tr><td>梅子紫、葡萄紫</td><td>深且偏红</td></tr>
<tr><td>奶白、象牙白</td><td>对比最强,手指显长</td></tr>
<tr><td>古铜亮粉、贝壳光</td><td>暖调金属感反光</td></tr>
</tbody>
</table>
<h2>需要斟酌的颜色</h2>
<p>与肤色完全接近的浅粉裸色会让指甲消失,建议深一个色阶并偏棕或偏橘。冷调马卡龙色和浅灰米色容易显得掉色,奶油质地的浓一些的版本更合适。</p>
<!--anh:2-->
<h2>怎么试色</h2>
<p>在自然光下把颜色贴在手背上,两三个颜色并排比较,不要在暖黄灯下试。在 VESSCA 可以请美甲师先用色卡试色。纯色甲油胶 130,000₫,混两色每色加 10,000₫,贝壳光与 AURORA QUEEN 亮粉 280,000₫。</p>'''
bai('nail-cho-da-ngam','2026-11-11T08:30:00+07:00','Xu hướng & Cảm hứng',
 A(('brick red nails manicure','Móng sơn đỏ gạch trên tay da ngăm','Brick red manicure on deeper skin','어두운 톤 피부의 브릭 레드 네일','深肤色手上的砖红色美甲'),
   [('caramel brown nails manicure','Móng nâu caramel tông đất cho da ngăm','Caramel brown nails for deeper skin','어두운 톤에 어울리는 카라멜 브라운 네일','适合深肤色的焦糖棕美甲'),
    ('milky white nails manicure','Móng trắng sữa làm ngón tay trông dài hơn','Milky white nails lengthening the fingers','손가락을 길어 보이게 하는 밀키 화이트 네일','让手指显长的奶白色美甲')]),
 ('Nail cho da ngăm: màu nào nổi, màu nào nên cân nhắc','Màu nail đẹp trên da ngăm theo độ tương phản và tông nền: đỏ gạch, cam đất, xanh lá đậm, trắng sữa; nhóm nude nhạt và pastel lạnh nên cân nhắc.',
  'Nail cho da ngăm: màu nào nổi nhất | VESSCA',
  'Da ngăm nổi với đỏ gạch, cam đất, xanh lá đậm, tím mận, trắng sữa, nhũ đồng. Nude hồng nhạt và pastel lạnh nên cân nhắc. Gel trơn 130.000₫. VESSCA Bình Thạnh.',
  ['nail cho da ngăm','màu nail da ngăm','da ngăm sơn màu gì','nail đẹp cho da ngăm','màu sơn tôn da ngăm'],vi,faq),
 ('Nail Colours for Deeper Skin Tones','Which shades stand out on deeper skin and which to reconsider, based on contrast and undertone.',
  'Nail Colours for Deeper Skin | VESSCA Saigon','Brick red, terracotta, deep green, plum and milky white stand out on deeper skin; pale pink nudes disappear. Gel from 130,000₫. VESSCA, Binh Thanh.',
  ['nail colours deeper skin','nail salon Binh Thanh','Korean nails Saigon','gel manicure Ho Chi Minh City','nude nails tan skin'],en,
  [('What colours suit deeper skin?','Brick red, wine, terracotta, caramel, deep green, plum, milky white and bronze shimmer.'),('Can I wear nude?','Yes, one shade deeper than your skin and leaning brown or peach rather than pink.'),('How do I test a shade?','Hold it against the back of your hand in daylight and compare a few side by side.')]),
 ('어두운 톤 피부에 어울리는 네일 컬러','명도 차와 언더톤 기준으로 어두운 톤 피부에 잘 받는 색과 다시 생각할 색.',
  '어두운 톤 피부 네일 컬러 | 호치민 VESSCA','브릭 레드, 테라코타, 딥그린, 플럼, 밀키 화이트가 잘 받습니다. 연한 핑크 누드는 피하세요. 단색 젤 130,000₫. 호치민 빈탄 VESSCA.',
  ['어두운 피부 네일','네일 컬러 추천','호치민 네일샵','빈탄 네일','한국 젤네일 호치민'],ko,
  [('어두운 톤에 어울리는 색은?','브릭 레드, 와인, 테라코타, 카라멜, 딥그린, 플럼, 밀키 화이트, 브론즈 펄입니다.'),('누드도 가능한가요?','피부보다 한 톤 진하고 브라운이나 피치 쪽이면 좋습니다.'),('어떻게 테스트하나요?','자연광에서 손등에 대고 두세 색을 나란히 비교하세요.')]),
 ('深肤色适合的美甲颜色','按明度差和底调,深肤色显白的颜色与需要斟酌的颜色。',
  '深肤色美甲颜色 | 胡志明 VESSCA','砖红、陶土色、墨绿、梅子紫、奶白在深肤色上很显色,浅粉裸色会让指甲消失。纯色 130,000₫。胡志明平盛郡 VESSCA。',
  ['深肤色 美甲','美甲颜色 推荐','胡志明 美甲','平盛郡 美甲店','韩式美甲 胡志明'],zh,
  [('深肤色适合什么颜色?','砖红、酒红、陶土色、焦糖棕、墨绿、梅子紫、奶白和古铜亮粉。'),('可以做裸色吗?','可以,选比肤色深一个色阶并偏棕或偏橘。'),('怎么试色?','在自然光下贴着手背,两三个颜色并排比较。')]))
