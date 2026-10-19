/**
 * ============================================================
 *  VESSCA — CẤU HÌNH CHUNG CỦA WEBSITE
 * ============================================================
 *  File này là "bộ não SEO" của trang. Sửa ở đây một lần,
 *  toàn bộ trang blog / sitemap / thẻ Google sẽ tự đổi theo.
 *  Không cần biết lập trình — chỉ sửa phần trong dấu nháy '...'
 */

export const site = {
  // --- Thông tin cơ bản ---
  url: 'https://vessca.com',
  name: 'VESSCA',
  legalName: 'VESSCA Korean Nail Lounge',
  tagline: 'Korean Nail Lounge',
  description:
    'VESSCA — tiệm nail phong cách Hàn Quốc tại Gia Định, Bình Thạnh, TP. Hồ Chí Minh. ' +
    'Kỹ thuật viên đào tạo bài bản, sản phẩm nhập khẩu chính hãng, mỗi khách một kỹ thuật viên riêng.',
  locale: 'vi_VN',
  lang: 'vi',

  // --- Liên hệ ---
  phone: '093 352 8501',
  phoneIntl: '+84933528501',
  email: 'hello@vessca.com',

  // --- Địa chỉ (dùng cho Google Maps / tìm kiếm địa phương) ---
  address: {
    street: '251/30 Lê Quang Định',
    ward: 'Gia Định',
    district: 'Bình Thạnh',
    city: 'TP. Hồ Chí Minh',
    region: 'SG',
    postalCode: '70000',
    country: 'VN',
    // Toạ độ lấy đúng từ hồ sơ Google Maps của tiệm (VESSCA Nail).
    // Trước đây để sai khoảng 600m — Google đối chiếu toạ độ này với
    // hồ sơ Maps, lệch là mất điểm tìm kiếm địa phương.
    latitude: 10.8094936,
    longitude: 106.6920892,
  },

  openingHours: 'Mo-Su 10:00-20:00',
  openingHoursText: '10:00 – 20:00, tất cả các ngày trong tuần',
  priceRange: '₫₫',

  // --- Mạng xã hội ---
  social: {
    instagram: 'https://www.instagram.com/vessca.nail/',
    facebook: 'https://www.facebook.com/profile.php?id=61595364530293',
    tiktok: '',
    // Hồ sơ Google Maps của tiệm. Khai báo ở đây để Google nối được
    // website với hồ sơ Maps — hai bên công nhận nhau thì cả hai cùng lên hạng.
    googleMaps: 'https://maps.app.goo.gl/ic8B2eEiF8PWipZg7',
  },

  // --- Ảnh mặc định khi chia sẻ lên Facebook/Zalo ---
  defaultImage: '/assets/blog-default.jpg',

  blog: {
    path: '/blog',
    postsPerPage: 12,
  },
};

/**
 * ============================================================
 *  BA NGÔN NGỮ CỦA BLOG
 * ============================================================
 *  Tiếng Việt ở /blog/, tiếng Anh ở /en/blog/, tiếng Trung ở /zh/blog/.
 *
 *  Mỗi bản có đường dẫn riêng và được nối với nhau bằng thẻ hreflang,
 *  để Google biết đây là cùng một bài ở ba thứ tiếng — chứ không phải
 *  ba bài trùng nội dung. Thiếu thẻ này thì Google tự chọn một bản để
 *  hiện và bỏ hai bản kia.
 */
