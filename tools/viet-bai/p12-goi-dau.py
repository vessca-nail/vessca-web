# -*- coding: utf-8 -*-
"""Đợt 42 — 10 bài gội đầu dưỡng sinh, slot 09:30 từ 24/11 đến 3/12.
Từ khoá lấy từ Google autocomplete (truy vấn từ TP.HCM, 23/11/2026):
  "gội đầu dưỡng sinh bao nhiêu tiền một lần", "... có tác dụng gì",
  "... bao gồm những gì", "... bao nhiêu bước", "... bao nhiêu phút",
  "... có giảm đau đầu không", "... có cần cởi áo không",
  "... có lấy ráy tai", "gội đầu đêm/khuya bình thạnh".
Số liệu gói và bước lấy đúng từ lib/goi-dau.mjs — không được tự đặt thêm."""
from lib import bai, A

C = 'Gội đầu & Thư giãn'
D = ['2026-11-24','2026-11-25','2026-11-26','2026-11-27','2026-11-28',
     '2026-11-29','2026-11-30','2026-12-01','2026-12-02','2026-12-03']
T = lambda i: D[i] + 'T09:30:00+07:00'

# ---------------------------------------------------------------- 1
bai('goi-dau-duong-sinh-gia-bao-nhieu', T(0), C,
A(('head spa shampoo salon basin','Khách gội đầu dưỡng sinh tại tiệm',
   'A guest having a head spa treatment','헤드 스파를 받는 고객','顧客正在做頭皮SPA'),[]),
('Gội đầu dưỡng sinh giá bao nhiêu? Bảng giá tại VESSCA',
 'Giá một lần gội đầu dưỡng sinh phụ thuộc vào thời lượng và dòng dầu gội. Tại VESSCA có bốn gói, từ 99.000₫ đến 469.000₫.',
 'Gội đầu dưỡng sinh giá bao nhiêu? Bảng giá VESSCA',
 'Gội đầu dưỡng sinh ở Bình Thạnh giá bao nhiêu: bốn gói 30–75 phút, từ 99.000₫ tới 469.000₫, giá thay đổi theo dòng dầu gội bạn chọn.',
 ['gội đầu dưỡng sinh giá bao nhiêu','gội đầu dưỡng sinh bao nhiêu tiền','giá gội đầu dưỡng sinh bình thạnh','gội đầu dưỡng sinh giá rẻ'],
'''<p>Đây là câu hỏi được tìm nhiều nhất khi người ta mới nghe tới gội đầu dưỡng sinh. Câu trả lời ngắn: giá một lần phụ thuộc vào hai thứ — gói bạn chọn dài bao nhiêu phút, và dòng dầu gội bạn muốn dùng.</p>
<h2>Bốn gói tại VESSCA</h2>
<ul>
<li><b>Gói 01 — Gội sạch thơm, 30 phút:</b> 99.000₫ – 149.000₫</li>
<li><b>Gói 02 — Gội sạch thơm, massage chăm da đầu, 50 phút:</b> 229.000₫ – 279.000₫</li>
<li><b>Gói 03 — Gội sạch thơm, chăm da mặt, 50 phút:</b> 269.000₫ – 319.000₫</li>
<li><b>Gói 04 — Gói thiên đường, 75 phút:</b> 419.000₫ – 469.000₫</li>
</ul>
<h2>Vì sao mỗi gói có ba mức giá</h2>
<p>Mỗi gói cho bạn chọn một trong ba dòng dầu gội xả, và chính lựa chọn đó quyết định mức giá trong khoảng trên:</p>
<ul>
<li><b>Nguyên Xuân</b> — dầu gội thảo dược, mức thấp nhất</li>
<li><b>Gừng sả thiên nhiên</b> — mức giữa</li>
<li><b>Unove Hàn Quốc</b> — mức cao nhất</li>
</ul>
<p>Cách tính này để bạn không phải trả cho thứ mình không cần. Người muốn thử trước có thể bắt đầu ở gói 30 phút với dầu gội thảo dược.</p>
<h2>Mức 99.000₫ gồm những gì</h2>
<p>Gói thấp nhất không phải gói rút ruột. Trong 30 phút đó có tẩy trang và rửa mặt, gội hai lần, xả dầu xả, sấy bằng máy sấy ion âm, dầu dưỡng tóc L’Oréal, kèm nước uống và bánh ngọt. Đây là một lần gội đầy đủ, chỉ không có phần massage dài.</p>
<h2>Những mục lẻ nếu bạn muốn thêm</h2>
<p>Ngoài bốn gói, tiệm có các mục lẻ để bạn ghép thêm: massage đầu và cổ vai gáy 89.000₫, massage cổ vai gáy 89.000₫, tẩy tế bào chết da đầu 49.000₫, chiếu đèn ánh sáng sinh học 49.000₫, massage mặt 89.000₫. Mặt nạ nâng cơ săn chắc cộng thêm 30.000₫, ba loại mặt nạ còn lại đã nằm trong gói.</p>
<h2>So với mặt bằng chung</h2>
<p>Khoảng giá gội đầu dưỡng sinh ở TP.HCM rất rộng, nên con số đơn lẻ không nói được nhiều. Điều đáng so sánh là thời lượng và số bước thật trong gói. Một gói 50 phút có massage hai lần khác hẳn một gói 50 phút chỉ gội rồi sấy. Khi hỏi giá ở bất cứ đâu, nên hỏi kèm hai câu: bao nhiêu phút, và trong đó gồm những bước nào.</p>
<p>Bảng giá đầy đủ từng bước của bốn gói có trên trang <a href="/goi-dau/">Gội đầu dưỡng sinh</a>. Bạn đọc trước rồi đặt lịch cho đúng gói mình cần.</p>''',
 [('Gói rẻ nhất bao nhiêu tiền?','99.000₫ cho gói 30 phút với dầu gội thảo dược Nguyên Xuân. Đây là mức thấp nhất trong bảng giá.'),
  ('Giá đã gồm massage chưa?','Gói 01 chưa có phần massage dài. Từ gói 02 trở lên có massage đầu, hoặc bạn ghép thêm mục lẻ 89.000₫ vào gói 01.'),
  ('Có phụ phí gì không?','Không. Chỉ mặt nạ nâng cơ săn chắc cộng thêm 30.000₫, và các mục lẻ bạn chủ động chọn thêm.')]),
('How Much Does a Head Spa Cost? VESSCA Price List',
 'The price of one head spa session depends on length and which shampoo line you pick. VESSCA has four packages, from 99,000₫ to 469,000₫.',
 'Head Spa Prices in Binh Thanh — from 99,000₫ | VESSCA',
 'Head spa prices in Binh Thanh, Saigon: four packages of 30–75 minutes, 99,000₫ to 469,000₫, with the shampoo line you choose setting the rate.',
 ['head spa price saigon','head spa binh thanh cost','vietnamese head spa price'],
'''<p>Two things set the price of a head spa session: how long the package runs, and which shampoo line you choose.</p>
<h2>Four packages at VESSCA</h2>
<ul>
<li><b>01 — Fresh Hair Wash, 30 min:</b> 99,000₫ – 149,000₫</li>
<li><b>02 — Hair Wash &amp; Scalp Therapy, 50 min:</b> 229,000₫ – 279,000₫</li>
<li><b>03 — Hair Wash &amp; Facial Glow Care, 50 min:</b> 269,000₫ – 319,000₫</li>
<li><b>04 — The Paradise Ritual, 75 min:</b> 419,000₫ – 469,000₫</li>
</ul>
<h2>Why each package has three rates</h2>
<p>Every package lets you pick one of three shampoo and conditioner lines, and that choice places you within the range: Nguyen Xuan herbal at the lowest rate, natural ginger and lemongrass in the middle, Korean Unove at the top. You pay for what you actually want.</p>
<h2>What the lowest rate includes</h2>
<p>The 30-minute package is not a stripped-down version. It covers make-up removal and a face cleanse, a double shampoo, conditioner, a blow-dry with a negative-ion dryer, L’Oréal hair oil, plus a drink and something sweet. It simply leaves out the longer massage.</p>
<h2>Add-ons</h2>
<p>Head with neck and shoulder massage 89,000₫, neck and shoulder massage 89,000₫, scalp exfoliation 49,000₫, LED light therapy 49,000₫, facial massage 89,000₫. The lifting and firming mask adds 30,000₫; the other three masks are included.</p>
<p>The full step-by-step list for all four packages is on the <a href="/en/goi-dau/">head spa page</a>.</p>''',
 [('What is the cheapest option?','99,000₫ for the 30-minute package with the Nguyen Xuan herbal shampoo.'),
  ('Is massage included?','Package 01 has no long massage. Packages 02 and up include a head massage, or you can add one to package 01 for 89,000₫.')]),
('두피 스파 가격은 얼마인가요? VESSCA 가격표',
 '1회 가격은 코스 길이와 선택한 샴푸 라인에 따라 달라집니다. VESSCA에는 99,000₫부터 469,000₫까지 네 가지 코스가 있습니다.',
 '빈탄 헤드 스파 가격 — 99,000₫부터 | VESSCA',
 '호치민 빈탄 헤드 스파 가격: 30~75분 네 가지 코스, 99,000₫~469,000₫. 선택하는 샴푸 라인에 따라 금액이 정해집니다.',
 ['호치민 헤드 스파 가격','빈탄 두피 스파','베트남 헤드 스파 비용'],
'''<p>가격을 정하는 것은 두 가지입니다. 코스가 몇 분인지, 그리고 어떤 샴푸 라인을 선택하는지입니다.</p>
<h2>VESSCA의 네 가지 코스</h2>
<ul>
<li><b>01 — 프레시 헤어 워시, 30분:</b> 99,000₫ – 149,000₫</li>
<li><b>02 — 헤어 워시 &amp; 두피 테라피, 50분:</b> 229,000₫ – 279,000₫</li>
<li><b>03 — 헤어 워시 &amp; 페이셜 글로우 케어, 50분:</b> 269,000₫ – 319,000₫</li>
<li><b>04 — 파라다이스 리추얼, 75분:</b> 419,000₫ – 469,000₫</li>
</ul>
<h2>한 코스에 세 가지 금액이 있는 이유</h2>
<p>모든 코스에서 샴푸와 컨디셔너 라인을 세 가지 중에 고를 수 있고, 그 선택이 위 범위 안에서 금액을 정합니다. Nguyen Xuan 허브가 가장 낮고, 천연 생강·레몬그라스가 중간, 한국 Unove가 가장 높습니다.</p>
<h2>가장 낮은 금액에 포함되는 것</h2>
<p>30분 코스도 축소판이 아닙니다. 클렌징과 세안, 샴푸 2회, 컨디셔너, 음이온 드라이어 드라이, 로레알 헤어 오일, 음료와 디저트가 들어갑니다. 긴 마사지만 빠집니다.</p>
<h2>추가 항목</h2>
<p>두피·목·어깨 마사지 89,000₫, 목·어깨 마사지 89,000₫, 두피 스케일링 49,000₫, LED 광테라피 49,000₫, 페이셜 마사지 89,000₫. 리프팅·탄력 마스크는 30,000₫ 추가이고 나머지 세 종류는 코스에 포함됩니다.</p>
<p>네 코스의 진행 순서는 <a href="/ko/goi-dau/">헤드 스파 페이지</a>에 모두 적어 두었습니다.</p>''',
 [('가장 저렴한 코스는 얼마인가요?','Nguyen Xuan 허브 샴푸를 선택한 30분 코스가 99,000₫입니다.'),
  ('마사지가 포함되어 있나요?','01 코스에는 긴 마사지가 없습니다. 02 코스부터 두피 마사지가 포함되며, 01 코스에 89,000₫으로 추가할 수도 있습니다.')]),
('養生洗髮多少錢？VESSCA 價目表',
 '單次價格取決於時長與您選擇的洗髮精。VESSCA 共有四種套餐，99,000₫ 至 469,000₫。',
 '平盛郡養生洗髮價格 — 99,000₫起 | VESSCA',
 '胡志明市平盛郡養生洗髮價格：四種套餐 30–75 分鐘，99,000₫ 至 469,000₫，金額依您選擇的洗髮精而定。',
 ['胡志明養生洗髮價格','平盛郡頭皮SPA','越南洗髮按摩費用'],
'''<p>決定價格的有兩件事：套餐多長，以及您選擇哪一款洗髮精。</p>
<h2>VESSCA 的四種套餐</h2>
<ul>
<li><b>01 — 清爽洗髮，30 分鐘：</b>99,000₫ – 149,000₫</li>
<li><b>02 — 洗髮＋頭皮護理，50 分鐘：</b>229,000₫ – 279,000₫</li>
<li><b>03 — 洗髮＋臉部亮采護理，50 分鐘：</b>269,000₫ – 319,000₫</li>
<li><b>04 — 天堂儀式，75 分鐘：</b>419,000₫ – 469,000₫</li>
</ul>
<h2>為什麼同一套餐有三個價格</h2>
<p>每個套餐都可以從三款洗髮精與護髮素中選擇，這個選擇決定了金額落在上面哪個位置。Nguyen Xuan 草本最低，天然薑香茅居中，韓國 Unove 最高。</p>
<h2>最低價包含什麼</h2>
<p>30 分鐘套餐並不是簡化版。其中包含卸妝與潔面、洗髮兩次、護髮素、負離子吹風機吹乾、L’Oréal 護髮油，以及飲品與甜點。只是少了較長的按摩。</p>
<h2>可以加選的項目</h2>
<p>頭部及肩頸按摩 89,000₫、肩頸按摩 89,000₫、頭皮去角質 49,000₫、LED 光療 49,000₫、臉部按摩 89,000₫。提拉緊緻面膜加 30,000₫，其餘三款已含在套餐內。</p>
<p>四個套餐的完整流程都寫在<a href="/zh/goi-dau/">養生洗髮頁面</a>。</p>''',
 [('最便宜的套餐多少錢？','選擇 Nguyen Xuan 草本洗髮精的 30 分鐘套餐為 99,000₫。'),
  ('價格包含按摩嗎？','01 套餐沒有較長的按摩。02 套餐起含頭部按摩，也可以在 01 套餐加價 89,000₫ 加入。')]))

