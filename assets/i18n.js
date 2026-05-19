/*!
 * Rivadent i18n runtime
 * =====================
 *
 * Statik TR (kök) + EN (`/en/`) ayna yapısı üzerinde çalışan dil
 * davranışları:
 *
 *   1. Dil tespiti: önce kullanıcı tercihi (`localStorage.rd_lang`), yoksa
 *      `navigator.language` (TR ile başlıyorsa TR, değilse EN), yoksa default
 *      TR.
 *   2. Otomatik yönlendirme: ilk ziyarette (kayıtlı tercih yoksa) ve mevcut
 *      sayfa kullanıcının dilinden FARKLI ise, sayfa <head>'inde tanımlı
 *      hreflang alternate URL'sine yönlendir. Sadece tarayıcı dilinden farklı
 *      olduğunda; aynı zamanda EN karşılığı VARSA. Bir kere yönlendirme
 *      yaptıktan sonra session boyunca tekrarlamaz.
 *   3. Akıllı dil değiştirici: `.lang-options a` linkleri hard-coded değil;
 *      runtime'da gerçek karşı-dil URL'sine bağlanır. Kullanıcı tıklayınca
 *      tercih `localStorage`'a yazılır → sonraki ziyaretlerde otomatik
 *      yönlendirme yapılmaz.
 *   4. Domain normalizasyonu: HTML dosyaları rivadent.com.tr'ye hardcode
 *      edilmiştir. Farklı bir domaine deploy edildiğinde canonical, hreflang,
 *      og:url, og:image ve JSON-LD URL'leri otomatik olarak gerçek origin'e
 *      güncellenir.
 *
 * SEO sinyali tamamen sunucu tarafı meta'larla (`canonical`, `hreflang`)
 * sağlanır; bu script yalnız kullanıcı deneyimi içindir.
 */
(function () {
  "use strict";

  var CANONICAL_ORIGIN = "https://rivadent.com.tr"; // HTML'e yazılı hardcode origin
  var STORAGE_KEY = "rd_lang";        // kalıcı kullanıcı tercihi
  var SESSION_FLAG = "rd_lang_redirected"; // session içinde tek redirect

  /* ------------------------------------------------------------------ */
  /* 4. Domain normalizasyonu                                            */
  /* ------------------------------------------------------------------ */
  function patchDomain() {
    var live = window.location.origin;
    if (!live || live === CANONICAL_ORIGIN) return; // aynı domain, bir şey yapma

    var escaped = CANONICAL_ORIGIN.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
    var re = new RegExp(escaped, "g");

    function swap(url) {
      return url ? url.replace(re, live) : url;
    }

    // <link rel="canonical">
    var canon = document.querySelector('link[rel="canonical"]');
    if (canon) canon.setAttribute("href", swap(canon.getAttribute("href")));

    // <link rel="alternate" hreflang="*">
    var alts = document.querySelectorAll('link[rel="alternate"]');
    for (var i = 0; i < alts.length; i++) {
      alts[i].setAttribute("href", swap(alts[i].getAttribute("href")));
    }

    // <meta property="og:url">
    var ogUrl = document.querySelector('meta[property="og:url"]');
    if (ogUrl) ogUrl.setAttribute("content", swap(ogUrl.getAttribute("content")));

    // <meta property="og:image">
    var ogImg = document.querySelector('meta[property="og:image"]');
    if (ogImg) ogImg.setAttribute("content", swap(ogImg.getAttribute("content")));

    // <meta name="twitter:image">
    var twImg = document.querySelector('meta[name="twitter:image"]');
    if (twImg) twImg.setAttribute("content", swap(twImg.getAttribute("content")));

    // JSON-LD blokları
    var jsonlds = document.querySelectorAll('script[type="application/ld+json"]');
    for (var j = 0; j < jsonlds.length; j++) {
      jsonlds[j].textContent = jsonlds[j].textContent.replace(re, live);
    }
  }

  function currentLocale() {
    var lang = (document.documentElement.getAttribute("lang") || "").toLowerCase();
    return lang.indexOf("en") === 0 ? "en" : "tr";
  }

  function readAlternates() {
    // <head>'deki <link rel="alternate" hreflang="..."> etiketlerini map'le.
    // Eleventy / Python injector tarafından inject_i18n.py ile basılıyor.
    var map = {};
    var links = document.querySelectorAll('link[rel="alternate"][hreflang]');
    for (var i = 0; i < links.length; i++) {
      var lang = (links[i].getAttribute("hreflang") || "").toLowerCase();
      var href = links[i].getAttribute("href");
      if (!lang || lang === "x-default" || !href) continue;
      map[lang] = href;
    }
    return map;
  }

  function getStored() {
    try { return localStorage.getItem(STORAGE_KEY); } catch (_) { return null; }
  }
  function setStored(value) {
    try { localStorage.setItem(STORAGE_KEY, value); } catch (_) {}
  }
  function getSessionFlag() {
    try { return sessionStorage.getItem(SESSION_FLAG); } catch (_) { return null; }
  }
  function setSessionFlag() {
    try { sessionStorage.setItem(SESSION_FLAG, "1"); } catch (_) {}
  }

  function detectPreferredLocale() {
    // 1) Kullanıcı tercihi varsa onu kullan
    var stored = getStored();
    if (stored === "tr" || stored === "en") return stored;
    // 2) Tarayıcı diline bak
    var nav = (navigator.language || navigator.userLanguage || "").toLowerCase();
    if (nav.indexOf("tr") === 0) return "tr";
    if (nav.indexOf("en") === 0) return "en";
    // 3) Default
    return "tr";
  }

  function rewriteSwitcher(altMap, currentLang) {
    var targetLang = currentLang === "tr" ? "en" : "tr";
    var targetHref = altMap[targetLang];
    var anchors = document.querySelectorAll(".lang-options a");
    if (!anchors.length) return;

    for (var i = 0; i < anchors.length; i++) {
      var a = anchors[i];
      if (targetHref) {
        a.setAttribute("href", targetHref);
        a.setAttribute("hreflang", targetLang);
        a.removeAttribute("data-no-alt");
      } else {
        // Karşı dilde eşdeğer yok → buton görünür kalsın ama uyarı ver
        a.setAttribute("data-no-alt", "1");
        a.addEventListener("click", function (e) {
          e.preventDefault();
        });
      }
      a.addEventListener("click", (function (lang) {
        return function () {
          if (lang) setStored(lang);
        };
      })(targetLang));
    }
  }

  function maybeAutoRedirect(altMap, currentLang) {
    // Tek tur yönlendirme (loop guard)
    if (getSessionFlag()) return;
    // Kullanıcı tercihi varsa otomatik karışma
    if (getStored()) return;

    var preferred = detectPreferredLocale();
    if (preferred === currentLang) return;          // zaten doğru dildeyiz
    var target = altMap[preferred];
    if (!target) return;                            // karşı dilde eşdeğer yok

    setSessionFlag();
    // Geçmişi kirletme
    location.replace(target);
  }

  function init() {
    patchDomain();                       // önce domain'i normalize et
    var altMap = readAlternates();       // sonra güncel href'leri oku
    var lang = currentLocale();
    rewriteSwitcher(altMap, lang);
    maybeAutoRedirect(altMap, lang);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
