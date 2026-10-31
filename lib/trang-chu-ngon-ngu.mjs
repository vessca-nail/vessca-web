/**
 * ============================================================
 *  TRANG CHỦ THEO NGÔN NGỮ — /en/, /ko/, /zh/
 * ============================================================
 *  Trang chủ (src/index.html) đổi ngôn ngữ ngay trong trình duyệt bằng bảng I18N.
 *  Google chỉ thấy một địa chỉ "/" nên khách nước ngoài tìm bằng tiếng Anh/Hàn/Trung
 *  không bao giờ gặp trang chủ. File này dựng sẵn bản đầy đủ của trang chủ cho từng
 *  ngôn ngữ ở địa chỉ riêng, kèm hreflang, để Google lập chỉ mục được.
 *
 *  Không sửa src/index.html — mọi biến đổi làm trên bản dựng trong dist/.
 */

export const HOME_LANGS = ['vi', 'en', 'ko', 'zh'];
export const homePath = (l) => (l === 'vi' ? '/' : `/${l}/`);

const HREFLANG = { vi: 'vi-VN', en: 'en', ko: 'ko', zh: 'zh-Hans' };
const OG_LOCALE = { vi: 'vi_VN', en: 'en_US', ko: 'ko_KR', zh: 'zh_CN' };

// Mô tả trang cho Google — dịch sát nghĩa thẻ description tiếng Việt, không thêm thông tin mới
const MO_TA = {
  en: 'VESSCA — Korean-style nail salon in Gia Dinh, Binh Thanh, Ho Chi Minh City. Trained technicians and genuine imported products. Book your appointment online.',
  ko: 'VESSCA — 호치민시 빈탄 자딘에 있는 한국식 네일샵입니다. 전문 교육을 받은 기술자와 정품 수입 제품. 온라인으로 예약하세요.',
  zh: 'VESSCA — 位于胡志明市平盛郡嘉定坊的韩式美甲店。技师经过专业培训，使用正品进口产品。欢迎在线预约。',
};

export function docI18N(html) {
  const i = html.indexOf('const I18N = ');
  if (i < 0) return null;
  let a = html.indexOf('{', i), sau = 0;
  for (let k = a; k < html.length; k++) {
    if (html[k] === '{') sau++;
    else if (html[k] === '}' && !--sau) {
      try { return Function(`"use strict";return (${html.slice(a, k + 1)});`)(); } catch { return null; }
    }
  }
  return null;
}


