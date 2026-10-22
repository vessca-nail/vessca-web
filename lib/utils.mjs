/** Các hàm tiện ích dùng chung cho build script và trang admin. */

/** Thoát ký tự đặc biệt để chèn an toàn vào HTML */
export function esc(str = '') {
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

/** Thoát ký tự đặc biệt để chèn vào XML (sitemap, RSS) */
export function escXml(str = '') {
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&apos;');
}

/** Bỏ dấu tiếng Việt — dùng để tạo đường dẫn bài viết (slug) */
export function removeDiacritics(str = '') {
  return String(str)
    .normalize('NFD')
    .replace(/[̀-ͯ]/g, '')
    .replace(/đ/g, 'd')
    .replace(/Đ/g, 'D');
}

/** "Chăm sóc móng mùa mưa" -> "cham-soc-mong-mua-mua" */
export function slugify(str = '') {
  return removeDiacritics(str)
    .toLowerCase()
    .replace(/[^a-z0-9\s-]/g, '')
    .trim()
    .replace(/\s+/g, '-')
    .replace(/-+/g, '-')
    .slice(0, 80)
    .replace(/^-|-$/g, '');
}

/** Bỏ toàn bộ thẻ HTML, lấy chữ thuần (dùng cho mô tả SEO) */
export function stripTags(html = '') {
  return String(html)
    .replace(/<script[\s\S]*?<\/script>/gi, ' ')
    .replace(/<style[\s\S]*?<\/style>/gi, ' ')
    .replace(/<[^>]+>/g, ' ')
    .replace(/&nbsp;/g, ' ')
    .replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'")
    .replace(/\s+/g, ' ')
    .trim();
}

/** Cắt chuỗi cho vừa độ dài mô tả SEO, không cắt giữa từ */
export function truncate(str = '', max = 158) {
  const s = stripTags(str);
  if (s.length <= max) return s;
  const cut = s.slice(0, max);
  const lastSpace = cut.lastIndexOf(' ');
  return (lastSpace > max * 0.6 ? cut.slice(0, lastSpace) : cut).trim() + '…';
}

const THANG = [
  'tháng 1', 'tháng 2', 'tháng 3', 'tháng 4', 'tháng 5', 'tháng 6',
  'tháng 7', 'tháng 8', 'tháng 9', 'tháng 10', 'tháng 11', 'tháng 12',
];
const MONTHS_EN = [
  'January', 'February', 'March', 'April', 'May', 'June',
  'July', 'August', 'September', 'October', 'November', 'December',
];

/** Ngày tháng theo đúng cách viết của từng ngôn ngữ */
export function formatDate(iso, lang = 'vi') {
  const d = new Date(iso);
  if (isNaN(d)) return '';
  const day = d.getDate(), mon = d.getMonth(), year = d.getFullYear();
  if (lang === 'en') return `${MONTHS_EN[mon]} ${day}, ${year}`;
  if (lang === 'zh') return `${year}年${mon + 1}月${day}日`;
  if (lang === 'ko') return `${year}년 ${mon + 1}월 ${day}일`;
  return `${day} ${THANG[mon]}, ${year}`;
}

/** Giữ tên cũ cho phần nào còn dùng */
export const formatDateVi = (iso) => formatDate(iso, 'vi');

/** Ước lượng thời gian đọc — tiếng Việt khoảng 200 từ/phút */
export function readingTime(html = '') {
  const words = stripTags(html).split(/\s+/).filter(Boolean).length;
  return Math.max(1, Math.round(words / 200));
}

/**
 * Lọc HTML bài viết: giữ lại thẻ định dạng an toàn, bỏ script/iframe/sự kiện.
 * Bảo vệ trang khỏi mã độc bị dán nhầm vào trình soạn thảo.
 */
const ALLOWED_TAGS = new Set([
  'p', 'br', 'strong', 'b', 'em', 'i', 'u', 's', 'blockquote',
  'h2', 'h3', 'h4', 'ul', 'ol', 'li', 'a', 'img', 'figure',
  'figcaption', 'hr', 'table', 'thead', 'tbody', 'tr', 'th', 'td', 'span',
]);
const ALLOWED_ATTRS = {
  a: ['href', 'title', 'target', 'rel'],
  img: ['src', 'alt', 'title', 'width', 'height', 'loading'],
  span: ['class'],
  td: ['colspan', 'rowspan'],
  th: ['colspan', 'rowspan'],
};

export function sanitizeHtml(html = '') {
  let out = String(html)
    .replace(/<script[\s\S]*?<\/script>/gi, '')
    .replace(/<style[\s\S]*?<\/style>/gi, '')
    .replace(/<iframe[\s\S]*?<\/iframe>/gi, '')
    .replace(/<!--[\s\S]*?-->/g, '');

  out = out.replace(/<\/?([a-zA-Z][a-zA-Z0-9]*)((?:[^>"']|"[^"]*"|'[^']*')*)>/g,
    (match, tag, attrs) => {
      const name = tag.toLowerCase();
      if (!ALLOWED_TAGS.has(name)) return '';
      if (match.startsWith('</')) return `</${name}>`;

      const allowed = ALLOWED_ATTRS[name] || [];
      const kept = [];
      const attrRe = /([a-zA-Z-]+)\s*=\s*("([^"]*)"|'([^']*)')/g;
      let m;
      while ((m = attrRe.exec(attrs))) {
        const key = m[1].toLowerCase();
        const value = m[3] ?? m[4] ?? '';
        if (!allowed.includes(key)) continue;
        if (/^on/i.test(key)) continue;
        if ((key === 'href' || key === 'src') && /^\s*(javascript|data|vbscript):/i.test(value)) continue;
        kept.push(`${key}="${esc(value)}"`);
      }
      // Link ra ngoài luôn mở tab mới và an toàn
      if (name === 'a') {
        const href = kept.find((a) => a.startsWith('href='));
        if (href && /href="https?:\/\//.test(href) && !href.includes('vessca.com')) {
          if (!kept.some((a) => a.startsWith('target='))) kept.push('target="_blank"');
          if (!kept.some((a) => a.startsWith('rel='))) kept.push('rel="noopener"');
        }
      }
      if (name === 'img' && !kept.some((a) => a.startsWith('loading='))) {
        kept.push('loading="lazy"');
      }
      const selfClosing = name === 'img' || name === 'br' || name === 'hr';
      return `<${name}${kept.length ? ' ' + kept.join(' ') : ''}${selfClosing ? ' /' : ''}>`;
    });

  return out.trim();
}
