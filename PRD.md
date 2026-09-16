# PRD — RivaDent Web Sitesi
**Versiyon:** 1.0  
**Tarih:** 2026-09-16  
**Hazırlayan:** Claude Code (Ömer Can Uyar ile birlikte)

---

## 1. Ürün Özeti

RivaDent web sitesi, Samsun (Atakum, İlkadım) ve İstanbul (Maltepe) şehirlerinde faaliyet gösteren RivaDent Ağız ve Diş Sağlığı Polikliniği'nin kurumsal dijital varlığıdır. Site, potansiyel hastaları bilgilendirmeyi, randevu almalarını kolaylaştırmayı ve arama motorlarında görünürlüğü artırmayı hedefler.

**Canlı URL:** https://rivadent.com.tr  
**Diller:** Türkçe (birincil) + İngilizce (sağlık turizmi hedef kitlesi)  
**Altyapı:** Statik HTML/CSS/JS (Bootstrap 5, Swiper.js, WOW.js, Fancybox)

---

## 2. Hedefler

| # | Hedef | Başarı Kriteri |
|---|-------|---------------|
| 1 | Organik arama trafiğini artırmak | "Samsun diş kliniği", "Atakum diş hekimi", "Maltepe diş hekimi" sorgularında ilk sayfa |
| 2 | Randevu dönüşüm oranını artırmak | Ziyaretçilerin en az %3'ü form dolduruyor |
| 3 | Sağlık turizmi hastası çekmek | İngilizce sayfalar Google'da indeksleniyor, EN trafik oluşuyor |
| 4 | Kurumsal güven inşa etmek | Doktor profilleri, sertifikalar ve hasta bilgilendirme içerikleriyle otorite |

---

## 3. Hedef Kitle

### 3.1 Birincil — Yerli Hasta
- Samsun (Atakum, İlkadım) ve İstanbul (Maltepe/Bağdat Caddesi) çevresindeki bireyler
- Diş tedavisi, implant, ortodonti veya estetik diş işlemleri arayanlar
- Mobil cihaz kullanımı yüksek

### 3.2 İkincil — Sağlık Turizmi Hastası
- Türkiye'ye dental tedavi için gelen yabancı uyruklu hastalar
- İngilizce içerik + Sağlık Turizmi Yetki Belgesi ile hedefleniyor
- Arama: "dental implant Turkey", "orthodontics Turkey"

### 3.3 Üçüncül — Sigorta / Anlaşmalı Kurum Çalışanları
- SGK, özel sağlık sigortası veya kurumsal anlaşma kapsamındaki hastalar
- Anlaşmalı Kurumlar sayfası üzerinden bilgi alıyor

---

## 4. Mevcut Site Yapısı

### 4.1 Sayfa Hiyerarşisi

```
rivadent.com.tr/
├── index.html                          # Anasayfa
├── hakkimizda/                         # Hakkımızda
├── hekimlerimiz/                       # Tüm doktor listesi
├── hekim/
│   ├── prof-dr-ibrahim-duran/
│   ├── doc-dr-erhan-sari/
│   ├── dr-erman-canli/
│   ├── uzm-dt-mesut-koksal/
│   ├── uzm-dt-cagla-gul-gurkan/
│   ├── dr-dt-esra-duran/
│   ├── uzm-dr-sevgin-ibis-tufenk/
│   ├── dt-huseyin-karacabey/
│   ├── dt-yusuf-akpinar/
│   ├── doc-dr-erhan-sari/
│   ├── dt-mustafa-ozdemir/
│   ├── dt-seray-tan/
│   ├── dr-dt-sina-yildirim/
│   ├── dr-dt-miray-yildirim/
│   ├── dt-basak-timarcioglu/
│   ├── dt-aleyna-beray-kidak/
│   └── dt-muhammet-alptekin-ozbek/
├── poliklinikler/
│   ├── rivadent-atakum/
│   ├── rivadent-ilkadim/
│   └── rivadent-maltepe/
├── tedavi/
│   ├── agiz-dis-ve-cene-cerrahisi/
│   ├── protez-dis/
│   ├── restoratif-dis-tedavisi/
│   ├── dis-beyazlatma/
│   ├── endodonti-kanal-tedavisi-29/
│   ├── zirkonyum-kaplama/
│   ├── periodontoloji/
│   ├── dental-implant/
│   ├── gulus-tasarimi/
│   └── ortodonti/
├── cocuk-dis/
│   ├── cocuk-dis-hekimligi/
│   └── pedodonti-cocuk-dis-hekimligi/
├── blog/                               # 9 makale, 5 kategori, 30 etiket
├── iletisim/                           # İletişim formu
├── randevu-al/                         # Randevu formu
├── anlasmali-kurumlar/                 # Anlaşmalı kurumlar listesi
├── sozlesme/
│   ├── saglik-turizmi/                 # Sağlık Turizmi Yetki Belgesi
│   ├── kvkk-aydinlatma-metni/
│   └── acik-riza-metni/
└── en/                                 # İngilizce versiyonlar (mirror)
```

