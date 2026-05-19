@ -0,0 +1,190 @@
# RivaDent Statik Site — Workspace Skills

## Proje Özeti
`https://rivadent.com.tr/` adresinin tam statik HTML/CSS/JS kopyası.  
Backend yoktur; tüm formlar WhatsApp'a yönlendirilir. Statik hosting'e (Netlify, GitHub Pages vb.) doğrudan deploy edilebilir.

---

## Kritik Değerler

| Değişken | Değer |
|---|---|
| `ROOT` | `c:\Users\omerc\CascadeProjects\whatsappBot\rivadentTransfer` |
| `SITE` | `ROOT/site` |
| `BASE_URL` | `https://rivadent.com.tr` |
| Lokal test | `python -m http.server 8765 --directory site` → `http://localhost:8765` |

### WhatsApp Numaraları
| Klinik | WhatsApp |
|---|---|
| RivaDent Atakum | `905079442275` |
| RivaDent İlkadım | `905522224285` |
| RivaDent Maltepe | `905413871738` |

---

## Klasör Yapısı

```
site/
├── index.html                 ← Anasayfa (TR)
├── 404.html
├── sitemap.xml                ← seo_boost.py tarafından üretilir
├── robots.txt                 ← seo_boost.py tarafından üretilir
├── assets/
│   ├── front/                 ← CSS, JS, fontlar, logo, şekiller
│   │   └── js/vendor/ajax.js  ← Eski backend AJAX çağrıları (artık override edilmiş)
│   ├── uploads/               ← Tüm sayfa görselleri (hash.jpg formatı)
│   ├── i18n.js                ← Dil değiştirici (TR↔EN) localStorage mantığı
│   └── hekim-modal.js         ← Hekim sayfası "Hızlı Soru Sor" → WhatsApp yönlendirmesi
├── en/                        ← Tüm İngilizce sayfa mirroru (TR ile birebir yapı)
├── hekim/                     ← 18 doktor profil sayfası
├── en/hekim/                  ← Aynı 18 doktor EN versiyonu
├── tedavi/                    ← 10 tedavi sayfası
├── blog/                      ← Blog yazıları + kategori + tag sayfaları
├── poliklinikler/             ← 3 şube sayfası
├── randevu-al/index.html      ← Randevu formu (WhatsApp entegreli, inline script)
├── hekimlerimiz/              ← Tüm hekimler listesi
├── iletisim/
├── hakkimizda/
├── anlasmali-kurumlar/
├── sozlesme/                  ← kvkk, acik-riza, saglik-turizmi
└── cocuk-dis/

tools/
├── seo_boost.py               ← ANA ARAÇ — idempotent, tüm SEO + footer + sitemap
├── inject_i18n.py             ← hreflang / canonical meta enjeksiyonu
├── expand_clinic_names.py     ← "RivaDent X" → "RivaDent X Diş Kliniği" (içerik alanları)
├── fix_hekim_modal.py         ← Hekim sayfalarına data-wa + hekim-modal.js ekler
├── update_dates.py            ← "Son Güncelleme Tarihi" / "Last Updated" günceller
└── crawl.py / crawl_admin.py  ← Canlı siteden yeniden mirror alma (nadiren kullanılır)
```

---

## Dil Mimarisi (i18n)

- TR sayfaları: `site/**` → `<html lang="tr">`
- EN sayfaları: `site/en/**` → `<html lang="en">`
- Dil değiştirici: `localStorage` anahtarı `rd_lang` (`"tr"` veya `"en"`)
- SessionStorage flag: `rd_lang_redirected` (sonsuz yönlendirme döngüsünü önler)
- `assets/i18n.js` tüm sayfalarda `<!-- i18n:script -->` bloğuna eklenir
- hreflang/canonical meta blokları `<!-- seo:start --> ... <!-- seo:end -->` arasında

---

## Form Mantığı

### Randevu Formu (`randevu-al/index.html`)
- Form ID: `#infoMeeting`
- `ajax.js` override: `randevu-al/index.html` içinde inline `<script>` bloğu
- Klinik seçilince hekim dropdown statik olarak doldurulur (backend yok)
- Submit → KVKK kontrolü → WhatsApp `api.whatsapp.com/send/?phone=...&text=...`

### Hekim "Hızlı Soru Sor" Modalı (tüm `hekim/**/index.html`)
- Form ID: `#infoQuestion`
- Modal ID: `#exampleModal`
- Override: `assets/hekim-modal.js` (tüm hekim sayfalarında referanslanır)
- Her hekim sayfasında `<div id="hekim-wa-data" data-wa="..." data-clinic="...">` mevcut
- Klinik → WA eşleşmesi (slug bazlı, `fix_hekim_modal.py` tarafından eklenir):
  - Atakum slugları → `905079442275`
  - İlkadım slugları → `905522224285`
  - Maltepe slugları → `905413871738`
- `Uzm. Dr. Sevgin İbiş Tüfenk` iki klinikte de çalışır:
  - `uzm-dr-sevgin-ibis-tufenk` → Atakum
  - `uzm-dr-sevgin-ibis-tufenk-29` → İlkadım

---

## SEO Yapısı

