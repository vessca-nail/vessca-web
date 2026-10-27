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

  // Danh sách bài Google chưa lập chỉ mục phải lấy tay trong Search Console
  // (API kiểm tra URL bị giới hạn quota nặng), nên giữ lại giá trị cũ.
  try {
    const cu = JSON.parse(await fs.readFile(path.join(OUT_DIR, 'latest.json'), 'utf8'));
    if (cu.chuaIndex) data.chuaIndex = cu.chuaIndex;
  } catch { /* lần chạy đầu chưa có file */ }

  await fs.mkdir(OUT_DIR, { recursive: true });
  await fs.writeFile(path.join(OUT_DIR, 'latest.json'), JSON.stringify(data, null, 2) + '\n');
  await fs.writeFile(path.join(OUT_DIR, `${range.endDate}.json`), JSON.stringify(data, null, 2) + '\n');

  console.log(`Xong: ${data.totals.clicks} nhấp / ${data.totals.impressions} hiển thị`);
  console.log(`${data.queries.length} truy vấn, ${data.pages.length} trang, ${data.opportunities.length} cơ hội`);
}

main().catch((err) => {
  console.error(err.message);
  process.exit(1);
});