export const languages = {
  vi: {
    code: 'vi',
    htmlLang: 'vi',
    hreflang: 'vi-VN',
    locale: 'vi_VN',
    label: 'Tiếng Việt',
    short: 'VI',
    base: '', // /blog/
    isDefault: true,
    blogTitle: 'Blog VESSCA — Kiến thức làm nail & chăm sóc móng',
    blogDescription:
      'Cẩm nang làm nail Hàn Quốc, chăm sóc móng tại nhà, xu hướng màu sơn gel và ' +
      'kinh nghiệm chọn tiệm nail uy tín tại Bình Thạnh, TP.HCM — viết bởi đội ngũ VESSCA.',
    blogHeading: 'Cẩm nang nail &amp; chăm sóc móng',
    ui: {
      eyebrow: 'Blog',
      navAbout: 'Câu chuyện',
      navServices: 'Dịch vụ',
      navBlog: 'Blog',
      navBook: 'Đặt lịch',
      all: 'Tất cả',
      readTime: 'phút đọc',
      related: 'Bài viết liên quan',
      ctaTitle: 'Ghé VESSCA một buổi?',
      ctaText:
        'Mỗi lịch hẹn được sắp xếp riêng — một kỹ thuật viên cho một khách, không chồng ca, không vội.',
      ctaBook: 'Đặt lịch ngay',
      contact: 'Liên hệ',
      hours: 'Giờ mở cửa',
      hoursText: '10:00 – 20:00, tất cả các ngày trong tuần',
      blogLink: 'Blog &amp; cẩm nang nail',
      empty: 'Bài viết đầu tiên đang được chuẩn bị. Hẹn bạn sớm nhé.',
      home: 'Trang chủ',
      notFound: 'Không tìm thấy trang này',
      notFoundText: 'Có thể đường dẫn đã thay đổi, hoặc bạn gõ nhầm một ký tự.',
      backHome: 'Về trang chủ',
      seeBlog: 'Xem blog',
      tagline: 'Korean Nail Lounge',
      otherLangs: 'Ngôn ngữ khác',
    },
  },

  en: {
    code: 'en',
    htmlLang: 'en',
    hreflang: 'en',
    locale: 'en_US',
    label: 'English',
    short: 'EN',
    base: '/en',
    blogTitle: 'VESSCA Journal — Korean Nail Care Guides in Saigon',
    blogDescription:
      'Korean nail techniques, at-home nail care, gel colour trends and how to pick a ' +
      'trustworthy nail salon in Binh Thanh, Ho Chi Minh City — written by the VESSCA team.',
    blogHeading: 'Nail care, the Korean way',
    ui: {
      eyebrow: 'Journal',
      navAbout: 'Our story',
      navServices: 'Services',
      navBlog: 'Journal',
      navBook: 'Book',
      all: 'All',
      readTime: 'min read',
      related: 'Related reading',
      ctaTitle: 'Come spend an hour with us',
      ctaText:
        'Every appointment is booked privately — one technician, one guest, no overlapping slots, no rush.',
      ctaBook: 'Book an appointment',
      contact: 'Contact',
      hours: 'Opening hours',
      hoursText: '10:00 – 20:00, every day',
      blogLink: 'Journal &amp; nail guides',
      empty: 'Our first article is on the way. See you soon.',
      home: 'Home',
      notFound: 'We couldn’t find that page',
      notFoundText: 'The link may have changed, or a character may have slipped in.',
      backHome: 'Back to home',
      seeBlog: 'Read the journal',
      tagline: 'Korean Nail Lounge',
      otherLangs: 'Other languages',
    },
  },

  zh: {
    code: 'zh',
    htmlLang: 'zh-Hans',
    hreflang: 'zh-Hans',
    locale: 'zh_CN',
    label: '中文',
    short: '中文',
    base: '/zh',
    blogTitle: 'VESSCA 美甲志 — 胡志明市韩式美甲指南',
    blogDescription:
      '韩式美甲技术、居家护甲方法、甲油胶流行色，以及如何在胡志明市平盛郡挑选可靠的美甲店 — 由 VESSCA 团队撰写。',
    blogHeading: '韩式美甲与护甲指南',
    ui: {
      eyebrow: '美甲志',
      navAbout: '关于我们',
      navServices: '服务项目',
      navBlog: '美甲志',
      navBook: '预约',
      all: '全部',
      readTime: '分钟阅读',
      related: '相关文章',
      ctaTitle: '来 VESSCA 坐一个下午',
      ctaText: '每位客人单独预约 — 一位技师只服务一位客人，不排重，不赶时间。',
      ctaBook: '立即预约',
      contact: '联系方式',
      hours: '营业时间',
      hoursText: '每天 10:00 – 20:00',
      blogLink: '美甲志与护甲指南',
      empty: '第一篇文章正在准备中，敬请期待。',
      home: '首页',
      notFound: '找不到这个页面',
      notFoundText: '链接可能已更改，或者地址输入有误。',
      backHome: '回到首页',
      seeBlog: '浏览美甲志',
      tagline: 'Korean Nail Lounge',
      otherLangs: '其他语言',
    },
  },
};