# ---------------------------------------------------------------- 2
bai('goi-dau-duong-sinh-co-tac-dung-gi', T(1), C,
A(('scalp massage relaxing spa','Massage da đầu trong buổi gội đầu dưỡng sinh',
   'A relaxing scalp massage','릴랙싱 두피 마사지','放鬆的頭皮按摩'),[]),
('Gội đầu dưỡng sinh có tác dụng gì?',
 'Tác dụng thật của gội đầu dưỡng sinh nằm ở ba chỗ: da đầu sạch hơn, cơ cổ vai gáy giãn ra, và thần kinh được nghỉ. Những gì nó không làm được cũng cần nói rõ.',
 'Gội đầu dưỡng sinh có tác dụng gì? Nói thật',
 'Gội đầu dưỡng sinh tác dụng gì: làm sạch da đầu, giãn cơ cổ vai gáy, giúp dễ ngủ hơn. Bài viết nói rõ cả những điều nó không làm được.',
 ['gội đầu dưỡng sinh có tác dụng gì','gội đầu dưỡng sinh có tốt không','lợi ích gội đầu dưỡng sinh'],
'''<p>Nhiều nơi quảng cáo gội đầu dưỡng sinh như một liệu pháp chữa bệnh. VESSCA nói thẳng những gì nó làm được và những gì không.</p>
<h2>Làm sạch sâu hơn gội ở nhà</h2>
<p>Gội ở nhà thường gội một lần, gấp, và khó với tới vùng sau đầu. Ở tiệm gội hai lần, có người làm sạch đúng vùng chân tóc và sau tai, tóc được xả dầu xả rồi sấy bằng máy sấy ion âm thay vì sấy nóng. Da đầu nhiều dầu hoặc bết nhanh thấy khác biệt rõ nhất ở điểm này.</p>
<h2>Giãn cơ cổ vai gáy</h2>
<p>Đây là phần nhiều người cần mà không biết mình cần. Ngồi máy tính nhiều, nhìn điện thoại nhiều thì cơ cổ và vai căng cứng theo ngày. Các gói từ 02 trở lên có massage đầu, và mục massage đầu cùng cổ vai gáy có thể ghép thêm. Sau một buổi, phần căng ở vai thường nhẹ đi.</p>
<h2>Giúp dễ ngủ hơn</h2>
<p>Khách hay kể là tối hôm đó ngủ sâu hơn. Lý do đơn giản: nằm yên 50 tới 75 phút, không điện thoại, có người massage đầu đều tay. Đây là tác dụng về nghỉ ngơi, không phải thuốc ngủ.</p>
<h2>Những điều gội đầu dưỡng sinh không làm được</h2>
<ul>
<li>Không chữa rụng tóc do nội tiết, do thuốc hay do bệnh. Rụng tóc nhiều và kéo dài thì nên gặp bác sĩ da liễu.</li>
<li>Không mọc lại tóc đã rụng.</li>
<li>Không chữa được nấm da đầu, vảy nến hay viêm da. Da đầu đang có tổn thương, mụn mủ hoặc vết xước thì nên chữa trước, gội sau.</li>
<li>Không thay thế điều trị đau đầu hay đau vai gáy do bệnh lý.</li>
</ul>
<p>Nói đúng công dụng thì khách biết mình mua gì. Nếu bạn cần một buổi nghỉ thật và một cái đầu sạch, dịch vụ này đáng. Nếu bạn đang có vấn đề về da đầu hay tóc, nên khám trước.</p>
<p>Chi tiết từng bước trong bốn gói có ở trang <a href="/goi-dau/">Gội đầu dưỡng sinh</a>, và bài <a href="/blog/goi-dau-duong-sinh-la-gi/">gội đầu dưỡng sinh là gì</a> giải thích tên gọi.</p>''',
 [('Gội đầu dưỡng sinh có trị rụng tóc không?','Không. Dịch vụ này làm sạch da đầu và giúp thư giãn, không điều trị rụng tóc. Rụng tóc nhiều nên gặp bác sĩ da liễu.'),
  ('Bao lâu thì thấy tác dụng?','Phần thư giãn và cơ vai nhẹ đi thấy ngay sau buổi đầu. Phần da đầu sạch và tóc mượt duy trì được vài ngày.'),
  ('Người da đầu nhạy cảm làm được không?','Được, nhưng nên nói trước để kỹ thuật viên chọn dầu gội dịu và giảm lực massage. Da đầu đang viêm hoặc có vết thương thì nên hoãn.')]),
('What Does a Head Spa Actually Do?',
 'A head spa does three real things: deeper scalp cleansing, release in the neck and shoulders, and genuine rest. What it cannot do matters too.',
 'What Does a Head Spa Actually Do? An Honest Answer',
 'What a head spa really does: cleans the scalp properly, releases neck and shoulder tension, helps you sleep. Also what it cannot treat.',
 ['head spa benefits','does head spa work','scalp massage benefits'],
'''<p>Plenty of places market a head spa as a cure. Here is what it does and what it does not.</p>
<h2>A deeper clean than washing at home</h2>
<p>At home most people shampoo once, in a hurry, and miss the back of the head. Here the hair is shampooed twice, someone else reaches the hairline and behind the ears, and the blow-dry uses a negative-ion dryer rather than high heat. Oily scalps notice this most.</p>
<h2>Release in the neck and shoulders</h2>
<p>This is the part people need without knowing it. Desk work and phone screens leave the neck and shoulders tight. Packages 02 and up include a head massage, and a head with neck and shoulder massage can be added to any package.</p>
<h2>Better sleep that night</h2>
<p>Guests often mention sleeping more deeply. The reason is simple: 50 to 75 minutes lying still, no phone, steady pressure on the scalp. That is rest, not medication.</p>
<h2>What it cannot do</h2>
<ul>
<li>It does not treat hair loss caused by hormones, medication or illness.</li>
<li>It does not regrow hair that has already fallen.</li>
<li>It does not treat scalp fungus, psoriasis or dermatitis. Treat an irritated or broken scalp first.</li>
<li>It does not replace medical care for headaches or shoulder pain.</li>
</ul>
<p>Full step lists for the four packages are on the <a href="/en/goi-dau/">head spa page</a>.</p>''',
 [('Does a head spa stop hair loss?','No. It cleans the scalp and helps you relax. Persistent hair loss needs a dermatologist.'),
  ('Can I come with a sensitive scalp?','Yes, but say so first so the technician picks a gentler shampoo and lighter pressure. Postpone if the scalp is broken or inflamed.')]),
('헤드 스파는 어떤 효과가 있나요?',
 '헤드 스파가 실제로 하는 일은 세 가지입니다. 두피를 깨끗하게, 목과 어깨를 풀어주고, 제대로 쉬게 합니다. 할 수 없는 일도 분명히 말씀드립니다.',
 '헤드 스파 효과 — 솔직하게 말하면 | VESSCA',
 '헤드 스파의 실제 효과: 두피 세정, 목·어깨 긴장 완화, 수면의 질. 치료할 수 없는 것도 함께 적었습니다.',
 ['헤드 스파 효과','두피 마사지 효과','호치민 헤드 스파'],
'''<p>헤드 스파를 치료처럼 광고하는 곳이 많습니다. 실제로 되는 것과 되지 않는 것을 적습니다.</p>
<h2>집에서 감는 것보다 깨끗하게</h2>
<p>집에서는 보통 한 번, 급하게 감고 뒤통수까지 닿지 않습니다. 여기서는 두 번 감고, 헤어라인과 귀 뒤까지 다른 사람이 닦아 주며, 뜨거운 바람 대신 음이온 드라이어로 말립니다. 두피가 쉽게 기름지는 분이 차이를 가장 많이 느낍니다.</p>
<h2>목과 어깨 이완</h2>
<p>필요한 줄 모르고 있던 부분입니다. 02 코스부터 두피 마사지가 포함되고, 두피·목·어깨 마사지는 어느 코스에나 추가할 수 있습니다.</p>
<h2>그날 밤 잠</h2>
<p>깊이 잤다는 말을 자주 듣습니다. 50~75분 동안 휴대폰 없이 가만히 누워 일정한 압으로 두피를 받기 때문입니다. 수면제가 아니라 휴식입니다.</p>
<h2>할 수 없는 것</h2>
<ul>
<li>호르몬, 약물, 질병으로 인한 탈모를 치료하지 않습니다.</li>
<li>이미 빠진 모발을 다시 자라게 하지 않습니다.</li>
<li>두피 진균, 건선, 피부염을 치료하지 않습니다. 상처나 염증이 있으면 먼저 치료하십시오.</li>
<li>두통이나 어깨 통증의 진료를 대신하지 않습니다.</li>
</ul>
<p>네 코스의 진행 순서는 <a href="/ko/goi-dau/">헤드 스파 페이지</a>에 있습니다.</p>''',
 [('탈모에 효과가 있나요?','없습니다. 두피 세정과 이완이 목적입니다. 탈모가 계속되면 피부과 진료를 권합니다.'),
  ('두피가 예민해도 받을 수 있나요?','가능합니다. 미리 말씀해 주시면 순한 샴푸로 바꾸고 압을 낮춥니다. 상처나 염증이 있으면 미루시는 편이 좋습니다.')]),
('養生洗髮有什麼效果？',
 '養生洗髮真正做到的有三件事：頭皮更乾淨、肩頸放鬆、好好休息。做不到的事也必須說清楚。',
 '養生洗髮有什麼效果？老實說 | VESSCA',
 '養生洗髮的實際效果：清潔頭皮、緩解肩頸緊繃、幫助入睡。也說明它無法治療的部分。',
 ['養生洗髮效果','頭皮按摩效果','胡志明頭皮SPA'],
'''<p>許多店家把養生洗髮當成治療來宣傳。這裡寫清楚做得到與做不到的事。</p>
<h2>比在家洗得乾淨</h2>
<p>在家通常只洗一次、很匆忙，後腦也洗不到。在店裡洗兩次，由別人把髮際線與耳後都清到，並用負離子吹風機而非高溫吹乾。頭皮容易出油的人感受最明顯。</p>
<h2>肩頸放鬆</h2>
<p>這是很多人需要卻不自知的部分。02 套餐起含頭部按摩，頭部及肩頸按摩也可以加在任何套餐上。</p>
<h2>當晚的睡眠</h2>
<p>常有顧客說那天睡得比較沉。原因很單純：50 到 75 分鐘躺著不看手機，有人以穩定的力道按頭皮。這是休息，不是藥。</p>
<h2>做不到的事</h2>
<ul>
<li>無法治療荷爾蒙、藥物或疾病造成的掉髮。</li>
<li>無法讓已經掉落的頭髮重新長出。</li>
<li>無法治療頭皮真菌、乾癬或皮膚炎。有傷口或發炎請先就醫。</li>
<li>無法取代頭痛或肩頸疼痛的醫療。</li>
</ul>
<p>四個套餐的流程都在<a href="/zh/goi-dau/">養生洗髮頁面</a>。</p>''',
 [('對掉髮有效嗎？','沒有。這項服務是清潔頭皮與放鬆，不治療掉髮。持續掉髮請看皮膚科。'),
  ('頭皮敏感可以做嗎？','可以，但請先告知，技術人員會改用溫和的洗髮精並減輕力道。頭皮有傷口或發炎時建議延後。')]))