### `seo_boost.py` ne yapar (idempotent, 5 adım)
1. Sağlık Turizmi sayfası oluşturur (TR + EN)
2. Tüm sayfalarda SEO meta + footer + Bydesign cleanup + `html lang` düzeltmesi
3. `sitemap.xml` üretir (156 URL, hreflang dahil, `404.html` ve `yonetim-paneli/` hariç)
4. `robots.txt` yazar
5. Tüm `<img alt="">` boş alt'ları SEO-uyumlu metinlerle doldurur (846 görsel)

### Görsel Alt Kuralları (`seo_boost.py` içinde `fix_image_alts`)
| Bağlam | Alt metni |
|---|---|
| `shape/*.png/svg`, `live.png` | `""` bırakılır (dekoratif) |
| `logo-wht.svg` | `RivaDent Diş Kliniği Logo` / `RivaDent Dental Clinic Logo` |
| `.treatment-img a[href]` | Tedavi adı slug'dan → map |
| `.blog-img` | Karşı `h3.title` metninden |
| `a[data-fancybox]` | `{klinik} Klinik Fotoğrafı` |
| `.treatment-detail-img` | Sayfa H1 + ` \| RivaDent` |
| `<p>` içi içerik görseli | Önceki `<h3>` + ` \| RivaDent` |

### Klinik İsmi Genişletme (`expand_clinic_names.py`)
- İçerik alanlarında (h1-h4, p.line-2, span.footer-title): `RivaDent X` → `RivaDent X Diş Kliniği`
- `<a>` tag linkleri (nav) **dokunulmaz**
- EN: `Dental Clinic`, TR: `Diş Kliniği`

---

## Hekim → Klinik Eşleşmesi

| Klinik | Hekimler |
|---|---|
| **Atakum** | Prof. Dr. İbrahim Duran, Dr. Erman Canlı, Uzm. Dt. Mesut Köksal, Uzm. Dt. Çağla Gül Gürkan, Dr. Dt. Esra Duran, Uzm. Dr. Sevgin İbiş Tüfenk, Dt. Hüseyin Karacabey, Dt. Yusuf Akpınar |
| **İlkadım** | Doç. Dr. Erhan Sarı, Dt. Mustafa Özdemir, Dt. Seray Tan, Dt. Osman Kılıç, Uzm. Dr. Sevgin İbiş Tüfenk |
| **Maltepe** | Dr. Dt. Sina Yıldırım, Dt. Başak Tımarcıoğlu, Dt. Sultan Taş, Dr. Dt. Miray Yıldırım, Dt. Muhammet Alptekin Özbek |

---

## Footer Yapısı

Her sayfada iki footer bloğu:
1. **Desktop** (`.d-none .d-lg-flex`) — yan yana sütunlar
2. **Mobile** (`.d-lg-none .d-block`) — accordion

Footer bloğunda şunlar bulunur:
- 3 klinik accordion (Atakum, İlkadım, Maltepe) — telefon, WA, harita
- Yasal accordion (KVKK, Açık Rıza, Sağlık Turizmi)
- Attribution span: `<span class="footer-attribution">RivaDent tarafından tasarlanmıştır</span>` (TR) / `Designed by RivaDent` (EN)
- "Son Güncelleme Tarihi: GG.AA.YYYY" — `update_dates.py` ile güncellenir

---

## HTML Düzenleme Kuralları

- **Mümkünse regex** ile orijinal HTML formatını koru (BS4 serialization kaçın)
- İdempotent yaz: marker comment (`<!-- seo:start -->`, `id="hekim-wa-data"` vb.) var mı kontrol et
- `assets/` ve `yonetim-paneli/` klasörlerini atla (artık yönetim paneli yok)
- EN sayfaları `rel.startswith("en/")` ile tespit et

---

## Yaygın Görevler

| Görev | Araç |
|---|---|
| Genel SEO güncellemesi | `python tools/seo_boost.py` |
| hreflang / canonical enjeksiyonu | `python tools/inject_i18n.py` |
| Klinik isimlerini genişlet | `python tools/expand_clinic_names.py` |
| Hekim modal WA güncelle | `python tools/fix_hekim_modal.py` |
| Tarih güncelle | `python tools/update_dates.py` |
| Lokal test | `python -m http.server 8765 --directory site` |

---

## Yasaklı / Dikkatli Olunacak Şeyler

- `ajax.js` içindeki handler'ları silme — sadece override et (inline script veya ayrı JS ile)
- Nav `<a>` linklerinin metin içeriğini değiştirme (çok uzar)
- JSON-LD `name` alanlarını elle değiştirme — `seo_boost.py` zaten yönetiyor
- `sitemap.xml` ve `robots.txt`'i elle yazma — `seo_boost.py` üretir
- `<html lang>` attribute'unu atlama — TR/EN ayrımı kritik (i18n.js'in bağımlılığı)
- `assets/` klasörüne HTML dışı dosya ekleme (crawl'dan gelir, dokunma)

---

## Bağımlılıklar

```
Python 3.11+
beautifulsoup4   (pip install beautifulsoup4)   ← seo_boost.py fix_image_alts + expand_clinic_names
```
jQuery, Bootstrap 5, SweetAlert2, Fancybox, Swiper — CDN değil, `assets/` içinde local kopya.