/** Thứ tự hiển thị nút đổi ngôn ngữ */
export const langOrder = ['vi', 'en', 'zh'];

/** Đường dẫn blog của một ngôn ngữ: vi → /blog, en → /en/blog */
export const blogPath = (lang) => `${languages[lang].base}${site.blog.path}`;

/**
 * ============================================================
 *  TỪ KHOÁ SEO — "mỏ vàng" để Google tìm thấy tiệm
 * ============================================================
 *  Đây là danh sách từ khoá khách hay gõ lên Google khi tìm tiệm nail.
 *  Trang admin sẽ gợi ý sẵn danh sách này mỗi khi bạn viết bài mới,
 *  bấm chọn là tự chèn vào bài — không cần nhớ.
 *
 *  Muốn thêm từ khoá mới: thêm một dòng vào đúng nhóm bên dưới.
 */
export const keywordLibrary = {
  'Địa phương': [
    'tiệm nail Bình Thạnh',
    'tiệm nail Gia Định',
    'làm nail Bình Thạnh',
    'nail Lê Quang Định',
    'tiệm nail quận Bình Thạnh',
    'tiệm nail TP.HCM',
    'làm móng Sài Gòn',
    'nail salon Hồ Chí Minh',
    'tiệm nail gần đây',
    'tiệm nail đẹp Bình Thạnh',
  ],
  'Phong cách Hàn Quốc': [
    'nail Hàn Quốc',
    'nail Hàn',
    'Korean nail',
    'nail style Hàn Quốc',
    'nail Hàn Quốc tối giản',
    'nail lounge',
    'tiệm nail cao cấp',
    'nail sang trọng',
  ],
  'Dịch vụ': [
    'sơn gel',
    'sơn thạch',
    'glass nail',
    'glass gel',
    'úp móng',
    'đắp móng bột',
    'nối móng',
    'nail art',
    'vẽ móng',
    'đính đá móng',
    'ombre nail',
    'nail trơn',
    'chăm sóc móng',
    'cắt da tay',
    'spa móng tay',
    'sơn móng chân',
    'làm móng tay đẹp',
  ],
  'Chủ đề bài viết': [
    'xu hướng nail',
    'màu nail hot',
    'nail màu trung tính',
    'chăm sóc móng tại nhà',
    'móng yếu phải làm sao',
    'bao lâu nên làm nail một lần',
    'sơn gel có hại không',
    'cách giữ nail lâu bong',
    'chọn tiệm nail uy tín',
    'giá làm nail',
    'nail cô dâu',
    'nail đi tiệc',
    'nail Tết',
  ],
};

/** Gộp tất cả từ khoá thành một mảng phẳng (dùng cho thẻ meta trang chủ blog) */
export const allKeywords = Object.values(keywordLibrary).flat();

/**
 * Tên danh mục ở ba thứ tiếng.
 * Bài viết vẫn lưu danh mục bằng tiếng Việt; bảng này chỉ để hiển thị.
 */
export const categoryLabels = {
  'Xu hướng & Cảm hứng': { en: 'Trends & Inspiration', zh: '流行趋势' },
  'Chăm sóc móng': { en: 'Nail Care', zh: '护甲知识' },
  'Kiến thức nghề nail': { en: 'Nail Know-how', zh: '美甲技术' },
  'Hậu trường VESSCA': { en: 'Inside VESSCA', zh: 'VESSCA 幕后' },
  'Hỏi & Đáp': { en: 'Questions & Answers', zh: '常见问答' },
};

/** Lấy tên danh mục theo ngôn ngữ, không có bản dịch thì giữ nguyên tiếng Việt */
export const categoryLabel = (cat, lang) =>
  lang === 'vi' ? cat : categoryLabels[cat]?.[lang] || cat;

/** Danh mục bài viết — hiện ở trang blog để khách lọc bài */
export const categories = [
  'Xu hướng & Cảm hứng',
  'Chăm sóc móng',
  'Kiến thức nghề nail',
  'Hậu trường VESSCA',
  'Hỏi & Đáp',
];
