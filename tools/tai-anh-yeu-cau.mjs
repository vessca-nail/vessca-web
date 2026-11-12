// Tải các ảnh có "url" trong content/media/yeu-cau.json (ảnh đã chọn tay, vd Pexels)
// về content/media/<luu>. Chạy bằng GitHub Actions (bấm tay) khi cần ảnh NGAY,
// không chờ lượt định kỳ của Worker. Mục nào tải xong thì ghi "xong".
import fs from 'node:fs/promises';
import path from 'node:path';
const F = 'content/media/yeu-cau.json';
const ds = JSON.parse(await fs.readFile(F, 'utf8'));
for (const x of ds) {
  if (!x || !x.luu || !x.url || x.xong) continue;
  const res = await fetch(x.url, { headers: { 'User-Agent': 'Mozilla/5.0 (vessca.com)' } });
  const loai = res.headers.get('content-type') || '';
  if (!res.ok || !loai.startsWith('image/')) { console.log(`${x.luu}: lỗi ${res.status} ${loai}`); continue; }
  const b = Buffer.from(await res.arrayBuffer());
  if (b.length > 900_000) { console.log(`${x.luu}: nặng quá (${b.length})`); continue; }
  const dich = path.join('content/media', x.luu);
  await fs.mkdir(path.dirname(dich), { recursive: true });
  await fs.writeFile(dich, b);
  x.xong = new Date().toISOString();
  x.nguon = { ten: x.ten || '', link: x.link || x.url, nguon: x.kho || 'Pexels', id: `url:${x.url}` };
  console.log(`${x.luu}: đã tải ${b.length} byte`);
}
await fs.writeFile(F, JSON.stringify(ds, null, 2) + '\n');
