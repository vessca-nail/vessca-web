# -*- coding: utf-8 -*-
"""Đợt 42 — 10 bài màu nail, slot 13:30 từ 24/11 đến 3/12.
Màu lấy đúng từ Google autocomplete 23/11/2026 cho "nail màu " và "nail tông ":
nâu trà, thạch gạo, tiffany blue, cam sữa, trắng sữa đính đá, nâu tây,
tím đậm, xanh lá, vàng mắt mèo, xanh biển."""
from lib import bai, A

C = 'Xu hướng & Cảm hứng'
D = ['2026-11-24','2026-11-25','2026-11-26','2026-11-27','2026-11-28',
     '2026-11-29','2026-11-30','2026-12-01','2026-12-02','2026-12-03']
T = lambda i: D[i] + 'T13:30:00+07:00'

def m(slug, i, tim, altvi, alten, altko, altzh, V, E, K, Z):
    bai(slug, T(i), C, A((tim, altvi, alten, altko, altzh), []), V, E, K, Z)

# ---------------------------------------------------------------- 21
m('nail-mau-nau-tra', 0, 'brown nails manicure neutral',
  'Bộ nail màu nâu trà', 'A tea-brown manicure', '밀크티 브라운 네일', '奶茶棕美甲',
('Nail màu nâu trà: màu dễ mặc nhất trong nhóm nâu',
 'Nâu trà là sắc nâu pha sữa, nhạt hơn nâu đất và ấm hơn nâu xám. Đây là màu hợp gần như mọi tông da và mọi dịp.',
 'Nail màu nâu trà — dễ mặc nhất nhóm nâu',
 'Nail màu nâu trà: sắc nâu pha sữa hợp mọi tông da, cách phối, và vì sao nó bền hơn các màu theo mùa.',
 ['nail màu nâu trà','nail nâu sữa','nail nâu trà sữa','nail tông nâu'],
'''<p>Nâu trà là sắc nâu có sữa pha vào, nhạt và ấm hơn nâu đất, không lạnh như nâu xám. Trong nhóm nâu, đây là sắc dễ mặc nhất vì nó đứng giữa nude và màu đậm.</p>
<h2>Vì sao hợp nhiều tông da</h2>
<p>Nâu trà gần với sắc da tự nhiên nên không tạo ranh giới gắt ở chân móng. Da sáng mặc nâu trà thì tay trông ấm hơn; da ngăm mặc nâu trà thì tay trông sạch và đều màu, không bị đục như khi dùng nude quá nhạt.</p>
<h2>Hai hướng hoàn thiện</h2>
<ul>
<li><b>Nâu trà đục trơn</b> — gọn gàng, đi làm được, che được khuyết điểm móng.</li>
<li><b>Nâu trà ánh nhũ mịn</b> — có chiều sâu dưới ánh đèn, hợp tiệc tối và mùa cuối năm.</li>
</ul>
<h2>Phối với một màu nhấn</h2>
<p>Nâu trà rất chịu màu nhấn vì bản thân nó trung tính. Hướng hay dùng: một móng trắng sữa, một đường viền nhũ vàng mảnh, hoặc một móng burgundy để kéo bộ nail về tông lễ cuối năm. Không nên phối nâu trà với màu neon hoặc pastel lạnh, vì hai nhiệt độ màu đánh nhau.</p>
<h2>Ưu điểm thực tế: không lệch mùa</h2>
<p>Khác với màu theo mùa, nâu trà dùng được quanh năm, nên bạn không cần tháo khi qua lễ. Đây cũng là màu được chọn nhiều cho móng ngắn vì nó không chia đôi bề mặt móng như màu tối.</p>
<p>Bảng giá ở trang <a href="/bang-gia/">Bảng giá</a>. Bài <a href="/blog/nail-mau-gi-hop-tong-da/">nail màu gì hợp tông da</a> hướng dẫn đọc tông da của chính bạn.</p>''',
 [('Da ngăm làm nâu trà được không?','Được, và thường rất ăn. Nâu trà làm tay trông đều màu hơn nude nhạt.'),
  ('Nâu trà có hợp móng ngắn không?','Hợp. Màu sáng trung tính không làm móng ngắn trông ngắn thêm như màu tối.')]),
('Tea-Brown Nails: The Easiest Brown to Wear',
 'Tea brown is brown with milk in it — lighter than earth brown, warmer than grey-brown. It suits almost every skin tone.',
 'Tea-Brown Nails — The Easiest Brown | VESSCA',
 'Tea-brown nails: a milky brown that suits most skin tones, how to pair it, and why it outlasts seasonal colours.',
 ['tea brown nails','milk tea nails','brown manicure korean'],
'''<p>Tea brown is brown with milk in it: lighter and warmer than earth brown, not cool like grey-brown. It sits between nude and a strong colour, which is why it is the easiest brown to wear.</p>
<h2>Why it suits many skin tones</h2>
<p>It is close to natural skin, so there is no harsh line at the cuticle. On fair skin it warms the hand; on tanned skin it reads clean and even, where a very pale nude can look dull.</p>
<h2>Two finishes</h2>
<ul><li><b>Opaque tea brown</b> — tidy, office-ready, hides imperfections.</li><li><b>Fine-shimmer tea brown</b> — depth under light, good for evenings.</li></ul>
<h2>One accent colour</h2>
<p>Being neutral, it takes an accent well: one milky white nail, a thin gold line, or one burgundy nail for the season. Avoid neon or cool pastels alongside it.</p>
<h2>It never looks out of season</h2>
<p>Unlike seasonal shades, tea brown works all year, so there is no need to remove it after a holiday.</p>
<p>Prices on the <a href="/en/bang-gia/">price list</a>.</p>''',
 [('Does it suit tanned skin?','Yes, usually very well — it evens the hand more than a pale nude.'),
  ('Is it good for short nails?','Yes. A light neutral does not shorten the nail the way dark colour does.')]),
('밀크티 브라운 네일: 브라운 중 가장 쉬운 색',
 '밀크티 브라운은 우유를 섞은 브라운입니다. 어시 브라운보다 밝고 그레이 브라운보다 따뜻합니다.',
 '밀크티 브라운 네일 — 가장 쉬운 브라운 | VESSCA',
 '밀크티 브라운 네일: 대부분의 피부톤에 맞는 밀키 브라운, 조합 방법, 계절을 타지 않는 이유.',
 ['밀크티 브라운 네일','브라운 네일','누드 브라운'],
'''<p>밀크티 브라운은 우유를 섞은 브라운입니다. 어시 브라운보다 밝고 따뜻하며 그레이 브라운처럼 차갑지 않습니다. 누드와 진한 색 사이에 있어 브라운 중 가장 쉽게 쓸 수 있습니다.</p>
<h2>여러 피부톤에 맞는 이유</h2>
<p>피부색에 가까워 큐티클 쪽에 경계가 생기지 않습니다. 밝은 피부에서는 손이 따뜻해 보이고, 태닝된 피부에서는 손이 고르게 보입니다.</p>
<h2>두 가지 마감</h2>
<ul><li><b>불투명 밀크티 브라운</b> — 단정하고 출근용으로 좋으며 결점을 가립니다.</li><li><b>고운 펄 밀크티 브라운</b> — 조명 아래 깊이가 생겨 저녁 자리에 좋습니다.</li></ul>
<h2>포인트 한 가지</h2>
<p>중립적이라 포인트를 잘 받습니다. 밀키 화이트 한 손가락, 얇은 골드 라인, 또는 버건디 한 손가락입니다.</p>
<p>금액은 <a href="/ko/bang-gia/">가격표</a>에 있습니다.</p>''',
 [('태닝된 피부에도 맞나요?','대체로 아주 잘 맞습니다. 연한 누드보다 손이 고르게 보입니다.'),
  ('짧은 손톱에도 어울리나요?','어울립니다. 밝은 중립색은 어두운 색처럼 손톱을 짧아 보이게 하지 않습니다.')]),
('奶茶棕美甲：棕色裡最好駕馭的一種',
 '奶茶棕是加了牛奶的棕色，比大地棕更淺，比灰棕更暖，幾乎適合所有膚色。',
 '奶茶棕美甲 — 最好駕馭的棕 | VESSCA',
 '奶茶棕美甲：適合多數膚色的牛奶棕、搭配方式，以及它不受季節限制的原因。',
 ['奶茶棕美甲','棕色指甲','裸棕色美甲'],
'''<p>奶茶棕是加了牛奶的棕色，比大地棕更淺更暖，也不像灰棕那樣冷。它介於裸色與濃色之間，因此是棕色裡最好駕馭的一種。</p>
<h2>為什麼適合多數膚色</h2>
<p>它接近膚色，甲根不會出現明顯界線。白皙膚色會顯得溫暖，膚色較深則顯得乾淨勻稱，而太淺的裸色反而會顯濁。</p>
<h2>兩種質地</h2>
<ul><li><b>不透明奶茶棕</b> — 乾淨、可上班，能遮瑕。</li><li><b>細珠光奶茶棕</b> — 燈下有層次，適合晚間場合。</li></ul>
<h2>一個點綴色</h2>
<p>因為中性，它很能配點綴：一指牛奶白、一道細金線，或一指酒紅。</p>
<p>價格請見<a href="/zh/bang-gia/">價目表</a>。</p>''',
 [('膚色深可以用嗎？','通常非常合適，比淺裸色更能讓手色勻稱。'),
  ('短甲適合嗎？','適合。明亮的中性色不會像深色那樣讓指甲顯短。')]))