### 4.2 Klinik ve Doktor Dağılımı

| Klinik | Konum | Doktor Sayısı | Telefon |
|--------|-------|--------------|---------|
| RivaDent Atakum | Mimar Sinan Mah. Atatürk Bulvarı, Riva İş Merkezi No:260 K:1, Atakum/Samsun | 8 | 0362 502 55 87 |
| RivaDent İlkadım | Hançerli Mah. 608. Sok. 5/9 (Faktör Ofis), İlkadım/Samsun | 4 | 0362 446 55 66 |
| RivaDent Maltepe | Cevizli Mh. Bağdat Cad. No:543-545, Maltepe/İstanbul | 5 | 0216 387 17 37 |

### 4.3 Tedavi Kategorileri (10 adet)
Ağız-Diş-Çene Cerrahisi · Protez Diş · Restoratif Diş · Diş Beyazlatma · Kanal Tedavisi · Zirkonyum Kaplama · Periodontoloji · Dental İmplant · Gülüş Tasarımı · Ortodonti

---

## 5. Mevcut Özellikler

### 5.1 Kullanıcı Arayüzü
- **Header Top Bar:** Sağlık Turizmi logosu, Hakkımızda, Anlaşmalı Kurumlar
- **Ana Navigasyon:** Anasayfa, Hekimler (klinik alt menülü), Poliklinikler, Tedaviler, Çocuk Diş, Blog, İletişim, Randevu Al
- **Dil Switcher:** TR / EN bayrak butonu
- **Mobil Menü:** Accordion yapılı hamburger menü
- **WhatsApp Butonu:** Sayfada kayan animasyonlu hızlı iletişim butonu

### 5.2 İçerik Bileşenleri
- Swiper.js ile doktor kartı carousel
- Swiper.js ile tedavi slider
- WOW.js scroll animasyonları
- Fancybox lightbox (sertifika/galeri görselleri)
- FAQ accordion (her tedavi sayfasında)
- İçindekiler listesi (tedavi sayfaları, mobil)

### 5.3 Formlar
| Form | Alanlar | Backend |
|------|---------|---------|
| İletişim | Ad-Soyad, E-posta, Şehir, Telefon, Mesaj | — |
| Randevu Al | Ad-Soyad, E-posta, Telefon, Tarih, Poliklinik, Şikayet | — |
| reCAPTCHA | v3 (token: 6Ld4sD8q...) | Google |

> ⚠️ Form gönderim backend'i henüz statik dosyalarda yok (eski PHP CMS üzerinde çalışıyor).

### 5.4 SEO & Teknik
- **Structured Data:** JSON-LD `DentalClinic` schema (her klinik için)
- **Hreflang:** TR/EN/x-default tüm sayfalarda
- **Canonical URL'ler:** Her sayfada mevcut
- **Sitemap:** `/sitemap.xml` — 90 URL, TR+EN hreflang pair, güncel tarih
- **Robots.txt:** Mevcut
- **OG / Twitter Card:** Her sayfada mevcut
- **Geo Meta:** `geo.region: TR-55`, `geo.placename: Samsun`

---

## 6. Eksikler / Bilinen Sorunlar

| # | Sorun | Öncelik | Durum |
|---|-------|---------|-------|
| 1 | Form backend'i çalışmıyor (PHP CMS üzerinde, statik sitede değil) | Yüksek | Açık |
| 2 | Google Analytics / GA4 entegrasyonu yok — ziyaretçi takibi yapılamıyor | Yüksek | Açık |
| 3 | Canlı site hâlâ eski PHP CMS'de — statik dosyalar deploy edilmedi | Yüksek | Açık |
| 4 | Blog makale sayısı az (9 makale) — SEO için içerik yetersiz | Orta | Açık |
| 5 | `blog/tag/ortodonti/` ve bazı etiket sayfaları EN versiyona sahip değil | Düşük | Açık |
| 6 | Bazı EN tedavi sayfaları yarım çeviri / boş içerik | Orta | Kısmen açık |
| 7 | Randevu formunda tarih min değeri hardcoded (`2026-05-19`) | Düşük | Açık |
| 8 | Görsel SEO: bazı `<img>` taglerinde `alt` metni eksik veya jenerik | Orta | Açık |

---

## 7. Öncelikli Geliştirme Alanları

### P1 — Kritik

