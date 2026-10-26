/**
 * ============================================================
 *  THỐNG KÊ TRUY CẬP — tự làm, không dùng dịch vụ ngoài
 * ============================================================
 *  • /tk.js trên mỗi trang gửi về POST /api/tk: một lượt "xem" khi mở trang,
 *    một lượt "bam" khi khách bấm nút quan trọng (gọi điện, chỉ đường, đặt lịch…).
 *  • Không cookie. "Khách" = mã băm từ IP + trình duyệt + ngày, chỉ để đếm
 *    số người khác nhau trong một ngày — không lưu IP, không lần ngược được.
 *  • Lưu vào D1 (cùng kho với đơn đặt lịch), bảng tk_luot, giữ 400 ngày.
 */

const BOT = /bot|crawl|spider|slurp|facebookexternalhit|preview|monitor|headless|lighthouse|pingdom|curl|wget|python|axios|httpclient|java\//i;

let daTaoBang = false;
async function taoBang(db) {
  if (daTaoBang) return;
  await db.batch([
    db.prepare(`CREATE TABLE IF NOT EXISTS tk_luot (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      ts TEXT NOT NULL, ngay TEXT NOT NULL, gio INTEGER,
      loai TEXT NOT NULL, trang TEXT, nguon TEXT, nhan TEXT,
      thiet_bi TEXT, hdh TEXT, trinh_duyet TEXT,
      quoc_gia TEXT, thanh_pho TEXT, ngon_ngu TEXT, khach TEXT)`),
    db.prepare(`CREATE INDEX IF NOT EXISTS tk_ngay ON tk_luot(ngay)`),
  ]);
  // Đợt sau: mã ẩn danh của trình duyệt (vid) và phiên (phien)
  for (const c of ['vid TEXT', 'phien TEXT']) {
    try { await db.prepare(`ALTER TABLE tk_luot ADD COLUMN ${c}`).run(); } catch {}
  }
  try { await db.prepare(`CREATE INDEX IF NOT EXISTS tk_vid ON tk_luot(vid)`).run(); } catch {}
  daTaoBang = true;
}

const json = (d, s = 200) =>
  new Response(JSON.stringify(d), { status: s, headers: { 'Content-Type': 'application/json' } });

function gioVN(d = new Date()) {
  const p = new Intl.DateTimeFormat('en-CA', {
    timeZone: 'Asia/Ho_Chi_Minh', year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', hour12: false,
  }).formatToParts(d);
  const g = (t) => p.find((x) => x.type === t)?.value;
  return { ngay: `${g('year')}-${g('month')}-${g('day')}`, gio: Number(g('hour')) % 24 };
}

