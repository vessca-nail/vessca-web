/**
 * ============================================================
 *  ĐẶT LỊCH TỪ WEBSITE — /api/booking
 * ============================================================
 *  Khách điền form ở trang chủ  →  đơn được lưu vào D1 (vessca-bookings)
 *                               →  email báo về hộp thư của tiệm
 *                               →  phần mềm ở tiệm hỏi /api/booking/new
 *                                  vài chục giây một lần để lấy đơn mới
 *
 *  Vì sao lưu vào D1 chứ không chỉ gửi mail: để không đơn nào rớt.
 *  Mail có thể vào spam, có thể gửi hụt — còn đơn thì vẫn nằm đó,
 *  mở /admin/bookings là thấy, và máy ở tiệm kéo về được cả đơn cũ.
 */

import { checkKey } from './auth.js';

const JSON_HEADERS = { 'Content-Type': 'application/json; charset=utf-8' };

const json = (data, status = 200, extra = {}) =>
  new Response(JSON.stringify(data), { status, headers: { ...JSON_HEADERS, ...extra } });

/** Giới hạn độ dài để không ai nhét cả quyển sách vào ô ghi chú */
const trim = (v, max) => String(v ?? '').replace(/\s+/g, ' ').trim().slice(0, max);

/** Giờ Việt Nam, dạng người đọc được: 19/10/2026 15:42 */
function gioVN(iso) {
  return new Intl.DateTimeFormat('vi-VN', {
    timeZone: 'Asia/Ho_Chi_Minh',
    day: '2-digit', month: '2-digit', year: 'numeric',
    hour: '2-digit', minute: '2-digit', hour12: false,
  }).format(new Date(iso));
}

// ============================================================
//  Gửi email báo đơn mới
// ============================================================

const b64 = (bytes) => btoa(String.fromCharCode(...bytes));

/**
 * Mã hoá tiêu đề có dấu tiếng Việt theo RFC 2047.
 * Chuẩn giới hạn mỗi "encoded-word" 75 ký tự, nên phải cắt thành nhiều đoạn —
 * và chỉ được cắt ở ranh giới ký tự, không cắt giữa một chữ có dấu.
 */
function encodeSubject(s) {
  const enc = new TextEncoder();
  const words = [];
  let buf = [];

  for (const ch of String(s)) {
    const bytes = enc.encode(ch);
    // 36 byte → 48 ký tự base64 → cả encoded-word dài 60, còn dư so với mức 75
    if (buf.length + bytes.length > 36) {
      words.push(`=?UTF-8?B?${b64(buf)}?=`);
      buf = [];
    }
    buf.push(...bytes);
  }
  if (buf.length) words.push(`=?UTF-8?B?${b64(buf)}?=`);

  // Nhiều encoded-word nối nhau bằng xuống dòng + khoảng trắng (folding)
  return words.join('\r\n ') || '=?UTF-8?B??=';
}

/** Thân thư UTF-8 → base64, cắt dòng 76 ký tự cho đúng chuẩn */
function encodeBody(s) {
  const out = b64(new TextEncoder().encode(s));
  return (out.match(/.{1,76}/g) || []).join('\r\n');
}

function soanThu({ from, to, subject, body }) {
  return [
    `From: VESSCA <${from}>`,
    `To: <${to}>`,
    `Subject: ${encodeSubject(subject)}`,
    `Message-ID: <${crypto.randomUUID()}@vessca.com>`,
    `Date: ${new Date().toUTCString()}`,
    'MIME-Version: 1.0',
    'Content-Type: text/plain; charset=utf-8',
    'Content-Transfer-Encoding: base64',
    '',
    encodeBody(body),
  ].join('\r\n');
}