# ---------------------------------------------------------------- 22
m('nail-mau-thach-gao', 1, 'sheer milky white nails translucent',
  'Bộ nail màu thạch gạo', 'A rice-jelly manicure', '라이스 젤리 네일', '米白果凍美甲',
('Nail màu thạch gạo: trắng trong như hạt gạo',
 'Thạch gạo là sắc trắng có độ trong, nhìn như hạt gạo ngâm nước. Màu trung tính nhất trong nhóm thạch, nhưng kén móng thật.',
 'Nail màu thạch gạo — trắng trong, trung tính nhất',
 'Nail màu thạch gạo: sắc trắng trong trung tính, điều kiện móng thật cần có, cách phối và lưu ý khi làm nhiều lớp mỏng.',
 ['nail màu thạch gạo','nail thạch gạo','nail trắng trong','nail màu gạo'],
'''<p>Thạch gạo là sắc trắng pha trong, không đục kín như trắng sữa và không hoàn toàn trong như sơn bóng. Hiệu ứng là móng trông như hạt gạo ngâm nước: trắng nhẹ, hơi mờ, ánh sáng vẫn xuyên qua.</p>
<h2>Vì sao được tìm nhiều</h2>
<p>Đây là sắc trung tính nhất trong nhóm thạch. Nó không nghiêng hồng, không nghiêng vàng, nên đi với mọi màu trang phục và không làm tay bị lệch tông. Người lần đầu thử màu thạch thường được gợi ý bắt đầu từ sắc này.</p>
<h2>Điều kiện: móng thật phải đều màu</h2>
<p>Vì có độ trong, thạch gạo không che được đốm trắng, vệt vàng hay phần móng không đều. Nếu móng bạn đang có những dấu hiệu đó, trắng sữa đục là lựa chọn hợp hơn. Bài <a href="/blog/mong-soc-doc-dom-trang/">móng sọc dọc, đốm trắng</a> nói về cách đọc các dấu hiệu này.</p>
<h2>Cần nhiều lớp mỏng</h2>
<p>Sơn thạch chỉ ra độ trong đều khi chồng nhiều lớp mỏng. Một lớp dày sẽ để lại vệt cọ. Nghĩa là bộ này mất thời gian hơn bộ sơn đục, nên nói trước khi đặt lịch.</p>
<h2>Phối thế nào</h2>
<p>Thạch gạo đứng một mình đã đủ. Nếu muốn thêm, chỉ nên thêm thứ không phá độ trong: vài hạt nhũ mịn rắc ở chân móng, hoặc một móng ánh xà cừ. Tránh đá lớn và hoạ tiết đậm vì chúng làm mất đi cảm giác nhẹ, vốn là lý do người ta chọn màu này.</p>
<p>Bảng giá ở trang <a href="/bang-gia/">Bảng giá</a>. Bài <a href="/blog/nail-thach-han-quoc/">nail thạch Hàn Quốc</a> nói chung về nhóm sơn thạch.</p>''',
 [('Thạch gạo khác trắng sữa ở đâu?','Trắng sữa đục, phủ kín và che khuyết điểm. Thạch gạo có độ trong, nhìn nhẹ hơn nhưng không che được gì.'),
  ('Móng vàng làm thạch gạo được không?','Không nên, vì vệt vàng sẽ lộ qua lớp trong. Nên dưỡng móng trước hoặc chọn trắng sữa.')]),
('Rice-Jelly Nails: Sheer White Like Soaked Rice',
 'Rice jelly is a sheer white that looks like soaked rice grains. The most neutral of the jelly shades, but it demands clean natural nails.',
 'Rice-Jelly Nails — The Most Neutral Sheer | VESSCA',
 'Rice-jelly nails: a neutral sheer white, what the natural nail needs, how to pair it and why it takes several thin coats.',
 ['rice jelly nails','sheer white nails','milky sheer manicure'],
'''<p>Rice jelly is white with transparency in it — not fully opaque like milky white, not clear like gloss. The nail looks like a soaked grain of rice: faintly white, slightly cloudy, light still passing through.</p>
<h2>Why it is popular</h2>
<p>It is the most neutral jelly shade. It leans neither pink nor yellow, so it goes with any outfit and never throws the hand off tone.</p>
<h2>The condition: an even natural nail</h2>
<p>Being sheer, it hides nothing — white spots, yellow streaks and uneven areas all show. If that describes your nails, opaque milky white is the better choice.</p>
<h2>Several thin coats</h2>
<p>Jelly only looks even built up in thin layers. One thick coat streaks, so it takes longer than opaque colour.</p>
<h2>Pairing</h2>
<p>It stands alone well. If you add anything, keep it light: fine shimmer at the cuticle, or one mother-of-pearl nail. Large stones defeat the point.</p>
<p>Prices on the <a href="/en/bang-gia/">price list</a>.</p>''',
 [('How is it different from milky white?','Milky white is opaque and hides flaws. Rice jelly is sheer — lighter looking, but it covers nothing.'),
  ('My nails are yellowed — can I use it?','Not ideally; the yellow shows through. Milky white is safer.')]),
('라이스 젤리 네일: 불린 쌀처럼 투명한 화이트',
 '라이스 젤리는 불린 쌀알처럼 보이는 투명한 화이트입니다. 젤리 중 가장 중립적이지만 자연 손톱이 깨끗해야 합니다.',
 '라이스 젤리 네일 — 가장 중립적인 투명 화이트',
 '라이스 젤리 네일: 중립적인 투명 화이트, 자연 손톱의 조건, 조합 방법과 얇게 여러 번 올려야 하는 이유.',
 ['라이스 젤리 네일','투명 화이트 네일','밀키 젤리'],
'''<p>라이스 젤리는 투명함이 섞인 화이트입니다. 밀키 화이트처럼 완전히 불투명하지도, 글로스처럼 투명하지도 않습니다. 불린 쌀알처럼 은은하게 희고 살짝 흐리며 빛이 통과합니다.</p>
<h2>많이 찾는 이유</h2>
<p>젤리 컬러 중 가장 중립적입니다. 핑크나 옐로로 기울지 않아 어떤 옷에도 맞고 손의 톤을 흐트러뜨리지 않습니다.</p>
<h2>조건: 고른 자연 손톱</h2>
<p>투명하므로 아무것도 가리지 못합니다. 흰 반점, 노란 자국, 고르지 않은 부분이 모두 보입니다. 그렇다면 불투명 밀키 화이트가 낫습니다.</p>
<h2>얇게 여러 번</h2>
<p>젤리는 얇게 쌓아야 고르게 나옵니다. 한 번에 두껍게 바르면 얼룩이 생기므로 시간이 더 걸립니다.</p>
<p>금액은 <a href="/ko/bang-gia/">가격표</a>에 있습니다.</p>''',
 [('밀키 화이트와 어떻게 다른가요?','밀키 화이트는 불투명해 결점을 가립니다. 라이스 젤리는 투명해서 가리지 못합니다.'),
  ('손톱이 노랗게 변했는데 가능할까요?','권하지 않습니다. 노란 기가 투명층으로 보입니다.')]),
('米白果凍美甲：像泡過水的米粒那樣透白',
 '米白果凍是帶透明度的白，看起來像泡過水的米粒。果凍色中最中性的一種，但對真甲要求高。',
 '米白果凍美甲 — 最中性的透白 | VESSCA',
 '米白果凍美甲：中性的透明白、真甲需要的條件、搭配方式，以及需要薄塗多層的原因。',
 ['米白果凍美甲','透明白指甲','牛奶果凍色'],
'''<p>米白果凍是摻了透明度的白：不像牛奶白完全不透，也不像亮油完全透明。指甲看起來像泡過水的米粒，微白、略霧，光線仍會穿過。</p>
<h2>為什麼受歡迎</h2>
<p>它是果凍色中最中性的。不偏粉也不偏黃，搭任何服裝都合適，也不會讓手色偏掉。</p>
<h2>條件：真甲要勻</h2>
<p>因為透，它遮不住任何東西。白點、黃痕、不勻的部分都會顯現。若是這種情況，不透明的牛奶白更合適。</p>
<h2>薄塗多層</h2>
<p>果凍色要薄塗堆疊才均勻。一次厚塗會有刷痕，因此比不透明色耗時。</p>
<p>價格請見<a href="/zh/bang-gia/">價目表</a>。</p>''',
 [('和牛奶白差在哪？','牛奶白不透明，能遮瑕。米白果凍是透的，遮不住。'),
  ('指甲泛黃可以用嗎？','不太建議，黃會透出來。牛奶白較保險。')]))

