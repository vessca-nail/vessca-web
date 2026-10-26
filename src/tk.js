/* Thống kê truy cập VESSCA — gửi lượt xem trang và các nút quan trọng được bấm.
   Không dùng cookie, không lưu gì trên máy khách, không gửi thông tin cá nhân. */
(function () {
  try {
    if (navigator.webdriver) return;
    // Máy đã đăng nhập trang quản trị (máy của tiệm) thì không đếm
    try { if (localStorage.getItem('vsNoTk') === '1') return; } catch (e) {}
    var gui = function (d) {
      d.p = location.pathname;
      d.l = document.documentElement.lang || '';
      d.m = navigator.maxTouchPoints || 0;
      var s = JSON.stringify(d);
      if (navigator.sendBeacon) navigator.sendBeacon('/api/tk', new Blob([s], { type: 'application/json' }));
      else fetch('/api/tk', { method: 'POST', body: s, keepalive: true, headers: { 'Content-Type': 'application/json' } });
    };
    window.vsTk = function (nhan) { try { gui({ t: 'bam', n: String(nhan).slice(0, 60) }); } catch (e) {} };

    gui({ t: 'xem', r: document.referrer || '' });

    var nhanCua = function (a) {
      if (a.dataset && a.dataset.tk) return a.dataset.tk;
      var h = a.getAttribute('href') || '';
      if (/^tel:/i.test(h)) return 'Gọi điện';
      if (/maps\.(google|app\.goo)|goo\.gl\/maps|maps\.app/i.test(h)) return 'Chỉ đường';
      if (/zalo\.me/i.test(h)) return 'Zalo';
      if (/instagram\.com/i.test(h)) return 'Instagram';
      if (/facebook\.com|fb\.com|m\.me/i.test(h)) return 'Facebook';
      if (/#booking/.test(h)) return 'Nút đặt lịch';
      if (/^\/(en\/|ko\/|zh\/)?blog\/?$/.test(h)) return 'Mở blog';
      return '';
    };
    document.addEventListener('click', function (e) {
      var el = e.target && e.target.closest ? e.target.closest('a,button') : null;
      if (!el) return;
      var n = '';
      if (el.tagName === 'A') n = nhanCua(el);
      else if (el.dataset && el.dataset.lang) n = 'Đổi ngôn ngữ: ' + el.dataset.lang;
      else if (el.dataset && el.dataset.tk) n = el.dataset.tk;
      if (n) window.vsTk(n);
    }, true);
  } catch (e) {}
})();