# ---------------------------------------------------------------- 3
bai('goi-dau-duong-sinh-gom-nhung-buoc-nao', T(2), C,
A(('hair washing salon sink towel','Các bước trong một buổi gội đầu dưỡng sinh',
   'The steps of a head spa session','헤드 스파의 진행 순서','養生洗髮的流程'),[]),
('Gội đầu dưỡng sinh gồm những bước nào?',
 'Một buổi gội đầu dưỡng sinh ở VESSCA có từ 6 tới 14 bước tuỳ gói. Bài này liệt kê đúng thứ tự từng bước để bạn biết mình sẽ trải qua những gì.',
 'Gội đầu dưỡng sinh gồm những bước nào?',
 'Gội đầu dưỡng sinh gồm bao nhiêu bước: liệt kê đúng thứ tự từng bước của bốn gói 30–75 phút tại VESSCA Bình Thạnh.',
 ['gội đầu dưỡng sinh gồm những bước nào','gội đầu dưỡng sinh bao nhiêu bước','quy trình gội đầu dưỡng sinh','gội đầu dưỡng sinh bao gồm những gì'],
'''<p>Người tìm câu này thường là người chưa đi lần nào và muốn biết trước. Dưới đây là đúng thứ tự các bước của bốn gói tại VESSCA.</p>
<h2>Gói 01 — 30 phút, 6 bước</h2>
<ol>
<li>Tẩy trang Garnier, rửa mặt SVR</li>
<li>Gội dầu gội 2 lần</li>
<li>Xả dầu xả siêu mượt</li>
<li>Sấy bảo vệ tóc bằng máy sấy ion âm</li>
<li>Dầu dưỡng tóc L’Oréal</li>
<li>Nước uống, bánh ngọt</li>
</ol>
<h2>Gói 02 — 50 phút, 11 bước</h2>
<p>Giữ nguyên các bước trên, thêm: tẩy tế bào chết da đầu, đắp mặt nạ mắt, massage đầu thư giãn lần 1 trước khi gội, massage đầu thư giãn lần 2 sau khi xả, và dưỡng da tay. Đây là gói dành cho người muốn phần massage đầu là trọng tâm.</p>
<h2>Gói 03 — 50 phút, 11 bước</h2>
<p>Cùng thời lượng với gói 02 nhưng đổi hướng sang da mặt: tẩy tế bào chết da mặt, đắp mặt nạ Hàn Quốc, massage mặt thư giãn nâng cơ, chiếu đèn ánh sáng sinh học, rồi mới sấy và dưỡng da tay. Chọn gói này nếu bạn quan tâm da mặt hơn da đầu.</p>
<h2>Gói 04 — Gói thiên đường, 75 phút, 14 bước</h2>
<p>Gói signature, gộp cả hai hướng: tẩy trang rửa mặt, tẩy tế bào chết da mặt, mặt nạ Hàn Quốc, tẩy tế bào chết da đầu, gội hai lần, xả, massage mặt nâng cơ, chiếu đèn sinh học, mặt nạ mắt, massage đầu cùng cổ vai gáy, sấy ion âm, dầu dưỡng tóc, dưỡng da tay, nước uống và bánh ngọt.</p>
<h2>Chọn gói theo điều bạn cần nhất</h2>
<p>Số bước nhiều không có nghĩa là tốt hơn cho bạn. Người cần cái đầu sạch nhanh thì gói 01 đủ. Người mỏi cổ vai thì gói 02 hoặc ghép thêm mục massage cổ vai gáy. Người đi trước một buổi tiệc thì gói 03 hợp hơn vì có phần da mặt.</p>
<p>Bảng giá từng gói kèm hình ở trang <a href="/goi-dau/">Gội đầu dưỡng sinh</a>.</p>''',
 [('Gói nào nhiều bước nhất?','Gói thiên đường 75 phút, 14 bước, gộp cả phần da đầu và da mặt.'),
  ('Có cần gội đầu trước khi tới không?','Không cần. Tóc bẩn hay nhiều dầu là bình thường, đó là việc của buổi gội.'),
  ('Mặt nạ có mất thêm tiền không?','Ba loại mặt nạ nằm trong gói. Chỉ mặt nạ nâng cơ săn chắc cộng thêm 30.000₫.')]),
('What Are the Steps in a Head Spa?',
 'A session at VESSCA runs from 6 to 14 steps depending on the package. Here is the exact order for each one.',
 'What Are the Steps in a Head Spa? | VESSCA',
 'The steps in a head spa session, in order, for all four VESSCA packages of 30 to 75 minutes in Binh Thanh, Saigon.',
 ['head spa steps','head spa procedure','what happens in a head spa'],
'''<p>Most people asking this have not been before. Here is the exact order.</p>
<h2>Package 01 — 30 minutes, 6 steps</h2>
<ol><li>Garnier make-up removal, SVR face cleanse</li><li>Double shampoo</li><li>Silky conditioner</li><li>Blow-dry with a negative-ion dryer</li><li>L’Oréal hair oil</li><li>A drink and a sweet treat</li></ol>
<h2>Package 02 — 50 minutes, 11 steps</h2>
<p>Everything above plus scalp exfoliation, an eye mask, a relaxing head massage before the wash, a second head massage after the conditioner, and hand care. Choose this if the head massage is the point.</p>
<h2>Package 03 — 50 minutes, 11 steps</h2>
<p>Same length, turned toward the face: facial exfoliation, a Korean sheet mask, a lifting facial massage, LED light therapy, then the blow-dry and hand care.</p>
<h2>Package 04 — The Paradise Ritual, 75 minutes, 14 steps</h2>
<p>The signature package combines both: cleanse, facial exfoliation, sheet mask, scalp exfoliation, double shampoo, conditioner, lifting facial massage, LED therapy, eye mask, head with neck and shoulder massage, negative-ion blow-dry, hair oil, hand care, and refreshments.</p>
<p>Prices for each package are on the <a href="/en/goi-dau/">head spa page</a>.</p>''',
 [('Which package has the most steps?','The Paradise Ritual, 75 minutes and 14 steps, covering both scalp and face.'),
  ('Should I wash my hair before coming?','No. Coming with oily or unwashed hair is normal and expected.')]),
('헤드 스파는 어떤 순서로 진행되나요?',
 'VESSCA의 한 회차는 코스에 따라 6단계에서 14단계까지입니다. 각 코스의 순서를 그대로 적었습니다.',
 '헤드 스파 진행 순서 | VESSCA 빈탄',
 '헤드 스파의 진행 순서: 30~75분 네 가지 코스의 단계를 순서대로 정리했습니다.',
 ['헤드 스파 순서','헤드 스파 과정','두피 스파 단계'],
'''<p>처음 오시는 분이 많이 찾는 내용이라 순서를 그대로 적습니다.</p>
<h2>01 코스 — 30분, 6단계</h2>
<ol><li>가르니에 클렌징, SVR 세안</li><li>샴푸 2회</li><li>실키 컨디셔너</li><li>음이온 드라이어 드라이</li><li>로레알 헤어 오일</li><li>음료와 디저트</li></ol>
<h2>02 코스 — 50분, 11단계</h2>
<p>위 단계에 두피 스케일링, 아이 마스크, 샴푸 전 두피 마사지 1차, 컨디셔너 후 2차, 핸드 케어가 더해집니다. 두피 마사지가 목적이라면 이 코스입니다.</p>
<h2>03 코스 — 50분, 11단계</h2>
<p>같은 시간이지만 얼굴 쪽으로 향합니다. 얼굴 각질 케어, 한국 마스크팩, 리프팅 페이셜 마사지, LED 광테라피 후 드라이와 핸드 케어로 마칩니다.</p>
<h2>04 코스 — 파라다이스 리추얼, 75분, 14단계</h2>
<p>두 방향을 모두 담은 시그니처 코스입니다. 클렌징, 얼굴 각질 케어, 마스크팩, 두피 스케일링, 샴푸 2회, 컨디셔너, 리프팅 페이셜 마사지, LED 광테라피, 아이 마스크, 두피·목·어깨 마사지, 음이온 드라이, 헤어 오일, 핸드 케어, 음료와 디저트.</p>
<p>코스별 금액은 <a href="/ko/goi-dau/">헤드 스파 페이지</a>에 있습니다.</p>''',
 [('단계가 가장 많은 코스는 무엇인가요?','파라다이스 리추얼입니다. 75분 14단계로 두피와 얼굴을 모두 다룹니다.'),
  ('오기 전에 머리를 감아야 하나요?','아닙니다. 감지 않은 상태로 오시는 것이 자연스럽습니다.')]),
('養生洗髮有哪些步驟？',
 'VESSCA 的一次服務依套餐有 6 到 14 個步驟。以下照順序列出每個套餐的流程。',
 '養生洗髮有哪些步驟？| VESSCA 平盛郡',
 '養生洗髮的完整步驟：依序列出 30 至 75 分鐘四種套餐的每一個環節。',
 ['養生洗髮步驟','頭皮SPA流程','洗髮按摩過程'],
'''<p>會找這個問題的多是還沒來過的人，所以把順序照實寫出來。</p>
<h2>01 套餐 — 30 分鐘，6 個步驟</h2>
<ol><li>Garnier 卸妝、SVR 潔面</li><li>洗髮兩次</li><li>柔順護髮素</li><li>負離子吹風機吹乾</li><li>L’Oréal 護髮油</li><li>飲品與甜點</li></ol>
<h2>02 套餐 — 50 分鐘，11 個步驟</h2>
<p>在上述之外加上頭皮去角質、眼膜、洗髮前的第一次頭部按摩、護髮素後的第二次按摩，以及手部保養。以頭部按摩為重點的人適合這個套餐。</p>
<h2>03 套餐 — 50 分鐘，11 個步驟</h2>
<p>時間相同但轉向臉部：臉部去角質、韓國面膜、提拉按摩、LED 光療，之後才吹乾並做手部保養。</p>
<h2>04 套餐 — 天堂儀式，75 分鐘，14 個步驟</h2>
<p>招牌套餐把兩個方向都包含進來：卸妝潔面、臉部去角質、韓國面膜、頭皮去角質、洗髮兩次、護髮素、提拉按摩、LED 光療、眼膜、頭部及肩頸按摩、負離子吹乾、護髮油、手部保養、飲品與甜點。</p>
<p>各套餐金額請見<a href="/zh/goi-dau/">養生洗髮頁面</a>。</p>''',
 [('步驟最多的是哪個套餐？','天堂儀式，75 分鐘 14 個步驟，頭皮與臉部都包含。'),
  ('來之前需要先洗頭嗎？','不需要。頭髮未洗或出油都很正常。')]))

