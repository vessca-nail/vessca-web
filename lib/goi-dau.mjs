/**
 * ============================================================
 *  TRANG BẢNG GIÁ GỘI ĐẦU — /goi-dau/ (+ /en/, /ko/, /zh/)   (đợt 38 — 12/11/2026)
 * ============================================================
 *  Theo đúng menu gội đầu chủ tiệm gửi 12/11/2026. MỌI con số, tên sản phẩm,
 *  quy trình đều lấy từ menu đó — không thêm thông tin ngoài menu.
 *  Sửa giá: sửa ở mảng GOI / LE bên dưới (và ở Admin → Bảng giá của app tiệm).
 *
 *  Cùng kiểu trình bày với /bang-gia/ (ảnh + bảng giá nền tối, mỗi lần hiện
 *  một nhóm). Trên cùng có nút chuyển Nail | Gội đầu giữa hai bảng giá.
 */

import { LOGO_SVG } from './render.mjs';
import { UI_BANG_GIA } from './bang-gia.mjs';

const LANGS = ['vi', 'en', 'ko', 'zh'];
const BASE = { vi: '', en: '/en', ko: '/ko', zh: '/zh' };
const HREFLANG = { vi: 'vi-VN', en: 'en', ko: 'ko', zh: 'zh-Hant' };
const LABEL = { vi: 'VI', en: 'EN', ko: '한국어', zh: '中文' };

const UI = {
  vi: {
    title: 'Menu gội đầu thư giãn',
    metaTitle: 'Bảng giá gội đầu thư giãn VESSCA — Bình Thạnh (Gia Định), TP.HCM',
    metaDesc: 'Menu gội đầu thư giãn tại VESSCA: gội sạch thơm từ 99.000₫, gội kèm massage da đầu từ 229.000₫, gội kèm chăm da mặt từ 269.000₫, Gói thiên đường 75 phút từ 419.000₫. 251/30 Lê Quang Định, Gia Định, TP.HCM.',
    intro: 'Chọn gói, rồi chọn dầu gội xả bạn thích. Vessca cam kết dùng sản phẩm chính hãng, nguồn gốc xuất xứ rõ ràng.',
    goi: 'Gói', phut: 'phút', quyTrinh: 'Quy trình', dauGoi: 'Chọn dầu gội xả', matNa: 'Chọn mặt nạ',
    matNaSub: 'Mặt nạ Hàn Quốc · chọn 1 loại', trongGoi: 'Trong gói', phuThu: 'phụ thu',
    le: 'Dịch vụ lẻ', leNote: 'Áp dụng khi dùng kèm các gói gội đầu.',
    daDau: 'Chăm sóc da đầu', daMat: 'Chăm sóc da mặt', nangCo: 'Loại nâng cơ, săn chắc phụ thu 30.000₫',
    tabNail: 'Nail', tabGoi: 'Gội đầu', bangGia: 'Bảng giá',
  },
  en: {
    title: 'Head spa menu',
    metaTitle: 'VESSCA Head Spa & Hair Wash Menu — Binh Thanh, Saigon',
    metaDesc: 'VESSCA hair wash menu: Fresh Hair Wash from 99,000₫, Hair Wash & Scalp Therapy from 229,000₫, Hair Wash & Facial Glow Care from 269,000₫, The Paradise Ritual (75 min) from 419,000₫. 251/30 Le Quang Dinh, Gia Dinh ward, Ho Chi Minh City.',
    intro: 'Pick a package, then the shampoo you like. Vessca uses genuine products with a clear origin.',
    goi: 'Package', phut: 'min', quyTrinh: 'What’s included', dauGoi: 'Choose your shampoo', matNa: 'Choose your mask',
    matNaSub: 'Korean sheet mask · choose one', trongGoi: 'Included', phuThu: 'extra',
    le: 'À la carte', leNote: 'Available together with a hair wash package.',
    daDau: 'Scalp care', daMat: 'Facial care', nangCo: 'Lifting & firming mask: 30,000₫ extra',
    tabNail: 'Nail', tabGoi: 'Head spa', bangGia: 'Prices',
  },
  ko: {
    title: '헤드 스파 메뉴',
    metaTitle: 'VESSCA 헤드 스파·샴푸 메뉴 — 호치민 빈탄',
    metaDesc: 'VESSCA 샴푸 메뉴: 프레시 헤어 워시 99,000₫부터, 두피 테라피 229,000₫부터, 페이셜 글로우 케어 269,000₫부터, 파라다이스 리추얼(75분) 419,000₫부터. 251/30 Le Quang Dinh, 호치민.',
    intro: '코스를 고른 뒤 원하는 샴푸를 선택하세요. Vessca는 원산지가 분명한 정품만 사용합니다.',
    goi: '코스', phut: '분', quyTrinh: '진행 순서', dauGoi: '샴푸 선택', matNa: '마스크 선택',
    matNaSub: '한국 마스크팩 · 1종 선택', trongGoi: '포함', phuThu: '추가',
    le: '단품 메뉴', leNote: '샴푸 코스와 함께 이용하실 수 있습니다.',
    daDau: '두피 케어', daMat: '페이셜 케어', nangCo: '리프팅·탄력 마스크는 30,000₫ 추가',
    tabNail: '네일', tabGoi: '헤드 스파', bangGia: '가격',
  },
  zh: {
    title: '頭皮舒壓洗髮價目表',
    metaTitle: 'VESSCA 洗髮・頭皮 SPA 價目表 — 胡志明市平盛郡',
    metaDesc: 'VESSCA 洗髮價目：清爽洗髮 99,000₫ 起、洗髮＋頭皮護理 229,000₫ 起、洗髮＋臉部亮采護理 269,000₫ 起、天堂儀式（75 分鐘）419,000₫ 起。251/30 Le Quang Dinh，胡志明市。',
    intro: '先選套餐，再選喜歡的洗髮精。Vessca 只使用來源清楚的正品。',
    goi: '套餐', phut: '分鐘', quyTrinh: '流程', dauGoi: '選擇洗髮精', matNa: '選擇面膜',
    matNaSub: '韓國面膜 · 任選一款', trongGoi: '已包含', phuThu: '加價',
    le: '單項服務', leNote: '需搭配洗髮套餐使用。',
    daDau: '頭皮護理', daMat: '臉部護理', nangCo: '提拉緊緻面膜加價 30,000₫',
    tabNail: '美甲', tabGoi: '洗髮', bangGia: '價目',
  },
};

