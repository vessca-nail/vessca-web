/**
 * ============================================================
 *  VESSCA — LẤY SỐ LIỆU GOOGLE SEARCH CONSOLE
 * ============================================================
 *  Chạy mỗi sáng bằng GitHub Actions, ghi kết quả vào data/gsc/.
 *  Không cần mở máy, không cần ai đăng nhập.
 *
 *  Cần biến môi trường GSC_SA_KEY = toàn bộ nội dung file JSON
 *  của service account (lưu trong GitHub Secrets, không nằm trong repo).
 *
 *  Chạy tay:  GSC_SA_KEY="$(cat key.json)" node tools/gsc-fetch.mjs
 */

import crypto from 'node:crypto';
import fs from 'node:fs/promises';
import path from 'node:path';

const SITE = 'sc-domain:vessca.com';
const OUT_DIR = 'data/gsc';
const SCOPE = 'https://www.googleapis.com/auth/webmasters.readonly';

// --- Ký JWT bằng khoá riêng rồi đổi lấy access token ------------------
function base64url(input) {
  return Buffer.from(input).toString('base64')
    .replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
}

async function getAccessToken(sa) {
  const now = Math.floor(Date.now() / 1000);
  const header = base64url(JSON.stringify({ alg: 'RS256', typ: 'JWT' }));
  const claim = base64url(JSON.stringify({
    iss: sa.client_email,
    scope: SCOPE,
    aud: 'https://oauth2.googleapis.com/token',
    iat: now,
    exp: now + 3600,
  }));
  const signer = crypto.createSign('RSA-SHA256');
  signer.update(`${header}.${claim}`);
  const signature = base64url(signer.sign(sa.private_key));
  const assertion = `${header}.${claim}.${signature}`;

  const res = await fetch('https://oauth2.googleapis.com/token', {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams({
      grant_type: 'urn:ietf:params:oauth:grant-type:jwt-bearer',
      assertion,
    }),
  });
  if (!res.ok) {
    throw new Error(`Lấy access token thất bại (${res.status}): ${await res.text()}`);
  }
  return (await res.json()).access_token;
}

// --- Gọi Search Console Search Analytics ------------------------------
async function query(token, body) {
  const url = `https://searchconsole.googleapis.com/webmasters/v3/sites/${encodeURIComponent(SITE)}/searchAnalytics/query`;
  const res = await fetch(url, {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${token}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(body),
  });
  if (!res.ok) {
    throw new Error(`Search Console trả lỗi (${res.status}): ${await res.text()}`);
  }
  return (await res.json()).rows || [];
}

function ymd(d) {
  return d.toISOString().slice(0, 10);
}

function shape(rows, keyNames) {
  return rows.map((r) => {
    const o = {};
    keyNames.forEach((n, i) => { o[n] = r.keys[i]; });
    o.clicks = r.clicks;
    o.impressions = r.impressions;
    o.ctr = Number((r.ctr * 100).toFixed(2));
    o.position = Number(r.position.toFixed(1));
    return o;
  });
}