# ---------------------------------------------------------------- 4
bai('goi-dau-duong-sinh-bao-nhieu-phut', T(3), C,
A(('spa clock relaxing towel treatment','Thời lượng một buổi gội đầu dưỡng sinh',
   'How long a head spa session takes','헤드 스파 소요 시간','養生洗髮所需時間'),[]),
('Gội đầu dưỡng sinh bao nhiêu phút?',
 'Tại VESSCA có bốn mốc thời gian: 30, 50, 50 và 75 phút. Bài này giúp bạn chọn mốc phù hợp với thời gian bạn thật sự có.',
 'Gội đầu dưỡng sinh bao nhiêu phút? Chọn đúng gói',
 'Gội đầu dưỡng sinh mất bao nhiêu phút: bốn mốc 30, 50 và 75 phút tại VESSCA Bình Thạnh, kèm cách chọn theo thời gian bạn có.',
 ['gội đầu dưỡng sinh bao nhiêu phút','gội đầu dưỡng sinh bao lâu','gội đầu dưỡng sinh mất bao lâu'],
'''<p>Câu hỏi này thường đi kèm một câu hỏi thật phía sau: tôi tranh được bao nhiêu thời gian trong ngày. Bốn gói của VESSCA tương ứng bốn khoảng rất khác nhau.</p>
<h2>30 phút — gói 01</h2>
<p>Vừa đủ cho giờ nghỉ trưa hoặc một lần ghé trên đường về. Có tẩy trang rửa mặt, gội hai lần, xả, sấy ion âm, dầu dưỡng tóc, nước uống. Không có phần massage dài.</p>
<h2>50 phút — gói 02 và gói 03</h2>
<p>Đây là mốc nhiều người chọn. Cùng 50 phút nhưng hai hướng khác nhau: gói 02 dồn vào da đầu với massage đầu hai lần, gói 03 dồn vào da mặt với mặt nạ Hàn Quốc, massage mặt và chiếu đèn sinh học. Bạn chọn theo thứ mình cần, không phải theo giá.</p>
<h2>75 phút — gói thiên đường</h2>
<p>Gói signature, gộp cả da đầu và da mặt, 14 bước. Nên đặt vào buổi rảnh thật, đừng ghép sát một hẹn khác.</p>
<h2>Nhớ cộng thêm thời gian ngoài gói</h2>
<p>Thời lượng trên là thời gian làm. Thực tế nên tính thêm 5 tới 10 phút cho lúc trao đổi với kỹ thuật viên về dầu gội và mặt nạ, và lúc tóc nguội trước khi ra ngoài. Nếu bạn làm cùng một bộ nail trong cùng buổi thì nên nói trước khi đặt lịch để tiệm xếp giờ liền mạch.</p>
<h2>Gợi ý chọn nhanh</h2>
<ul>
<li>Có dưới 45 phút: gói 01</li>
<li>Mỏi cổ vai, cần massage: gói 02</li>
<li>Đi tiệc, muốn da mặt sáng: gói 03</li>
<li>Có hơn 90 phút và muốn một buổi trọn: gói 04</li>
</ul>
<p>Bảng giá bốn gói ở trang <a href="/goi-dau/">Gội đầu dưỡng sinh</a>. Muốn làm cùng lúc với nail thì xem bài <a href="/blog/nail-va-goi-dau-cung-mot-buoi/">nail và gội đầu cùng một buổi</a>.</p>''',
 [('Gói ngắn nhất bao nhiêu phút?','30 phút, gói 01, gồm sáu bước.'),
  ('Có gói dưới 30 phút không?','Không. 30 phút là mốc ngắn nhất để làm đủ các bước mà không phải làm gấp.'),
  ('Làm nail và gội đầu trong một buổi mất bao lâu?','Tuỳ bộ nail và gói gội. Khi đặt lịch bạn nói cả hai dịch vụ để tiệm tính giờ và xếp liền nhau.')]),
('How Long Does a Head Spa Take?',
 'VESSCA has four lengths: 30, 50, 50 and 75 minutes. Here is how to pick the one that fits the time you actually have.',
 'How Long Does a Head Spa Take? | VESSCA',
 'Head spa length: 30, 50 and 75-minute packages at VESSCA in Binh Thanh, with help choosing by the time you have.',
 ['how long head spa','head spa duration','head spa 60 minutes'],
'''<p>Behind this question is usually another one: how much time can I spare today.</p>
<h2>30 minutes — package 01</h2>
<p>Enough for a lunch break or a stop on the way home. Cleanse, double shampoo, conditioner, negative-ion blow-dry, hair oil, a drink. No long massage.</p>
<h2>50 minutes — packages 02 and 03</h2>
<p>The most popular length. Same time, two directions: 02 goes deep on the scalp with two head massages, 03 goes to the face with a Korean sheet mask, lifting massage and LED therapy. Choose by what you need, not by price.</p>
<h2>75 minutes — The Paradise Ritual</h2>
<p>The signature package, scalp and face together, 14 steps. Book it on a genuinely free afternoon.</p>
<h2>Add time outside the package</h2>
<p>Those are treatment times. Allow another 5 to 10 minutes for choosing your shampoo and mask, and letting the hair settle. If you are having nails done in the same visit, say so when booking.</p>
<p>Prices are on the <a href="/en/goi-dau/">head spa page</a>.</p>''',
 [('What is the shortest package?','30 minutes, package 01, six steps.'),
  ('Is there anything under 30 minutes?','No. Thirty minutes is the shortest that fits every step without rushing.')]),
('헤드 스파는 몇 분 걸리나요?',
 'VESSCA에는 30분, 50분, 50분, 75분 네 가지가 있습니다. 실제로 낼 수 있는 시간에 맞춰 고르는 방법을 적었습니다.',
 '헤드 스파 소요 시간 | VESSCA 빈탄',
 '헤드 스파 소요 시간: 30분·50분·75분 코스와, 가진 시간에 맞춰 고르는 방법.',
 ['헤드 스파 시간','헤드 스파 몇 분','두피 스파 소요'],
'''<p>이 질문 뒤에는 보통 다른 질문이 있습니다. 오늘 시간을 얼마나 낼 수 있는지입니다.</p>
<h2>30분 — 01 코스</h2>
<p>점심시간이나 퇴근길에 들르기 좋습니다. 클렌징, 샴푸 2회, 컨디셔너, 음이온 드라이, 헤어 오일, 음료가 들어가고 긴 마사지는 없습니다.</p>
<h2>50분 — 02·03 코스</h2>
<p>가장 많이 선택하시는 길이입니다. 같은 시간이지만 방향이 다릅니다. 02는 두피 마사지 2회로 두피에 집중하고, 03은 한국 마스크팩과 리프팅 마사지, LED 광테라피로 얼굴에 집중합니다.</p>
<h2>75분 — 파라다이스 리추얼</h2>
<p>두피와 얼굴을 함께 담은 14단계 시그니처 코스입니다. 여유 있는 날에 예약하시는 편이 좋습니다.</p>
<h2>코스 밖의 시간도 생각해 주십시오</h2>
<p>위 시간은 시술 시간입니다. 샴푸와 마스크를 고르고 머리가 가라앉기까지 5~10분을 더 보시면 됩니다. 같은 방문에 네일도 하실 경우 예약 때 말씀해 주십시오.</p>
<p>금액은 <a href="/ko/goi-dau/">헤드 스파 페이지</a>에 있습니다.</p>''',
 [('가장 짧은 코스는 몇 분인가요?','01 코스 30분, 6단계입니다.'),
  ('30분보다 짧은 코스가 있나요?','없습니다. 서두르지 않고 모든 단계를 하려면 30분이 최소입니다.')]),
('養生洗髮需要多少時間？',
 'VESSCA 有 30 分鐘、50 分鐘、50 分鐘與 75 分鐘四種。這裡說明如何依您實際能空出的時間選擇。',
 '養生洗髮需要多少時間？| VESSCA',
 '養生洗髮所需時間：30、50、75 分鐘套餐，以及依您能空出的時間選擇的建議。',
 ['養生洗髮時間','頭皮SPA多久','洗髮按摩時間'],
'''<p>這個問題背後通常還有另一個問題：今天能空出多少時間。</p>
<h2>30 分鐘 — 01 套餐</h2>
<p>適合午休或下班途中。包含卸妝潔面、洗髮兩次、護髮素、負離子吹乾、護髮油與飲品，沒有較長的按摩。</p>
<h2>50 分鐘 — 02 與 03 套餐</h2>
<p>最多人選擇的長度。時間相同但方向不同：02 以兩次頭部按摩專注頭皮，03 以韓國面膜、提拉按摩與 LED 光療專注臉部。</p>
<h2>75 分鐘 — 天堂儀式</h2>
<p>把頭皮與臉部都包含的 14 步驟招牌套餐，建議安排在真正有空的時段。</p>
<h2>別忘了套餐以外的時間</h2>
<p>上面是實際服務時間。挑選洗髮精與面膜、等頭髮定下來，另外再算 5 到 10 分鐘。同一次要做美甲請在預約時告知。</p>
<p>價格請見<a href="/zh/goi-dau/">養生洗髮頁面</a>。</p>''',
 [('最短的套餐是多少分鐘？','01 套餐 30 分鐘，共 6 個步驟。'),
  ('有 30 分鐘以下的套餐嗎？','沒有。要不趕時間地完成所有步驟，30 分鐘是最短。')]))

# ---------------------------------------------------------------- 5
bai('goi-dau-duong-sinh-co-giam-dau-dau-khong', T(4), C,
A(('head massage temples relax spa','Massage đầu và vùng cổ vai gáy',
   'A head and shoulder massage','두피와 어깨 마사지','頭部與肩頸按摩'),[]),
('Gội đầu dưỡng sinh có giảm đau đầu không?',
 'Với cơn đau đầu do căng cơ cổ vai gáy thì massage đầu thường giúp dễ chịu hơn. Với các loại đau đầu khác thì không, và bài này nói rõ ranh giới đó.',
 'Gội đầu dưỡng sinh có giảm đau đầu không?',
 'Gội đầu dưỡng sinh và đau đầu: giúp được với đau do căng cơ cổ vai gáy, không thay thế điều trị y tế. Khi nào nên đi khám thay vì đi gội.',
 ['gội đầu dưỡng sinh có giảm đau đầu không','massage đầu giảm đau đầu','gội đầu dưỡng sinh đau vai gáy'],
'''<p>Câu trả lời phụ thuộc vào nguyên nhân cơn đau. VESSCA không phải cơ sở y tế, nên chỗ nào giúp được thì nói giúp được, chỗ nào không thì nói không.</p>
<h2>Trường hợp thường dễ chịu hơn</h2>
<p>Đau đầu do căng cơ là loại phổ biến nhất ở người làm việc máy tính: cảm giác siết quanh đầu, nặng vùng sau cổ, lan xuống vai. Massage đầu cùng cổ vai gáy làm giãn nhóm cơ đang căng, nên nhiều khách thấy nhẹ hơn ngay sau buổi. Phần nằm yên không điện thoại cũng góp phần.</p>
<h2>Trường hợp không giúp được</h2>
<ul>
<li>Đau nửa đầu migraine. Lúc đang lên cơn, áp lực lên đầu và mùi tinh dầu có thể làm nặng thêm.</li>
<li>Đau đầu do xoang, do huyết áp, do thuốc.</li>
<li>Đau đầu kèm sốt, nôn, mờ mắt, yếu một bên người. Đây là dấu hiệu cần đi khám ngay, không phải đi gội đầu.</li>
<li>Đau đầu mới xuất hiện, dữ dội chưa từng có.</li>
</ul>
<h2>Nếu bạn vẫn muốn thử</h2>
<p>Nói trước với kỹ thuật viên rằng bạn đang hay đau đầu. Tiệm sẽ giảm lực massage, tránh ấn mạnh vùng thái dương, và chọn dầu gội ít mùi. Gói 02 với massage đầu hai lần, hoặc ghép mục massage đầu cùng cổ vai gáy 89.000₫ vào gói 01, là hướng hợp lý hơn gói nhiều bước về da mặt.</p>
<h2>Giới hạn cần nhớ</h2>
<p>Một buổi massage làm dịu triệu chứng trong ngày, không xử lý nguyên nhân. Nếu đau đầu lặp lại nhiều lần mỗi tuần, nguyên nhân thường là tư thế ngồi, màn hình, giấc ngủ hoặc một vấn đề sức khoẻ cần bác sĩ xem. Đi gội đầu để dễ chịu là hợp lý; thay thế việc khám bệnh thì không.</p>
<p>Chi tiết các gói ở trang <a href="/goi-dau/">Gội đầu dưỡng sinh</a>, và bài <a href="/blog/goi-dau-massage-co-vai-gay-binh-thanh/">gội đầu massage cổ vai gáy</a> nói riêng về phần vai.</p>''',
 [('Đang đau đầu có nên đi gội không?','Nếu là đau do căng cơ, thường dễ chịu hơn. Nếu đang lên cơn migraine hoặc đau kèm sốt, nôn, mờ mắt thì nên đi khám.'),
  ('Massage mạnh có tốt hơn không?','Không. Với người hay đau đầu, lực nhẹ và đều tốt hơn lực mạnh. Bạn nói trước để kỹ thuật viên điều chỉnh.')]),
('Does a Head Spa Help With Headaches?',
 'For tension headaches from a tight neck and shoulders, a head massage often eases things. For other kinds it does not, and the line matters.',
 'Does a Head Spa Help With Headaches? | VESSCA',
 'Head spa and headaches: it can ease tension-type pain from neck and shoulder tightness, but it does not replace medical care.',
 ['head spa headache','scalp massage tension headache','head massage for headache'],
'''<p>It depends on the cause. VESSCA is not a medical clinic, so here is the honest line.</p>
<h2>When it usually helps</h2>
<p>Tension headaches are the common kind among people who work at screens: a band of pressure around the head, heaviness behind the neck, spreading to the shoulders. A head with neck and shoulder massage releases those muscles, and many guests feel lighter straight after. Lying still without a phone helps too.</p>
<h2>When it does not</h2>
<ul>
<li>Migraine. During an attack, pressure on the head and scented products can make it worse.</li>
<li>Sinus, blood-pressure or medication-related headaches.</li>
<li>Headache with fever, vomiting, blurred vision or weakness on one side. That needs a doctor now.</li>
<li>A sudden, severe headache unlike any before.</li>
</ul>
<h2>If you still want to try</h2>
<p>Tell the technician you get headaches. Pressure is reduced, the temples are left alone, and a low-scent shampoo is used. Package 02, or adding the head with neck and shoulder massage to package 01, suits this better than a face-focused package.</p>
<p>Details on the <a href="/en/goi-dau/">head spa page</a>.</p>''',
 [('Should I come while a headache is active?','If it is tension-type, usually yes. During a migraine, or with fever or vision changes, see a doctor instead.'),
  ('Is firmer pressure better?','No. For headache-prone guests, light and steady works better. Say so beforehand.')]),
('헤드 스파가 두통에 도움이 되나요?',
 '목과 어깨가 굳어 생긴 긴장성 두통에는 두피 마사지가 도움이 되는 편입니다. 다른 종류의 두통에는 그렇지 않습니다.',
 '헤드 스파와 두통 | VESSCA 빈탄',
 '헤드 스파와 두통: 목·어깨 긴장으로 인한 두통에는 도움이 될 수 있지만 진료를 대신하지는 않습니다.',
 ['헤드 스파 두통','두피 마사지 두통','긴장성 두통 마사지'],
'''<p>원인에 따라 다릅니다. VESSCA는 의료기관이 아니므로 가능한 것과 아닌 것을 그대로 적습니다.</p>
<h2>도움이 되는 경우</h2>
<p>모니터를 오래 보는 분에게 흔한 긴장성 두통입니다. 머리를 띠처럼 조이는 느낌, 뒷목이 무겁고 어깨까지 이어지는 통증입니다. 두피·목·어깨 마사지로 굳은 근육이 풀리면 직후에 가벼워졌다고 하시는 분이 많습니다.</p>
<h2>도움이 되지 않는 경우</h2>
<ul>
<li>편두통. 발작 중에는 압력과 향이 오히려 부담이 됩니다.</li>
<li>부비동, 혈압, 약물로 인한 두통.</li>
<li>열, 구토, 시야 흐림, 한쪽 마비가 함께 있는 두통. 바로 진료가 필요합니다.</li>
<li>처음 겪는 갑작스럽고 심한 두통.</li>
</ul>
<h2>그래도 받아 보고 싶다면</h2>
<p>두통이 잦다고 미리 말씀해 주십시오. 압을 낮추고 관자놀이는 누르지 않으며 향이 약한 샴푸를 씁니다. 얼굴 중심 코스보다 02 코스, 또는 01 코스에 두피·목·어깨 마사지를 더하는 편이 맞습니다.</p>
<p>자세한 내용은 <a href="/ko/goi-dau/">헤드 스파 페이지</a>에 있습니다.</p>''',
 [('두통이 있는 상태로 가도 되나요?','긴장성이라면 대체로 괜찮습니다. 편두통 발작 중이거나 열·시야 이상이 있으면 진료를 먼저 받으십시오.'),
  ('세게 받는 편이 좋은가요?','아닙니다. 두통이 잦은 분은 약하고 일정한 압이 낫습니다.')]),
('養生洗髮能緩解頭痛嗎？',
 '若是肩頸緊繃造成的緊張型頭痛，頭部按摩通常會舒服一些。其他類型的頭痛則不然。',
 '養生洗髮能緩解頭痛嗎？| VESSCA',
 '養生洗髮與頭痛：對肩頸緊繃引起的頭痛可能有幫助，但不能取代醫療。',
 ['養生洗髮頭痛','頭皮按摩頭痛','緊張型頭痛按摩'],
'''<p>要看原因。VESSCA 不是醫療機構，所以把能與不能說清楚。</p>
<h2>通常有幫助的情況</h2>
<p>長時間看螢幕的人最常見的是緊張型頭痛：頭部像被束緊、後頸沉重、延伸到肩膀。頭部及肩頸按摩讓緊繃的肌肉放鬆，許多顧客結束後覺得輕了一些。躺著不看手機也有作用。</p>
<h2>沒有幫助的情況</h2>
<ul>
<li>偏頭痛。發作時按壓與香氣可能讓情況更糟。</li>
<li>鼻竇、血壓或藥物引起的頭痛。</li>
<li>伴隨發燒、嘔吐、視力模糊或單側無力的頭痛，需要立刻就醫。</li>
<li>從未有過的突發劇烈頭痛。</li>
</ul>
<h2>若仍想嘗試</h2>
<p>請先告知您常頭痛。我們會減輕力道、避開太陽穴，並使用氣味較淡的洗髮精。比起以臉部為主的套餐，02 套餐或在 01 套餐加上頭部及肩頸按摩更合適。</p>
<p>詳細內容請見<a href="/zh/goi-dau/">養生洗髮頁面</a>。</p>''',
 [('頭痛的時候可以來嗎？','若是緊張型通常可以。偏頭痛發作中，或伴隨發燒、視力變化，請先就醫。'),
  ('力道重一點比較好嗎？','不是。常頭痛的人適合輕而穩定的力道。')]))