# ---------------------------------------------------------------- 23
m('nail-mau-tiffany-blue', 2, 'light blue nails pastel manicure',
  'Bộ nail màu xanh Tiffany', 'A Tiffany-blue manicure', '티파니 블루 네일', '蒂芬妮藍美甲',
('Nail màu Tiffany blue: xanh ngọc nhạt và cách làm cho nó không bị lạnh',
 'Tiffany blue là xanh ngọc pha trắng, nổi bật nhưng dễ làm tay trông xám nếu không chọn đúng độ đục và đúng form.',
 'Nail màu Tiffany blue — cách làm không bị lạnh',
 'Nail màu Tiffany blue: chọn độ đục phù hợp, tông da nào ăn màu này, và cách phối để tay không trông xám.',
 ['nail màu tiffany blue','nail xanh ngọc','nail xanh pastel','nail xanh tiffany'],
'''<p>Tiffany blue là sắc xanh ngọc pha trắng, nằm giữa xanh mint và xanh da trời. Màu này được tìm nhiều vì nó tươi và dễ nhận ra, nhưng cũng là một trong những màu kén nhất với tông da châu Á.</p>
<h2>Vấn đề: màu lạnh trên da ấm</h2>
<p>Phần lớn tông da người Việt ngả vàng hoặc ngả olive, tức là da ấm. Màu lạnh như Tiffany blue đặt cạnh da ấm sẽ làm cả hai nổi bật theo hướng đối lập, và kết quả thường là tay trông xám hơn thực tế. Đây là lý do nhiều người thấy màu đẹp trong lọ mà lên tay thì không ưng.</p>
<h2>Ba cách khắc phục</h2>
<ul>
<li><b>Chọn sắc đục hơn</b> — Tiffany blue pha thêm trắng sữa sẽ mềm đi và ít tương phản với da.</li>
<li><b>Giảm diện tích</b> — làm hai hoặc ba móng Tiffany blue trong bộ nền trắng sữa, thay vì mười móng.</li>
<li><b>Thêm chi tiết ấm</b> — một đường viền nhũ vàng mảnh hoặc một móng nude kéo nhiệt độ màu về giữa.</li>
</ul>
<h2>Form và độ dài</h2>
<p>Màu sáng lạnh làm móng trông rộng hơn, nên form oval hoặc almond nhẹ cân đối hơn form vuông. Móng ngắn làm màu này vẫn được, chỉ cần chọn sắc đục.</p>
<h2>Khi nào màu này rất ăn</h2>
<p>Da sáng ngả hồng mặc Tiffany blue rất nổi. Màu này cũng rất ăn ảnh ngoài trời và hợp mùa nắng, dịp đi biển. Mùa lễ cuối năm thì nó hơi lệch không khí, trừ khi bạn làm nó ở dạng hai móng nhấn trong bộ trắng.</p>
<p>Bài <a href="/blog/nail-mau-gi-hop-tong-da/">nail màu gì hợp tông da</a> giúp bạn xác định tông da. Bảng giá ở trang <a href="/bang-gia/">Bảng giá</a>.</p>''',
 [('Da ngăm làm Tiffany blue được không?','Được nhưng nên chọn sắc đục hơn và chỉ làm hai tới ba móng nhấn, thay vì cả bộ.'),
  ('Màu này có hợp mùa lễ cuối năm không?','Không hẳn. Nó thuộc nhóm màu mùa nắng. Nếu muốn dùng dịp lễ, nên làm dạng nhấn trong bộ trắng sữa.')]),
('Tiffany-Blue Nails: Keeping a Cool Blue From Greying the Hand',
 'Tiffany blue is turquoise with white in it — striking, but it can drain a warm skin tone if the opacity and shape are wrong.',
 'Tiffany-Blue Nails — Without the Grey | VESSCA',
 'Tiffany-blue nails: choosing the right opacity, which skin tones it suits, and how to pair it so hands do not look grey.',
 ['tiffany blue nails','pastel blue manicure','turquoise nails'],
'''<p>Tiffany blue sits between mint and sky blue. It is popular because it is fresh and recognisable, but it is one of the harder colours on Asian skin tones.</p>
<h2>The problem: a cool colour on warm skin</h2>
<p>Most Vietnamese skin tones lean yellow or olive, meaning warm. A cool blue beside warm skin pushes both in opposite directions, and the hand often reads greyer than it is.</p>
<h2>Three fixes</h2>
<ul><li><b>Choose a more opaque version</b> — milky white mixed in softens the contrast.</li><li><b>Use less of it</b> — two or three blue nails in a milky white set rather than all ten.</li><li><b>Add a warm detail</b> — a thin gold line or one nude nail pulls the temperature back.</li></ul>
<h2>Shape</h2>
<p>A bright cool colour widens the nail, so a soft oval or almond balances better than a square.</p>
<h2>When it works beautifully</h2>
<p>On fair, pink-undertoned skin, and for sunny-season or beach occasions. It sits slightly off-season in December unless used as an accent.</p>
<p>Prices on the <a href="/en/bang-gia/">price list</a>.</p>''',
 [('Can tanned skin wear it?','Yes, with a more opaque shade and only as two or three accent nails.'),
  ('Does it suit December?','Not especially — it belongs to the sunny season. Use it as an accent if you want it now.')]),
('티파니 블루 네일: 차가운 블루가 손을 회색으로 만들지 않게',
 '티파니 블루는 흰색이 섞인 터콰이즈입니다. 눈에 띄지만 불투명도와 셰이프를 잘못 고르면 따뜻한 피부톤을 탁하게 만듭니다.',
 '티파니 블루 네일 — 회색 없이 | VESSCA',
 '티파니 블루 네일: 알맞은 불투명도, 어울리는 피부톤, 손이 회색으로 보이지 않게 조합하는 방법.',
 ['티파니 블루 네일','파스텔 블루 네일','터콰이즈 네일'],
'''<p>티파니 블루는 민트와 스카이 블루 사이에 있습니다. 상쾌하고 알아보기 쉬워 인기가 있지만, 아시아 피부톤에는 까다로운 색 중 하나입니다.</p>
<h2>문제: 따뜻한 피부에 차가운 색</h2>
<p>베트남과 한국의 피부톤은 대개 옐로나 올리브, 즉 웜톤입니다. 차가운 블루가 웜톤 옆에 오면 서로 반대 방향으로 밀려 손이 실제보다 회색빛으로 보입니다.</p>
<h2>세 가지 해법</h2>
<ul><li><b>더 불투명한 버전</b> — 밀키 화이트가 섞이면 대비가 부드러워집니다.</li><li><b>면적을 줄이기</b> — 밀키 화이트 세트에 두세 손가락만.</li><li><b>따뜻한 디테일</b> — 얇은 골드 라인이나 누드 한 손가락.</li></ul>
<h2>잘 맞는 경우</h2>
<p>밝고 핑크 기가 있는 피부, 그리고 여름이나 바다 일정에 잘 맞습니다. 12월에는 포인트로 쓰시는 편이 좋습니다.</p>
<p>금액은 <a href="/ko/bang-gia/">가격표</a>에 있습니다.</p>''',
 [('태닝된 피부도 가능한가요?','더 불투명한 색으로, 두세 손가락 포인트로만 쓰시면 됩니다.'),
  ('12월에 어울리나요?','계절감은 여름 쪽입니다. 지금 쓰시려면 포인트로 넣으십시오.')]),
('蒂芬妮藍美甲：別讓冷藍把手襯灰',
 '蒂芬妮藍是摻白的土耳其藍，很搶眼，但若不透明度與甲形選錯，會讓暖膚色顯得沒有血色。',
 '蒂芬妮藍美甲 — 不顯灰的做法 | VESSCA',
 '蒂芬妮藍美甲：挑對不透明度、適合的膚色，以及搭配方式讓手不顯灰。',
 ['蒂芬妮藍美甲','粉彩藍指甲','土耳其藍美甲'],
'''<p>蒂芬妮藍介於薄荷綠與天空藍之間。它清爽好認所以受歡迎，但在亞洲膚色上屬於較難駕馭的顏色。</p>
<h2>問題：冷色放在暖膚上</h2>
<p>多數越南與華人膚色偏黃或橄欖，屬暖調。冷藍放在暖膚旁會互相往反方向推，手常顯得比實際更灰。</p>
<h2>三個解法</h2>
<ul><li><b>選更不透明的版本</b> — 摻了牛奶白，對比會柔和。</li><li><b>減少面積</b> — 牛奶白底中只做兩三指。</li><li><b>加一點暖</b> — 一道細金線或一指裸色，把色溫拉回來。</li></ul>
<h2>什麼時候很好看</h2>
<p>白皙偏粉的膚色，以及夏天或海邊的場合。十二月建議當成點綴使用。</p>
<p>價格請見<a href="/zh/bang-gia/">價目表</a>。</p>''',
 [('膚色深能用嗎？','可以，選更不透明的色號，只做兩三指點綴。'),
  ('適合十二月嗎？','季節感偏夏天。想現在用就當點綴。')]))

# ---------------------------------------------------------------- 24
m('nail-mau-cam-sua', 3, 'peach nails soft manicure warm',
  'Bộ nail màu cam sữa', 'A milky peach manicure', '밀키 오렌지 네일', '奶橘色美甲',
('Nail màu cam sữa: cam pha sữa nên không bị chói',
 'Cam nguyên bản khó mặc, nhưng cam pha sữa lại là một trong những màu làm tay trông sáng nhất mà không gắt.',
 'Nail màu cam sữa — sáng tay mà không gắt',
 'Nail màu cam sữa: cam pha sữa làm tay sáng, hợp tông da ngả vàng, cách phối và dịp nên dùng.',
 ['nail màu cam sữa','nail cam nhạt','nail màu đào sữa','nail cam pastel'],
'''<p>Cam tươi là màu ít người dám làm cả bộ, vì nó rất hút mắt và dễ gắt. Cam sữa thì khác: thêm sữa vào, độ chói giảm hẳn, còn lại là một màu ấm nhẹ nằm giữa đào và nude.</p>
<h2>Vì sao màu này làm tay trông sáng</h2>
<p>Da ngả vàng hoặc ngả olive là tông da ấm. Màu ấm đặt cạnh da ấm thì hoà vào nhau chứ không đối lập, nên tay trông đều màu và sáng hơn. Đây là ưu điểm cam sữa có mà các màu lạnh không có.</p>
<h2>Ai nên làm, ai nên tránh</h2>
<ul>
<li><b>Rất ăn:</b> da ngả vàng, da ngăm nhẹ, người thấy màu hồng làm tay mình trông nhợt.</li>
<li><b>Nên thử sắc đậm hơn:</b> da rất ngăm, vì cam quá nhạt dễ bị lẫn vào da.</li>
<li><b>Cân nhắc:</b> da sáng ngả hồng, vì cam sữa có thể làm tay trông hơi vàng.</li>
</ul>
<h2>Phối thế nào</h2>
<p>Cam sữa đủ nhẹ để làm trơn cả mười móng. Nếu muốn nhấn, dùng trắng sữa hoặc nhũ vàng mịn, cả hai cùng nhiệt độ màu. Tránh nhấn bằng xanh lạnh hoặc tím, vì chúng kéo bộ nail về hai hướng ngược nhau.</p>
<h2>Dịp nào dùng</h2>
<p>Đây là màu cho ngày thường, đi làm, đi cà phê. Mùa lễ cuối năm thì nó hơi nhẹ so với không khí, nhưng nếu bạn muốn một màu dễ chịu không theo mùa thì cam sữa và nâu trà là hai lựa chọn hợp nhất.</p>
<p>Bảng giá ở trang <a href="/bang-gia/">Bảng giá</a>.</p>''',
 [('Cam sữa có hợp móng ngắn không?','Hợp. Màu ấm sáng không làm móng ngắn trông ngắn thêm.'),
  ('Da sáng làm cam sữa được không?','Được, nhưng nếu da ngả hồng thì nên chọn sắc nghiêng đào thay vì nghiêng cam.')]),
('Milky Peach Nails: Orange With Milk, So It Never Shouts',
 'Straight orange is hard to wear. Orange with milk in it is one of the colours that brightens the hand most without turning loud.',
 'Milky Peach Nails — Bright, Not Loud | VESSCA',
 'Milky peach nails: a soft warm orange that brightens the hand, suits yellow undertones, and how to pair it.',
 ['milky peach nails','soft orange manicure','peach nail colour'],
'''<p>Few people wear bright orange on all ten nails — it is loud. Milky peach is different: add milk and the glare drops, leaving a soft warm shade between peach and nude.</p>
<h2>Why it brightens the hand</h2>
<p>Yellow and olive undertones are warm. A warm colour beside warm skin blends rather than fights, so the hand reads even and brighter.</p>
<h2>Who it suits</h2>
<ul><li><b>Very well:</b> yellow undertones, lightly tanned skin, anyone who finds pink makes their hand look washed out.</li><li><b>Go deeper:</b> deeply tanned skin, where a pale peach disappears.</li><li><b>Consider:</b> fair pink-undertoned skin, where it can read yellow.</li></ul>
<h2>Pairing</h2>
<p>Milky white or fine gold shimmer, both the same temperature. Avoid cool blue or violet accents.</p>
<h2>When to wear it</h2>
<p>An everyday colour. Slightly light for the December mood, but a good year-round choice alongside tea brown.</p>
<p>Prices on the <a href="/en/bang-gia/">price list</a>.</p>''',
 [('Good for short nails?','Yes. A bright warm colour does not shorten the nail.'),
  ('Does it work on fair skin?','Yes, though pink undertones should pick a peachier version.')]),
('밀키 오렌지 네일: 우유를 섞어 과하지 않은 오렌지',
 '선명한 오렌지는 쓰기 어렵습니다. 우유를 섞은 오렌지는 손을 가장 밝게 보이게 하면서도 과하지 않습니다.',
 '밀키 오렌지 네일 — 밝지만 과하지 않게 | VESSCA',
 '밀키 오렌지 네일: 손을 밝게 하는 부드러운 웜 컬러, 옐로 베이스에 잘 맞는 이유와 조합법.',
 ['밀키 오렌지 네일','소프트 오렌지 네일','피치 네일'],
'''<p>선명한 오렌지를 열 손가락에 올리는 분은 많지 않습니다. 밀키 오렌지는 다릅니다. 우유를 섞으면 쨍함이 빠지고 피치와 누드 사이의 부드러운 웜 컬러가 남습니다.</p>
<h2>손이 밝아 보이는 이유</h2>
<p>옐로나 올리브 베이스는 웜톤입니다. 웜 컬러가 웜 피부 옆에 오면 부딪히지 않고 섞여서 손이 고르고 밝게 보입니다.</p>
<h2>어울리는 분</h2>
<ul><li><b>아주 잘:</b> 옐로 베이스, 가볍게 태닝된 피부, 핑크가 손을 창백하게 만든다고 느끼는 분.</li><li><b>더 진하게:</b> 많이 태닝된 피부. 연한 피치는 묻힙니다.</li><li><b>참고:</b> 밝고 핑크 기가 있는 피부에서는 노랗게 보일 수 있습니다.</li></ul>
<h2>조합</h2>
<p>밀키 화이트나 고운 골드 펄이 같은 색온도로 잘 맞습니다. 쿨 블루나 바이올렛 포인트는 피하십시오.</p>
<p>금액은 <a href="/ko/bang-gia/">가격표</a>에 있습니다.</p>''',
 [('짧은 손톱에도 좋나요?','좋습니다. 밝은 웜 컬러는 손톱을 짧아 보이게 하지 않습니다.'),
  ('밝은 피부에도 맞나요?','맞습니다. 핑크 기가 있다면 피치에 가까운 쪽을 고르십시오.')]),
('奶橘色美甲：加了牛奶的橘，所以不吵',
 '純橘色很難駕馭。加了牛奶的橘，是最能讓手色變亮又不喧鬧的顏色之一。',
 '奶橘色美甲 — 亮但不吵 | VESSCA',
 '奶橘色美甲：讓手色變亮的柔和暖色，適合黃調膚色的原因與搭配方式。',
 ['奶橘色美甲','柔橘色指甲','蜜桃色美甲'],
'''<p>很少有人十指都做鮮橘色，太吵。奶橘不同：加了牛奶，刺眼感消失，剩下介於蜜桃與裸色之間的柔和暖色。</p>
<h2>為什麼會讓手變亮</h2>
<p>黃調與橄欖調屬暖膚。暖色放在暖膚旁是融合而非對抗，所以手色顯得勻而亮。</p>
<h2>適合誰</h2>
<ul><li><b>非常適合：</b>黃調膚色、微曬膚色，以及覺得粉色讓手顯白慘的人。</li><li><b>選深一點：</b>膚色較深者，太淺的蜜桃會被吃掉。</li><li><b>斟酌：</b>白皙偏粉的膚色，可能顯黃。</li></ul>
<h2>搭配</h2>
<p>牛奶白或細金珠光，色溫相同。避免冷藍或紫色點綴。</p>
<p>價格請見<a href="/zh/bang-gia/">價目表</a>。</p>''',
 [('短甲適合嗎？','適合。明亮暖色不會讓指甲顯短。'),
  ('白皙膚色可以用嗎？','可以，若偏粉調建議選更偏蜜桃的版本。')]))

