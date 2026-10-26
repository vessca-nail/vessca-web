"""BÀI MẪU — chép file này, đổi nội dung, chạy: python3 tools/viet-bai/<ten>.py
Đây là bài thật đã viết (son-gel-va-son-thuong-khac-nhau, hẹn 9/11/2026) — CHẠY FILE NÀY SẼ TẠO BÀI ĐÓ."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *

# ---------- P2-1. Sơn gel và sơn thường ----------
vi='''<p>Sơn thường và sơn gel nhìn chai thì giống nhau, nhưng cách khô, độ bền và cách tháo khác hẳn. Hiểu khác biệt này giúp bạn chọn đúng loại cho nhu cầu của mình. Bài này so sánh hai loại một cách ngắn gọn.</p>

<h2>Khác nhau ở cách khô</h2>

<p>Sơn thường khô nhờ dung môi bay hơi trong không khí. Lớp sơn mềm trong vài giờ đầu và dễ móp, in vân vải. Sơn gel chỉ cứng lại khi được hơ dưới đèn UV hoặc LED, nhờ chất khơi mào quang hoá. Ra khỏi đèn là gel đã cứng hoàn toàn. Chi tiết về đèn ở bài <a href="/blog/den-uv-led-lam-nail-co-hai-khong/">đèn UV và đèn LED làm nail</a>.</p>

<!--anh:1-->
<h2>Bảng so sánh</h2>

<table>
<thead><tr><th></th><th>Sơn thường</th><th>Sơn gel</th></tr></thead>
<tbody>
<tr><td>Cách khô</td><td>Bay hơi, cần 1–2 giờ</td><td>Hơ đèn, khô ngay</td></tr>
<tr><td>Độ bền</td><td>Vài ngày đến một tuần, dễ tróc đầu móng</td><td>2–3 tuần</td></tr>
<tr><td>Độ bóng</td><td>Giảm dần sau vài ngày</td><td>Giữ bóng gần như suốt thời gian sơn</td></tr>
<tr><td>Cách tháo</td><td>Lau bằng nước tẩy sơn</td><td>Dũa top, ủ dung dịch, đẩy nhẹ (khoảng 20 phút)</td></tr>
<tr><td>Tự làm ở nhà</td><td>Dễ</td><td>Cần đèn và tay nghề, dễ dính gel lên da</td></tr>
<tr><td>Hiệu ứng</td><td>Hạn chế</td><td>Thạch, mắt mèo, velvet, aurora, tráng gương…</td></tr>
</tbody>
</table>

<h2>Khi nào chọn loại nào</h2>

<ul>
<li><strong>Chọn sơn gel</strong> khi bạn muốn bộ nail giữ đẹp 2–3 tuần, cần hiệu ứng đặc biệt, hoặc làm việc tay nhiều.</li>
<li><strong>Sơn thường hợp</strong> khi bạn muốn đổi màu liên tục vài ngày một lần, tự sơn ở nhà, hoặc đang nghỉ gel.</li>
<li><strong>Không sơn màu:</strong> chỉ chăm sóc móng và sơn cứng móng. Xem bài <a href="/blog/son-cung-mong-la-gi/">sơn cứng móng</a>.</li>
</ul>

<!--anh:2-->
<h2>Sơn gel có hại hơn sơn thường không</h2>

<p>Sơn gel không tự làm hại móng. Móng yếu đi thường do tháo sai cách (bóc, cạy), dũa quá tay hoặc gel chạm vào da. Đọc thêm bài <a href="/blog/son-gel-co-hai-cho-mong-khong/">sơn gel có hại cho móng không</a>.</p>

<p>Tại VESSCA, các dịch vụ màu dùng sơn gel: gel trơn 130.000₫, thạch 150.000₫, mắt mèo và nhũ 170.000₫, sơn Hàn cao cấp từ 220.000₫.</p>'''
faq=[('Sơn gel và sơn thường khác nhau thế nào?','Sơn thường khô do bay hơi và giữ vài ngày; sơn gel cứng dưới đèn và giữ 2–3 tuần.'),
 ('Sơn gel có cần hơ đèn không?','Có. Gel chỉ cứng khi hơ dưới đèn UV hoặc LED.'),
 ('Tháo sơn gel có khó không?','Cần dũa lớp top và ủ dung dịch khoảng 20 phút, không nên bóc.'),
 ('Sơn gel có hại hơn sơn thường không?','Không tự làm hại móng; móng yếu thường do tháo sai cách hoặc dũa quá tay.')]
en='''<p>Regular polish and gel look alike in the bottle but differ in curing, durability and removal.</p>
<h2>How they dry</h2>
<p>Regular polish air-dries as solvents evaporate and stays soft for hours. Gel hardens only under a UV or LED lamp and is fully cured when you leave.</p>
<!--anh:1-->
<h2>Comparison</h2>
<table>
<thead><tr><th></th><th>Regular</th><th>Gel</th></tr></thead>
<tbody>
<tr><td>Drying</td><td>1–2 hours</td><td>Instant under lamp</td></tr>
<tr><td>Wear</td><td>Days to a week</td><td>2–3 weeks</td></tr>
<tr><td>Shine</td><td>Fades</td><td>Stays glossy</td></tr>
<tr><td>Removal</td><td>Polish remover</td><td>File top, soak ~20 min</td></tr>
<tr><td>Finishes</td><td>Limited</td><td>Jelly, cat-eye, velvet, aurora, chrome…</td></tr>
</tbody>
</table>
<h2>Which to choose</h2>
<p>Gel for 2–3 weeks of wear, special finishes or busy hands; regular polish for frequent DIY changes; or no colour with a strengthener.</p>
<!--anh:2-->
<h2>Is gel more damaging?</h2>
<p>Not by itself — damage comes from peeling, over-filing or gel touching skin. VESSCA uses gel for colour services: plain 130,000₫, jelly 150,000₫, cat-eye or shimmer 170,000₫, premium Korean from 220,000₫.</p>'''
ko='''<p>일반 매니큐어와 젤은 병은 비슷해 보이지만 굳는 방식, 지속력, 제거 방법이 다릅니다.</p>
<h2>굳는 방식</h2>
<p>일반 폴리시는 용제가 증발하며 마르고 몇 시간 동안 무릅니다. 젤은 UV·LED 램프에서만 굳고 샵을 나설 때 완전히 경화되어 있습니다.</p>
<!--anh:1-->
<h2>비교</h2>
<table>
<thead><tr><th></th><th>일반</th><th>젤</th></tr></thead>
<tbody>
<tr><td>건조</td><td>1–2시간</td><td>램프로 즉시</td></tr>
<tr><td>지속</td><td>며칠~일주일</td><td>2–3주</td></tr>
<tr><td>광택</td><td>점점 줄어듦</td><td>유지</td></tr>
<tr><td>제거</td><td>리무버</td><td>탑 제거 후 약 20분 불림</td></tr>
<tr><td>질감</td><td>제한적</td><td>시럽, 자석, 벨벳, 오로라, 미러 등</td></tr>
</tbody>
</table>
<h2>선택 기준</h2>
<p>2–3주 유지, 특별한 질감, 손을 많이 쓰면 젤. 자주 바꾸며 셀프로 하려면 일반. 컬러 없이 강화제만도 좋습니다.</p>
<!--anh:2-->
<h2>젤이 더 해로울까요</h2>
<p>젤 자체가 손상시키지 않습니다. 뜯기, 과한 파일링, 피부에 닿은 젤이 원인입니다. VESSCA 컬러 시술은 젤을 씁니다: 단색 130,000₫, 시럽 150,000₫, 자석·펄 170,000₫, 한국 프리미엄 220,000₫부터.</p>'''
zh='''<p>普通指甲油和甲油胶瓶子看起来差不多,但干燥方式、持久度和卸除方法完全不同。</p>
<h2>干燥方式</h2>
<p>普通指甲油靠溶剂挥发风干,几小时内都较软。甲油胶只在 UV 或 LED 灯下固化,离开灯时已完全变硬。</p>
<!--anh:1-->
<h2>对比</h2>
<table>
<thead><tr><th></th><th>普通</th><th>甲油胶</th></tr></thead>
<tbody>
<tr><td>干燥</td><td>1–2 小时</td><td>照灯即干</td></tr>
<tr><td>持久</td><td>几天到一周</td><td>2–3 周</td></tr>
<tr><td>光泽</td><td>逐渐变暗</td><td>持续亮</td></tr>
<tr><td>卸除</td><td>洗甲水</td><td>磨封层、浸泡约 20 分钟</td></tr>
<tr><td>效果</td><td>有限</td><td>果冻、猫眼、丝绒、极光、镜面等</td></tr>
</tbody>
</table>
<h2>怎么选</h2>
<p>想保持 2–3 周、要特殊效果或常用手选甲油胶;想经常自己换色选普通指甲油;也可只涂护甲油。</p>
<!--anh:2-->
<h2>甲油胶更伤指甲吗</h2>
<p>甲油胶本身不伤甲,伤害来自撕甲、过度打磨或胶碰到皮肤。VESSCA 上色服务使用甲油胶:纯色 130,000₫,果冻 150,000₫,猫眼或亮粉 170,000₫,韩国高端 220,000₫ 起。</p>'''
bai('son-gel-va-son-thuong-khac-nhau','2026-11-09T08:30:00+07:00','Kiến thức nghề nail',
 A(('gel polish manicure','Sơn gel bóng sau khi hơ đèn','Glossy gel after curing','경화 후 광택 나는 젤','照灯后光亮的甲油胶'),
   [('nail polish bottles','Chai sơn thường và sơn gel','Regular polish and gel bottles','일반 폴리시와 젤 병','普通指甲油与甲油胶'),
    ('gel nails manicure','Bộ gel giữ bóng 2–3 tuần','Gel that stays glossy for weeks','몇 주간 광택이 유지되는 젤','数周保持光泽的甲油胶')]),
 ('Sơn gel và sơn thường khác nhau thế nào: nên chọn loại nào','So sánh sơn gel và sơn thường về cách khô, độ bền, độ bóng, cách tháo và hiệu ứng, khi nào nên chọn loại nào, sơn gel có hại hơn không.',
  'Sơn gel và sơn thường khác nhau thế nào | VESSCA',
  'Sơn gel và sơn thường: gel hơ đèn khô ngay, giữ 2–3 tuần, nhiều hiệu ứng; sơn thường khô bay hơi, giữ vài ngày. Nên chọn loại nào. VESSCA Bình Thạnh.',
  ['sơn gel và sơn thường','sơn gel là gì','sơn móng tay thường','sơn gel giữ bao lâu','nên sơn gel hay sơn thường'],vi,faq),
 ('Gel vs Regular Nail Polish: Differences and Which to Choose','Curing, durability, shine, removal and finishes compared, when to choose each and whether gel is more damaging.',
  'Gel vs Regular Polish | VESSCA Saigon','Gel cures instantly, lasts 2–3 weeks and offers more finishes; regular polish air-dries and lasts days. Which to choose. VESSCA, Binh Thanh.',
  ['gel vs regular polish','gel manicure Ho Chi Minh City','Korean nails Saigon','nail salon Binh Thanh','gel polish'],en,
  [('What is the main difference?','Regular polish air-dries and lasts days; gel cures under a lamp and lasts 2–3 weeks.'),('Does gel need a lamp?','Yes, UV or LED.'),('Is gel more damaging?','Not by itself; peeling and over-filing cause damage.')]),
 ('젤 vs 일반 매니큐어: 차이와 선택법','건조, 지속력, 광택, 제거, 질감 비교와 선택 기준, 젤이 더 해로운지.',
  '젤과 일반 매니큐어 차이 | 호치민 VESSCA','젤은 즉시 경화, 2–3주 유지, 다양한 질감. 일반 폴리시는 자연 건조, 며칠 유지. 호치민 빈탄 VESSCA.',
  ['젤네일 차이','일반 매니큐어','호치민 젤네일','호치민 네일샵','빈탄 네일'],ko,
  [('가장 큰 차이는?','일반은 자연 건조로 며칠, 젤은 램프 경화로 2–3주입니다.'),('젤은 램프가 필요한가요?','네, UV나 LED 램프가 필요합니다.'),('젤이 더 해로운가요?','젤 자체가 아니라 뜯기와 과한 파일링이 원인입니다.')]),
 ('甲油胶和普通指甲油有什么区别','干燥、持久、光泽、卸除和效果对比,何时选哪种,以及甲油胶是否更伤甲。',
  '甲油胶与普通指甲油区别 | 胡志明 VESSCA','甲油胶照灯即干、保持 2–3 周、效果多;普通指甲油风干、保持几天。如何选择。胡志明平盛郡 VESSCA。',
  ['甲油胶 区别','普通指甲油','胡志明 美甲','韩式美甲 胡志明','平盛郡 美甲店'],zh,
  [('主要区别是什么?','普通指甲油风干保持几天;甲油胶照灯固化保持 2–3 周。'),('甲油胶需要灯吗?','需要 UV 或 LED 灯。'),('甲油胶更伤甲吗?','本身不会,伤害来自撕甲和过度打磨。')]))