# ---------------------------------------------------------------- 6
bai('goi-dau-duong-sinh-khac-goi-dau-thuong', T(5), C,
A(('salon hair wash chair comparison','So sánh gội đầu dưỡng sinh và gội đầu thường',
   'Comparing a head spa with an ordinary wash','일반 샴푸와 헤드 스파 비교','養生洗髮與一般洗髮的差別'),[]),
('Gội đầu dưỡng sinh khác gội đầu thường thế nào?',
 'Khác ở bốn chỗ: thời lượng, số bước, phần massage và cách sấy. Hiểu rõ bốn chỗ này thì bạn biết khi nào nên chọn loại nào.',
 'Gội đầu dưỡng sinh khác gội đầu thường ở đâu?',
 'So sánh gội đầu dưỡng sinh và gội đầu thường: khác nhau về thời lượng, số bước, massage và cách sấy tóc. Khi nào nên chọn loại nào.',
 ['gội đầu dưỡng sinh khác gội đầu thường','so sánh gội đầu dưỡng sinh','gội đầu thường và gội đầu dưỡng sinh'],
'''<p>Hai dịch vụ cùng bắt đầu bằng việc làm ướt tóc, nhưng sau đó đi hai đường khác nhau.</p>
<h2>Thời lượng</h2>
<p>Gội đầu thường ở tiệm tóc mất 10 tới 20 phút, thường là bước đệm trước khi cắt hoặc uốn. Gội đầu dưỡng sinh là dịch vụ độc lập, ngắn nhất 30 phút, dài nhất 75 phút.</p>
<h2>Số bước</h2>
<p>Gội thường: làm ướt, gội, xả, sấy. Gói 30 phút của VESSCA đã có sáu bước, kể cả tẩy trang rửa mặt và dầu dưỡng tóc. Các gói dài hơn có tẩy tế bào chết da đầu, mặt nạ, massage và dưỡng da tay.</p>
<h2>Phần massage</h2>
<p>Đây là khác biệt lớn nhất. Gội thường có xoa bóp vài chục giây trong lúc tạo bọt. Gói 02 có massage đầu hai lần, một lần trước khi gội và một lần sau khi xả. Gói thiên đường còn có massage đầu cùng cổ vai gáy.</p>
<h2>Cách sấy</h2>
<p>Gội thường hay sấy nhanh bằng hơi nóng cho kịp bước sau. Ở đây sấy bằng máy sấy ion âm, chậm hơn nhưng tóc đỡ khô xơ, rồi thêm dầu dưỡng L’Oréal.</p>
<h2>Khi nào chọn loại nào</h2>
<ul>
<li>Cần tóc sạch trước khi cắt hoặc đi đâu gấp: gội thường ở tiệm tóc là đủ.</li>
<li>Da đầu bết nhanh, nhiều dầu, muốn làm sạch sâu: gói 01 trở lên.</li>
<li>Mỏi cổ vai, cần nghỉ thật: gói 02 hoặc gói 04.</li>
<li>Đi tiệc, muốn cả da mặt: gói 03.</li>
</ul>
<p>Bảng giá và các bước ở trang <a href="/goi-dau/">Gội đầu dưỡng sinh</a>. Bài <a href="/blog/head-spa-la-gi/">head spa là gì</a> giải thích tên gọi theo cách người Hàn và người Nhật dùng.</p>''',
 [('Gội đầu dưỡng sinh có cắt tóc không?','Không. VESSCA không làm tóc, chỉ gội, massage và chăm da đầu, da mặt.'),
  ('Gội thường ở đây giá bao nhiêu?','Mốc thấp nhất là gói 01, 30 phút, từ 99.000₫. Tiệm không có dịch vụ gội nhanh dưới 30 phút.')]),
('Head Spa vs an Ordinary Hair Wash',
 'Four differences: length, number of steps, the massage, and how the hair is dried. Knowing them tells you which to book.',
 'Head Spa vs Ordinary Hair Wash | VESSCA',
 'Head spa compared with an ordinary salon wash: length, steps, massage and drying method, plus when to choose each.',
 ['head spa vs hair wash','difference head spa','korean head spa explained'],
'''<p>Both start by wetting the hair, then go separate ways.</p>
<h2>Length</h2>
<p>An ordinary wash at a hair salon takes 10 to 20 minutes and usually precedes a cut. A head spa is its own service: 30 minutes at the shortest, 75 at the longest.</p>
<h2>Steps</h2>
<p>An ordinary wash is wet, shampoo, rinse, dry. The 30-minute package here already has six steps including a face cleanse and hair oil. Longer packages add scalp exfoliation, masks, massage and hand care.</p>
<h2>The massage</h2>
<p>The biggest difference. An ordinary wash includes a few seconds of rubbing while lathering. Package 02 has two full head massages, before the wash and after the conditioner. The Paradise Ritual adds neck and shoulders.</p>
<h2>Drying</h2>
<p>Ordinary washes are blasted dry with heat to keep the chair moving. Here a negative-ion dryer is used, slower but gentler, followed by L’Oréal hair oil.</p>
<h2>Which to choose</h2>
<ul><li>Clean hair before a cut or an event: an ordinary wash is enough.</li><li>Oily scalp, want a deep clean: package 01 and up.</li><li>Tight neck and shoulders: package 02 or 04.</li><li>Going out, want facial care too: package 03.</li></ul>
<p>Prices on the <a href="/en/goi-dau/">head spa page</a>.</p>''',
 [('Do you cut hair?','No. VESSCA does washing, massage, scalp and facial care only.'),
  ('Is there a quick wash option?','No. The shortest is the 30-minute package from 99,000₫.')]),
('헤드 스파와 일반 샴푸의 차이',
 '차이는 네 가지입니다. 시간, 단계 수, 마사지, 그리고 말리는 방식입니다.',
 '헤드 스파와 일반 샴푸의 차이 | VESSCA',
 '헤드 스파와 일반 샴푸 비교: 시간, 단계, 마사지, 드라이 방식의 차이와 선택 기준.',
 ['헤드 스파 차이','일반 샴푸 비교','한국식 헤드 스파'],
'''<p>둘 다 머리를 적시는 것으로 시작하지만 그 뒤가 다릅니다.</p>
<h2>시간</h2>
<p>미용실의 일반 샴푸는 10~20분이고 보통 커트 전 단계입니다. 헤드 스파는 독립된 서비스로 짧게 30분, 길게 75분입니다.</p>
<h2>단계 수</h2>
<p>일반 샴푸는 적시고 감고 헹구고 말립니다. 여기 30분 코스는 세안과 헤어 오일까지 6단계이고, 긴 코스에는 두피 스케일링, 마스크, 마사지, 핸드 케어가 더해집니다.</p>
<h2>마사지</h2>
<p>가장 큰 차이입니다. 일반 샴푸는 거품을 낼 때 몇 초 문지르는 정도입니다. 02 코스는 샴푸 전과 컨디셔너 후에 두피 마사지를 두 번 하고, 파라다이스 리추얼은 목과 어깨까지 포함합니다.</p>
<h2>드라이</h2>
<p>일반 샴푸는 다음 순서를 위해 뜨거운 바람으로 빨리 말립니다. 여기서는 음이온 드라이어로 천천히 말리고 로레알 헤어 오일을 바릅니다.</p>
<p>금액은 <a href="/ko/goi-dau/">헤드 스파 페이지</a>에 있습니다.</p>''',
 [('커트도 하나요?','하지 않습니다. VESSCA는 샴푸와 마사지, 두피·얼굴 케어만 합니다.'),
  ('빠른 샴푸만 받을 수 있나요?','없습니다. 가장 짧은 것이 99,000₫부터 시작하는 30분 코스입니다.')]),
('養生洗髮與一般洗髮的差別',
 '差別有四處：時間、步驟數、按摩，以及吹乾的方式。',
 '養生洗髮與一般洗髮的差別 | VESSCA',
 '養生洗髮與一般洗髮比較：時間、步驟、按摩與吹乾方式的差異，以及如何選擇。',
 ['養生洗髮差別','一般洗髮比較','韓式頭皮SPA'],
'''<p>兩者都從濕髮開始，之後就分道了。</p>
<h2>時間</h2>
<p>美髮店的一般洗髮約 10 到 20 分鐘，多是剪髮前的步驟。養生洗髮是獨立服務，最短 30 分鐘，最長 75 分鐘。</p>
<h2>步驟數</h2>
<p>一般洗髮是弄濕、洗、沖、吹。這裡的 30 分鐘套餐已有六個步驟，含潔面與護髮油。較長的套餐再加上頭皮去角質、面膜、按摩與手部保養。</p>
<h2>按摩</h2>
<p>最大的差別。一般洗髮只在起泡時搓幾秒。02 套餐在洗髮前與護髮素後各做一次完整頭部按摩，天堂儀式還包含肩頸。</p>
<h2>吹乾</h2>
<p>一般洗髮為了趕下一位客人會用熱風快速吹乾。這裡使用負離子吹風機，慢一些但較不傷髮，之後再上 L’Oréal 護髮油。</p>
<p>價格請見<a href="/zh/goi-dau/">養生洗髮頁面</a>。</p>''',
 [('有剪髮服務嗎？','沒有。VESSCA 只做洗髮、按摩與頭皮臉部保養。'),
  ('可以只洗快的嗎？','沒有。最短是 99,000₫ 起的 30 分鐘套餐。')]))