#### 7.1 Deploy & Hosting
- Statik siteyi canlıya taşı (Netlify / Vercel / doğrudan sunucu)
- PHP CMS'i kapat, Nginx/Apache ile statik dosyaları sun
- HTTPS / SSL doğrula

#### 7.2 Analytics
- Google Analytics 4 (GA4) entegrasyonu — tüm sayfalara `gtag.js`
- Google Search Console doğrulaması tamamlanmalı (DNS TXT kaydı eklendi)
- Tercihen: Microsoft Clarity (ısı haritası + session recording, ücretsiz)

#### 7.3 Form Backend
- Randevu ve iletişim formlarını çalıştıracak backend:
  - Seçenek A: Formspree / EmailJS (sıfır backend, statik uyumlu)
  - Seçenek B: Netlify Forms (eğer Netlify'a deploy edilirse)
  - Seçenek C: AWS Lambda / Cloudflare Worker

### P2 — Önemli

#### 7.4 SEO İçerik Genişletme
- Her klinik için lokal SEO sayfası güçlendirilmeli:
  - Maltepe: "Maltepe diş hekimi", "Bağdat Caddesi diş" anahtar kelimeleri
  - Atakum: "Atakum diş kliniği" zaten iyi
- Aylık en az 2 blog makalesi hedeflenmeli
- Eksik `<meta name="description">` ve boş `alt` etiketleri tamamlanmalı

#### 7.5 Eksik EN Sayfaları
- EN sayfalarından yarım kalan içerikleri tamamla (tedavi açıklamaları)
- Uluslararası hastalara yönelik landing page: fiyat aralığı, süreç, ulaşım

#### 7.6 Structured Data Genişletme
- `FAQPage` schema: tedavi sayfalarındaki SSS bölümlerine ekle
- `Person` schema: hekim sayfaları için (ad, uzmanlık, bağlı klinik)
- `BreadcrumbList`: navigasyon izi için

### P3 — İyileştirme

#### 7.7 Performans
- Resimleri `loading="lazy"` ile işaretle
- Core Web Vitals ölçümü (LCP, CLS, FID)
- CSS/JS bundle boyutunu kontrol et

#### 7.8 UX
- Randevu formuna gerçek zamanlı tarih validasyonu
- "Whatsapp ile Randevu" direkt link butonu (klinik bazlı)
- Doktor profil sayfalarına "Bu Doktordan Randevu Al" CTA

---

## 8. İçerik Yönetimi

### 8.1 Yeni Doktor Ekleme Süreci
1. `hekim/[slug]/index.html` oluştur (mevcut şablondan kopyala)
2. `en/hekim/[slug]/index.html` oluştur (EN şablondan)
3. Ana sayfadaki hekimlerimiz swiper'a kart ekle
4. İlgili klinik sayfasına kart ekle
5. Navigasyon alt menüsüne ekle (tüm sayfalarda)
6. `sitemap.xml` güncelle

### 8.2 Yeni Tedavi Sayfası Ekleme
1. `tedavi/[slug]/index.html` oluştur
2. `en/tedavi/[slug]/index.html` oluştur (İngilizce içerikle)
3. Navigasyon Tedaviler alt menüsüne ekle (tüm sayfalarda)
4. `tedaviler/index.html` listesine ekle
5. `sitemap.xml` güncelle

### 8.3 Blog Yazısı Ekleme
1. `blog/[slug]/index.html` oluştur
2. `en/blog/[slug]/index.html` oluştur
3. `blog/index.html` ve ilgili kategori/etiket sayfalarına ekle
4. `sitemap.xml` güncelle

---

## 9. Teknik Bileşenler

| Kütüphane | Versiyon | Kullanım |
|-----------|----------|---------|
| Bootstrap | 5.x | Grid, responsive layout |
| Swiper.js | bundle | Carousel / slider |
| WOW.js | — | Scroll animasyonları |
| Animate.css | — | CSS animasyon sınıfları |
| Fancybox | — | Lightbox / galeri |
| Font Awesome | 6.x | İkonlar |
| Google reCAPTCHA | v3 | Form spam koruması |

---

## 10. Dağıtım Notları

- **Mevcut durum:** Statik dosyalar `localhost:8080`'de çalışıyor; canlı site hâlâ PHP CMS'de
- **Önerilen deploy:** Statik dosyaların doğrudan web sunucusuna (veya CDN'e) taşınması
- **CNAME:** Eklenmiş durumda (`CNAME` dosyası repo'da mevcut)
- **robots.txt:** Mevcut
- **sitemap.xml:** 90 URL, güncel (son güncelleme: 2026-09-16)

---

## 11. Kapsam Dışı

- Hasta kayıt / hasta takip sistemi (HIS/HBS entegrasyonu)
- Online ödeme
- Çok dilli destek (EN + TR dışı)
- Mobil uygulama