async function main() {
  const raw = process.env.GSC_SA_KEY;
  if (!raw) {
    console.error('Thiếu GSC_SA_KEY. Thêm nó vào GitHub Secrets của repo.');
    process.exit(1);
  }
  const sa = JSON.parse(raw);
  const token = await getAccessToken(sa);

  // Search Console trễ dữ liệu ~2 ngày.
  const end = new Date(Date.now() - 2 * 86400000);
  const start = new Date(end.getTime() - 27 * 86400000);
  const range = { startDate: ymd(start), endDate: ymd(end) };

  const [queries, pages, pageQuery] = await Promise.all([
    query(token, { ...range, dimensions: ['query'], rowLimit: 500 }),
    query(token, { ...range, dimensions: ['page'], rowLimit: 500 }),
    query(token, { ...range, dimensions: ['page', 'query'], rowLimit: 1000 }),
  ]);

  const data = {
    site: SITE,
    fetchedAt: new Date().toISOString(),
    range,
    totals: pages.reduce((a, r) => ({
      clicks: a.clicks + r.clicks,
      impressions: a.impressions + r.impressions,
    }), { clicks: 0, impressions: 0 }),
    queries: shape(queries, ['query']),
    pages: shape(pages, ['page']),
    pageQuery: shape(pageQuery, ['page', 'query']),
  };

  // Cơ hội: đang ở vị trí 5-20 — nhóm đẩy lên trang 1 rẻ nhất.
  // Ưu tiên cặp trang+truy vấn vì nó chỉ rõ phải sửa cái gì. Site còn ít
  // dữ liệu thì Google giấu gần hết cặp này, nên bù thêm bằng mức trang
  // để bảng không bị trống.
  const trongTam = (r) => r.position >= 5 && r.position <= 20;
  const theoCap = data.pageQuery.filter((r) => trongTam(r) && r.impressions >= 2);
  const daCo = new Set(theoCap.map((r) => r.page));
  const theoTrang = data.pages.filter((r) => trongTam(r) && r.impressions >= 2 && !daCo.has(r.page));
  data.opportunities = [...theoCap, ...theoTrang]
    .sort((a, b) => b.impressions - a.impressions)
    .slice(0, 40);

  // Bài Google chưa thấy. Trước đây đây là danh sách gõ tay rồi chép
  // nguyên sang file mới mỗi ngày, nên nó không bao giờ tự đúng lại:
  // tới 2026-11-02 vẫn còn liệt son-gel-han-quoc-chinh-hang và
  // nail-mat-meo-han-quoc là "chưa index", trong khi số liệu cùng file
  // cho thấy hai bài đó đã có hiển thị (vị trí 3 và 11) — tức là đã
  // được index từ lâu. Trang /admin/thong-ke vì vậy báo sai cho chủ tiệm.
  //
  // Nay tính thẳng từ số liệu: bài đã đăng quá 14 ngày mà suốt 28 ngày
  // không có một lần hiển thị nào.
  //
  // Sửa 2026-11-23: trước đây gộp tất cả vào một rổ và khuyên "thêm liên
  // kết nội bộ". Số liệu 20/11 cho thấy cách gộp đó sai: 8 trong 11 bài
  // tiếng Việt không hiện lại CÓ bản dịch EN/KO/ZH đang hiện bình thường
  // (nam-gioi-cham-soc-mong: bản Việt 0, bản Anh 13 hiển thị + 2 nhấp).
  // Bản dịch hiện được nghĩa là Google đã thu thập và lập chỉ mục bài đó
  // rồi — vấn đề không phải chỉ mục mà là bản tiếng Việt xếp sau đối thủ
  // trong kết quả tiếng Việt. Thêm liên kết nội bộ không chữa được việc
  // đó (đã thử 02/11, không nhích hạng nào). Nên tách hai nhóm ra, vì
  // chúng cần hai cách xử lý khác nhau.
  data.chuaIndex = await timBaiChuaThay(data.pages, range.endDate);

  await fs.mkdir(OUT_DIR, { recursive: true });
  await fs.writeFile(path.join(OUT_DIR, 'latest.json'), JSON.stringify(data, null, 2) + '\n');
  await fs.writeFile(path.join(OUT_DIR, `${range.endDate}.json`), JSON.stringify(data, null, 2) + '\n');

  const soMoc = await ghiLichSu();

  console.log(`Xong: ${data.totals.clicks} nhấp / ${data.totals.impressions} hiển thị`);
  console.log(`Lịch sử: ${soMoc} mốc trong data/gsc/lich-su.json`);
  console.log(`${data.queries.length} truy vấn, ${data.pages.length} trang, ${data.opportunities.length} cơ hội`);
}