# ---------------------------------------------------------------- 7
bai('goi-dau-duong-sinh-co-can-coi-ao-khong', T(6), C,
A(('woman lying salon hair wash bed','Khách nằm gội tại giường gội',
   'A guest lying on the wash bed','샴푸 베드에 누운 고객','顧客躺在洗髮床上'),[]),
('Gội đầu dưỡng sinh có cần cởi áo không?',
 'Không cần. Mọi bước trong bốn gói của VESSCA chỉ làm ở đầu, mặt, cổ vai gáy và tay, nên bạn giữ nguyên trang phục.',
 'Gội đầu dưỡng sinh có cần cởi áo không?',
 'Gội đầu dưỡng sinh có phải cởi áo không: không cần. Các bước chỉ làm ở đầu, mặt, cổ vai gáy và tay, bạn giữ nguyên trang phục.',
 ['gội đầu dưỡng sinh có cần cởi áo không','gội đầu dưỡng sinh mặc gì','đi gội đầu dưỡng sinh cần chuẩn bị gì'],
'''<p>Đây là lo lắng thường thấy của người đi lần đầu, nhất là khi đọc thấy chữ dưỡng sinh và tưởng là một liệu trình toàn thân. Câu trả lời ngắn: không cần cởi áo.</p>
<h2>Vì sao không cần</h2>
<p>Nhìn vào danh sách bước của cả bốn gói sẽ thấy mọi thao tác đều nằm ở bốn vùng: đầu và da đầu, mặt, cổ vai gáy, và bàn tay. Không có bước nào làm ở lưng, bụng hay chân. Bạn nằm trên giường gội, mặc nguyên bộ đang mặc.</p>
<h2>Nên mặc gì cho dễ chịu</h2>
<ul>
<li><b>Cổ áo rộng hoặc cổ tròn thấp</b> dễ hơn cổ cao, vì phần cổ vai gáy được massage.</li>
<li><b>Áo không quá dày ở vai</b> giúp kỹ thuật viên ấn đúng vùng vai.</li>
<li><b>Tóc không buộc chặt</b>, không gôm nhiều thì bước đầu nhanh hơn. Dù vậy tóc đang bết hay vừa xịt gôm cũng không sao, đó là việc của buổi gội.</li>
<li>Bỏ tai nghe, kẹp tóc kim loại và trang sức ở cổ trước khi nằm.</li>
</ul>
<h2>Áo có bị ướt không</h2>
<p>Bạn sẽ được choàng khăn và áo choàng trước khi gội. Phần cổ áo có thể hơi ẩm nếu áo cổ cao, đó là lý do nên chọn cổ rộng. Nếu bạn vừa tới từ chỗ làm và mặc áo sơ mi quan trọng, nói với kỹ thuật viên để họ che kỹ hơn.</p>
<h2>Trang điểm thì sao</h2>
<p>Không cần tẩy trang trước khi tới. Cả bốn gói đều bắt đầu bằng bước tẩy trang Garnier và rửa mặt SVR, nên lớp trang điểm được xử lý ngay tại tiệm. Nếu bạn còn hẹn ngay sau buổi gội thì nên mang theo đồ trang điểm để dặm lại, vì mặt sẽ được làm sạch.</p>
<p>Các bước đầy đủ của từng gói có ở trang <a href="/goi-dau/">Gội đầu dưỡng sinh</a>.</p>''',
 [('Có phòng riêng không?','Khu gội được bố trí để bạn nằm yên tĩnh. Nếu cần sự riêng tư nhiều hơn, bạn nói khi đặt lịch để tiệm xếp giờ vắng khách.'),
  ('Nam giới tới có bất tiện gì không?','Không. Các bước giống nhau cho mọi khách và không yêu cầu cởi áo. Bài riêng về nội dung này là gội đầu dưỡng sinh cho nam.'),
  ('Có cần mang theo gì không?','Không cần. Nếu bạn có hẹn ngay sau đó thì mang đồ trang điểm để dặm lại.')]),
('Do I Need to Undress for a Head Spa?',
 'No. Every step in the four VESSCA packages is on the head, face, neck and shoulders, or hands, so you stay in your own clothes.',
 'Do I Need to Undress for a Head Spa? | VESSCA',
 'No undressing is needed for a head spa: every step works on the head, face, neck, shoulders and hands. What to wear for comfort.',
 ['head spa undress','what to wear head spa','first head spa what to expect'],
'''<p>A common worry for first-timers. The short answer is no.</p>
<h2>Why not</h2>
<p>Looking at the step list for all four packages, every action happens in four areas: head and scalp, face, neck and shoulders, and hands. Nothing involves the back, torso or legs. You lie on the wash bed in what you arrived in.</p>
<h2>What to wear for comfort</h2>
<ul><li>A wide or low round neckline is easier than a high collar, since the neck and shoulders are massaged.</li><li>Nothing too padded at the shoulders.</li><li>Hair loose rather than tightly tied. Unwashed hair or hairspray is fine either way.</li><li>Remove earphones, metal clips and necklaces before lying down.</li></ul>
<h2>Will my top get wet</h2>
<p>You are given towels and a cape before the wash. A high collar can still get slightly damp, which is why a wider neckline is better. Coming straight from work in a shirt you care about, say so and the staff will cover more carefully.</p>
<h2>Make-up</h2>
<p>No need to remove it beforehand. All four packages begin with Garnier make-up removal and an SVR face cleanse. If you have plans right after, bring what you need to touch up.</p>
<p>Full step lists on the <a href="/en/goi-dau/">head spa page</a>.</p>''',
 [('Is there a private room?','The wash area is arranged so you can lie quietly. If you want more privacy, mention it when booking and a quieter time can be arranged.'),
  ('Do I need to bring anything?','No. Bring make-up only if you have plans straight afterwards.')]),
('헤드 스파를 받을 때 옷을 벗어야 하나요?',
 '그러지 않습니다. VESSCA 네 코스의 모든 단계는 머리, 얼굴, 목·어깨, 손에서만 진행되므로 입고 오신 옷 그대로 받으십니다.',
 '헤드 스파에 옷을 벗어야 하나요? | VESSCA',
 '헤드 스파는 옷을 벗지 않습니다. 모든 단계가 머리, 얼굴, 목·어깨, 손에서 진행됩니다. 편한 옷차림 안내.',
 ['헤드 스파 복장','헤드 스파 처음','헤드 스파 준비물'],
'''<p>처음 오시는 분이 자주 걱정하시는 부분입니다. 답은 간단합니다. 벗지 않습니다.</p>
<h2>이유</h2>
<p>네 코스의 단계를 보면 모든 작업이 네 곳에서만 이루어집니다. 머리와 두피, 얼굴, 목과 어깨, 그리고 손입니다. 등이나 몸통, 다리를 다루는 단계는 없습니다.</p>
<h2>편한 옷차림</h2>
<ul><li>목·어깨를 마사지하므로 목이 넓게 트인 옷이 편합니다.</li><li>어깨에 패드가 두껍지 않은 옷이 좋습니다.</li><li>머리는 묶지 않은 상태가 편합니다. 감지 않았거나 스프레이를 뿌린 상태도 괜찮습니다.</li><li>누우시기 전에 이어폰, 금속 핀, 목걸이는 빼 주십시오.</li></ul>
<h2>옷이 젖지 않을까요</h2>
<p>샴푸 전에 수건과 가운을 둘러 드립니다. 목이 높은 옷은 약간 축축해질 수 있어 넓은 목선을 권합니다. 중요한 셔츠를 입고 오셨다면 말씀해 주십시오.</p>
<h2>화장은요</h2>
<p>미리 지우지 않아도 됩니다. 네 코스 모두 가르니에 클렌징과 SVR 세안으로 시작합니다. 바로 다음 일정이 있으면 수정 화장 도구를 챙겨 오십시오.</p>
<p>단계는 <a href="/ko/goi-dau/">헤드 스파 페이지</a>에 있습니다.</p>''',
 [('개인실이 있나요?','조용히 누워 계실 수 있도록 공간을 배치했습니다. 더 조용한 시간을 원하시면 예약 때 말씀해 주십시오.'),
  ('무엇을 가져가야 하나요?','따로 없습니다. 이후 일정이 있으면 화장품만 챙기십시오.')]),
('做養生洗髮需要脫衣服嗎？',
 '不需要。VESSCA 四個套餐的所有步驟都在頭部、臉部、肩頸與手部進行，您穿著原本的衣服即可。',
 '做養生洗髮需要脫衣服嗎？| VESSCA',
 '養生洗髮不需要脫衣服：所有步驟都在頭部、臉部、肩頸與手部進行。另附穿著建議。',
 ['養生洗髮穿什麼','頭皮SPA第一次','養生洗髮要帶什麼'],
'''<p>第一次來的人常有的疑慮。答案很簡單：不需要。</p>
<h2>原因</h2>
<p>看四個套餐的步驟就知道，所有動作只在四個部位：頭部與頭皮、臉部、肩頸、手部。沒有任何步驟涉及背部、身體或腿部。</p>
<h2>怎麼穿比較舒服</h2>
<ul><li>因為會按摩肩頸，領口寬鬆的上衣比高領舒服。</li><li>肩部不要太厚的墊肩。</li><li>頭髮不要綁太緊。沒洗或噴過定型液都沒關係。</li><li>躺下前請取下耳機、金屬髮夾與項鍊。</li></ul>
<h2>衣服會濕嗎</h2>
<p>洗髮前會為您圍上毛巾與罩衣。高領仍可能稍微潮濕，所以建議寬領口。若您剛下班、穿著重要的襯衫，請告知我們會加強遮蓋。</p>
<h2>化妝呢</h2>
<p>不需要事先卸妝。四個套餐都以 Garnier 卸妝與 SVR 潔面開始。如果結束後還有行程，請自行帶補妝用品。</p>
<p>步驟請見<a href="/zh/goi-dau/">養生洗髮頁面</a>。</p>''',
 [('有單獨包廂嗎？','洗髮區的安排讓您可以安靜地躺著。若需要更安靜的時段，請在預約時告知。'),
  ('需要帶什麼嗎？','不需要。若結束後有行程，帶補妝用品即可。')]))

