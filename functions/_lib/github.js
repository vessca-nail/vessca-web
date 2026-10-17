/**
 * Đọc/ghi file trong kho GitHub của website.
 * Mỗi lần bạn bấm "Lưu" ở trang admin, hàm ở đây sẽ gửi file lên
 * GitHub. Cloudflare thấy có file mới sẽ tự build lại website.
 * Nhờ vậy mọi thay đổi đều có lịch sử và quay lui được.
 */

const API = 'https://api.github.com';

function headers(env) {
  return {
    Authorization: `Bearer ${env.GITHUB_TOKEN}`,
    Accept: 'application/vnd.github+json',
    'X-GitHub-Api-Version': '2022-11-28',
    'User-Agent': 'vessca-admin',
    'Content-Type': 'application/json',
  };
}

const branch = (env) => env.GITHUB_BRANCH || 'main';

/** Chuyển chữ (có dấu tiếng Việt) sang base64 đúng chuẩn UTF-8 */
export function toBase64(text) {
  const bytes = new TextEncoder().encode(text);
  return bytesToBase64(bytes);
}

/** Chuyển dữ liệu nhị phân (ảnh) sang base64, chia nhỏ để không tràn bộ nhớ */
export function bytesToBase64(bytes) {
  let out = '';
  const CHUNK = 0x8000;
  for (let i = 0; i < bytes.length; i += CHUNK) {
    out += String.fromCharCode.apply(null, bytes.subarray(i, i + CHUNK));
  }
  return btoa(out);
}

export function fromBase64(b64) {
  const bin = atob(b64.replace(/\s/g, ''));
  const bytes = new Uint8Array(bin.length);
  for (let i = 0; i < bin.length; i++) bytes[i] = bin.charCodeAt(i);
  return new TextDecoder().decode(bytes);
}

async function call(env, path, init = {}) {
  const res = await fetch(`${API}/repos/${env.GITHUB_REPO}${path}`, {
    ...init,
    headers: headers(env),
  });
  return res;
}

/** Lấy nội dung 1 file. Trả về null nếu file chưa tồn tại. */
export async function getFile(env, filePath) {
  const res = await call(env, `/contents/${encodeURI(filePath)}?ref=${branch(env)}`);
  if (res.status === 404) return null;
  if (!res.ok) throw new Error(`GitHub đọc file lỗi ${res.status}: ${await res.text()}`);
  const data = await res.json();
  return { sha: data.sha, text: fromBase64(data.content || ''), size: data.size };
}

/** Liệt kê file trong 1 thư mục. Trả về [] nếu thư mục chưa có. */
export async function listDir(env, dirPath) {
  const res = await call(env, `/contents/${encodeURI(dirPath)}?ref=${branch(env)}`);
  if (res.status === 404) return [];
  if (!res.ok) throw new Error(`GitHub đọc thư mục lỗi ${res.status}`);
  const data = await res.json();
  return Array.isArray(data) ? data : [];
}

/** Tạo mới hoặc ghi đè 1 file (nội dung truyền vào đã là base64) */
export async function putFile(env, filePath, contentBase64, message) {
  const existing = await getFile(env, filePath).catch(() => null);
  const res = await call(env, `/contents/${encodeURI(filePath)}`, {
    method: 'PUT',
    body: JSON.stringify({
      message,
      content: contentBase64,
      branch: branch(env),
      ...(existing ? { sha: existing.sha } : {}),
      committer: { name: 'VESSCA Admin', email: 'admin@vessca.com' },
    }),
  });
  if (!res.ok) throw new Error(`GitHub ghi file lỗi ${res.status}: ${await res.text()}`);
  return res.json();
}

export async function deleteFile(env, filePath, message) {
  const existing = await getFile(env, filePath);
  if (!existing) return { deleted: false };
  const res = await call(env, `/contents/${encodeURI(filePath)}`, {
    method: 'DELETE',
    body: JSON.stringify({
      message,
      sha: existing.sha,
      branch: branch(env),
      committer: { name: 'VESSCA Admin', email: 'admin@vessca.com' },
    }),
  });
  if (!res.ok) throw new Error(`GitHub xoá file lỗi ${res.status}: ${await res.text()}`);
  return { deleted: true };
}

/** Lịch sử thay đổi của 1 file — dùng cho tính năng quay lui giao diện */
export async function fileHistory(env, filePath, limit = 15) {
  const res = await call(
    env,
    `/commits?path=${encodeURIComponent(filePath)}&sha=${branch(env)}&per_page=${limit}`
  );
  if (!res.ok) return [];
  const data = await res.json();
  return data.map((c) => ({
    sha: c.sha,
    date: c.commit?.committer?.date || c.commit?.author?.date,
    message: (c.commit?.message || '').split('\n')[0],
  }));
}

/** Lấy nội dung 1 file tại một thời điểm cũ (theo mã commit) */
export async function getFileAt(env, filePath, sha) {
  const res = await call(env, `/contents/${encodeURI(filePath)}?ref=${sha}`);
  if (!res.ok) throw new Error(`Không đọc được bản cũ (${res.status})`);
  const data = await res.json();
  return fromBase64(data.content || '');
}

/** Kiểm tra token còn dùng được và có quyền ghi không */
export async function checkAccess(env) {
  const res = await fetch(`${API}/repos/${env.GITHUB_REPO}`, { headers: headers(env) });
  if (!res.ok) {
    return { ok: false, reason: res.status === 404
      ? 'Không tìm thấy kho GitHub — kiểm tra lại biến GITHUB_REPO'
      : `GitHub trả về lỗi ${res.status} — token có thể đã hết hạn` };
  }
  const repo = await res.json();
  if (!repo.permissions?.push) {
    return { ok: false, reason: 'Token không có quyền ghi vào kho này' };
  }
  return { ok: true, repo: repo.full_name, branch: branch(env) };
}
