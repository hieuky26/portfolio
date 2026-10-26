/* Portfolio - tuong tac phia client. Khong phu thuoc thu vien ngoai. */
(function () {
  "use strict";

  /* ---------- Nam hien tai o footer ---------- */
  var yearEl = document.getElementById("year");
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  /* ---------- Ghi nho ngon ngu nguoi dung chon ---------- */
  document.querySelectorAll("a[data-lang]").forEach(function (a) {
    a.addEventListener("click", function () {
      try {
        localStorage.setItem("lang", a.dataset.lang || "en");
      } catch (e) {}
    });
  });

  /* ---------- Logo: thieu file thi quay ve dau hieu chu cai ---------- */
  var brandLogo = document.getElementById("brandLogo");
  if (brandLogo) {
    var useInitials = function () {
      if (!brandLogo.parentNode) return;
      var mark = document.createElement("span");
      mark.className = "brand__mark";
      mark.setAttribute("aria-hidden", "true");
      mark.textContent = brandLogo.dataset.fallback || "";
      brandLogo.replaceWith(mark);
    };
    brandLogo.addEventListener("error", useInitials);
    // Script chay voi defer nen anh co the da loi xong truoc khi gan listener
    if (brandLogo.complete && brandLogo.naturalWidth === 0) useInitials();
  }

  /* ---------- Menu mobile tu dong sau khi chon ---------- */
  var menu = document.querySelector(".menu");
  if (menu) {
    menu.addEventListener("click", function (e) {
      if (e.target.closest("a")) menu.open = false;
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") menu.open = false;
    });
    document.addEventListener("click", function (e) {
      if (!menu.contains(e.target)) menu.open = false;
    });
  }

  /* ---------- Tabs ky nang: phim mui ten chuyen tab, panel con lai an ---------- */
  var tabs = Array.prototype.slice.call(document.querySelectorAll('[role="tab"]'));

  function pick(tab) {
    tabs.forEach(function (b) {
      var on = b === tab;
      b.setAttribute("aria-selected", on ? "true" : "false");
      b.tabIndex = on ? 0 : -1;
      document.getElementById(b.getAttribute("aria-controls")).hidden = !on;
    });
  }

  tabs.forEach(function (tab, i) {
    tab.addEventListener("click", function () {
      pick(tab);
    });
    tab.addEventListener("keydown", function (e) {
      var step = { ArrowDown: 1, ArrowRight: 1, ArrowUp: -1, ArrowLeft: -1 }[e.key];
      if (!step) return;
      e.preventDefault();
      var next = tabs[(i + step + tabs.length) % tabs.length];
      next.focus();
      pick(next);
    });
  });

  /* ---------- Bam ky nang -> hien mo ta o cuoi panel ---------- */
  document.querySelectorAll(".panel").forEach(function (panel) {
    var detail = panel.querySelector(".detail");
    var chips = panel.querySelectorAll(".chip");

    chips.forEach(function (chip) {
      chip.addEventListener("click", function () {
        chips.forEach(function (c) {
          c.setAttribute("aria-pressed", c === chip ? "true" : "false");
        });

        var name = document.createElement("b");
        name.textContent = chip.dataset.name || "";
        var text = document.createElement("span");
        text.appendChild(name);
        text.appendChild(document.createTextNode(chip.dataset.detail || ""));

        detail.classList.remove("swap");
        detail.replaceChildren(text);
        void detail.offsetWidth; // ep trinh duyet chay lai animation
        detail.classList.add("swap");
      });
    });
  });

  /* ---------- Hien dan khi cuon toi ---------- */
  var revealables = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          entry.target.classList.add("in");
          io.unobserve(entry.target);
        });
      },
      { threshold: 0.12 }
    );
    revealables.forEach(function (el) {
      io.observe(el);
    });
  } else {
    revealables.forEach(function (el) {
      el.classList.add("in");
    });
  }

  /* ---------- Nut sao chep email ---------- */
  document.querySelectorAll("[data-copy]").forEach(function (btn) {
    var label = btn.dataset.label || btn.textContent;

    function show(text) {
      btn.textContent = text;
      setTimeout(function () {
        btn.textContent = label;
      }, 2000);
    }

    function fallback(value) {
      // Du phong cho trinh duyet cu / ket noi http
      var ta = document.createElement("textarea");
      ta.value = value;
      ta.style.position = "fixed";
      ta.style.opacity = "0";
      document.body.appendChild(ta);
      ta.select();
      var ok = false;
      try {
        ok = document.execCommand("copy");
      } catch (err) {}
      document.body.removeChild(ta);
      show(ok ? btn.dataset.done : btn.dataset.fail);
    }

    btn.addEventListener("click", function () {
      var value = btn.dataset.copy || "";
      if (navigator.clipboard && window.isSecureContext) {
        navigator.clipboard.writeText(value).then(
          function () {
            show(btn.dataset.done);
          },
          function () {
            fallback(value);
          }
        );
      } else {
        fallback(value);
      }
    });
  });
})();
