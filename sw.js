/* Prozesswurm – Zwischenspeicher im Browser.
   Schriften, Aussehen und Bilder kommen beim zweiten Besuch sofort aus dem Speicher.
   Seiten selbst werden immer frisch geholt (damit neue Montags-Wurm-Ausgaben sofort da sind)
   und nur ohne Netz aus dem Speicher gezeigt.
   Bei jeder Änderung an CSS oder JS: VERSION hochzählen. */
const VERSION = "pw-2026-10-29-5";
const CORE = [
  "./",
  "assets/css/style.css",
  "assets/js/main.js",
  "assets/js/theme.js",
  "assets/fonts/atkinson-hyperlegible-latin-400-normal.woff2",
  "assets/fonts/atkinson-hyperlegible-latin-700-normal.woff2",
  "assets/fonts/bricolage-grotesque-latin-800-normal.woff2",
  "assets/img/prozesswurm.webp",
  "suche.json"
];

self.addEventListener("install", (event) => {
  event.waitUntil(caches.open(VERSION).then((c) => c.addAll(CORE)).then(() => self.skipWaiting()));
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((keys) => Promise.all(keys.filter((k) => k !== VERSION).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", (event) => {
  const req = event.request;
  const url = new URL(req.url);
  if (req.method !== "GET" || url.origin !== self.location.origin) return;
  // Lernwerkstatt und Newsletter-Archiv regeln sich selbst
  if (url.pathname.startsWith("/lernwerkstatt/") || url.pathname.startsWith("/newsletter/")) return;

  // Seiten: erst Netz, dann Speicher
  if (req.mode === "navigate") {
    event.respondWith(
      fetch(req).then((res) => {
        const copy = res.clone();
        caches.open(VERSION).then((c) => c.put(req, copy));
        return res;
      }).catch(() => caches.match(req).then((r) => r || caches.match("./")))
    );
    return;
  }

  // Alles andere: sofort aus dem Speicher, im Hintergrund auffrischen
  event.respondWith(
    caches.match(req).then((cached) => {
      const fresh = fetch(req).then((res) => {
        if (res.ok) { const copy = res.clone(); caches.open(VERSION).then((c) => c.put(req, copy)); }
        return res;
      }).catch(() => cached);
      return cached || fresh;
    })
  );
});
