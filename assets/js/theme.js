/* Gewählte Farbdarstellung sofort setzen, bevor die Seite gezeichnet wird (kein Aufblitzen). */
try {
  var t = localStorage.getItem("pw-theme");
  if (t === "light" || t === "dark") document.documentElement.setAttribute("data-theme", t);
} catch (e) { /* ohne Speicher: Gerät entscheidet */ }
