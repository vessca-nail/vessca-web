/**
 * ============================================================
 *  VIỆC CHẠY ĐỊNH KỲ — ẢNH CHO BÀI BLOG + ĐĂNG BÀI ĐÚNG GIỜ
 * ============================================================
 *  Cloudflare gọi hàm `chayDinhKy` mỗi ngày lúc 08:31, 09:31, 14:31, 20:31 (giờ VN).
 *
 *  1. ĐĂNG BÀI ĐÚNG GIỜ. Website là trang tĩnh: bài hẹn 20:30 chỉ hiện ra
 *     khi web được dựng lại. Trước đây việc dựng lại chỉ xảy ra khi có bài
 *     mới được thêm (khoảng 10 giờ sáng) → bài 20:30 trễ tới sáng hôm sau.
 *     Giờ tới giờ hẹn mà chưa dựng lại thì ghi một dòng vào kho GitHub để
 *     Cloudflare dựng lại.
 *
 *  2. ẢNH CHO BÀI. Bài nào có mục `anh` (do người viết bài điền) mà chưa
 *     làm thì tìm ảnh trên Pixabay (hoặc Pexels), TẢI VỀ và lưu ngay trong kho của web
 *     (content/media/blog/) — ảnh nằm trên vessca.com, không mượn link nhà
 *     khác, tốt cho SEO và không bao giờ chết link.
 *
 *     Mục `anh` trong bài:
 *       "anh": {
 *         "bia":      { "tim": "bride white nails manicure",
 *                       "alt": "Bộ nail trắng ngọc trai cho cô dâu" },
 *         "trong_bai": [ { "tim": "...", "alt": "..." } ]   // 0–2 ảnh
 *       }
 *     Trong nội dung, chỗ đặt ảnh trong bài đánh dấu <!--anh:1-->, <!--anh:2-->.
 *     Không đánh dấu thì ảnh tự đặt trước tiêu đề mục (h2) thứ 2 / thứ 4.
 *
 *  Giấy phép Pixabay/Pexels: dùng thương mại miễn phí, không bắt buộc ghi nguồn —
 *  vẫn ghi tên tác giả dưới ảnh cho đàng hoàng.
 *
 *  Cloudflare gói miễn phí cho tối đa 50 lần gọi ra ngoài mỗi lượt, nên
 *  mỗi lượt chỉ làm 1 bài (4 lượt/ngày > 2 bài viết mỗi ngày) và gộp tất cả
 *  vào MỘT lần ghi GitHub (một lần ghi = một lần dựng web).
 */

const API_GH = 'https://api.github.com';
const BAI_MOI_LUOT = 1;   // gói miễn phí giới hạn thời gian xử lý mỗi lượt
const DA_DUNG = 'content/media/blog/_da-dung.json';

const ghHeaders = (env) => ({
  Authorization: `Bearer ${env.GITHUB_TOKEN}`,
  Accept: 'application/vnd.github+json',
  'X-GitHub-Api-Version': '2022-11-28',
  'User-Agent': 'vessca-dinh-ky',
  'Content-Type': 'application/json',
});
const nhanh = (env) => env.GITHUB_BRANCH || 'main';

async function gh(env, path, init = {}) {
  const res = await fetch(`${API_GH}/repos/${env.GITHUB_REPO}${path}`, { ...init, headers: ghHeaders(env) });
  if (!res.ok) throw new Error(`GitHub ${init.method || 'GET'} ${path} → ${res.status}: ${(await res.text()).slice(0, 200)}`);
  return res.json();
}

function b64ToText(b64) {
  const bin = atob(b64.replace(/\s/g, ''));
  const bytes = new Uint8Array(bin.length);
  for (let i = 0; i < bin.length; i++) bytes[i] = bin.charCodeAt(i);
  return new TextDecoder().decode(bytes);
}
function bytesToB64(bytes) {
  let out = '';
  for (let i = 0; i < bytes.length; i += 0x8000) out += String.fromCharCode.apply(null, bytes.subarray(i, i + 0x8000));
  return btoa(out);
}
const textToB64 = (t) => bytesToB64(new TextEncoder().encode(t));

async function docFile(env, path) {
  const res = await fetch(`${API_GH}/repos/${env.GITHUB_REPO}/contents/${encodeURI(path)}?ref=${nhanh(env)}`, { headers: ghHeaders(env) });
  if (res.status === 404) return null;
  if (!res.ok) throw new Error(`GitHub đọc ${path} → ${res.status}`);
  return b64ToText((await res.json()).content || '');
}

