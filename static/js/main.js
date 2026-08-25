/* Portfolio — tuong tac phia client. Khong phu thuoc thu vien ngoai. */
(function () {
  "use strict";

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- Nam hien tai o footer ---------- */
  var yearEl = document.getElementById("year");
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  /* ---------- Nav: do bong khi cuon + thanh tien do ---------- */
  var nav = document.getElementById("nav");
  var progress = document.getElementById("navProgress");
  var toTop = document.getElementById("toTop");

  function onScroll() {
    var y = window.scrollY || document.documentElement.scrollTop;

    if (nav) nav.classList.toggle("is-stuck", y > 8);
    if (toTop) toTop.classList.toggle("is-show", y > 600);

    if (progress) {
      var max = document.documentElement.scrollHeight - window.innerHeight;
      progress.style.width = (max > 0 ? (y / max) * 100 : 0) + "%";
    }
  }

  var ticking = false;
  window.addEventListener(
    "scroll",
    function () {
      if (ticking) return;
      ticking = true;
      window.requestAnimationFrame(function () {
        onScroll();
        ticking = false;
      });
    },
    { passive: true }
  );
  onScroll();

  /* ---------- Menu mobile ---------- */
  var burger = document.getElementById("navBurger");
  var links = document.getElementById("navLinks");

  function closeMenu() {
    if (!links) return;
    links.classList.remove("is-open");
    if (burger) burger.setAttribute("aria-expanded", "false");
  }

  if (burger && links) {
    burger.addEventListener("click", function () {
      var open = links.classList.toggle("is-open");
      burger.setAttribute("aria-expanded", open ? "true" : "false");
    });

    links.addEventListener("click", function (e) {
      if (e.target.closest("a")) closeMenu();
    });

    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") closeMenu();
    });

    document.addEventListener("click", function (e) {
      if (!links.contains(e.target) && !burger.contains(e.target)) closeMenu();
    });
  }

  /* ---------- Highlight muc dang xem tren nav ---------- */
  var navAnchors = Array.prototype.slice.call(
    document.querySelectorAll('.nav__links a[href^="#"]')
  );
  var sections = navAnchors
    .map(function (a) {
      return document.querySelector(a.getAttribute("href"));
    })
    .filter(Boolean);

  if (sections.length && "IntersectionObserver" in window) {
    var spy = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          navAnchors.forEach(function (a) {
            a.classList.toggle(
              "is-active",
              a.getAttribute("href") === "#" + entry.target.id
            );
          });
        });
      },
      { rootMargin: "-45% 0px -50% 0px", threshold: 0 }
    );
    sections.forEach(function (s) {
      spy.observe(s);
    });
  }

  /* ---------- Hien dan noi dung khi cuon toi ---------- */
  var revealables = document.querySelectorAll("[data-reveal]");
  if (reduceMotion || !("IntersectionObserver" in window)) {
    revealables.forEach(function (el) {
      el.classList.add("is-in");
    });
  } else {
    var revealer = new IntersectionObserver(
      function (entries, obs) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          entry.target.classList.add("is-in");
          obs.unobserve(entry.target);
        });
      },
      { rootMargin: "0px 0px -8% 0px", threshold: 0.08 }
    );
    revealables.forEach(function (el) {
      revealer.observe(el);
    });
  }

  /* ---------- Bang chi tiet ky nang ---------- */
  var panel = document.getElementById("skillPanel");
  var elGroup = document.getElementById("skillGroup");
  var elName = document.getElementById("skillName");
  var elDetail = document.getElementById("skillDetail");
  var chips = document.querySelectorAll(".chip");

  function swapIn(el, text) {
    el.textContent = text;
    el.classList.remove("is-swap");
    void el.offsetWidth; // ep trinh duyet chay lai animation
    el.classList.add("is-swap");
  }

  chips.forEach(function (chip) {
    chip.addEventListener("click", function () {
      chips.forEach(function (c) {
        c.classList.remove("is-active");
      });
      chip.classList.add("is-active");

      swapIn(elGroup, chip.dataset.group || "");
      swapIn(elName, chip.dataset.name || "");
      swapIn(elDetail, chip.dataset.detail || "");
      if (panel) panel.classList.add("is-filled");
    });
  });

  /* ---------- Nut sao chep o phan lien he ---------- */
  document.querySelectorAll("[data-copy]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var value = btn.dataset.copy || "";
      var done = function () {
        btn.classList.add("is-done");
        btn.setAttribute("aria-label", btn.dataset.done || "Copied");
        setTimeout(function () {
          btn.classList.remove("is-done");
          btn.setAttribute("aria-label", btn.dataset.label || "Copy");
        }, 1600);
      };

      if (navigator.clipboard && window.isSecureContext) {
        navigator.clipboard.writeText(value).then(done).catch(function () {});
        return;
      }

      // Du phong cho trinh duyet cu / ket noi http
      var ta = document.createElement("textarea");
      ta.value = value;
      ta.style.position = "fixed";
      ta.style.opacity = "0";
      document.body.appendChild(ta);
      ta.select();
      try {
        document.execCommand("copy");
        done();
      } catch (err) {
        /* bo qua */
      }
      document.body.removeChild(ta);
    });
  });
})();