async function guiMail(env, don) {
  // Chưa gắn binding (ví dụ chạy thử ở máy) thì bỏ qua, đơn vẫn được lưu.
  if (!env.NOTIFY_EMAIL) return { ok: false, reason: 'chưa gắn NOTIFY_EMAIL' };

  const { EmailMessage } = await import('cloudflare:email');

  const from = 'dat-lich@vessca.com';
  const to = env.NOTIFY_TO || 'lamiesnail@gmail.com';

  const body = [
    'ĐƠN ĐẶT LỊCH MỚI TỪ WEBSITE',
    '',
    `Họ tên:    ${don.name}`,
    `Điện thoại: ${don.phone}`,
    `Dịch vụ:   ${don.service || '—'}`,
    `Mong muốn: ${don.preferred || '—'}`,
    `Ghi chú:   ${don.note || '—'}`,
    '',
    `Nhận lúc:  ${gioVN(don.created_at)} (giờ VN)`,
    `Mã đơn:    #${don.id}`,
    '',
    'Gọi khách: ' + don.phone,
    'Xem tất cả đơn: https://vessca.com/admin/bookings',
  ].join('\n');

  const raw = soanThu({
    from,
    to,
    subject: `Đặt lịch mới — ${don.name} — ${don.phone}`,
    body,
  });

  await env.NOTIFY_EMAIL.send(new EmailMessage(from, to, raw));
  return { ok: true };
}

// ============================================================
//  POST /api/booking  — khách gửi form
// ============================================================

async function nhanDon(request, env, ctx) {
  if (!env.BOOKINGS) {
    return json({ ok: false, error: 'Hệ thống đặt lịch chưa sẵn sàng.' }, 503);
  }

  // Form trang chủ gửi FormData; chừa đường cho JSON phòng khi sau này cần.
  let f;
  try {
    const ct = request.headers.get('Content-Type') || '';
    if (ct.includes('application/json')) {
      const o = await request.json();
      f = (k) => o[k];
    } else {
      const fd = await request.formData();
      f = (k) => fd.get(k);
    }
  } catch {
    return json({ ok: false, error: 'Dữ liệu gửi lên không đọc được.' }, 400);
  }

  // Bẫy robot: người thật không thấy ô này nên không bao giờ điền.
  // Trả về "thành công" để con bot tưởng xong việc mà đi chỗ khác.
  if (trim(f('botcheck'), 10)) return json({ ok: true });

  const name = trim(f('name') ?? f('Ho ten'), 80);
  const phone = trim(f('phone') ?? f('So dien thoai'), 30);
  const service = trim(f('service') ?? f('Dich vu'), 80);
  const preferred = trim(f('preferred') ?? f('Ngay gio mong muon'), 120);
  const note = trim(f('note') ?? f('Ghi chu'), 500);

  if (!name || !phone) {
    return json({ ok: false, error: 'Thiếu họ tên hoặc số điện thoại.' }, 400);
  }
  // Số điện thoại VN: chấp nhận cả +84, khoảng trắng, dấu chấm, gạch ngang.
  if (!/^[\d\s.+()-]{8,20}$/.test(phone)) {
    return json({ ok: false, error: 'Số điện thoại trông không đúng.' }, 400);
  }

  // Chặn gửi dồn: cùng một số, trong 15 phút, tối đa 3 đơn.
  const cutoff = new Date(Date.now() - 15 * 60 * 1000).toISOString();
  const { results: gan } = await env.BOOKINGS
    .prepare('SELECT COUNT(*) AS n FROM bookings WHERE phone = ? AND created_at > ?')
    .bind(phone, cutoff)
    .all();
  if ((gan?.[0]?.n ?? 0) >= 3) {
    return json(
      { ok: false, error: 'Bạn vừa gửi mấy yêu cầu liền nhau rồi. VESSCA sẽ gọi lại sớm nhé.' },
      429
    );
  }

  const created_at = new Date().toISOString();
  const row = await env.BOOKINGS
    .prepare(
      `INSERT INTO bookings (created_at, name, phone, service, preferred, note, status, source)
       VALUES (?, ?, ?, ?, ?, ?, 'moi', 'web')
       RETURNING id`
    )
    .bind(created_at, name, phone, service, preferred, note)
    .first();

  const don = { id: row?.id, created_at, name, phone, service, preferred, note };

  // Đơn đã nằm trong kho rồi. Mail gửi sau, và CÓ HỎNG CŨNG KHÔNG SAO —
  // không được để khách thấy lỗi chỉ vì mail trục trặc.
  const sendIt = guiMail(env, don).catch((err) => {
    console.error('Gửi mail báo đơn thất bại:', err?.message || err);
  });
  if (ctx?.waitUntil) ctx.waitUntil(sendIt); else await sendIt;

  return json({ ok: true, id: don.id });
}