# ---------------------------------------------------------------- 25
m('nail-mau-trang-sua-dinh-da', 4, 'white nails pearl stones elegant',
  'Bộ nail trắng sữa có đính đá', 'A milky white set with stones', '큐빅을 올린 밀키 화이트 네일', '鑲鑽的牛奶白美甲',
('Nail màu trắng sữa đính đá: nền dễ nhất cho đá',
 'Trắng sữa là nền được chọn nhiều nhất khi muốn đính đá, vì nó không cạnh tranh với đá. Nhưng chọn loại đá sai thì đá biến mất.',
 'Nail trắng sữa đính đá — chọn loại đá nào',
 'Nail màu trắng sữa đính đá: vì sao trắng sữa là nền dễ nhất cho đá, loại đá nào nổi trên nền sáng, và nên đặt mấy viên.',
 ['nail màu trắng sữa đính đá','nail trắng đính đá','nail trắng sữa đá','nail trắng sang trọng'],
'''<p>Trắng sữa là nền được chọn nhiều nhất cho các bộ có đá, vì nó đục, phủ đều và không có sắc màu nào cạnh tranh với phần đá. Nhưng chính vì nền sáng nên việc chọn loại đá quan trọng hơn người ta nghĩ.</p>
<h2>Vấn đề: đá trắng trên nền trắng thì mất hút</h2>
<p>Đá trắng trong là loại phổ biến nhất, và nó nổi rất rõ trên nền tối. Trên nền trắng sữa, đá trắng dễ bị lẫn, nhìn gần mới thấy. Nếu bạn muốn phần đá nhìn thấy rõ, nên đổi sang:</p>
<ul>
<li><b>Đá ánh ngũ sắc</b> — đổi màu theo góc nhìn nên vẫn tách khỏi nền trắng.</li>
<li><b>Ngọc trai</b> — cùng tông với nền nhưng khác chất, tạo tương phản bằng bề mặt thay vì bằng màu.</li>
<li><b>Đá nhỏ ánh vàng hoặc champagne</b> — ấm hơn nền nên nổi vừa phải, không gắt.</li>
</ul>
<h2>Số lượng và vị trí</h2>
<p>Hai móng có đá, mỗi móng ba tới năm viên nhỏ, là mức cân đối. Đặt ở chân móng là an toàn nhất vì ít cọ và trông như một đường trang sức. Đầu móng dễ bật nhất nên tránh nếu bạn làm việc tay nhiều.</p>
<h2>Vì sao bộ này được chọn cho cưới và tiệc</h2>
<p>Trắng sữa làm tay trông sáng trong ảnh và không bị trùng với váy trắng như trắng tinh. Thêm vài viên đá là đủ chi tiết cho tiệc mà không vướng khi cầm hoa. Bài <a href="/blog/nail-co-dau-kieu-han/">nail cô dâu kiểu Hàn</a> và <a href="/blog/nail-noel-dinh-da/">nail Noel đính đá</a> nói kỹ hơn về từng dịp.</p>
<p>Đá tính lẻ theo viên. Bảng giá ở trang <a href="/bang-gia/">Bảng giá</a>.</p>''',
 [('Đá trắng có nổi trên nền trắng sữa không?','Không rõ bằng trên nền tối. Nên dùng đá ánh ngũ sắc, ngọc trai, hoặc đá ánh vàng.'),
  ('Bao nhiêu viên là vừa?','Hai móng, mỗi móng ba tới năm viên nhỏ.'),
  ('Trắng sữa khác trắng tinh ở đâu?','Trắng sữa có sữa pha vào nên mềm và ấm hơn, không bị thô như trắng tinh và không trùng với váy trắng trong ảnh.')]),
('Milky White Nails With Stones: The Easiest Base for Crystals',
 'Milky white is the most chosen base for stones because it does not compete with them. But the wrong stone disappears on it.',
 'Milky White Nails With Stones | VESSCA',
 'Milky white nails with stones: why it is the easiest base, which stones show on a light base, and how many to use.',
 ['white nails with stones','milky white rhinestone nails','elegant white manicure'],
'''<p>Milky white is the most chosen base for stoned sets: opaque, even, and with no colour competing with the crystals. But a light base makes stone choice matter more.</p>
<h2>Clear stones vanish on white</h2>
<p>Clear crystals, the most common kind, pop on dark bases. On milky white they blend in. If you want the stones to read, switch to:</p>
<ul><li><b>Iridescent stones</b> — shift colour with the angle, so they separate from white.</li><li><b>Pearls</b> — same tone, different texture; contrast by surface rather than colour.</li><li><b>Small gold or champagne stones</b> — warmer than the base, so they show without shouting.</li></ul>
<h2>How many, and where</h2>
<p>Two nails, three to five small stones each. At the cuticle is safest — least rubbing, and it reads like fine jewellery.</p>
<h2>Why this set suits weddings</h2>
<p>Milky white brightens the hand on camera and does not merge with a white gown the way stark white can. A few stones give enough detail for a reception without catching on a bouquet.</p>
<p>Stones are charged per piece. Prices on the <a href="/en/bang-gia/">price list</a>.</p>''',
 [('Do clear stones show on milky white?','Not strongly. Use iridescent, pearl, or gold-toned stones instead.'),
  ('How is milky white different from stark white?','Milky white has white softened with warmth; it is less harsh and separates from a white dress in photos.')]),
('큐빅을 올린 밀키 화이트 네일: 큐빅에 가장 쉬운 베이스',
 '밀키 화이트는 큐빅 세트에서 가장 많이 쓰는 베이스입니다. 큐빅과 경쟁하지 않기 때문입니다. 다만 잘못된 알을 올리면 사라집니다.',
 '밀키 화이트 큐빅 네일 | VESSCA',
 '밀키 화이트 큐빅 네일: 가장 쉬운 베이스인 이유, 밝은 베이스에서 보이는 큐빅 종류, 적당한 개수.',
 ['화이트 큐빅 네일','밀키 화이트 네일','우아한 화이트 네일'],
'''<p>밀키 화이트는 큐빅 세트에서 가장 많이 쓰이는 베이스입니다. 불투명하고 고르며 큐빅과 경쟁할 색이 없습니다. 다만 밝은 베이스이므로 알 선택이 더 중요해집니다.</p>
<h2>투명 큐빅은 화이트에서 사라집니다</h2>
<p>가장 흔한 투명 알은 어두운 베이스에서 돋보입니다. 밀키 화이트에서는 묻힙니다. 큐빅이 보이길 원하시면 바꾸십시오.</p>
<ul><li><b>오로라 알</b> — 각도에 따라 색이 변해 화이트에서 구분됩니다.</li><li><b>진주</b> — 같은 톤, 다른 질감으로 표면으로 대비를 만듭니다.</li><li><b>작은 골드·샴페인 알</b> — 베이스보다 따뜻해 과하지 않게 보입니다.</li></ul>
<h2>개수와 위치</h2>
<p>두 손가락에 각각 작은 알 세 개에서 다섯 개. 큐티클 쪽이 가장 안전하고 고급스럽게 보입니다.</p>
<p>큐빅은 개당 계산됩니다. 금액은 <a href="/ko/bang-gia/">가격표</a>에 있습니다.</p>''',
 [('투명 큐빅이 밀키 화이트에서 보이나요?','강하게 보이지 않습니다. 오로라, 진주, 골드 톤을 쓰십시오.'),
  ('순백과 어떻게 다른가요?','밀키 화이트가 더 부드럽고 따뜻해서 흰 드레스와 사진에서 구분됩니다.')]),
('鑲鑽的牛奶白美甲：最好搭鑽的底色',
 '牛奶白是鑲鑽最常用的底色，因為它不與鑽搶。但選錯鑽，鑽就消失了。',
 '鑲鑽的牛奶白美甲 | VESSCA',
 '鑲鑽的牛奶白美甲：最好搭鑽的原因、淺底色上看得見的鑽種類，以及合適的數量。',
 ['白色鑲鑽美甲','牛奶白指甲','優雅白色美甲'],
'''<p>牛奶白是鑲鑽組合最常用的底色：不透明、均勻，也沒有顏色與鑽競爭。但淺底色讓選鑽變得更重要。</p>
<h2>透明鑽在白底上會消失</h2>
<p>最常見的透明鑽在深底色上很突出，在牛奶白上卻會融進去。若希望鑽看得見，改用：</p>
<ul><li><b>極光鑽</b> — 隨角度變色，能與白底區隔。</li><li><b>珍珠</b> — 同色調但不同質地，用表面而非顏色製造對比。</li><li><b>小顆金色或香檳色鑽</b> — 比底色暖，看得見又不刺眼。</li></ul>
<h2>數量與位置</h2>
<p>兩指各三到五顆小鑽。甲根最安全，磨擦最少，看起來像精緻的首飾。</p>
<p>鑽按顆計價。價格請見<a href="/zh/bang-gia/">價目表</a>。</p>''',
 [('透明鑽在牛奶白上看得見嗎？','不明顯。改用極光、珍珠或金色系的鑽。'),
  ('牛奶白和純白差在哪？','牛奶白更柔和溫潤，不刺眼，照片裡也能與白紗區隔。')]))