/** Ghi nhiều file trong MỘT commit (Git Data API) */
async function ghiMotLan(env, files, message) {
  const ref = await gh(env, `/git/ref/heads/${nhanh(env)}`);
  const goc = await gh(env, `/git/commits/${ref.object.sha}`);
  const tree = [];
  for (const f of files) {
    const blob = await gh(env, '/git/blobs', { method: 'POST', body: JSON.stringify({ content: f.b64, encoding: 'base64' }) });
    tree.push({ path: f.path, mode: '100644', type: 'blob', sha: blob.sha });
  }
  const cay = await gh(env, '/git/trees', { method: 'POST', body: JSON.stringify({ base_tree: goc.tree.sha, tree }) });
  const ai = { name: 'VESSCA tự động', email: 'admin@vessca.com', date: new Date().toISOString() };
  const cm = await gh(env, '/git/commits', { method: 'POST', body: JSON.stringify({ message, tree: cay.sha, parents: [ref.object.sha], author: ai, committer: ai }) });
  await gh(env, `/git/refs/heads/${nhanh(env)}`, { method: 'PATCH', body: JSON.stringify({ sha: cm.sha }) });
  return cm.sha;
}

// ------------------------------------------------------------
//  Kho ảnh: Pixabay (đang dùng — Pexels tạm ngưng cấp khoá mới từ 10/2026),
//  Pexels nếu có khoá. Cả hai cho dùng thương mại miễn phí. Pixabay BẮT BUỘC
//  tải ảnh về máy chủ của mình, không được dùng link của họ lâu dài — đúng
//  cách hệ thống này làm.
//  Ảnh trả về dạng chung: { id, ten, link, nguon, tai(laBia) → URL tải }
// ------------------------------------------------------------
async function timPixabay(env, tuKhoa) {
  const url = `https://pixabay.com/api/?key=${encodeURIComponent(env.PIXABAY_API_KEY)}` +
    `&q=${encodeURIComponent(tuKhoa).slice(0, 100)}&image_type=photo&orientation=horizontal` +
    `&safesearch=true&min_width=1000&per_page=30`;
  // Pixabay báo 429 "gọi nhanh quá" khi hai lượt tìm sát nhau (dù tài liệu
  // nói 100 lượt/phút) → giãn mỗi lượt tìm ~1,5 giây, bị 429 thì chờ thêm
  // rồi thử lại tối đa 2 lần. Thời gian chờ không tính vào giới hạn CPU.
  await new Promise((r) => setTimeout(r, 1500));
  let res = await fetch(url);
  for (let lan = 0; res.status === 429 && lan < 2; lan++) {
    await new Promise((r) => setTimeout(r, 4000 * (lan + 1)));
    res = await fetch(url);
  }
  if (!res.ok) {
    const h = (k) => res.headers.get(k);
    throw new Error(`Pixabay tìm "${tuKhoa}" → ${res.status} (còn ${h('x-ratelimit-remaining')}/${h('x-ratelimit-limit')}, ` +
      `mở lại sau ${h('x-ratelimit-reset')}s; ${(await res.text()).slice(0, 80)})`);
  }
  const hits = ((await res.json()).hits || []).map((h) => ({
    id: `pb-${h.id}`, ten: h.user, link: h.pageURL, nguon: 'Pixabay',
    nhan: String(h.tags || '').toLowerCase(),
    // Ưu tiên máy chủ ảnh cdn.pixabay.com (bản 1280px, cùng ảnh với
    // largeImageURL); đường pixabay.com/get hay báo 429 khi tải từ Cloudflare.
    tai: () => [String(h.webformatURL || '').replace(/_640\.(jpe?g|png)$/i, '_1280.$1'), h.largeImageURL]
      .filter((u) => u && /^https:/.test(u)),
  }));
  return locTheoNhan(tuKhoa, hits);
}

/* Pixabay xếp theo độ phổ biến nên hay trả ảnh lạc đề (tìm "damaged peeling
   nails" ra mặt người nứt nẻ). Lọc theo NHÃN của ảnh:
   - từ khoá có chữ chủ đề (nail, manicure, polish, gel…) thì ảnh BẮT BUỘC có
     nhãn chứa ít nhất một chữ chủ đề;
   - còn lại xếp theo số từ khoá trùng với nhãn, nhiều trước. */
const CHU_DE = ['nail', 'manicure', 'pedicure', 'polish', 'gel', 'cuticle', 'acrylic'];
function locTheoNhan(tuKhoa, hits) {
  const tu = tuKhoa.toLowerCase().split(/\s+/).filter((w) => w.length > 2);
  const can = CHU_DE.filter((c) => tu.some((w) => w.startsWith(c)));
  const diem = (h) => tu.filter((w) => h.nhan.includes(w.replace(/s$/, ''))).length;
  return hits
    .filter((h) => !can.length || can.some((c) => h.nhan.includes(c)))
    .map((h, i) => ({ h, d: diem(h), i }))
    .sort((a, b) => b.d - a.d || a.i - b.i)
    .map((x) => x.h);
}