// ============================================================
//  GET /api/booking/new  — phần mềm ở tiệm hỏi đơn mới
// ============================================================

async function donMoi(request, env) {
  const url = new URL(request.url);
  const since = Number(url.searchParams.get('since') || 0) || 0;
  const limit = Math.min(Number(url.searchParams.get('limit') || 50) || 50, 200);

  const { results } = await env.BOOKINGS
    .prepare(
      `SELECT id, created_at, name, phone, service, preferred, note, status
         FROM bookings
        WHERE id > ?
        ORDER BY id
        LIMIT ?`
    )
    .bind(since, limit)
    .all();

  const last = await env.BOOKINGS
    .prepare('SELECT COALESCE(MAX(id), 0) AS maxId FROM bookings')
    .first();

  return json(
    {
      ok: true,
      bookings: (results || []).map((r) => ({ ...r, created_at_vn: gioVN(r.created_at) })),
      lastId: last?.maxId ?? 0,
    },
    200,
    { 'Cache-Control': 'no-store' }
  );
}

/** POST /api/booking/seen — tiệm báo đã xem / đã xác nhận các đơn này */
async function danhDau(request, env) {
  let body;
  try {
    body = await request.json();
  } catch {
    return json({ ok: false, error: 'Dữ liệu không đọc được.' }, 400);
  }

  const ids = (Array.isArray(body?.ids) ? body.ids : [])
    .map(Number)
    .filter((n) => Number.isInteger(n) && n > 0)
    .slice(0, 200);
  if (!ids.length) return json({ ok: false, error: 'Không có mã đơn nào.' }, 400);

  const status = ['da_xem', 'da_xac_nhan', 'huy'].includes(body?.status) ? body.status : 'da_xem';
  const cho = ids.map(() => '?').join(',');

  await env.BOOKINGS
    .prepare(`UPDATE bookings SET status = ?, seen_at = ? WHERE id IN (${cho})`)
    .bind(status, new Date().toISOString(), ...ids)
    .run();

  return json({ ok: true, updated: ids.length });
}

// ============================================================
//  Bộ định tuyến
// ============================================================

export async function onRequest({ request, env, ctx }) {
  const path = new URL(request.url).pathname.replace(/\/+$/, '');
  const method = request.method;

  if (path === '/api/booking' && method === 'POST') {
    return await nhanDon(request, env, ctx);
  }

  // Hai đường dưới đây dành cho máy ở tiệm — phải có chìa khoá mới vào được.
  if (path === '/api/booking/new' || path === '/api/booking/seen') {
    if (!env.BOOKINGS) return json({ ok: false, error: 'Chưa gắn kho dữ liệu.' }, 503);

    const key =
      request.headers.get('X-Vessca-Key') ||
      (request.headers.get('Authorization') || '').replace(/^Bearer\s+/i, '');

    if (!(await checkKey(key, 'instore-poll', env))) {
      return json({ ok: false, error: 'Sai chìa khoá.' }, 401);
    }

    if (path === '/api/booking/new' && method === 'GET') return await donMoi(request, env);
    if (path === '/api/booking/seen' && method === 'POST') return await danhDau(request, env);
  }

  return json({ ok: false, error: 'Không có đường này.' }, 404);
}