# ---------------------------------------------------------------- 26
m('nail-mau-nau-tay', 5, 'dark brown nails chic manicure',
  'Bộ nail màu nâu tây', 'A deep Western-brown manicure', '다크 브라운 네일', '深棕色美甲',
('Nail màu nâu tây: nâu đậm cho mùa cuối năm',
 'Nâu tây là sắc nâu đậm ngả xám hoặc ngả đỏ, trầm hơn nâu trà. Đây là màu rất hợp mùa lạnh và dịp lễ cuối năm.',
 'Nail màu nâu tây — nâu đậm cho cuối năm',
 'Nail màu nâu tây: nâu đậm ngả xám hoặc ngả đỏ, hợp mùa cuối năm, cách chọn sắc và lưu ý với móng ngắn.',
 ['nail màu nâu tây','nail nâu đậm','nail nâu socola','nail nâu trầm'],
'''<p>Nâu tây là cách gọi nhóm nâu đậm, trầm, có sắc xám hoặc sắc đỏ bên trong, khác với nâu trà nhạt và ấm. Đây là màu lên mạnh vào mùa cuối năm vì nó cùng nhóm nhiệt độ với burgundy và các tông đất.</p>
<h2>Hai sắc chính</h2>
<ul>
<li><b>Nâu ngả xám</b> — lạnh, hiện đại, hợp trang phục tông trung tính và đồ đen.</li>
<li><b>Nâu ngả đỏ, nâu socola</b> — ấm, mềm hơn, hợp tông da ngả vàng và dịp lễ.</li>
</ul>
<p>Nếu bạn không chắc, nâu ngả đỏ dễ mặc hơn với phần lớn tông da người Việt, vì nó cùng nhiệt độ với da.</p>
<h2>Lưu ý với móng ngắn</h2>
<p>Màu đậm làm bề mặt móng trông nhỏ lại, nên móng rất ngắn mà sơn nâu đậm kín sẽ trông cụt hơn. Hai cách xử lý: để chừa một khoảng rất mảnh ở chân móng, hoặc chọn form oval nhẹ để kéo dài mắt nhìn. Bài <a href="/blog/nail-cho-ngon-tay-ngan/">nail cho ngón tay ngắn</a> nói kỹ về tỷ lệ.</p>
<h2>Phối với một chất liệu</h2>
<p>Nâu tây là nền rất chịu chất liệu vì nó tối. Đá trắng trong nổi rõ trên nền này, khác với nền trắng sữa. Nhũ vàng mịn cũng ăn. Nên giới hạn một chất liệu cho cả bộ để giữ sự tĩnh.</p>
<h2>Dùng được bao lâu</h2>
<p>Khác với màu gắn chặt với Noel, nâu tây dùng được từ giờ qua Tết. Nếu muốn chuyển sang bộ Tết, chỉ cần thay một móng thành đỏ.</p>
<p>Bảng giá ở trang <a href="/bang-gia/">Bảng giá</a>.</p>''',
 [('Nâu tây và nâu trà khác nhau thế nào?','Nâu trà nhạt, pha sữa, ấm và nhẹ. Nâu tây đậm, trầm, ngả xám hoặc ngả đỏ.'),
  ('Móng ngắn làm nâu đậm được không?','Được, nhưng nên chừa một khoảng mảnh ở chân móng hoặc chọn form oval để móng không trông cụt.')]),
('Deep Brown Nails for the End of the Year',
 'Deep brown leans either grey or red, darker than tea brown. It belongs to the same family as burgundy and earth tones.',
 'Deep Brown Nails — For the Cooler Months | VESSCA',
 'Deep brown nails: grey-leaning or red-leaning, which to choose, and how to wear a dark colour on short nails.',
 ['dark brown nails','chocolate brown manicure','deep brown nail colour'],
'''<p>Deep brown covers the darker, muted browns with grey or red inside them — the opposite of light, warm tea brown. It rises every year end because it shares a temperature with burgundy and earth tones.</p>
<h2>Two directions</h2>
<ul><li><b>Grey-leaning brown</b> — cool and modern, good with neutrals and black.</li><li><b>Red-leaning or chocolate brown</b> — warmer and softer, good with yellow undertones.</li></ul>
<p>If unsure, red-leaning is easier on most Asian skin tones because it matches the skin's temperature.</p>
<h2>On short nails</h2>
<p>Dark colour makes the nail plate look smaller, so a very short nail painted fully dark can look stubby. Either leave a very fine gap at the cuticle, or use a soft oval shape.</p>
<h2>One accent material</h2>
<p>A dark base takes material well. Clear crystals pop here, unlike on milky white. Fine gold shimmer also works. Keep to one material.</p>
<h2>How long it lasts in season</h2>
<p>Unlike Christmas-specific shades, deep brown carries through to Lunar New Year; swap one nail to red and the set turns festive.</p>
<p>Prices on the <a href="/en/bang-gia/">price list</a>.</p>''',
 [('How is it different from tea brown?','Tea brown is light, milky and warm. Deep brown is dark and muted, leaning grey or red.'),
  ('Can short nails take a dark colour?','Yes — leave a fine gap at the cuticle or use a soft oval shape.')]),
('다크 브라운 네일: 연말에 어울리는 진한 브라운',
 '다크 브라운은 그레이나 레드 기가 있는 진한 브라운입니다. 버건디와 어시 톤과 같은 계열입니다.',
 '다크 브라운 네일 — 연말에 | VESSCA',
 '다크 브라운 네일: 그레이 기와 레드 기 중 선택, 짧은 손톱에 진한 색을 올리는 방법.',
 ['다크 브라운 네일','초콜릿 브라운 네일','진한 브라운 네일'],
'''<p>다크 브라운은 그레이나 레드가 섞인 진하고 차분한 브라운입니다. 밝고 따뜻한 밀크티 브라운과 반대쪽입니다. 버건디, 어시 톤과 색온도가 같아 연말마다 많이 쓰입니다.</p>
<h2>두 방향</h2>
<ul><li><b>그레이 기 브라운</b> — 차갑고 현대적이며 블랙과 잘 맞습니다.</li><li><b>레드 기 또는 초콜릿 브라운</b> — 더 따뜻하고 부드러워 옐로 베이스에 맞습니다.</li></ul>
<p>고민되시면 레드 기가 아시아 피부톤에 더 쉽습니다.</p>
<h2>짧은 손톱이라면</h2>
<p>진한 색은 네일 플레이트를 작아 보이게 합니다. 큐티클 쪽에 아주 얇은 여백을 두거나 부드러운 오벌 셰이프를 쓰십시오.</p>
<h2>포인트 소재 한 가지</h2>
<p>어두운 베이스는 소재를 잘 받습니다. 밀키 화이트와 달리 투명 큐빅이 여기서는 돋보입니다.</p>
<p>금액은 <a href="/ko/bang-gia/">가격표</a>에 있습니다.</p>''',
 [('밀크티 브라운과 어떻게 다른가요?','밀크티 브라운은 밝고 따뜻합니다. 다크 브라운은 진하고 차분하며 그레이나 레드 기가 있습니다.'),
  ('짧은 손톱에 진한 색을 올려도 되나요?','됩니다. 큐티클 쪽에 얇은 여백을 두거나 오벌 셰이프를 쓰십시오.')]),
('深棕色美甲：適合年末的濃棕',
 '深棕是帶灰調或紅調的濃棕色，比奶茶棕更沉。它與酒紅、大地色屬同一個色溫家族。',
 '深棕色美甲 — 適合年末 | VESSCA',
 '深棕色美甲：偏灰或偏紅的選擇，以及短甲如何駕馭深色。',
 ['深棕色美甲','巧克力棕指甲','濃棕色美甲'],
'''<p>深棕涵蓋帶灰或帶紅的濃而沉的棕色，與明亮溫暖的奶茶棕相反。它與酒紅、大地色色溫相同，所以每年年末都會流行。</p>
<h2>兩個方向</h2>
<ul><li><b>偏灰的棕</b> — 冷調現代，搭中性色與黑色好看。</li><li><b>偏紅或巧克力棕</b> — 較暖較柔，適合黃調膚色。</li></ul>
<p>不確定的話，偏紅對多數亞洲膚色更好駕馭。</p>
<h2>短甲要注意</h2>
<p>深色會讓甲面看起來更小，很短的甲全塗深色會顯得更短。可以在甲根留一道極細的空隙，或改用柔和的橢圓形。</p>
<h2>一種點綴材質</h2>
<p>深色底很能承載材質。與牛奶白不同，透明鑽在這裡會突出。</p>
<p>價格請見<a href="/zh/bang-gia/">價目表</a>。</p>''',
 [('和奶茶棕差在哪？','奶茶棕明亮溫暖。深棕濃而沉，帶灰或帶紅。'),
  ('短甲能做深色嗎？','可以。甲根留細空隙，或改用橢圓形。')]))