function thietBi(ua, cham) {
  if (/iPad|Tablet|PlayBook|Silk|(Android(?!.*Mobile))/i.test(ua)) return 'Máy tính bảng';
  if (/Mobi|iPhone|iPod|Android.*Mobile|Windows Phone/i.test(ua)) return 'Điện thoại';
  // iPad đời mới tự xưng là "Macintosh" — nhận ra nhờ có màn hình cảm ứng
  if (/Macintosh/i.test(ua) && cham > 1) return 'Máy tính bảng';
  return 'Máy tính';
}
function hdh(ua) {
  if (/iPhone|iPad|iPod/i.test(ua)) return 'iOS';
  if (/Android/i.test(ua)) return 'Android';
  if (/Windows/i.test(ua)) return 'Windows';
  if (/Mac OS X|Macintosh/i.test(ua)) return 'macOS';
  if (/Linux/i.test(ua)) return 'Linux';
  return 'Khác';
}
function trinhDuyet(ua) {
  if (/Zalo/i.test(ua)) return 'Zalo';
  if (/FBAN|FBAV|FB_IAB|Instagram/i.test(ua)) return 'Facebook/Instagram';
  if (/CocCoc|coc_coc/i.test(ua)) return 'Cốc Cốc';
  if (/Edg\//i.test(ua)) return 'Edge';
  if (/SamsungBrowser/i.test(ua)) return 'Samsung';
  if (/CriOS|Chrome\//i.test(ua)) return 'Chrome';
  if (/Firefox|FxiOS/i.test(ua)) return 'Firefox';
  if (/Safari/i.test(ua)) return 'Safari';
  return 'Khác';
}
function nguon(ref, ua) {
  if (/Zalo/i.test(ua)) return 'Zalo';
  if (/FBAN|FBAV|FB_IAB/i.test(ua)) return 'Facebook';
  if (/Instagram/i.test(ua)) return 'Instagram';
  if (!ref) return 'Vào thẳng';
  let h = '';
  try { h = new URL(ref).hostname.replace(/^www\./, ''); } catch { return 'Khác'; }
  if (h.endsWith('vessca.com')) return 'Trong web';
  if (/google\./.test(h)) return 'Google';
  if (/bing\.|duckduckgo|yahoo|coccoc|naver|baidu/.test(h)) return 'Công cụ tìm kiếm khác';
  if (/facebook|fb\.|messenger/.test(h)) return 'Facebook';
  if (/instagram/.test(h)) return 'Instagram';
  if (/zalo/.test(h)) return 'Zalo';
  if (/tiktok/.test(h)) return 'TikTok';
  if (/chatgpt|openai|claude|perplexity|gemini/.test(h)) return 'Trợ lý AI';
  return h.slice(0, 60);
}

async function maKhach(request, ngay, env) {
  const ip = request.headers.get('CF-Connecting-IP') || '';
  const ua = request.headers.get('User-Agent') || '';
  const muoi = env.SESSION_SECRET || 'vessca';
  const buf = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(`${muoi}|${ngay}|${ip}|${ua}`));
  return [...new Uint8Array(buf)].slice(0, 8).map((b) => b.toString(16).padStart(2, '0')).join('');
}

const sach = (x) => (String(x || '').replace(/[^a-z0-9]/gi, '').slice(0, 32) || null);

// ------------------------------------------------------------
//  POST /api/tk
// ------------------------------------------------------------
export async function ghiLuot(request, env) {
  if (request.method !== 'POST' || !env.BOOKINGS) return new Response(null, { status: 204 });
  const ua = request.headers.get('User-Agent') || '';
  if (!ua || BOT.test(ua)) return new Response(null, { status: 204 });
  let d;
  try { d = JSON.parse((await request.text()).slice(0, 2000)); } catch { return new Response(null, { status: 204 }); }
  const loai = d.t === 'bam' ? 'bam' : 'xem';
  const trang = String(d.p || '/').slice(0, 200);
  if (trang.startsWith('/admin')) return new Response(null, { status: 204 });

  const { ngay, gio } = gioVN();
  const cf = request.cf || {};
  const db = env.BOOKINGS;
  await taoBang(db);
  await db.prepare(
    `INSERT INTO tk_luot (ts, ngay, gio, loai, trang, nguon, nhan, thiet_bi, hdh, trinh_duyet, quoc_gia, thanh_pho, ngon_ngu, khach, vid, phien)
     VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)`
  ).bind(
    new Date().toISOString(), ngay, gio, loai, trang,
    loai === 'xem' ? nguon(String(d.r || ''), ua) : null,
    loai === 'bam' ? String(d.n || '').slice(0, 60) : null,
    thietBi(ua, Number(d.m) || 0), hdh(ua), trinhDuyet(ua),
    String(cf.country || '').slice(0, 4), String(cf.city || '').slice(0, 60),
    String(d.l || '').slice(0, 8),
    await maKhach(request, ngay, env),
    sach(d.v), sach(d.s)
  ).run();
  return new Response(null, { status: 204 });
}

/** Xoá dữ liệu cũ hơn 400 ngày — gọi từ lượt chạy định kỳ. */
export async function donDep(env) {
  if (!env.BOOKINGS) return;
  await taoBang(env.BOOKINGS);
  const moc = gioVN(new Date(Date.now() - 400 * 86400000)).ngay;
  await env.BOOKINGS.prepare(`DELETE FROM tk_luot WHERE ngay < ?`).bind(moc).run();
}

// ------------------------------------------------------------
//  Số liệu cho trang /admin/thong-ke
// ------------------------------------------------------------
export async function layThongKe(env, soNgay) {
  const db = env.BOOKINGS;
  await taoBang(db);
  const tu = gioVN(new Date(Date.now() - (soNgay - 1) * 86400000)).ngay;
  const q = (sql, ...b) => db.prepare(sql).bind(tu, ...b).all().then((r) => r.results || []);
  const nhom = (cot, loai = 'xem', lim = 12) =>
    q(`SELECT ${cot} AS k, COUNT(*) AS n, COUNT(DISTINCT COALESCE(vid, khach)) AS kh
         FROM tk_luot WHERE ngay >= ? AND loai = ? AND ${cot} IS NOT NULL AND ${cot} != ''${cot === 'nguon' ? ` AND nguon != 'Trong web'` : ''}
        GROUP BY ${cot} ORDER BY n DESC LIMIT ${lim}`, loai);

  const [tong, theoNgay, thietBi, nguon, trang, nut, quocGia, thanhPho, ngonNgu, trinhDuyet, theoGio, don] =
    await Promise.all([
      q(`SELECT SUM(loai='xem') AS xem, COUNT(DISTINCT CASE WHEN loai='xem' THEN COALESCE(vid, khach) END) AS khach,
                SUM(loai='bam') AS bam FROM tk_luot WHERE ngay >= ?`),
      q(`SELECT ngay, SUM(loai='xem') AS xem, COUNT(DISTINCT CASE WHEN loai='xem' THEN COALESCE(vid, khach) END) AS khach
           FROM tk_luot WHERE ngay >= ? GROUP BY ngay ORDER BY ngay`),
      nhom('thiet_bi'), nhom('nguon'), nhom('trang', 'xem', 15), nhom('nhan', 'bam', 15),
      nhom('quoc_gia'), nhom('thanh_pho', 'xem', 10), nhom('ngon_ngu'), nhom('trinh_duyet'),
      q(`SELECT gio AS k, COUNT(*) AS n FROM tk_luot WHERE ngay >= ? AND loai='xem' GROUP BY gio ORDER BY gio`),
      db.prepare(`SELECT COUNT(*) AS n FROM bookings WHERE created_at >= ?`).bind(tu).first().catch(() => ({ n: null })),
    ]);
  // ---- Khách mới / quay lại (theo mã ẩn danh của trình duyệt) ----
  const [mq] = await q(
    `SELECT COUNT(*) AS tong, SUM(dau >= ?1) AS moi, SUM(so_ngay >= 2) AS quay_lai FROM (
       SELECT vid, MIN(ngay) AS dau, COUNT(DISTINCT COALESCE(phien, ngay)) AS so_ngay FROM tk_luot
        WHERE vid IN (SELECT DISTINCT vid FROM tk_luot WHERE ngay >= ?1 AND vid IS NOT NULL)
        GROUP BY vid)`);

  // ---- Hành trình 40 khách gần nhất ----
  const gan = await q(
    `SELECT vid, MAX(ts) AS cuoi, MIN(ts) AS dau_ky, COUNT(DISTINCT phien) AS so_lan
       FROM tk_luot WHERE ngay >= ? AND vid IS NOT NULL GROUP BY vid ORDER BY cuoi DESC LIMIT 40`);
  let khachGan = [];
  if (gan.length) {
    const ds = gan.map((g) => g.vid);
    const dau = ds.map(() => '?').join(',');
    const ev = (await db.prepare(
      `SELECT vid, ts, loai, trang, nhan, nguon, thiet_bi, thanh_pho, quoc_gia, phien FROM tk_luot
        WHERE ngay >= ? AND vid IN (${dau}) ORDER BY ts`).bind(tu, ...ds).all()).results || [];
    let don = [];
    try {
      don = (await db.prepare(`SELECT vid, name, created_at FROM bookings WHERE vid IN (${dau})`).bind(...ds).all()).results || [];
    } catch {}
    const [lanTruoc] = await Promise.all([
      db.prepare(`SELECT vid, COUNT(DISTINCT ngay) AS n FROM tk_luot WHERE ngay < ? AND vid IN (${dau}) GROUP BY vid`).bind(tu, ...ds).all().then((r) => r.results || []).catch(() => []),
    ]);
    const truoc = Object.fromEntries(lanTruoc.map((r) => [r.vid, r.n]));
    khachGan = gan.map((g) => {
      const e = ev.filter((x) => x.vid === g.vid);
      const xem1 = e.find((x) => x.loai === 'xem') || e[0] || {};
      return {
        vid: g.vid, cuoi: g.cuoi, soLan: g.so_lan, ngayTruoc: truoc[g.vid] || 0,
        nguon: xem1.nguon, thietBi: xem1.thiet_bi, thanhPho: xem1.thanh_pho, quocGia: xem1.quoc_gia,
        don: don.filter((d) => d.vid === g.vid),
        buoc: e.slice(-40).map((x) => ({ ts: x.ts, loai: x.loai, trang: x.trang, nhan: x.nhan, nguon: x.nguon, phien: x.phien })),
      };
    });
  }

  return { soNgay, tu, tong: tong[0] || {}, theoNgay, thietBi, nguon, trang, nut, quocGia, thanhPho, ngonNgu, trinhDuyet, theoGio, donDatLich: don?.n,
    khachMoi: mq?.moi || 0, khachQuayLai: mq?.quay_lai || 0, khachGan };
}
