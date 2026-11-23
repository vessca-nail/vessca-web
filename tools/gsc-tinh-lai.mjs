/**
 * Tính lại các mục suy ra được từ số liệu đã có sẵn trong data/gsc/,
 * KHÔNG gọi Google. Dùng khi sửa cách tính (ví dụ 23/11 tách nhóm bài
 * bản Việt không hiện) và muốn trang /admin/thong-ke đúng ngay, không
 * phải đợi lượt chạy sáng mai của GitHub Actions.
 *
 *   node tools/gsc-tinh-lai.mjs
 */
import fs from 'node:fs/promises';
import path from 'node:path';
import { timBaiChuaThay, ghiLichSu, OUT_DIR } from './gsc-fetch.mjs';

const duong = path.join(OUT_DIR, 'latest.json');
const data = JSON.parse(await fs.readFile(duong, 'utf8'));
data.chuaIndex = await timBaiChuaThay(data.pages, data.range.endDate);
await fs.writeFile(duong, JSON.stringify(data, null, 2) + '\n');

const banChot = path.join(OUT_DIR, `${data.range.endDate}.json`);
try {
  const d2 = JSON.parse(await fs.readFile(banChot, 'utf8'));
  d2.chuaIndex = data.chuaIndex;
  await fs.writeFile(banChot, JSON.stringify(d2, null, 2) + '\n');
} catch { /* chưa có bản chốt cùng ngày thì thôi */ }

const soMoc = await ghiLichSu();
const chuaThay = data.chuaIndex.filter((x) => !x.banDichHien).length;
console.log(`Tính lại xong: ${data.chuaIndex.length} bài bản Việt không hiện ` +
  `(${data.chuaIndex.length - chuaThay} bài có bản dịch đang hiện, ${chuaThay} bài im cả bốn bản)`);
console.log(`Lịch sử: ${soMoc} mốc`);