# ---------------------------------------------------------------- 27
m('nail-tong-tim', 6, 'purple nails manicure violet',
  'Bộ nail tông tím', 'A violet-toned manicure', '퍼플 톤 네일', '紫色調美甲',
('Nail tông tím: chọn sắc tím nào để không bị tối tay',
 'Tím là màu có khoảng rộng nhất, từ tím khói nhạt tới tím đậm gần đen. Chọn sai sắc là lúc tay trông tối và thiếu sức sống.',
 'Nail tông tím — chọn sắc để không tối tay',
 'Nail tông tím: tím khói, tím lavender hay tím đậm, chọn theo tông da và dịp để tay không trông tối.',
 ['nail tông tím','nail màu tím','nail tím đậm','nail tím nhạt'],
'''<p>Tím có khoảng màu rộng hơn hầu hết các màu khác, từ lavender nhạt gần trắng tới tím đậm gần đen. Vì vậy câu hỏi không phải tím có hợp không, mà là sắc tím nào.</p>
<h2>Ba sắc và ai nên dùng</h2>
<ul>
<li><b>Tím khói nhạt</b> — pha xám, trầm, dễ mặc đi làm. Hợp hầu hết tông da vì nó không rực.</li>
<li><b>Lavender</b> — nhạt và lạnh, nổi nhất trên da sáng. Da ngăm dùng sắc này dễ bị bạc màu, nên chọn lavender đục hơn.</li>
<li><b>Tím đậm, tím nho</b> — hút mắt, hợp mùa cuối năm và tiệc tối. Cùng nhóm với burgundy nên dùng được tới Tết.</li>
</ul>
<h2>Lý do tím hay bị nói là làm tối tay</h2>
<p>Tím là màu lạnh và đậm. Trên tông da ấm, màu lạnh đậm tạo tương phản mạnh, khiến mắt đọc phần da là tối hơn. Cách xử lý: hạ độ đậm xuống, hoặc chọn sắc tím ngả đỏ, hoặc dùng tím ở dạng hai móng nhấn trong bộ nude.</p>
<h2>Hướng dễ nhất cho người mới thử</h2>
<p>Tím khói nhạt trơn mười móng. Nó đủ khác nude để thấy mình đã làm màu, nhưng không đủ rực để phải cân nhắc khi mặc đồ.</p>
<h2>Chất liệu ăn với tím</h2>
<p>Tím là một trong những nền ăn nhũ nhất. Nhũ bạc mịn và nhũ ánh ngũ sắc nổi rõ trên nền tím mà không gắt. Bài <a href="/blog/nail-nhu-aurora-han-quoc/">nail nhũ aurora Hàn Quốc</a> nói về nhóm chất liệu này.</p>
<p>Bảng giá ở trang <a href="/bang-gia/">Bảng giá</a>.</p>''',
 [('Da ngăm làm tím được không?','Được, nhưng nên chọn tím khói hoặc tím ngả đỏ, tránh lavender quá nhạt vì dễ bị bạc.'),
  ('Tím nào dùng được qua Tết?','Tím đậm, tím nho. Chúng cùng nhóm với burgundy nên không lệch dịp.')]),
('Violet Nails: Choosing a Purple That Does Not Darken the Hand',
 'Purple has the widest range of any colour, from pale smoke to near-black. The wrong shade is where the hand starts to look drained.',
 'Violet Nails — Choosing the Right Purple | VESSCA',
 'Violet nails: smoky, lavender or deep purple, chosen by skin tone and occasion so hands do not look dark.',
 ['purple nails','violet manicure','lavender nail colour'],
'''<p>Purple spans more ground than most colours, from a lavender close to white to a purple close to black. The question is not whether purple suits you but which purple.</p>
<h2>Three shades</h2>
<ul><li><b>Pale smoky violet</b> — greyed and muted, easy for work, suits most skin tones.</li><li><b>Lavender</b> — pale and cool, best on fair skin. On tanned skin it can look chalky, so choose a more opaque version.</li><li><b>Deep plum</b> — striking, suits the end of the year and evening events, and carries to Lunar New Year with burgundy.</li></ul>
<h2>Why purple is said to darken the hand</h2>
<p>It is cool and deep. On warm skin, a deep cool colour creates strong contrast, so the eye reads the skin as darker. Lower the depth, pick a red-leaning purple, or use purple as two accent nails in a nude set.</p>
<h2>Easiest starting point</h2>
<p>Pale smoky violet on all ten. Clearly a colour, never loud.</p>
<h2>Material</h2>
<p>Purple is one of the best bases for shimmer — fine silver and iridescent both show clearly without turning harsh.</p>
<p>Prices on the <a href="/en/bang-gia/">price list</a>.</p>''',
 [('Does purple work on tanned skin?','Yes — choose smoky or red-leaning purple rather than a very pale lavender.'),
  ('Which purple lasts into the new year?','Deep plum; it sits with burgundy and never looks out of season.')]),
('퍼플 톤 네일: 손이 어두워 보이지 않는 보라 고르기',
 '퍼플은 어떤 색보다 폭이 넓습니다. 연한 스모키부터 블랙에 가까운 톤까지 있습니다.',
 '퍼플 톤 네일 — 어떤 보라를 고를까 | VESSCA',
 '퍼플 톤 네일: 스모키, 라벤더, 딥 플럼 중 피부톤과 상황에 맞춰 골라 손이 어두워 보이지 않게.',
 ['퍼플 네일','보라색 네일','라벤더 네일'],
'''<p>퍼플은 대부분의 색보다 범위가 넓습니다. 흰색에 가까운 라벤더부터 블랙에 가까운 보라까지 있습니다. 질문은 퍼플이 어울리는지가 아니라 어떤 퍼플인지입니다.</p>
<h2>세 가지</h2>
<ul><li><b>연한 스모키 바이올렛</b> — 그레이가 섞여 차분하고 출근용으로 쉽습니다.</li><li><b>라벤더</b> — 연하고 차가워 밝은 피부에 가장 좋습니다. 태닝된 피부에서는 불투명한 쪽을 고르십시오.</li><li><b>딥 플럼</b> — 눈에 띄고 연말과 저녁 자리에 맞으며 버건디와 함께 설까지 이어집니다.</li></ul>
<h2>퍼플이 손을 어둡게 한다는 이유</h2>
<p>차갑고 깊은 색입니다. 웜 피부에서 깊은 쿨 컬러는 강한 대비를 만들어 피부가 더 어둡게 읽힙니다. 농도를 낮추거나, 레드 기 보라를 고르거나, 누드 세트에 두 손가락 포인트로 쓰십시오.</p>
<p>금액은 <a href="/ko/bang-gia/">가격표</a>에 있습니다.</p>''',
 [('태닝된 피부도 가능한가요?','가능합니다. 아주 연한 라벤더보다 스모키나 레드 기 보라를 고르십시오.'),
  ('설까지 쓸 수 있는 보라는요?','딥 플럼입니다. 버건디와 같은 계열이라 계절을 타지 않습니다.')]),
('紫色調美甲：挑一個不會讓手顯暗的紫',
 '紫色的幅度比任何顏色都寬，從淺煙紫到近黑都有。挑錯色號，手就開始顯得沒有血色。',
 '紫色調美甲 — 挑對那個紫 | VESSCA',
 '紫色調美甲：煙紫、薰衣草或深紫，依膚色與場合挑選，讓手不顯暗。',
 ['紫色美甲','薰衣草紫指甲','深紫色美甲'],
'''<p>紫色的範圍比多數顏色都寬，從接近白的薰衣草到接近黑的深紫。問題不是紫色適不適合你，而是哪一個紫。</p>
<h2>三種</h2>
<ul><li><b>淺煙紫</b> — 摻灰而沉穩，上班好駕馭，適合多數膚色。</li><li><b>薰衣草</b> — 淺而冷，白皙膚色最好看。膚色深請選更不透明的版本。</li><li><b>深梅紫</b> — 搶眼，適合年末與晚宴，與酒紅同列可以留到新年。</li></ul>
<h2>為什麼說紫色讓手顯暗</h2>
<p>它冷而深。在暖膚上，深的冷色造成強烈對比，眼睛會把皮膚讀得更暗。降低濃度、改選偏紅的紫，或在裸色組合中只做兩指點綴。</p>
<p>價格請見<a href="/zh/bang-gia/">價目表</a>。</p>''',
 [('膚色深能用紫色嗎？','可以。選煙紫或偏紅的紫，避開太淺的薰衣草。'),
  ('哪種紫能留到新年？','深梅紫。它與酒紅同列，不會顯得過季。')]))

