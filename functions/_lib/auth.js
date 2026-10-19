/**
 * Đăng nhập trang admin.
 * Mật khẩu KHÔNG nằm trong code — nó được đặt trong phần
 * "Environment variables" của Cloudflare (biến ADMIN_PASSWORD),
 * nên dù ai đó xem được mã nguồn trên GitHub cũng không thấy mật khẩu.
 */

const COOKIE = 'vessca_session';
const MAX_AGE = 60 * 60 * 24 * 7; // 7 ngày

const enc = new TextEncoder();

function b64url(buf) {
  let s = '';
  const bytes = new Uint8Array(buf);
  for (let i = 0; i < bytes.length; i++) s += String.fromCharCode(bytes[i]);
  return btoa(s).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
}

async function hmac(data, secret) {
  const key = await crypto.subtle.importKey(
    'raw', enc.encode(secret), { name: 'HMAC', hash: 'SHA-256' }, false, ['sign']
  );
  return b64url(await crypto.subtle.sign('HMAC', key, enc.encode(data)));
}

/** So sánh chuỗi theo kiểu không để lộ thông tin qua thời gian xử lý */
function safeEqual(a = '', b = '') {
  if (a.length !== b.length) return false;
  let diff = 0;
  for (let i = 0; i < a.length; i++) diff |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return diff === 0;
}

/**
 * Sinh ra một "chìa khoá" cố định cho máy móc dùng (ví dụ phần mềm ở tiệm
 * hỏi đơn đặt lịch mới). Khoá này tính ra từ SESSION_SECRET nên:
 *   • không phải thêm biến bí mật mới trên Cloudflare
 *   • không nằm trong mã nguồn, dù kho GitHub để công khai
 *   • đổi SESSION_SECRET là mọi khoá cũ hết hiệu lực
 */
export async function deriveKey(purpose, env) {
  if (!env.SESSION_SECRET) return null;
  return await hmac(`key:${purpose}`, env.SESSION_SECRET);
}

/** So khoá máy gửi lên với khoá đúng, theo kiểu không lộ qua thời gian xử lý */
export async function checkKey(input, purpose, env) {
  const want = await deriveKey(purpose, env);
  if (!want) return false;
  return safeEqual(String(input || ''), want);
}

export async function createSession(env) {
  const exp = Date.now() + MAX_AGE * 1000;
  const payload = String(exp);
  const sig = await hmac(payload, env.SESSION_SECRET);
  return `${COOKIE}=${payload}.${sig}; Path=/admin; HttpOnly; Secure; SameSite=Lax; Max-Age=${MAX_AGE}`;
}

export function clearSession() {
  return `${COOKIE}=; Path=/admin; HttpOnly; Secure; SameSite=Lax; Max-Age=0`;
}

export async function isLoggedIn(request, env) {
  if (!env.SESSION_SECRET) return false;
  const raw = request.headers.get('Cookie') || '';
  const match = raw.match(new RegExp(`${COOKIE}=([^;]+)`));
  if (!match) return false;

  const [payload, sig] = match[1].split('.');
  if (!payload || !sig) return false;
  if (!safeEqual(sig, await hmac(payload, env.SESSION_SECRET))) return false;
  return Number(payload) > Date.now();
}

export function checkPassword(input, env) {
  if (!env.ADMIN_PASSWORD) return false;
  return safeEqual(String(input || ''), String(env.ADMIN_PASSWORD));
}

/** Kiểm tra các biến môi trường bắt buộc — báo rõ nếu thiếu cái nào */
export function missingConfig(env) {
  return ['ADMIN_PASSWORD', 'SESSION_SECRET', 'GITHUB_TOKEN', 'GITHUB_REPO']
    .filter((k) => !env[k]);
}