async function timPexels(env, tuKhoa) {
  const url = `https://api.pexels.com/v1/search?query=${encodeURIComponent(tuKhoa)}&orientation=landscape&per_page=20`;
  const res = await fetch(url, { headers: { Authorization: env.PEXELS_API_KEY } });
  if (!res.ok) throw new Error(`Pexels tìm "${tuKhoa}" → ${res.status}`);
  return ((await res.json()).photos || []).map((p) => ({
    id: `px-${p.id}`, ten: p.photographer, link: p.url, nguon: 'Pexels',
    // Pexels tự cắt + nén: bìa 16:9 đúng khung 1000×563 của trang bài
    tai: (laBia) => `${p.src.original}?auto=compress&cs=tinysrgb&fm=jpg&q=72&` +
      (laBia ? 'w=1200&h=675&fit=crop' : 'w=1000'),
  }));
}

const coKho = (env) => !!(env.PIXABAY_API_KEY || env.PEXELS_API_KEY);

async function timAnh(env, tuKhoa, daDung) {
  const kq = env.PIXABAY_API_KEY ? await timPixabay(env, tuKhoa) : await timPexels(env, tuKhoa);
  // Không lặp ảnh, và mỗi người chụp chỉ dùng MỘT lần trên toàn blog: Pixabay
  // có nhiều tấm của cùng một buổi chụp, khác id nhưng nhìn gần như y hệt.
  return kq.find((p) => !daDung.has(p.id) && !daDung.has(`u:${p.ten}`)) || null;
}

async function taiAnh(photo, laBia) {
  const urls = [].concat(photo.tai(laBia));
  let res = null;
  for (const u of urls) {
    for (let lan = 0; lan < 3; lan++) {
      res = await fetch(u, { headers: { 'User-Agent': 'Mozilla/5.0 (vessca.com blog)' } });
      if (res.status !== 429) break;
      await new Promise((r) => setTimeout(r, 3000 * (lan + 1)));
    }
    if (res.ok && (res.headers.get('content-type') || '').startsWith('image/')) break;
  }
  if (!res || !res.ok) throw new Error(`Tải ảnh ${photo.id} → ${res ? res.status : 'không gọi được'}`);
  const bytes = new Uint8Array(await res.arrayBuffer());
  if (bytes.length > 900_000) throw new Error(`Ảnh ${photo.id} nặng quá (${bytes.length} byte)`);
  return bytes;
}

const escAttr = (s) => String(s || '').replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;');

const CHU_ANH = { vi: 'Ảnh', en: 'Photo', ko: '사진', zh: '图片' };

function hinhTrongBai(src, alt, photo, lang = 'vi') {
  return `<figure><img src="${src}" alt="${escAttr(alt)}" width="1000" loading="lazy" />` +
    `<figcaption>${escAttr(alt)} · ${CHU_ANH[lang] || 'Photo'}: <a href="${escAttr(photo.link)}">${escAttr(photo.ten)} / ${photo.nguon}</a></figcaption></figure>`;
}

/** Đặt ảnh thứ i vào nội dung: chỗ đánh dấu <!--anh:i-->, không có thì trước h2 thứ (2i) */
function chenAnh(html, i, figure) {
  const dau = `<!--anh:${i}-->`;
  if (html.includes(dau)) return html.replace(dau, figure);
  const viTri = [];
  const re = /<h2[\s>]/gi;
  let m;
  while ((m = re.exec(html))) viTri.push(m.index);
  const k = Math.min(viTri.length - 1, i * 2 - 1);
  if (k < 1) return html + figure;
  return html.slice(0, viTri[k]) + figure + html.slice(viTri[k]);
}