/**
 * Bài đã đăng nhưng 28 ngày qua bản tiếng Việt không có lần hiển thị nào.
 *
 * Trả về cả tình trạng của ba bản dịch, vì đó là thứ phân biệt hai ca
 * hoàn toàn khác nhau:
 *   - banDichHien > 0  → Google đã lập chỉ mục bài này (bản dịch đang
 *     hiện), bản tiếng Việt chỉ đơn giản là xếp sau đối thủ Việt. Thêm
 *     liên kết nội bộ vô ích; muốn ăn thì phải viết hơn đối thủ.
 *   - banDichHien = 0  → cả bốn bản đều im, mới đáng nghi là chưa được
 *     thu thập.
 */
async function timBaiChuaThay(pages, ngayChot) {
  const hienThiTheoUrl = new Map(
    pages.map((r) => [r.page.replace(/\/+$/, '/'), r])
  );
  const coHienThi = (url) => (hienThiTheoUrl.get(url)?.impressions || 0) > 0;
  // Mốc 14 ngày tính theo ngày chốt số liệu, không phải hôm nay: bài đăng
  // sát ngày chốt thì chưa đủ dữ liệu để kết luận Google có thấy hay chưa.
  const hanMoi = new Date(ngayChot).getTime() - 14 * 86400000;
  const ra = [];

  let files;
  try {
    files = (await fs.readdir('content/posts')).filter((f) => f.endsWith('.json'));
  } catch {
    return ra; // chạy ngoài repo thì bỏ qua, thà trống còn hơn báo sai
  }

  for (const f of files.sort()) {
    let post;
    try {
      post = JSON.parse(await fs.readFile(path.join('content/posts', f), 'utf8'));
    } catch { continue; }
    if (post.status !== 'published' || !post.slug) continue;
    const dang = post.publishedAt ? new Date(post.publishedAt).getTime() : 0;
    if (!dang || dang > hanMoi) continue; // chưa đăng, hoặc đăng chưa đủ 14 ngày
    const url = `https://vessca.com/blog/${post.slug}/`;
    if (coHienThi(url)) continue;

    const banDich = {};
    let banDichHien = 0;
    for (const ma of ['en', 'ko', 'zh']) {
      const r = hienThiTheoUrl.get(`https://vessca.com/${ma}/blog/${post.slug}/`);
      const h = r?.impressions || 0;
      banDich[ma] = h;
      banDichHien += h;
    }
    ra.push({ url, slug: post.slug, title: post.title || post.slug, banDich, banDichHien });
  }
  return ra;
}

/**
 * Sổ tay nhấp/hiển thị theo từng bản đã chốt, để trang /admin/thong-ke vẽ
 * được đường đi lên hay đi ngang. Không có nó thì chủ tiệm chỉ thấy con số
 * của 28 ngày gần nhất và không cách nào biết tuần này hơn tuần trước hay
 * không — đúng chỗ dễ hiểu sai nhất.
 */
async function ghiLichSu() {
  const files = (await fs.readdir(OUT_DIR))
    .filter((f) => /^\d{4}-\d{2}-\d{2}\.json$/.test(f))
    .sort();
  const moc = [];
  for (const f of files) {
    try {
      const s = JSON.parse(await fs.readFile(path.join(OUT_DIR, f), 'utf8'));
      moc.push({
        ngay: f.replace('.json', ''),
        nhap: s.totals?.clicks ?? 0,
        hienThi: s.totals?.impressions ?? 0,
        soTrang: (s.pages || []).length,
      });
    } catch { /* bản lỗi thì bỏ qua, không làm sập cả lượt chạy */ }
  }
  await fs.writeFile(
    path.join(OUT_DIR, 'lich-su.json'),
    JSON.stringify({ dungLuc: new Date().toISOString(), moc }, null, 1) + '\n'
  );
  return moc.length;
}

// Chỉ chạy khi gọi thẳng file này. Có export để tools/gsc-tinh-lai.mjs
// dùng lại đúng hàm này mà không chép lại logic lần hai.
if (process.argv[1] && process.argv[1].endsWith('gsc-fetch.mjs')) {
  main().catch((err) => {
    console.error(err.message);
    process.exit(1);
  });
}

export { timBaiChuaThay, ghiLichSu, OUT_DIR };