/* ---- các bước trong quy trình ---- */
const B = {
  tt:    { vi: 'Tẩy trang Garnier, rửa mặt SVR', en: 'Garnier make-up removal, SVR face cleanse', ko: '가르니에 클렌징, SVR 세안', zh: 'Garnier 卸妝、SVR 潔面' },
  goi2:  { vi: 'Gội dầu gội 2 lần', en: 'Double shampoo', ko: '샴푸 2회', zh: '洗髮兩次' },
  xa:    { vi: 'Xả dầu xả siêu mượt', en: 'Silky conditioner', ko: '실키 컨디셔너', zh: '柔順護髮素' },
  say:   { vi: 'Sấy bảo vệ tóc bằng máy sấy ion âm', en: 'Blow-dry with a negative-ion dryer', ko: '음이온 드라이어로 모발 보호 드라이', zh: '負離子吹風機護髮吹乾' },
  duong: { vi: 'Dầu dưỡng tóc L’Oréal', en: 'L’Oréal hair oil', ko: '로레알 헤어 오일', zh: 'L’Oréal 護髮油' },
  nuoc:  { vi: 'Nước uống, bánh ngọt', en: 'A drink and a sweet treat', ko: '음료와 디저트', zh: '飲品與甜點' },
  ttdau: { vi: 'Tẩy tế bào chết da đầu', en: 'Scalp exfoliation', ko: '두피 스케일링', zh: '頭皮去角質' },
  mmat:  { vi: 'Đắp mặt nạ mắt', en: 'Eye mask', ko: '아이 마스크', zh: '眼膜' },
  mas1:  { vi: 'Massage đầu thư giãn lần 1', en: 'Relaxing head massage, round 1', ko: '릴랙싱 두피 마사지 1차', zh: '頭部放鬆按摩（第一次）' },
  mas2:  { vi: 'Massage đầu thư giãn lần 2', en: 'Relaxing head massage, round 2', ko: '릴랙싱 두피 마사지 2차', zh: '頭部放鬆按摩（第二次）' },
  tay:   { vi: 'Dưỡng da tay', en: 'Hand care', ko: '핸드 케어', zh: '手部保養' },
  ttmat: { vi: 'Tẩy tế bào chết da mặt', en: 'Facial exfoliation', ko: '얼굴 각질 케어', zh: '臉部去角質' },
  mnhan: { vi: 'Đắp mặt nạ Hàn Quốc', en: 'Korean sheet mask', ko: '한국 마스크팩', zh: '韓國面膜' },
  masmat:{ vi: 'Massage mặt thư giãn, nâng cơ, hỗ trợ giảm nếp nhăn', en: 'Relaxing, lifting facial massage', ko: '릴랙싱·리프팅 페이셜 마사지', zh: '臉部放鬆提拉按摩' },
  den:   { vi: 'Chiếu đèn ánh sáng sinh học cải thiện làn da', en: 'LED light therapy', ko: 'LED 광테라피', zh: 'LED 光療' },
  masdau:{ vi: 'Massage đầu, cổ vai gáy thư giãn', en: 'Head, neck & shoulder massage', ko: '두피·목·어깨 마사지', zh: '頭部及肩頸按摩' },
};

