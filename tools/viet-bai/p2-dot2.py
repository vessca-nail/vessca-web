# -*- coding: utf-8 -*-
"""Giai đoạn 2 — đợt 2: 18/11, 20/11, 23/11."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *

# ---------- 18/11 — Tự làm ở nhà hay ra tiệm ----------
vi='''<p>Câu trả lời ngắn: sơn thường, dưỡng móng và cắt móng làm ở nhà rất ổn; sơn gel, tháo gel, nối móng và cắt da nên để tiệm. Lý do không phải vì khó học, mà vì ba việc sau cần đèn, cần dụng cụ tiệt trùng và cần nhìn thấy rõ phần mình đang xử lý. Bài này phân tách từng việc để bạn biết nên tự làm tới đâu.</p>

<h2>Việc nào ở nhà cũng tốt</h2>

<ul>
<li><strong>Cắt và dũa móng.</strong> Chỉ cần cắt đúng nguyên tắc và dũa một chiều. Xem bài <a href="/blog/cat-mong-tay-dung-cach/">cắt móng tay đúng cách</a>.</li>
<li><strong>Dưỡng viền móng.</strong> Dầu dưỡng bôi hằng ngày hiệu quả hơn bất kỳ buổi làm nail nào, vì đây là việc của sự đều đặn. Xem <a href="/blog/dau-duong-vien-mong-cuticle-oil/">dầu dưỡng viền móng</a>.</li>
<li><strong>Sơn thường.</strong> Khô bằng bay hơi, không cần thiết bị, sơn lệch thì lau lại được.</li>
<li><strong>Sơn cứng móng.</strong> Dùng khi đang nghỉ gel, bôi như sơn thường.</li>
</ul>

<!--anh:1-->
<h2>Việc nào nên để tiệm</h2>

<table>
<thead><tr><th>Việc</th><th>Vì sao khó tự làm</th></tr></thead>
<tbody>
<tr><td>Sơn gel</td><td>Cần đèn LED hoặc UV đúng công suất. Gel phải phủ mỏng, nhiều lớp, và không được chạm viền da — gel chạm da là nguyên nhân chính gây dị ứng</td></tr>
<tr><td>Tháo gel</td><td>Phải dũa đúng lớp top rồi ủ dung dịch khoảng 20 phút. Nóng tay bóc ra là cách làm mỏng móng nhanh nhất</td></tr>
<tr><td>Cắt da</td><td>Dụng cụ phải tiệt trùng, và cắt sai sẽ chảy máu hoặc tạo đường vào cho vi khuẩn</td></tr>
<tr><td>Nối móng, úp móng, đắp gel</td><td>Cần tạo form cân đối và dán đúng độ cong của móng thật, tay không nghề sẽ bị lệch trục</td></tr>
<tr><td>Dũa bề mặt móng</td><td>Dũa quá tay làm mỏng móng thật, và tổn thương này phải chờ móng mọc mới hết</td></tr>
</tbody>
</table>

<h2>So chi phí cho đúng</h2>

<p>Nhiều người so giá một bộ gel ở tiệm với giá một bộ kit ở nhà và thấy kit rẻ hơn. Phép so này thiếu vài khoản. Bộ kit cần đèn, base, top, màu, dung dịch tháo, dũa, và cần mua lại khi hết. Quan trọng hơn, kit không gồm phần khó nhất là tay nghề, nên hai ba bộ đầu thường phải tháo sớm.</p>

<p>Tại VESSCA, sơn gel trơn 130.000₫, thạch 150.000₫, mắt mèo và nhũ 170.000₫. Phá gel hoặc tháo móng úp 30.000₫, mất khoảng 20 phút. Cắt da, chỉnh form, dưỡng viền tay 60.000₫. Bạn cũng không phải tự chịu rủi ro dũa quá tay.</p>

<!--anh:2-->
<h2>Cách chia hợp lý nhất</h2>

<p>Cách tiết kiệm mà vẫn giữ móng khoẻ là: ra tiệm cho phần cần thiết bị và tay nghề, còn ở nhà lo phần cần đều đặn. Cụ thể là làm gel ở tiệm mỗi hai đến ba tuần, và giữa hai lần đó bôi dầu dưỡng hằng ngày, đeo bao tay khi làm việc nhà, không dùng móng để cạy mở. Lịch chăm giữa hai lần làm nail có trong bài <a href="/blog/lich-duong-mong-giua-hai-lan-lam-nail/">lịch dưỡng móng 4 tuần</a>.</p>

<p>Nếu bạn vẫn muốn tự tháo gel ở nhà, các bước an toàn và những lỗi thường gặp nằm trong bài <a href="/blog/tu-thao-gel-o-nha-co-duoc-khong/">tự tháo gel ở nhà có được không</a>. Về tiêu chuẩn tiệt trùng dụng cụ, xem <a href="/blog/may-tiet-trung-dung-cu-nail/">máy tiệt trùng dụng cụ nail</a>.</p>'''
faq=[('Tự làm nail ở nhà có rẻ hơn ra tiệm không?','Khi cộng đủ đèn, base, top, màu, dung dịch tháo và phần phải mua lại thì chênh lệch nhỏ hơn nhiều so với cảm giác ban đầu, chưa kể các bộ đầu thường phải tháo sớm.'),
 ('Việc nào ở nhà làm được?','Cắt và dũa móng, bôi dầu dưỡng viền móng, sơn thường và sơn cứng móng.'),
 ('Vì sao không nên tự cắt da ở nhà?','Vì dụng cụ cần được tiệt trùng và cắt sai dễ gây chảy máu hoặc tạo đường cho vi khuẩn vào.'),
 ('Tự sơn gel ở nhà có hại móng không?','Bản thân gel không hại. Rủi ro nằm ở dũa quá tay, gel chạm viền da gây dị ứng, và bóc gel khi tháo.')]
en='''<p>Short answer: regular polish, cuticle oil and nail trimming are fine at home; gel application, gel removal, extensions and cuticle cutting belong in a salon. Not because they are hard to learn, but because they need a lamp, sterilised tools and a clear view of what you are working on.</p>
<h2>Fine at home</h2>
<p>Trimming and filing, daily cuticle oil, regular polish and nail strengthener all work well at home. Daily oil does more for nail condition than any single salon visit, because it depends on consistency.</p>
<!--anh:1-->
<h2>Better in a salon</h2>
<table>
<thead><tr><th>Task</th><th>Why</th></tr></thead>
<tbody>
<tr><td>Gel application</td><td>Needs a proper LED or UV lamp, thin layers, and gel kept off the skin — skin contact is the main cause of allergy</td></tr>
<tr><td>Gel removal</td><td>File the top layer, then soak about 20 minutes. Peeling it off thins the nail fast</td></tr>
<tr><td>Cuticle cutting</td><td>Tools must be sterilised, and a wrong cut bleeds or opens a path for bacteria</td></tr>
<tr><td>Extensions</td><td>Needs a balanced form matched to the curve of your own nail</td></tr>
<tr><td>Surface filing</td><td>Over-filing thins the natural nail and only grows out</td></tr>
</tbody>
</table>
<h2>Comparing cost properly</h2>
<p>A home kit looks cheaper than a salon set until you add the lamp, base, top, colours, remover and refills — and it does not include the skill, so the first sets often come off early. At VESSCA plain gel is 130,000₫, jelly 150,000₫, cat-eye or shimmer 170,000₫, removal 30,000₫ in about 20 minutes, hand cuticle work 60,000₫.</p>
<!--anh:2-->
<h2>The sensible split</h2>
<p>Salon for what needs equipment and skill, home for what needs consistency: a gel set every two to three weeks, plus daily oil, gloves for housework, and never using nails as tools.</p>'''
ko='''<p>짧은 답: 일반 폴리시, 큐티클 오일, 손톱 길이 정리는 집에서 충분합니다. 젤 시술과 제거, 연장, 큐티클 정리는 샵이 맞습니다. 배우기 어려워서가 아니라 램프, 멸균 도구, 그리고 작업 부위를 또렷이 보는 조건이 필요하기 때문입니다.</p>
<h2>집에서 해도 되는 것</h2>
<p>길이 정리와 파일링, 매일 바르는 큐티클 오일, 일반 폴리시, 네일 강화제입니다. 매일 바르는 오일은 한 번의 샵 방문보다 손톱 상태에 더 큰 영향을 줍니다.</p>
<!--anh:1-->
<h2>샵이 나은 것</h2>
<table>
<thead><tr><th>작업</th><th>이유</th></tr></thead>
<tbody>
<tr><td>젤 시술</td><td>적정 LED·UV 램프, 얇은 여러 층, 피부에 닿지 않게 — 피부 접촉이 알레르기의 주원인</td></tr>
<tr><td>젤 제거</td><td>탑층을 갈고 약 20분 불림. 뜯어내면 손톱이 빠르게 얇아짐</td></tr>
<tr><td>큐티클 정리</td><td>도구 멸균 필요, 잘못 자르면 출혈이나 감염 경로</td></tr>
<tr><td>연장</td><td>본인 손톱 커브에 맞춘 균형 잡힌 폼이 필요</td></tr>
<tr><td>표면 파일링</td><td>과하면 자연 손톱이 얇아지고 자라야 회복</td></tr>
</tbody>
</table>
<h2>비용 비교</h2>
<p>홈 키트는 램프, 베이스, 탑, 컬러, 리무버, 리필을 더하면 생각보다 차이가 적고 기술은 포함되지 않습니다. VESSCA 단색 젤 130,000₫, 시럽 150,000₫, 자석·펄 170,000₫, 제거 30,000₫(약 20분), 손 큐티클 정리 60,000₫.</p>
<!--anh:2-->
<h2>합리적인 분담</h2>
<p>장비와 기술이 필요한 것은 샵, 꾸준함이 필요한 것은 집. 2–3주마다 젤 시술, 매일 오일, 집안일 때 장갑, 손톱을 도구로 쓰지 않기입니다.</p>'''
zh='''<p>简短回答:普通指甲油、护甲油和修剪长度在家做完全可以;上甲油胶、卸甲、延长和修死皮建议交给店里。不是因为难学,而是这些需要灯具、灭菌工具,以及能看清操作部位。</p>
<h2>在家可以做的</h2>
<p>修剪与打磨、每天涂护甲油、普通指甲油和护甲底油。每天涂油对指甲状态的作用大于任何一次到店护理,因为它靠的是持续。</p>
<!--anh:1-->
<h2>建议到店做的</h2>
<table>
<thead><tr><th>项目</th><th>原因</th></tr></thead>
<tbody>
<tr><td>上甲油胶</td><td>需要合适的 LED 或 UV 灯、薄涂多层,并避免碰到皮肤——碰皮肤是过敏主因</td></tr>
<tr><td>卸甲</td><td>先磨封层再浸泡约 20 分钟。硬撕会让甲面迅速变薄</td></tr>
<tr><td>修死皮</td><td>工具必须灭菌,剪错会出血或留下感染途径</td></tr>
<tr><td>延长甲</td><td>需要贴合自身甲面弧度的均衡甲型</td></tr>
<tr><td>打磨甲面</td><td>过度打磨会让真甲变薄,只能等它长出来</td></tr>
</tbody>
</table>
<h2>正确地算成本</h2>
<p>家用套装看着便宜,但加上灯、底胶、封层、颜色、卸甲水和补货后差距不大,而且不含手艺,前几副往往提早脱落。VESSCA 纯色胶 130,000₫,果冻 150,000₫,猫眼或亮粉 170,000₫,卸甲 30,000₫(约 20 分钟),手部死皮护理 60,000₫。</p>
<!--anh:2-->
<h2>合理的分工</h2>
<p>需要设备与手艺的交给店里,需要坚持的在家做:每 2–3 周做一次甲油胶,平时每天涂护甲油、做家务戴手套、不用指甲当工具。</p>'''
bai('lam-nail-o-nha-hay-o-tiem','2026-11-18T08:30:00+07:00','Hỏi & Đáp',
 A(('manicure salon table nails','Kỹ thuật viên làm nail tại tiệm','Technician working at a salon table','샵에서 네일 시술 중','美甲师在店内操作'),
   [('nail polish bottles home manicure','Bộ sơn thường tự làm ở nhà','Regular polish for home use','집에서 쓰는 일반 폴리시','在家使用的普通指甲油'),
    ('gel manicure lamp nails','Hơ gel dưới đèn LED tại tiệm','Curing gel under a LED lamp','샵의 LED 램프 경화','店内 LED 灯照干甲油胶')]),
 ('Làm nail ở nhà hay ra tiệm: việc nào nên tự, việc nào không','Phân tách từng việc: cắt dũa, dưỡng viền và sơn thường làm ở nhà tốt; sơn gel, tháo gel, cắt da và nối móng nên để tiệm, kèm so sánh chi phí thật.',
  'Làm nail ở nhà hay ra tiệm | VESSCA',
  'Cắt dũa, dưỡng viền, sơn thường tự làm được. Sơn gel, tháo gel, cắt da nên ra tiệm. Gel trơn 130.000₫, tháo 30.000₫. VESSCA Bình Thạnh.',
  ['làm nail ở nhà hay ra tiệm','tự làm nail tại nhà','tự sơn gel ở nhà','bộ kit làm nail tại nhà','có nên tự cắt da'],vi,faq),
 ('DIY Nails at Home or Go to a Salon?','Which tasks work at home, which need a salon, and an honest cost comparison.',
  'Home Manicure or Salon? | VESSCA Saigon','Trimming, cuticle oil and regular polish work at home. Gel, removal and cuticle cutting need a salon. Gel 130,000₫, removal 30,000₫. VESSCA, Binh Thanh.',
  ['DIY nails at home','nail salon Binh Thanh','gel manicure Ho Chi Minh City','Korean nails Saigon','home gel kit'],en,
  [('Is doing nails at home cheaper?','Less than it first looks once you add the lamp, base, top, colours and refills, and the kit does not include skill.'),('What can I do at home?','Trimming and filing, daily cuticle oil, regular polish and nail strengthener.'),('Why not cut cuticles at home?','Tools need sterilising and a wrong cut bleeds or opens a path for bacteria.')]),
 ('집에서 셀프 네일 vs 샵 방문','집에서 해도 되는 작업과 샵이 필요한 작업, 그리고 솔직한 비용 비교.',
  '셀프 네일과 샵 비교 | 호치민 VESSCA','길이 정리, 큐티클 오일, 일반 폴리시는 집에서. 젤, 제거, 큐티클 정리는 샵에서. 젤 130,000₫, 제거 30,000₫. 호치민 빈탄 VESSCA.',
  ['셀프 네일','홈 젤네일','호치민 네일샵','빈탄 네일','한국 젤네일 호치민'],ko,
  [('집에서 하면 더 저렴한가요?','램프와 베이스, 탑, 컬러, 리필을 더하면 차이가 크지 않고 기술은 포함되지 않습니다.'),('집에서 가능한 작업은?','길이 정리와 파일링, 매일 큐티클 오일, 일반 폴리시, 강화제입니다.'),('큐티클은 왜 집에서 안 되나요?','도구 멸균이 필요하고 잘못 자르면 출혈이나 감염 위험이 있습니다.')]),
 ('在家自己做还是去美甲店','哪些项目在家可以做、哪些需要到店,以及一份实在的成本对比。',
  '在家做美甲还是去店里 | 胡志明 VESSCA','修剪、护甲油、普通指甲油在家可做。甲油胶、卸甲、修死皮建议到店。纯色 130,000₫,卸甲 30,000₫。胡志明平盛郡 VESSCA。',
  ['自己做美甲','胡志明 美甲','平盛郡 美甲店','韩式美甲 胡志明','家用美甲套装'],zh,
  [('在家做更便宜吗?','加上灯、底胶、封层、颜色和补货后差距不大,而且不含手艺。'),('在家能做什么?','修剪打磨、每天涂护甲油、普通指甲油和护甲底油。'),('为什么不建议在家修死皮?','工具需要灭菌,剪错会出血或留下感染途径。')]))

# ---------- 20/11 — Nail cho ngón tay ngắn ----------
vi='''<p>Ngón tay ngắn không bị giới hạn kiểu nail, nhưng có một nguyên tắc giúp tay trông dài hơn: <strong>mọi đường kẻ nên chạy dọc, và phần da hở ở hai bên móng nên ít nhất có thể</strong>. Bài này nói rõ chọn form nào, dài bao nhiêu, màu nào và kiểu vẽ nào theo nguyên tắc đó.</p>

<h2>Vì sao đường dọc làm ngón trông dài</h2>

<p>Mắt đọc chiều dài theo đường mà nó lần theo được. Đường kẻ dọc, dải màu dọc hay ombre chuyển từ gốc ra đầu móng đều kéo mắt đi theo chiều dài ngón. Ngược lại, đường kẻ ngang, viền French quá dày hay khối màu đậm nằm chắn ngang đầu móng sẽ cắt ngón thành từng đoạn ngắn.</p>

<p>Thứ hai là phần móng lộ ra. Khi sơn, nếu chừa khoảng trống hai bên cạnh móng, phần da hở đó làm móng trông hẹp và ngắn. Sơn sát hai cạnh, chỉ chừa viền rất mảnh ở gốc, sẽ tận dụng hết diện tích móng.</p>

<!--anh:1-->
<h2>Form và độ dài</h2>

<table>
<thead><tr><th>Yếu tố</th><th>Nên</th><th>Nên cân nhắc</th></tr></thead>
<tbody>
<tr><td>Form</td><td>Oval, almond nhẹ — đầu móng thu lại tạo cảm giác thuôn</td><td>Vuông cạnh sắc, làm móng trông bè ngang</td></tr>
<tr><td>Độ dài</td><td>Dài hơn đầu ngón 2–4 mm, đủ để thấy chiều dài</td><td>Dài quá tỉ lệ, dễ gãy và vướng</td></tr>
<tr><td>Hai cạnh</td><td>Dũa thẳng, không thu hẹp thân móng</td><td>Dũa vào hai bên thân móng cho nhọn</td></tr>
<tr><td>Viền gốc</td><td>Chừa viền mảnh, sơn sát cạnh</td><td>Chừa trống rộng quanh móng</td></tr>
</tbody>
</table>

<p>So sánh đầy đủ giữa các form có trong bài <a href="/blog/form-mong-oval-vuong-almond/">form móng oval, vuông, almond</a>.</p>

<h2>Màu và kiểu vẽ</h2>

<ul>
<li><strong>Tông sáng và trung tính</strong> như nude ngả hồng, be sữa, trắng ngà làm móng và ngón liền mạch về màu, nên trông dài hơn.</li>
<li><strong>Ombre dọc</strong> chuyển màu từ gốc ra đầu móng là kiểu ăn nhất với ngón ngắn. Xem <a href="/blog/nail-ombre-kieu-han/">nail ombre kiểu Hàn</a>.</li>
<li><strong>French viền mảnh</strong> giữ được nét sạch mà không chắn ngang. Viền dày mới là phần nên tránh. Xem <a href="/blog/nail-french-kieu-han/">nail French kiểu Hàn</a>.</li>
<li><strong>Một chi tiết nhỏ ở gốc móng</strong> như một viên đá nhỏ hoặc chỉ nhũ mảnh đặt dọc, giúp hướng mắt theo chiều dài.</li>
<li><strong>Nên cân nhắc:</strong> khối màu đậm chắn ngang đầu móng, hoa văn to kín mặt móng, và móng rất ngắn sơn màu tối đặc.</li>
</ul>

<!--anh:2-->
<h2>Một bộ gợi ý</h2>

<p>Form oval, dài hơn đầu ngón khoảng 3 mm, sơn gel nude ngả hồng sát hai cạnh, chừa viền gốc mảnh, thêm một chỉ nhũ dọc ở ngón áp út. Tại VESSCA, bộ này gồm cắt da chỉnh form tay 60.000₫ và sơn gel trơn 130.000₫, phần chỉ nhũ tính thêm từ 10.000₫.</p>

<p>Nếu bạn để móng ngắn, các gợi ý riêng cho độ dài ngắn nằm trong bài <a href="/blog/nail-mong-ngan-kieu-han/">nail móng ngắn kiểu Hàn</a>. Hai bài khác nhau: bài đó bàn về móng ngắn, bài này bàn về ngón ngắn.</p>'''
faq=[('Ngón tay ngắn nên làm form móng nào?','Oval hoặc almond nhẹ, vì đầu móng thu lại tạo cảm giác thuôn. Form vuông cạnh sắc làm móng trông bè ngang.'),
 ('Ngón tay ngắn nên sơn màu gì?','Tông sáng trung tính như nude ngả hồng, be sữa, trắng ngà, vì màu liền mạch với màu da làm móng trông dài hơn.'),
 ('Vì sao nên sơn sát hai cạnh móng?','Chừa trống hai bên làm móng trông hẹp và ngắn. Sơn sát cạnh và chỉ chừa viền mảnh ở gốc sẽ dùng hết diện tích móng.'),
 ('Ngón tay ngắn làm French được không?','Được, với điều kiện viền mảnh. Viền dày tạo đường ngang chắn đầu móng và làm ngón trông ngắn hơn.')]
en='''<p>Short fingers do not limit your options, but one rule helps: <strong>keep every line vertical, and leave as little bare skin as possible at the sides of the nail</strong>.</p>
<h2>Why vertical lines lengthen</h2>
<p>The eye reads length along any line it can follow. Vertical lines and a gradient running from base to tip pull the eye down the finger. Horizontal lines, a thick French edge or a dark block across the tip cut the finger into segments. Leaving a gap at the sides also makes the nail look narrow and short.</p>
<!--anh:1-->
<h2>Shape and length</h2>
<table>
<thead><tr><th></th><th>Do</th><th>Reconsider</th></tr></thead>
<tbody>
<tr><td>Shape</td><td>Oval, soft almond</td><td>Sharp square</td></tr>
<tr><td>Length</td><td>2–4 mm past the fingertip</td><td>Out of proportion</td></tr>
<tr><td>Sides</td><td>File straight</td><td>Narrowing the nail body</td></tr>
<tr><td>Base</td><td>Thin margin, paint close to the edges</td><td>Wide bare gap</td></tr>
</tbody>
</table>
<h2>Colour and art</h2>
<p>Light neutrals — pink nude, milky beige, ivory — blend nail and finger. A vertical gradient suits short fingers best. A thin French line keeps it clean; a thick one does not. Avoid dark blocks across the tip and large patterns covering the nail.</p>
<!--anh:2-->
<h2>A suggested set</h2>
<p>Oval, about 3 mm past the tip, pink nude gel painted close to the sides with a thin base margin, plus one vertical shimmer line on the ring finger. At VESSCA: hand cuticle work and shaping 60,000₫, plain gel 130,000₫, line work from 10,000₫.</p>'''
ko='''<p>손가락이 짧아도 선택이 제한되지는 않습니다. 다만 <strong>모든 선을 세로로 두고, 손톱 양옆에 드러나는 피부를 최소로</strong> 하면 길어 보입니다.</p>
<h2>세로선이 길어 보이는 이유</h2>
<p>눈은 따라갈 수 있는 선을 따라 길이를 읽습니다. 세로선과 큐티클에서 끝으로 가는 그라데이션은 시선을 손가락 길이 방향으로 이끕니다. 가로선, 두꺼운 프렌치, 끝을 가로지르는 진한 색은 손가락을 토막처럼 나눕니다. 양옆에 여백을 남기면 손톱이 좁고 짧아 보입니다.</p>
<!--anh:1-->
<h2>모양과 길이</h2>
<table>
<thead><tr><th></th><th>권장</th><th>재고</th></tr></thead>
<tbody>
<tr><td>모양</td><td>오벌, 부드러운 아몬드</td><td>각진 스퀘어</td></tr>
<tr><td>길이</td><td>손끝에서 2–4 mm</td><td>비율에 맞지 않는 길이</td></tr>
<tr><td>양옆</td><td>일자로 파일</td><td>손톱 몸통을 좁히기</td></tr>
<tr><td>큐티클 쪽</td><td>여백 얇게, 가장자리까지</td><td>넓은 여백</td></tr>
</tbody>
</table>
<h2>컬러와 아트</h2>
<p>핑크 누드, 밀키 베이지, 아이보리 같은 밝은 뉴트럴은 손톱과 손가락을 이어 보이게 합니다. 세로 그라데이션이 가장 잘 맞고, 프렌치는 얇게만. 끝을 가로지르는 진한 블록과 손톱을 덮는 큰 패턴은 피하세요.</p>
<!--anh:2-->
<h2>추천 조합</h2>
<p>오벌, 손끝에서 약 3 mm, 핑크 누드 젤을 가장자리까지, 큐티클 여백은 얇게, 약지에 세로 펄 라인 하나. VESSCA: 손 큐티클·모양 정리 60,000₫, 단색 젤 130,000₫, 라인 10,000₫부터.</p>'''
zh='''<p>手指短并不会限制款式,但有一条原则能让手显长:<strong>所有线条走竖向,指甲两侧裸露的皮肤尽量少</strong>。</p>
<h2>为什么竖线显长</h2>
<p>眼睛沿着能跟随的线条判断长度。竖线和从甲根到甲尖的渐变会把视线引向手指的长度方向。横线、过厚的法式边或横在甲尖的深色块会把手指切成几段。两侧留空也会让指甲显得窄而短。</p>
<!--anh:1-->
<h2>甲型与长度</h2>
<table>
<thead><tr><th></th><th>建议</th><th>斟酌</th></tr></thead>
<tbody>
<tr><td>甲型</td><td>椭圆、柔和尖圆</td><td>硬朗方形</td></tr>
<tr><td>长度</td><td>超出指尖 2–4 mm</td><td>超出比例</td></tr>
<tr><td>两侧</td><td>平直打磨</td><td>收窄甲身</td></tr>
<tr><td>甲根</td><td>留白细,涂到边缘</td><td>大面积留白</td></tr>
</tbody>
</table>
<h2>颜色与彩绘</h2>
<p>浅中性色如粉裸、奶米、象牙白让指甲与手指连成一片。竖向渐变最适合短手指。法式要细边;粗边反而不行。避免横在甲尖的深色块和铺满甲面的大图案。</p>
<!--anh:2-->
<h2>一个推荐组合</h2>
<p>椭圆形,超出指尖约 3 mm,粉裸甲油胶涂到两侧边缘、甲根留白细,无名指加一道竖向亮粉细线。VESSCA:手部死皮与修形 60,000₫,纯色胶 130,000₫,线条 10,000₫ 起。</p>'''
bai('nail-cho-ngon-tay-ngan','2026-11-20T08:30:00+07:00','Xu hướng & Cảm hứng',
 A(('oval nude nails manicure','Móng oval sơn nude trên ngón tay ngắn','Oval nude nails on short fingers','짧은 손가락의 오벌 누드 네일','短手指上的椭圆裸色美甲'),
   [('vertical ombre nails manicure','Ombre dọc từ gốc ra đầu móng','Vertical gradient from base to tip','큐티클에서 끝으로 가는 세로 그라데이션','从甲根到甲尖的竖向渐变'),
    ('thin french nails manicure','French viền mảnh không chắn ngang','Thin French line that does not cut across','가로지르지 않는 얇은 프렌치 라인','不横断甲面的细法式边')]),
 ('Nail cho ngón tay ngắn: form, độ dài và màu nào tôn tay','Nguyên tắc đường dọc và sơn sát cạnh giúp ngón trông dài hơn: chọn form oval hay almond, dài 2–4 mm, tông nude sáng, ombre dọc và French viền mảnh.',
  'Nail cho ngón tay ngắn: form và màu tôn tay | VESSCA',
  'Ngón tay ngắn nên chọn form oval hoặc almond, dài 2–4 mm, nude sáng, ombre dọc, French viền mảnh. Cắt da 60.000₫, gel trơn 130.000₫. VESSCA Bình Thạnh.',
  ['nail cho ngón tay ngắn','ngón tay ngắn nên làm nail gì','form móng cho ngón ngắn','nail tôn ngón tay','móng oval ngón ngắn'],vi,faq),
 ('Nails for Short Fingers: Shape, Length and Colour','The vertical-line rule and painting close to the sides, with shape, length and colour choices that lengthen the hand.',
  'Nails for Short Fingers | VESSCA Saigon','Oval or soft almond, 2–4 mm past the tip, light nudes, vertical gradients and thin French lines lengthen short fingers. Gel 130,000₫. VESSCA, Binh Thanh.',
  ['nails for short fingers','nail shape short fingers','nail salon Binh Thanh','Korean nails Saigon','gel manicure Ho Chi Minh City'],en,
  [('Which shape suits short fingers?','Oval or a soft almond, because the tapered tip reads as longer. Sharp squares look wider.'),('Which colours work?','Light neutrals such as pink nude, milky beige and ivory that blend with skin.'),('Can I wear French?','Yes with a thin line. A thick French edge cuts across the tip and shortens the finger.')]),
 ('짧은 손가락을 위한 네일: 모양, 길이, 컬러','세로선 원칙과 가장자리까지 바르는 법, 길어 보이게 하는 모양·길이·컬러 선택.',
  '짧은 손가락 네일 가이드 | 호치민 VESSCA','오벌이나 부드러운 아몬드, 손끝 2–4 mm, 밝은 누드, 세로 그라데이션, 얇은 프렌치가 길어 보입니다. 젤 130,000₫. 호치민 빈탄 VESSCA.',
  ['짧은 손가락 네일','네일 모양 추천','호치민 네일샵','빈탄 네일','한국 젤네일 호치민'],ko,
  [('어떤 모양이 어울리나요?','오벌이나 부드러운 아몬드가 길어 보입니다. 각진 스퀘어는 넓어 보입니다.'),('어떤 색이 좋나요?','핑크 누드, 밀키 베이지, 아이보리 같은 밝은 뉴트럴입니다.'),('프렌치도 되나요?','얇게 하면 좋습니다. 두꺼운 프렌치는 끝을 가로질러 짧아 보입니다.')]),
 ('短手指适合的美甲:甲型、长度与颜色','竖线原则与涂到两侧边缘的做法,以及让手显长的甲型、长度和颜色。',
  '短手指美甲指南 | 胡志明 VESSCA','短手指适合椭圆或柔和尖圆、超出指尖 2–4 mm、浅裸色、竖向渐变与细法式。纯色胶 130,000₫。胡志明平盛郡 VESSCA。',
  ['短手指 美甲','美甲 甲型','胡志明 美甲','平盛郡 美甲店','韩式美甲 胡志明'],zh,
  [('短手指适合什么甲型?','椭圆或柔和尖圆显长,硬朗方形会显宽。'),('适合什么颜色?','粉裸、奶米、象牙白等与皮肤相融的浅中性色。'),('可以做法式吗?','可以,但要细边。粗边横断甲尖会显短。')]))
