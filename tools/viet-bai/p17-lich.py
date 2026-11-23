# -*- coding: utf-8 -*-
"""Đợt 42 — gán ngày đăng cho 40 bài còn lại (10 bài đã lên 23/11).
Mỗi ngày 4 bài mới ở 4 khung 09:30 / 11:30 / 13:30 / 16:30, từ 24/11 tới 3/12.
Khung 08:30, 14:30 và 20:30 để nguyên cho các bài đã hẹn từ trước,
nên tổng mỗi ngày là 5 bài. Trộn chủ đề để mỗi ngày đều có gội đầu + nail."""
import json, os
B = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'content', 'posts') + os.sep

GOI = ['goi-dau-duong-sinh-gom-nhung-buoc-nao','goi-dau-duong-sinh-bao-nhieu-phut',
       'goi-dau-duong-sinh-co-giam-dau-dau-khong','goi-dau-duong-sinh-khac-goi-dau-thuong',
       'goi-dau-duong-sinh-co-can-coi-ao-khong','goi-dau-duong-sinh-co-lay-ray-tai-khong']
MUA = ['nail-noel-chan','nail-noel-tong-hong','nail-co-dau-chup-anh-cuoi','nail-co-dau-tone-hong',
       'nail-co-dau-hao-mon','nail-co-dau-2027','nail-tet-mong-ngan','nail-tet-mau-do',
       'nail-tet-mat-meo','nail-tet-nhe-nhang','nail-tet-don-gian','nail-tet-cho-nguoi-di-lam',
       'nail-tet-tong-nau','nail-tet-dinh-da','nail-tet-chup-anh-ao-dai']
MAU = ['nail-mau-thach-gao','nail-mau-tiffany-blue','nail-mau-cam-sua','nail-mau-trang-sua-dinh-da',
       'nail-mau-nau-tay','nail-tong-tim','nail-mau-xanh-la','nail-mau-xanh-bien']
KT  = ['nail-mong-ngan-don-gian','nail-mong-ngan-de-thuong','nail-mong-ngan-mat-meo',
       'nail-mong-ngan-tron-hay-vuong','up-mong-giu-duoc-bao-lau','up-mong-son-thach',
       'up-mong-base-la-gi','nail-han-quoc-de-thuong','nail-basic-han-quoc','nail-dep-sang-chanh',
       'xu-huong-nail-2027']

NGAY = ['2026-11-24','2026-11-25','2026-11-26','2026-11-27','2026-11-28',
        '2026-11-29','2026-11-30','2026-12-01','2026-12-02','2026-12-03']
KHUNG = ['09:30','11:30','13:30','16:30']

# Xếp xen kẽ: mỗi ngày lấy 1 bài từ mỗi nhóm, nhóm nào hết thì lấy bù từ nhóm dài nhất.
nhom = [GOI[:], MUA[:], MAU[:], KT[:]]
lich = []
for ngay in NGAY:
    for k, khung in enumerate(KHUNG):
        ds = nhom[k] or max(nhom, key=len)
        if not ds:
            continue
        lich.append((ds.pop(0), ngay + 'T' + khung + ':00+07:00'))

con = [s for ds in nhom for s in ds]
assert not con, 'còn sót: %s' % con
assert len(lich) == 40, len(lich)

for slug, at in lich:
    p = B + slug + '.json'
    d = json.load(open(p))
    d['publishedAt'] = at
    d['updatedAt'] = at
    json.dump(d, open(p, 'w'), ensure_ascii=False, indent=2)
print('da gan lich cho', len(lich), 'bai')
