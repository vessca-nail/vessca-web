#!/usr/bin/env node
/**
 * ============================================================
 *  LẤY ẢNH THẬT TỪ INSTAGRAM VỀ KHO CỦA WEB
 * ============================================================
 *  Vì sao cần: web đang dùng ảnh kho Pixabay. Ảnh kho có hàng nghìn
 *  trang khác dùng cùng tấm đó, nên gần như không có cơ hội lên Google
 *  Hình ảnh. Ảnh tay tiệm tự làm là ảnh độc nhất — đó mới là ảnh có giá.
 *
 *  Đường chính thức: Instagram API with Instagram Login.
 *  Tài khoản của chính mình thì Meta chỉ cần Standard Access —
 *  KHÔNG cần App Review, KHÔNG cần Business Verification, KHÔNG cần
 *  liên kết Facebook Page. Yêu cầu duy nhất: IG phải là tài khoản
 *  Professional (Business hoặc Creator).
 *
 *  CHẠY:
 *    export IG_ACCESS_TOKEN='...'                 # KHÔNG bao giờ ghi vào repo (repo public)
 *    node tools/anh-social/lay-anh-instagram.mjs           # chạy thử, không ghi gì
 *    node tools/anh-social/lay-anh-instagram.mjs --ghi     # tải ảnh về thật
 *    node tools/anh-social/lay-anh-instagram.mjs --ghi --so=5
 *
 *  Ảnh lưu ở content/media/instagram/, danh mục ở _index.json.
 *  Ảnh đã lấy rồi thì lần sau bỏ qua (theo id của Instagram).
 *
 *  LƯU Ý media_url: Meta gọi đây là CDN "privacy-aware" và KHÔNG cam kết
 *  thời hạn — nên bắt buộc tải về tự lưu, không được dán link thẳng vào web.
 */

import { writeFile, readFile, mkdir } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import path from 'node:path';

const API = 'https://graph.instagram.com/v26.0';
const THU_MUC = 'content/media/instagram';
const DANH_MUC = `${THU_MUC}/_index.json`;

const args = process.argv.slice(2);
const GHI = args.includes('--ghi');
const SO_TOI_DA = Number((args.find((a) => a.startsWith('--so=')) || '').split('=')[1]) || 12;

const token = process.env.IG_ACCESS_TOKEN;
if (!token) {
  console.error(`
Chưa có IG_ACCESS_TOKEN.

Cách lấy (làm một lần, khoảng 15 phút):
  1. Instagram > Settings > Account type  →  chuyển sang Professional
     (Business hoặc Creator). API không đọc được tài khoản cá nhân.
  2. developers.facebook.com  →  Create App  →  thêm sản phẩm "Instagram"
     →  "API setup with Instagram login"  →  Add account  →  Generate token
  3. Token vừa hiện ra là long-lived, hạn 60 ngày.

KHÔNG dán token vào bất kỳ file nào trong repo — repo này là public.
Chạy:  export IG_ACCESS_TOKEN='token-vua-lay'
`);
  process.exit(1);
}

/** Gọi API, báo lỗi rõ ràng thay vì để JSON.parse chết không hiểu vì sao */
async function goi(url) {
  const res = await fetch(url);
  const text = await res.text();
  let data;
  try { data = JSON.parse(text); } catch { throw new Error(`API trả về không phải JSON (${res.status}): ${text.slice(0, 200)}`); }
  if (!res.ok || data.error) {
    const e = data.error || {};
    throw new Error(`API lỗi ${res.status}: ${e.message || text.slice(0, 200)}${e.code ? ` (code ${e.code})` : ''}`);
  }
  return data;
}

/** Lấy danh sách bài, đi hết các trang (cursor) */
async function layDanhSach() {
  const fields = [
    'id', 'caption', 'media_type', 'media_url', 'permalink', 'timestamp',
    'thumbnail_url',
    'children{id,media_type,media_url,thumbnail_url}',
  ].join(',');
  let url = `${API}/me/media?fields=${fields}&limit=50&access_token=${encodeURIComponent(token)}`;
  const tatCa = [];
  for (let trang = 0; trang < 20 && url; trang++) {
    const d = await goi(url);
    tatCa.push(...(d.data || []));
    url = d.paging?.next || null;
  }
  return tatCa;
}

/**
 * Mở bài thành danh sách ảnh đơn.
 *
 *  IMAGE           → tải media_url (ảnh gốc)
 *  CAROUSEL_ALBUM  → tải từng ảnh con; con là video thì lấy ảnh bìa
 *  VIDEO / REELS   → lấy thumbnail_url (ẢNH BÌA), không tải file video.
 *
 *  Vì sao không tải video: Meta bỏ trống media_url với video dùng nhạc có
 *  bản quyền (reels nail gần như luôn gắn nhạc trending), nên phần lớn tải
 *  không được. Và nhạc đó được cấp phép để phát TRÊN Instagram — mang về
 *  host trên web thương mại của tiệm là chuyện khác. Thêm nữa file video
 *  nặng, commit vào git sẽ phình kho rất nhanh.
 *  Cách làm: lưu ảnh bìa trên vessca.com (có giá SEO), video phát bằng
 *  link về Instagram — đúng chỗ nhạc được cấp phép, và kéo thêm người theo dõi.
 */
