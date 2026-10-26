# -*- coding: utf-8 -*-
"""Giai đoạn 2 — đợt 3: 23/11, 25/11, 27/11, 30/11, 2/12, 4/12."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *

# ---------- 23/11 — Thuật ngữ nail ----------
vi='''<p>Bài này giải thích những từ bạn hay gặp khi làm nail: base coat, top coat, cuticle, form, fill, phá gel, đèn UV và LED, builder gel. Mỗi từ có một câu định nghĩa và một dòng nói rõ bạn sẽ nghe nó vào lúc nào.</p>

<h2>Biết thuật ngữ giúp được gì</h2>

<p>Có hai lợi ích. Thứ nhất, bạn gọi đúng tên dịch vụ khi đặt lịch, nên yêu cầu không bị hiểu sai: "tháo gel rồi làm bộ mới" khác "fill gel", và hai việc này khác nhau cả về thời gian lẫn giá. Thứ hai, bạn hiểu kỹ thuật viên đang làm gì trên tay mình, nên thấy rõ vì sao một bộ gel giữ được hai đến ba tuần và vì sao bóc gel là việc nên tránh.</p>

<!--anh:1-->
<h2>Bảng thuật ngữ nail</h2>

<table>
<thead><tr><th>Thuật ngữ</th><th>Nghĩa</th><th>Gặp khi nào</th></tr></thead>
<tbody>
<tr><td>Base coat</td><td>Lớp lót trong suốt bôi đầu tiên, giúp màu bám chắc và ngăn màu ăn vào móng thật</td><td>Bước đầu của mọi bộ gel</td></tr>
<tr><td>Top coat</td><td>Lớp phủ trong suốt bôi sau cùng, khoá màu và tạo độ bóng</td><td>Bước cuối, cũng là lớp bị dũa khi tháo</td></tr>
<tr><td>Cuticle</td><td>Viền da mỏng ở gốc móng, có nhiệm vụ bịt kín khe giữa da và móng</td><td>Lúc cắt da, dưỡng viền</td></tr>
<tr><td>Form móng</td><td>Hình dáng đầu móng sau khi dũa: vuông, tròn, oval, almond</td><td>Lúc chỉnh form đầu buổi</td></tr>
<tr><td>Phá gel</td><td>Tháo lớp gel cũ: dũa lớp top rồi ủ dung dịch, khoảng 20 phút</td><td>Khi làm bộ mới</td></tr>
<tr><td>Fill gel</td><td>Giữ phần gel cũ còn chắc và đắp thêm vào phần móng đã mọc ra ở gốc</td><td>Sau hai đến ba tuần</td></tr>
<tr><td>Builder gel</td><td>Gel đặc tạo thêm độ dày và độ cứng, đắp được trên móng thật</td><td>Khi móng mỏng, dễ gãy</td></tr>
<tr><td>Úp móng</td><td>Dán móng giả làm sẵn lên móng thật rồi dũa chỉnh form</td><td>Khi muốn có độ dài ngay</td></tr>
<tr><td>Gel X</td><td>Móng úp bằng gel, dán bằng gel và hơ đèn nên mép liền với móng thật</td><td>Khi muốn dài mà vẫn mỏng nhẹ</td></tr>
<tr><td>Dual form</td><td>Khuôn trong suốt dùng tạo móng dài bằng gel ngay trên tay</td><td>Khi muốn dài và dày</td></tr>
<tr><td>Đèn LED, đèn UV</td><td>Thiết bị phát tia cực tím làm lớp gel cứng lại</td><td>Sau mỗi lớp gel</td></tr>
<tr><td>Hơ đèn</td><td>Bước đặt tay vào đèn để lớp gel vừa bôi cứng hoàn toàn</td><td>Sau từng lớp, vài chục giây</td></tr>
<tr><td>Sơn cứng móng</td><td>Sơn dưỡng làm móng thật cứng hơn, không cần đèn</td><td>Khi bạn đang nghỉ gel</td></tr>
<tr><td>Ombre</td><td>Kiểu chuyển màu dần, thường từ gốc móng ra đầu móng</td><td>Khi chọn mẫu</td></tr>
<tr><td>French</td><td>Kiểu sơn một đường viền ngang ở đầu móng bằng màu khác nền</td><td>Khi chọn mẫu</td></tr>
<tr><td>Mắt mèo</td><td>Hiệu ứng vệt sáng trên mặt móng, tạo bằng gel có hạt kim loại và thanh từ</td><td>Khi chọn hiệu ứng</td></tr>
</tbody>
</table>

<h2>Bốn cặp từ dễ nhầm</h2>

<p><strong>Phá gel và fill gel.</strong> Phá gel là tháo sạch lớp gel cũ để làm bộ mới, 30.000₫ và khoảng 20 phút. Fill gel là giữ phần gel cũ còn chắc rồi đắp thêm vào phần gốc đã mọc ra, 190.000₫ một bộ. Chi tiết trong bài <a href="/blog/fill-gel-dam-gel-la-gi/">fill gel và đắp gel là gì</a>.</p>

<p><strong>Base coat và sơn cứng móng.</strong> Base coat là lớp lót nằm dưới màu gel, không dùng riêng. Sơn cứng móng là sản phẩm độc lập, bôi lên móng trần khi bạn không sơn màu. Xem bài <a href="/blog/base-coat-top-coat-la-gi/">base coat và top coat là gì</a>.</p>

<p><strong>Úp móng và đắp gel.</strong> Úp móng dùng móng làm sẵn dán lên móng thật. Đắp gel dùng gel lỏng tạo hình trực tiếp, nên chỉnh được độ cong và độ dày theo từng ngón. Bài <a href="/blog/up-mong-va-dap-gel-khac-nhau/">úp móng và đắp gel khác nhau thế nào</a> so sánh độ bền và giá.</p>

<p><strong>Đèn UV và đèn LED.</strong> Cả hai đều phát tia cực tím để làm cứng gel, khác nhau ở bước sóng. Đèn LED hơ nhanh hơn.</p>

<!--anh:2-->
<h2>Dùng thuật ngữ khi đặt lịch</h2>

<p>Bạn không cần nói đúng từ chuyên môn để được làm đúng ý. Ba thông tin sau là đủ để tiệm chuẩn bị chính xác: trên tay bạn đang có gì (móng trần, gel, móng úp), bạn muốn tháo rồi làm mới hay chỉ fill, và bạn muốn sơn trơn hay có hiệu ứng.</p>

<p>Nếu không chắc tên hiệu ứng mình thích, mang theo một tấm ảnh. Kỹ thuật viên của VESSCA sẽ gọi tên giúp bạn và nói rõ phần nào làm được trên độ dài móng hiện tại.</p>'''
faq=[('Base coat và top coat khác nhau thế nào?','Base coat là lớp lót trong suốt bôi trước màu, giúp màu bám chắc và không ăn vào móng thật. Top coat là lớp phủ sau cùng, khoá màu và tạo độ bóng.'),
 ('Phá gel và fill gel khác nhau ra sao?','Phá gel là tháo sạch lớp gel cũ, 30.000₫, khoảng 20 phút. Fill gel giữ phần gel cũ còn chắc và đắp thêm vào phần móng mới mọc, 190.000₫ một bộ.'),
 ('Cuticle là gì?','Là viền da mỏng ở gốc móng, giữ vai trò bịt kín khe giữa da và móng. Cắt quá sâu sẽ mất lớp bảo vệ này.'),
 ('Builder gel dùng để làm gì?','Là loại gel đặc dùng tạo thêm độ dày và độ cứng cho móng, thường dùng khi móng thật mỏng hoặc dễ gãy.')]
en='''<p>This is a plain-language glossary of the words you meet in a nail salon: base coat, top coat, cuticle, shape, fill, gel removal, UV and LED lamps, builder gel. Read it through or jump to the table for the one word you need.</p>
<h2>Why the words help</h2>
<p>Two reasons. You can name the service you want when booking, so nothing is misunderstood — "remove and start a new set" is not the same job as "fill". And you understand what is happening on your hands, which makes it obvious why a gel set lasts two to three weeks and why peeling it off is a bad idea.</p>
<!--anh:1-->
<h2>Glossary</h2>
<table>
<thead><tr><th>Term</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td>Base coat</td><td>Clear first layer; helps colour grip and keeps pigment off the natural nail</td></tr>
<tr><td>Top coat</td><td>Clear final layer; seals the colour and gives the shine</td></tr>
<tr><td>Cuticle</td><td>The thin skin at the base of the nail that seals the gap between skin and nail</td></tr>
<tr><td>Shape</td><td>The filed outline: square, round, oval, almond</td></tr>
<tr><td>Gel removal</td><td>Filing the top layer, then soaking about 20 minutes</td></tr>
<tr><td>Fill</td><td>Keeping the sound gel and rebuilding only the regrown area at the base</td></tr>
<tr><td>Builder gel</td><td>Thicker gel that adds strength and thickness over the natural nail</td></tr>
<tr><td>Tips / Gel X</td><td>Pre-made extensions glued on; Gel X ones are gel and cured under the lamp</td></tr>
<tr><td>Dual form</td><td>A clear mould used to build length in gel directly on the hand</td></tr>
<tr><td>Curing</td><td>Hardening each gel layer under a UV or LED lamp</td></tr>
<tr><td>Tacky layer</td><td>The slightly sticky film left after curing, wiped off with alcohol</td></tr>
<tr><td>Nail strengthener</td><td>A treatment polish used on bare nails, no lamp needed</td></tr>
<tr><td>Ombre</td><td>A gradient, usually from base to tip</td></tr>
<tr><td>French</td><td>A line of a second colour across the tip</td></tr>
<tr><td>Cat-eye</td><td>A light streak made with magnetic gel and a magnet</td></tr>
</tbody>
</table>
<h2>Pairs people mix up</h2>
<p>Removal (30,000₫, about 20 minutes) clears the old gel for a new set; a fill (190,000₫ per set) keeps it. A base coat sits under colour; a strengthener is used alone on bare nails. Tips are glued on, while builder gel is shaped on the nail. UV and LED lamps both cure gel, LED faster.</p>
<!--anh:2-->
<h2>Booking in three sentences</h2>
<p>Tell us what is on your nails now, whether you want removal or a fill, and whether you want plain colour or an effect. Photos are welcome, and our technicians will name the effect for you.</p>'''
ko='''<p>네일샵에서 자주 듣는 용어를 쉬운 말로 정리했습니다. 베이스 코트, 탑 코트, 큐티클, 모양, 필, 젤 제거, UV·LED 램프, 빌더 젤까지 표로 찾아보실 수 있습니다.</p>
<h2>용어를 알면 좋은 이유</h2>
<p>두 가지입니다. 예약할 때 원하는 시술을 정확히 말할 수 있습니다. "제거하고 새로 하기"와 "필"은 다른 작업이고 시간과 가격도 다릅니다. 또 손에서 무슨 일이 일어나는지 알게 되어, 젤이 2–3주 유지되는 이유와 뜯어내면 안 되는 이유가 분명해집니다.</p>
<!--anh:1-->
<h2>용어 표</h2>
<table>
<thead><tr><th>용어</th><th>뜻</th></tr></thead>
<tbody>
<tr><td>베이스 코트</td><td>가장 먼저 바르는 투명 층. 컬러 밀착을 돕고 색소가 자연 손톱에 배는 것을 막습니다</td></tr>
<tr><td>탑 코트</td><td>마지막 투명 층. 컬러를 덮어 광택을 냅니다</td></tr>
<tr><td>큐티클</td><td>손톱 뿌리의 얇은 피부. 피부와 손톱 사이를 막아 주는 역할입니다</td></tr>
<tr><td>모양</td><td>파일로 다듬은 끝 형태: 스퀘어, 라운드, 오벌, 아몬드</td></tr>
<tr><td>젤 제거</td><td>탑층을 갈고 약 20분 불리는 과정</td></tr>
<tr><td>필</td><td>단단한 젤은 남기고 자라난 뿌리 쪽만 다시 채우는 시술</td></tr>
<tr><td>빌더 젤</td><td>자연 손톱 위에 두께와 강도를 더하는 된 젤</td></tr>
<tr><td>팁, 젤엑스</td><td>미리 만든 연장. 젤엑스는 젤 재질로 램프에 경화합니다</td></tr>
<tr><td>듀얼 폼</td><td>손 위에서 젤로 길이를 만드는 투명 몰드</td></tr>
<tr><td>경화</td><td>램프로 젤 층을 굳히는 단계</td></tr>
<tr><td>미경화 층</td><td>경화 후 남는 끈적한 막. 알코올로 닦습니다</td></tr>
<tr><td>강화제</td><td>맨 손톱에 바르는 관리용 폴리시. 램프가 필요 없습니다</td></tr>
<tr><td>옴브레</td><td>뿌리에서 끝으로 가는 그라데이션</td></tr>
<tr><td>프렌치</td><td>끝을 가로지르는 다른 색 라인</td></tr>
<tr><td>자석 네일</td><td>자석 젤과 마그넷으로 만드는 빛줄기 효과</td></tr>
</tbody>
</table>
<h2>혼동하기 쉬운 짝</h2>
<p>제거(30,000₫, 약 20분)는 새 시술을 위해 젤을 벗기고, 필(190,000₫, 한 세트)은 남깁니다. 베이스 코트는 컬러 아래 층이고 강화제는 맨 손톱에 단독으로 씁니다. 팁은 붙이고 빌더 젤은 손톱 위에서 모양을 만듭니다.</p>
<!--anh:2-->
<h2>예약은 세 문장으로</h2>
<p>지금 손톱 상태, 제거인지 필인지, 단색인지 효과를 원하시는지만 알려 주세요. 사진을 가져오시면 담당자가 효과 이름을 대신 찾아 드립니다.</p>'''
zh='''<p>这是一份美甲常用术语的通俗解释:底胶、封层、甲缘皮肤、甲型、填补、卸甲、UV 与 LED 灯、加固胶。您可以整篇读完,也可以直接看表格查一个词。</p>
<h2>懂这些词有什么用</h2>
<p>两点。预约时能说清要做的项目,"卸掉重做"和"填补"是两种不同的工作,时间和价格都不一样。其次,您会明白手上正在发生什么,也就清楚甲油胶为什么能保持 2–3 周,以及为什么不该硬撕。</p>
<!--anh:1-->
<h2>术语表</h2>
<table>
<thead><tr><th>术语</th><th>含义</th></tr></thead>
<tbody>
<tr><td>底胶</td><td>最先涂的透明层,帮助颜色附着,并隔开色素与真甲</td></tr>
<tr><td>封层</td><td>最后涂的透明层,封住颜色并带来光泽</td></tr>
<tr><td>甲缘皮肤</td><td>甲根处的薄皮,作用是封住皮肤与指甲之间的缝隙</td></tr>
<tr><td>甲型</td><td>打磨后的轮廓:方形、圆形、椭圆、尖圆</td></tr>
<tr><td>卸甲</td><td>先磨掉封层,再浸泡约 20 分钟</td></tr>
<tr><td>填补</td><td>保留仍牢固的胶,只补甲根长出来的部分</td></tr>
<tr><td>加固胶</td><td>较稠的胶,在真甲上增加厚度与硬度</td></tr>
<tr><td>甲片 / Gel X</td><td>预成型的延长片;Gel X 为胶质,照灯固化</td></tr>
<tr><td>双层模具</td><td>透明模具,直接在手上用胶做长度</td></tr>
<tr><td>照灯固化</td><td>用 UV 或 LED 灯把每一层胶照硬</td></tr>
<tr><td>浮胶层</td><td>固化后留下的黏膜,用酒精擦掉</td></tr>
<tr><td>护甲油</td><td>涂在裸甲上的养护油,不需要照灯</td></tr>
<tr><td>渐变</td><td>从甲根到甲尖的颜色过渡</td></tr>
<tr><td>法式</td><td>甲尖横向的一道异色线</td></tr>
<tr><td>猫眼</td><td>用磁性胶和磁铁做出的光带效果</td></tr>
</tbody>
</table>
<h2>容易混的几组词</h2>
<p>卸甲(30,000₫,约 20 分钟)是清掉旧胶重做,填补(190,000₫ 一套)是保留旧胶。底胶在颜色之下,护甲油单独涂在裸甲上。甲片是粘上去的,加固胶是在甲面上塑形的。</p>
<!--anh:2-->
<h2>三句话完成预约</h2>
<p>告诉我们您现在甲面上是什么、要卸掉重做还是填补、想要纯色还是带效果。带一张图片也可以,美甲师会替您说出那个效果的名称。</p>'''
bai('thuat-ngu-nail','2026-11-23T08:30:00+07:00','Kiến thức nghề nail',
 A(('nail polish bottles','Các chai sơn và dụng cụ trên bàn làm nail','Polish bottles and tools on a salon table','네일샵 테이블의 폴리시와 도구','美甲桌上的甲油与工具'),
   [('manicure tools nails','Bộ dụng cụ dùng khi chỉnh form móng','Tools used for shaping nails','손톱 모양을 다듬는 도구','用于修形的美甲工具'),
    ('gel manicure lamp','Hơ gel dưới đèn LED sau mỗi lớp','Curing gel under a LED lamp','층마다 LED 램프로 경화','每一层都用 LED 灯照干')]),
 ('Thuật ngữ nail: base coat, top coat, cuticle, fill, phá gel nghĩa là gì',
  'Bảng tra 18 thuật ngữ nail thường gặp kèm định nghĩa ngắn và lúc bạn sẽ nghe tới, cùng bốn cặp từ dễ nhầm như phá gel với fill gel, úp móng với đắp gel.',
  'Thuật ngữ nail giải thích dễ hiểu | VESSCA',
  'Base coat, top coat, cuticle, form, fill, phá gel, builder gel, đèn UV và LED nghĩa là gì. Phá gel 30.000₫, fill gel 190.000₫. VESSCA Bình Thạnh.',
  ['thuật ngữ nail','base coat là gì','top coat là gì','cuticle là gì','fill gel là gì','phá gel là gì'],vi,faq),
 ('Nail Terms Explained: Base Coat, Top Coat, Cuticle, Fill',
  'A plain-language glossary of salon words, plus the pairs people mix up and the three sentences that make booking simple.',
  'Nail Terms Glossary | VESSCA Saigon',
  'Base coat, top coat, cuticle, fill, removal, builder gel and lamps explained. Removal 30,000₫, fill 190,000₫. VESSCA, Binh Thanh.',
  ['nail terms explained','base coat and top coat','nail salon Binh Thanh','Korean nails Saigon','gel manicure Ho Chi Minh City'],en,
  [('What does a base coat do?','It grips the colour and keeps pigment off the natural nail; the top coat seals and adds shine.'),
   ('Removal or fill?','Removal clears the old gel for a new set, about 20 minutes. A fill keeps the sound gel and rebuilds the regrown base.'),
   ('What is builder gel?','A thicker gel that adds strength and thickness, used when natural nails are thin or break easily.')]),
 ('네일 용어 정리: 베이스 코트, 탑 코트, 큐티클, 필',
  '네일샵 용어를 쉬운 말로 정리한 표와, 혼동하기 쉬운 짝, 그리고 예약을 간단히 끝내는 세 문장.',
  '네일 용어 정리 | 호치민 VESSCA',
  '베이스 코트, 탑 코트, 큐티클, 필, 제거, 빌더 젤, 램프 설명. 제거 30,000₫, 필 190,000₫. 호치민 빈탄 VESSCA.',
  ['네일 용어','베이스 코트','젤 제거','호치민 네일샵','빈탄 네일'],ko,
  [('베이스 코트는 왜 바르나요?','컬러 밀착을 돕고 색소가 자연 손톱에 배는 것을 막습니다. 탑 코트는 덮어 광택을 냅니다.'),
   ('제거와 필 중 무엇이 맞나요?','새로 하려면 제거(약 20분), 지금 젤이 단단하면 필이 맞습니다.'),
   ('빌더 젤은 무엇인가요?','두께와 강도를 더하는 된 젤로, 손톱이 얇거나 잘 깨질 때 씁니다.')]),
 ('美甲术语解释:底胶、封层、甲缘皮肤、填补',
  '用通俗说法整理的美甲术语表,容易混淆的几组词,以及三句话完成预约的方法。',
  '美甲术语表 | 胡志明 VESSCA',
  '底胶、封层、甲缘皮肤、填补、卸甲、加固胶与灯具解释。卸甲 30,000₫,填补 190,000₫。胡志明平盛郡 VESSCA。',
  ['美甲 术语','底胶 封层','胡志明 美甲','平盛郡 美甲店','韩式美甲 胡志明'],zh,
  [('底胶有什么用?','帮助颜色附着,并隔开色素与真甲;封层负责封住颜色和提供光泽。'),
   ('该卸掉重做还是填补?','要换新的就卸甲,约 20 分钟;旧胶仍牢固就填补。'),
   ('加固胶是什么?','较稠的胶,用来增加厚度与硬度,适合指甲薄或易裂的情况。')]))

# ---------- 25/11 — Nail nặn 3D, bột 3D ----------
vi='''<p>Nail nặn 3D là phần hoạ tiết nổi lên khỏi mặt móng, được tạo bằng bột acrylic hoặc gel đặc rồi gắn trên nền gel đã hơ khô. Tại VESSCA, mỗi chi tiết 3D tính 40.000–50.000₫ tuỳ độ phức tạp, cộng vào giá bộ nền. Bài này nói rõ cách làm, độ bền thật, nên nặn mấy ngón và kiểu này hợp dịp nào.</p>

<h2>Nặn 3D làm thế nào</h2>

<p>Nền phải xong trước. Kỹ thuật viên sơn gel màu, hơ đèn, rồi mới đặt chi tiết lên trên. Với bột 3D, bột acrylic được trộn với dung dịch chuyên dụng thành một viên dẻo, kỹ thuật viên dùng cọ và que nhỏ nặn từng cánh hoa, từng múi nơ ngay trên móng; viên bột tự cứng lại trong vài phút nên phải làm nhanh và dứt khoát. Với gel 3D, gel đặc giữ nguyên hình đã nặn cho đến khi hơ đèn, nên kỹ thuật viên có thời gian chỉnh dáng, nhưng chi tiết thường mềm hơn một chút.</p>

<p>Bước cuối là khoá chân chi tiết: phủ một ít top coat quanh phần tiếp giáp giữa chi tiết và mặt móng, rồi hơ lại. Đây là bước quyết định chi tiết có bám lâu hay không.</p>

<h2>Độ bền thật và cảm giác khi dùng</h2>

<p>Nền gel giữ hai đến ba tuần như bình thường. Chi tiết 3D thì phụ thuộc vào độ cao và vị trí. Chi tiết cao một đến hai milimét, nằm ở gốc hoặc giữa mặt móng, thường trụ được hết bộ. Chi tiết cao bốn đến năm milimét hoặc đặt ở đầu móng dễ bị cạy ra khi va vào mép bàn, túi xách, tay lái.</p>

<p>Về cảm giác, chi tiết nổi làm một số việc hằng ngày khó hơn: gõ phím, cài nút áo, đeo bao tay cao su, gội đầu. Nếu bạn làm việc bàn phím nhiều, nên để chi tiết ở ngón áp út hoặc ngón giữa thay vì ngón trỏ.</p>

<!--anh:1-->
<h2>Nên nặn mấy ngón</h2>

<table>
<thead><tr><th>Cách bố trí</th><th>Hợp với</th><th>Lưu ý</th></tr></thead>
<tbody>
<tr><td>Một chi tiết nhỏ ở một ngón</td><td>Đi làm, dùng hằng ngày</td><td>Ít vướng nhất, thêm 40.000–50.000₫ vào giá bộ</td></tr>
<tr><td>Hai ngón nhấn, mỗi bàn một ngón</td><td>Tiệc, chụp ảnh, sinh nhật</td><td>Nên đặt cùng vị trí ở hai bàn cho cân</td></tr>
<tr><td>Một chi tiết lớn cộng vài chi tiết nhỏ</td><td>Dịp quan trọng, ảnh cận tay</td><td>Chi tiết lớn nên ở ngón giữa hoặc áp út</td></tr>
<tr><td>Kín mười ngón</td><td>Buổi chụp hình, biểu diễn</td><td>Khó dùng việc hằng ngày, thường tháo sớm</td></tr>
<tr><td>Móng chân</td><td>Dịp mặc sandal, đi biển</td><td>Chọn chi tiết thấp, tránh ngón cái cọ vào giày kín</td></tr>
</tbody>
</table>

<h2>Hợp dịp nào</h2>

<p>Nặn 3D mạnh nhất ở các dịp có chụp ảnh gần: sinh nhật, tiệc cuối năm, đám cưới, lễ tốt nghiệp. Hoa nổi và nơ nhỏ cho hiệu ứng rõ trên ảnh hơn hẳn hoạ tiết vẽ phẳng, vì chúng có bóng đổ thật. Nếu bạn chỉ muốn một bộ dùng dài ngày, một hai chi tiết nhỏ là đủ, phần còn lại để nền trơn.</p>

<p>Nền càng chắc thì chi tiết càng bám lâu. Nếu móng thật mỏng, nên đắp một lớp builder gel mỏng làm nền trước. Xem bài <a href="/blog/gel-builder-lam-cung-mong/">gel builder làm cứng móng</a>.</p>

<!--anh:2-->
<h2>Giá và cách đặt</h2>

<p>Một bộ nền gồm cắt da, chỉnh form, dưỡng viền tay 60.000₫ và sơn gel trơn 130.000₫, tức 190.000₫. Thêm hai chi tiết 3D ở mức 40.000₫ mỗi chi tiết: 190.000 + 2 × 40.000 = 270.000₫. Nếu chi tiết phức tạp hơn, tính 50.000₫ mỗi chi tiết: 190.000 + 2 × 50.000 = 290.000₫. Muốn đính thêm thì đá thường 10.000₫ một viên, đá Swarovski 20.000₫ một viên, ngọc trai và charm từ 5.000₫ một viên.</p>

<p>Khi đặt lịch, nói rõ bạn muốn nặn mấy ngón và mang ảnh mẫu. Nặn 3D mất thêm thời gian so với bộ trơn, nên tiệm cần xếp lịch dài hơn. So sánh với cách vẽ phẳng có trong bài <a href="/blog/ve-nail-tay-hay-sticker/">vẽ nail tay hay dán sticker</a>, còn kiểu đính đá nằm ở bài <a href="/blog/nail-dinh-da-kieu-han/">nail đính đá kiểu Hàn</a>.</p>'''
faq=[('Nặn 3D giá bao nhiêu?','Mỗi chi tiết 3D 40.000–50.000₫ tuỳ độ phức tạp, cộng vào giá bộ nền. Ví dụ cắt da tay 60.000₫ cộng gel trơn 130.000₫ cộng hai chi tiết 40.000₫ là 270.000₫.'),
 ('Chi tiết 3D giữ được bao lâu?','Nền gel giữ hai đến ba tuần. Chi tiết cao một đến hai milimét thường trụ hết bộ, chi tiết cao hơn hoặc nằm ở đầu móng dễ bị cạy ra khi va.'),
 ('Nên nặn 3D mấy ngón?','Đi làm hằng ngày thì một ngón. Dịp tiệc hoặc chụp ảnh thì hai ngón nhấn, mỗi bàn một ngón cho cân.'),
 ('Bột 3D và gel 3D khác nhau thế nào?','Bột acrylic tự cứng trong vài phút nên nét dứt khoát và cứng hơn. Gel đặc chỉ cứng khi hơ đèn nên chỉnh dáng được lâu hơn.')]
en='''<p>A 3D nail detail is a raised shape — a flower, a bow, a small figure — sculpted from acrylic powder or thick gel onto a cured gel base. At VESSCA each 3D detail is 40,000–50,000₫ depending on complexity, added to the price of the set.</p>
<h2>How it is made</h2>
<p>The coloured base is cured first. Acrylic powder is mixed into a soft bead and sculpted petal by petal on the nail; it sets in minutes, so the work is fast and decisive. Thick gel holds its shape until it is cured, which allows more adjusting but stays a little softer. The last step seals the foot of the detail with top coat.</p>
<h2>How long it lasts</h2>
<p>The gel base still gives two to three weeks. A detail 1–2 mm high in the middle of the nail usually survives the whole set; a 4–5 mm one, or anything near the tip, catches on bags and desk edges. Raised details also make typing, buttons and rubber gloves harder, so keep them off the index finger.</p>
<!--anh:1-->
<h2>How many fingers</h2>
<table>
<thead><tr><th>Placement</th><th>Best for</th></tr></thead>
<tbody>
<tr><td>One small detail on one nail</td><td>Everyday and office wear</td></tr>
<tr><td>Two accent nails, one per hand</td><td>Parties, birthdays, photos</td></tr>
<tr><td>One large detail plus small ones</td><td>Weddings and close-up photos</td></tr>
<tr><td>All ten nails</td><td>Photo shoots; hard to live with</td></tr>
<tr><td>Toes</td><td>Sandals; keep details low</td></tr>
</tbody>
</table>
<h2>Price example</h2>
<p>Hand cuticle work and shaping 60,000₫ plus plain gel 130,000₫ is 190,000₫. Two 3D details at 40,000₫ each: 190,000 + 2 × 40,000 = 270,000₫. Stones are 10,000₫ each, Swarovski 20,000₫, pearls and charms from 5,000₫.</p>
<!--anh:2-->
<h2>Booking</h2>
<p>Say how many nails you want sculpted and bring a photo. Sculpting takes longer than a plain set, so we book extra time. A thin builder gel base helps the details hold if your nails are thin.</p>'''
ko='''<p>3D 네일은 손톱 위로 올라오는 입체 장식입니다. 아크릴 파우더나 된 젤로 꽃, 리본, 작은 캐릭터를 경화된 젤 베이스 위에 직접 올립니다. VESSCA에서는 디테일 하나당 40,000–50,000₫이며, 세트 가격에 더해집니다.</p>
<h2>만드는 방법</h2>
<p>먼저 컬러 베이스를 경화합니다. 아크릴 파우더는 전용 리퀴드와 섞어 부드러운 덩어리로 만들어 꽃잎 하나씩 손톱 위에서 올립니다. 몇 분 안에 굳으므로 빠르고 단호한 작업이 필요합니다. 된 젤은 경화할 때까지 모양을 유지하므로 수정 시간이 길지만 조금 더 무릅니다. 마지막에 장식 밑동을 탑 코트로 감싸 고정합니다.</p>
<h2>지속력</h2>
<p>젤 베이스는 평소처럼 2–3주 유지됩니다. 높이 1–2 mm, 손톱 가운데 쪽 장식은 보통 끝까지 버팁니다. 4–5 mm거나 끝에 가까운 장식은 가방과 책상 모서리에 걸려 떨어지기 쉽습니다. 입체 장식은 타이핑, 단추, 고무장갑에도 불편하니 검지는 피하시는 편이 좋습니다.</p>
<!--anh:1-->
<h2>몇 손가락에 할까요</h2>
<table>
<thead><tr><th>배치</th><th>추천 상황</th></tr></thead>
<tbody>
<tr><td>작은 장식 한 손가락</td><td>출근, 일상</td></tr>
<tr><td>양손 각 한 손가락 포인트</td><td>파티, 생일, 사진</td></tr>
<tr><td>큰 장식 하나 + 작은 장식</td><td>예식, 손 클로즈업</td></tr>
<tr><td>열 손가락 전체</td><td>촬영용. 일상에는 불편합니다</td></tr>
<tr><td>발</td><td>샌들 시즌. 낮은 장식으로</td></tr>
</tbody>
</table>
<h2>가격 예시</h2>
<p>손 큐티클·모양 정리 60,000₫에 단색 젤 130,000₫이면 190,000₫입니다. 40,000₫짜리 3D 두 개를 더하면 190,000 + 2 × 40,000 = 270,000₫입니다. 스톤 10,000₫, 스와로브스키 20,000₫, 진주·참 5,000₫부터입니다.</p>
<!--anh:2-->
<h2>예약 안내</h2>
<p>몇 손가락에 올릴지 알려 주시고 사진을 가져오세요. 단색보다 시간이 더 걸리므로 넉넉히 예약해 드립니다. 손톱이 얇으면 얇은 빌더 젤 베이스가 장식 유지에 도움이 됩니다.</p>'''
zh='''<p>3D 美甲是凸出甲面的立体装饰:用亚克力粉或稠胶在已固化的胶面上做出花朵、蝴蝶结或小造型。在 VESSCA,每个 3D 细节 40,000–50,000₫,按复杂度计,另加在整套价格之上。</p>
<h2>怎么做出来</h2>
<p>先把颜色底色照灯固化。亚克力粉与专用液调成一个软团,美甲师用笔和小棒在甲面上一片一片塑出花瓣;它几分钟就硬,所以手要快而准。稠胶在照灯前一直保持形状,可以反复修形,但成品略软一些。最后一步是用封层包住装饰的根部并再照灯。</p>
<h2>实际能戴多久</h2>
<p>胶底色照常保持 2–3 周。高 1–2 mm 且位于甲面中段的装饰通常能坚持到整套结束;4–5 mm 或靠近甲尖的装饰,容易被包袋、桌沿勾掉。立体装饰也会让打字、扣纽扣、戴橡胶手套变麻烦,建议避开食指。</p>
<!--anh:1-->
<h2>做几个手指</h2>
<table>
<thead><tr><th>布局</th><th>适合</th></tr></thead>
<tbody>
<tr><td>一指一个小装饰</td><td>上班、日常</td></tr>
<tr><td>两手各一指点缀</td><td>聚会、生日、拍照</td></tr>
<tr><td>一个大装饰加几个小的</td><td>婚礼、手部特写</td></tr>
<tr><td>十指满做</td><td>拍摄用,日常不便</td></tr>
<tr><td>脚趾</td><td>凉鞋季,装饰要低</td></tr>
</tbody>
</table>
<h2>价格示例</h2>
<p>手部死皮与修形 60,000₫ 加纯色胶 130,000₫,即 190,000₫。再加两个 40,000₫ 的 3D:190,000 + 2 × 40,000 = 270,000₫。普通钻 10,000₫ 一颗,施华洛世奇 20,000₫ 一颗,珍珠与挂饰 5,000₫ 起。</p>
<!--anh:2-->
<h2>预约提示</h2>
<p>请告诉我们您想在几个指甲上做,并带一张参考图。立体塑形比纯色耗时,我们会预留更长时间。若您的指甲偏薄,先打一层薄加固胶底会让装饰更牢。</p>'''
bai('nail-3d-nan-hoat-hinh','2026-11-25T08:30:00+07:00','Xu hướng & Cảm hứng',
 A(('3d flower nails','Hoa nổi nặn 3D trên nền gel','Sculpted 3D flowers on a gel base','젤 베이스 위 3D 입체 꽃','胶底色上的 3D 立体花'),
   [('nail art manicure','Kỹ thuật viên nặn chi tiết trên móng','Technician sculpting a detail on the nail','손톱에 입체 장식을 올리는 모습','美甲师在甲面塑形'),
    ('party nails manicure','Hai ngón nhấn chi tiết 3D cho dịp tiệc','Two accent nails with 3D details','파티용 3D 포인트 두 손가락','聚会用的两指 3D 点缀')]),
 ('Nail nặn 3D và bột 3D: cách làm, độ bền và nên nặn mấy ngón',
  'Nặn 3D bằng bột acrylic hay gel đặc khác nhau thế nào, chi tiết giữ được bao lâu, nên nặn mấy ngón theo nhu cầu, hợp dịp nào và giá cộng ra sao.',
  'Nail nặn 3D, bột 3D: cách làm và giá | VESSCA',
  'Nặn 3D mỗi chi tiết 40.000–50.000₫ cộng vào bộ nền. Nền gel 190.000₫ cộng hai chi tiết là 270.000₫. Nên nặn mấy ngón. VESSCA Bình Thạnh.',
  ['nail nặn 3D','bột 3D nail','nail 3D giá bao nhiêu','nail nặn hoa nổi','nail 3D giữ được bao lâu'],vi,faq),
 ('3D Sculpted Nails: How They Are Made, How Long They Last',
  'Acrylic powder versus thick gel, realistic wear time, how many nails to sculpt and a worked price example.',
  '3D Sculpted Nails | VESSCA Saigon',
  '3D details are 40,000–50,000₫ each on top of the set: gel base 190,000₫ plus two details is 270,000₫. VESSCA, Binh Thanh.',
  ['3D sculpted nails','3D nail art Saigon','nail salon Binh Thanh','Korean nails Saigon','acrylic 3D nails'],en,
  [('How much is a 3D detail?','40,000–50,000₫ each, added to the set. Hand prep 60,000₫ plus plain gel 130,000₫ plus two details at 40,000₫ is 270,000₫.'),
   ('How long do the details last?','The gel base lasts two to three weeks; low 1–2 mm details usually last the whole set, taller ones catch and come off.'),
   ('How many nails should I sculpt?','One for everyday wear, or two accent nails, one per hand, for parties and photos.')]),
 ('3D 입체 네일: 만드는 방법과 지속력',
  '아크릴 파우더와 된 젤의 차이, 실제 지속력, 몇 손가락이 좋은지, 가격 계산 예시.',
  '3D 입체 네일 안내 | 호치민 VESSCA',
  '3D 디테일은 개당 40,000–50,000₫ 추가. 젤 베이스 190,000₫ + 두 개면 270,000₫. 호치민 빈탄 VESSCA.',
  ['3D 네일','입체 네일','호치민 네일샵','빈탄 네일','한국 젤네일 호치민'],ko,
  [('3D 디테일 가격은?','개당 40,000–50,000₫이며 세트에 더해집니다. 손 정리 60,000₫ + 단색 젤 130,000₫ + 40,000₫ 두 개면 270,000₫입니다.'),
   ('얼마나 유지되나요?','젤 베이스는 2–3주. 1–2 mm 낮은 장식은 보통 끝까지 가고, 높은 장식은 걸려 떨어집니다.'),
   ('몇 손가락이 좋을까요?','일상은 한 손가락, 파티나 사진은 양손 각 한 손가락 포인트가 좋습니다.')]),
 ('3D 立体美甲:怎么做、能戴多久',
  '亚克力粉与稠胶的差别、真实持久度、做几个手指合适,以及价格计算示例。',
  '3D 立体美甲指南 | 胡志明 VESSCA',
  '3D 细节每个 40,000–50,000₫ 另加。胶底色 190,000₫ 加两个即 270,000₫。胡志明平盛郡 VESSCA。',
  ['3D 美甲','立体美甲','胡志明 美甲','平盛郡 美甲店','韩式美甲 胡志明'],zh,
  [('一个 3D 细节多少钱?','每个 40,000–50,000₫,另加在整套之上。手部护理 60,000₫ + 纯色胶 130,000₫ + 两个 40,000₫ 即 270,000₫。'),
   ('能保持多久?','胶底色 2–3 周;1–2 mm 的低装饰通常能到最后,过高的容易被勾掉。'),
   ('做几个指甲合适?','日常一个指甲,聚会或拍照时两手各一指点缀。')]))

# ---------- 27/11 — Nail cho mẹ, người lớn tuổi ----------
vi='''<p>Nail cho mẹ hoặc người lớn tuổi nên đặt việc dưỡng lên trước việc chọn màu. Theo tuổi, móng mỏng dần, xuất hiện sọc dọc và dễ giòn hơn, nên bộ phù hợp thường là móng ngắn, bề mặt phẳng, màu sáng ấm và không đính chi tiết nổi. Bài này nói rõ móng thay đổi thế nào, màu nào tôn tay, độ dài nào tiện, và cách tặng mẹ một buổi làm móng.</p>

<h2>Móng thay đổi thế nào theo tuổi</h2>

<p>Có ba thay đổi thường gặp. Thứ nhất, bản móng mỏng dần và mọc chậm hơn, nên móng chịu được ít lần dũa hơn trước. Thứ hai, trên mặt móng xuất hiện sọc dọc, là những đường gân nhỏ chạy từ gốc ra đầu móng; đây là thay đổi thường gặp theo tuổi, không phải dấu hiệu bệnh. Thứ ba, da quanh móng mỏng và khô hơn vì da tiết ít dầu hơn, nên dễ xước măng rô và dễ rát khi cắt da.</p>

<p>Bài viết chỉ mang tính tham khảo. Nếu móng dày lên bất thường, đổi màu ở một móng, có sọc ngang rõ hoặc đau, nên gặp bác sĩ da liễu thay vì xử lý ở tiệm. Phân biệt các loại sọc và đốm có trong bài <a href="/blog/mong-soc-doc-dom-trang/">móng có sọc dọc và đốm trắng</a>.</p>

<h2>Vì sao nên ưu tiên dưỡng và sơn nhẹ</h2>

<p>Với móng mỏng, phần làm nên khác biệt là viền da và độ ẩm, không phải lớp màu. Một buổi cắt da nhẹ tay, chỉnh form ngắn gọn và dưỡng viền kỹ cho kết quả thấy rõ hơn một bộ nhiều chi tiết. Tại VESSCA, cắt da, chỉnh form và dưỡng viền tay 60.000₫, thêm sơn cứng móng 40.000₫ thì tổng là 100.000₫. Đây là bộ nhẹ nhất mà vẫn gọn gàng. Nếu móng còn đủ chắc và mẹ muốn có màu giữ lâu, sơn gel trơn 130.000₫, cộng với phần cắt da là 190.000₫.</p>

<p>Điều cần nói trước với kỹ thuật viên là móng mỏng, để tiệm dũa bề mặt ít nhất có thể và không dùng lực mạnh ở viền da. Khi tháo gel cũng vậy: ủ dung dịch đủ thời gian rồi đẩy nhẹ, không cạy.</p>

<!--anh:1-->
<h2>Màu nào tôn tay</h2>

<table>
<thead><tr><th>Nhóm màu</th><th>Vì sao hợp</th></tr></thead>
<tbody>
<tr><td>Hồng sữa, nude ngả hồng</td><td>Che được sọc dọc nhẹ, làm tay trông tươi mà không lộ</td></tr>
<tr><td>Be ấm, nâu hồng nhạt</td><td>Trung tính, đi với mọi màu áo và mọi dịp</td></tr>
<tr><td>Đỏ trầm, đỏ gạch</td><td>Tông ấm cổ điển, lên tay rõ nét, hợp dịp gặp họ hàng</td></tr>
<tr><td>Tím mận nhạt, hồng khô</td><td>Có sắc mà vẫn nhã, tôn bàn tay có mạch máu nổi</td></tr>
<tr><td>Trắng sữa đục</td><td>Làm móng ngắn trông sạch và dài hơn một chút</td></tr>
<tr><td>Nên cân nhắc</td><td>Xám tro nhạt, màu neon, đen đặc trên móng rất ngắn: dễ làm tay trông khô và cứng</td></tr>
</tbody>
</table>

<p>Màu đục sữa nhìn chung dễ mặc hơn màu trong, vì lớp màu đặc che được phần mặt móng không còn phẳng. Các sắc nude cụ thể có trong bài <a href="/blog/nail-nude-kieu-han/">nail nude kiểu Hàn</a>.</p>

<h2>Độ dài và form nào tiện</h2>

<p>Ngắn là tiện nhất: dài hơn đầu ngón một đến hai milimét, hoặc bằng đầu ngón. Form tròn hoặc oval nhẹ, đầu móng không để nhọn. Lý do rất thực tế: móng ngắn và tròn không xước da khi chăm cháu nhỏ, không vướng khi cài nút áo, không cộm khi vo gạo hay rửa rau, và đỡ gãy khi móng đã giòn. Móng chân cũng nên cắt ngang, không cắt sâu hai bên, để tránh mọc quặp.</p>

<!--anh:2-->
<h2>Tặng mẹ một buổi làm móng</h2>

<p>Đây là món quà dùng được ngay và không cần chọn size. Cách làm gọn nhất là đặt lịch trước giúp mẹ và đi cùng, vì nhiều người lớn tuổi không quen đặt lịch qua form hay nhắn tin. Khi đặt, nói rõ là làm cho người lớn tuổi và móng mỏng, tiệm sẽ xếp kỹ thuật viên và thời gian phù hợp.</p>

<p>Nếu muốn nhẹ nhàng hơn nữa, Hand Ritual 250.000₫ trong 30 phút tập trung vào làm sạch, làm mềm và dưỡng ẩm cả bàn tay. Phần chân có Foot Ritual 350.000₫ trong 45 phút, hoặc cắt da, chỉnh form, dưỡng viền chân 70.000₫. Chi tiết hai gói này ở bài <a href="/blog/hand-ritual-foot-ritual-vessca/">Hand Ritual và Foot Ritual</a>. VESSCA giới hạn số khách cùng lúc nên không gian yên, phù hợp với người không thích chỗ đông.</p>'''
faq=[('Người lớn tuổi có làm sơn gel được không?','Được nếu móng còn đủ chắc. Nên nói trước là móng mỏng để kỹ thuật viên dũa bề mặt ít nhất có thể và tháo bằng cách ủ dung dịch, không cạy.'),
 ('Móng có sọc dọc thì sơn màu gì?','Màu đục sữa như hồng sữa, be ấm, trắng sữa che bề mặt tốt hơn màu trong. Sọc dọc là thay đổi thường gặp theo tuổi.'),
 ('Nên để móng dài bao nhiêu?','Dài hơn đầu ngón một đến hai milimét, form tròn hoặc oval nhẹ, đầu móng không nhọn để tiện việc nhà và đỡ gãy.'),
 ('Tặng mẹ buổi làm móng thì chọn gì?','Cắt da chỉnh form dưỡng viền tay 60.000₫ cộng sơn cứng móng 40.000₫ là 100.000₫ cho bộ nhẹ. Muốn thư giãn hơn thì Hand Ritual 250.000₫ trong 30 phút.')]
en='''<p>For older hands, care comes before colour. With age the nail plate thins, vertical ridges appear and nails become more brittle, so the set that works is short, flat-surfaced, in a warm light shade, with no raised decoration.</p>
<h2>What changes with age</h2>
<p>Three things. The plate thins and grows more slowly, so it tolerates less filing. Vertical ridges run from base to tip — a common age-related change, not a disease. The skin around the nail is thinner and drier, so hangnails and soreness after cuticle work are more likely. This article is general information; see a dermatologist for thickening, discolouration of one nail, horizontal ridges or pain.</p>
<h2>Why gentle is better</h2>
<p>On thin nails, cuticle condition and moisture matter more than the colour layer. Gentle cuticle work, light shaping and oil give a clearer result than a busy design. At VESSCA hand cuticle work and shaping is 60,000₫; with a strengthener at 40,000₫ the total is 100,000₫. Plain gel is 130,000₫, so 190,000₫ with the prep. Tell the technician the nails are thin so surface filing stays minimal and removal is done by soaking.</p>
<!--anh:1-->
<h2>Colours that flatter</h2>
<table>
<thead><tr><th>Family</th><th>Why</th></tr></thead>
<tbody>
<tr><td>Milky pink, pink nude</td><td>Covers light ridging, looks fresh without drawing attention</td></tr>
<tr><td>Warm beige, soft rosy brown</td><td>Neutral, works with anything</td></tr>
<tr><td>Deep red, brick red</td><td>Classic warm tone, reads clearly on the hand</td></tr>
<tr><td>Soft plum, dusty rose</td><td>Colour without loudness</td></tr>
<tr><td>Milky white</td><td>Makes short nails look clean and slightly longer</td></tr>
<tr><td>Reconsider</td><td>Pale grey, neon, solid black on very short nails</td></tr>
</tbody>
</table>
<h2>Length and shape</h2>
<p>Short is practical: one to two millimetres past the fingertip, round or soft oval, no sharp points. Short round nails do not scratch a grandchild, do not catch on buttons and break less when nails are brittle.</p>
<!--anh:2-->
<h2>As a gift</h2>
<p>Book ahead and come along — many older customers are not used to online forms. Say it is for an older guest with thin nails so we allow the right time. Hand Ritual is 250,000₫ for 30 minutes, Foot Ritual 350,000₫ for 45 minutes, foot cuticle work 70,000₫. VESSCA keeps the number of guests limited, so the room stays quiet.</p>'''
ko='''<p>어머니나 연세 있는 분의 네일은 컬러보다 관리가 먼저입니다. 나이가 들면 손톱이 얇아지고 세로 줄이 생기며 더 쉽게 부러집니다. 그래서 짧은 길이, 평평한 표면, 따뜻한 밝은 색, 입체 장식 없는 구성이 잘 맞습니다.</p>
<h2>나이에 따른 변화</h2>
<p>세 가지입니다. 손톱판이 얇아지고 성장이 느려져 파일링을 견디는 정도가 줄어듭니다. 뿌리에서 끝으로 가는 세로 줄이 생기는데, 이는 흔한 노화 변화이며 질병이 아닙니다. 손톱 주변 피부도 얇고 건조해져 거스러미와 자극이 생기기 쉽습니다. 이 글은 참고용입니다. 한 손톱만 색이 변하거나 두꺼워지거나 가로 줄, 통증이 있으면 피부과 진료를 권합니다.</p>
<h2>부드러운 시술이 좋은 이유</h2>
<p>얇은 손톱에서는 컬러보다 큐티클 상태와 수분이 결과를 좌우합니다. VESSCA 손 큐티클·모양 정리 60,000₫, 강화제 40,000₫을 더하면 100,000₫입니다. 단색 젤은 130,000₫이라 정리까지 190,000₫입니다. 손톱이 얇다고 미리 말씀해 주시면 표면 파일링을 최소화하고 제거는 불려서 진행합니다.</p>
<!--anh:1-->
<h2>잘 어울리는 컬러</h2>
<table>
<thead><tr><th>계열</th><th>이유</th></tr></thead>
<tbody>
<tr><td>밀키 핑크, 핑크 누드</td><td>가벼운 세로 줄을 덮고 손이 생기 있어 보입니다</td></tr>
<tr><td>웜 베이지, 로지 브라운</td><td>중립적이라 어떤 옷에도 맞습니다</td></tr>
<tr><td>딥 레드, 브릭 레드</td><td>따뜻한 클래식 톤으로 손에 또렷하게 올라옵니다</td></tr>
<tr><td>연한 플럼, 더스티 로즈</td><td>색감은 있으면서 과하지 않습니다</td></tr>
<tr><td>밀키 화이트</td><td>짧은 손톱이 깔끔하고 조금 길어 보입니다</td></tr>
<tr><td>재고</td><td>흐린 그레이, 네온, 아주 짧은 손톱의 진한 블랙</td></tr>
</tbody>
</table>
<h2>길이와 모양</h2>
<p>짧은 쪽이 편합니다. 손끝에서 1–2 mm, 라운드나 부드러운 오벌, 끝은 뾰족하지 않게. 짧고 둥근 손톱은 아이를 돌볼 때 긁히지 않고 단추에 걸리지 않으며 잘 부러지지 않습니다.</p>
<!--anh:2-->
<h2>선물로 드릴 때</h2>
<p>미리 예약하고 함께 오시는 방법을 권합니다. 연세 있는 분은 온라인 예약이 익숙하지 않을 수 있습니다. 손톱이 얇은 어르신이라고 알려 주시면 시간을 넉넉히 잡습니다. 핸드 리추얼 250,000₫(30분), 풋 리추얼 350,000₫(45분), 발 큐티클 정리 70,000₫입니다. 동시 손님 수를 제한해 조용합니다.</p>'''
zh='''<p>给母亲或长辈做美甲,养护要排在选色之前。随着年龄增长,甲板变薄、出现竖纹、更容易脆裂,因此合适的做法是短长度、平整甲面、温暖的浅色,并且不加立体装饰。</p>
<h2>指甲随年龄的变化</h2>
<p>有三点。甲板变薄、生长变慢,能承受的打磨更少。甲面出现从甲根到甲尖的竖纹,这是常见的年龄变化,不是疾病。甲周皮肤更薄更干,容易起倒刺,修皮后也更容易发痛。本文仅供参考;若出现单个指甲变色、异常增厚、明显横纹或疼痛,建议就医。</p>
<h2>为什么要做得轻</h2>
<p>在薄甲上,甲缘状态和水分比色层更决定效果。VESSCA 手部死皮与修形 60,000₫,加护甲油 40,000₫,合计 100,000₫。纯色胶 130,000₫,连同前期护理为 190,000₫。请提前说明指甲偏薄,我们会尽量少磨甲面,并用浸泡方式卸甲。</p>
<!--anh:1-->
<h2>显气色的颜色</h2>
<table>
<thead><tr><th>色系</th><th>原因</th></tr></thead>
<tbody>
<tr><td>奶粉色、粉裸色</td><td>能盖住轻微竖纹,显得干净有气色</td></tr>
<tr><td>暖米色、浅玫瑰棕</td><td>中性,搭配任何衣服</td></tr>
<tr><td>深红、砖红</td><td>温暖的经典色,在手上很分明</td></tr>
<tr><td>浅梅子色、干玫瑰</td><td>有颜色但不张扬</td></tr>
<tr><td>奶白色</td><td>让短甲显得干净、稍长</td></tr>
<tr><td>建议斟酌</td><td>浅灰、荧光色,以及很短甲面上的纯黑</td></tr>
</tbody>
</table>
<h2>长度与甲型</h2>
<p>短一点更方便:超出指尖 1–2 mm,圆形或柔和椭圆,甲尖不留尖。短而圆的指甲抱孩子不会刮到,扣纽扣不勾手,脆甲也更不容易裂。</p>
<!--anh:2-->
<h2>作为礼物</h2>
<p>建议您提前预约并陪同前来,长辈常不习惯线上预约。告诉我们是长辈、指甲偏薄,我们会安排更充裕的时间。手部仪式 250,000₫(30 分钟),足部仪式 350,000₫(45 分钟),足部死皮护理 70,000₫。VESSCA 限制同时接待人数,环境安静。</p>'''
bai('nail-cho-me-nguoi-lon-tuoi','2026-11-27T08:30:00+07:00','Xu hướng & Cảm hứng',
 A(('elegant short nails','Bàn tay người lớn tuổi với móng ngắn sơn hồng sữa','Older hands with short milky pink nails','짧은 밀키 핑크 네일을 한 어른의 손','短款奶粉色美甲的长辈双手'),
   [('nude nail polish','Màu nude ngả hồng trên móng ngắn','Pink nude on short nails','짧은 손톱의 핑크 누드','短甲上的粉裸色'),
    ('hand care manicure','Buổi dưỡng tay và viền móng tại tiệm','Hand and cuticle care at the salon','샵에서 받는 손·큐티클 관리','店内的手部与甲缘护理')]),
 ('Nail cho mẹ và người lớn tuổi: màu nào tôn tay, độ dài nào tiện',
  'Móng mỏng và có sọc dọc theo tuổi nên cần dưỡng trước, sơn nhẹ sau. Nhóm màu tôn tay, độ dài và form tiện việc nhà, cùng cách tặng mẹ một buổi làm móng.',
  'Nail cho mẹ, người lớn tuổi: màu và độ dài | VESSCA',
  'Móng mỏng, có sọc dọc nên chọn móng ngắn, màu đục sữa, bề mặt phẳng. Cắt da 60.000₫ cộng sơn cứng móng 40.000₫ là 100.000₫. VESSCA Bình Thạnh.',
  ['nail cho người lớn tuổi','nail cho mẹ','móng mỏng sơn màu gì','quà tặng mẹ làm nail','móng có sọc dọc sơn gì'],vi,faq),
 ('Nails for Older Hands: Colours, Length and Gentle Care',
  'Thinning nails and vertical ridges change what works: short length, milky shades, flat surfaces, and care before colour.',
  'Nails for Older Hands | VESSCA Saigon',
  'Thin, ridged nails suit short length and milky shades. Cuticle work 60,000₫ plus strengthener 40,000₫ is 100,000₫. VESSCA, Binh Thanh.',
  ['nails for older hands','gentle manicure','nail salon Binh Thanh','Korean nails Saigon','nail ridges age'],en,
  [('Can older nails take gel?','Yes if the nail is sound. Say the nails are thin so filing stays minimal and removal is done by soaking.'),
   ('Which colours cover ridges?','Milky shades — milky pink, warm beige, milky white — cover better than sheer colours.'),
   ('What length is practical?','One to two millimetres past the fingertip, round or soft oval, with no sharp points.')]),
 ('어머니·어르신 네일: 컬러, 길이, 부드러운 관리',
  '얇아진 손톱과 세로 줄에 맞는 선택: 짧은 길이, 밀키 컬러, 평평한 표면, 그리고 컬러보다 먼저인 관리.',
  '어르신 네일 가이드 | 호치민 VESSCA',
  '얇고 세로 줄 있는 손톱에는 짧은 길이와 밀키 컬러. 큐티클 정리 60,000₫ + 강화제 40,000₫ = 100,000₫. 호치민 빈탄 VESSCA.',
  ['어르신 네일','부드러운 네일 관리','호치민 네일샵','빈탄 네일','손톱 세로 줄'],ko,
  [('어르신도 젤이 가능한가요?','손톱이 단단하면 가능합니다. 얇다고 말씀해 주시면 파일링을 최소화하고 불려서 제거합니다.'),
   ('세로 줄은 어떤 색이 덮나요?','밀키 핑크, 웜 베이지, 밀키 화이트 같은 불투명 계열이 잘 덮습니다.'),
   ('어떤 길이가 편한가요?','손끝에서 1–2 mm, 라운드나 부드러운 오벌, 끝은 뾰족하지 않게 합니다.')]),
 ('长辈美甲:颜色、长度与轻柔护理',
  '甲板变薄与竖纹改变了选择:短长度、奶油色系、平整甲面,以及养护先于颜色。',
  '长辈美甲指南 | 胡志明 VESSCA',
  '薄甲与竖纹适合短长度和奶油色系。死皮护理 60,000₫ 加护甲油 40,000₫ 共 100,000₫。胡志明平盛郡 VESSCA。',
  ['长辈 美甲','薄甲 美甲','胡志明 美甲','平盛郡 美甲店','指甲 竖纹'],zh,
  [('长辈可以做甲油胶吗?','指甲状况良好就可以。请说明指甲偏薄,我们会少磨甲面并用浸泡卸甲。'),
   ('什么颜色能盖竖纹?','奶粉色、暖米色、奶白色等不透明色系比透色更能覆盖。'),
   ('多长比较方便?','超出指尖 1–2 mm,圆形或柔和椭圆,甲尖不留尖。')]))

# ---------- 30/11 — Nail hoa nhí vẽ tay ----------
vi='''<p>Hoa nhí vẽ tay là những bông hoa nhỏ cỡ hai đến bốn milimét, kỹ thuật viên vẽ trực tiếp lên móng bằng cọ mảnh và gel màu. Tại VESSCA, phần vẽ tính từ 10.000₫ mỗi chi tiết, cộng vào giá bộ nền. Bài này nói về cách vẽ, cỡ hoa theo độ dài móng, cách phối nền và điểm khác so với sticker.</p>

<h2>Hoa nhí được vẽ thế nào</h2>

<p>Nền phải khô trước. Kỹ thuật viên sơn gel màu nền, hơ đèn, rồi mới vẽ lên trên. Cọ dùng để vẽ hoa nhí là cọ đầu nhỏ và cọ liner, loại có lông dài và mảnh để kéo được nét liền. Gel màu dùng để vẽ đặc hơn gel sơn thường, nhờ vậy nét không loang ra khi đặt lên nền.</p>

<p>Mỗi cánh hoa là một nét: đặt cọ xuống, kéo nhẹ về phía tâm hoa, nhấc lên. Bốn đến năm nét là xong một bông. Hoa nhiều lớp cánh thì vẽ lớp dưới, hơ đèn, rồi mới vẽ lớp trên để hai lớp không lẫn màu. Nhuỵ hoa chấm sau cùng, thường bằng màu vàng hoặc trắng. Lá vẽ bằng nét mảnh. Cuối cùng phủ top coat để hoa nằm phẳng dưới bề mặt, không bị gờ và không bị cọ mất nét.</p>

<!--anh:1-->
<h2>Cỡ hoa theo độ dài móng</h2>

<table>
<thead><tr><th>Độ dài móng</th><th>Cỡ hoa nên chọn</th><th>Cách bố trí</th></tr></thead>
<tbody>
<tr><td>Rất ngắn, bằng đầu ngón</td><td>Khoảng 2 mm</td><td>Một hai bông ở một góc móng, chừa phần giữa trống</td></tr>
<tr><td>Ngắn, hơn đầu ngón 1–2 mm</td><td>2–3 mm</td><td>Một chùm ba bông ở góc dưới, hoặc rải thưa hai ba bông</td></tr>
<tr><td>Vừa, hơn đầu ngón 3–4 mm</td><td>3–4 mm</td><td>Chùm hoa chéo từ gốc móng lên, thêm vài nét lá</td></tr>
<tr><td>Dài, hơn 5 mm</td><td>4–5 mm</td><td>Dải hoa chạy dọc thân móng, hoặc viền hoa ở đầu móng</td></tr>
</tbody>
</table>

<p>Nguyên tắc chung: hoa không nên rộng quá một phần ba bề ngang móng. Hoa lớn trên móng ngắn làm mặt móng trông chật và mất hết phần nền. Nếu móng ngắn mà bạn vẫn muốn mẫu rõ nét, cách gọn là vẽ hoa nhỏ trên hai ngón nhấn và để tám ngón còn lại trơn. Các gợi ý khác cho móng ngắn có trong bài <a href="/blog/nail-mong-ngan-kieu-han/">nail móng ngắn kiểu Hàn</a>.</p>

<h2>Phối nền cho hoa nổi</h2>

<p>Nền quyết định hoa có thấy được hay không. Nền đục sữa như trắng sữa, hồng sữa, be nhạt là nền dễ nhất, vì hoa màu nào cũng tách khỏi nền. Nền thạch trong cho cảm giác hoa trôi trong nước, nhưng cần hoa màu đậm hơn mới rõ. Nền tối như xanh rêu, nâu đậm thì hoa nên là trắng, vàng nhạt hoặc hồng nhạt. Nền nhũ dày là nền khó nhất: hạt nhũ bắt sáng làm nét hoa mờ đi, nên nếu muốn có ánh thì để nhũ ở ngón khác. Mix từ hai màu nền tính thêm 10.000₫ mỗi màu. Tông pastel hợp với hoa nhí nhất, xem bài <a href="/blog/nail-pastel-kieu-han/">nail pastel kiểu Hàn</a>.</p>

<!--anh:2-->
<h2>Vẽ tay khác sticker ở đâu</h2>

<p>Vẽ tay chỉnh được cỡ hoa theo đúng móng của bạn, chọn được màu khớp với nền, và nét nằm phẳng dưới lớp top. Hai bàn tay sẽ không giống nhau tuyệt đối, đó là nét riêng của hàng vẽ. Sticker in sẵn thì sắc nét hơn ở chi tiết rất nhỏ, nhanh hơn và rẻ hơn, từ 5.000₫ mỗi chi tiết, nhưng mẫu cố định. So sánh đầy đủ có trong bài <a href="/blog/ve-nail-tay-hay-sticker/">vẽ nail tay hay dán sticker</a>.</p>

<h2>Giá và cách đặt</h2>

<p>Bộ nền gồm cắt da, chỉnh form, dưỡng viền tay 60.000₫ và sơn gel trơn 130.000₫, tức 190.000₫. Thêm bốn bông hoa nhí ở bốn ngón, mỗi bông 10.000₫: 190.000 + 4 × 10.000 = 230.000₫. Hoa nhiều lớp cánh hoặc chùm hoa kín một ngón tính cao hơn mức khởi điểm, kỹ thuật viên sẽ nói giá trước khi vẽ. Khi đặt lịch, mang ảnh mẫu và nói rõ bạn muốn hoa ở mấy ngón.</p>'''
faq=[('Vẽ hoa nhí trên móng giá bao nhiêu?','Từ 10.000₫ mỗi chi tiết, cộng vào bộ nền. Ví dụ cắt da tay 60.000₫ cộng gel trơn 130.000₫ cộng bốn bông 10.000₫ là 230.000₫.'),
 ('Móng ngắn vẽ hoa nhí được không?','Được, với hoa cỡ khoảng 2 mm đặt ở một góc móng và chừa phần giữa trống. Hoa không nên rộng quá một phần ba bề ngang móng.'),
 ('Nền màu nào làm hoa nổi nhất?','Nền đục sữa như trắng sữa, hồng sữa, be nhạt. Nền nhũ dày là nền khó nhất vì hạt nhũ làm nét hoa mờ.'),
 ('Hoa vẽ tay có bền như sticker không?','Cả hai đều bền khi được khoá kỹ bằng top coat. Vẽ tay chỉnh được cỡ và màu theo móng, sticker sắc nét hơn ở chi tiết rất nhỏ.')]
en='''<p>Hand-painted mini florals are small flowers, two to four millimetres across, drawn straight onto the nail with a fine brush and thick coloured gel. At VESSCA painting starts at 10,000₫ per detail, added to the price of the set.</p>
<h2>How they are painted</h2>
<p>The coloured base is cured first. A liner brush with long fine bristles draws each petal in one stroke: touch down, pull towards the centre, lift. Four or five strokes make a flower. Layered petals are cured between layers so the colours stay separate. The centre dot goes last, then a top coat so the flower sits flat under the surface and cannot rub away.</p>
<!--anh:1-->
<h2>Flower size by nail length</h2>
<table>
<thead><tr><th>Nail length</th><th>Flower size</th><th>Layout</th></tr></thead>
<tbody>
<tr><td>Very short</td><td>About 2 mm</td><td>One or two at a corner, centre left clear</td></tr>
<tr><td>Short, 1–2 mm past the tip</td><td>2–3 mm</td><td>A cluster of three low on the nail</td></tr>
<tr><td>Medium, 3–4 mm</td><td>3–4 mm</td><td>A diagonal cluster from the base</td></tr>
<tr><td>Long, over 5 mm</td><td>4–5 mm</td><td>A trail along the nail, or a floral tip</td></tr>
</tbody>
</table>
<p>A flower should not be wider than a third of the nail. On short nails, paint two accent fingers and leave the rest plain.</p>
<h2>Choosing the base</h2>
<p>Milky bases — milky white, milky pink, soft beige — are the easiest, because any flower colour separates from them. A jelly base makes the flowers look suspended in water but needs deeper colours. On dark bases use white or pale yellow. Heavy glitter is the hardest base: the sparkle blurs the lines. Mixing two base colours adds 10,000₫ per colour.</p>
<!--anh:2-->
<h2>Painting versus stickers</h2>
<p>Painting lets us size the flower to your nail and match the base colour, and the two hands will never be perfectly identical — that is the mark of hand work. Stickers are sharper on very fine detail, faster and cheaper, from 5,000₫, but the design is fixed. A set: prep 60,000₫ plus plain gel 130,000₫ is 190,000₫; four flowers at 10,000₫ makes 190,000 + 4 × 10,000 = 230,000₫.</p>'''
ko='''<p>핸드페인팅 미니 플라워는 2–4 mm 크기의 작은 꽃을, 얇은 세필과 된 컬러 젤로 손톱에 직접 그리는 아트입니다. VESSCA에서는 아트가 디테일당 10,000₫부터이며 세트 가격에 더해집니다.</p>
<h2>그리는 방법</h2>
<p>먼저 컬러 베이스를 경화합니다. 결이 길고 가는 라이너 붓으로 꽃잎을 한 번에 한 획씩 그립니다. 붓을 내리고, 중심 쪽으로 당기고, 들어 올립니다. 네다섯 획이면 꽃 하나가 완성됩니다. 겹꽃은 층마다 경화해 색이 섞이지 않게 합니다. 꽃술 점을 마지막에 찍고 탑 코트를 올려 꽃이 표면 아래에 평평하게 눕도록 마감합니다.</p>
<!--anh:1-->
<h2>길이에 맞는 꽃 크기</h2>
<table>
<thead><tr><th>손톱 길이</th><th>꽃 크기</th><th>배치</th></tr></thead>
<tbody>
<tr><td>아주 짧음</td><td>약 2 mm</td><td>한쪽 모서리에 한두 송이, 가운데는 비움</td></tr>
<tr><td>짧음(손끝 1–2 mm)</td><td>2–3 mm</td><td>아래쪽에 세 송이 묶음</td></tr>
<tr><td>보통(3–4 mm)</td><td>3–4 mm</td><td>뿌리에서 대각선으로 올라가는 묶음</td></tr>
<tr><td>긴 편(5 mm 이상)</td><td>4–5 mm</td><td>손톱을 따라 흐르는 줄, 또는 꽃 프렌치</td></tr>
</tbody>
</table>
<p>꽃 하나가 손톱 너비의 3분의 1을 넘지 않는 편이 좋습니다. 짧은 손톱이면 두 손가락만 포인트로 그리고 나머지는 단색으로 두세요.</p>
<h2>베이스 고르기</h2>
<p>밀키 화이트, 밀키 핑크, 연한 베이지 같은 불투명 베이스가 가장 쉽습니다. 어떤 꽃 색이든 또렷하게 떠오릅니다. 시럽 베이스는 꽃이 물에 떠 있는 느낌을 주지만 진한 색이 필요합니다. 어두운 베이스에는 흰색이나 연한 노란색을. 글리터가 많은 베이스는 반짝임이 선을 흐리므로 가장 어렵습니다. 베이스 두 색 믹스는 색당 10,000₫ 추가입니다.</p>
<!--anh:2-->
<h2>페인팅과 스티커</h2>
<p>페인팅은 손톱 크기에 맞춰 꽃을 조절하고 베이스 색과 맞출 수 있습니다. 양손이 완전히 같지 않은 점이 손작업의 특징입니다. 스티커는 아주 미세한 디테일이 더 선명하고 빠르며 5,000₫부터로 저렴하지만 도안이 고정입니다. 예시: 손 정리 60,000₫ + 단색 젤 130,000₫ = 190,000₫, 꽃 네 송이 10,000₫씩이면 190,000 + 4 × 10,000 = 230,000₫입니다.</p>'''
zh='''<p>手绘小花是 2–4 mm 的小朵花型,美甲师用细笔和稠质彩胶直接画在甲面上。在 VESSCA,彩绘每个细节 10,000₫ 起,另加在整套价格之上。</p>
<h2>怎么画出来</h2>
<p>先把底色照灯固化。用笔毛细长的拉线笔一笔一瓣:落笔、向花心拉、提笔。四到五笔完成一朵花。重瓣花要分层画、分层照灯,颜色才不会混。花心最后点上,再上封层,让花朵平贴在表面之下,不会被磨掉。</p>
<!--anh:1-->
<h2>按甲长选花的大小</h2>
<table>
<thead><tr><th>甲长</th><th>花朵大小</th><th>布局</th></tr></thead>
<tbody>
<tr><td>很短</td><td>约 2 mm</td><td>一角放一两朵,中间留空</td></tr>
<tr><td>短(超出指尖 1–2 mm)</td><td>2–3 mm</td><td>甲面下方一簇三朵</td></tr>
<tr><td>中等(3–4 mm)</td><td>3–4 mm</td><td>自甲根斜向上的一簇</td></tr>
<tr><td>较长(5 mm 以上)</td><td>4–5 mm</td><td>沿甲面的一条花带,或花朵法式</td></tr>
</tbody>
</table>
<p>一朵花不要超过甲面宽度的三分之一。甲短时,只在两个指甲上点缀,其余留纯色。</p>
<h2>底色怎么配</h2>
<p>奶白、奶粉、浅米等不透明底最省事,任何花色都跳得出来。果冻底会让花像浮在水中,但需要更深的花色。深色底上适合白色或浅黄。亮粉厚的底最难,闪光会把线条糊掉。底色混两色,每色加 10,000₫。</p>
<!--anh:2-->
<h2>手绘和贴纸的差别</h2>
<p>手绘能按您的甲面调整花的大小,并与底色相配;两只手不会完全一样,这正是手工的痕迹。贴纸在极细节处更清晰、更快也更便宜,5,000₫ 起,但图案固定。示例:手部护理 60,000₫ + 纯色胶 130,000₫ = 190,000₫,再画四朵每朵 10,000₫,即 190,000 + 4 × 10,000 = 230,000₫。</p>'''
bai('nail-hoa-nhi-ve-tay','2026-11-30T08:30:00+07:00','Xu hướng & Cảm hứng',
 A(('floral nails manicure','Hoa nhí vẽ tay trên nền sữa đục','Hand-painted mini florals on a milky base','밀키 베이스의 핸드페인팅 작은 꽃','奶油底色上的手绘小花'),
   [('nail art brush nails','Cọ liner vẽ cánh hoa trên móng','A liner brush painting a petal','라이너 붓으로 꽃잎 그리기','用拉线笔绘制花瓣'),
    ('pastel nails manicure','Hoa nhí trên nền pastel','Mini florals on a pastel base','파스텔 베이스의 작은 꽃','粉彩底色上的小花')]),
 ('Nail hoa nhí vẽ tay: kỹ thuật, cỡ hoa theo độ dài móng và cách phối nền',
  'Cách kỹ thuật viên vẽ hoa nhí bằng cọ liner, chọn cỡ hoa theo độ dài móng, nền nào làm hoa nổi nhất và hoa vẽ tay khác sticker ở đâu.',
  'Nail hoa nhí vẽ tay: cỡ hoa và cách phối nền | VESSCA',
  'Hoa nhí vẽ tay từ 10.000₫ mỗi bông. Nền gel 190.000₫ cộng bốn bông là 230.000₫. Cỡ hoa theo độ dài móng. VESSCA Bình Thạnh.',
  ['nail hoa nhí','vẽ hoa nhí trên móng','nail hoa vẽ tay','nail hoa nhỏ móng ngắn','nail vẽ hoa giá bao nhiêu'],vi,faq),
 ('Hand-Painted Mini Floral Nails: Technique, Size and Base Colours',
  'How each petal is drawn, which flower size suits your nail length, which bases make florals stand out, and how painting differs from stickers.',
  'Hand-Painted Floral Nails | VESSCA Saigon',
  'Hand-painted mini florals from 10,000₫ per flower. Gel base 190,000₫ plus four flowers is 230,000₫. VESSCA, Binh Thanh.',
  ['hand painted floral nails','mini floral nail art','nail salon Binh Thanh','Korean nails Saigon','nail art Ho Chi Minh City'],en,
  [('How much is hand-painted floral art?','From 10,000₫ per flower, added to the set. Prep 60,000₫ plus plain gel 130,000₫ plus four flowers is 230,000₫.'),
   ('Do florals work on short nails?','Yes, at about 2 mm placed at one corner. A flower should not be wider than a third of the nail.'),
   ('Which base shows florals best?','Milky bases — milky white, milky pink, soft beige. Heavy glitter blurs the painted lines.')]),
 ('핸드페인팅 작은 꽃 네일: 기법, 크기, 베이스',
  '꽃잎을 그리는 방법, 손톱 길이에 맞는 꽃 크기, 꽃이 돋보이는 베이스, 스티커와의 차이.',
  '핸드페인팅 플라워 네일 | 호치민 VESSCA',
  '핸드페인팅 작은 꽃은 송이당 10,000₫부터. 젤 베이스 190,000₫ + 네 송이면 230,000₫. 호치민 빈탄 VESSCA.',
  ['플라워 네일','핸드페인팅 네일','호치민 네일샵','빈탄 네일','네일 아트 호치민'],ko,
  [('꽃 아트 가격은 얼마인가요?','송이당 10,000₫부터이며 세트에 더해집니다. 손 정리 60,000₫ + 단색 젤 130,000₫ + 네 송이면 230,000₫입니다.'),
   ('짧은 손톱도 가능한가요?','가능합니다. 약 2 mm 크기로 한쪽 모서리에 배치하세요. 손톱 너비의 3분의 1을 넘지 않게 합니다.'),
   ('어떤 베이스가 좋나요?','밀키 화이트, 밀키 핑크, 연한 베이지입니다. 글리터가 많은 베이스는 선이 흐려집니다.')]),
 ('手绘小花美甲:画法、大小与底色',
  '花瓣的画法、按甲长选择花朵大小、哪种底色最显花,以及手绘与贴纸的差别。',
  '手绘小花美甲 | 胡志明 VESSCA',
  '手绘小花每朵 10,000₫ 起。胶底色 190,000₫ 加四朵即 230,000₫。胡志明平盛郡 VESSCA。',
  ['手绘 美甲','小花 美甲','胡志明 美甲','平盛郡 美甲店','美甲彩绘 胡志明'],zh,
  [('手绘小花多少钱?','每朵 10,000₫ 起,另加在整套之上。手部护理 60,000₫ + 纯色胶 130,000₫ + 四朵即 230,000₫。'),
   ('短甲能画吗?','可以,约 2 mm 放在一角。一朵花不要超过甲面宽度的三分之一。'),
   ('哪种底色最显花?','奶白、奶粉、浅米等不透明底;亮粉厚的底会让线条变糊。')]))

# ---------- 2/12 — Chăm móng mùa khô ----------
vi='''<p>Từ khoảng tháng 12 đến tháng 4, Sài Gòn vào mùa khô: độ ẩm trong không khí giảm, gió nhiều hơn, nắng gắt hơn. Móng và viền da mất nước nhanh hơn trong những tháng này, nên dễ giòn, dễ xước măng rô và mép gel dễ hở. Cách xử lý là tăng tần suất dưỡng, không phải đổi kiểu nail.</p>

<h2>Vì sao mùa khô móng và viền da khô hơn</h2>

<p>Bản móng không phải một khối đặc. Đó là nhiều lớp keratin xếp lên nhau, và giữa các lớp luôn có một lượng nước nhất định. Lượng nước này giữ cho móng dẻo. Khi không khí quanh tay khô, nước trong lớp sừng bay ra ngoài nhanh hơn mức móng bù lại được, móng mất độ dẻo và chuyển sang giòn. Móng giòn thì nứt dọc ở đầu móng, tách lớp ở mép, và sứt khi va nhẹ.</p>

<p>Ba yếu tố nữa cộng vào trong mùa này: máy lạnh và quạt chạy nhiều giờ, nước rửa tay có cồn làm khô lớp dầu tự nhiên, và nắng gắt trên mu bàn tay khi chạy xe. Với người đang để gel, hậu quả thường thấy nhất là mép gel ở gốc móng hở sớm hơn bình thường, vì móng khô co lại trong khi lớp gel không co theo.</p>

<!--anh:1-->
<h2>Lịch dưỡng cho mùa khô</h2>

<table>
<thead><tr><th>Việc</th><th>Tần suất</th><th>Ghi chú</th></tr></thead>
<tbody>
<tr><td>Dầu dưỡng viền móng</td><td>Mỗi tối, thêm một lần giữa ngày</td><td>Xoa cả mặt dưới đầu móng, không chỉ viền trên</td></tr>
<tr><td>Kem tay</td><td>Sau mỗi lần rửa tay, khi da còn hơi ẩm</td><td>Chọn loại có glycerin, bơ hạt mỡ hoặc ceramide</td></tr>
<tr><td>Ủ tay bằng lớp kem dày, đeo găng cotton khi ngủ</td><td>Một đến hai lần mỗi tuần</td><td>Dùng khi da mu tay đã ráp hoặc nứt nhẹ</td></tr>
<tr><td>Cắt dũa lại đầu móng</td><td>Khoảng mười ngày một lần</td><td>Dũa một chiều, bỏ góc nhọn trước khi nó nứt</td></tr>
<tr><td>Kem chống nắng cho mu bàn tay</td><td>Mỗi lần ra đường</td><td>Phần này hay bị bỏ qua, nhất là khi chạy xe máy</td></tr>
<tr><td>Chăm tại tiệm</td><td>Khi da ráp nhiều hoặc trước dịp quan trọng</td><td>Hand Ritual 250.000₫ trong 30 phút, làm sạch và dưỡng ẩm cả bàn tay</td></tr>
</tbody>
</table>

<p>Lịch chăm chi tiết giữa hai lần làm nail có trong bài <a href="/blog/lich-duong-mong-giua-hai-lan-lam-nail/">lịch dưỡng móng bốn tuần</a>. Cách chọn và dùng dầu dưỡng ở bài <a href="/blog/dau-duong-vien-mong-cuticle-oil/">dầu dưỡng viền móng</a>.</p>

<h2>Những sai lầm thường gặp</h2>

<p>Sai lầm phổ biến nhất là bôi dầu dưỡng lên mặt móng đã sơn gel và nghĩ như vậy là dưỡng được móng thật. Dầu không đi qua lớp gel. Phần cần bôi là viền da quanh móng và mặt dưới đầu móng, vì dầu thấm vào da rồi mới tới phần móng đang mọc.</p>

<p>Sai lầm thứ hai là dùng nước tẩy sơn liên tục để đổi màu. Acetone lấy nước và dầu khỏi móng, nên trong mùa khô càng làm móng giòn nhanh hơn. Thứ ba là rửa tay bằng nước nóng. Thứ tư là dũa mặt móng cho hết sọc; việc này làm bản móng mỏng đi và phải chờ móng mọc mới hồi. Thứ năm là bóc mép gel đã hở, vì lớp móng trên cùng sẽ đi theo. Mép hở nên quay lại tiệm xử lý, VESSCA bảo hành năm ngày.</p>

<p>Bài viết chỉ mang tính tham khảo. Nếu da quanh móng nứt chảy máu, sưng đỏ hoặc đau kéo dài dù đã dưỡng ẩm đều, nên gặp bác sĩ. Các trường hợp da tay khô nứt được nói kỹ hơn ở bài <a href="/blog/da-tay-kho-nut-ne/">da tay khô, nứt nẻ</a>.</p>

<!--anh:2-->
<h2>Mùa khô nên làm kiểu nail nào</h2>

<p>Mùa khô ít rủi ro hơn mùa mưa, nên bạn không cần bỏ kiểu nào. Chỉ có ba điều chỉnh đáng làm. Giữ độ dài ngắn vừa, vì móng giòn thì móng dài gãy ngang dễ hơn. Nói trước với kỹ thuật viên là móng đang khô, để tiệm dũa bề mặt ít nhất có thể. Và nếu bộ gel cũ còn chắc, chọn fill gel 190.000₫ một bộ thay vì tháo rồi làm mới liên tục, vì mỗi lần tháo là thêm một lần dũa lớp top.</p>

<p>Với móng thật mỏng và dễ gãy trong mùa này, một lớp gel builder mỏng làm nền giúp móng chịu lực tốt hơn. Cắt da, chỉnh form và dưỡng viền tay 60.000₫, cộng sơn gel trơn 130.000₫ là 190.000₫ cho một bộ cơ bản.</p>'''
faq=[('Vì sao mùa khô móng dễ giòn hơn?','Vì không khí ít ẩm làm nước giữa các lớp keratin của móng bay ra nhanh hơn mức móng bù lại được. Mất nước thì móng mất độ dẻo và nứt, tách lớp.'),
 ('Mùa khô nên bôi dầu dưỡng bao nhiêu lần một ngày?','Mỗi tối một lần, thêm một lần giữa ngày nếu ngồi máy lạnh nhiều hoặc rửa tay nhiều.'),
 ('Bôi dầu dưỡng lên lớp gel có tác dụng không?','Không. Dầu không đi qua lớp gel. Nên bôi vào viền da quanh móng và mặt dưới đầu móng.'),
 ('Mùa khô mép gel hở sớm hơn, xử lý thế nào?','Không bóc, vì lớp móng trên cùng sẽ bong theo. Quay lại tiệm để xử lý; VESSCA bảo hành năm ngày.')]
en='''<p>From December to April Saigon is in its dry season: lower humidity, more wind, stronger sun. Nails and the skin around them lose water faster in these months, so they turn brittle, hangnails appear and gel edges lift sooner. The fix is more frequent care, not a different style of manicure.</p>
<h2>Why dry air matters</h2>
<p>The nail plate is layers of keratin with water held between them, and that water is what keeps the nail flexible. When the air is dry, water leaves faster than the nail replaces it, so the plate turns brittle and splits at the tip. Air conditioning, alcohol hand gel and sun on the backs of the hands all add to it. For anyone wearing gel, the usual sign is the edge at the base lifting earlier than normal.</p>
<!--anh:1-->
<h2>Dry-season routine</h2>
<table>
<thead><tr><th>What</th><th>How often</th></tr></thead>
<tbody>
<tr><td>Cuticle oil, including under the free edge</td><td>Every evening, plus once midday</td></tr>
<tr><td>Hand cream on slightly damp skin</td><td>After every hand wash</td></tr>
<tr><td>Thick cream plus cotton gloves overnight</td><td>Once or twice a week</td></tr>
<tr><td>Trim and file the tip, one direction only</td><td>About every ten days</td></tr>
<tr><td>Sunscreen on the backs of the hands</td><td>Every time you go out</td></tr>
<tr><td>Hand Ritual, 250,000₫ for 30 minutes</td><td>When skin is rough or before an event</td></tr>
</tbody>
</table>
<h2>Common mistakes</h2>
<p>Oiling over gel does nothing for the natural nail — oil does not pass through gel, so apply it to the surrounding skin and under the tip. Frequent acetone removal, hot water, filing the surface smooth and peeling a lifted edge all make the dry season worse. Bring a lifted edge back to us instead; VESSCA guarantees sets for five days. This is general information: see a doctor for skin that cracks, bleeds or stays painful.</p>
<!--anh:2-->
<h2>What to wear this season</h2>
<p>Keep length short to medium, tell the technician the nails are dry so surface filing stays minimal, and choose a fill at 190,000₫ per set while the old gel is sound rather than removing and rebuilding each time. A basic set is 60,000₫ prep plus 130,000₫ plain gel, so 190,000₫.</p>'''
ko='''<p>12월부터 4월까지 사이공은 건기입니다. 습도가 낮고 바람이 많고 햇빛이 강합니다. 이 기간에 손톱과 주변 피부는 수분을 더 빨리 잃어 쉽게 부러지고 거스러미가 생기며 젤 들뜸도 빨라집니다. 해결책은 스타일 변경이 아니라 관리 횟수를 늘리는 것입니다.</p>
<h2>건조한 공기가 문제인 이유</h2>
<p>손톱판은 케라틴 층 사이에 수분을 품고 있고, 그 수분이 유연성을 만듭니다. 공기가 건조하면 손톱이 보충하는 속도보다 수분이 빠져나가는 속도가 빨라져 끝이 갈라지고 층이 뜹니다. 에어컨, 알코올 손 소독제, 손등에 닿는 햇빛도 더해집니다. 젤을 하고 계시면 뿌리 쪽 들뜸이 평소보다 이르게 나타납니다.</p>
<!--anh:1-->
<h2>건기 관리 루틴</h2>
<table>
<thead><tr><th>항목</th><th>주기</th></tr></thead>
<tbody>
<tr><td>큐티클 오일, 손톱 끝 아래까지</td><td>매일 저녁, 낮에 한 번 더</td></tr>
<tr><td>살짝 젖은 손에 핸드크림</td><td>손 씻을 때마다</td></tr>
<tr><td>된 크림 + 면장갑 수면팩</td><td>주 1–2회</td></tr>
<tr><td>끝 정리, 한 방향 파일링</td><td>열흘에 한 번쯤</td></tr>
<tr><td>손등 자외선 차단</td><td>외출할 때마다</td></tr>
<tr><td>핸드 리추얼 250,000₫(30분)</td><td>피부가 거칠 때, 행사 전</td></tr>
</tbody>
</table>
<h2>흔한 실수</h2>
<p>젤 위에 오일을 바르는 것은 자연 손톱에 도움이 되지 않습니다. 오일은 젤을 통과하지 않으므로 주변 피부와 손톱 끝 아래에 바르세요. 잦은 아세톤 제거, 뜨거운 물, 표면 파일링, 들뜬 부분 뜯기는 건기에 특히 해롭습니다. 들뜸은 직접 뜯지 말고 샵으로 오세요. VESSCA는 5일 보증을 드립니다. 이 글은 참고용이며, 피부가 갈라져 피가 나거나 통증이 계속되면 진료를 받으시기 바랍니다.</p>
<!--anh:2-->
<h2>이 시기에 맞는 시술</h2>
<p>길이는 짧거나 중간으로, 손톱이 건조하다고 미리 알려 주셔서 표면 파일링을 줄이시고, 기존 젤이 단단하면 매번 제거하지 말고 필(190,000₫, 한 세트)을 선택하세요. 기본 세트는 정리 60,000₫ + 단색 젤 130,000₫로 190,000₫입니다.</p>'''
zh='''<p>12 月到 4 月是西贡的干季:空气湿度下降、风更多、日照更强。这几个月里,指甲和甲周皮肤失水更快,于是变脆、起倒刺,胶的边缘也更早翘起。应对办法是提高养护频率,而不是换一种美甲。</p>
<h2>干燥空气为什么要紧</h2>
<p>甲板是一层层角蛋白,层间含有水分,而这些水分决定了指甲的韧性。空气干燥时,水分流失快于指甲补充的速度,甲面失去韧性,甲尖出现纵向裂口、边缘分层。空调、含酒精的免洗洗手液、照在手背上的阳光都会叠加。做了甲油胶的人,最常见的信号是甲根处比平时更早翘边。</p>
<!--anh:1-->
<h2>干季养护节奏</h2>
<table>
<thead><tr><th>项目</th><th>频率</th></tr></thead>
<tbody>
<tr><td>护甲油,连甲尖下方一起涂</td><td>每晚一次,白天再补一次</td></tr>
<tr><td>皮肤微湿时涂护手霜</td><td>每次洗手后</td></tr>
<tr><td>厚涂护手霜加棉手套过夜</td><td>每周一到两次</td></tr>
<tr><td>修剪与单向打磨甲尖</td><td>约每十天一次</td></tr>
<tr><td>手背防晒</td><td>每次外出</td></tr>
<tr><td>手部仪式 250,000₫(30 分钟)</td><td>皮肤粗糙时或重要场合前</td></tr>
</tbody>
</table>
<h2>常见误区</h2>
<p>在胶面上涂护甲油对真甲没有帮助,油不会穿过胶层,应该涂在甲周皮肤和甲尖下方。频繁用洗甲水、热水洗手、把甲面磨平、硬撕翘起的边缘,在干季都会让情况更糟。翘边请回店处理,VESSCA 提供五天保固。本文仅供参考;若皮肤开裂出血或持续疼痛,建议您就医。</p>
<!--anh:2-->
<h2>这个季节适合做什么</h2>
<p>长度保持短到中等;提前说明指甲偏干,我们会尽量少磨甲面;旧胶仍牢固时选择填补(190,000₫ 一套),不必每次卸掉重做。基础一套为前期护理 60,000₫ 加纯色胶 130,000₫,共 190,000₫。</p>'''
bai('cham-soc-mong-mua-kho','2026-12-02T08:30:00+07:00','Chăm sóc móng',
 A(('cuticle oil manicure','Bôi dầu dưỡng vào viền móng buổi tối','Applying cuticle oil in the evening','저녁에 큐티클 오일 바르기','晚间涂抹护甲油'),
   [('dry hands nails','Da quanh móng khô trong mùa khô','Dry skin around the nails','건기의 건조한 손톱 주변','干季里干燥的甲周皮肤'),
    ('hand cream manicure','Thoa kem tay sau khi rửa tay','Hand cream after washing','손 씻은 뒤 핸드크림','洗手后涂护手霜')]),
 ('Chăm móng mùa khô Sài Gòn: vì sao móng giòn hơn và dưỡng thế nào',
  'Tháng 12 đến tháng 4 không khí khô làm móng mất nước, giòn và hở mép gel sớm. Lịch dưỡng theo tần suất, năm sai lầm thường gặp và ba điều chỉnh khi làm nail.',
  'Chăm móng mùa khô Sài Gòn (tháng 12–4) | VESSCA',
  'Mùa khô móng mất nước nên giòn, mép gel hở sớm. Lịch dưỡng, sai lầm cần tránh, fill gel 190.000₫ thay vì tháo liên tục. VESSCA Bình Thạnh.',
  ['chăm móng mùa khô','móng giòn dễ gãy','móng khô nứt','dưỡng móng mùa khô Sài Gòn','mép gel hở sớm'],vi,faq),
 ('Dry-Season Nail Care in Saigon: Why Nails Turn Brittle',
  'What low humidity does to the nail plate from December to April, a care routine by frequency, the common mistakes and three adjustments at the salon.',
  'Dry-Season Nail Care | VESSCA Saigon',
  'Dry air makes nails brittle and gel edges lift early. Care routine, mistakes to avoid, fill 190,000₫ instead of repeat removal. VESSCA, Binh Thanh.',
  ['dry season nail care','brittle nails','nail salon Binh Thanh','Korean nails Saigon','cuticle oil routine'],en,
  [('Why are nails more brittle in the dry season?','Dry air pulls water from between the keratin layers faster than the nail replaces it, so the plate loses flexibility and splits.'),
   ('How often should I use cuticle oil?','Every evening, plus once midday if you sit in air conditioning or wash your hands often.'),
   ('Does oil work over gel?','No. Oil does not pass through gel; apply it to the surrounding skin and under the free edge.')]),
 ('건기 손톱 관리: 손톱이 잘 부러지는 이유',
  '12월–4월 낮은 습도가 손톱판에 미치는 영향, 주기별 관리 루틴, 흔한 실수와 샵에서의 세 가지 조정.',
  '건기 손톱 관리 | 호치민 VESSCA',
  '건조한 공기는 손톱을 부러지게 하고 젤 들뜸을 앞당깁니다. 관리 루틴과 필 190,000₫ 안내. 호치민 빈탄 VESSCA.',
  ['건기 손톱 관리','손톱 부러짐','호치민 네일샵','빈탄 네일','큐티클 오일'],ko,
  [('건기에 손톱이 왜 잘 부러지나요?','건조한 공기가 케라틴 층 사이 수분을 보충 속도보다 빨리 빼앗아 유연성이 떨어집니다.'),
   ('큐티클 오일은 얼마나 자주 바르나요?','매일 저녁 한 번, 에어컨이나 손 씻기가 잦으면 낮에 한 번 더 바르세요.'),
   ('젤 위에 오일을 발라도 되나요?','오일은 젤을 통과하지 않습니다. 주변 피부와 손톱 끝 아래에 바르세요.')]),
 ('西贡干季护甲:指甲为什么变脆',
  '12 月到 4 月的低湿度如何影响甲板、按频率安排的养护节奏、常见误区,以及到店时的三点调整。',
  '干季护甲指南 | 胡志明 VESSCA',
  '干燥空气让指甲变脆、胶边更早翘起。养护节奏与填补 190,000₫ 建议。胡志明平盛郡 VESSCA。',
  ['干季 护甲','指甲 变脆','胡志明 美甲','平盛郡 美甲店','护甲油'],zh,
  [('干季指甲为什么更脆?','干燥空气让层间水分流失快于补充速度,甲板失去韧性因而开裂。'),
   ('护甲油要多久涂一次?','每晚一次;常待空调房或频繁洗手就白天再补一次。'),
   ('在胶面上涂油有用吗?','没有用,油不会穿过胶层;请涂在甲周皮肤和甲尖下方。')]))

# ---------- 4/12 — Nail Noel nhẹ nhàng đi làm được ----------
vi='''<p>Nail Noel đi làm được là bộ móng có không khí mùa lễ nhưng vẫn phẳng, ngắn và kín đáo: một tông trầm phủ kín mười ngón, chi tiết nhỏ chỉ ở một hoặc hai ngón, và không kim tuyến kín mặt móng. Bài này nói rõ ba tông màu nên chọn, đặt chi tiết ở đâu, vì sao nên tránh nhũ kín mặt, và cách mô tả yêu cầu đó khi đặt lịch. Nếu bạn muốn xem các hướng mẫu Noel nói chung, đọc bài <a href="/blog/nail-noel-2026/">nail Noel 2026</a>.</p>

<h2>"Đi làm được" nghĩa là gì</h2>

<p>Đây là bốn tiêu chí cụ thể. Thứ nhất, bề mặt phẳng: không chi tiết nổi, không đá to, để gõ phím không lộc cộc và không vướng tay áo. Thứ hai, độ dài ngắn vừa, hơn đầu ngón một đến ba milimét. Thứ ba, màu nhìn nghiêm khi bàn tay xuất hiện trong họp hoặc ảnh chụp. Thứ tư, phần lấp lánh giới hạn ở một ngón hoặc một đường mảnh. Các hướng nail dùng được trong môi trường công sở có thêm ở bài <a href="/blog/nail-van-phong-kieu-han/">nail văn phòng kiểu Hàn</a>.</p>

<!--anh:1-->
<h2>Ba tông màu nên chọn</h2>

<table>
<thead><tr><th>Tông</th><th>Mô tả</th><th>Chi tiết nên thêm</th></tr></thead>
<tbody>
<tr><td>Đỏ trầm</td><td>Đỏ rượu vang hoặc đỏ cherry trầm, đục không trong. Đậm nhưng không rực, nên lên tay vẫn nghiêm</td><td>Để trơn mười ngón, hoặc một đường French mảnh cùng màu đậm hơn</td></tr>
<tr><td>Xanh rêu</td><td>Xanh lá đậm ngả xám hoặc ngả nâu. Ít người chọn nên trông mới, và rất ăn dưới đèn vàng</td><td>Một chỉ nhũ vàng mảnh dọc ở ngón áp út</td></tr>
<tr><td>Trắng sữa</td><td>Trắng đục nhẹ, không phải trắng phấn. Gợi tuyết mà vẫn sạch và trung tính nhất</td><td>Một bông hoa nhí trắng hoặc một viên đá nhỏ ở gốc móng</td></tr>
<tr><td>Nude ánh nhẹ</td><td>Phương án an toàn nhất khi môi trường làm việc yêu cầu kín đáo</td><td>Viền nhũ rất mảnh ở đầu móng, một hoặc hai ngón</td></tr>
</tbody>
</table>

<p>Ba tông đầu đều là màu đục. Màu đục che được phần mặt móng không hoàn toàn phẳng và giữ nét gọn hơn màu trong trong suốt hai ba tuần. Nếu bạn muốn hướng đỏ, các sắc đỏ cụ thể có trong bài <a href="/blog/nail-mau-do-kieu-han/">nail màu đỏ kiểu Hàn</a>.</p>

<h2>Chi tiết nhỏ đặt ở đâu</h2>

<p>Nguyên tắc là một loại chi tiết, trên một đến hai ngón, ở vị trí ít va chạm. Ngón áp út và ngón giữa là tốt nhất, vì hai ngón này ít dùng để gõ phím và ít cọ vào bàn. Ngón trỏ nên để trơn.</p>

<p>Bốn dạng sau đều phẳng nên dùng được hằng ngày: một đường French mảnh ở đầu móng bằng màu đậm hơn nền; một chỉ nhũ mảnh kẻ dọc theo thân móng; một bông hoa nhí trắng cỡ hai milimét ở gốc móng; một viên đá nhỏ đặt sát gốc móng. Đá thường 10.000₫ một viên, Swarovski 20.000₫ một viên. Phần vẽ và kẻ nhũ tính từ 10.000₫, French tính từ 15.000₫.</p>

<!--anh:2-->
<h2>Vì sao tránh kim tuyến kín mặt móng</h2>

<p>Có ba lý do thực tế. Lớp kim tuyến dày làm bề mặt hơi gồ, nên tay cộm khi gõ phím và dễ mắc vào vải. Hạt kim tuyến bắt sáng mạnh dưới đèn trần văn phòng, nên bộ nail trông rực hơn nhiều so với lúc thử ở tiệm. Và khi móng mọc ra, phần chân móng lộ rõ hơn hẳn so với màu trơn, nên bộ nail xuống nhanh hơn dù gel vẫn còn chắc.</p>

<p>Nếu bạn vẫn muốn độ lấp lánh, hai cách gọn hơn là để kim tuyến ở một ngón duy nhất, hoặc chọn hiệu ứng ánh mịn thay cho hạt to. Xà cừ ánh trai và nhũ AURORA QUEEN tại tiệm 280.000₫, cho ánh chuyển màu nhẹ khi xoay tay thay vì lấp lánh thành hạt.</p>

<h2>Giá và thời điểm nên làm</h2>

<p>Một bộ cơ bản gồm cắt da, chỉnh form, dưỡng viền tay 60.000₫ và sơn gel trơn 130.000₫, tức 190.000₫. Thêm một đường French mảnh 15.000₫: 190.000 + 15.000 = 205.000₫. Nếu nền mix hai màu thì cộng 10.000₫ mỗi màu.</p>

<p>Một bộ gel giữ hai đến ba tuần, nên làm trong khoảng mùng 8 đến 20 tháng 12 là vừa đẹp qua Giáng sinh và còn dùng tới gần Tết dương lịch. Những ngày sát 24 và 25 tháng 12 thường đông hơn, nên đặt lịch trước qua form trên web, gọi điện hoặc Instagram và Facebook. VESSCA bảo hành năm ngày.</p>'''
faq=[('Nail Noel nào đi làm được?','Một tông trầm phủ kín mười ngón như đỏ rượu, xanh rêu hoặc trắng sữa, bề mặt phẳng, dài hơn đầu ngón một đến ba milimét, chi tiết nhỏ chỉ ở một hai ngón.'),
 ('Vì sao không nên để kim tuyến kín mặt móng khi đi làm?','Lớp kim tuyến dày làm bề mặt gồ nhẹ, bắt sáng mạnh dưới đèn trần, và khi móng mọc ra thì phần chân móng lộ rõ hơn màu trơn.'),
 ('Nail Noel đi làm giá bao nhiêu?','Cắt da chỉnh form dưỡng viền tay 60.000₫ cộng sơn gel trơn 130.000₫ là 190.000₫. Thêm một đường French mảnh 15.000₫ thì tổng 205.000₫.'),
 ('Nên làm nail Noel vào lúc nào?','Khoảng mùng 8 đến 20 tháng 12, vì một bộ gel giữ hai đến ba tuần nên vừa đẹp qua Giáng sinh và còn dùng tới gần Tết dương lịch.')]
en='''<p>An office-friendly Christmas manicure is flat, short and quiet: one deep shade across all ten nails, a small detail on one or two fingers, and no glitter covering the whole nail. Our general Christmas designs are in a separate article.</p>
<h2>What "office-friendly" means here</h2>
<p>Four concrete things. A flat surface, so typing is comfortable and nothing catches on sleeves. Length one to three millimetres past the fingertip. A colour that still reads as serious when your hands appear in a meeting. And sparkle limited to one nail or one thin line.</p>
<!--anh:1-->
<h2>Three shades</h2>
<table>
<thead><tr><th>Shade</th><th>Why it works</th><th>Detail to add</th></tr></thead>
<tbody>
<tr><td>Deep red</td><td>Wine or muted cherry, opaque not sheer: rich without being bright</td><td>Plain on all ten, or a thin French line in a darker red</td></tr>
<tr><td>Moss green</td><td>Deep green with grey or brown in it; uncommon, and good under warm light</td><td>One thin gold shimmer line on the ring finger</td></tr>
<tr><td>Milky white</td><td>Soft opaque white, not chalky; the most neutral way to suggest snow</td><td>A 2 mm white flower or one small stone at the base</td></tr>
<tr><td>Soft shimmer nude</td><td>The safest option in a conservative workplace</td><td>A very thin shimmer line at the tip</td></tr>
</tbody>
</table>
<h2>Where to put the detail</h2>
<p>One kind of detail, on one or two nails, on the ring and middle fingers — they take the least impact. Leave the index finger plain. Flat options: a thin French line, a vertical shimmer line, a tiny painted flower, or one small stone near the base. Stones are 10,000₫ each, Swarovski 20,000₫; line and painted work from 10,000₫, French from 15,000₫.</p>
<!--anh:2-->
<h2>Why not full glitter</h2>
<p>Thick glitter raises the surface slightly, catches office ceiling light far more than it did in the salon, and shows regrowth at the base much more clearly than a plain colour. If you want shine, keep glitter to one nail or choose a fine pearl finish instead — our shell and aurora shimmer sets are 280,000₫.</p>
<h2>Price and timing</h2>
<p>Hand prep 60,000₫ plus plain gel 130,000₫ is 190,000₫; with a thin French line at 15,000₫ the total is 205,000₫. A gel set lasts two to three weeks, so book between 8 and 20 December. The days just before 24–25 December are busier, so book ahead.</p>'''
ko='''<p>출근용 크리스마스 네일은 평평하고 짧고 조용합니다. 열 손가락에 깊은 한 가지 색을 깔고, 작은 디테일은 한두 손가락에만, 글리터로 손톱 전체를 덮지 않습니다. 일반적인 크리스마스 디자인은 별도 글에서 다룹니다.</p>
<h2>'출근 가능'의 기준</h2>
<p>네 가지입니다. 평평한 표면이라 타이핑이 편하고 옷소매에 걸리지 않습니다. 길이는 손끝에서 1–3 mm입니다. 회의에서 손이 보일 때도 단정해 보이는 색입니다. 반짝임은 한 손가락이나 얇은 라인 하나로 제한합니다.</p>
<!--anh:1-->
<h2>세 가지 컬러</h2>
<table>
<thead><tr><th>컬러</th><th>이유</th><th>추천 디테일</th></tr></thead>
<tbody>
<tr><td>딥 레드</td><td>와인이나 가라앉은 체리, 불투명. 깊지만 튀지 않습니다</td><td>열 손가락 단색, 또는 더 진한 레드로 얇은 프렌치</td></tr>
<tr><td>모스 그린</td><td>회색·브라운이 섞인 진한 그린. 흔하지 않고 따뜻한 조명에서 좋습니다</td><td>약지에 얇은 골드 펄 라인 하나</td></tr>
<tr><td>밀키 화이트</td><td>부드러운 불투명 화이트. 눈을 가장 중립적으로 표현합니다</td><td>2 mm 흰 꽃 하나, 또는 뿌리 쪽 작은 스톤</td></tr>
<tr><td>펄 누드</td><td>보수적인 직장에서 가장 안전합니다</td><td>끝에 아주 얇은 펄 라인</td></tr>
</tbody>
</table>
<h2>디테일 위치</h2>
<p>한 종류를 한두 손가락에, 충격이 적은 약지와 중지에 올리세요. 검지는 단색으로 둡니다. 평평한 선택지: 얇은 프렌치 라인, 세로 펄 라인, 작은 꽃 하나, 뿌리 쪽 작은 스톤 하나. 스톤 10,000₫, 스와로브스키 20,000₫, 라인·아트 10,000₫부터, 프렌치 15,000₫부터입니다.</p>
<!--anh:2-->
<h2>글리터를 꽉 채우지 않는 이유</h2>
<p>두꺼운 글리터는 표면이 살짝 올라와 걸리고, 사무실 천장 조명에서 샵에서보다 훨씬 강하게 빛나며, 자라난 뿌리 부분이 단색보다 또렷하게 드러납니다. 반짝임을 원하시면 한 손가락만 글리터로 하거나 고운 펄 질감을 고르세요. 전복펄과 오로라 펄 시술은 280,000₫입니다.</p>
<h2>가격과 시기</h2>
<p>손 정리 60,000₫ + 단색 젤 130,000₫ = 190,000₫, 얇은 프렌치 15,000₫을 더하면 205,000₫입니다. 젤은 2–3주 유지되므로 12월 8–20일 사이가 좋습니다. 24–25일 직전은 붐비니 미리 예약해 주세요.</p>'''
zh='''<p>适合上班的圣诞美甲是平整、短、低调的:十指铺一种深色,细节只放在一两个指甲上,不用亮粉铺满甲面。一般的圣诞款式我们另有一篇专门介绍。</p>
<h2>"能上班"的四个标准</h2>
<p>一是甲面平整,打字舒服,不勾袖口。二是长度超出指尖 1–3 mm。三是颜色在会议中露出双手时依然稳重。四是闪光只留在一个指甲或一条细线上。</p>
<!--anh:1-->
<h2>三个色调</h2>
<table>
<thead><tr><th>色调</th><th>为什么合适</th><th>建议细节</th></tr></thead>
<tbody>
<tr><td>深红</td><td>酒红或沉静的樱桃红,不透色。浓而不艳</td><td>十指纯色,或用更深的红画一道细法式</td></tr>
<tr><td>苔绿</td><td>带灰或带棕的深绿,少见,暖光下很好看</td><td>无名指一道细金色亮线</td></tr>
<tr><td>奶白</td><td>柔和的不透明白,不显粉白;表达雪意最中性</td><td>一朵 2 mm 白花,或甲根一颗小钻</td></tr>
<tr><td>细闪裸色</td><td>在要求保守的职场最稳妥</td><td>甲尖一道极细的珠光线</td></tr>
</tbody>
</table>
<h2>细节放在哪里</h2>
<p>只用一种细节,放在一到两个指甲上,选无名指和中指,它们受到的碰撞最少;食指留纯色。平整的做法有:一道细法式、一条竖向亮线、一朵小花、甲根一颗小钻。普通钻 10,000₫ 一颗,施华洛世奇 20,000₫;线条与彩绘 10,000₫ 起,法式 15,000₫ 起。</p>
<!--anh:2-->
<h2>为什么不铺满亮粉</h2>
<p>厚亮粉会让甲面略微凸起、容易勾住衣物;在办公室顶灯下比在店里亮得多;指甲长出来后,甲根空档也比纯色明显得多。若您想要光泽,可以只在一个指甲上用亮粉,或改用细腻的珠光质感——贝壳光与极光珠光系列为 280,000₫。</p>
<h2>价格与时间</h2>
<p>手部护理 60,000₫ 加纯色胶 130,000₫ 为 190,000₫;再加一道细法式 15,000₫,共 205,000₫。一套甲油胶可保持 2–3 周,因此 12 月 8 日至 20 日之间来做最合适。24–25 日前几天较忙,请提前预约。</p>'''
bai('nail-noel-di-lam-don-gian','2026-12-04T08:30:00+07:00','Xu hướng & Cảm hứng',
 A(('dark red nails','Móng sơn đỏ rượu trầm, bề mặt phẳng','Deep wine red nails with a flat surface','표면이 평평한 딥 와인 레드 네일','平整甲面的深酒红美甲'),
   [('green nails manicure','Nền xanh rêu với một chỉ nhũ mảnh','Moss green with one thin shimmer line','얇은 펄 라인을 더한 모스 그린','带一道细亮线的苔绿底色'),
    ('white nails manicure','Trắng sữa với một chi tiết nhỏ ở gốc móng','Milky white with one small detail at the base','뿌리 쪽 작은 디테일의 밀키 화이트','甲根带一个小细节的奶白色')]),
 ('Nail Noel nhẹ nhàng đi làm được: ba tông màu và chi tiết nhỏ',
  'Tiêu chí để một bộ nail Noel dùng được ở công sở: đỏ trầm, xanh rêu hay trắng sữa phủ kín, bề mặt phẳng, chi tiết nhỏ ở một hai ngón và không kim tuyến kín mặt móng.',
  'Nail Noel đi làm được: tông màu và giá | VESSCA',
  'Nail Noel kín đáo: đỏ trầm, xanh rêu, trắng sữa, bề mặt phẳng, chi tiết một hai ngón. Gel trơn 190.000₫, thêm French 205.000₫. VESSCA Bình Thạnh.',
  ['nail Noel đi làm','nail Noel đơn giản','nail Noel nhẹ nhàng','nail Noel văn phòng','nail Noel không kim tuyến'],vi,faq),
 ('Understated Christmas Nails for the Office',
  'Four concrete criteria, three deep shades, where to place one small detail and why full glitter is a problem at work.',
  'Office Christmas Nails | VESSCA Saigon',
  'Deep red, moss green or milky white, flat surface, one small detail. Gel set 190,000₫, with a thin French 205,000₫. VESSCA, Binh Thanh.',
  ['office Christmas nails','understated holiday nails','nail salon Binh Thanh','Korean nails Saigon','Christmas gel nails'],en,
  [('What makes a Christmas set office-friendly?','One deep shade on all ten nails, a flat surface, 1–3 mm length and a small detail on only one or two fingers.'),
   ('Why avoid full glitter at work?','It raises the surface, catches ceiling light far more than in the salon, and shows regrowth more clearly than plain colour.'),
   ('How much is it?','Hand prep 60,000₫ plus plain gel 130,000₫ is 190,000₫; a thin French line adds 15,000₫ for 205,000₫.')]),
 ('출근용 크리스마스 네일: 차분한 세 가지 컬러',
  '사무실에서 무리 없는 네 가지 기준, 깊은 세 가지 컬러, 작은 디테일의 위치, 글리터를 꽉 채우지 않는 이유.',
  '출근용 크리스마스 네일 | 호치민 VESSCA',
  '딥 레드, 모스 그린, 밀키 화이트에 평평한 표면과 작은 디테일. 젤 190,000₫, 프렌치 추가 205,000₫. 호치민 빈탄 VESSCA.',
  ['출근 네일','크리스마스 네일','호치민 네일샵','빈탄 네일','차분한 겨울 네일'],ko,
  [('어떤 크리스마스 네일이 출근에 맞나요?','열 손가락 단색의 깊은 컬러, 평평한 표면, 1–3 mm 길이, 한두 손가락에만 작은 디테일입니다.'),
   ('글리터를 꽉 채우면 왜 불편한가요?','표면이 올라오고, 사무실 조명에서 훨씬 강하게 빛나며, 자란 뿌리가 단색보다 또렷하게 보입니다.'),
   ('가격은 얼마인가요?','손 정리 60,000₫ + 단색 젤 130,000₫ = 190,000₫, 얇은 프렌치 15,000₫을 더하면 205,000₫입니다.')]),
 ('适合上班的低调圣诞美甲',
  '四个具体标准、三种深色调、一个小细节放在哪里,以及为什么铺满亮粉不适合上班。',
  '上班圣诞美甲 | 胡志明 VESSCA',
  '深红、苔绿或奶白,甲面平整,只做一个小细节。纯色胶一套 190,000₫,加细法式 205,000₫。胡志明平盛郡 VESSCA。',
  ['上班 圣诞美甲','低调 圣诞美甲','胡志明 美甲','平盛郡 美甲店','圣诞 甲油胶'],zh,
  [('什么样的圣诞美甲适合上班?','十指一种深色、甲面平整、长度 1–3 mm,细节只放在一两个指甲上。'),
   ('为什么上班不建议铺满亮粉?','甲面会略微凸起,在办公室顶灯下比店里亮得多,长出来后甲根空档也更明显。'),
   ('价格是多少?','手部护理 60,000₫ 加纯色胶 130,000₫ 为 190,000₫;再加一道细法式 15,000₫,共 205,000₫。')]))
