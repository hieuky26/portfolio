/* Chuyen dong: GSAP + Lenis (hero hien bang CSS, khong cho JS), hieu ung kieu React Bits viet lai bang JS thuong.
   - Lenis: cuon muot, dong bo voi ScrollTrigger.
   - Count Up: so lieu o muc Cong cu dem tu 0 khi cuon toi.
   - Magnet: nut chinh va icon mang xa hoi hut nhe theo chuot.
   - Spotlight Card: vet sang ho phach theo chuot tren cac the.
   Tat het khi nguoi dung chon giam chuyen dong, hoac thu vien khong tai duoc. */
(function () {
  "use strict";

  var gsap = window.gsap;
  if (!gsap) return;
  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

  var ScrollTrigger = window.ScrollTrigger;
  if (ScrollTrigger) gsap.registerPlugin(ScrollTrigger);

  var finePointer = window.matchMedia("(hover: hover) and (pointer: fine)").matches;
  var HEADER = 72;

  /* ---------- Lenis: cuon muot ---------- */
  var lenis = null;
  if (window.Lenis) {
    lenis = new window.Lenis({ lerp: 0.1, wheelMultiplier: 1 });
    if (ScrollTrigger) lenis.on("scroll", ScrollTrigger.update);
    gsap.ticker.add(function (time) { lenis.raf(time * 1000); });
    gsap.ticker.lagSmoothing(0);

    // Link "#muc" cuon muot qua Lenis (tru link "bo qua" de giu dung hanh vi focus cho ban phim)
    document.addEventListener("click", function (e) {
      var a = e.target.closest('a[href^="#"]');
      if (!a || a.classList.contains("skip")) return;
      var id = a.getAttribute("href");
      var target = id === "#top" ? 0 : document.querySelector(id);
      if (target === null) return;
      e.preventDefault();
      lenis.scrollTo(target, { offset: target === 0 ? 0 : -HEADER });
      history.pushState(null, "", id);
    });
  }

  /* ---------- Parallax nhe cho anh chan dung ---------- */
  var portrait = document.querySelector(".portrait img");
  if (portrait && ScrollTrigger) {
    gsap.fromTo(portrait, { yPercent: 6 }, {
      yPercent: -6, ease: "none",
      scrollTrigger: { trigger: ".portrait", start: "top bottom", end: "bottom top", scrub: true }
    });
  }

  /* ---------- Count Up: so lieu ---------- */
  if (ScrollTrigger) {
    document.querySelectorAll(".metrics dd").forEach(function (dd) {
      var original = dd.textContent.trim();
      var m = original.match(/^(\D*?)(\d+(?:\.\d+)?)(.*)$/);   // "~7.8k" -> "~", "7.8", "k"
      if (!m) return;
      var end = parseFloat(m[2]);
      var decimals = (m[2].split(".")[1] || "").length;
      var counter = { v: 0 };
      dd.textContent = m[1] + (0).toFixed(decimals) + m[3];
      gsap.to(counter, {
        v: end, duration: 1.6, ease: "power2.out",
        scrollTrigger: { trigger: dd, start: "top 90%", once: true },
        onUpdate: function () { dd.textContent = m[1] + counter.v.toFixed(decimals) + m[3]; },
        onComplete: function () { dd.textContent = original; }
      });
    });
  }

  if (!finePointer) return;

  /* ---------- Magnet: nut chinh + icon mang xa hoi ---------- */
  document.querySelectorAll(".btn.primary, .social a").forEach(function (el) {
    var xTo = gsap.quickTo(el, "x", { duration: 0.5, ease: "power3.out" });
    var yTo = gsap.quickTo(el, "y", { duration: 0.5, ease: "power3.out" });
    el.addEventListener("pointermove", function (e) {
      var r = el.getBoundingClientRect();
      xTo((e.clientX - (r.left + r.width / 2)) * 0.3);
      yTo((e.clientY - (r.top + r.height / 2)) * 0.3);
    });
    el.addEventListener("pointerleave", function () { xTo(0); yTo(0); });
  });

  /* ---------- Spotlight Card: vet sang theo chuot ---------- */
  document.querySelectorAll(".panel, .tile, .case, .edu").forEach(function (card) {
    card.classList.add("spot");
    card.addEventListener("pointermove", function (e) {
      var r = card.getBoundingClientRect();
      card.style.setProperty("--mx", (e.clientX - r.left) + "px");
      card.style.setProperty("--my", (e.clientY - r.top) + "px");
    });
  });
})();
