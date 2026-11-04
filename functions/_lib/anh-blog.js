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
// Đợt 33: 2 bài/lượt (8 bài/ngày) để rút hàng chờ 48 bài đang đọng trong ~6
// ngày. Sổ tạm boNho đã cắt phần lớn lượt gọi lặp nên vẫn dưới mức 50 lượt
// gọi ra ngoài mỗi lượt của gói miễn phí: mỗi bài chừng 3 lượt tìm + 3 lượt
// tải + 1 lượt đọc GitHub.
const BAI_MOI_LUOT = 2;
const LOI_TOI_DA = 3;     // quá số này thì dừng lượt, để lượt sau chạy tiếp
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
//  Kho ảnh: thử lần lượt Unsplash → Pexels → Pixabay → Openverse (xem cacKho),
//  kho nào có khoá và không lỗi thì dùng. Openverse không cần khoá nên luôn có
//  mặt làm lưới cuối. Khi mọi kho đều không ra ảnh thì trang web lùi về ảnh
//  thương hiệu của tiệm (anhBia trong lib/render.mjs), bài vẫn hiện bình thường.
//  Cả hai cho dùng thương mại miễn phí. Pixabay BẮT BUỘC
//  tải ảnh về máy chủ của mình, không được dùng link của họ lâu dài — đúng
//  cách hệ thống này làm.
//  Ảnh trả về dạng chung: { id, ten, link, nguon, tai(laBia) → URL tải }
// ------------------------------------------------------------
async function timPixabay(env, tuKhoa) {
  const url = `https://pixabay.com/api/?key=${encodeURIComponent(env.PIXABAY_API_KEY)}` +
    `&q=${encodeURIComponent(tuKhoa).slice(0, 100)}&image_type=photo&orientation=horizontal` +
    `&safesearch=true&min_width=1000&per_page=100`;
  // Pixabay báo 429 "gọi nhanh quá" khi hai lượt tìm sát nhau (dù tài liệu
  // nói 100 lượt/phút) → giãn mỗi lượt tìm ~1,5 giây, bị 429 thì chờ thêm
  // rồi thử lại tối đa 2 lần. Thời gian chờ không tính vào giới hạn CPU.
  await new Promise((r) => setTimeout(r, 1500));
  let res = await fetch(url);
  // Đợt 33: còn 1 lần thử lại (trước là 2, chờ 4s rồi 8s). Khi Pixabay chặn
  // dài ngày thì chờ thêm không giúp gì, chỉ ăn hết thời gian của lượt chạy;
  // chặn thật thì khoHong lo phần còn lại.
  if (res.status === 429) {
    await new Promise((r) => setTimeout(r, 3000));
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
    tai: () => [String(h.webformatURL || '').replace(/_640\.(jpe?g|png)$/i, '_1280.$1'), h.largeImageURL, h.webformatURL]
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
/* Đợt 32 (26/10): chữ "nail(s)" trong tiếng Anh còn là ĐINH đóng gỗ và MÓNG
   của chó mèo → từng ra búa, cờ lê, đinh rỉ, chó. Nên khi tìm ảnh nail, nhãn
   ảnh phải có ít nhất một chữ THẬT SỰ về làm móng, và không được có chữ nào
   trong danh sách cấm. */
const LAM_MONG = ['manicure', 'pedicure', 'nail polish', 'nail art', 'nail design', 'nail salon',
  'gel polish', 'gel nails', 'fingernail', 'nail varnish', 'nail care', 'varnish', 'lacquer'];
const LAM_MONG_CU = ['manicure', 'pedicure', 'nail polish', 'nail art', 'nail design', 'nail salon',
  'varnish', 'lacquer', 'fingernail', 'nail care', 'gel nails', 'nail varnish', 'polish', 'cosmetic', 'beauty'];
const CAM = ['landscape', 'meadow', 'park', 'tree', 'tattoo', 'sketch', 'drawing', 'illustration',
  'abstract', 'pattern', 'book', 'reading', 'glitch', 'hammer', 'wrench', 'screw', 'rust', 'iron', 'hardware', 'carpentry', 'construction', 'workshop',
  'pet', 'dog', 'cat ', 'puppy', 'animal', 'grooming', 'claw', 'paw', 'fruit', 'berr', 'apple', 'food',
  'keyboard', 'laptop', 'computer', 'office', 'horror', 'fantasy', 'zombie', 'skull', 'wood', 'nails tool'];
function locTheoNhan(tuKhoa, hits) {
  const tu = tuKhoa.toLowerCase().split(/\s+/).filter((w) => w.length > 2);
  const can = CHU_DE.filter((c) => tu.some((w) => w.startsWith(c)));
  const diem = (h) => tu.filter((w) => h.nhan.includes(w.replace(/s$/, ''))).length;
  return hits
    // Không có nhãn (Pexels đôi khi để trống alt) thì bỏ hai bước lọc chủ đề:
    // Pexels xếp theo độ khớp từ khoá, không theo độ phổ biến như Pixabay,
    // nên không cần nhãn để chặn ảnh lạc đề. Danh sách CẤM vẫn áp dụng.
    .filter((h) => !h.nhan || !can.length || can.some((c) => h.nhan.includes(c)))
    .filter((h) => !h.nhan || !can.length || LAM_MONG.some((c) => h.nhan.includes(c)))
    .filter((h) => !CAM.some((c) => (h.nhan + ' ').includes(c)))
    .map((h, i) => ({ h, d: diem(h), i }))
    .sort((a, b) => b.d - a.d || a.i - b.i)
    .map((x) => x.h);
}

async function timPexels(env, tuKhoa) {
  const url = `https://api.pexels.com/v1/search?query=${encodeURIComponent(tuKhoa)}&orientation=landscape&per_page=20`;
  const res = await fetch(url, { headers: { Authorization: env.PEXELS_API_KEY } });
  if (!res.ok) throw new Error(`Pexels tìm "${tuKhoa}" → ${res.status}`);
  const hits = ((await res.json()).photos || []).map((p) => ({
    id: `px-${p.id}`, ten: p.photographer, link: p.url, nguon: 'Pexels',
    // Pexels có mô tả ảnh ở `alt` → dùng làm nhãn để lọc như Pixabay.
    // Ảnh nào Pexels để trống alt thì locTheoNhan bỏ qua bước lọc chủ đề.
    nhan: String(p.alt || '').toLowerCase(),
    // Pexels tự cắt + nén: bìa 16:9 đúng khung 1000×563 của trang bài
    tai: (laBia) => `${p.src.original}?auto=compress&cs=tinysrgb&fm=jpg&q=72&` +
      (laBia ? 'w=1200&h=675&fit=crop' : 'w=1000'),
  }));
  return locTheoNhan(tuKhoa, hits);
}

/* Đợt 33b: thêm Unsplash và Openverse. Trước đây code chỉ biết Pixabay và
   Pexels — Pixabay bị chặn, Pexels ngưng cấp khoá mới, thế là hết đường.
   Kho ảnh miễn phí cho dùng thương mại còn nhiều, nên xếp thành một dãy để
   sau này thêm kho chỉ là viết một hàm nữa rồi khai vào cacKho().

   LƯU Ý: hai hàm dưới viết theo tài liệu API, CHƯA gọi thử được vào API
   thật (môi trường chạy thử của phiên này bị chặn ra ngoài). Nếu dạng dữ
   liệu trả về khác, kho đó sẽ lỗi và bị khoHong loại trong lượt đầu — các
   kho còn lại vẫn chạy, bài vẫn có ảnh thương hiệu, không hỏng gì. Lượt cron
   đầu tiên sẽ ghi rõ lỗi vào thân commit nếu có. */

async function timUnsplash(env, tuKhoa) {
  const url = `https://api.unsplash.com/search/photos?query=${encodeURIComponent(tuKhoa)}` +
    '&per_page=30&orientation=landscape&content_filter=high';
  const res = await fetch(url, {
    headers: { Authorization: `Client-ID ${env.UNSPLASH_ACCESS_KEY}`, 'Accept-Version': 'v1' },
  });
  if (!res.ok) throw new Error(`Unsplash tìm "${tuKhoa}" → ${res.status}`);
  const hits = ((await res.json()).results || []).map((p) => ({
    id: `us-${p.id}`, ten: p.user?.name || 'Unsplash', link: p.links?.html || '', nguon: 'Unsplash',
    // Nhãn: mô tả ảnh + các thẻ, gộp lại cho locTheoNhan lọc chủ đề
    nhan: [p.alt_description, p.description, ...(p.tags || []).map((t) => t.title)]
      .filter(Boolean).join(' ').toLowerCase(),
    // urls.raw nhận tham số cắt/nén của Imgix → bìa 16:9 đúng khung 1000×563
    tai: (laBia) => `${p.urls?.raw}&fm=jpg&q=72&` + (laBia ? 'w=1200&h=675&fit=crop' : 'w=1000'),
    // Điều khoản API Unsplash buộc gọi download_location mỗi lần dùng ảnh.
    // Lỗi ở bước này không được làm hỏng việc lấy ảnh → bọc try trong taiAnh.
    sauKhiTai: p.links?.download_location
      ? () => fetch(p.links.download_location, { headers: { Authorization: `Client-ID ${env.UNSPLASH_ACCESS_KEY}` } })
      : null,
  }));
  return locTheoNhan(tuKhoa, hits);
}

/* Openverse (của Creative Commons) — KHÔNG CẦN KHOÁ. Đây là lưới cuối: dù
   chủ tiệm chưa đăng ký khoá nào thì vẫn có ảnh. Lọc license=cc0,pdm tức
   chỉ lấy ảnh thuộc phạm vi công cộng / miễn trừ bản quyền, dùng thương mại
   không ràng buộc ghi nguồn — vẫn ghi tên người chụp cho đàng hoàng.
   Hạn mức khi gọi không khoá khá thấp nên xếp cuối dãy. */
async function timOpenverse(env, tuKhoa) {
  const url = `https://api.openverse.org/v1/images/?q=${encodeURIComponent(tuKhoa)}` +
    '&page_size=20&license=cc0,pdm&mature=false';
  const res = await fetch(url, { headers: { 'User-Agent': 'vessca.com blog (lamiesnail@gmail.com)' } });
  if (!res.ok) throw new Error(`Openverse tìm "${tuKhoa}" → ${res.status}`);
  /* Đợt 33c — lần chạy thật đầu tiên (04/11, bài nail-mau-dam-cuoi-nam) cho
     thấy Openverse khác Pixabay ở chỗ nhãn rất nghèo (thường chỉ "manicure")
     nên bộ lọc chủ đề cũ để lọt: ảnh cái bát thuỷ tinh 240×180 gắn alt "nail
     xanh navy", ảnh ghép hướng dẫn tự làm gắn alt "nail đen bóng". Đã dọn
     bài và siết ba lớp:
     1) Đủ lớn: cạnh dài tối thiểu 1000px (nếu API báo kích thước).
     2) Không phải ảnh ghép/hướng dẫn: cấm collage, tutorial, diy, how to…
     3) ĐÚNG Ý TỪ KHOÁ: từ khoá tìm có chữ riêng (màu, kiểu: "navy", "black",
        "french"…) thì tiêu đề hoặc nhãn ảnh PHẢI chứa ít nhất một chữ đó.
        Không đạt thì thà không có ảnh (bài lùi về ảnh thương hiệu của tiệm)
        còn hơn một ảnh sai gắn alt sai — alt sai là lỗi SEO và lừa người đọc. */
  const CHUNG = new Set(['nail', 'nails', 'manicure', 'pedicure', 'polish', 'gel', 'hands', 'hand', 'art',
    'design', 'close', 'closeup', 'salon', 'fingernail', 'fingernails', 'beauty', 'photo']);
  const rieng = String(tuKhoa).toLowerCase().split(/\s+/).filter((w) => w.length > 2 && !CHUNG.has(w));
  const BO = ['collage', 'tutorial', 'diy', 'how to', 'step by step', 'before and after', 'infographic', 'logo', 'icon', 'drawing', 'clipart'];
  const hits = ((await res.json()).results || [])
    .map((p) => ({
      id: `ov-${p.id}`, ten: p.creator || 'Openverse', link: p.foreign_landing_url || p.url || '',
      nguon: 'Openverse', rong: Number(p.width) || 0, cao: Number(p.height) || 0,
      nhan: [p.title, ...(p.tags || []).map((t) => t.name)].filter(Boolean).join(' ').toLowerCase(),
      // Openverse trả link ảnh gốc, không có tham số cắt → lấy nguyên, thử cả
      // ảnh nhỏ nếu bản gốc quá nặng (taiAnh tự lùi khi > 900KB)
      tai: () => [p.url, p.thumbnail].filter(Boolean),
    }))
    .filter((h) => !(h.rong && h.cao) || Math.max(h.rong, h.cao) >= 1000)
    .filter((h) => !BO.some((c) => h.nhan.includes(c)))
    .filter((h) => !rieng.length || rieng.some((w) => h.nhan.includes(w.replace(/s$/, ''))));
  return locTheoNhan(tuKhoa, hits);
}

const coKho = (env) => cacKho(env).length > 0;

/* Đợt 33 (04/11/2026) — VÌ SAO 48 BÀI KẸT KHÔNG CÓ ẢNH.
   Từ 01/11 Pixabay trả 429 "Rate limit exceeded" ở gần như mọi lượt, và
   header giới hạn trả về null — nghĩa là bị chặn ở tầng ngoài chứ không phải
   vượt 100 lượt/phút (mỗi lượt cron chỉ gọi chừng 10 lần). Code cũ chọn kho
   bằng `env.PIXABAY_API_KEY ? Pixabay : Pexels`, nên khi có key Pixabay thì
   KHÔNG BAO GIỜ thử Pexels — Pixabay chặn là cả hàng chờ đứng im.
   Giờ thử lần lượt từng kho có key, kho nào lỗi thì sang kho kế. Pexels đi
   trước vì Pixabay đang bị chặn; nếu sau này Pixabay thông thì nó vẫn là
   lưới dự phòng, không cần sửa code lại. */
function cacKho(env) {
  const ds = [];
  // Thứ tự: khoá tốt nhất trước, kho không cần khoá chốt cuối.
  // - Unsplash: ảnh nail nhiều và đẹp nhất, khoá miễn phí xin trong vài phút
  //   tại unsplash.com/developers (hạn mức 50 lượt/giờ bản thử, 5.000 khi
  //   đăng ký xong) — gấp nhiều lần mức 8 ảnh/ngày hệ thống này cần.
  // - Pexels: giữ lại cho trường hợp đã có khoá cũ (ngưng cấp khoá mới 10/2026).
  // - Pixabay: tụt xuống dưới vì đang bị chặn 429 từ 01/11/2026.
  // - Openverse: KHÔNG CẦN KHOÁ nên luôn có mặt, làm lưới cuối.
  if (env.UNSPLASH_ACCESS_KEY) ds.push(timUnsplash);
  if (env.PEXELS_API_KEY) ds.push(timPexels);
  if (env.PIXABAY_API_KEY) ds.push(timPixabay);
  ds.push(timOpenverse);
  return ds;
}

/* Sổ tạm trong MỘT lượt chạy: cùng một từ khoá không gọi API hai lần.
   Các từ khoá dự phòng ("manicure", "nail art"…) bị gọi lặp cho từng ô ảnh
   của từng bài — chính chỗ này đốt lượt gọi và làm Pixabay chặn nặng hơn.
   Phải xoá đầu mỗi lượt (xoaBoNho): isolate của Worker sống qua nhiều lượt. */
let boNho = new Map();
/* Kho đã hỏng trong lượt này: Pixabay bị chặn thì chặn cho MỌI từ khoá, nên
   thử lại từng từ khoá là vô ích mà rất đắt — mỗi lượt tìm lỗi mất ~13 giây
   (1,5s giãn + 4s + 8s chờ thử lại). Ba ô ảnh nhân bốn từ khoá dự phòng là
   hơn 200 giây, quá giới hạn thời gian của Worker → lượt chạy bị cắt giữa
   đường. Hỏng một lần thì bỏ kho đó tới hết lượt. */
let khoHong = new Set();
let hetGio = 0;
const NGAN_SACH_MS = 20_000;   // quá mức này thì để phần còn lại cho lượt sau
export const xoaBoNho = () => { boNho = new Map(); khoHong = new Set(); hetGio = Date.now() + NGAN_SACH_MS; };

async function timTheoKho(env, tuKhoa, bao) {
  if (boNho.has(tuKhoa)) return boNho.get(tuKhoa);
  if (Date.now() > hetGio) return [];           // hết ngân sách thời gian
  const loi = [];
  for (const tim of cacKho(env)) {
    if (khoHong.has(tim)) continue;
    try {
      const kq = await tim(env, tuKhoa);
      boNho.set(tuKhoa, kq);
      return kq;
    } catch (e) {
      loi.push(e.message);
      khoHong.add(tim);
    }
  }
  // Mọi kho đều lỗi: ghi vào báo cáo (thân commit) rồi trả rỗng, KHÔNG ném
  // lỗi — bài này hụt ảnh thì để lượt sau thử lại, không chặn bài kế tiếp.
  if (loi.length) bao.push(`tìm "${tuKhoa}" lỗi: ${loi.join(' | ')}`);
  boNho.set(tuKhoa, []);
  return [];
}

/** Còn kho nào dùng được trong lượt này không (hết thì khỏi thử tiếp cho nhanh) */
const conKho = (env) => cacKho(env).some((t) => !khoHong.has(t)) && Date.now() < hetGio;

async function timAnh(env, tuKhoa, daDung, bao, duPhong = true) {
  const kq = await timTheoKho(env, tuKhoa, bao);
  // Không lặp ảnh, và mỗi người chụp chỉ dùng MỘT lần trên toàn blog: Pixabay
  // có nhiều tấm của cùng một buổi chụp, khác id nhưng nhìn gần như y hệt.
  // Không có ảnh của người chụp mới thì chấp nhận người chụp cũ (khác ảnh) —
  // vẫn hơn là lấy ảnh lạc đề từ từ khoá chung chung.
  const p = kq.find((x) => !daDung.has(x.id) && !daDung.has(`u:${x.ten}`))
    || kq.find((x) => !daDung.has(x.id)) || null;
  if (p || !duPhong) return p;
  // Đợt 32: không tìm ra thì thử dần các từ khoá chung về làm móng, để bài
  // không bao giờ bị bỏ trống ảnh bìa (ô xám trên trang blog).
  for (const k of ['manicure', 'nail polish', 'manicure hands', 'nail art']) {
    if (k === tuKhoa) continue;
    const q = await timAnh(env, k, daDung, bao, false);
    // Đánh dấu ảnh lấy từ từ khoá chung: nó chỉ "có nail", KHÔNG chắc đúng màu/
    // kiểu bài đang nói, nên alt phải trung tính (xem altChoAnh).
    if (q) return { ...q, laDuPhong: true };
  }
  return null;
}

/** Alt thật thà: ảnh đúng từ khoá thì dùng alt người viết bài đã soạn; ảnh dự
    phòng (chỉ biết là có nail) thì không được khẳng định màu/kiểu mà ảnh có
    thể không có — dùng câu minh hoạ trung tính kèm tiêu đề bài. */
function altChoAnh(photo, altViet, post, lang = 'vi') {
  if (!photo.laDuPhong) return altViet;
  const tienTo = { vi: 'Ảnh minh hoạ', en: 'Illustration', ko: '참고 이미지', zh: '示意图' }[lang] || 'Illustration';
  return `${tienTo}: ${post.title}`;
}

async function taiAnh(photo, laBia) {
  const urls = [].concat(photo.tai(laBia));
  let loi = 'không gọi được';
  for (const u of urls) {
    let res = null;
    for (let lan = 0; lan < 3; lan++) {
      res = await fetch(u, { headers: { 'User-Agent': 'Mozilla/5.0 (vessca.com blog)' } });
      if (res.status !== 429) break;
      await new Promise((r) => setTimeout(r, 3000 * (lan + 1)));
    }
    if (!res.ok || !(res.headers.get('content-type') || '').startsWith('image/')) { loi = String(res.status); continue; }
    const bytes = new Uint8Array(await res.arrayBuffer());
    // Đợt 32: bản to quá thì thử bản nhỏ hơn (640px) thay vì kẹt mãi ở một ảnh
    if (bytes.length > 900_000) { loi = `nặng quá (${bytes.length} byte)`; continue; }
    // Unsplash buộc báo lại mỗi lần dùng ảnh. Lỗi ở đây không được làm hỏng
    // việc lấy ảnh — ảnh đã tải xong rồi.
    if (photo.sauKhiTai) { try { await photo.sauKhiTai(); } catch { /* bỏ qua */ } }
    return bytes;
  }
  throw new Error(`Tải ảnh ${photo.id} → ${loi}`);
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
  // Đợt 32: "lam_lai": ["bia", "2"] = chỉ làm lại đúng những ô đó (ảnh bìa,
  // ảnh trong bài thứ 2), giữ nguyên ảnh đang đẹp. Không có = làm lại hết.
  const chi = Array.isArray(post.anh.lam_lai) ? new Set(post.anh.lam_lai.map(String)) : null;
  const lam = (k) => !chi || chi.has(String(k));
  const goAnh = (html) => String(html || '').replace(
    new RegExp(`<figure><img src="/media/blog/${post.slug}-(\\d)\\.jpg"[\\s\\S]*?</figure>`, 'g'),
    (m, n) => (lam(n) ? `<!--anh:${n}-->` : m));
  post.content = goAnh(post.content);
  const banDich = post.i18n && typeof post.i18n === 'object' ? Object.entries(post.i18n) : [];
  for (const [, t] of banDich) if (t && t.content) t.content = goAnh(t.content);

  const files = [];
  const conThieu = [];      // ô ảnh cần làm mà lượt này không tìm được
  const bia = post.anh.bia;
  if (bia && bia.tim && lam('bia')) {
    const p = await timAnh(env, bia.tim, daDung, bao);
    if (p) {
      const bytes = await taiAnh(p, true);
      const path = `content/media/blog/${post.slug}.jpg`;
      files.push({ path, b64: bytesToB64(bytes) });
      daDung.add(p.id); daDung.add(`u:${p.ten}`);
      post.coverImage = `/media/blog/${post.slug}.jpg`;
      post.coverAlt = altChoAnh(p, bia.alt || post.coverAlt || post.title, post);
      // Ảnh dự phòng thì bỏ alt dịch (nó khẳng định màu/kiểu ảnh không chắc có)
      if (bia.altI18n && !p.laDuPhong) for (const [lang, t] of banDich) if (t && bia.altI18n[lang]) t.coverAlt = bia.altI18n[lang];
      post.coverCredit = { ten: p.ten, link: p.link, nguon: p.nguon, id: p.id };
    } else { bao.push(`${post.slug}: không tìm được ảnh bìa cho "${bia.tim}"`); conThieu.push('bia'); }
  }

  const trong = Array.isArray(post.anh.trong_bai) ? post.anh.trong_bai.slice(0, 2) : [];
  for (let i = 0; i < trong.length; i++) {
    const a = trong[i];
    if (!a || !a.tim || !lam(i + 1)) continue;
    const p = await timAnh(env, a.tim, daDung, bao);
    if (!p) { bao.push(`${post.slug}: không tìm được ảnh "${a.tim}"`); conThieu.push(String(i + 1)); continue; }
    const bytes = await taiAnh(p, false);
    const ten = `${post.slug}-${i + 1}.jpg`;
    files.push({ path: `content/media/blog/${ten}`, b64: bytesToB64(bytes) });
    daDung.add(p.id); daDung.add(`u:${p.ten}`);
    post.content = chenAnh(post.content || '', i + 1, hinhTrongBai(`/media/blog/${ten}`, altChoAnh(p, a.alt || post.title, post), p));
    // Bản dịch: dùng alt theo ngôn ngữ (a.altI18n.en …), không có thì lấy tiêu đề bản dịch
    for (const [lang, t] of banDich) {
      if (!t || !t.content) continue;
      const alt = p.laDuPhong ? altChoAnh(p, '', { title: t.title || post.title }, lang)
        : (a.altI18n && a.altI18n[lang]) || t.coverAlt || t.title;
      t.content = chenAnh(t.content, i + 1, hinhTrongBai(`/media/blog/${ten}`, alt, p, lang));
    }
  }

  /* Đợt 33: TRƯỚC ĐÂY đánh dấu `xong` vô điều kiện — kể cả khi không tìm
     được ảnh nào. Lỗi này chưa lộ ra vì Pixabay 429 ném lỗi nên không chạy
     tới đây; từ đợt này kho lỗi không còn ném lỗi, nên phải xử lý đúng:
     còn ô trống thì GIỮ bài trong hàng chờ, chỉ làm lại đúng ô còn thiếu.
     Thử tối đa 3 lượt rồi chấp nhận bỏ ô đó, kẻo một từ khoá không bao giờ
     ra ảnh sẽ chặn vĩnh viễn các bài xếp sau. Bài thiếu bìa vẫn hiện được:
     trang bài và trang danh sách đều lùi về ảnh mặc định. */
  const soAnh = files.length;
  const thu = Number(post.anh.thu || 0) + 1;
  if (conThieu.length && thu < 3) {
    post.anh.thu = thu;
    post.anh.lam_lai = conThieu;
  } else {
    if (conThieu.length) bao.push(`${post.slug}: bỏ ${conThieu.join(', ')} sau ${thu} lượt thử`);
    delete post.anh.thu;
    delete post.anh.lam_lai;
    post.anh.xong = new Date().toISOString();
  }
  files.push({ path: duongDan, b64: textToB64(JSON.stringify(post, null, 2) + '\n') });
  bao.push(`${post.slug}: ${soAnh} ảnh${conThieu.length ? ` (thiếu ${conThieu.join(', ')})` : ''}`);
  return { files, soAnh };
}

// ------------------------------------------------------------
//  Lượt chạy
// ------------------------------------------------------------
export async function chayDinhKy(env, { ep = false } = {}) {
  const bao = [];
  xoaBoNho();   // isolate Worker sống qua nhiều lượt — sổ tạm phải mới mỗi lượt
  const res = await env.ASSETS.fetch(new Request('https://vessca.com/_noi-bo/bai-viet.json'));
  const so = res.ok ? await res.json() : { henGio: [], canAnh: [], dungLuc: null };
  const files = [];

  // 1) Ảnh
  if (coKho(env) && so.canAnh?.length) {
    const daDungRaw = await docFile(env, DA_DUNG);
    const daDung = new Set(daDungRaw ? JSON.parse(daDungRaw) : []);
    // Sổ nội bộ chỉ mới lại sau khi web dựng xong — bài vừa làm ở lượt trước
    // có thể vẫn nằm trong danh sách. Bài nào đã xong thì bỏ qua, xét tối đa 4 bài.
    /* Đợt 33: trước đây gặp lỗi là `break` — thoát cả lượt. Một bài kẹt
       (nail-ombre-kieu-han, 3 lượt liền) chặn luôn mọi bài xếp sau, nên
       hàng chờ không nhúc nhích. Giờ bỏ qua bài lỗi và làm bài kế tiếp;
       chỉ dừng khi lỗi dồn quá LOI_TOI_DA (hỏng kho ảnh, không phải hỏng
       một bài) để khỏi đốt hết lượt gọi của gói miễn phí. */
    let lam = 0, loi = 0;
    for (const b of so.canAnh.slice(0, 8)) {
      if (lam >= BAI_MOI_LUOT || loi >= LOI_TOI_DA) break;
      if (!conKho(env)) { bao.push('hết kho ảnh dùng được trong lượt này — để lượt sau'); break; }
      try {
        const kq = await lamAnhChoBai(env, b.file, daDung, bao);
        if (!kq) continue;                      // bài đã xong, bỏ qua
        if (kq.files.length) files.push(...kq.files);
        if (kq.soAnh) lam++; else loi++;        // chỉ tính là làm được khi có ảnh
      } catch (e) {
        bao.push(`${b.slug}: lỗi — ${e.message}`);
        loi++;
      }
    }
    if (files.length) files.push({ path: DA_DUNG, b64: textToB64(JSON.stringify([...daDung]) + '\n') });
  } else if (!coKho(env) && so.canAnh?.length) {
    bao.push(`Chưa có PIXABAY_API_KEY lẫn PEXELS_API_KEY — ${so.canAnh.length} bài đang chờ ảnh`);
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