const DAU_GOI = [
  { anh: 'dau-nguyen-xuan.jpg',
    ten: { vi: 'Nguyên Xuân', en: 'Nguyen Xuan herbal', ko: 'Nguyen Xuan 허브', zh: 'Nguyen Xuan 草本' },
    mo: { vi: 'Thảo dược truyền thống, tóc mềm bồng bềnh.', en: 'Traditional herbal formula for soft, airy hair.', ko: '전통 허브 샴푸, 부드럽고 풍성한 머릿결.', zh: '傳統草本配方，髮絲柔軟蓬鬆。' },
    phu: { vi: 'Bản vàng cho da đầu dễ bết · bản xanh lá cho tóc khô, hư tổn.', en: 'Gold for oily scalps · green for dry, damaged hair.', ko: '골드: 지성 두피 · 그린: 건조·손상 모발', zh: '金色款適合易油頭皮 · 綠色款適合乾燥受損髮質' } },
  { anh: 'dau-gung-sa.jpg',
    ten: { vi: 'Gừng sả thiên nhiên', en: 'Natural ginger & lemongrass', ko: '천연 생강·레몬그라스', zh: '天然薑香茅' },
    mo: { vi: 'Nguyên liệu tự nhiên chuẩn spa, hương gừng sả ấm.', en: 'Spa-grade natural ingredients with a warm ginger-lemongrass scent.', ko: '스파급 천연 원료, 따뜻한 생강·레몬그라스 향.', zh: 'SPA 級天然原料，溫暖的薑與香茅香氣。' },
    phu: { vi: 'Hợp da đầu nhạy cảm · hương lưu lâu trên tóc.', en: 'Suits sensitive scalps · long-lasting scent.', ko: '민감한 두피에 적합 · 향이 오래 지속', zh: '適合敏感頭皮 · 香氣持久' } },
  { anh: 'dau-unove.jpg',
    ten: { vi: 'Unove Hàn Quốc', en: 'Unove (Korea)', ko: '어노브 (한국)', zh: '韓國 Unove' },
    mo: { vi: 'Dưỡng chất chuyên sâu, hương nước hoa sang trọng.', en: 'Deep-nourishing care with an elegant perfume scent.', ko: '집중 영양 케어, 고급스러운 향수 향.', zh: '深層滋養，高雅香水香氣。' },
    phu: { vi: 'Bán chạy số 1 Hàn Quốc · hợp tóc nhuộm, uốn, hư tổn.', en: 'A best-seller in Korea · for coloured, permed or damaged hair.', ko: '한국 인기 제품 · 염색·펌·손상 모발에 적합', zh: '韓國熱銷 · 適合染燙、受損髮質' } },
];

const MAT_NA = [
  { ten: { vi: 'Mờ thâm, trắng da', en: 'Brightening, dark-spot care', ko: '미백·잡티 케어', zh: '淡斑亮白' }, them: 0 },
  { ten: { vi: 'Cấp ẩm, phục hồi', en: 'Hydrating & repair', ko: '수분·진정 회복', zh: '補水修護' }, them: 0 },
  { ten: { vi: 'Sáng da, trẻ hoá', en: 'Glow & rejuvenating', ko: '광채·안티에이징', zh: '亮膚煥顏' }, them: 0 },
  { ten: { vi: 'Nâng cơ, săn chắc, dưỡng chuyên sâu', en: 'Lifting, firming, intensive care', ko: '리프팅·탄력 집중 케어', zh: '提拉緊緻深層保養' }, them: 30000 },
];

export const GOI = [
  { id: 'goi-1', phut: 30, gia: [99000, 129000, 149000], buoc: ['tt', 'goi2', 'xa', 'say', 'duong', 'nuoc'],
    ten: { vi: 'Gội sạch thơm', en: 'Fresh Hair Wash', ko: '프레시 헤어 워시', zh: '清爽洗髮' },
    mo: { vi: 'Nhanh gọn cho ngày bận rộn — da đầu sạch sâu, tóc mượt và thơm suốt ngày.', en: 'Quick and easy for a busy day — a deeply clean scalp and smooth, fragrant hair all day.', ko: '바쁜 날을 위한 간편 코스 — 두피는 깨끗하게, 머릿결은 부드럽고 향기롭게.', zh: '忙碌日子的快速選擇——頭皮深層潔淨，秀髮柔順、整日清香。' } },
  { id: 'goi-2', phut: 50, gia: [229000, 259000, 279000], buoc: ['tt', 'ttdau', 'mmat', 'mas1', 'goi2', 'xa', 'mas2', 'say', 'duong', 'tay', 'nuoc'],
    ten: { vi: 'Gội sạch thơm, massage chăm da đầu', en: 'Hair Wash & Scalp Therapy', ko: '헤어 워시 & 두피 테라피', zh: '洗髮＋頭皮護理' },
    mo: { vi: 'Massage đầu thư giãn và tẩy tế bào chết giúp da đầu nhẹ bẫng, tóc lâu bết hơn.', en: 'A relaxing head massage and scalp exfoliation leave your scalp feeling light and your hair fresh for longer.', ko: '릴랙싱 두피 마사지와 스케일링으로 두피는 가볍게, 머리는 더 오래 산뜻하게.', zh: '放鬆的頭部按摩搭配頭皮去角質，頭皮輕盈，秀髮更持久清爽。' } },
  { id: 'goi-3', phut: 50, gia: [269000, 299000, 319000], matNa: true, buoc: ['tt', 'ttmat', 'mnhan', 'goi2', 'xa', 'masmat', 'den', 'say', 'duong', 'tay', 'nuoc'],
    ten: { vi: 'Gội sạch thơm, chăm da mặt', en: 'Hair Wash & Facial Glow Care', ko: '헤어 워시 & 페이셜 글로우 케어', zh: '洗髮＋臉部亮采護理' },
    mo: { vi: 'Massage mặt thư giãn, nâng cơ — bước ra với làn da tươi mới, căng bừng sức sống.', en: 'A relaxing, lifting facial massage — walk out with fresh, radiant skin.', ko: '리프팅 페이셜 마사지로 생기 있고 탄력 있는 피부로.', zh: '放鬆提拉的臉部按摩，讓肌膚煥然一新、充滿光采。' } },
  { id: 'goi-4', phut: 75, signature: true, gia: [419000, 449000, 469000], matNa: true, buoc: ['tt', 'ttmat', 'mnhan', 'ttdau', 'goi2', 'xa', 'masmat', 'den', 'mmat', 'masdau', 'say', 'duong', 'tay', 'nuoc'],
    ten: { vi: 'Gói thiên đường', en: 'The Paradise Ritual', ko: '파라다이스 리추얼', zh: '天堂儀式' },
    mo: { vi: 'Trọn vẹn 75 phút: da mặt, da đầu và cổ vai gáy đều được chăm sóc, nâng niu.', en: 'A full 75 minutes of care for your face, scalp, neck and shoulders.', ko: '75분 동안 얼굴, 두피, 목과 어깨까지 꼼꼼하게 케어합니다.', zh: '完整 75 分鐘：臉部、頭皮與肩頸都得到細緻呵護。' } },
];

