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
    latitude: 10.8045,
    longitude: 106.6975,
  },

  openingHours: 'Mo-Su 10:00-20:00',
  openingHoursText: '10:00 – 20:00, tất cả các ngày trong tuần',
  priceRange: '₫₫',

  // --- Mạng xã hội ---
  social: {
    instagram: 'https://www.instagram.com/vessca.nail/',
    facebook: 'https://www.facebook.com/profile.php?id=61595364530293',
    tiktok: '',
  },

  // --- Ảnh mặc định khi chia sẻ lên Facebook/Zalo ---
  defaultImage: '/assets/blog-default.jpg',

  blog: {
    path: '/blog',
    title: 'Blog VESSCA — Kiến thức làm nail & chăm sóc móng',
    description:
      'Cẩm nang làm nail Hàn Quốc, chăm sóc móng tại nhà, xu hướng màu sơn gel và ' +
      'kinh nghiệm chọn tiệm nail uy tín tại Bình Thạnh, TP.HCM — viết bởi đội ngũ VESSCA.',
    postsPerPage: 12,
  },
};

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

/** Danh mục bài viết — hiện ở trang blog để khách lọc bài */
export const categories = [
  'Xu hướng & Cảm hứng',
  'Chăm sóc móng',
  'Kiến thức nghề nail',
  'Hậu trường VESSCA',
  'Hỏi & Đáp',
];