async function lamAnhChoBai(env, file, daDung, bao) {
  const duongDan = `content/posts/${file}`;
  const raw = await docFile(env, duongDan);
  if (!raw) return null;
  const post = JSON.parse(raw);
  if (!post.anh || post.anh.xong) return null;

  // Làm lại bài đã có ảnh: gỡ ảnh trong bài cũ, trả lại chỗ đánh dấu để
  // ảnh mới vào đúng vị trí cũ (tên file giữ nguyên, ghi đè).
  const goAnh = (html) => String(html || '').replace(
    new RegExp(`<figure><img src="/media/blog/${post.slug}-(\\d)\\.jpg"[\\s\\S]*?</figure>`, 'g'),
    (_, n) => `<!--anh:${n}-->`);
  post.content = goAnh(post.content);
  const banDich = post.i18n && typeof post.i18n === 'object' ? Object.entries(post.i18n) : [];
  for (const [, t] of banDich) if (t && t.content) t.content = goAnh(t.content);

  const files = [];
  const bia = post.anh.bia;
  if (bia && bia.tim) {
    const p = await timAnh(env, bia.tim, daDung);
    if (p) {
      const bytes = await taiAnh(p, true);
      const path = `content/media/blog/${post.slug}.jpg`;
      files.push({ path, b64: bytesToB64(bytes) });
      daDung.add(p.id); daDung.add(`u:${p.ten}`);
      post.coverImage = `/media/blog/${post.slug}.jpg`;
      post.coverAlt = bia.alt || post.coverAlt || post.title;
      if (bia.altI18n) for (const [lang, t] of banDich) if (t && bia.altI18n[lang]) t.coverAlt = bia.altI18n[lang];
      post.coverCredit = { ten: p.ten, link: p.link, nguon: p.nguon, id: p.id };
    } else bao.push(`${post.slug}: không tìm được ảnh bìa cho "${bia.tim}"`);
  }

  const trong = Array.isArray(post.anh.trong_bai) ? post.anh.trong_bai.slice(0, 2) : [];
  for (let i = 0; i < trong.length; i++) {
    const a = trong[i];
    if (!a || !a.tim) continue;
    const p = await timAnh(env, a.tim, daDung);
    if (!p) { bao.push(`${post.slug}: không tìm được ảnh "${a.tim}"`); continue; }
    const bytes = await taiAnh(p, false);
    const ten = `${post.slug}-${i + 1}.jpg`;
    files.push({ path: `content/media/blog/${ten}`, b64: bytesToB64(bytes) });
    daDung.add(p.id); daDung.add(`u:${p.ten}`);
    post.content = chenAnh(post.content || '', i + 1, hinhTrongBai(`/media/blog/${ten}`, a.alt || post.title, p));
    // Bản dịch: dùng alt theo ngôn ngữ (a.altI18n.en …), không có thì lấy tiêu đề bản dịch
    for (const [lang, t] of banDich) {
      if (!t || !t.content) continue;
      const alt = (a.altI18n && a.altI18n[lang]) || t.coverAlt || t.title;
      t.content = chenAnh(t.content, i + 1, hinhTrongBai(`/media/blog/${ten}`, alt, p, lang));
    }
  }

  post.anh.xong = new Date().toISOString();
  files.push({ path: duongDan, b64: textToB64(JSON.stringify(post, null, 2) + '\n') });
  bao.push(`${post.slug}: ${files.length - 1} ảnh`);
  return files;
}

// ------------------------------------------------------------
//  Lượt chạy
// ------------------------------------------------------------
export async function chayDinhKy(env, { ep = false } = {}) {
  const bao = [];
  const res = await env.ASSETS.fetch(new Request('https://vessca.com/_noi-bo/bai-viet.json'));
  const so = res.ok ? await res.json() : { henGio: [], canAnh: [], dungLuc: null };
  const files = [];

  // 1) Ảnh
  if (coKho(env) && so.canAnh?.length) {
    const daDungRaw = await docFile(env, DA_DUNG);
    const daDung = new Set(daDungRaw ? JSON.parse(daDungRaw) : []);
    // Sổ nội bộ chỉ mới lại sau khi web dựng xong — bài vừa làm ở lượt trước
    // có thể vẫn nằm trong danh sách. Bài nào đã xong thì bỏ qua, xét tối đa 4 bài.
    let lam = 0;
    for (const b of so.canAnh.slice(0, 4)) {
      if (lam >= BAI_MOI_LUOT) break;
      try {
        const f = await lamAnhChoBai(env, b.file, daDung, bao);
        if (f) { files.push(...f); lam++; }
      } catch (e) {
        bao.push(`${b.slug}: lỗi — ${e.message}`);
        break;
      }
    }
    if (files.length) files.push({ path: DA_DUNG, b64: textToB64(JSON.stringify([...daDung]) + '\n') });
  } else if (!coKho(env) && so.canAnh?.length) {
    bao.push(`Chưa có PIXABAY_API_KEY — ${so.canAnh.length} bài đang chờ ảnh`);
  }

  // 2) Bài tới giờ đăng mà web chưa dựng lại
  const now = Date.now();
  const toiGio = (so.henGio || []).filter((h) => new Date(h.at).getTime() <= now);
  if (toiGio.length) bao.push(`Tới giờ đăng: ${toiGio.map((h) => h.slug).join(', ')}`);

  if (!files.length && !toiGio.length && !ep) return { ghi: false, bao };

  if (!files.length) {
    files.push({ path: 'content/.lan-dung-cuoi', b64: textToB64(new Date().toISOString() + '\n') });
  }
  const tin = files.some((f) => f.path.endsWith('.jpg'))
    ? `Thêm ảnh cho bài blog${toiGio.length ? ' + đăng bài tới giờ' : ''}\n\n${bao.join('\n')}`
    : `Dựng lại web: đăng bài tới giờ\n\n${bao.join('\n')}`;
  const sha = await ghiMotLan(env, files, tin);
  return { ghi: true, sha, bao };
}