const M15 = { vi: '15 phút', en: '15 min', ko: '15분', zh: '15 分鐘' };
const LE = [
  { nhom: 'daDau', dong: [
    { ten: B.ttdau, gia: 49000 },
    { ten: { vi: 'Massage đầu & cổ vai gáy', en: 'Head, neck & shoulder massage', ko: '두피·목·어깨 마사지', zh: '頭部及肩頸按摩' }, phu: M15, gia: 89000 },
    { ten: { vi: 'Massage cổ vai gáy', en: 'Neck & shoulder massage', ko: '목·어깨 마사지', zh: '肩頸按摩' }, phu: M15, gia: 89000 },
  ] },
  { nhom: 'daMat', dong: [
    { ten: B.tt, gia: 49000 },
    { ten: B.ttmat, gia: 29000 },
    { ten: B.mnhan, phuKey: 'nangCo', gia: 49000 },
    { ten: { vi: 'Massage mặt', en: 'Facial massage', ko: '페이셜 마사지', zh: '臉部按摩' }, phu: M15, gia: 89000 },
    { ten: { vi: 'Chiếu đèn ánh sáng sinh học', en: 'LED light therapy', ko: 'LED 광테라피', zh: 'LED 光療' }, gia: 49000 },
    { ten: B.mmat, gia: 19000 },
  ] },
];

const esc = (s = '') => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
export const tienGoi = (n, lang) => n.toLocaleString(lang === 'vi' ? 'vi-VN' : 'en-US') + '₫';
const url = (site, lang) => `${site.url}${BASE[lang]}/goi-dau/`;

