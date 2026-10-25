(function () {
  var nav = document.getElementById("nav");
  function onScroll() { nav.classList.toggle("solid", window.scrollY > 60); }
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  var b = document.getElementById("burger"), d = document.getElementById("drawer");
  function close() { d.classList.remove("open"); b.setAttribute("aria-expanded", "false"); b.textContent = "Menu"; }
  b.addEventListener("click", function () {
    var open = d.classList.toggle("open");
    b.setAttribute("aria-expanded", open ? "true" : "false");
    b.textContent = open ? "Close" : "Menu";
    if (open) nav.classList.add("solid");
  });
  d.addEventListener("click", function (e) { if (e.target.tagName === "A") close(); });

  // Days until April 16, 2027 (Atlanta time, EDT)
  var cd = document.querySelector("[data-countdown]");
  if (cd) {
    var target = new Date("2027-04-16T00:00:00-04:00").getTime();
    var n = Math.max(0, Math.ceil((target - Date.now()) / 86400000));
    cd.textContent = String(n).padStart(3, "0");
  }

  // Price windows (Eastern time). Presale ends Nov 15, early bird Nov 16 - Dec 15, market from Dec 16.
  var now = Date.now();
  var windows = [
    { id: "presale", end: new Date("2026-11-15T23:59:59-05:00").getTime(), bar: "Register · Presale ends Nov 15", name: "Private Placement presale" },
    { id: "early", start: new Date("2026-11-16T00:00:00-05:00").getTime(), end: new Date("2026-12-15T23:59:59-05:00").getTime(), bar: "Register · Early bird ends Dec 15", name: "IPO early bird" },
    { id: "market", start: new Date("2026-12-16T00:00:00-05:00").getTime(), bar: "Register · April 16–18, 2027", name: "Market price" }
  ];
  var current = windows[2];
  for (var i = 0; i < windows.length; i++) {
    var w = windows[i];
    if ((!w.start || now >= w.start) && (!w.end || now <= w.end)) { current = w; break; }
  }
  var bar = document.getElementById("sticky-reg");
  if (bar) bar.textContent = current.bar;

  // Register page
  var tiers = document.querySelectorAll(".tier");
  if (tiers.length) {
    var idx = windows.indexOf(current);
    tiers.forEach(function (el) {
      var k = windows.map(function (w) { return w.id; }).indexOf(el.dataset.tier);
      var b = el.querySelector("[data-badge]");
      if (k === idx) { el.classList.add("current"); b.textContent = "Open now"; }
      else if (k < idx) { el.classList.add("past"); b.textContent = "Closed"; }
      else { b.textContent = "Opens " + (k === 1 ? "Nov 16" : "Dec 16"); }
    });
  }
})();