# ---------------------------------------------------------------- 8
bai('goi-dau-duong-sinh-co-lay-ray-tai-khong', T(7), C,
A(('spa treatment towels tray clean','Khu gội đầu và dụng cụ tại tiệm',
   'The wash area and its tools','샴푸 공간과 도구','洗髮區與器具'),[]),
('Gội đầu dưỡng sinh có lấy ráy tai không?',
 'Tại VESSCA thì không. Bài này nói rõ vì sao tiệm không làm dịch vụ đó, và những gì có trong gói thay thế phần đó.',
 'Gội đầu dưỡng sinh có lấy ráy tai không?',
 'VESSCA không có dịch vụ lấy ráy tai trong gói gội đầu dưỡng sinh. Lý do, và những bước thực tế có trong bốn gói.',
 ['gội đầu dưỡng sinh có lấy ráy tai không','gội đầu lấy ráy tai','gội đầu dưỡng sinh có những gì'],
'''<p>Nhiều tiệm gội đầu ở Việt Nam gộp lấy ráy tai vào gói. VESSCA không làm dịch vụ này, và nên nói trước để bạn khỏi mất công tới.</p>
<h2>Vì sao tiệm không làm</h2>
<p>Lấy ráy tai bằng que ở tiệm là thao tác có rủi ro: dễ đẩy ráy vào sâu hơn, dễ xước ống tai, và dụng cụ dùng cho nhiều người là đường lây nhiễm nếu không tiệt trùng đúng cách. Khuyến nghị chung của giới y khoa là ống tai tự làm sạch, không cần can thiệp thường xuyên; ráy tai gây bít tắc, đau hay giảm nghe thì nên để bác sĩ tai mũi họng xử lý.</p>
<p>VESSCA chọn làm đúng phạm vi của mình là da đầu, tóc, da mặt và cơ cổ vai gáy, thay vì nhận thêm một việc cần chuyên môn y tế.</p>
<h2>Trong gói có những gì</h2>
<p>Thay cho phần đó, bốn gói tập trung vào các bước sau:</p>
<ul>
<li>Tẩy trang và rửa mặt trước khi gội</li>
<li>Tẩy tế bào chết da đầu, gội hai lần, xả dầu xả</li>
<li>Massage đầu, hoặc massage đầu cùng cổ vai gáy</li>
<li>Mặt nạ Hàn Quốc, massage mặt, chiếu đèn ánh sáng sinh học ở các gói có phần da mặt</li>
<li>Sấy bằng máy sấy ion âm, dầu dưỡng tóc L’Oréal, dưỡng da tay</li>
</ul>
<h2>Nếu bạn vẫn muốn dịch vụ đó</h2>
<p>Nên tới phòng khám tai mũi họng. Việc này được làm có đèn soi và dụng cụ tiệt trùng, an toàn hơn hẳn làm ở tiệm. Sau đó bạn vẫn có thể đi gội đầu bình thường.</p>
<p>Danh sách bước đầy đủ ở trang <a href="/goi-dau/">Gội đầu dưỡng sinh</a>.</p>''',
 [('Có massage tai hay vùng quanh tai không?','Vùng sau tai và chân tóc được làm sạch khi gội, và phần massage đầu đi qua vùng quanh tai. Nhưng không có thao tác đưa dụng cụ vào ống tai.'),
  ('Nước có vào tai khi gội không?','Kỹ thuật viên nghiêng đầu và che tai khi xả. Nếu bạn dễ bị nước vào tai thì nói trước.')]),
('Does a Head Spa Include Ear Cleaning?',
 'Not at VESSCA. Here is why the shop does not offer it, and what the four packages include instead.',
 'Does a Head Spa Include Ear Cleaning? | VESSCA',
 'VESSCA does not offer ear cleaning with its head spa packages. The reason, and what the four packages actually include.',
 ['head spa ear cleaning','ear cleaning salon vietnam','head spa included services'],
'''<p>Many hair-wash shops in Vietnam bundle ear cleaning into the service. VESSCA does not, and it is better to say so in advance.</p>
<h2>Why not</h2>
<p>Ear cleaning with a pick carries real risk: wax can be pushed deeper, the canal is easily scratched, and shared tools are an infection route unless sterilised properly. General medical advice is that the ear canal cleans itself; blockage, pain or hearing loss belongs with an ENT doctor.</p>
<p>VESSCA stays within its own scope: scalp, hair, facial skin, and the neck and shoulder muscles.</p>
<h2>What the packages include</h2>
<ul><li>Make-up removal and face cleanse before the wash</li><li>Scalp exfoliation, double shampoo, conditioner</li><li>Head massage, or head with neck and shoulder massage</li><li>Korean sheet mask, facial massage and LED therapy in the face-focused packages</li><li>Negative-ion blow-dry, L’Oréal hair oil, hand care</li></ul>
<h2>If you want it anyway</h2>
<p>See an ENT clinic, where it is done with proper light and sterilised instruments.</p>
<p>Full step lists on the <a href="/en/goi-dau/">head spa page</a>.</p>''',
 [('Is the area around the ears touched at all?','Behind the ears and the hairline are cleaned during the wash, and the head massage passes around the ears. Nothing enters the ear canal.'),
  ('Will water get in my ears?','The technician tilts your head and shields the ears while rinsing. Mention it beforehand if water bothers you.')]),
('헤드 스파에 귀 청소가 포함되나요?',
 'VESSCA에서는 하지 않습니다. 하지 않는 이유와, 네 코스에 실제로 포함되는 내용을 적었습니다.',
 '헤드 스파에 귀 청소가 포함되나요? | VESSCA',
 'VESSCA의 헤드 스파에는 귀 청소가 없습니다. 그 이유와 네 코스에 포함되는 단계를 안내합니다.',
 ['헤드 스파 귀청소','베트남 귀청소','헤드 스파 포함 내역'],
'''<p>베트남의 많은 샴푸 가게가 귀 청소를 코스에 넣습니다. VESSCA는 하지 않으므로 미리 알려 드립니다.</p>
<h2>하지 않는 이유</h2>
<p>도구로 귀를 파는 일은 위험이 따릅니다. 귀지가 더 깊이 밀려 들어가거나 외이도에 상처가 날 수 있고, 여러 사람이 쓰는 도구는 제대로 소독하지 않으면 감염 경로가 됩니다. 일반적인 의학 권고는 외이도가 스스로 청소된다는 것이며, 막힘이나 통증, 청력 저하는 이비인후과의 영역입니다.</p>
<h2>코스에 포함되는 것</h2>
<ul><li>샴푸 전 클렌징과 세안</li><li>두피 스케일링, 샴푸 2회, 컨디셔너</li><li>두피 마사지 또는 두피·목·어깨 마사지</li><li>얼굴 중심 코스의 한국 마스크팩, 페이셜 마사지, LED 광테라피</li><li>음이온 드라이, 로레알 헤어 오일, 핸드 케어</li></ul>
<p>단계 전체는 <a href="/ko/goi-dau/">헤드 스파 페이지</a>에 있습니다.</p>''',
 [('귀 주변은 전혀 만지지 않나요?','샴푸할 때 귀 뒤와 헤어라인을 닦고, 두피 마사지가 귀 주변을 지나갑니다. 외이도 안으로는 들어가지 않습니다.'),
  ('귀에 물이 들어가지 않을까요?','헹굴 때 고개를 기울이고 귀를 가립니다. 걱정되시면 미리 말씀해 주십시오.')]),
('養生洗髮有附挖耳朵嗎？',
 'VESSCA 沒有這項服務。這裡說明不做的原因，以及四個套餐實際包含的內容。',
 '養生洗髮有附挖耳朵嗎？| VESSCA',
 'VESSCA 的養生洗髮不含挖耳朵服務。說明原因，以及四個套餐實際包含的步驟。',
 ['養生洗髮挖耳','越南采耳','養生洗髮包含'],
'''<p>越南許多洗髮店會把挖耳朵併入套餐。VESSCA 不做這項服務，先說清楚比較好。</p>
<h2>不做的原因</h2>
<p>用器具挖耳有實際風險：耳垢可能被推得更深、外耳道容易刮傷，共用器具若未妥善消毒則是感染途徑。一般醫學建議認為外耳道會自行清潔；若有阻塞、疼痛或聽力下降，應由耳鼻喉科處理。</p>
<h2>套餐包含什麼</h2>
<ul><li>洗髮前的卸妝與潔面</li><li>頭皮去角質、洗髮兩次、護髮素</li><li>頭部按摩，或頭部及肩頸按摩</li><li>臉部套餐中的韓國面膜、臉部按摩與 LED 光療</li><li>負離子吹乾、L’Oréal 護髮油、手部保養</li></ul>
<p>完整步驟請見<a href="/zh/goi-dau/">養生洗髮頁面</a>。</p>''',
 [('耳朵周圍完全不碰嗎？','洗髮時會清到耳後與髮際線，頭部按摩也會經過耳朵周圍，但不會進入耳道。'),
  ('洗頭時水會進耳朵嗎？','沖水時會側頭並遮住耳朵。若您擔心，請事先告知。')]))

# ---------------------------------------------------------------- 9
bai('goi-dau-duong-sinh-gia-re-binh-thanh', T(8), C,
A(('affordable salon hair wash service','Gói gội đầu 30 phút tại tiệm',
   'The 30-minute hair wash package','30분 헤어 워시 코스','30 分鐘洗髮套餐'),[]),
('Gội đầu dưỡng sinh giá rẻ ở Bình Thạnh: nên nhìn vào đâu',
 'Rẻ mà đáng tiền phụ thuộc vào số bước thật trong gói, không chỉ con số trên bảng giá. Đây là cách so sánh cho đúng.',
 'Gội đầu dưỡng sinh giá rẻ Bình Thạnh — từ 99.000₫',
 'Gội đầu dưỡng sinh giá rẻ ở Bình Thạnh: gói 30 phút từ 99.000₫ tại VESSCA, và cách so sánh các gói rẻ cho đúng.',
 ['gội đầu dưỡng sinh giá rẻ bình thạnh','gội đầu bình thạnh giá rẻ','gội đầu rẻ bình thạnh','gội đầu dưỡng sinh giá rẻ'],
'''<p>Tìm gói rẻ là chuyện hợp lý, nhất là khi muốn thử lần đầu. Nhưng hai gói cùng giá có thể rất khác nhau, nên đáng bỏ hai phút để so sánh cho đúng.</p>
<h2>Mức rẻ nhất tại VESSCA</h2>
<p>Gói 01, 30 phút, từ 99.000₫ với dầu gội thảo dược Nguyên Xuân. Trong đó có tẩy trang Garnier và rửa mặt SVR, gội hai lần, xả dầu xả, sấy bằng máy sấy ion âm, dầu dưỡng tóc L’Oréal, kèm nước uống và bánh ngọt.</p>
<h2>Ba câu nên hỏi trước khi chọn gói rẻ ở bất cứ đâu</h2>
<ol>
<li><b>Bao nhiêu phút?</b> Một gói 99.000₫ trong 30 phút khác một gói 99.000₫ trong 15 phút.</li>
<li><b>Gồm những bước nào?</b> Có xả dầu xả không, có sấy không, hay chỉ gội rồi lau khăn.</li>
<li><b>Giá đó là giá cuối chưa?</b> Nhiều chỗ báo giá gốc rồi cộng thêm từng mục nhỏ.</li>
</ol>
<h2>Cách tiết kiệm mà vẫn đủ</h2>
<ul>
<li>Chọn dòng dầu gội ở mức thấp. Cả ba dòng đều gội hai lần và xả như nhau, chỉ khác sản phẩm.</li>
<li>Chọn gói 01 rồi ghép thêm đúng một mục bạn cần, ví dụ massage đầu cùng cổ vai gáy 89.000₫, thay vì mua luôn gói dài.</li>
<li>Không mua mặt nạ nâng cơ nếu chưa cần, vì mục đó cộng thêm 30.000₫. Ba loại mặt nạ còn lại đã nằm trong gói.</li>
</ul>
<h2>Khi nào không nên tiết kiệm</h2>
<p>Nếu lý do bạn đi là mỏi cổ vai thì gói 30 phút sẽ không giải quyết, vì gói đó không có phần massage dài. Trong trường hợp này mua gói 02 đúng hơn là mua gói rẻ rồi thấy chưa đủ.</p>
<p>Bảng giá bốn gói và từng bước ở trang <a href="/goi-dau/">Gội đầu dưỡng sinh</a>. Bài <a href="/blog/goi-dau-duong-sinh-gia-bao-nhieu/">gội đầu dưỡng sinh giá bao nhiêu</a> ghi đủ các mức.</p>''',
 [('Gói 99.000₫ có bị cắt bước không?','Không. Gói đó đủ sáu bước, chỉ không có phần massage dài như các gói trên.'),
  ('Có giảm giá cho khách quen không?','Bạn hỏi trực tiếp tại tiệm hoặc khi đặt lịch, vì chương trình thay đổi theo thời điểm.'),
  ('Tiệm ở đâu?','251/30 Lê Quang Định, phường Gia Định, mở 9:00–20:30 mỗi ngày.')]),
('Affordable Head Spa in Binh Thanh: What to Compare',
 'Cheap and worth it depends on the number of real steps in the package, not only the price on the board.',
 'Affordable Head Spa in Binh Thanh — from 99,000₫',
 'Affordable head spa in Binh Thanh: the 30-minute package from 99,000₫ at VESSCA, and how to compare budget packages properly.',
 ['cheap head spa binh thanh','affordable head spa saigon','budget hair wash saigon'],
'''<p>Looking for the cheapest option is reasonable, especially for a first try. But two packages at the same price can differ a lot.</p>
<h2>The lowest rate at VESSCA</h2>
<p>Package 01, 30 minutes, from 99,000₫ with Nguyen Xuan herbal shampoo. It includes Garnier make-up removal and an SVR face cleanse, a double shampoo, conditioner, a negative-ion blow-dry, L’Oréal hair oil, and refreshments.</p>
<h2>Three questions to ask anywhere</h2>
<ol><li><b>How many minutes?</b> The same price over 30 minutes is not the same as over 15.</li><li><b>Which steps?</b> Is there conditioner, is there a blow-dry, or just a wash and a towel.</li><li><b>Is that the final price?</b> Some places quote a base and add items.</li></ol>
<h2>How to spend less and still get enough</h2>
<ul><li>Choose the lower shampoo line. All three get the same double wash and conditioner.</li><li>Take package 01 and add just the one thing you need, such as the 89,000₫ head with neck and shoulder massage.</li><li>Skip the lifting mask at 30,000₫ extra; the other three masks are included.</li></ul>
<h2>When not to economise</h2>
<p>If you are coming because your neck and shoulders ache, the 30-minute package will not solve it — there is no long massage in it. Package 02 is the right buy.</p>
<p>Full prices on the <a href="/en/goi-dau/">head spa page</a>.</p>''',
 [('Is the 99,000₫ package cut down?','No. It has all six steps; it simply has no long massage.'),
  ('Where is the shop?','251/30 Le Quang Dinh, Gia Dinh ward, open 9:00–20:30 daily.')]),
('빈탄에서 저렴한 헤드 스파, 무엇을 비교해야 할까',
 '저렴하면서 값어치가 있는지는 코스에 실제로 들어 있는 단계 수로 판단합니다. 가격표의 숫자만으로는 알 수 없습니다.',
 '빈탄 저렴한 헤드 스파 — 99,000₫부터 | VESSCA',
 '빈탄의 저렴한 헤드 스파: VESSCA 30분 코스 99,000₫부터, 그리고 저가 코스를 제대로 비교하는 방법.',
 ['빈탄 저렴한 헤드 스파','호치민 가성비 헤드 스파','저가 두피 스파'],
'''<p>처음 받아 볼 때 저렴한 코스를 찾는 것은 당연합니다. 다만 같은 금액이라도 내용이 크게 다를 수 있습니다.</p>
<h2>VESSCA의 가장 낮은 금액</h2>
<p>01 코스, 30분, Nguyen Xuan 허브 샴푸 선택 시 99,000₫. 가르니에 클렌징과 SVR 세안, 샴푸 2회, 컨디셔너, 음이온 드라이, 로레알 헤어 오일, 음료와 디저트가 들어갑니다.</p>
<h2>어디서든 물어볼 세 가지</h2>
<ol><li><b>몇 분인가요.</b> 같은 금액의 30분과 15분은 다릅니다.</li><li><b>어떤 단계가 들어가나요.</b> 컨디셔너와 드라이가 있는지 확인하십시오.</li><li><b>그 금액이 최종인가요.</b> 기본가만 안내하고 항목마다 더하는 곳도 있습니다.</li></ol>
<h2>덜 쓰면서도 충분하게</h2>
<ul><li>낮은 샴푸 라인을 고르십시오. 세 라인 모두 샴푸 2회와 컨디셔너는 같습니다.</li><li>01 코스에 필요한 한 가지만 추가하십시오. 두피·목·어깨 마사지 89,000₫ 등입니다.</li><li>리프팅 마스크(30,000₫ 추가)는 필요할 때만. 나머지 세 종류는 포함입니다.</li></ul>
<p>금액은 <a href="/ko/goi-dau/">헤드 스파 페이지</a>에 있습니다.</p>''',
 [('99,000₫ 코스는 축소판인가요?','아닙니다. 6단계가 모두 들어 있고 긴 마사지만 없습니다.'),
  ('매장 위치는요?','251/30 Lê Quang Định, Gia Định 동. 매일 9:00–20:30.')]),
('平盛郡平價養生洗髮：該比較什麼',
 '便宜又值得，取決於套餐裡實際有幾個步驟，而不只是價目表上的數字。',
 '平盛郡平價養生洗髮 — 99,000₫起 | VESSCA',
 '平盛郡平價養生洗髮：VESSCA 30 分鐘套餐 99,000₫起，以及正確比較平價套餐的方法。',
 ['平盛郡便宜洗髮','胡志明平價頭皮SPA','養生洗髮便宜'],
'''<p>第一次嘗試時想找便宜的選項很合理。但同樣價格的兩個套餐，內容可能差很多。</p>
<h2>VESSCA 的最低價</h2>
<p>01 套餐，30 分鐘，選擇 Nguyen Xuan 草本洗髮精為 99,000₫。包含 Garnier 卸妝與 SVR 潔面、洗髮兩次、護髮素、負離子吹乾、L’Oréal 護髮油，以及飲品與甜點。</p>
<h2>在任何店家都該問的三個問題</h2>
<ol><li><b>幾分鐘？</b>同樣價格的 30 分鐘與 15 分鐘不同。</li><li><b>包含哪些步驟？</b>有沒有護髮素、有沒有吹乾。</li><li><b>這是最終價格嗎？</b>有些店先報基本價再逐項加價。</li></ol>
<h2>怎麼省又不將就</h2>
<ul><li>選較低價的洗髮精。三款都是洗兩次並上護髮素。</li><li>選 01 套餐再只加一項您需要的，例如 89,000₫ 的頭部及肩頸按摩。</li><li>提拉面膜加 30,000₫，非必要可略過；其餘三款已含。</li></ul>
<p>價格請見<a href="/zh/goi-dau/">養生洗髮頁面</a>。</p>''',
 [('99,000₫ 的套餐有被簡化嗎？','沒有。六個步驟都在，只是沒有較長的按摩。'),
  ('店在哪裡？','251/30 Lê Quang Định，Gia Định 坊，每天 9:00–20:30。')]))

