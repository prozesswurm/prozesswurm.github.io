/* Weiche für alte Lernwerkstatt-Links.
   Früher lag die Lernwerkstatt direkt unter prozesswurm.github.io/. Geteilte Links wie
   #lektion=v07, #problem=…, #team=…, #lektion-der-woche oder Speicherlinks landen jetzt
   auf dieser Startseite und werden hier sofort in die Lernwerkstatt weitergereicht. */
(function () {
  var h = location.hash;
  if (h && h.length > 1 && !/^#(inhalt|nervt|titel|nervt-titel|wege-titel|duo-titel|kanaele-titel|newsletter-titel)$/.test(h)) {
    location.replace("lernwerkstatt/" + location.search + h);
  }
})();
