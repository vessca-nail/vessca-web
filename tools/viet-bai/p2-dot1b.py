# -*- coding: utf-8 -*-
"""Giai đoạn 2 — đợt 1 (tiếp): 13/11, 16/11, 18/11."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *

# ---------- 13/11 — Móng chân mọc quặp ----------
vi='''<p>Móng chân mọc quặp là khi cạnh móng ăn vào phần thịt hai bên ngón, gây đau khi đi lại hoặc khi mang giày. Nguyên nhân phổ biến nhất không phải do móng, mà do <strong>cách cắt móng</strong>. Bài này giải thích vì sao, cách phòng, và mốc nào thì nên đi khám thay vì ra tiệm nail.</p>

<p><em>Bài viết chỉ mang tính tham khảo, không thay thế chẩn đoán của bác sĩ. Nếu ngón đang sưng đau hoặc có mủ, bạn nên đến cơ sở y tế.</em></p>

<h2>Vì sao móng mọc quặp</h2>

<ul>
<li><strong>Cắt móng cong theo đầu ngón.</strong> Đây là nguyên nhân hàng đầu. Khi bạn cắt vòng cung, hai góc móng bị cắt ngắn hơn phần giữa. Móng mọc dài ra sẽ không có đường trượt thẳng, mà đâm chéo vào rãnh da bên cạnh.</li>
<li><strong>Cắt quá sát khoé.</strong> Lấy sâu vào khoé làm mất điểm tựa của cạnh móng.</li>
<li><strong>Giày bó mũi.</strong> Áp lực dồn vào hai bên ngón, đẩy thịt trùm lên cạnh móng.</li>
<li><strong>Chấn thương</strong> như va đập đầu ngón, hoặc đứng lâu, chạy nhiều với giày chật.</li>
<li><strong>Móng dày, móng cuộn</strong> theo cơ địa, thường rõ hơn ở ngón cái.</li>
</ul>

<!--anh:1-->
<h2>Cắt đúng: thẳng ngang, không vòng cung</h2>

<table>
<thead><tr><th></th><th>Nên</th><th>Không nên</th></tr></thead>
<tbody>
<tr><td>Đường cắt</td><td>Thẳng ngang, song song đầu ngón</td><td>Vòng cung theo đầu ngón</td></tr>
<tr><td>Độ dài</td><td>Bằng hoặc hơi dài hơn đầu ngón</td><td>Cắt lọt vào trong đầu ngón</td></tr>
<tr><td>Hai góc</td><td>Giữ nguyên, chỉ dũa nhẹ cho bớt sắc</td><td>Bấm sâu vào khoé</td></tr>
<tr><td>Dụng cụ</td><td>Kìm cắt móng chân lưỡi thẳng</td><td>Kìm móng tay lưỡi cong</td></tr>
<tr><td>Thời điểm</td><td>Sau khi tắm, móng mềm</td><td>Khi móng khô cứng, dễ nứt</td></tr>
</tbody>
</table>

<p>Nguyên tắc cắt móng nói chung được trình bày kỹ hơn trong bài <a href="/blog/cat-mong-tay-dung-cach/">cắt móng tay đúng cách</a>. Riêng móng chân, điểm khác quan trọng nhất là đường cắt phải thẳng.</p>

<h2>Khi nào ra tiệm được, khi nào phải đi khám</h2>

<p>Ra tiệm nail phù hợp khi móng <strong>chưa có dấu hiệu viêm</strong>: chỉ hơi cấn, da quanh móng bình thường, không đau nhiều. Kỹ thuật viên có thể chỉnh lại đường cắt cho thẳng, dũa gọn góc, làm mềm và đẩy nhẹ viền da để cạnh móng có đường trượt ra ngoài.</p>

<p>Bạn nên đến bác sĩ, không ra tiệm, khi có bất kỳ dấu hiệu sau:</p>

<ul>
<li>Sưng đỏ lan rộng, đau tăng, nóng vùng quanh móng</li>
<li>Có mủ, chảy dịch, hoặc mùi</li>
<li>Mọc thịt đỏ trùm lên cạnh móng</li>
<li>Tái đi tái lại nhiều lần ở cùng một ngón</li>
<li>Bạn có bệnh tiểu đường, tuần hoàn máu kém hoặc giảm cảm giác ở bàn chân — nhóm này nên để bác sĩ xử lý mọi vấn đề ở móng chân</li>
</ul>

<!--anh:2-->
<h2>VESSCA làm gì và không làm gì</h2>

<p>Tiệm nhận cắt da, chỉnh form, dưỡng viền móng chân với giá 70.000₫, dụng cụ kim loại được tiệt trùng bằng máy sau mỗi khách. Trong buổi làm, bạn có thể nói rõ ngón nào hay bị cấn để kỹ thuật viên cắt thẳng và chừa góc.</p>

<p>Tiệm <strong>không xử lý móng đang nhiễm trùng</strong> và không cắt sâu vào khoé để lấy phần móng ăn vào thịt. Việc đó thuộc về bác sĩ. Nếu bạn tới tiệm với ngón đang sưng mủ, kỹ thuật viên sẽ đề nghị bạn đi khám trước.</p>

<p>Nếu móng chân đổi màu, dày lên hoặc bong từng lớp, dấu hiệu cần phân biệt nằm trong bài <a href="/blog/nam-mong-dau-hieu/">nấm móng: dấu hiệu nhận biết</a>. Quy trình làm móng chân tại tiệm có trong bài <a href="/blog/lam-mong-chan-kieu-han/">làm móng chân kiểu Hàn</a>.</p>'''
faq=[('Móng chân mọc quặp do đâu?','Phổ biến nhất là do cắt móng vòng cung theo đầu ngón và cắt quá sát khoé, khiến cạnh móng đâm chéo vào da. Giày bó mũi và chấn thương cũng góp phần.'),
 ('Cắt móng chân thế nào cho đúng?','Cắt thẳng ngang, để dài bằng hoặc hơi hơn đầu ngón, giữ nguyên hai góc và chỉ dũa nhẹ. Cắt sau khi tắm lúc móng còn mềm.'),
 ('Móng mọc quặp có nên ra tiệm nail không?','Được, nếu chưa viêm: kỹ thuật viên chỉnh lại đường cắt và dũa gọn góc. Nếu đã sưng đỏ, có mủ hoặc đau nhiều thì cần đi khám.'),
 ('Khi nào móng chân mọc quặp phải gặp bác sĩ?','Khi sưng đỏ lan rộng, có mủ hoặc dịch, mọc thịt đỏ quanh móng, tái lại nhiều lần, hoặc khi bạn có tiểu đường và tuần hoàn kém.')]
en='''<p>An ingrown toenail is when the edge of the nail grows into the skin beside it. The most common cause is not the nail but <strong>how it was cut</strong>.</p>
<p><em>This article is general information, not a medical diagnosis. See a doctor if the toe is swollen or has pus.</em></p>
<h2>Why it happens</h2>
<p>Cutting the nail in a curve follows the fingertip shape and leaves the corners shorter than the centre, so the growing edge angles into the skin. Cutting deep into the corners, tight shoes and injury add to it.</p>
<!--anh:1-->
<h2>Cut straight across</h2>
<table>
<thead><tr><th></th><th>Do</th><th>Avoid</th></tr></thead>
<tbody>
<tr><td>Cut line</td><td>Straight across</td><td>Curved to the toe shape</td></tr>
<tr><td>Length</td><td>Level with the toe tip</td><td>Shorter than the tip</td></tr>
<tr><td>Corners</td><td>Keep, file lightly</td><td>Dig into the corners</td></tr>
<tr><td>Tool</td><td>Straight-blade toenail nipper</td><td>Curved fingernail clipper</td></tr>
</tbody>
</table>
<h2>Salon or doctor</h2>
<p>A salon is fine while there is no inflammation: the technician can straighten the cut line and file the corners. See a doctor if there is spreading redness, pus or discharge, overgrown tissue, repeated episodes, or if you have diabetes or poor circulation.</p>
<!--anh:2-->
<h2>What VESSCA does</h2>
<p>Cuticle work and shaping for toes is 70,000₫, with metal tools machine-sterilised after every client. VESSCA does not treat infected nails and does not cut into the corners to remove an embedded edge — that is a doctor's work.</p>'''
ko='''<p>발톱 내향증은 발톱 모서리가 옆 살을 파고드는 상태입니다. 가장 흔한 원인은 발톱 자체가 아니라 <strong>깎는 방식</strong>입니다.</p>
<p><em>본 글은 일반 정보이며 진단을 대체하지 않습니다. 붓거나 고름이 있으면 병원에 가세요.</em></p>
<h2>원인</h2>
<p>발톱을 둥글게 깎으면 모서리가 가운데보다 짧아져, 자라는 모서리가 살 쪽으로 비스듬히 파고듭니다. 모서리를 깊게 자르는 습관, 앞이 좁은 신발, 외상도 영향을 줍니다.</p>
<!--anh:1-->
<h2>일자로 깎기</h2>
<table>
<thead><tr><th></th><th>권장</th><th>피하기</th></tr></thead>
<tbody>
<tr><td>절단선</td><td>일자로</td><td>발가락 모양대로 둥글게</td></tr>
<tr><td>길이</td><td>발가락 끝과 같은 높이</td><td>끝보다 짧게</td></tr>
<tr><td>모서리</td><td>남기고 살짝만 파일</td><td>깊게 파기</td></tr>
<tr><td>도구</td><td>일자 발톱 니퍼</td><td>곡선 손톱깎이</td></tr>
</tbody>
</table>
<h2>샵과 병원</h2>
<p>염증이 없다면 샵에서 절단선을 바로잡고 모서리를 다듬을 수 있습니다. 붉게 번지거나 고름, 살이 덮이는 경우, 반복되는 경우, 당뇨나 혈액순환 문제가 있으면 병원으로 가세요.</p>
<!--anh:2-->
<h2>VESSCA의 범위</h2>
<p>발 큐티클 정리와 모양 정리는 70,000₫이며, 금속 도구는 고객마다 기계로 멸균합니다. 감염된 발톱은 다루지 않으며, 파고든 모서리를 잘라내는 시술도 하지 않습니다.</p>'''
zh='''<p>甲嵌入是指趾甲边缘长进旁边的皮肤。最常见的原因不是趾甲本身,而是<strong>修剪方式</strong>。</p>
<p><em>本文仅供参考,不替代医生诊断。如果脚趾红肿或有脓,请就医。</em></p>
<h2>为什么会这样</h2>
<p>把趾甲剪成弧形会让两角比中间更短,长出来的边缘便斜着扎进皮肤。剪得太深入甲角、鞋头过窄和外伤也会加重。</p>
<!--anh:1-->
<h2>要剪成平直</h2>
<table>
<thead><tr><th></th><th>建议</th><th>避免</th></tr></thead>
<tbody>
<tr><td>剪线</td><td>平直横剪</td><td>顺着脚趾剪成弧形</td></tr>
<tr><td>长度</td><td>与趾尖齐平</td><td>短于趾尖</td></tr>
<tr><td>两角</td><td>保留,轻轻打磨</td><td>深挖甲角</td></tr>
<tr><td>工具</td><td>平口趾甲钳</td><td>弯口指甲剪</td></tr>
</tbody>
</table>
<h2>去店里还是看医生</h2>
<p>没有发炎时可以到店里修正剪线、打磨甲角。如果红肿扩散、有脓或渗液、长出红肉、反复发作,或您有糖尿病和血液循环问题,请就医。</p>
<!--anh:2-->
<h2>VESSCA 的范围</h2>
<p>修脚部死皮与修形 70,000₫,金属工具每位顾客后用机器灭菌。本店不处理已感染的趾甲,也不会深挖甲角取出嵌入部分,那属于医生的工作。</p>'''
bai('mong-chan-moc-quap','2026-11-13T08:30:00+07:00','Hỏi & Đáp',
 A(('pedicure toenails feet care','Bàn chân được chăm sóc móng đúng cách','Feet after a careful pedicure','올바르게 관리한 발과 발톱','经过正确护理的双脚'),
   [('pedicure toenail clipper','Kìm cắt móng chân lưỡi thẳng','Straight-blade toenail nipper','일자 발톱 니퍼','平口趾甲钳'),
    ('pedicure feet care salon','Kỹ thuật viên chỉnh form móng chân','Technician shaping toenails','발톱 모양을 정리하는 모습','美甲师修整趾甲形状')]),
 ('Móng chân mọc quặp: vì sao, cách phòng và khi nào cần khám','Móng chân mọc quặp phần lớn do cắt vòng cung và cắt sát khoé. Cách cắt thẳng đúng chuẩn, khi nào ra tiệm được và khi nào phải gặp bác sĩ.',
  'Móng chân mọc quặp: nguyên nhân và cách phòng | VESSCA',
  'Móng chân mọc quặp chủ yếu do cắt vòng cung và cắt sát khoé. Cách cắt thẳng đúng, dấu hiệu phải đi khám. Chỉnh form móng chân 70.000₫. VESSCA Bình Thạnh.',
  ['móng chân mọc quặp','móng chân đâm vào thịt','cắt móng chân đúng cách','móng chân bị quặp','móng chọc thịt'],vi,faq),
 ('Ingrown Toenails: Causes, Prevention and When to See a Doctor','Why ingrown toenails happen, how to cut toenails correctly, and the signs that need a doctor rather than a salon.',
  'Ingrown Toenails: Causes and Prevention | VESSCA','Ingrown toenails mostly come from curved cutting and digging into corners. How to cut straight, and when to see a doctor. Toe shaping 70,000₫. VESSCA, Binh Thanh.',
  ['ingrown toenail','pedicure Binh Thanh','nail salon Binh Thanh','toenail cutting','pedicure Ho Chi Minh City'],en,
  [('What causes an ingrown toenail?','Most often cutting the nail in a curve and digging into the corners, plus tight shoes and injury.'),('How should I cut toenails?','Straight across, level with the toe tip, keeping the corners and filing them lightly.'),('Can a salon help?','Yes while there is no inflammation. With redness, pus or repeated episodes, see a doctor.')]),
 ('발톱 내향증: 원인, 예방, 병원에 갈 시점','발톱이 파고드는 이유, 올바른 절단법, 샵이 아니라 병원에 가야 하는 신호.',
  '발톱 내향증 원인과 예방 | 호치민 VESSCA','발톱 내향증은 둥글게 깎기와 모서리 깊게 자르기가 주원인입니다. 일자 절단법과 병원에 갈 신호. 발 모양 정리 70,000₫. 호치민 빈탄 VESSCA.',
  ['발톱 내향증','발톱 깎는 법','호치민 페디큐어','호치민 네일샵','빈탄 네일'],ko,
  [('원인이 무엇인가요?','둥글게 깎기와 모서리를 깊게 자르는 습관이 가장 흔하며, 좁은 신발과 외상도 영향을 줍니다.'),('어떻게 깎아야 하나요?','일자로, 발가락 끝과 같은 높이로, 모서리는 남기고 살짝만 다듬습니다.'),('샵에서 해결되나요?','염증이 없으면 가능합니다. 고름이나 반복되는 경우 병원에 가세요.')]),
 ('甲嵌入:原因、预防与何时就医','趾甲为什么会长进肉里、正确的修剪方法,以及需要看医生而不是去美甲店的信号。',
  '趾甲嵌入的原因与预防 | 胡志明 VESSCA','趾甲嵌入多因剪成弧形和深挖甲角。正确的平直剪法与就医信号。修脚修形 70,000₫。胡志明平盛郡 VESSCA。',
  ['趾甲 嵌入','趾甲 修剪','胡志明 修脚','胡志明 美甲','平盛郡 美甲店'],zh,
  [('为什么会甲嵌入?','最常见是把趾甲剪成弧形和深挖甲角,鞋头过窄与外伤也有影响。'),('趾甲该怎么剪?','平直横剪,与趾尖齐平,保留两角只轻轻打磨。'),('美甲店能处理吗?','没有发炎时可以。若红肿有脓或反复发作,请就医。')]))

# ---------- 16/11 — Nail vân đá ----------
vi='''<p>Nail vân đá là kiểu vẽ mô phỏng đường vân của đá cẩm thạch trên nền sơn gel. Điểm mạnh của kiểu này là trông tinh tế trên móng ngắn và không kén môi trường làm việc. Bài này nói rõ kiểu vân đá được làm thế nào, có mấy biến thể, giá cộng thêm bao nhiêu và giữ được bao lâu.</p>

<h2>Vân đá được làm thế nào</h2>

<p>Kỹ thuật viên sơn nền trước, thường là trắng sữa, be hoặc xám nhạt, rồi hơ đèn cho cứng. Trên nền đó, một lớp gel trong được phủ mỏng, và khi gel còn ướt, kỹ thuật viên dùng cọ mảnh hoặc đầu kim kéo những đường mảnh không đều để tạo vân. Vân được kéo nhoè nhẹ cho mềm cạnh, rồi hơ đèn và phủ top coat.</p>

<p>Vân đá thật không có đường nào song song và không có đường nào khép kín thành hình. Đó là lý do kiểu này phụ thuộc tay nghề: vẽ đều tay quá thì ra hình mạng nhện, vẽ quá nhiều thì rối mắt.</p>

<!--anh:1-->
<h2>Bốn biến thể thường làm</h2>

<table>
<thead><tr><th>Biến thể</th><th>Nền</th><th>Vân</th><th>Phù hợp</th></tr></thead>
<tbody>
<tr><td>Cẩm thạch trắng</td><td>Trắng sữa</td><td>Xám tro mảnh</td><td>Đi làm, nhẹ nhàng, móng ngắn</td></tr>
<tr><td>Xám khói</td><td>Xám nhạt</td><td>Trắng và xám đậm</td><td>Tông trung tính, ít bám bẩn mắt</td></tr>
<tr><td>Travertine nâu</td><td>Be, nâu sữa</td><td>Nâu đậm, ngả cam</td><td>Da ngăm, tông ấm, mùa thu đông</td></tr>
<tr><td>Vân đá viền nhũ vàng</td><td>Trắng hoặc be</td><td>Vân xám kèm chỉ nhũ</td><td>Dịp cần nổi hơn, tiệc</td></tr>
</tbody>
</table>

<p>Bạn không cần làm vân cả mười ngón. Cách phổ biến và dễ giữ nhất là hai ngón vân đá làm điểm nhấn, tám ngón còn lại sơn trơn cùng tông nền.</p>

<h2>Giá và thời gian</h2>

<p>Vân đá là phần vẽ cộng thêm trên nền sơn gel. Tại VESSCA, nền gel trơn 130.000₫, phần vân đá tính từ 15.000₫. Một bộ hai ngón nhấn vân đá tính ra khoảng 160.000₫, trong khi làm vân cả mười ngón sẽ cao hơn tuỳ độ chi tiết. Nếu muốn nền xà cừ ánh trai thay cho nền trơn, nền đó là 280.000₫.</p>

<p>Vân đá vẽ tay nên cần thêm thời gian so với sơn trơn. Bạn nên tính dư thời gian cho buổi hẹn, nhất là khi làm nhiều ngón.</p>

<!--anh:2-->
<h2>Giữ được bao lâu</h2>

<p>Vì vân nằm giữa hai lớp gel và được top coat phủ lên, vân không bị mờ hay trôi. Độ bền của bộ nail vân đá bằng với bộ gel thường, khoảng hai đến ba tuần, và phụ thuộc vào móng mọc dài ra chứ không phụ thuộc phần vẽ. Cách kéo dài thời gian giữ nằm trong bài <a href="/blog/cach-giu-nail-lau-bong/">cách giữ nail lâu bong</a>.</p>

<p>Nếu bạn thích nhóm hiệu ứng bề mặt, hai kiểu gần với vân đá là <a href="/blog/nail-trang-guong/">nail tráng gương</a> cho mặt móng phản chiếu, và <a href="/blog/nail-french-kieu-han/">nail French kiểu Hàn</a> cho viền mảnh tối giản. Với móng ngắn, gợi ý về form và tỉ lệ có trong bài <a href="/blog/nail-mong-ngan-kieu-han/">nail móng ngắn kiểu Hàn</a>.</p>'''
faq=[('Nail vân đá làm thế nào?','Sơn nền và hơ đèn, phủ một lớp gel trong, rồi kéo đường vân bằng cọ mảnh hoặc đầu kim khi gel còn ướt, cuối cùng hơ đèn và phủ top coat.'),
 ('Nail vân đá giá bao nhiêu?','Phần vân tính thêm từ 15.000₫ trên nền sơn gel 130.000₫. Bộ hai ngón nhấn vân đá khoảng 160.000₫.'),
 ('Vân đá có bị mờ hay trôi không?','Không. Vân nằm giữa hai lớp gel và được top coat phủ lên, nên giữ nguyên suốt thời gian đeo bộ nail.'),
 ('Móng ngắn làm vân đá được không?','Được, và đây là một trong những kiểu hợp móng ngắn nhất. Nên làm vân ở hai ngón nhấn, các ngón còn lại sơn trơn cùng tông.')]
en='''<p>Marble nails imitate the veining of stone over a gel base. The look reads as subtle on short nails and suits most workplaces.</p>
<h2>How it is done</h2>
<p>The base colour is cured first, then a thin layer of clear gel goes on. While that layer is still wet, the technician drags uneven fine lines with a thin brush or needle, softens the edges, cures, and seals with top coat. Real stone veining has no parallel and no closed lines, which is why the look depends on the technician's hand.</p>
<!--anh:1-->
<h2>Four versions</h2>
<table>
<thead><tr><th>Version</th><th>Base</th><th>Veining</th><th>Suits</th></tr></thead>
<tbody>
<tr><td>White marble</td><td>Milky white</td><td>Fine ash grey</td><td>Office, short nails</td></tr>
<tr><td>Smoke grey</td><td>Pale grey</td><td>White and dark grey</td><td>Neutral tones</td></tr>
<tr><td>Brown travertine</td><td>Beige</td><td>Warm dark brown</td><td>Deeper skin, autumn</td></tr>
<tr><td>Marble with gold line</td><td>White or beige</td><td>Grey veins plus gold</td><td>Events</td></tr>
</tbody>
</table>
<h2>Price and time</h2>
<p>Marble is an add-on over gel. Plain gel is 130,000₫ and the veining starts at 15,000₫, so two accent nails come to about 160,000₫. A pearl base instead of plain is 280,000₫. Hand-painted veining takes longer than plain colour, so allow extra time.</p>
<!--anh:2-->
<h2>How long it lasts</h2>
<p>The veining sits between two gel layers under top coat, so it does not smudge or fade. Wear time matches a normal gel set, about two to three weeks, limited by nail growth rather than by the art.</p>'''
ko='''<p>마블 네일은 젤 베이스 위에 돌의 결을 흉내 낸 아트입니다. 짧은 손톱에서도 과하지 않고 직장에서도 무리가 없습니다.</p>
<h2>시술 방법</h2>
<p>베이스 컬러를 경화한 뒤 투명 젤을 얇게 올리고, 젤이 마르기 전에 얇은 브러시나 니들로 불규칙한 선을 그립니다. 경계를 부드럽게 풀고 경화한 다음 탑젤로 마감합니다. 실제 돌의 결은 평행선도 닫힌 선도 없기 때문에 손기술에 좌우됩니다.</p>
<!--anh:1-->
<h2>네 가지 버전</h2>
<table>
<thead><tr><th>버전</th><th>베이스</th><th>결</th><th>추천</th></tr></thead>
<tbody>
<tr><td>화이트 마블</td><td>밀키 화이트</td><td>얇은 애쉬 그레이</td><td>직장, 짧은 손톱</td></tr>
<tr><td>스모크 그레이</td><td>연한 그레이</td><td>화이트와 진한 그레이</td><td>중성 톤</td></tr>
<tr><td>브라운 트래버틴</td><td>베이지</td><td>웜한 다크 브라운</td><td>어두운 톤, 가을</td></tr>
<tr><td>골드 라인 마블</td><td>화이트·베이지</td><td>그레이 결과 골드</td><td>행사</td></tr>
</tbody>
</table>
<h2>가격과 시간</h2>
<p>마블은 젤 위에 추가되는 아트입니다. 단색 젤 130,000₫, 마블은 15,000₫부터이므로 포인트 두 손가락은 약 160,000₫입니다. 자개 베이스는 280,000₫. 핸드페인팅이라 단색보다 시간이 더 걸립니다.</p>
<!--anh:2-->
<h2>지속 기간</h2>
<p>결이 젤 두 층 사이 탑젤 아래에 있어 번지거나 흐려지지 않습니다. 일반 젤과 같은 2–3주이며, 아트가 아니라 손톱이 자라는 속도가 기준입니다.</p>'''
zh='''<p>大理石美甲是在甲油胶底色上模仿石材纹理的彩绘。短指甲上看起来也很内敛,适合多数工作场合。</p>
<h2>怎么做</h2>
<p>先上底色并照灯,再薄薄盖一层透明胶。趁这层未干,用细笔或针拉出不规则的细线,把边缘晕开,照灯后封上封层。真实石材的纹理没有平行线也没有闭合线,所以这个款式很看手艺。</p>
<!--anh:1-->
<h2>四种版本</h2>
<table>
<thead><tr><th>版本</th><th>底色</th><th>纹理</th><th>适合</th></tr></thead>
<tbody>
<tr><td>白色大理石</td><td>奶白</td><td>细灰色</td><td>上班、短指甲</td></tr>
<tr><td>烟灰色</td><td>浅灰</td><td>白与深灰</td><td>中性色调</td></tr>
<tr><td>棕色洞石</td><td>米色</td><td>暖调深棕</td><td>深肤色、秋冬</td></tr>
<tr><td>金线大理石</td><td>白或米色</td><td>灰纹加金线</td><td>宴会场合</td></tr>
</tbody>
</table>
<h2>价格与时间</h2>
<p>大理石是在甲油胶上加的彩绘。纯色胶 130,000₫,纹理从 15,000₫ 起,两个重点指甲约 160,000₫。换成贝壳光底色为 280,000₫。手绘比纯色耗时更久,请预留时间。</p>
<!--anh:2-->
<h2>能保持多久</h2>
<p>纹理夹在两层胶之间、封层之下,不会蹭花或褪色。与普通甲油胶一样约 2–3 周,取决于指甲生长而不是彩绘本身。</p>'''
bai('nail-van-da-marble','2026-11-16T08:30:00+07:00','Xu hướng & Cảm hứng',
 A(('marble nails manicure','Bộ nail vân đá cẩm thạch trắng','White marble nails','화이트 마블 네일','白色大理石美甲'),
   [('white marble nails manicure','Vân đá trắng xám trên móng ngắn','White and grey marble on short nails','짧은 손톱의 화이트 그레이 마블','短指甲上的白灰大理石纹'),
    ('grey marble nails manicure','Vân đá xám khói tông trung tính','Smoke grey marble nails','스모크 그레이 마블 네일','烟灰色大理石美甲')]),
 ('Nail vân đá: cách làm, biến thể, giá và độ bền','Nail vân đá được vẽ thế nào, bốn biến thể thường làm, giá cộng thêm từ 15.000₫ và vì sao vân không bị mờ trong hai đến ba tuần.',
  'Nail vân đá: cách làm, biến thể và giá | VESSCA',
  'Nail vân đá vẽ giữa hai lớp gel nên không mờ, giữ 2–3 tuần. Bốn biến thể và giá: nền gel 130.000₫, vân từ 15.000₫. VESSCA Bình Thạnh.',
  ['nail vân đá','nail marble','nail cẩm thạch','mẫu nail vân đá','nail vân đá móng ngắn'],vi,faq),
 ('Marble Nails: Technique, Versions, Price and Wear','How marble veining is painted, four common versions, what it adds to the price and why it does not smudge.',
  'Marble Nails: Technique and Price | VESSCA Saigon','Marble veining is sealed between gel layers, so it lasts 2–3 weeks. Gel base 130,000₫ plus veining from 15,000₫. VESSCA, Binh Thanh.',
  ['marble nails','nail art Binh Thanh','Korean nails Saigon','gel manicure Ho Chi Minh City','nail salon Binh Thanh'],en,
  [('How is marble nail art done?','Lines are dragged with a thin brush or needle through wet clear gel over a cured base, then sealed with top coat.'),('What does it cost?','Gel base 130,000₫ plus veining from 15,000₫; two accent nails about 160,000₫.'),('Does it smudge?','No. It sits between gel layers under top coat and lasts as long as the set.')]),
 ('마블 네일: 기법, 버전, 가격, 지속력','마블 결을 그리는 방법, 자주 하는 네 가지 버전, 추가 비용과 번지지 않는 이유.',
  '마블 네일 기법과 가격 | 호치민 VESSCA','마블 결은 젤 층 사이에 봉해져 2–3주 유지됩니다. 젤 베이스 130,000₫에 결 15,000₫부터. 호치민 빈탄 VESSCA.',
  ['마블 네일','네일 아트','호치민 네일샵','빈탄 네일','한국 젤네일 호치민'],ko,
  [('어떻게 그리나요?','경화된 베이스 위 투명 젤이 마르기 전에 얇은 브러시나 니들로 선을 긋고 탑젤로 마감합니다.'),('가격은요?','젤 베이스 130,000₫에 결 15,000₫부터, 포인트 두 손가락 약 160,000₫.'),('번지지 않나요?','젤 층 사이 탑젤 아래에 있어 번지지 않고 세트 수명만큼 유지됩니다.')]),
 ('大理石美甲:做法、版本、价格与持久度','大理石纹怎么画、四种常见版本、加价多少,以及为什么不会蹭花。',
  '大理石美甲做法与价格 | 胡志明 VESSCA','大理石纹封在胶层之间,可保持 2–3 周。底胶 130,000₫,纹理 15,000₫ 起。胡志明平盛郡 VESSCA。',
  ['大理石 美甲','美甲彩绘','胡志明 美甲','平盛郡 美甲店','韩式美甲 胡志明'],zh,
  [('大理石纹怎么画?','在照干的底色上薄涂透明胶,趁未干用细笔或针拉线,再封层。'),('价格多少?','底胶 130,000₫ 加纹理 15,000₫ 起,两个重点指甲约 160,000₫。'),('会蹭花吗?','不会,纹理在胶层之间与封层之下,能保持整副的寿命。')]))