# ---------------------------------------------------------------- 10
bai('tiem-goi-dau-buoi-toi-binh-thanh', T(9), C,
A(('salon evening warm light interior','Khu gội đầu buổi tối tại tiệm',
   'The wash area in the evening','저녁 시간의 샴푸 공간','傍晚的洗髮區'),[]),
('Tiệm gội đầu buổi tối ở Bình Thạnh: giờ nào còn nhận khách',
 'VESSCA nhận khách tới 20:30 mỗi ngày. Bài này nói rõ khung giờ tối nào còn chỗ và nên chọn gói nào khi đi sau giờ làm.',
 'Gội đầu buổi tối ở Bình Thạnh — mở tới 20:30',
 'Tiệm gội đầu buổi tối ở Bình Thạnh: VESSCA mở 9:00–20:30 mỗi ngày, gần Phú Nhuận. Cách chọn gói khi đi sau giờ làm.',
 ['gội đầu buổi tối bình thạnh','gội đầu tối bình thạnh','tiệm gội đầu mở tối bình thạnh','gội đầu sau giờ làm'],
'''<p>Người tìm cụm này thường vừa tan làm và muốn ghé trên đường về. Nói thẳng trước để bạn không mất công: VESSCA mở 9:00 tới 20:30 mỗi ngày, không nhận khách sau 20:30 và không làm khuya.</p>
<h2>Khung giờ tối nên chọn</h2>
<ul>
<li><b>18:00 – 19:00:</b> khung dễ đặt nhất cho gói 50 phút, vẫn kịp xong trước giờ đóng.</li>
<li><b>19:00 – 19:30:</b> còn vừa cho gói 30 phút. Gói 50 hoặc 75 phút khung này thường không kịp.</li>
<li><b>Sau 19:30:</b> nên gọi trước số 0933.528.501 để biết còn nhận hay không.</li>
</ul>
<p>Vì tiệm giới hạn số khách mỗi khung giờ để không chồng ca, buổi tối thường kín trước. Đặt lịch sớm trong ngày là chắc nhất.</p>
<h2>Đi buổi tối thì chọn gói nào</h2>
<p>Nếu bạn đi sau một ngày ngồi máy tính, phần đáng tiền nhất là massage. Gói 02 với massage đầu hai lần hợp hơn gói 03 nghiêng về da mặt. Trường hợp chỉ còn 30 phút thì lấy gói 01 rồi ghép thêm massage đầu cùng cổ vai gáy 89.000₫.</p>
<h2>Một lưu ý về tóc ướt buổi tối</h2>
<p>Tóc được sấy bằng máy sấy ion âm trước khi bạn ra khỏi tiệm, nên không phải về nhà với tóc ướt. Nếu bạn đi xe máy thì nên đợi tóc nguội hẳn vài phút rồi hãy đội nón bảo hiểm, tóc đỡ bị ép và đỡ bết sáng sau.</p>
<h2>Vị trí</h2>
<p>251/30 Lê Quang Định, phường Gia Định. Từ phía Phú Nhuận hoặc Gò Vấp đi theo đường Lê Quang Định là tới, có chỗ gửi xe. Hướng dẫn chi tiết ở bài <a href="/blog/den-vessca-gui-xe-dat-lich/">đến VESSCA, gửi xe, đặt lịch</a>.</p>
<p>Bảng giá bốn gói ở trang <a href="/goi-dau/">Gội đầu dưỡng sinh</a>.</p>''',
 [('Tiệm có mở khuya không?','Không. Tiệm nhận khách tới 20:30 mỗi ngày.'),
  ('Buổi tối có cần đặt trước không?','Nên đặt. Tiệm giới hạn số khách mỗi khung giờ nên buổi tối thường kín trước.'),
  ('Cuối tuần có mở buổi tối không?','Có. Giờ mở cửa 9:00–20:30 áp dụng cả bảy ngày.')]),
('Evening Head Spa in Binh Thanh: Latest Booking Times',
 'VESSCA takes guests until 20:30 every day. Here are the evening slots that still work and which package to pick after work.',
 'Evening Head Spa in Binh Thanh — open till 20:30',
 'Evening head spa in Binh Thanh: VESSCA is open 9:00–20:30 daily, near Phu Nhuan. How to choose a package after work.',
 ['evening head spa binh thanh','late head spa saigon','head spa after work saigon'],
'''<p>People searching this have usually just finished work. Plainly: VESSCA is open 9:00 to 20:30 every day, takes no guests after 20:30, and does not run late nights.</p>
<h2>Which evening slot to take</h2>
<ul><li><b>18:00 – 19:00:</b> the easiest slot for a 50-minute package.</li><li><b>19:00 – 19:30:</b> still fine for the 30-minute package. Longer ones usually will not fit.</li><li><b>After 19:30:</b> call 0933 528 501 first.</li></ul>
<p>Guest numbers per slot are limited so appointments never overlap, which means evenings fill early. Book during the day.</p>
<h2>Which package suits an evening</h2>
<p>After a day at a screen, the massage is the part worth paying for. Package 02 with two head massages suits better than the face-focused 03. With only 30 minutes, take package 01 and add the 89,000₫ head with neck and shoulder massage.</p>
<h2>Wet hair in the evening</h2>
<p>Hair is dried with a negative-ion dryer before you leave. If you ride a motorbike, let it cool for a few minutes before putting on a helmet.</p>
<h2>Where</h2>
<p>251/30 Le Quang Dinh, Gia Dinh ward, with parking. Prices on the <a href="/en/goi-dau/">head spa page</a>.</p>''',
 [('Are you open late?','No. The shop takes guests until 20:30 daily.'),
  ('Do I need to book for the evening?','Yes, it is advisable. Slots are limited and evenings fill first.')]),
('빈탄의 저녁 헤드 스파: 몇 시까지 받나요',
 'VESSCA는 매일 20:30까지 손님을 받습니다. 저녁에 가능한 시간대와 퇴근 후에 맞는 코스를 적었습니다.',
 '빈탄 저녁 헤드 스파 — 20:30까지 | VESSCA',
 '빈탄의 저녁 헤드 스파: VESSCA는 매일 9:00–20:30 영업. 퇴근 후 코스 선택 안내.',
 ['빈탄 저녁 헤드 스파','호치민 늦은 시간 헤드 스파','퇴근 후 두피 스파'],
'''<p>이 검색을 하는 분은 대개 퇴근 직후입니다. 먼저 분명히 말씀드리면 VESSCA는 매일 9:00~20:30 영업이며 20:30 이후에는 받지 않습니다.</p>
<h2>저녁에 권하는 시간대</h2>
<ul><li><b>18:00~19:00:</b> 50분 코스를 넣기 가장 쉬운 시간입니다.</li><li><b>19:00~19:30:</b> 30분 코스는 가능합니다. 더 긴 코스는 어렵습니다.</li><li><b>19:30 이후:</b> 0933 528 501로 먼저 확인해 주십시오.</li></ul>
<p>예약이 겹치지 않도록 시간대별 인원을 제한하므로 저녁은 먼저 찹니다.</p>
<h2>저녁에 맞는 코스</h2>
<p>하루 종일 모니터를 본 뒤라면 마사지가 가장 값어치 있는 부분입니다. 두피 마사지 2회가 있는 02 코스가 얼굴 중심의 03 코스보다 맞습니다. 30분만 있다면 01 코스에 89,000₫ 마사지를 더하십시오.</p>
<h2>위치</h2>
<p>251/30 Lê Quang Định, Gia Định 동. 금액은 <a href="/ko/goi-dau/">헤드 스파 페이지</a>에 있습니다.</p>''',
 [('늦게까지 하나요?','아닙니다. 매일 20:30까지 손님을 받습니다.'),
  ('저녁에는 예약이 필요한가요?','권합니다. 인원 제한이 있어 저녁이 먼저 찹니다.')]),
('平盛郡的傍晚洗髮：最晚幾點收客',
 'VESSCA 每天收客到 20:30。這裡說明傍晚還可以排進的時段，以及下班後適合的套餐。',
 '平盛郡傍晚養生洗髮 — 營業至 20:30 | VESSCA',
 '平盛郡傍晚養生洗髮：VESSCA 每天 9:00–20:30 營業，鄰近富潤區。下班後的套餐建議。',
 ['平盛郡晚上洗髮','胡志明晚間頭皮SPA','下班後養生洗髮'],
'''<p>搜尋這個的人多半剛下班。先說清楚：VESSCA 每天 9:00 到 20:30，20:30 之後不再收客，也不做深夜時段。</p>
<h2>傍晚建議的時段</h2>
<ul><li><b>18:00–19:00：</b>最容易排進 50 分鐘套餐。</li><li><b>19:00–19:30：</b>30 分鐘套餐還可以，較長的通常來不及。</li><li><b>19:30 之後：</b>請先電話 0933 528 501 確認。</li></ul>
<p>為了讓預約不重疊，每個時段的人數有上限，所以傍晚最先滿。</p>
<h2>傍晚適合哪個套餐</h2>
<p>看了一整天螢幕之後，按摩才是最值得的部分。含兩次頭部按摩的 02 套餐比偏臉部的 03 套餐合適。只有 30 分鐘時，選 01 套餐再加 89,000₫ 的頭部及肩頸按摩。</p>
<h2>位置</h2>
<p>251/30 Lê Quang Định，Gia Định 坊。價格請見<a href="/zh/goi-dau/">養生洗髮頁面</a>。</p>''',
 [('有營業到很晚嗎？','沒有。每天收客到 20:30。'),
  ('傍晚需要預約嗎？','建議預約。時段人數有限，傍晚最先滿。')]))