# ---------------------------------------------------------------- 28
m('nail-mau-xanh-la', 7, 'green nails manicure olive',
  'Bộ nail màu xanh lá', 'A green manicure', '그린 네일', '綠色美甲',
('Nail màu xanh lá: ba sắc xanh và sắc nào mặc được hằng ngày',
 'Xanh lá bị coi là màu khó, nhưng đó là vì phần lớn người ta nghĩ tới xanh lá tươi. Xanh rêu và xanh olive lại rất dễ mặc.',
 'Nail màu xanh lá — sắc nào mặc được hằng ngày',
 'Nail màu xanh lá: xanh rêu, xanh olive hay xanh lá tươi, sắc nào dễ mặc, hợp tông da nào và phối với gì.',
 ['nail màu xanh lá','nail xanh rêu','nail xanh olive','nail xanh đậm'],
'''<p>Xanh lá hay bị gạt khỏi danh sách vì người ta hình dung xanh lá tươi kiểu lá non. Nhưng nhóm xanh lá rộng hơn thế, và hai sắc trong đó thuộc nhóm dễ mặc nhất.</p>
<h2>Xanh rêu và xanh olive: dễ nhất</h2>
<p>Hai sắc này có xám và vàng pha vào nên trầm, gần nhóm màu đất. Chúng cùng nhiệt độ với tông da ngả vàng, nên đặt lên tay không tạo tương phản gắt. Đây là lý do xanh olive đi làm được trong khi xanh lá tươi thì không.</p>
<h2>Xanh lá tươi: dùng ở dạng nhấn</h2>
<p>Xanh lá tươi rất hút mắt và lạnh. Nếu bạn muốn dùng, làm hai móng nhấn trong bộ nền trắng sữa hoặc nude, thay vì cả mười móng. Dịp Noel thì xanh lá tươi ghép với đỏ là bộ kinh điển, nhưng nên chia tỷ lệ chứ không để hai màu bằng nhau.</p>
<h2>Xanh lá đậm gần đen</h2>
<p>Sắc này trầm và sang, hợp mùa cuối năm, và là nền rất tốt cho đá trắng trong hoặc nhũ vàng. Nó cùng nhóm với burgundy và nâu tây nên dùng được qua Tết.</p>
<h2>Phối với chất liệu gì</h2>
<p>Trên nền xanh đậm, nhũ vàng mịn ăn hơn nhũ bạc, vì vàng cùng nhiệt độ ấm với phần vàng có trong sắc xanh. Đá trắng trong nổi rõ. Nên dùng một chất liệu cho cả bộ.</p>
<h2>Form nào cân đối</h2>
<p>Màu đậm thu nhỏ bề mặt móng, nên móng rất ngắn sơn xanh đậm kín sẽ trông cụt. Chừa khoảng mảnh ở chân móng hoặc chọn form oval.</p>
<p>Bảng giá ở trang <a href="/bang-gia/">Bảng giá</a>. Bộ Noel đỏ xanh có ở bài <a href="/blog/nail-noel-do-xanh/">nail Noel đỏ xanh</a>.</p>''',
 [('Xanh lá có đi làm được không?','Xanh rêu và xanh olive thì được. Xanh lá tươi nên để dạng hai móng nhấn.'),
  ('Xanh đậm nên phối nhũ bạc hay nhũ vàng?','Nhũ vàng ăn hơn, vì nó cùng nhiệt độ ấm với phần vàng trong sắc xanh.')]),
('Green Nails: Three Shades, and Which One Is Everyday',
 'Green is treated as difficult because people picture bright leaf green. Moss and olive are among the easiest colours to wear.',
 'Green Nails — Which Shade Is Everyday | VESSCA',
 'Green nails: moss, olive or bright green — which is wearable daily, which skin tones suit them, and what to pair.',
 ['green nails','olive nails','moss green manicure'],
'''<p>Green gets dismissed because people imagine bright leaf green. The family is wider, and two of its shades are among the easiest to wear.</p>
<h2>Moss and olive: the easy ones</h2>
<p>Both have grey and yellow in them, which puts them near the earth tones. They share a temperature with yellow-undertoned skin, so there is no harsh contrast. That is why olive works at the office and bright green does not.</p>
<h2>Bright green: as an accent</h2>
<p>Use it on two nails in a milky white or nude set rather than all ten. For Christmas, green with red is the classic, but keep the proportion uneven.</p>
<h2>Near-black green</h2>
<p>Deep and elegant, good for the year end, and an excellent base for clear crystals or gold shimmer. It sits with burgundy and deep brown, so it carries into the new year.</p>
<h2>Material</h2>
<p>On a dark green base, fine gold shimmer suits better than silver, since gold matches the warmth inside the green.</p>
<p>Prices on the <a href="/en/bang-gia/">price list</a>.</p>''',
 [('Is green office-appropriate?','Moss and olive are. Keep bright green to two accent nails.'),
  ('Gold or silver shimmer with dark green?','Gold — it matches the warmth already in the colour.')]),
('그린 네일: 세 가지 톤과 일상에 쓸 수 있는 색',
 '그린은 어렵다고 여겨지지만, 그것은 선명한 잎 색을 떠올리기 때문입니다. 모스와 올리브는 가장 쓰기 쉬운 색에 속합니다.',
 '그린 네일 — 일상에 쓸 수 있는 톤 | VESSCA',
 '그린 네일: 모스, 올리브, 선명한 그린 중 일상에 맞는 색과 어울리는 피부톤, 조합할 소재.',
 ['그린 네일','올리브 네일','모스 그린 네일'],
'''<p>그린은 선명한 잎 색을 떠올리기 때문에 제외되곤 합니다. 하지만 그린 계열은 더 넓고, 그중 두 가지는 가장 쓰기 쉬운 색에 속합니다.</p>
<h2>모스와 올리브: 쉬운 쪽</h2>
<p>둘 다 그레이와 옐로가 섞여 어시 톤에 가깝습니다. 옐로 베이스 피부와 색온도가 같아 대비가 거칠지 않습니다. 올리브가 출근용으로 되는 이유입니다.</p>
<h2>선명한 그린: 포인트로</h2>
<p>밀키 화이트나 누드 세트에 두 손가락만. 크리스마스에는 레드와의 조합이 정석이지만 비율을 다르게 두십시오.</p>
<h2>블랙에 가까운 그린</h2>
<p>깊고 우아하며 연말에 좋고, 투명 큐빅이나 골드 펄의 베이스로 훌륭합니다. 버건디, 다크 브라운과 함께 새해까지 이어집니다.</p>
<h2>소재</h2>
<p>다크 그린 베이스에는 실버보다 고운 골드 펄이 맞습니다. 그린 안의 따뜻함과 색온도가 같기 때문입니다.</p>
<p>금액은 <a href="/ko/bang-gia/">가격표</a>에 있습니다.</p>''',
 [('그린이 출근용으로 괜찮을까요?','모스와 올리브는 괜찮습니다. 선명한 그린은 두 손가락 포인트로 두십시오.'),
  ('다크 그린에는 골드와 실버 중 무엇이 맞나요?','골드입니다. 색 안의 따뜻함과 맞습니다.')]),
('綠色美甲：三種綠，哪一種能天天擦',
 '綠色常被當成難駕馭，是因為大家想到的是鮮亮的葉綠。苔綠與橄欖綠其實是最好擦的顏色之一。',
 '綠色美甲 — 哪一種能天天擦 | VESSCA',
 '綠色美甲：苔綠、橄欖綠或鮮綠，哪一種適合日常、適合哪些膚色、搭什麼材質。',
 ['綠色美甲','橄欖綠指甲','苔綠美甲'],
'''<p>綠色常被排除，是因為大家想到鮮亮的葉綠。但綠色家族更寬，其中兩種屬於最好擦的顏色。</p>
<h2>苔綠與橄欖綠：好駕馭的那兩種</h2>
<p>兩者都摻了灰與黃，接近大地色。它們與黃調膚色色溫相同，不會有刺眼的對比。這就是橄欖綠能上班、鮮綠不能的原因。</p>
<h2>鮮綠：當點綴</h2>
<p>在牛奶白或裸色組合中只做兩指。聖誕時綠配紅是經典，但比例要不對等。</p>
<h2>接近黑的深綠</h2>
<p>深沉優雅，適合年末，也是透明鑽與金色珠光的絕佳底色。與酒紅、深棕同列，可以用到新年。</p>
<h2>材質</h2>
<p>深綠底搭細金珠光比銀色合適，因為金與綠裡的暖意色溫相同。</p>
<p>價格請見<a href="/zh/bang-gia/">價目表</a>。</p>''',
 [('綠色適合上班嗎？','苔綠與橄欖綠適合。鮮綠請留給兩指點綴。'),
  ('深綠搭金色還是銀色？','金色。與顏色裡本身的暖意相合。')]))

# ---------------------------------------------------------------- 29
m('nail-mau-vang-mat-meo', 8, 'golden cat eye nails shimmer',
  'Bộ nail mắt mèo tông vàng', 'A gold cat-eye manicure', '골드 캣아이 네일', '金色貓眼美甲',
('Nail màu vàng mắt mèo: dải sáng vàng chạy giữa móng',
 'Mắt mèo tông vàng là sắc ấm nhất trong nhóm mắt mèo, nên nó làm tay trông sáng hơn thay vì tối đi như mắt mèo xanh hay tím.',
 'Nail màu vàng mắt mèo — sắc ấm nhất nhóm mắt mèo',
 'Nail màu vàng mắt mèo: vì sao sắc vàng làm tay sáng, cách dải sáng được tạo ra, và chọn hướng dải nào.',
 ['nail màu vàng mắt mèo','nail mắt mèo vàng','nail mắt mèo champagne','nail mắt mèo ánh vàng'],
'''<p>Sơn mắt mèo có hạt từ tính trong lớp sơn. Khi kỹ thuật viên đưa thanh từ lại gần, các hạt dồn về một phía và để lại một dải sáng chạy dọc móng. Dải sáng đó di chuyển theo góc nhìn, giống con mắt mèo, nên có tên như vậy.</p>
<h2>Vì sao sắc vàng dễ mặc hơn các sắc khác</h2>
<p>Phần lớn sơn mắt mèo là tông lạnh: xanh, tím, xám. Trên tông da ngả vàng, các sắc lạnh đậm tạo tương phản mạnh và dễ làm tay trông tối. Mắt mèo tông vàng, champagne hoặc đồng thì cùng nhiệt độ với da, nên hiệu ứng ngược: tay trông ấm và sáng hơn.</p>
<h2>Hướng dải sáng</h2>
<ul>
<li><b>Dải dọc giữa móng</b> — phổ biến nhất, kéo mắt nhìn theo chiều dài nên ngón trông dài hơn.</li>
<li><b>Dải ngang</b> — lạ mắt hơn nhưng chia ngang bề mặt móng, không nên dùng cho móng ngắn.</li>
<li><b>Dải chéo</b> — mềm, hợp form oval.</li>
</ul>
<p>Với móng ngắn, dải dọc là hướng hợp nhất.</p>
<h2>Khi nào bộ này rất ăn</h2>
<p>Dưới ánh đèn vàng của quán và tiệc tối, dải sáng hiện rõ nhất. Đây là lý do mắt mèo được chọn nhiều cho dịp cuối năm. Ban ngày ngoài trời thì hiệu ứng nhẹ hơn, nhìn gần giống sơn nhũ mịn.</p>
<h2>Có cần thêm chi tiết không</h2>
<p>Không. Bản thân dải sáng đã là chi tiết. Thêm đá hoặc vẽ lên trên thường làm mất hiệu ứng vì chúng chắn mất đường sáng. Nếu muốn nhấn, để một móng trơn cùng tông làm chỗ nghỉ cho mắt.</p>
<p>Bài <a href="/blog/nail-mat-meo-han-quoc/">nail mắt mèo Hàn Quốc</a> nói chung về nhóm sơn này. Bảng giá ở trang <a href="/bang-gia/">Bảng giá</a>.</p>''',
 [('Mắt mèo vàng có hợp móng ngắn không?','Hợp, nếu chọn dải dọc. Dải ngang chia bề mặt móng nên làm móng ngắn trông ngắn thêm.'),
  ('Có nên đính đá lên nền mắt mèo không?','Không nên nhiều. Đá chắn mất dải sáng, vốn là điểm chính của loại sơn này.')]),
('Gold Cat-Eye Nails: A Warm Light Running Down the Nail',
 'Gold is the warmest shade in the cat-eye family, so it brightens the hand instead of darkening it the way blue or violet can.',
 'Gold Cat-Eye Nails — The Warmest Cat-Eye | VESSCA',
 'Gold cat-eye nails: why the warm shade brightens the hand, how the light band is made, and which direction to choose.',
 ['gold cat eye nails','champagne cat eye','magnetic gel nails'],
'''<p>Cat-eye gel holds magnetic particles. A magnet drawn near gathers them to one side and leaves a band of light down the nail that shifts as the hand moves.</p>
<h2>Why gold is the easiest shade</h2>
<p>Most cat-eye gels are cool: blue, violet, grey. On yellow-undertoned skin, deep cool shades contrast strongly and can darken the hand. Gold, champagne and bronze share the skin's warmth, so the hand reads brighter.</p>
<h2>Direction of the band</h2>
<ul><li><b>Vertical down the centre</b> — the most common; it lengthens the finger.</li><li><b>Horizontal</b> — more unusual, but it cuts the nail across; avoid on short nails.</li><li><b>Diagonal</b> — softer, suits an oval shape.</li></ul>
<h2>When it looks best</h2>
<p>Under warm evening light the band is at its strongest, which is why cat-eye is popular at year end. In daylight the effect is subtler, closer to a fine shimmer.</p>
<h2>Leave it alone</h2>
<p>The band is the detail. Stones placed on top block the light line. If you want an accent, keep one plain nail in the same tone.</p>
<p>Prices on the <a href="/en/bang-gia/">price list</a>.</p>''',
 [('Does it suit short nails?','Yes with a vertical band. Horizontal bands shorten the nail visually.'),
  ('Should I add stones?','Not many — they block the light band, which is the whole point.')]),
('골드 캣아이 네일: 손톱을 따라 흐르는 따뜻한 빛',
 '골드는 캣아이 중 가장 따뜻한 톤이라, 블루나 바이올렛처럼 손을 어둡게 하지 않고 밝게 보이게 합니다.',
 '골드 캣아이 네일 — 가장 따뜻한 캣아이 | VESSCA',
 '골드 캣아이 네일: 따뜻한 톤이 손을 밝게 하는 이유, 빛의 띠가 생기는 원리, 방향 선택.',
 ['골드 캣아이 네일','샴페인 캣아이','매그네틱 젤'],
'''<p>캣아이 젤에는 자성 입자가 들어 있습니다. 자석을 가까이 대면 입자가 한쪽으로 모여 손톱을 따라 빛의 띠가 남고, 손을 움직이면 그 띠가 따라 움직입니다.</p>
<h2>골드가 가장 쉬운 이유</h2>
<p>대부분의 캣아이는 블루, 바이올렛, 그레이 같은 쿨 톤입니다. 옐로 베이스 피부에서 깊은 쿨 톤은 대비가 강해 손이 어두워 보일 수 있습니다. 골드, 샴페인, 브론즈는 피부의 따뜻함과 같아 손이 밝아 보입니다.</p>
<h2>띠의 방향</h2>
<ul><li><b>세로 중앙</b> — 가장 흔하며 손가락이 길어 보입니다.</li><li><b>가로</b> — 독특하지만 손톱을 가로로 끊어 짧은 손톱에는 권하지 않습니다.</li><li><b>사선</b> — 부드럽고 오벌 셰이프에 맞습니다.</li></ul>
<h2>가장 예쁜 순간</h2>
<p>따뜻한 저녁 조명에서 띠가 가장 선명합니다. 연말에 캣아이가 인기 있는 이유입니다.</p>
<p>금액은 <a href="/ko/bang-gia/">가격표</a>에 있습니다.</p>''',
 [('짧은 손톱에도 맞나요?','세로 띠라면 맞습니다. 가로 띠는 짧아 보이게 합니다.'),
  ('큐빅을 올려도 될까요?','많이는 권하지 않습니다. 빛의 띠를 가립니다.')]),
('金色貓眼美甲：沿著指甲流動的暖光',
 '金色是貓眼裡最暖的色調，所以它讓手變亮，而不像藍或紫那樣讓手顯暗。',
 '金色貓眼美甲 — 最暖的貓眼 | VESSCA',
 '金色貓眼美甲：暖色調讓手變亮的原因、光帶的形成原理，以及方向的選擇。',
 ['金色貓眼美甲','香檳貓眼','磁石膠美甲'],
'''<p>貓眼膠裡含有磁性顆粒。技術人員把磁棒靠近，顆粒聚到一側，在指甲上留下一道光帶，手一動光帶也跟著動。</p>
<h2>金色最好駕馭的原因</h2>
<p>多數貓眼膠是冷色：藍、紫、灰。在黃調膚色上，深冷色對比強烈，容易讓手顯暗。金色、香檳與古銅與膚色的暖意相同，手反而更亮。</p>
<h2>光帶方向</h2>
<ul><li><b>直向正中</b> — 最常見，讓手指顯長。</li><li><b>橫向</b> — 較特別，但會橫切甲面，短甲不建議。</li><li><b>斜向</b> — 柔和，適合橢圓形。</li></ul>
<h2>什麼時候最好看</h2>
<p>暖黃的夜間燈光下光帶最明顯，這是貓眼在年末受歡迎的原因。</p>
<p>價格請見<a href="/zh/bang-gia/">價目表</a>。</p>''',
 [('短甲適合嗎？','直向光帶適合。橫向會讓指甲視覺上更短。'),
  ('可以貼鑽嗎？','不建議多貼，會遮住光帶。')]))

