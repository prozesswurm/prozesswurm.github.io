/* Prozesswurm – Farbdarstellung für Website UND Lernwerkstatt (eine Datei für beide, seit 15.11.2026).
   Die Wahl (Hell, Dunkel, Automatisch nach Gerät) gilt überall auf prozesswurm.de und in allen Tabs.
   Läuft im Kopf der Seite, damit nichts aufblitzt. Bedienelemente:
   - [data-theme-set="light|auto|dark"]  feste Auswahl (Fußzeile, Mein Stand)
   - [data-theme-cycle]                   Knopf oben in der Kopfzeile, wechselt Automatisch → Hell → Dunkel */
(function () {
  "use strict";
  var KEY = "pw-theme";
  var root = document.documentElement;
  var ORDER = ["auto", "light", "dark"];
  var NAME = { auto: "Automatisch", light: "Hell", dark: "Dunkel" };

  function read() {
    try { var v = localStorage.getItem(KEY); return v === "light" || v === "dark" ? v : "auto"; }
    catch (e) { return "auto"; }
  }
  function sync(v) {
    var i, list = document.querySelectorAll("[data-theme-set]");
    for (i = 0; i < list.length; i++) list[i].setAttribute("aria-pressed", String(list[i].getAttribute("data-theme-set") === v));
    list = document.querySelectorAll("[data-theme-cycle]");
    for (i = 0; i < list.length; i++) {
      list[i].setAttribute("data-current", v);
      list[i].setAttribute("aria-label", "Darstellung: " + NAME[v] + ". Antippen zum Wechseln");
      list[i].setAttribute("title", "Darstellung: " + NAME[v]);
    }
  }
  function apply(v) {
    if (v === "light" || v === "dark") root.setAttribute("data-theme", v);
    else root.removeAttribute("data-theme");
    sync(v);
  }
  function set(v) {
    try { localStorage.setItem(KEY, v); } catch (e) { /* ohne Speicher gilt die Wahl nur für diese Seite */ }
    apply(v);
  }

  apply(read());
  document.addEventListener("DOMContentLoaded", function () { sync(read()); });
  document.addEventListener("click", function (e) {
    var t = e.target && e.target.closest ? e.target.closest("[data-theme-set],[data-theme-cycle]") : null;
    if (!t) return;
    if (t.hasAttribute("data-theme-set")) { set(t.getAttribute("data-theme-set")); return; }
    var now = root.getAttribute("data-theme") || "auto";
    set(ORDER[(ORDER.indexOf(now) + 1) % ORDER.length]);
  });
  /* Wahl in einem anderen Tab geändert (z. B. Website offen, Lernwerkstatt daneben) */
  window.addEventListener("storage", function (e) { if (e.key === KEY) apply(read()); });
})();
