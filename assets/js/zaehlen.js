/* Prozesswurm – Besucherzählung ohne Zugriff auf dein Gerät.
   Ersetzt das fertige GoatCounter-Skript. Der Unterschied: Dieses Skript liest
   nichts aus deinem Browser-Speicher (kein localStorage, keine Cookies) und
   fragt keine Geräteangaben wie die Bildschirmgröße ab. Es schickt nur:
   - welche Seite aufgerufen wurde (ohne ?-Teil und ohne #-Teil),
   - den Seitentitel,
   - von welcher Seite du kamst,
   - bei Klick-Ereignissen deren Namen.
   Gezählt wird bei GoatCounter (prozesswurm.goatcounter.com).
   Bestehende Aufrufe von window.goatcounter.count({...}) funktionieren weiter. */
(function () {
  "use strict";
  var tag = document.querySelector("script[data-goatcounter]");
  var endpoint = tag ? tag.getAttribute("data-goatcounter") : "";
  var settings = {};
  try { settings = JSON.parse((tag && tag.getAttribute("data-goatcounter-settings")) || "{}"); } catch (e) { settings = {}; }

  function erlaubt() {
    if (!endpoint || !/^https:\/\/[a-z0-9-]+\.goatcounter\.com\/count$/.test(endpoint)) return false;
    if (!/(^|\.)prozesswurm\.de$/.test(location.hostname)) return false;   // keine Zählung in Vorschau und Tests
    if (window.top !== window.self) return false;                           // nicht in fremden Rahmen
    if (document.visibilityState === "prerender") return false;
    return true;
  }

  function senden(daten) {
    if (!erlaubt()) return;
    var teile = [];
    for (var k in daten) if (daten[k] !== undefined && daten[k] !== "") teile.push(k + "=" + encodeURIComponent(daten[k]));
    teile.push("rnd=" + Math.random().toString(36).slice(2, 7));
    var url = endpoint + "?" + teile.join("&");
    var img = new Image(1, 1);
    img.alt = "";
    img.referrerPolicy = "strict-origin-when-cross-origin";
    img.src = url;
  }

  function zaehlen(v) {
    v = v || {};
    var ereignis = !!v.event;
    senden({
      p: v.path || location.pathname || "/",
      t: v.title || document.title,
      r: ereignis ? "" : (v.referrer !== undefined ? v.referrer : document.referrer),
      e: ereignis ? "true" : ""
    });
  }

  /* Aufräumen: Alte Cookies aus der Zeit mit Google Sites und Google Analytics
     (bis Oktober 2026) liegen bei manchen Besuchern noch im Browser. Die Seite
     wertet sie nicht aus, sie schaut nur nach dem Namen und löscht sie. */
  try {
    if (document.cookie) {
      var alt = /^(_ga|_gid|_gat|SITES_|NID$)/;
      document.cookie.split(";").forEach(function (c) {
        var name = c.split("=")[0].trim();
        if (!alt.test(name)) return;
        ["", "; domain=prozesswurm.de", "; domain=.prozesswurm.de", "; domain=www.prozesswurm.de"].forEach(function (d) {
          document.cookie = name + "=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/" + d;
        });
      });
    }
  } catch (e) { /* nichts zu tun */ }

  window.goatcounter = window.goatcounter || {};
  window.goatcounter.count = zaehlen;

  if (!settings.no_onload) {
    if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", function () { zaehlen(); });
    else zaehlen();
  }
})();
