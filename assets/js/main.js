/* Prozesswurm – Bedienung aller Seiten. Kein Tracking, keine fremden Bibliotheken. */
(function () {
  "use strict";
  var doc = document;
  var root = doc.documentElement;
  var base = (doc.querySelector('link[rel="stylesheet"][href*="assets/css/style.css"]') || {}).getAttribute
    ? doc.querySelector('link[rel="stylesheet"][href*="assets/css/style.css"]').getAttribute("href").replace("assets/css/style.css", "")
    : "";

  /* Farbdarstellung: Hell, Dunkel oder automatisch nach Gerät */
  function readTheme() { try { return localStorage.getItem("pw-theme") || "auto"; } catch (e) { return "auto"; } }
  function applyTheme(value) {
    if (value === "light" || value === "dark") root.setAttribute("data-theme", value);
    else root.removeAttribute("data-theme");
    doc.querySelectorAll("[data-theme-set]").forEach(function (b) {
      b.setAttribute("aria-pressed", String(b.getAttribute("data-theme-set") === value));
    });
  }
  applyTheme(readTheme());
  doc.addEventListener("click", function (e) {
    var b = e.target.closest("[data-theme-set]");
    if (!b) return;
    var v = b.getAttribute("data-theme-set");
    try { localStorage.setItem("pw-theme", v); } catch (err) { /* ohne Speicher gilt die Wahl nur für diese Seite */ }
    applyTheme(v);
  });

  /* Menü auf dem Handy */
  var toggle = doc.querySelector(".menu-toggle");
  var nav = doc.getElementById("hauptmenue");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = toggle.getAttribute("aria-expanded") === "true";
      toggle.setAttribute("aria-expanded", String(!open));
      nav.setAttribute("data-open", String(!open));
    });
    doc.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && toggle.getAttribute("aria-expanded") === "true") {
        toggle.setAttribute("aria-expanded", "false");
        nav.setAttribute("data-open", "false");
        toggle.focus();
      }
    });
  }

  /* Vorher-Nachher-Regler */
  doc.querySelectorAll("[data-compare]").forEach(function (box) {
    var input = box.querySelector('input[type="range"]');
    if (!input) return;
    function update() {
      box.style.setProperty("--pos", input.value + "%");
      input.setAttribute("aria-valuetext", input.value < 35 ? "Mehr Vorher, Kuddelmuddel" : input.value > 65 ? "Mehr Nachher, Prozesswurm" : "Halb und halb");
    }
    input.addEventListener("input", update);
    update();
  });

  /* Bilderleiste blättern */
  doc.querySelectorAll("[data-gallery]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var list = btn.closest(".wrap").querySelector(".gallery");
      if (!list) return;
      var step = list.clientWidth * 0.8 * Number(btn.getAttribute("data-gallery"));
      var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
      list.scrollBy({ left: step, behavior: reduce ? "auto" : "smooth" });
    });
  });

  /* Reiter „Im Job“ / „Zu Hause“ (Pfeiltasten wie bei echten Reitern) */
  doc.querySelectorAll('[role="tablist"]').forEach(function (list) {
    var tabs = Array.prototype.slice.call(list.querySelectorAll('[role="tab"]'));
    function select(tab) {
      tabs.forEach(function (t) {
        var on = t === tab;
        t.setAttribute("aria-selected", String(on));
        t.tabIndex = on ? 0 : -1;
        var panel = doc.getElementById(t.getAttribute("aria-controls"));
        if (panel) panel.hidden = !on;
      });
      var more = list.parentNode.querySelector("[data-show-all]");
      if (more) {
        var panelId = tab.getAttribute("aria-controls");
        var p = doc.getElementById(panelId);
        more.setAttribute("data-show-all", panelId);
        more.hidden = !p || !p.querySelector("li[data-extra]") || p.classList.contains("show-all");
      }
    }
    tabs.forEach(function (t, i) {
      t.addEventListener("click", function () { select(t); });
      t.addEventListener("keydown", function (e) {
        var n = e.key === "ArrowRight" ? i + 1 : e.key === "ArrowLeft" ? i - 1 : null;
        if (n === null) return;
        e.preventDefault();
        var next = tabs[(n + tabs.length) % tabs.length];
        select(next); next.focus();
      });
    });
    var current = tabs.filter(function (t) { return t.getAttribute("aria-selected") === "true"; })[0] || tabs[0];
    setTimeout(function () { select(current); }, 0);
  });

  /* Lange Listen kürzen, „Alle anzeigen“ blendet den Rest ein */
  doc.querySelectorAll("[data-limit]").forEach(function (list) {
    var limit = Number(list.getAttribute("data-limit"));
    Array.prototype.forEach.call(list.children, function (li, i) { if (i >= limit) li.setAttribute("data-extra", ""); });
  });
  doc.querySelectorAll("[data-show-all]").forEach(function (btn) {
    var panel = doc.getElementById(btn.getAttribute("data-show-all"));
    if (panel && panel.querySelector("li[data-extra]") && !panel.hidden) btn.hidden = false;
    btn.addEventListener("click", function () {
      var p = doc.getElementById(btn.getAttribute("data-show-all"));
      if (!p) return;
      p.classList.add("show-all");
      btn.hidden = true;
      var first = p.querySelector("li[data-extra] a");
      if (first) first.focus();
    });
  });

  /* Hören und sehen: filtern nach Art, Thema und Titel */
  var mediaList = doc.getElementById("medienliste");
  if (mediaList) {
    var state = { art: "", kat: "", q: "" };
    var rows = Array.prototype.slice.call(mediaList.children);
    var count = doc.getElementById("medienanzahl");
    var empty = doc.getElementById("medienleer");
    var filterInput = doc.getElementById("medienfilter");
    var normText = function (s) { return s.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/ß/g, "ss"); };
    rows.forEach(function (r) { r._t = normText(r.textContent); });
    var apply = function () {
      var shown = 0;
      var q = normText(state.q.trim());
      rows.forEach(function (r) {
        var ok = (!state.art || r.getAttribute("data-art") === state.art) &&
                 (!state.kat || r.getAttribute("data-kat") === state.kat) &&
                 (!q || r._t.indexOf(q) > -1);
        r.hidden = !ok;
        if (ok) shown++;
      });
      count.textContent = shown === 1 ? "1 Titel" : shown + " Titel";
      empty.hidden = shown > 0;
    };
    doc.querySelectorAll("[data-art-set]").forEach(function (b) {
      b.addEventListener("click", function () {
        state.art = b.getAttribute("data-art-set");
        doc.querySelectorAll("[data-art-set]").forEach(function (x) { x.setAttribute("aria-pressed", String(x === b)); });
        apply();
      });
    });
    doc.querySelectorAll(".chip[data-kat]").forEach(function (b) {
      b.addEventListener("click", function () {
        state.kat = b.getAttribute("data-kat");
        doc.querySelectorAll(".chip[data-kat]").forEach(function (x) { x.setAttribute("aria-pressed", String(x === b)); });
        apply();
      });
    });
    if (filterInput) filterInput.addEventListener("input", function () { state.q = filterInput.value; apply(); });
    apply();
  }

  /* Begriffe von A bis Z: filtern */
  var termInput = doc.getElementById("begriffsfilter");
  if (termInput) {
    var termCards = Array.prototype.slice.call(doc.querySelectorAll(".term-card"));
    var groups = Array.prototype.slice.call(doc.querySelectorAll(".term-group"));
    var termCount = doc.getElementById("begriffsanzahl");
    var termEmpty = doc.getElementById("begriffsleer");
    var nt = function (s) { return s.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/ß/g, "ss"); };
    termCards.forEach(function (c) { c._t = nt(c.querySelector("h3").textContent); c._d = nt(c.textContent); });
    termInput.addEventListener("input", function () {
      var q = nt(termInput.value.trim()), n = 0;
      termCards.forEach(function (c) {
        var ok = !q || c._t.indexOf(q) > -1 || (q.length >= 4 && c._d.indexOf(q) > -1);
        c.hidden = !ok; if (ok) n++;
      });
      groups.forEach(function (g) { g.hidden = !g.querySelector(".term-card:not([hidden])"); });
      termCount.textContent = n === 1 ? "1 Begriff" : n + " Begriffe";
      termEmpty.hidden = n > 0;
    });
  }

  /* Sanftes Einblenden beim Scrollen */
  if ("IntersectionObserver" in window && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    var revealEls = doc.querySelectorAll(".journey li, .audience, .latest, .path-card, .pick, .value-grid li, .proof-list li");
    if (revealEls.length) {
      root.classList.add("js-reveal");
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("is-in"); io.unobserve(en.target); } });
      }, { rootMargin: "0px 0px -8% 0px" });
      revealEls.forEach(function (el, i) {
        el.classList.add("reveal");
        el.style.transitionDelay = (i % 4) * 60 + "ms";
        io.observe(el);
      });
      /* Sicherheitsnetz: nach dem Drucken oder bei Problemen alles zeigen */
      window.addEventListener("beforeprint", function () { revealEls.forEach(function (el) { el.classList.add("is-in"); }); });
    }
  }

  /* E-Mail-Adresse kopieren */
  doc.querySelectorAll("[data-copy]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var text = btn.getAttribute("data-copy");
      var done = function () { var old = btn.textContent; btn.textContent = "Kopiert"; setTimeout(function () { btn.textContent = old; }, 1600); };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(done, function () { selectText(btn.previousElementSibling); });
      } else { selectText(btn.previousElementSibling); }
    });
  });
  function selectText(el) {
    if (!el) return;
    var r = doc.createRange(); r.selectNodeContents(el);
    var s = window.getSelection(); s.removeAllRanges(); s.addRange(r);
  }

  /* Suche über alle Seiten */
  var dialog = doc.getElementById("suche");
  var field = doc.getElementById("suchfeld");
  var results = doc.getElementById("suchergebnisse");
  var hint = doc.getElementById("suchhinweis");
  var index = null;
  function loadIndex() {
    if (index) return Promise.resolve(index);
    return fetch(base + "suche.json").then(function (r) { return r.json(); }).then(function (d) { index = d; return d; })
      .catch(function () { index = []; return index; });
  }
  function norm(s) { return s.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/ß/g, "ss"); }
  function render(q) {
    results.textContent = "";
    hint.hidden = true;
    if (!q.trim()) return;
    var words = norm(q).split(/\s+/).filter(Boolean);
    /* Treffer am Wortanfang („hut“ findet „Hüte“, aber nicht „Datenschutz“);
       ab fünf Buchstaben auch mitten im Wort („management“ findet „Prozessmanagement“) */
    function hit(text, w) {
      if (w.length >= 5 && text.indexOf(w) > -1) return true;
      return text.split(/[^a-z0-9]+/).some(function (x) { return x.indexOf(w) === 0; });
    }
    var hits = index.map(function (p) {
      var titel = norm(p.titel);
      var hay = norm(p.titel + " " + p.text + " " + (p.stichworte || ""));
      var score = 0;
      words.forEach(function (w) { if (hit(hay, w)) score += hit(titel, w) ? 3 : 1; });
      return { p: p, score: score };
    }).filter(function (h) { return h.score >= words.length; }).sort(function (a, b) { return b.score - a.score; }).slice(0, 8);
    if (!hits.length) { hint.hidden = false; return; }
    hits.forEach(function (h) {
      var li = doc.createElement("li");
      var a = doc.createElement("a");
      a.href = /^https?:/.test(h.p.url) ? h.p.url : base + h.p.url;
      var t = doc.createElement("strong"); t.textContent = h.p.titel;
      var s = doc.createElement("small"); s.textContent = h.p.text;
      a.appendChild(t); a.appendChild(s); li.appendChild(a); results.appendChild(li);
    });
  }
  doc.querySelectorAll("[data-search-open]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      if (!dialog) return;
      loadIndex();
      if (typeof dialog.showModal === "function") dialog.showModal(); else dialog.setAttribute("open", "");
      field.value = ""; render(""); field.focus();
    });
  });
  if (field) {
    field.addEventListener("input", function () { loadIndex().then(function () { render(field.value); }); });
    /* Escape schließt die Suche sofort, auch wenn schon etwas eingetippt ist */
    field.addEventListener("keydown", function (e) { if (e.key === "Escape") { e.preventDefault(); dialog.close(); } });
  }
  if (dialog) dialog.addEventListener("click", function (e) { if (e.target === dialog) dialog.close(); });
  doc.addEventListener("keydown", function (e) {
    if (e.key === "/" && !/input|textarea/i.test((doc.activeElement || {}).tagName || "") && dialog && !dialog.open) {
      e.preventDefault(); doc.querySelector("[data-search-open]").click();
    }
  });

  /* Tempo: Seiten vorladen, sobald jemand auf einen Link zeigt */
  var prefetched = {};
  function prefetch(a) {
    if (!a || !a.href || a.target === "_blank") return;
    var url;
    try { url = new URL(a.href, location.href); } catch (e) { return; }
    if (url.origin !== location.origin || url.hash && url.pathname === location.pathname) return;
    if (prefetched[url.href]) return;
    prefetched[url.href] = true;
    var l = doc.createElement("link"); l.rel = "prefetch"; l.href = url.href; doc.head.appendChild(l);
  }
  ["mouseover", "focusin", "touchstart"].forEach(function (ev) {
    doc.addEventListener(ev, function (e) { prefetch(e.target.closest && e.target.closest("a[href]")); }, { passive: true });
  });

  /* Tempo: eigener Zwischenspeicher, nur auf der echten Seite */
  if ("serviceWorker" in navigator && /prozesswurm\.de$/.test(location.hostname)) {
    window.addEventListener("load", function () { navigator.serviceWorker.register(base + "sw.js").catch(function () {}); });
  }
})();
