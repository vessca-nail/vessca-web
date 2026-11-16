"""Đợt 16/11/2026 — cụm bài TÌM QUANH ĐÂY (chủ tiệm cho biết khách đặt lịch hay search
"tiệm nail quanh đây", "tiệm nail gần đây"). Mốc quanh tiệm đã đối chiếu bằng Google Maps:
chợ Bà Chiểu, Lăng Ông Bà Chiểu (Lăng Lê Văn Duyệt), Bệnh viện Nhân dân Gia Định (1 Nơ Trang Long),
THCS Hà Huy Tập (7 Phan Đăng Lưu), TH Nguyễn Đình Chiểu (1 Lê Quang Định), TH/THCS Yên Thế (377/399 Lê Quang Định).
KHÔNG ghi số km hay số phút cụ thể — chưa đo; chỉ nói cùng đường / cùng khu và bảo khách mở Google Maps."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *

H, Q, G = 'Hậu trường VESSCA', 'Hỏi & Đáp', 'Gội đầu & Thư giãn'

# ---------- 1. Tiệm nail gần đây / quanh đây ----------
vi = '''<p>Nhiều người mở điện thoại gõ "tiệm nail gần đây" rồi chọn đại một chỗ trong danh sách hiện ra. Cách đó nhanh, nhưng gần nhà không có nghĩa là hợp. Bài này gợi ý vài điều nên xem trước khi bấm chỉ đường, và chỉ rõ VESSCA nằm ở đâu để bạn biết tiệm có thuộc "quanh đây" của bạn không.</p>

<h2>Bốn điều nên xem trước khi đi</h2>

<table>
<thead><tr><th>Xem gì</th><th>Vì sao</th></tr></thead>
<tbody>
<tr><td>Bảng giá công khai</td><td>Biết trước phải trả bao nhiêu, không bị cộng thêm lúc tính tiền</td></tr>
<tr><td>Cách tiệm xử lý dụng cụ</td><td>Dụng cụ kim loại nên được tiệt trùng bằng máy sau mỗi khách</td></tr>
<tr><td>Có nhận đặt lịch không</td><td>Đặt trước thì không phải ngồi chờ, nhất là buổi tối và cuối tuần</td></tr>
<tr><td>Ảnh thật của tiệm</td><td>Ảnh do tiệm tự chụp cho bạn hình dung đúng tay nghề hơn ảnh sưu tầm</td></tr>
</tbody>
</table>

<p>Chi tiết cách nhìn một tiệm lạ có ở bài <a href="/blog/chon-tiem-nail-uy-tin-binh-thanh/">chọn tiệm nail uy tín ở Bình Thạnh</a>.</p>

<h2>VESSCA nằm ở đâu</h2>

<p>Địa chỉ: 251/30 Lê Quang Định, phường Gia Định, TP.HCM, tức khu Bình Thạnh cũ. Vài mốc quen thuộc cùng khu để bạn dễ hình dung:</p>

<ul>
<li>Cùng phường với <strong>chợ Bà Chiểu</strong> và <strong>Lăng Ông Bà Chiểu</strong> (Lăng Lê Văn Duyệt).</li>
<li>Cùng khu với <strong>Bệnh viện Nhân dân Gia Định</strong> ở 1 Nơ Trang Long.</li>
<li>Cùng đường Lê Quang Định với <strong>Trường Tiểu học Nguyễn Đình Chiểu</strong> và <strong>Trường Yên Thế</strong>.</li>
<li>Giáp ranh <strong>Phú Nhuận</strong> và <strong>Gò Vấp</strong>.</li>
</ul>

<p>Tiệm nằm trong hẻm 251, có chỗ để xe trước tiệm. Cách tìm hẻm có ở bài <a href="/blog/den-vessca-gui-xe-dat-lich/">đến VESSCA: tìm hẻm, gửi xe và đặt lịch</a>. Để biết chính xác quãng đường từ chỗ bạn, mở Google Maps và tìm "VESSCA Nail" rồi bấm chỉ đường.</p>

<h2>Nếu bạn ở các khu lân cận</h2>

<ul>
<li><strong>Phú Nhuận, Gò Vấp:</strong> xem bài <a href="/blog/tiem-nail-gan-phu-nhuan-go-vap/">tiệm nail kiểu Hàn gần Phú Nhuận, Gò Vấp</a>.</li>
<li><strong>Khu Quận 2 cũ, Thủ Đức:</strong> xem bài <a href="/blog/nail-han-quoc-cho-khach-quan-2-thu-duc/">khách Quận 2, Thủ Đức có nên qua Bình Thạnh</a>.</li>
<li><strong>Quanh chợ Bà Chiểu:</strong> xem bài <a href="/blog/tiem-nail-gan-cho-ba-chieu/">tiệm nail gần chợ Bà Chiểu</a>.</li>
</ul>

<h2>Làm được gì trong một lần ghé</h2>

<p>Sơn gel trơn 130.000₫, sơn thạch 150.000₫, mắt mèo 170.000₫; cắt da, chỉnh form, dưỡng viền tay 60.000₫. Tiệm cũng có gội đầu thư giãn từ 99.000₫, đặt chung một lịch với nail được. Bảng giá đầy đủ ở trang <a href="/bang-gia/">bảng giá</a>.</p>

<p>Tiệm phục vụ số khách giới hạn cùng lúc nên nếu bạn định ghé ngay, hãy gọi 0933.528.501 hỏi giờ trống, hoặc đặt ở mục <a href="/#booking">Đặt lịch</a>.</p>'''
faq = [('Tiệm nail gần đây có gì khác nhau?', 'Khác ở bảng giá công khai, cách tiệt trùng dụng cụ, có nhận đặt lịch hay không và ảnh thật của tiệm.'),
       ('VESSCA ở khu nào?', '251/30 Lê Quang Định, phường Gia Định (Bình Thạnh cũ), cùng phường với chợ Bà Chiểu và Lăng Ông, giáp Phú Nhuận và Gò Vấp.'),
       ('Ghé ngay không đặt lịch được không?', 'Nên gọi 0933.528.501 hỏi giờ trống trước, vì tiệm phục vụ số khách giới hạn cùng lúc.'),
       ('Có chỗ để xe không?', 'Có chỗ để xe trước tiệm, trong hẻm 251 Lê Quang Định.')]
en = '''<p>Searching "nail salon near me" is quick, but close to home does not always mean a good fit. Here is what to check before tapping directions, and where VESSCA actually is.</p>
<h2>Four things to check</h2>
<ul><li>A published price list, so nothing is added at the till</li><li>How tools are handled: metal tools machine-sterilised after every guest</li><li>Whether the salon takes bookings, which saves waiting</li><li>Real photos taken in the salon rather than stock images</li></ul>
<h2>Where VESSCA is</h2>
<p>251/30 Le Quang Dinh, Gia Dinh ward (formerly Binh Thanh). It is in the same ward as Ba Chieu market and the Le Van Duyet Tomb, near Nhan Dan Gia Dinh Hospital, and borders Phu Nhuan and Go Vap. Parking is in front of the salon, inside alley 251. Search "VESSCA Nail" on Google Maps for directions from where you are.</p>
<h2>In one visit</h2>
<p>Plain gel 130,000₫, jelly 150,000₫, cat-eye 170,000₫; cuticle care and shaping for hands 60,000₫. A relaxing hair wash starts at 99,000₫ and can be booked in the same appointment. The salon serves a limited number of guests at a time, so call 0933.528.501 or use the <a href="/en/#booking">booking form</a>.</p>'''
ko = '''<p>"근처 네일샵"을 검색하면 빠르지만, 가깝다고 꼭 맞는 곳은 아닙니다. 길찾기를 누르기 전에 확인할 것과 VESSCA의 위치를 정리했습니다.</p>
<h2>확인할 네 가지</h2>
<ul><li>공개된 가격표 — 계산할 때 추가 요금이 붙지 않습니다</li><li>도구 관리 — 금속 도구는 손님마다 기계로 멸균</li><li>예약 가능 여부 — 기다리지 않아도 됩니다</li><li>샵에서 직접 찍은 사진인지</li></ul>
<h2>VESSCA 위치</h2>
<p>251/30 Le Quang Dinh, 자딘 동(옛 빈탄)입니다. 벤짜이 시장, 레반주엣 묘와 같은 동이고 자딘 병원 인근이며 푸뉴언·고밥과 맞닿아 있습니다. 251번 골목 안, 샵 앞 주차 가능합니다. 구글 지도에서 "VESSCA Nail"을 검색해 길을 확인하세요.</p>
<h2>한 번 방문으로</h2>
<p>원컬러 젤 130,000₫, 시럽 150,000₫, 자석 170,000₫, 손 큐티클 케어 60,000₫. 헤드 스파는 99,000₫부터이며 같이 예약하실 수 있습니다. 동시 손님 수를 제한하므로 0933.528.501로 연락 주세요.</p>'''
zh = '''<p>搜索"附近的美甲店"很快,但离家近不等于合适。下面是按下导航前值得先看的几点,以及 VESSCA 的具体位置。</p>
<h2>先看四件事</h2>
<ul><li>公开的价目表,结账时不会另加费用</li><li>工具如何处理:金属工具每位客人用后经机器消毒</li><li>是否接受预约,可以免去等待</li><li>是否为店内实拍照片</li></ul>
<h2>VESSCA 在哪里</h2>
<p>251/30 Le Quang Dinh,嘉定坊(原平盛郡)。与 Ba Chieu 市场、黎文悦墓同坊,邻近嘉定人民医院,并紧邻富润郡和鹅邑郡。店位于 251 巷内,门前可停车。在 Google 地图搜索"VESSCA Nail"即可导航。</p>
<h2>一次到店可以做什么</h2>
<p>纯色凝胶 130,000₫、果冻 150,000₫、猫眼 170,000₫;手部修死皮修形 60,000₫。洗发 99,000₫ 起,可与美甲一起预约。店内限客接待,请致电 0933.528.501。</p>'''
bai('tiem-nail-gan-day-chon-the-nao', '2026-11-16T09:00:00+07:00', Q,
 A(('nail salon manicure', 'Tìm tiệm nail gần đây trên điện thoại', 'Looking up a nail salon nearby', '근처 네일샵 찾기', '查找附近的美甲店'), []),
 ('Tìm "tiệm nail gần đây": nên xem gì trước khi bấm chỉ đường',
  'Gõ "tiệm nail gần đây" ra một danh sách dài. Bốn điều nên xem trước khi chọn, và VESSCA nằm ở mốc nào trong khu Bình Thạnh, Gia Định.',
  'Tiệm nail gần đây ở Bình Thạnh: chọn thế nào | VESSCA',
  'Tìm tiệm nail gần đây quanh Bình Thạnh, Gia Định? Xem bảng giá, cách tiệt trùng, đặt lịch. VESSCA ở 251/30 Lê Quang Định, gần chợ Bà Chiểu.',
  ['tiệm nail gần đây', 'tiệm nail quanh đây', 'nail gần đây', 'tiệm nail Bình Thạnh', 'làm nail gần đây'], vi, faq),
 ('"Nail Salon Near Me": What to Check First',
  'What to look at before tapping directions, and where VESSCA is in Binh Thanh.',
  'Nail Salon Near Me in Binh Thanh | VESSCA',
  'Looking for a nail salon near you in Binh Thanh, Saigon? Check prices, sterilisation and booking. VESSCA, 251/30 Le Quang Dinh.',
  ['nail salon near me', 'nail salon Binh Thanh', 'nail salon Saigon'], en,
  [('How do nearby salons differ?', 'In published prices, tool sterilisation, whether they take bookings, and whether photos are their own.'),
   ('Where is VESSCA?', '251/30 Le Quang Dinh, Gia Dinh ward, near Ba Chieu market, bordering Phu Nhuan and Go Vap.')]),
 ('"근처 네일샵" 검색, 무엇을 먼저 볼까',
  '길찾기를 누르기 전 확인할 것과 빈탄 VESSCA의 위치.',
  '근처 네일샵 빈탄 | 호치민 VESSCA',
  '호치민 빈탄 근처 네일샵을 찾으신다면: 가격표, 멸균, 예약 확인. VESSCA, 251/30 Le Quang Dinh.',
  ['호치민 근처 네일샵', '빈탄 네일샵', '호치민 네일'], ko,
  [('가까운 샵은 무엇이 다른가요?', '공개 가격표, 도구 멸균, 예약 가능 여부, 직접 찍은 사진 여부가 다릅니다.'),
   ('위치가 어디인가요?', '251/30 Le Quang Dinh, 자딘 동이며 벤짜이 시장 인근입니다.')]),
 ('搜"附近美甲店"先看什么',
  '按下导航前值得确认的几点,以及 VESSCA 在平盛郡的位置。',
  '附近的美甲店 平盛郡 | 胡志明 VESSCA',
  '在胡志明平盛郡找附近的美甲店?先看价目表、消毒与预约。VESSCA,251/30 Le Quang Dinh。',
  ['胡志明 附近美甲', '平盛郡 美甲', '胡志明 美甲店'], zh,
  [('附近的店有什么不同?', '公开价目表、工具消毒、是否接受预约、照片是否实拍。'),
   ('店在哪里?', '251/30 Le Quang Dinh,嘉定坊,邻近 Ba Chieu 市场。')]))

# ---------- 2. Gần Bệnh viện Nhân dân Gia Định, Lăng Ông ----------
vi = '''<p>Nếu bạn đang ở khu Bệnh viện Nhân dân Gia Định, Lăng Ông Bà Chiểu hay Phan Đăng Lưu và muốn tìm chỗ làm nail hoặc gội đầu, VESSCA nằm cùng khu đó: 251/30 Lê Quang Định, phường Gia Định.</p>

<h2>Những mốc quen cùng khu</h2>

<table>
<thead><tr><th>Mốc</th><th>Địa chỉ</th></tr></thead>
<tbody>
<tr><td>Bệnh viện Nhân dân Gia Định</td><td>1 Nơ Trang Long</td></tr>
<tr><td>Lăng Ông Bà Chiểu (Lăng Lê Văn Duyệt)</td><td>Đường Lê Văn Duyệt</td></tr>
<tr><td>Chợ Bà Chiểu</td><td>Khu Bà Chiểu, phường Gia Định</td></tr>
<tr><td>VESSCA</td><td>251/30 Lê Quang Định, trong hẻm 251</td></tr>
</tbody>
</table>

<p>Tất cả đều nằm trong phường Gia Định, khu Bình Thạnh cũ. Quãng đường thực tế từ chỗ bạn thì mở Google Maps tìm "VESSCA Nail" sẽ chính xác hơn.</p>

<h2>Có khoảng một tiếng thì làm được gì</h2>

<ul>
<li><strong>Khoảng 30 phút:</strong> cắt da, chỉnh form, dưỡng viền tay 60.000₫; hoặc gội đầu gói 30 phút từ 99.000₫.</li>
<li><strong>Khoảng 45–60 phút:</strong> sơn gel trơn 130.000₫, sơn thạch 150.000₫; Hand Ritual 250.000₫.</li>
<li><strong>Hơn một tiếng:</strong> đắp gel 250.000₫, dual form 350.000₫, hoặc Gói thiên đường 75 phút.</li>
</ul>

<p>Nếu móng đang có gel cũ, cộng thêm khoảng 20 phút phá gel (30.000₫). Lý do bước này cần thời gian có ở bài <a href="/blog/vi-sao-thao-gel-mat-20-phut/">vì sao tháo gel mất 20 phút</a>.</p>

<h2>Khi đi cùng người nhà</h2>

<p>Nếu bạn đi cùng mẹ hoặc người lớn tuổi, gói gội đầu 30 phút hoặc Foot Ritual 350.000₫ là lựa chọn nhẹ nhàng. Tiệm phục vụ số khách giới hạn cùng lúc nên nhóm từ hai người trở lên hãy gọi 0933.528.501 trước để tiệm sắp xếp.</p>

<h2>Giờ mở cửa và đặt lịch</h2>

<p>Tiệm mở 9:00–20:30 mỗi ngày, kể cả cuối tuần. Đặt ở mục <a href="/#booking">Đặt lịch</a> hoặc gọi 0933.528.501. Đường vào hẻm và chỗ để xe có trong bài <a href="/blog/den-vessca-gui-xe-dat-lich/">đến VESSCA: tìm hẻm, gửi xe và đặt lịch</a>. Bảng giá đầy đủ ở trang <a href="/bang-gia/">bảng giá</a>.</p>'''
faq = [('Có tiệm nail nào gần Bệnh viện Nhân dân Gia Định không?', 'VESSCA ở 251/30 Lê Quang Định, cùng phường Gia Định với bệnh viện.'),
       ('Gần Lăng Ông Bà Chiểu có chỗ làm nail không?', 'Có, VESSCA nằm cùng phường Gia Định với Lăng Ông và chợ Bà Chiểu.'),
       ('Có khoảng 30 phút thì làm được gì?', 'Cắt da, chỉnh form, dưỡng viền tay 60.000₫ hoặc gói gội đầu 30 phút từ 99.000₫.')]
en = '''<p>If you are around Nhan Dan Gia Dinh Hospital, the Le Van Duyet Tomb or Phan Dang Luu street, VESSCA is in the same area: 251/30 Le Quang Dinh, Gia Dinh ward.</p>
<h2>Landmarks in the same ward</h2>
<ul><li>Nhan Dan Gia Dinh Hospital, 1 No Trang Long</li><li>Le Van Duyet Tomb (Lang Ong Ba Chieu)</li><li>Ba Chieu market</li><li>VESSCA, inside alley 251 Le Quang Dinh</li></ul>
<p>For the real distance from where you are, search "VESSCA Nail" on Google Maps.</p>
<h2>If you have about an hour</h2>
<p>About 30 minutes: cuticle care and shaping for hands 60,000₫, or a 30-minute hair wash from 99,000₫. About 45–60 minutes: plain gel 130,000₫, jelly 150,000₫, or the Hand Ritual 250,000₫. Longer: builder gel 250,000₫, dual form 350,000₫, or the 75-minute Paradise Ritual. Add about 20 minutes if old gel needs removing (30,000₫).</p>
<h2>Hours</h2>
<p>Open 9:00–20:30 daily. Book through the <a href="/en/#booking">booking form</a> or call 0933.528.501; for two or more people, call ahead.</p>'''
ko = '''<p>자딘 병원, 레반주엣 묘, 판당르우 거리 근처에 계신다면 VESSCA도 같은 지역입니다. 251/30 Le Quang Dinh, 자딘 동입니다.</p>
<h2>같은 동의 주요 지점</h2>
<ul><li>자딘 인민병원, 1 No Trang Long</li><li>레반주엣 묘(랑옹 벤짜이)</li><li>벤짜이 시장</li><li>VESSCA, Le Quang Dinh 251번 골목 안</li></ul>
<p>실제 거리는 구글 지도에서 "VESSCA Nail"을 검색해 확인하세요.</p>
<h2>한 시간 정도 있다면</h2>
<p>30분: 손 큐티클 케어 60,000₫ 또는 30분 샴푸 99,000₫부터. 45–60분: 원컬러 젤 130,000₫, 시럽 150,000₫, 핸드 리추얼 250,000₫. 그 이상: 젤 연장 250,000₫, 듀얼폼 350,000₫, 75분 파라다이스 리추얼. 기존 젤 제거는 약 20분(30,000₫)이 더 걸립니다.</p>
<h2>영업시간</h2>
<p>매일 9:00–20:30. <a href="/ko/#booking">예약 양식</a> 또는 0933.528.501로 예약하세요. 2인 이상은 미리 연락 주세요.</p>'''
zh = '''<p>如果您在嘉定人民医院、黎文悦墓或 Phan Dang Luu 街一带,VESSCA 就在同一区域:251/30 Le Quang Dinh,嘉定坊。</p>
<h2>同坊的几个地标</h2>
<ul><li>嘉定人民医院,1 No Trang Long</li><li>黎文悦墓(Lang Ong Ba Chieu)</li><li>Ba Chieu 市场</li><li>VESSCA,Le Quang Dinh 251 巷内</li></ul>
<p>实际距离请在 Google 地图搜索"VESSCA Nail"查看。</p>
<h2>大约一小时可以做什么</h2>
<p>约 30 分钟:手部修死皮修形 60,000₫,或 30 分钟洗发 99,000₫ 起。约 45–60 分钟:纯色凝胶 130,000₫、果冻 150,000₫、Hand Ritual 250,000₫。更长:延长凝胶 250,000₫、双型膜 350,000₫,或 75 分钟天堂套餐。若需卸旧甲,另加约 20 分钟(30,000₫)。</p>
<h2>营业时间</h2>
<p>每天 9:00–20:30。可用<a href="/zh/#booking">预约表单</a>或致电 0933.528.501;两人以上请提前联系。</p>'''
bai('nail-goi-dau-gan-benh-vien-gia-dinh', '2026-11-16T14:30:00+07:00', Q,
 A(('nail salon manicure', 'Làm nail ở khu Bà Chiểu, Gia Định', 'Nails done in the Ba Chieu area', '벤짜이 지역에서 받는 네일', '在 Ba Chieu 一带做美甲'), []),
 ('Làm nail, gội đầu gần Bệnh viện Gia Định và Lăng Ông Bà Chiểu',
  'Đang ở khu Bệnh viện Nhân dân Gia Định, Lăng Ông hay Phan Đăng Lưu: VESSCA nằm cùng phường, có khoảng một tiếng thì làm được những gì.',
  'Nail, gội đầu gần Bệnh viện Gia Định, Lăng Ông | VESSCA',
  'Làm nail và gội đầu gần Bệnh viện Nhân dân Gia Định, Lăng Ông Bà Chiểu: VESSCA ở 251/30 Lê Quang Định, mở 9:00–20:30 mỗi ngày.',
  ['nail gần Bệnh viện Gia Định', 'nail gần Lăng Ông', 'tiệm nail Bà Chiểu', 'nail Phan Đăng Lưu', 'tiệm nail gần đây'], vi, faq),
 ('Nails and a Hair Wash near Gia Dinh Hospital and Lang Ong',
  'In the Gia Dinh Hospital or Lang Ong area: where VESSCA is and what fits in an hour.',
  'Nails near Gia Dinh Hospital, Saigon | VESSCA',
  'Nails and a hair wash near Nhan Dan Gia Dinh Hospital and the Le Van Duyet Tomb: VESSCA, 251/30 Le Quang Dinh, open 9:00–20:30.',
  ['nail salon Ba Chieu', 'nail salon near Gia Dinh Hospital', 'nail salon Binh Thanh'], en,
  [('Is there a nail salon near Gia Dinh Hospital?', 'VESSCA is at 251/30 Le Quang Dinh, in the same ward as the hospital.'),
   ('What fits in 30 minutes?', 'Cuticle care and shaping for hands 60,000₫, or a 30-minute hair wash from 99,000₫.')]),
 ('자딘 병원·랑옹 근처에서 네일과 헤드 스파',
  '자딘 병원, 랑옹 근처에 계신다면: VESSCA 위치와 한 시간 안에 가능한 시술.',
  '자딘 병원 근처 네일 | 호치민 VESSCA',
  '호치민 자딘 인민병원·레반주엣 묘 근처 네일과 헤드 스파: VESSCA, 251/30 Le Quang Dinh, 매일 9:00–20:30.',
  ['벤짜이 네일', '자딘 병원 근처 네일', '빈탄 네일샵'], ko,
  [('병원 근처에 네일샵이 있나요?', 'VESSCA가 같은 동인 251/30 Le Quang Dinh에 있습니다.'),
   ('30분이면 무엇이 되나요?', '손 큐티클 케어 60,000₫ 또는 30분 샴푸 99,000₫부터입니다.')]),
 ('嘉定医院、黎文悦墓附近做美甲与洗发',
  '在嘉定人民医院或黎文悦墓一带:VESSCA 的位置,以及一小时内能做什么。',
  '嘉定医院附近美甲 | 胡志明 VESSCA',
  '胡志明嘉定人民医院、黎文悦墓附近的美甲与洗发:VESSCA,251/30 Le Quang Dinh,每天 9:00–20:30。',
  ['Ba Chieu 美甲', '嘉定医院 附近美甲', '平盛郡 美甲'], zh,
  [('医院附近有美甲店吗?', 'VESSCA 就在同坊的 251/30 Le Quang Dinh。'),
   ('30 分钟能做什么?', '手部修死皮修形 60,000₫,或 30 分钟洗发 99,000₫ 起。')]))

# ---------- 3. Nail đường Lê Quang Định ----------
vi = '''<p>Lê Quang Định là con đường dài, chạy từ khu Bà Chiểu lên tới gần Gò Vấp, hai bên san sát hàng quán. Nếu bạn hay đi qua đường này và muốn tìm chỗ làm nail, bài này cho biết VESSCA nằm đoạn nào và làm những gì.</p>

<h2>VESSCA nằm đoạn nào của Lê Quang Định</h2>

<p>Tiệm ở số 251/30, tức trong hẻm 251, thuộc phường Gia Định. Vài mốc trên cùng con đường giúp bạn định vị: Trường Tiểu học Nguyễn Đình Chiểu ở đầu đường phía Bà Chiểu, Trường Yên Thế ở đoạn gần Gò Vấp hơn. VESSCA nằm giữa hai mốc đó. Mở Google Maps tìm "VESSCA Nail" sẽ ra đúng lối vào hẻm.</p>

<h2>Dịch vụ và giá</h2>

<table>
<thead><tr><th>Dịch vụ</th><th>Giá</th></tr></thead>
<tbody>
<tr><td>Cắt da, chỉnh form, dưỡng viền (tay)</td><td>60.000₫</td></tr>
<tr><td>Cắt da, chỉnh form, dưỡng viền (chân)</td><td>70.000₫</td></tr>
<tr><td>Sơn gel trơn</td><td>130.000₫</td></tr>
<tr><td>Sơn thạch</td><td>150.000₫</td></tr>
<tr><td>Sơn mắt mèo</td><td>170.000₫</td></tr>
<tr><td>Úp móng / Gel X / đắp gel / dual form</td><td>130.000 / 190.000 / 250.000 / 350.000₫</td></tr>
<tr><td>Gội đầu thư giãn</td><td>từ 99.000₫</td></tr>
</tbody>
</table>

<p>Bảng giá đầy đủ, gồm cả vẽ, đính đá và các dòng sơn Hàn, ở trang <a href="/bang-gia/">bảng giá</a>.</p>

<h2>Đi ngang thì ghé được không</h2>

<p>Tiệm phục vụ số khách giới hạn cùng lúc, nên ghé ngang có thể trùng giờ khách đã đặt. Cách chắc chắn là gọi 0933.528.501 hỏi giờ trống, hoặc đặt trước ở mục <a href="/#booking">Đặt lịch</a>. Buổi tối và cuối tuần thường kín trước.</p>

<h2>Gửi xe</h2>

<p>Có chỗ để xe trước tiệm, trong hẻm. Hẻm 251 nhỏ nên đi chậm, hướng dẫn chi tiết có ở bài <a href="/blog/den-vessca-gui-xe-dat-lich/">đến VESSCA: tìm hẻm, gửi xe và đặt lịch</a>.</p>

<p>Nếu bạn ở đoạn gần Gò Vấp hoặc Phú Nhuận, xem thêm bài <a href="/blog/tiem-nail-gan-phu-nhuan-go-vap/">tiệm nail kiểu Hàn gần Phú Nhuận, Gò Vấp</a>.</p>'''
faq = [('Tiệm nail trên đường Lê Quang Định ở số mấy?', 'VESSCA ở 251/30 Lê Quang Định, trong hẻm 251, phường Gia Định.'),
       ('Đi ngang ghé luôn được không?', 'Nên gọi 0933.528.501 hỏi giờ trống trước, vì tiệm phục vụ số khách giới hạn cùng lúc.'),
       ('Giá sơn gel ở đây bao nhiêu?', 'Sơn gel trơn 130.000₫, sơn thạch 150.000₫, mắt mèo 170.000₫.')]
en = '''<p>Le Quang Dinh is a long street running from the Ba Chieu area up towards Go Vap. If you pass along it often, here is where VESSCA sits and what it offers.</p>
<h2>Which stretch</h2>
<p>The salon is at number 251/30, inside alley 251, in Gia Dinh ward — between Nguyen Dinh Chieu Primary School at the Ba Chieu end and Yen The School closer to Go Vap. Search "VESSCA Nail" on Google Maps for the alley entrance.</p>
<h2>Prices</h2>
<p>Cuticle care and shaping 60,000₫ (hands) or 70,000₫ (feet); plain gel 130,000₫, jelly 150,000₫, cat-eye 170,000₫; tips 130,000₫, Gel X 190,000₫, builder gel 250,000₫, dual form 350,000₫. A relaxing hair wash starts at 99,000₫.</p>
<h2>Dropping in</h2>
<p>The salon takes a limited number of guests at a time, so call 0933.528.501 to check, or book ahead. Evenings and weekends fill first. Parking is in front of the salon inside the alley.</p>'''
ko = '''<p>Le Quang Dinh은 벤짜이 지역에서 고밥 쪽으로 이어지는 긴 길입니다. 이 길을 자주 지나신다면 VESSCA의 위치와 메뉴를 참고하세요.</p>
<h2>어느 구간인가요</h2>
<p>251/30번지, 251번 골목 안, 자딘 동입니다. 벤짜이 쪽 응우옌딘찌에우 초등학교와 고밥 쪽 옌테 학교 사이에 있습니다. 구글 지도에서 "VESSCA Nail"을 검색하면 골목 입구가 나옵니다.</p>
<h2>가격</h2>
<p>큐티클 케어 손 60,000₫ / 발 70,000₫, 원컬러 젤 130,000₫, 시럽 150,000₫, 자석 170,000₫, 팁 130,000₫, 젤엑스 190,000₫, 젤 연장 250,000₫, 듀얼폼 350,000₫. 헤드 스파는 99,000₫부터입니다.</p>
<h2>바로 방문</h2>
<p>동시 손님 수를 제한하므로 0933.528.501로 확인하시거나 미리 예약해 주세요. 저녁과 주말이 먼저 찹니다. 골목 안 샵 앞에 주차하실 수 있습니다.</p>'''
zh = '''<p>Le Quang Dinh 是一条从 Ba Chieu 一带通往鹅邑郡方向的长街。如果您常经过这条路,以下是 VESSCA 的位置与服务。</p>
<h2>在哪一段</h2>
<p>门牌 251/30,位于 251 巷内,嘉定坊。大致在靠 Ba Chieu 一端的阮廷炤小学与靠鹅邑郡一端的 Yen The 学校之间。在 Google 地图搜索"VESSCA Nail"可找到巷口。</p>
<h2>价格</h2>
<p>修死皮修形:手 60,000₫、脚 70,000₫;纯色凝胶 130,000₫、果冻 150,000₫、猫眼 170,000₫;甲片 130,000₫、Gel X 190,000₫、延长凝胶 250,000₫、双型膜 350,000₫。洗发 99,000₫ 起。</p>
<h2>临时到店</h2>
<p>店内限客接待,建议先致电 0933.528.501 或提前预约。晚上和周末最先约满。巷内店门前可停车。</p>'''
bai('tiem-nail-duong-le-quang-dinh', '2026-11-17T08:30:00+07:00', H,
 A(('nail salon manicure', 'Tiệm nail trên đường Lê Quang Định', 'A nail salon on Le Quang Dinh street', 'Le Quang Dinh 거리의 네일샵', 'Le Quang Dinh 街上的美甲店'), []),
 ('Tiệm nail trên đường Lê Quang Định: VESSCA ở đoạn nào',
  'Lê Quang Định dài và nhiều hàng quán. VESSCA nằm ở số 251/30, trong hẻm 251: cách định vị, bảng giá và lưu ý khi muốn ghé ngang.',
  'Tiệm nail đường Lê Quang Định | VESSCA 251/30',
  'Tiệm nail trên đường Lê Quang Định: VESSCA ở 251/30, trong hẻm 251, phường Gia Định. Sơn gel từ 130.000₫, gội đầu từ 99.000₫.',
  ['tiệm nail Lê Quang Định', 'nail Lê Quang Định', 'tiệm nail gần đây', 'tiệm nail Gia Định', 'làm nail Bình Thạnh'], vi, faq),
 ('A Nail Salon on Le Quang Dinh: Where VESSCA Sits',
  'Which stretch of Le Quang Dinh the salon is on, prices and dropping in.',
  'Nail Salon on Le Quang Dinh | VESSCA',
  'A nail salon on Le Quang Dinh street, Saigon: VESSCA at 251/30, inside alley 251. Gel from 130,000₫, hair wash from 99,000₫.',
  ['nail salon Le Quang Dinh', 'nail salon Binh Thanh', 'nail salon Saigon'], en,
  [('What number on Le Quang Dinh?', '251/30, inside alley 251, Gia Dinh ward.'),
   ('Can I just drop in?', 'Call 0933.528.501 first; the salon serves a limited number of guests at a time.')]),
 ('Le Quang Dinh 거리의 네일샵: VESSCA 위치',
  '어느 구간에 있는지, 가격, 바로 방문 시 참고사항.',
  'Le Quang Dinh 네일샵 | 호치민 VESSCA',
  '호치민 Le Quang Dinh 거리의 네일샵: VESSCA 251/30, 251번 골목 안. 젤 130,000₫부터, 샴푸 99,000₫부터.',
  ['호치민 네일샵', '빈탄 네일', '자딘 네일'], ko,
  [('몇 번지인가요?', '251/30번지, 251번 골목 안, 자딘 동입니다.'),
   ('바로 가도 되나요?', '먼저 0933.528.501로 확인해 주세요. 동시 손님 수가 제한됩니다.')]),
 ('Le Quang Dinh 街的美甲店:VESSCA 在哪一段',
  '店在这条街的哪一段、价格,以及临时到店的提醒。',
  'Le Quang Dinh 美甲店 | 胡志明 VESSCA',
  '胡志明 Le Quang Dinh 街的美甲店:VESSCA 门牌 251/30,位于 251 巷内。凝胶 130,000₫ 起,洗发 99,000₫ 起。',
  ['胡志明 美甲店', '平盛郡 美甲', '嘉定坊 美甲'], zh,
  [('门牌几号?', '251/30,位于 251 巷内,嘉定坊。'),
   ('可以直接去吗?', '建议先致电 0933.528.501,店内限客接待。')]))

# ---------- 4. Phường Gia Định là ở đâu ----------
vi = '''<p>Từ 1/7/2025, TP.HCM sắp xếp lại các phường. Quận Bình Thạnh cũ được chia lại, trong đó bốn phường 1, 2, 7 và 17 nhập thành <strong>phường Gia Định</strong>. Địa chỉ VESSCA vì vậy ghi là phường Gia Định, dù nhiều người vẫn quen gọi khu này là Bình Thạnh.</p>

<h2>Phường Gia Định gồm khu nào</h2>

<p>Phường Gia Định nằm ở khu trung tâm Bình Thạnh cũ, gồm khu Bà Chiểu và các tuyến quanh đó. Một số mốc quen thuộc trong phường:</p>

<ul>
<li>Chợ Bà Chiểu</li>
<li>Lăng Ông Bà Chiểu, tức Lăng Lê Văn Duyệt</li>
<li>Bệnh viện Nhân dân Gia Định, 1 Nơ Trang Long</li>
<li>Các tuyến Lê Quang Định, Phan Đăng Lưu, Lê Văn Duyệt</li>
</ul>

<p>Phường giáp Phú Nhuận và gần Gò Vấp, Quận 1.</p>

<h2>Địa chỉ cũ và mới ghi thế nào</h2>

<table>
<thead><tr><th>Cách ghi</th><th>Ví dụ</th></tr></thead>
<tbody>
<tr><td>Mới (đang dùng)</td><td>251/30 Lê Quang Định, phường Gia Định, TP.HCM</td></tr>
<tr><td>Quen thuộc</td><td>251/30 Lê Quang Định, Bình Thạnh</td></tr>
</tbody>
</table>

<p>Hai cách đều chỉ cùng một nơi. Khi đặt xe công nghệ hoặc giao hàng, ghi đầy đủ "251/30 Lê Quang Định, phường Gia Định" là tài xế tìm được. Nếu ứng dụng chưa cập nhật tên phường mới, gõ "VESSCA Nail" trên Google Maps.</p>

<h2>Vì sao tên Gia Định quay lại</h2>

<p>Gia Định là địa danh lâu đời ở vùng đất này. Sau năm 1975, tỉnh Gia Định nhập với Sài Gòn, tên gọi dần không còn trong tên đơn vị hành chính, nhưng người dân vẫn gọi quen. Đợt sắp xếp phường năm 2025 đưa tên này trở lại.</p>

<h2>Tìm VESSCA</h2>

<p>Tiệm ở 251/30 Lê Quang Định, phường Gia Định, trong hẻm 251, mở 9:00–20:30 mỗi ngày. Hướng dẫn vào hẻm và chỗ để xe có ở bài <a href="/blog/den-vessca-gui-xe-dat-lich/">đến VESSCA: tìm hẻm, gửi xe và đặt lịch</a>. Giới thiệu đầy đủ về tiệm ở bài <a href="/blog/tiem-nail-phuong-gia-dinh/">tiệm nail phường Gia Định</a>.</p>'''
faq = [('Phường Gia Định thuộc quận nào?', 'Phường Gia Định nằm ở khu quận Bình Thạnh cũ, TP.HCM. Từ 1/7/2025 TP.HCM bỏ cấp quận, phường thuộc thẳng thành phố.'),
       ('Phường Gia Định gồm những phường cũ nào?', 'Các phường 1, 2, 7 và 17 của quận Bình Thạnh cũ.'),
       ('Ghi địa chỉ Bình Thạnh có sai không?', 'Không sai về vị trí, nhưng cách ghi đang dùng là phường Gia Định, TP.HCM.'),
       ('Chợ Bà Chiểu thuộc phường nào?', 'Chợ Bà Chiểu nằm trong phường Gia Định.')]
en = '''<p>Since 1 July 2025 Ho Chi Minh City has reorganised its wards. In the former Binh Thanh district, wards 1, 2, 7 and 17 were merged into <strong>Gia Dinh ward</strong>. That is why VESSCA's address now reads Gia Dinh ward, even though people still say Binh Thanh.</p>
<h2>What is in Gia Dinh ward</h2>
<ul><li>Ba Chieu market</li><li>The Le Van Duyet Tomb (Lang Ong Ba Chieu)</li><li>Nhan Dan Gia Dinh Hospital, 1 No Trang Long</li><li>Le Quang Dinh, Phan Dang Luu and Le Van Duyet streets</li></ul>
<p>The ward borders Phu Nhuan and sits near Go Vap and District 1.</p>
<h2>Writing the address</h2>
<p>New: 251/30 Le Quang Dinh, Gia Dinh ward, Ho Chi Minh City. Familiar: 251/30 Le Quang Dinh, Binh Thanh. Both point to the same place; if an app has not updated the ward name, search "VESSCA Nail" on Google Maps.</p>
<h2>Finding VESSCA</h2>
<p>The salon is inside alley 251, open 9:00–20:30 daily.</p>'''
ko = '''<p>2025년 7월 1일부터 호치민시는 동을 재편했습니다. 옛 빈탄군의 1·2·7·17동이 합쳐져 <strong>자딘(Gia Định) 동</strong>이 되었습니다. 그래서 VESSCA의 주소가 자딘 동으로 표기됩니다. 사람들은 여전히 빈탄이라고 부릅니다.</p>
<h2>자딘 동에 있는 곳</h2>
<ul><li>벤짜이 시장</li><li>레반주엣 묘(랑옹 벤짜이)</li><li>자딘 인민병원, 1 No Trang Long</li><li>Le Quang Dinh, Phan Dang Luu, Le Van Duyet 거리</li></ul>
<p>푸뉴언과 맞닿아 있고 고밥, 1군과 가깝습니다.</p>
<h2>주소 표기</h2>
<p>새 표기: 251/30 Le Quang Dinh, 자딘 동, 호치민시. 익숙한 표기: 251/30 Le Quang Dinh, 빈탄. 같은 곳이며, 앱에 새 동 이름이 없으면 구글 지도에서 "VESSCA Nail"을 검색하세요.</p>'''
zh = '''<p>自 2025 年 7 月 1 日起,胡志明市重新调整了坊级行政区。原平盛郡的第 1、2、7、17 坊合并为<strong>嘉定坊</strong>。因此 VESSCA 的地址写作嘉定坊,但大家仍习惯说平盛郡。</p>
<h2>嘉定坊里有什么</h2>
<ul><li>Ba Chieu 市场</li><li>黎文悦墓(Lang Ong Ba Chieu)</li><li>嘉定人民医院,1 No Trang Long</li><li>Le Quang Dinh、Phan Dang Luu、Le Van Duyet 等街道</li></ul>
<p>该坊与富润郡相邻,靠近鹅邑郡和第一郡。</p>
<h2>地址怎么写</h2>
<p>新写法:251/30 Le Quang Dinh,嘉定坊,胡志明市。习惯写法:251/30 Le Quang Dinh,平盛郡。两者指同一个地方;若应用尚未更新坊名,请在 Google 地图搜索"VESSCA Nail"。</p>'''
bai('phuong-gia-dinh-o-dau', '2026-11-17T11:30:00+07:00', Q,
 A(('nail salon manicure', 'Khu phường Gia Định, Bình Thạnh cũ', 'The Gia Dinh ward area', '자딘 동 일대', '嘉定坊一带'), []),
 ('Phường Gia Định ở đâu, gồm những phường cũ nào của Bình Thạnh',
  'Từ 1/7/2025 bốn phường 1, 2, 7, 17 của Bình Thạnh nhập thành phường Gia Định. Phường gồm khu nào, ghi địa chỉ thế nào và tìm VESSCA ra sao.',
  'Phường Gia Định ở đâu, gồm phường nào | VESSCA',
  'Phường Gia Định (TP.HCM) gồm các phường 1, 2, 7, 17 của Bình Thạnh cũ, có chợ Bà Chiểu, Lăng Ông, Bệnh viện Gia Định. Cách ghi địa chỉ mới.',
  ['phường Gia Định', 'phường Gia Định thuộc quận nào', 'Bình Thạnh sáp nhập', 'chợ Bà Chiểu phường nào', 'địa chỉ phường Gia Định'], vi, faq),
 ('Where Is Gia Dinh Ward, and Which Binh Thanh Wards Formed It',
  'Since 1 July 2025 wards 1, 2, 7 and 17 of Binh Thanh merged into Gia Dinh ward. What is in it and how to write the address.',
  'Where Is Gia Dinh Ward, Ho Chi Minh City | VESSCA',
  'Gia Dinh ward, Ho Chi Minh City, was formed from wards 1, 2, 7 and 17 of Binh Thanh. It holds Ba Chieu market, Lang Ong and Gia Dinh Hospital.',
  ['Gia Dinh ward', 'Binh Thanh ward merger', 'Ba Chieu market ward'], en,
  [('Which district is Gia Dinh ward in?', 'It covers the former Binh Thanh district area; since 1 July 2025 the city no longer uses districts.'),
   ('Which old wards formed it?', 'Wards 1, 2, 7 and 17 of the former Binh Thanh district.')]),
 ('자딘 동은 어디인가요, 어느 동이 합쳐졌나요',
  '2025년 7월 1일 빈탄 1·2·7·17동이 자딘 동으로 합쳐졌습니다. 구성과 주소 표기법.',
  '자딘 동 위치 | 호치민 VESSCA',
  '호치민 자딘 동은 옛 빈탄 1·2·7·17동이 합쳐진 곳으로 벤짜이 시장, 랑옹, 자딘 병원이 있습니다.',
  ['자딘 동', '빈탄 동 통합', '벤짜이 시장'], ko,
  [('어느 군에 속하나요?', '옛 빈탄군 지역이며, 2025년 7월 1일부터 군 단위는 사용하지 않습니다.'),
   ('어느 동이 합쳐졌나요?', '옛 빈탄군 1·2·7·17동입니다.')]),
 ('嘉定坊在哪里,由平盛郡哪些坊合并而成',
  '2025 年 7 月 1 日起,平盛郡第 1、2、7、17 坊合并为嘉定坊。坊内有什么、地址怎么写。',
  '嘉定坊在哪里 | 胡志明 VESSCA',
  '胡志明嘉定坊由原平盛郡第 1、2、7、17 坊合并而成,坊内有 Ba Chieu 市场、黎文悦墓和嘉定人民医院。',
  ['嘉定坊', '平盛郡 合并', 'Ba Chieu 市场'], zh,
  [('属于哪个郡?', '为原平盛郡区域;自 2025 年 7 月 1 日起不再设郡级。'),
   ('由哪些旧坊合并?', '原平盛郡第 1、2、7、17 坊。')]))

# ---------- 5. Gội đầu dưỡng sinh ----------
vi = '''<p>"Gội đầu dưỡng sinh" là cách gọi quen thuộc ở Việt Nam cho buổi gội đầu dài, có massage, thường kèm chăm sóc da mặt. Nhiều khách hỏi VESSCA có làm kiểu đó không. Bài này nói rõ tiệm làm gì trong mỗi gói để bạn tự đối chiếu với điều mình đang tìm.</p>

<h2>Hai cách gọi, cùng một ý</h2>

<p>Dù gọi là gội đầu dưỡng sinh hay gội đầu thư giãn, điểm chung là buổi gội kéo dài hơn gội thường, có massage đầu và thường có bước chăm da mặt. Khác nhau ở từng tiệm là số bước và sản phẩm dùng.</p>

<h2>VESSCA làm những bước nào</h2>

<table>
<thead><tr><th>Gói</th><th>Thời lượng</th><th>Điểm chính</th><th>Giá</th></tr></thead>
<tbody>
<tr><td>01 · Gội sạch thơm</td><td>30 phút</td><td>Gội 2 lần, xả, sấy ion âm, dầu dưỡng</td><td>99.000–149.000₫</td></tr>
<tr><td>02 · Massage chăm da đầu</td><td>50 phút</td><td>Thêm tẩy tế bào chết da đầu, 2 lần massage đầu, mặt nạ mắt</td><td>229.000–279.000₫</td></tr>
<tr><td>03 · Chăm da mặt</td><td>50 phút</td><td>Thêm mặt nạ Hàn Quốc, massage mặt, chiếu đèn sinh học</td><td>269.000–319.000₫</td></tr>
<tr><td>04 · Gói thiên đường</td><td>75 phút</td><td>Gộp cả hai, thêm massage đầu, cổ vai gáy</td><td>419.000–469.000₫</td></tr>
</tbody>
</table>

<p>Ba mức giá mỗi gói là do bạn chọn một trong ba loại dầu gội xả: Nguyên Xuân, gừng sả thiên nhiên hoặc Unove Hàn Quốc. So sánh ba loại ở bài <a href="/blog/chon-dau-goi-nguyen-xuan-gung-sa-unove/">chọn dầu gội Nguyên Xuân, gừng sả hay Unove</a>.</p>

<h2>Điều nên biết trước</h2>

<ul>
<li>Đây là dịch vụ chăm sóc, thư giãn, không phải điều trị y tế. Da đầu có vấn đề kéo dài như gàu nặng, rụng tóc bất thường thì nên khám bác sĩ da liễu.</li>
<li>Báo trước nếu bạn từng dị ứng mỹ phẩm, da đầu đang có vết thương hoặc da mặt đang điều trị.</li>
<li>Gói 75 phút nên bắt đầu trước 19:00 để kịp trước giờ đóng cửa 20:30.</li>
</ul>

<h2>Đặt lịch</h2>

<p>Chọn "Gội đầu thư giãn" ở mục <a href="/#booking">Đặt lịch</a>, hoặc "Nail và gội đầu" nếu muốn làm cả hai. Menu từng bước có ở trang <a href="/goi-dau/">menu gội đầu</a>. Bảng giá bốn gói có ở bài <a href="/blog/goi-dau-thu-gian-binh-thanh/">gội đầu thư giãn ở Bình Thạnh</a>.</p>'''
faq = [('Gội đầu dưỡng sinh là gì?', 'Là cách gọi quen thuộc cho buổi gội đầu dài, có massage đầu và thường kèm chăm sóc da mặt.'),
       ('VESSCA có gội đầu dưỡng sinh không?', 'Tiệm có bốn gói gội đầu từ 30 đến 75 phút, có massage đầu, massage mặt, mặt nạ Hàn Quốc tuỳ gói.'),
       ('Gội đầu dưỡng sinh có chữa rụng tóc không?', 'Không. Đây là dịch vụ chăm sóc thư giãn; vấn đề da đầu kéo dài nên khám bác sĩ da liễu.'),
       ('Giá bao nhiêu?', 'Từ 99.000₫ cho gói 30 phút đến 469.000₫ cho gói 75 phút, tuỳ loại dầu gội.')]
en = '''<p>In Vietnam a long shampoo session with massage, often with facial care, is commonly called "gội đầu dưỡng sinh". Guests often ask whether VESSCA offers that. Here is exactly what each package includes.</p>
<h2>What VESSCA does</h2>
<table>
<thead><tr><th>Package</th><th>Time</th><th>Price</th></tr></thead>
<tbody>
<tr><td>01 · Fresh Hair Wash</td><td>30 min</td><td>99,000–149,000₫</td></tr>
<tr><td>02 · Scalp Therapy</td><td>50 min</td><td>229,000–279,000₫</td></tr>
<tr><td>03 · Facial Glow Care</td><td>50 min</td><td>269,000–319,000₫</td></tr>
<tr><td>04 · Paradise Ritual</td><td>75 min</td><td>419,000–469,000₫</td></tr>
</tbody>
</table>
<p>Each has three prices because you choose one of three shampoos. Packages 02 and 04 add scalp exfoliation and head massage; 03 and 04 add a Korean sheet mask, facial massage and LED care.</p>
<h2>Worth knowing</h2>
<p>This is care and relaxation, not medical treatment: see a dermatologist for persistent scalp problems. Tell your technician about any allergy or treated skin. Start the 75-minute package before 19:00 to finish before closing at 20:30.</p>'''
ko = '''<p>베트남에서는 마사지와 페이셜 케어가 포함된 긴 샴푸를 흔히 "gội đầu dưỡng sinh"이라고 부릅니다. VESSCA에서도 가능한지 묻는 분이 많아 코스별 구성을 정리했습니다.</p>
<h2>코스 구성</h2>
<table>
<thead><tr><th>코스</th><th>시간</th><th>가격</th></tr></thead>
<tbody>
<tr><td>01 · 프레시 헤어 워시</td><td>30분</td><td>99,000–149,000₫</td></tr>
<tr><td>02 · 두피 테라피</td><td>50분</td><td>229,000–279,000₫</td></tr>
<tr><td>03 · 페이셜 글로우 케어</td><td>50분</td><td>269,000–319,000₫</td></tr>
<tr><td>04 · 파라다이스 리추얼</td><td>75분</td><td>419,000–469,000₫</td></tr>
</tbody>
</table>
<p>샴푸 3종 중 선택에 따라 가격이 달라집니다. 02·04는 두피 스케일링과 두피 마사지, 03·04는 한국 마스크팩과 페이셜 마사지, LED 케어가 포함됩니다.</p>
<h2>참고</h2>
<p>치료가 아닌 케어 서비스입니다. 두피 문제가 오래가면 피부과 진료를 받으세요. 알레르기나 치료 중인 피부는 미리 알려 주세요. 75분 코스는 20:30 마감 전에 끝나도록 19:00 이전에 시작해 주세요.</p>'''
zh = '''<p>在越南,时间较长、含按摩并常带面部护理的洗发,常被称为"养生洗发"。不少客人问 VESSCA 是否有这类服务。下面说明每种套餐的具体内容。</p>
<h2>套餐内容</h2>
<table>
<thead><tr><th>套餐</th><th>时长</th><th>价格</th></tr></thead>
<tbody>
<tr><td>01 · 清爽洗发</td><td>30 分钟</td><td>99,000–149,000₫</td></tr>
<tr><td>02 · 头皮护理</td><td>50 分钟</td><td>229,000–279,000₫</td></tr>
<tr><td>03 · 面部护理</td><td>50 分钟</td><td>269,000–319,000₫</td></tr>
<tr><td>04 · 天堂套餐</td><td>75 分钟</td><td>419,000–469,000₫</td></tr>
</tbody>
</table>
<p>价格依所选三款洗发水而定。套餐 02、04 含头皮去角质与头部按摩;03、04 含韩国面膜、面部按摩与 LED 光疗。</p>
<h2>需要知道的</h2>
<p>这是护理与放松服务,不是医疗治疗。头皮问题持续请就医。若有过敏或皮肤正在治疗,请提前告知。75 分钟套餐建议 19:00 前开始,以便在 20:30 关门前完成。</p>'''
bai('goi-dau-duong-sinh-la-gi', '2026-11-17T14:30:00+07:00', G,
 A(('scalp massage', 'Massage đầu trong buổi gội đầu dưỡng sinh', 'A head massage during a long shampoo session', '긴 샴푸 코스의 두피 마사지', '养生洗发中的头部按摩'), []),
 ('Gội đầu dưỡng sinh là gì, VESSCA làm những bước nào',
  '"Gội đầu dưỡng sinh" gồm những gì, khác gội thường ra sao, và bốn gói gội đầu tại VESSCA có bước nào, giá bao nhiêu.',
  'Gội đầu dưỡng sinh là gì | VESSCA Bình Thạnh',
  'Gội đầu dưỡng sinh là buổi gội dài có massage đầu, thường kèm chăm da mặt. Bốn gói tại VESSCA: 30–75 phút, 99.000–469.000₫.',
  ['gội đầu dưỡng sinh', 'gội đầu dưỡng sinh là gì', 'gội đầu thư giãn', 'gội đầu Bình Thạnh', 'gội đầu massage'], vi, faq),
 ('What a Long Vietnamese Shampoo Session Includes at VESSCA',
  'What the Vietnamese "gội đầu dưỡng sinh" means and what each VESSCA package includes.',
  'Long Shampoo & Head Spa Sessions | VESSCA',
  'What a long Vietnamese shampoo and head spa session includes: four packages at VESSCA, 30–75 minutes, 99,000–469,000₫.',
  ['head spa Saigon', 'Vietnamese shampoo session', 'head spa Binh Thanh'], en,
  [('Is it a medical treatment?', 'No, it is care and relaxation. See a dermatologist for persistent scalp problems.'),
   ('How much?', 'From 99,000₫ for 30 minutes to 469,000₫ for 75 minutes.')]),
 ('베트남식 롱 샴푸 코스, VESSCA는 어떻게 하나요',
  '"gội đầu dưỡng sinh"의 의미와 VESSCA 코스별 구성.',
  '베트남식 헤드 스파 | 호치민 VESSCA',
  '베트남식 롱 샴푸·헤드 스파 구성: VESSCA 네 가지 코스, 30–75분, 99,000–469,000₫.',
  ['호치민 헤드스파', '베트남 샴푸', '빈탄 헤드스파'], ko,
  [('치료인가요?', '아니요, 케어와 휴식을 위한 서비스입니다.'),
   ('가격은요?', '30분 99,000₫부터 75분 469,000₫까지입니다.')]),
 ('越南式"养生洗发"包含什么,VESSCA 怎么做',
  '"养生洗发"的含义,以及 VESSCA 各套餐的具体步骤。',
  '越南式养生洗发 | 胡志明 VESSCA',
  '越南式养生洗发与头皮护理包含什么:VESSCA 四种套餐,30–75 分钟,99,000–469,000₫。',
  ['胡志明 头皮护理', '越南 洗发', '平盛郡 洗发'], zh,
  [('这是治疗吗?', '不是,这是护理与放松服务。'),
   ('价格多少?', '30 分钟 99,000₫ 起,75 分钟最高 469,000₫。')]))