function trang(site, lang, coAnh) {
  const U = UI[lang], C = UI_BANG_GIA[lang];
  const thang = new Intl.DateTimeFormat('vi-VN', { month: '2-digit', year: 'numeric', timeZone: 'Asia/Ho_Chi_Minh' }).format(new Date());
  const tel = '+84933528501';
  const maps = site.mapsUrl || 'https://maps.app.goo.gl/ic8B2eEiF8PWipZg7';
  // Ảnh lấy từ kho ảnh (content/media/goi-dau, do cron tải) nếu đã có, chưa có thì dùng ảnh cắt từ menu.
  const anh = (ten) => (coAnh.has(ten) ? `/media/goi-dau/${ten}` : `/images/goi-dau/${ten}`);
  const alts = LANGS.map((l) => `<link rel="alternate" hreflang="${HREFLANG[l]}" href="${url(site, l)}">`).join('\n');
  const muc = [...GOI.map((g, i) => ({ id: g.id, chip: `${U.goi} ${String(i + 1).padStart(2, '0')}`, ten: g.ten[lang] })),
    { id: 'le', chip: U.le, ten: U.le }];
  const chips = muc.map((m, i) => `<a href="#${m.id}" data-cat="${m.id}"${i ? '' : ' class="on"'}>${esc(m.chip)}</a>`).join('');
  const pager = (i) => {
    const p = muc[i - 1], q = muc[i + 1];
    const a = (n, cls, txt) => `<a class="${cls}" href="#${n.id}" data-go="${n.id}">${txt}</a>`;
    return `<nav class="pager">${p ? a(p, 'prev', '← ' + esc(p.ten)) : '<span></span>'}${q ? a(q, 'next', esc(q.ten) + ' →') : ''}</nav>`;
  };

  const goiHtml = GOI.map((g, i) => {
    const so = String(i + 1).padStart(2, '0');
    const buoc = g.buoc.map((k) => `<li>${esc(B[k][lang])}</li>`).join('');
    const dau = DAU_GOI.map((d, j) => `<div class="row sp"><img src="/images/goi-dau/${d.anh}" alt="${esc(d.ten[lang])}" loading="lazy" width="204" height="228"><span class="nm">${esc(d.ten[lang])}<small>${esc(d.mo[lang])}</small><small class="mo2">${esc(d.phu[lang])}</small></span><span class="pr">${tienGoi(g.gia[j], lang)}</span></div>`).join('');
    const mn = g.matNa ? `<div class="grp">${esc(U.matNa)} <i>· ${esc(U.matNaSub)}</i></div>` + MAT_NA.map((m) =>
      `<div class="row"><span class="nm">${esc(m.ten[lang])}</span><span class="pr">${m.them ? '+' + tienGoi(m.them, lang) : esc(U.trongGoi)}</span></div>`).join('') : '';
    return `<section class="cat" id="${g.id}">
  <div class="media"><img src="${anh(g.id + '.jpg')}" alt="${esc(g.ten[lang])}" loading="${i ? 'lazy' : 'eager'}">
    <div class="cap"><span>${esc(U.goi)} ${so} · ${g.phut} ${esc(U.phut)}${g.signature ? ' · Signature' : ''}</span><h2>${esc(g.ten[lang])}</h2></div></div>
  <div class="pane"><div class="eyebrow">${esc(U.goi)} ${so} · ${g.phut} ${esc(U.phut)}${g.signature ? ' · Signature' : ''}</div>
    <p class="lead">${esc(g.mo[lang])}</p>
    <div class="grp">${esc(U.dauGoi)}</div>${dau}
    ${mn}
    <div class="grp">${esc(U.quyTrinh)}</div><ol class="buoc">${buoc}</ol>
    ${pager(i)}</div>
</section>`;
  }).join('\n');

  const leHtml = `<section class="cat" id="le">
  <div class="media"><img src="${anh('goi-2.jpg')}" alt="${esc(U.le)}" loading="lazy">
    <div class="cap"><span>À la carte</span><h2>${esc(U.le)}</h2></div></div>
  <div class="pane"><div class="eyebrow">${esc(U.bangGia)}</div><p class="lead">${esc(U.leNote)}</p>
    ${LE.map((n) => `<div class="grp">${esc(U[n.nhom])}</div>` + n.dong.map((d) => {
      const phu = d.phuKey ? U[d.phuKey] : (d.phu ? d.phu[lang] : '');
      return `<div class="row"><span class="nm">${esc(d.ten[lang])}${phu ? `<small>${esc(phu)}</small>` : ''}</span><span class="pr">${tienGoi(d.gia, lang)}</span></div>`;
    }).join('')).join('')}
    ${pager(GOI.length)}</div>
</section>`;

  const langLinks = LANGS.map((l) => `<a href="${BASE[l]}/goi-dau/${l === 'vi' ? '?lang=vi' : ''}" data-l="${l}"${l === lang ? ' class="on" aria-current="true"' : ''} lang="${HREFLANG[l]}">${LABEL[l]}</a>`).join('');
  const ld = {
    '@context': 'https://schema.org', '@type': 'WebPage', name: U.metaTitle, url: url(site, lang), inLanguage: HREFLANG[lang],
    about: { '@id': 'https://vessca.com/#business' },
  };
  const ic = {
    cal: '<svg viewBox="0 0 24 24"><path d="M7 3v3M17 3v3M4 9h16M5 5h14a1 1 0 0 1 1 1v13a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1z"/></svg>',
    tel: '<svg viewBox="0 0 24 24"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a1 1 0 0 1-1 1A16 16 0 0 1 4 5a1 1 0 0 1 1-1z"/></svg>',
    map: '<svg viewBox="0 0 24 24"><path d="M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/></svg>',
    share: '<svg viewBox="0 0 24 24"><path d="M12 15V3M8 7l4-4 4 4M5 12v7a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-7"/></svg>',
  };
  return `<!DOCTYPE html>
<html lang="${HREFLANG[lang]}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>${esc(U.metaTitle)}</title>
<meta name="description" content="${esc(U.metaDesc)}">
<link rel="canonical" href="${url(site, lang)}">
${alts}
<link rel="alternate" hreflang="x-default" href="${url(site, 'vi')}">
<meta property="og:type" content="website">
<meta property="og:title" content="${esc(U.metaTitle)}">
<meta property="og:description" content="${esc(U.metaDesc)}">
<meta property="og:url" content="${url(site, lang)}">
<meta property="og:image" content="${site.url}${anh('goi-2.jpg')}">
<meta property="og:site_name" content="VESSCA">
<meta name="theme-color" content="#111111">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@400;500&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
${lang === 'vi' ? `<script>
(function(){try{
  if(/[?&]lang=vi/.test(location.search)){ localStorage.setItem('vessca-lang','vi'); return; }
  var l=localStorage.getItem('vessca-lang');
  if(!l){ l=((navigator.languages&&navigator.languages[0])||navigator.language||'').slice(0,2).toLowerCase(); }
  if(l==='en'||l==='ko'||l==='zh') location.replace('/'+l+'/goi-dau/'+location.hash);
}catch(e){}})();
</script>` : ''}
<script type="application/ld+json">${JSON.stringify(ld).replace(/</g, '\\u003c')}</script>
<style>
:root{--ink:#111;--soft:#6E6E6E;--line:rgba(17,17,17,.1);--dark:#161616;--dline:rgba(255,255,255,.14);
  --gold:#C7C7C7;--serif:'Noto Serif KR',Georgia,serif;--sans:'Inter',-apple-system,sans-serif;}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:var(--sans);font-weight:300;color:var(--ink);background:#0D0D0D;line-height:1.55;-webkit-font-smoothing:antialiased}
a{color:inherit;text-decoration:none}
.media img{display:block;width:100%;height:100%;object-fit:cover}
.top{position:sticky;top:0;z-index:30;background:#fff;box-shadow:0 1px 0 var(--line)}
.top-in{max-width:1180px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;gap:10px;padding:12px 18px}
.brand{display:flex;align-items:center;gap:10px}
.brand svg{width:26px;height:28px;color:var(--ink)}
.brand b{display:block;font-weight:600;font-size:16px;letter-spacing:.24em}
.brand small{display:block;font-size:8.5px;letter-spacing:.16em;color:var(--soft);margin-top:1px}
.mang{display:flex;border:1px solid var(--ink);border-radius:999px;overflow:hidden;flex:none}
.mang a{font-size:12.5px;padding:7px 14px;min-height:34px;display:flex;align-items:center;white-space:nowrap}
.mang a.on{background:var(--ink);color:#fff}
.langs{display:flex;gap:4px}.langs a{font-size:10.5px;border:1px solid var(--line);padding:4px 7px;color:var(--soft)}
.langs a.on{background:var(--ink);color:#fff;border-color:var(--ink)}
.langs{flex:none}.langs a{white-space:nowrap}
@media(max-width:350px){.top-in{padding-left:12px;padding-right:12px;gap:8px}.mang a{padding:7px 9px;font-size:12px}.langs{gap:3px}.langs a{padding:4px 5px}}
.chips{max-width:1180px;margin:0 auto;display:flex;gap:8px;overflow-x:auto;padding:2px 18px 12px;scrollbar-width:none;-webkit-overflow-scrolling:touch}
.chips::-webkit-scrollbar{display:none}
.chips a{flex:none;font-size:13px;border:1px solid var(--line);border-radius:999px;padding:8px 15px;white-space:nowrap;background:#fff;transition:background .2s,color .2s}
.chips a.on{background:var(--ink);color:#fff;border-color:var(--ink)}
.hero{position:relative;background:#111;color:#fff;overflow:hidden}
.hero::before{content:"";position:absolute;inset:0;background:url(${anh('goi-4.jpg')}) center/cover;opacity:.34;filter:saturate(.75)}
.hero::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(17,17,17,.35),rgba(17,17,17,.92))}
.hero-in{position:relative;z-index:1;max-width:1180px;margin:0 auto;padding:44px 18px 30px}
.eyebrow{font-size:11.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--gold)}
.hero h1{font-family:var(--serif);font-weight:400;font-size:clamp(30px,6.6vw,50px);line-height:1.15;margin:10px 0 12px}
.hero p{color:#CFCFCF;font-size:14.5px;max-width:620px}
.info{display:flex;flex-wrap:wrap;gap:4px 18px;margin-top:16px;font-size:12.5px;color:#A9A9A9}
.acts{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-top:20px;max-width:560px}
.acts a,.acts button{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:5px;min-height:62px;border:1px solid var(--dline);font:inherit;font-size:12px;font-weight:400;letter-spacing:.02em;background:transparent;color:#fff;cursor:pointer}
.acts svg{width:19px;height:19px;fill:none;stroke:currentColor;stroke-width:1.5;stroke-linecap:round;stroke-linejoin:round}
.acts .main{background:#fff;color:var(--ink);border-color:#fff}
.list{max-width:1180px;margin:0 auto;padding:0 0 10px}
.cat{display:flex;flex-direction:column;background:var(--dark);border-top:1px solid #000}
.media{position:relative;aspect-ratio:16/10;background:#000;overflow:hidden}
.media img{filter:saturate(.9) brightness(.86)}
.media::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 45%,rgba(0,0,0,.78))}
.cap{position:absolute;left:20px;right:20px;bottom:16px;z-index:1;color:#fff}
.cap span{font-size:11.5px;letter-spacing:.12em;color:var(--gold);text-transform:uppercase}
.cap h2{font-family:var(--serif);font-weight:400;font-size:24px;line-height:1.2;margin-top:2px}
.pane{color:#F0F0F0;padding:22px 20px 26px;min-width:0}
.pane .eyebrow{margin-bottom:8px}
.lead{font-size:14.5px;color:#CFCFCF;line-height:1.6}
.grp{font-size:11.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--gold);margin-top:22px;padding-top:16px;border-top:1px solid rgba(255,255,255,.18)}
.grp i{font-style:normal;text-transform:none;letter-spacing:.02em;color:#9A9A9A}
.row{display:flex;justify-content:space-between;align-items:baseline;gap:14px;padding:13px 0;border-bottom:1px dotted rgba(255,255,255,.16)}
.row .nm{font-size:14.5px;min-width:0;overflow-wrap:anywhere;flex:1}
.row .nm small{display:block;font-size:12px;color:#B5B5B5;margin-top:3px;line-height:1.5}
.row .nm small.mo2{color:#8C8C8C;font-size:11.5px}
.row .pr{font-size:15px;color:#fff;white-space:nowrap;font-weight:400}
.row.sp{align-items:center}
.row.sp img{flex:none;width:54px;height:60px;object-fit:cover;border-radius:4px;background:#EFEAE2}
.buoc{list-style:none;counter-reset:b;margin-top:6px}
.buoc li{counter-increment:b;display:flex;gap:12px;padding:9px 0;font-size:13.5px;color:#DADADA;border-bottom:1px dotted rgba(255,255,255,.1)}
.buoc li::before{content:counter(b,decimal-leading-zero);font-size:11px;color:var(--gold);letter-spacing:.06em;padding-top:2px;flex:none;width:20px}
.js .cat{display:none}.js .cat.show{display:flex;animation:hien .25s ease}
@keyframes hien{from{opacity:0}to{opacity:1}}
.pager{display:flex;justify-content:space-between;gap:10px;margin-top:26px}
.pager a{font-size:13px;color:#EDEDED;border:1px solid var(--dline);padding:11px 14px;min-height:44px;display:flex;align-items:center;max-width:48%}
.pager a.next{margin-left:auto;background:#fff;color:var(--ink);border-color:#fff}
.foot{max-width:1180px;margin:0 auto;padding:28px 18px 120px;color:#8A8A8A;font-size:12.5px}
.foot p{margin-bottom:6px}.foot a{color:#CFCFCF;text-decoration:underline}
.bar{position:fixed;left:0;right:0;bottom:0;z-index:40;background:rgba(17,17,17,.94);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);
  border-top:1px solid var(--dline);padding:10px 16px calc(10px + env(safe-area-inset-bottom));display:flex;gap:8px;justify-content:center}
.bar a{flex:1;max-width:280px;display:flex;align-items:center;justify-content:center;min-height:46px;font-size:14px;font-weight:400;letter-spacing:.02em;border:1px solid var(--dline);color:#fff}
.bar a.main{background:#fff;color:var(--ink);border-color:#fff}
.toast{position:fixed;left:50%;bottom:86px;transform:translateX(-50%);background:#fff;color:var(--ink);font-size:13px;padding:8px 14px;border-radius:999px;opacity:0;transition:opacity .2s;pointer-events:none;z-index:50}
.toast.show{opacity:1}
@media(max-width:560px){.brand span{display:none}}
@media(min-width:700px){
  .hero-in{padding:64px 28px 40px}
  .chips{padding-left:28px;padding-right:28px}.top-in{padding-left:28px;padding-right:28px}
  .cat{flex-direction:row;align-items:stretch}
  .media{flex:1 1 0;aspect-ratio:auto;position:sticky;top:var(--top-h,120px);align-self:flex-start;height:calc(100vh - var(--top-h,120px) - 66px);min-height:380px;max-height:640px}
  .media img{position:absolute;inset:0}
  .pane{flex:1 1 0;padding:34px 30px 34px;border-left:1px solid var(--dline)}
  .cap{left:28px;bottom:24px}.cap h2{font-size:28px}
}
@media(min-width:1024px){.media{flex:1.05 1 0}.buoc{columns:2;column-gap:28px}.buoc li{break-inside:avoid}}
@media print{.top,.bar,.acts,.chips,.pager,.hero::before{display:none}.foot{padding-bottom:0}.js .cat{display:flex}}
</style>
</head>
<body>
<script>document.body.className='js'</script>
<header class="top">
  <div class="top-in">
    <a class="brand" href="${BASE[lang]}/" aria-label="VESSCA">${LOGO_SVG}<span><b>VESSCA</b><small>KOREAN NAIL LOUNGE</small></span></a>
    <nav class="mang" aria-label="${esc(U.bangGia)}"><a href="${BASE[lang]}/bang-gia/${lang === 'vi' ? '?lang=vi' : ''}">${esc(U.tabNail)}</a><a class="on" aria-current="page" href="${BASE[lang]}/goi-dau/${lang === 'vi' ? '?lang=vi' : ''}">${esc(U.tabGoi)}</a></nav>
    <nav class="langs" aria-label="Language">${langLinks}</nav>
  </div>
  <nav class="chips" id="chips">${chips}</nav>
</header>
<div class="hero"><div class="hero-in">
  <div class="eyebrow">VESSCA · Head Spa</div>
  <h1>${esc(U.title)}</h1>
  <p>${esc(U.intro)}</p>
  <div class="info"><span>${esc(C.address)}</span><span>${esc(C.hours)}</span><span>0933.528.501</span></div>
  <div class="acts">
    <a class="main" href="/?dv=goi#booking" data-tk="Gội đầu: Đặt lịch">${ic.cal}${esc(C.book)}</a>
    <a href="tel:${tel}">${ic.tel}${esc(C.call)}</a>
    <a href="${maps}" target="_blank" rel="noopener">${ic.map}${esc(C.map)}</a>
    <button type="button" id="shareBtn" data-tk="Gội đầu: Chia sẻ">${ic.share}${esc(C.share)}</button>
  </div>
</div></div>
<main class="list">
${goiHtml}
${leHtml}
</main>
<div class="foot">
  <p>${esc(C.updated)}: ${esc(thang)} · <a href="${BASE[lang]}/">${esc(C.home)}</a> · <a href="${BASE[lang]}/bang-gia/${lang === 'vi' ? '?lang=vi' : ''}">${esc(U.bangGia)} ${esc(U.tabNail)}</a> · <a href="${BASE[lang]}/blog/">${esc(C.blog)}</a></p>
</div>
<div class="bar"><a href="tel:${tel}">${esc(C.call)} 0933.528.501</a><a class="main" href="/?dv=goi#booking" data-tk="Gội đầu: Đặt lịch">${esc(C.book)}</a></div>
<div class="toast" id="toast">${esc(C.copied)}</div>
<script>
(function(){
  [].forEach.call(document.querySelectorAll('.langs a'),function(a){
    a.addEventListener('click',function(){ try{ localStorage.setItem('vessca-lang',a.getAttribute('data-l')); }catch(e){} });
  });
  var b=document.getElementById('shareBtn'), t=document.getElementById('toast');
  b.addEventListener('click',function(){
    var u=location.href.split('#')[0].split('?')[0];
    if(navigator.share){ navigator.share({title:document.title,url:u}).catch(function(){}); return; }
    (navigator.clipboard?navigator.clipboard.writeText(u):Promise.reject()).then(function(){
      t.classList.add('show'); setTimeout(function(){t.classList.remove('show');},1600);
    }).catch(function(){ prompt('Link:',u); });
  });
  var chips=[].slice.call(document.querySelectorAll('#chips a'));
  var hdr=document.querySelector('.top'), list=document.querySelector('.list');
  function setTop(){ document.documentElement.style.setProperty('--top-h',hdr.offsetHeight+'px'); }
  setTop(); window.addEventListener('resize',setTop);
  function chon(cat,cuon){
    var s=document.getElementById(cat); if(!s) return;
    [].forEach.call(document.querySelectorAll('.cat'),function(c){ c.classList.toggle('show',c===s); });
    chips.forEach(function(a){
      var on=a.dataset.cat===cat; a.classList.toggle('on',on);
      if(on){ var bar=a.parentNode; bar.scrollTo({left:a.offsetLeft-(bar.clientWidth-a.offsetWidth)/2,behavior:'smooth'}); }
    });
    if(cuon){ var y=list.getBoundingClientRect().top+window.scrollY-hdr.offsetHeight; if(window.scrollY>y+1||cuon==='luon') window.scrollTo({top:y,behavior:'instant'}); }
    history.replaceState(null,'',location.pathname+location.search+'#'+cat);
  }
  chips.forEach(function(a){ a.addEventListener('click',function(e){ e.preventDefault(); chon(a.dataset.cat,true); }); });
  [].forEach.call(document.querySelectorAll('[data-go]'),function(a){ a.addEventListener('click',function(e){ e.preventDefault(); chon(a.dataset.go,'luon'); }); });
  var h=location.hash.slice(1), dau=chips[0]&&chips[0].dataset.cat;
  chon(document.getElementById(h)&&document.getElementById(h).classList.contains('cat')?h:dau,false);
  if(!h) history.replaceState(null,'',location.pathname+location.search);
  window.addEventListener('hashchange',function(){ var k=location.hash.slice(1), e=document.getElementById(k); if(e&&e.classList.contains('cat')) chon(k,'luon'); });
})();
</script>
<script src="/tk.js" defer></script>
</body>
</html>`;
}

/** coAnh: Set tên file đã có trong content/media/goi-dau (ảnh cron tải về). */
export function trangGoiDau(site, coAnh = new Set()) {
  return LANGS.map((l) => ({
    dir: (BASE[l] + '/goi-dau').replace(/^\//, ''),
    html: trang(site, l, coAnh),
    loc: url(site, l),
    lang: l,
  }));
}
export const GOI_DAU_UI = UI;