# ---------------------------------------------------------------- 30
m('nail-mau-xanh-bien', 9, 'navy blue nails deep manicure',
  'Bộ nail màu xanh biển', 'A deep sea-blue manicure', '네이비 블루 네일', '海藍色美甲',
('Nail màu xanh biển: từ xanh navy tới xanh nước nhạt',
 'Xanh biển gồm cả navy đậm và xanh nước nhạt, hai đầu rất khác nhau. Bài này phân biệt và chỉ cách chọn cho đúng dịp.',
 'Nail màu xanh biển — navy hay xanh nước nhạt',
 'Nail màu xanh biển: phân biệt navy đậm và xanh nước nhạt, sắc nào hợp tông da nào và dịp nào nên dùng.',
 ['nail màu xanh biển','nail xanh navy','nail xanh dương','nail xanh nước'],
'''<p>Khi khách nói muốn màu xanh biển, hai người có thể đang nghĩ tới hai màu rất khác: navy đậm gần đen, hoặc xanh nước nhạt kiểu nước biển cạn. Nên nói rõ trước khi làm.</p>
<h2>Navy đậm</h2>
<p>Đây là sắc dễ mặc nhất trong nhóm xanh. Nó đủ đậm để trông như một màu trung tính, gần như đen nhưng mềm hơn. Hợp mùa cuối năm, hợp tiệc tối, và là nền rất tốt cho đá trắng trong hoặc nhũ bạc. Navy cũng ít làm tối tay hơn xanh trung bình, vì ở độ đậm đó mắt đọc nó là màu nền chứ không so sánh với da.</p>
<h2>Xanh nước nhạt</h2>
<p>Sắc này tươi, lạnh và nhẹ, thuộc nhóm màu mùa nắng. Trên tông da ngả vàng, nó tạo tương phản lạnh nên có thể làm tay trông xám. Cách xử lý giống Tiffany blue: chọn sắc đục hơn, hoặc dùng ở dạng hai móng nhấn trong bộ trắng sữa.</p>
<h2>Sắc giữa: xanh dương trung bình</h2>
<p>Đây là sắc khó nhất. Không đủ đậm để thành trung tính, không đủ nhạt để thành pastel, nên nó nổi theo kiểu hơi thô trên tay. Nếu thích xanh dương, nên đi về một trong hai đầu.</p>
<h2>Dịp nào dùng sắc nào</h2>
<ul>
<li><b>Tiệc cuối năm, tất niên:</b> navy đậm với một chất liệu nhấn.</li>
<li><b>Đi biển, du lịch:</b> xanh nước nhạt, dạng trơn hoặc hai móng nhấn.</li>
<li><b>Đi làm:</b> navy đậm trơn, không chi tiết.</li>
</ul>
<p>Bài <a href="/blog/nail-di-bien-du-lich/">nail đi biển, du lịch</a> và <a href="/blog/nail-tat-nien-cong-ty/">nail tất niên công ty</a> nói riêng từng dịp. Bảng giá ở trang <a href="/bang-gia/">Bảng giá</a>.</p>''',
 [('Navy có hợp đi làm không?','Hợp. Ở độ đậm đó navy trông như một màu trung tính, gần đen nhưng mềm hơn.'),
  ('Da ngăm làm xanh nước nhạt được không?','Nên chọn sắc đục hơn hoặc chỉ làm hai móng nhấn, vì sắc lạnh nhạt dễ làm tay trông xám.')]),
('Sea-Blue Nails: From Deep Navy to Pale Water',
 'Sea blue covers both deep navy and pale water blue — two very different ends. Here is how to tell a client which one they mean.',
 'Sea-Blue Nails — Navy or Pale Water | VESSCA',
 'Sea-blue nails: deep navy versus pale water blue, which suits which skin tone, and which occasion calls for each.',
 ['navy nails','sea blue manicure','blue nail colour'],
'''<p>Two people asking for sea blue may picture very different colours: a navy close to black, or a pale shallow-water blue.</p>
<h2>Deep navy</h2>
<p>The easiest blue to wear. It is dark enough to read as a neutral — nearly black but softer. It suits the year end and evening events, and it is an excellent base for clear crystals or silver shimmer. It also darkens the hand less than a mid blue, because at that depth the eye reads it as a background rather than comparing it to skin.</p>
<h2>Pale water blue</h2>
<p>Fresh, cool and light — a sunny-season colour. On yellow undertones it contrasts coolly and can grey the hand. Same fix as Tiffany blue: a more opaque version, or two accent nails in a milky white set.</p>
<h2>The middle is hardest</h2>
<p>A mid blue is neither neutral nor pastel, so it stands out somewhat bluntly. Go to one end or the other.</p>
<h2>By occasion</h2>
<ul><li><b>Year-end parties:</b> deep navy with one accent material.</li><li><b>Beach and travel:</b> pale water blue.</li><li><b>Office:</b> plain deep navy.</li></ul>
<p>Prices on the <a href="/en/bang-gia/">price list</a>.</p>''',
 [('Is navy office-appropriate?','Yes. At that depth it reads as a neutral, nearly black but softer.'),
  ('Pale blue on tanned skin?','Use a more opaque version, or keep it to two accent nails.')]),
('네이비 블루 네일: 딥 네이비부터 연한 물빛까지',
 '바다색이라는 말에는 딥 네이비와 연한 물빛이 모두 들어갑니다. 양쪽 끝이 매우 다릅니다.',
 '네이비 블루 네일 — 네이비냐 물빛이냐 | VESSCA',
 '바다색 네일: 딥 네이비와 연한 물빛의 차이, 어울리는 피부톤과 상황별 선택.',
 ['네이비 네일','블루 네일','물빛 네일'],
'''<p>바다색을 원한다고 할 때 두 사람이 서로 다른 색을 떠올릴 수 있습니다. 블랙에 가까운 네이비, 또는 얕은 바닷물 같은 연한 블루입니다.</p>
<h2>딥 네이비</h2>
<p>블루 중 가장 쓰기 쉽습니다. 충분히 어두워 중립색처럼 읽히고, 블랙보다 부드럽습니다. 연말과 저녁 자리에 맞고 투명 큐빅이나 실버 펄의 베이스로 좋습니다. 중간 톤 블루보다 손을 덜 어둡게 합니다.</p>
<h2>연한 물빛</h2>
<p>상쾌하고 차갑고 가벼운 여름 색입니다. 옐로 베이스에서는 차가운 대비로 손이 회색빛이 될 수 있습니다. 불투명한 버전이나 두 손가락 포인트로 쓰십시오.</p>
<h2>중간이 가장 어렵습니다</h2>
<p>중간 톤 블루는 중립도 파스텔도 아니어서 다소 투박하게 튑니다. 양쪽 끝 중 하나로 가십시오.</p>
<p>금액은 <a href="/ko/bang-gia/">가격표</a>에 있습니다.</p>''',
 [('네이비가 출근용으로 괜찮나요?','괜찮습니다. 그 깊이에서는 중립색처럼 읽힙니다.'),
  ('태닝된 피부에 연한 블루는요?','불투명한 버전이나 두 손가락 포인트로 쓰십시오.')]),
('海藍色美甲：從深海軍藍到淺水藍',
 '所謂海藍，包含深海軍藍與淺水藍，兩端差別很大。',
 '海藍色美甲 — 海軍藍或淺水藍 | VESSCA',
 '海藍色美甲：深海軍藍與淺水藍的差別、適合的膚色，以及場合上的選擇。',
 ['海軍藍美甲','藍色指甲','水藍色美甲'],
'''<p>兩個人說想做海藍色，腦中可能是很不同的顏色：接近黑的海軍藍，或淺淺的水藍。</p>
<h2>深海軍藍</h2>
<p>藍色裡最好駕馭的。它夠深，讀起來像中性色，接近黑但更柔。適合年末與晚宴，也是透明鑽與銀色珠光的好底色。比中間調的藍更不容易讓手顯暗。</p>
<h2>淺水藍</h2>
<p>清爽、冷、輕，屬夏季色。在黃調膚色上冷對比明顯，可能讓手顯灰。改用更不透明的版本，或只做兩指點綴。</p>
<h2>中間最難</h2>
<p>中間調的藍既不中性也不粉彩，會有些生硬地跳出來。往兩端選一邊。</p>
<p>價格請見<a href="/zh/bang-gia/">價目表</a>。</p>''',
 [('海軍藍適合上班嗎？','適合。在那個深度讀起來像中性色。'),
  ('膚色深能用淺水藍嗎？','用更不透明的版本，或只做兩指點綴。')]))