function tachAnh(bai) {
  const ra = [];
  const chung = { permalink: bai.permalink, timestamp: bai.timestamp, caption: bai.caption || '' };
  const loai = bai.media_type;

  if (loai === 'IMAGE' && bai.media_url) {
    ra.push({ id: bai.id, url: bai.media_url, kieu: 'anh', ...chung });

  } else if (loai === 'VIDEO') {
    // Reels / video: chỉ ảnh bìa. Không có bìa thì bỏ hẳn.
    if (bai.thumbnail_url) ra.push({ id: bai.id, url: bai.thumbnail_url, kieu: 'reel', ...chung });

  } else if (loai === 'CAROUSEL_ALBUM' && Array.isArray(bai.children?.data)) {
    for (const con of bai.children.data) {
      if (con.media_type === 'IMAGE' && con.media_url) {
        ra.push({ id: con.id, url: con.media_url, kieu: 'anh', ...chung });
      } else if (con.media_type === 'VIDEO' && con.thumbnail_url) {
        ra.push({ id: con.id, url: con.thumbnail_url, kieu: 'reel', ...chung });
      }
    }
  }
  return ra;
}

/** Tên file từ ngày đăng + id, để thư mục tự sắp theo thời gian */
function tenFile(anh) {
  const ngay = (anh.timestamp || '').slice(0, 10) || 'khong-ro';
  return `${ngay}-${String(anh.id).slice(-10)}.jpg`;
}

async function docDanhMuc() {
  if (!existsSync(DANH_MUC)) return { anh: [] };
  try { return JSON.parse(await readFile(DANH_MUC, 'utf8')); }
  catch { return { anh: [] }; }
}

const main = async () => {
  console.log(GHI ? '▸ Chế độ GHI — sẽ tải ảnh về\n' : '▸ Chế độ chạy thử — không ghi gì. Thêm --ghi để tải thật\n');

  const danhMuc = await docDanhMuc();
  const daCo = new Set((danhMuc.anh || []).map((a) => a.id));

  const bai = await layDanhSach();
  const anhTatCa = bai.flatMap(tachAnh);
  const moi = anhTatCa.filter((a) => !daCo.has(a.id));

  console.log(`Instagram  : ${bai.length} bài`);
  const soAnh = anhTatCa.filter((a) => a.kieu === 'anh').length;
  const soReel = anhTatCa.length - soAnh;
  console.log(`Lấy được   : ${anhTatCa.length} tấm — ${soAnh} ảnh, ${soReel} ảnh bìa reels`);
  console.log(`Đã có      : ${anhTatCa.length - moi.length}`);
  console.log(`Ảnh mới    : ${moi.length}${moi.length > SO_TOI_DA ? ` → lấy ${SO_TOI_DA} lượt này` : ''}\n`);

  const can = moi.slice(0, SO_TOI_DA);
  if (!can.length) { console.log('Không có ảnh mới. Xong.'); return; }

  if (!GHI) {
    for (const a of can) {
      const cap = (a.caption || '').replace(/\s+/g, ' ').slice(0, 70);
      console.log(`  [${a.kieu === 'reel' ? 'reel' : 'ảnh '}] ${tenFile(a)}  ${cap ? `“${cap}…”` : '(không có chú thích)'}`);
    }
    console.log('\nChạy lại với --ghi để tải về.');
    return;
  }

  await mkdir(THU_MUC, { recursive: true });
  const themVao = [];
  for (const a of can) {
    const ten = tenFile(a);
    const dich = path.join(THU_MUC, ten);
    try {
      const res = await fetch(a.url);
      if (!res.ok) { console.log(`  BỎ  ${ten} — tải lỗi ${res.status}`); continue; }
      const buf = Buffer.from(await res.arrayBuffer());
      if (buf.length < 5000) { console.log(`  BỎ  ${ten} — file quá nhỏ (${buf.length} byte), nghi lỗi`); continue; }
      await writeFile(dich, buf);
      themVao.push({
        id: a.id,
        file: `/media/instagram/${ten}`,
        kieu: a.kieu,                 // 'anh' = ảnh tự lưu | 'reel' = ảnh bìa, video phát trên IG
        permalink: a.permalink,
        timestamp: a.timestamp,
        caption: (a.caption || '').trim(),
        alt: '',                 // điền sau: alt tiếng Việt là phần mang giá trị SEO
        kb: Math.round(buf.length / 1024),
      });
      console.log(`  ok  ${ten}  ${Math.round(buf.length / 1024)} KB`);
    } catch (e) {
      console.log(`  BỎ  ${ten} — ${e.message}`);
    }
  }

  if (!themVao.length) { console.log('\nKhông tải được ảnh nào.'); return; }

  danhMuc.anh = [...themVao, ...(danhMuc.anh || [])]
    .sort((a, b) => String(b.timestamp).localeCompare(String(a.timestamp)));
  danhMuc.capNhat = new Date().toISOString();
  await writeFile(DANH_MUC, JSON.stringify(danhMuc, null, 2) + '\n');

  console.log(`\n✓ Thêm ${themVao.length} ảnh. Tổng trong kho: ${danhMuc.anh.length}`);
  console.log('  Còn thiếu: alt tiếng Việt cho từng ảnh (chạy bước viết alt).');
};

main().catch((e) => { console.error('\nLỗi:', e.message); process.exit(1); });