// Chữ mô tả ảnh (alt) và nhãn — giúp tìm ảnh trên Google và đọc bằng trình đọc màn hình
const NHAN = {
  'Bảng màu Popsicle Collection từ Aurora Queen': { en: 'Popsicle Collection colour palette by Aurora Queen', ko: 'Aurora Queen 팝시클 컬렉션 컬러 팔레트', zh: 'Aurora Queen Popsicle 系列色板' },
  'Bảng màu TinkerGel Neverland từ Kiss New York Gel Pro': { en: 'TinkerGel Neverland colour palette by Kiss New York Gel Pro', ko: 'Kiss New York Gel Pro 팅커젤 네버랜드 컬러 팔레트', zh: 'Kiss New York Gel Pro TinkerGel Neverland 色板' },
  'Bộ sơn Snow Velvet Candy': { en: 'Snow Velvet Candy gel polish set', ko: '스노우 벨벳 캔디 젤 세트', zh: 'Snow Velvet Candy 甲油胶套装' },
  'Chăm sóc móng &amp; thư giãn': { en: 'Nail care &amp; relaxation', ko: '네일 케어 &amp; 휴식', zh: '指甲护理与放松' },
  'Design, đính phụ kiện': { en: 'Nail art and decorations', ko: '네일 아트, 파츠 장식', zh: '美甲彩绘与饰品' },
  'Kỹ thuật viên đang chăm sóc nail cho khách tại tiệm': { en: 'A technician doing a manicure for a client at the salon', ko: '매장에서 고객의 네일을 관리하는 기술자', zh: '技师正在店内为顾客护理指甲' },
  'Nail chrome nude tông trung tính': { en: 'Nude chrome nails in a neutral tone', ko: '뉴트럴 톤 누드 크롬 네일', zh: '中性色裸色镜面美甲' },
  'Nail glazed jelly trắng sữa bóng gương': { en: 'Milky white glazed jelly nails with a mirror shine', ko: '우윳빛 글레이즈드 젤리 네일', zh: '奶白色釉面果冻美甲' },
  'Nail ánh nhũ lấp lánh': { en: 'Sparkling glitter nails', ko: '반짝이는 글리터 네일', zh: '闪亮亮片美甲' },
  'Nail đỏ cà chua nổi bật': { en: 'Bold tomato-red nails', ko: '선명한 토마토 레드 네일', zh: '醒目的番茄红美甲' },
  'Những lọ sơn gel nhiều màu sắp trên kệ': { en: 'Gel polish bottles in many colours on a shelf', ko: '선반에 진열된 다양한 색상의 젤 폴리시', zh: '架上摆放的多色甲油胶' },
  'Nối móng, đắp gel': { en: 'Nail extensions and builder gel', ko: '연장, 젤 오버레이', zh: '延长甲与建构胶' },
  'Sơn Hàn cao cấp': { en: 'Premium Korean gel polish', ko: '프리미엄 한국 젤', zh: '高端韩国甲油胶' },
  'Sơn gel cơ bản': { en: 'Classic gel polish', ko: '기본 젤 네일', zh: '基础甲油胶' },
  'VESSCA trên Google Maps': { en: 'VESSCA on Google Maps', ko: 'Google 지도의 VESSCA', zh: 'VESSCA 在 Google 地图上' },
};
// Đơn vị giá — dùng đúng chữ của trang bảng giá (lib/bang-gia.mjs)
const DON_VI = {
  en: { from: (p) => `from ${p}`, each: 'piece', color: 'colour', set: 'set' },
  ko: { from: (p) => `${p}부터`, each: '개', color: '컬러', set: '세트' },
  zh: { from: (p) => `${p} 起`, each: '颗', color: '色', set: '套' },
};
function dichPhu(html, lang) {
  const U = DON_VI[lang];
  let out = html.replace(/(\s(?:alt|title|aria-label)=")([^"]*)"/g, (m, a, v) => (NHAN[v] ? `${a}${NHAN[v][lang]}"` : m));
  out = out
    .replace(/>từ ([0-9.]+₫) \/ (bộ|viên|màu)</g, (m, p, d) => `>${U.from(p)} / ${U[{ 'bộ': 'set', 'viên': 'each', 'màu': 'color' }[d]]}<`)
    .replace(/>từ ([0-9.]+₫)</g, (m, p) => `>${U.from(p)}<`)
    .replace(/>([+]?[0-9.]+₫) \/ (bộ|viên|màu)</g, (m, p, d) => `>${p} / ${U[{ 'bộ': 'set', 'viên': 'each', 'màu': 'color' }[d]]}<`);
  return out;
}

const escAttr = (s) => String(s).replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;');

/** Thay nội dung bên trong mọi phần tử có data-i18n — giống applyLanguage() bản máy tính */
function apDungI18N(html, T) {
  const re = /<([a-zA-Z][\w-]*)\b[^>]*\bdata-i18n="([^"]+)"[^>]*>/g;
  let out = '', vt = 0, m, dem = 0;
  while ((m = re.exec(html))) {
    const [mo, the, key] = m;
    if (mo.endsWith('/>') || T[key] === undefined) continue;
    const batDau = m.index + mo.length;
    // tìm thẻ đóng tương ứng, tính cả thẻ cùng tên lồng bên trong
    const reThe = new RegExp(`<(/?)${the}\\b[^>]*>`, 'gi');
    reThe.lastIndex = batDau;
    let sau = 1, t, ketThuc = -1;
    while ((t = reThe.exec(html))) {
      if (t[1]) { if (!--sau) { ketThuc = t.index; break; } }
      else if (!t[0].endsWith('/>')) sau++;
    }
    if (ketThuc < 0 || batDau < vt) continue;
    out += html.slice(vt, batDau) + T[key];
    vt = ketThuc;
    re.lastIndex = ketThuc;
    dem++;
  }
  out += html.slice(vt);
  // placeholder ô nhập
  out = out.replace(/<[^>]*\bdata-i18n-ph="([^"]+)"[^>]*>/g, (the, key) =>
    T[key] === undefined ? the : the.replace(/\splaceholder="[^"]*"/, ` placeholder="${escAttr(T[key])}"`));
  return { html: out, dem };
}

/** Thẻ hreflang cho cả 4 trang chủ */
function theHreflang(site) {
  return HOME_LANGS.map((l) => `<link rel="alternate" hreflang="${HREFLANG[l]}" href="${site.url}${homePath(l)}">`).join('\n')
    + `\n<link rel="alternate" hreflang="x-default" href="${site.url}/">`;
}

/**
 * Sửa chung cho mọi bản trang chủ (kể cả tiếng Việt):
 *  - ngôn ngữ của trang cố định theo địa chỉ, không đoán theo trình duyệt.
 *    (Trước đây Googlebot — trình duyệt tiếng Anh — có thể thấy "/" thành tiếng Anh.)
 *  - nút đổi ngôn ngữ chuyển sang đúng địa chỉ của ngôn ngữ đó.
 *  - thêm hreflang.
 */
function suaChung(html, site, lang, canhBao) {
  let out = html;
  const thay = (cu, moi, ten) => {
    if (!out.includes(cu)) { canhBao(`không tìm thấy đoạn "${ten}" trong trang chủ — bỏ qua`); return; }
    out = out.replace(cu, moi);
  };
  thay("currentLang = saved || (['en','ko','zh'].includes(nav) ? nav : 'vi');",
       `currentLang = '${lang}'; void saved; void nav;`, 'chọn ngôn ngữ ban đầu');
  thay("btn.addEventListener('click', ()=> applyLanguage(btn.dataset.lang));",
       "btn.addEventListener('click', ()=>{ const l = btn.dataset.lang; location.href = l === 'vi' ? '/' : '/' + l + '/'; });",
       'nút đổi ngôn ngữ');
  out = out.replace(/<link rel="alternate" hreflang="[^"]*"[^>]*>\n?/g, '');
  out = out.replace(/<\/head>/i, `${theHreflang(site)}\n</head>`);
  return out;
}

/**
 * @param site  cấu hình web (site.url)
 * @param html  trang chủ tiếng Việt đã dựng (dist/index.html)
 * @returns { vi: html, en: html, ko: html, zh: html }
 */
export function dungTrangChu(site, html, canhBao = console.warn) {
  const I18N = docI18N(html);
  const ket = { vi: suaChung(html, site, 'vi', canhBao) };
  if (!I18N) { canhBao('không đọc được bảng I18N — chỉ dựng trang chủ tiếng Việt'); return ket; }

  for (const lang of HOME_LANGS.filter((l) => l !== 'vi')) {
    const T = I18N[lang];
    if (!T) { canhBao(`bảng I18N thiếu "${lang}"`); continue; }
    let { html: out, dem } = apDungI18N(html, T);
    out = dichPhu(out, lang);
    const url = site.url + homePath(lang);
    const tieuDe = (T['meta.title'] || '').replace(/<[^>]+>/g, '');
    out = out
      .replace(/<html\b([^>]*)\blang="[^"]*"/i, `<html$1lang="${HREFLANG[lang]}"`)
      .replace(/<title>[^<]*<\/title>/i, `<title>${escAttr(tieuDe)}</title>`)
      .replace(/(<meta name="description" content=")[^"]*"/i, `$1${escAttr(MO_TA[lang])}"`)
      .replace(/(<meta property="og:title" content=")[^"]*"/i, `$1${escAttr(tieuDe)}"`)
      .replace(/(<meta property="og:description" content=")[^"]*"/i, `$1${escAttr(MO_TA[lang])}"`)
      .replace(/(<meta property="og:locale" content=")[^"]*"/i, `$1${OG_LOCALE[lang]}"`)
      .replace(/(<meta property="og:url" content=")[^"]*"/i, `$1${url}"`)
      .replace(/(<link rel="canonical" href=")[^"]*"/i, `$1${url}"`)
      .replace(/(<link rel="alternate" type="application\/rss\+xml"[^>]*href=")[^"]*"/i, `$1${site.url}/${lang}/rss.xml"`)
      // đường dẫn tương đối (images/…, videos/…) sẽ gãy khi trang nằm ở /en/
      .replace(/(["'`(])(images|videos|assets)\//g, '$1/$2/')
      // menu trỏ tới blog và bảng giá đúng ngôn ngữ, kể cả khi không chạy JS
      .replace(/href="\/bang-gia\/"/g, `href="/${lang}/bang-gia/"`)
      .replace(/href="\/blog\/"/g, `href="/${lang}/blog/"`)
      // nút ngôn ngữ đang chọn
      .replace(/(<button type="button" data-lang="vi") class="active">/, '$1>')
      .replace(new RegExp(`(<button type="button" data-lang="${lang}")>`), '$1 class="active">');
    ket[lang] = suaChung(out, site, lang, canhBao);
    ket[lang + ':dem'] = dem;
  }
  return ket;
}
