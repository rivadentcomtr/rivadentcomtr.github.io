"""
Kurban Bayramı blog yazısını TR ve EN olarak oluşturur.
Mevcut blog template'ini baz alır, sadece içerik değiştirilir.
"""
from pathlib import Path
import re

SITE = Path(__file__).resolve().parent.parent

TR_TEMPLATE = SITE / "blog/gulumsemenin-onemi-ve-agiz-sagligina-etkileri/index.html"
EN_TEMPLATE = SITE / "en/blog/gulumsemenin-onemi-ve-agiz-sagligina-etkileri/index.html"
TR_SLUG  = "kurban-bayrami-et-tuketimi-ve-dis-sagligi"
EN_SLUG  = TR_SLUG  # aynı slug

# ── TR içerik ──────────────────────────────────────────────────────────────
TR_TITLE  = "Kurban Bayramı'nda Et Tüketimi ve Diş Sağlığı | RivaDent Samsun"
TR_DESC   = ("Kurban bayramında geçici diş, implant ve doğal diş kullanan "
             "hastalara önemli uyarılar. Samsun Atakum, İlkadım ve Maltepe "
             "RivaDent diş kliniği.")
TR_KW     = ("kurban bayramı diş sağlığı, implant samsun, atakum diş kliniği, "
             "ilkadım diş kliniği, maltepe diş kliniği, geçici diş, samsun diş")
TR_H1     = "Kurban Bayramı'nda Et Tüketimi ve Diş Sağlığı"

TR_BODY = """
<h2><strong>Kurban Bayramı'nda Et Tüketimi ve Diş Sağlığı</strong></h2>
<p><em>Geçici Diş, İmplant ve Doğal Diş Kullanan Hastalar İçin Küçük Ama Önemli Uyarılar</em></p>
<p>Kurban Bayramı denince akla ilk gelen şeylerden biri hiç şüphesiz kavurma, et yemekleri ve uzun sofralar oluyor. Ancak bayram döneminde özellikle sert ve lifli etlerin yoğun tüketimi, hem doğal dişlerde hem de geçici protez, kaplama veya implant üstü restorasyonlarda bazı problemlere neden olabiliyor. Bayram sonrası Samsun Atakum, İlkadım ve Maltepe kliniklerimizde en sık karşılaştığımız durumlardan biri; kırılan geçici dişler, yerinden çıkan kaplamalar ve çatlayan eski dolgular oluyor.</p>
<h3><strong>Geçici Diş ve İmplant Üstü Restorasyonlar</strong></h3>
<p>Özellikle yeni yapılan implant üstü geçici dişler veya geçici kronlar, estetik ve fonksiyon sağlamak için hazırlanır; ancak doğal diş kadar yüksek çiğneme kuvvetlerine dayanıklı olmayabilir. Bu nedenle ilk günlerde sert kavurma parçaları, kemik kenarları, uzun lifli etler veya çok kuru pişmiş etler kontrollü tüketilmelidir. Samsun'da implant tedavisi yaptırmış ya da geçici kron kullanan hastalarımız için bayram döneminde bu kurallara dikkat etmek, olası acil diş ziyaretlerinin önüne geçecektir.</p>
<h3><strong>Doğal Diş Kullanan Hastalarda Dikkat Edilmesi Gerekenler</strong></h3>
<p>Özellikle eski dolgular, çatlak dişler veya kanal tedavili dişler; ani ve yüksek çiğneme basınçlarında hassas hale gelebilir. Bayramda "bir anda sert parçaya denk gelme" sonrası oluşan diş çatlakları oldukça sık görülür. Atakum ve İlkadım şubelerimizde kanal tedavisi görmüş dişlerin üzerine kron yapılmamışsa, bu dişler özellikle kırılmaya daha yatkın olabilir.</p>
<h3><strong>İmplant Tedavisi Gören Hastalar</strong></h3>
<p>İmplant kemiğe kaynamış olsa bile, üzerindeki geçici parçalar veya vidalı sistemler aşırı kuvvet altında zarar görebilir. Özellikle kürdan kullanarak diş arası zorlamak veya kemiği dişle ayırmaya çalışmak implant çevresinde travmaya neden olabilir. Maltepe ve Samsun'daki implant hastalarımız bu konuda özellikle dikkatli olmalıdır.</p>
<h3><strong>Bayram Boyunca Önerilerimiz</strong></h3>
<ul>
<li><p>Çok sert ve kuru etleri küçük lokmalar halinde tüketin</p></li>
<li><p>Kemik kenarlarını dişle sıyırmaktan kaçının</p></li>
<li><p>Geçici dişlerle sert kuruyemiş veya kemikli et tüketmeyin</p></li>
<li><p>Tek taraflı yoğun çiğneme yapmayın</p></li>
<li><p>Yemek sonrası ağız temizliğini ihmal etmeyin</p></li>
<li><p>Takılma, sallanma veya ani hassasiyet hissederseniz zorlamaya devam etmeyin</p></li>
</ul>
<p>RivaDent olarak Samsun Atakum, İlkadım ve İstanbul Maltepe şubelerimizde bayram döneminde de randevu alabilirsiniz. Acil durumlar için kliniğimizin iletişim numaralarını saklı tutmanızı öneririz.</p>
<p>Sağlıklı, huzurlu ve gülümsemesi bol bir bayram geçirmeniz dileğiyle.</p>
<p><strong>RivaDent Diş Kliniği Ekibi</strong></p>
"""

TR_TAGS = """<li><a href="../tag/atakum-dis-klinigi/index.html">atakum diş kliniği</a></li>
                                                    <li><a href="../tag/ilkadim-dis-doktoru/index.html">ilkadım diş doktoru</a></li>
                                                    <li><a href="../tag/samsun-dis-doktoru/index.html">samsun diş doktoru</a></li>
                                                    <li><a href="../tag/dis-sagligi/index.html">diş sağlığı</a></li>
                                                    <li><a href="../tag/kanal-tedavisi/index.html">kanal tedavisi</a></li>"""

# ── EN içerik ──────────────────────────────────────────────────────────────
EN_TITLE = "Eid al-Adha Meat Consumption and Dental Health | RivaDent Samsun"
EN_DESC  = ("Important warnings for patients with temporary teeth, implants "
            "and natural teeth during Eid al-Adha. RivaDent dental clinic in "
            "Samsun Atakum, Ilkadim and Maltepe.")
EN_KW    = ("eid al-adha dental health, implant samsun, atakum dental clinic, "
            "ilkadim dental clinic, maltepe dental clinic, temporary crown, samsun dentist")
EN_H1    = "Eid al-Adha Meat Consumption and Dental Health"

EN_BODY = """
<h2><strong>Eid al-Adha Meat Consumption and Dental Health</strong></h2>
<p><em>Important Warnings for Patients with Temporary Teeth, Implants and Natural Teeth</em></p>
<p>One of the first things that comes to mind during Eid al-Adha is roasted meat dishes and long family meals. However, the heavy consumption of tough and fibrous meats during the holiday can cause problems for both natural teeth and temporary prostheses, veneers or implant-supported restorations. Some of the most common issues we see after the holiday at our RivaDent clinics in Samsun Atakum, Ilkadim and Maltepe include broken temporary teeth, dislodged veneers and cracked old fillings.</p>
<h3><strong>Temporary Teeth and Implant-Supported Restorations</strong></h3>
<p>Temporary crowns or implant-supported temporaries are designed for aesthetics and function, but they may not withstand the same chewing forces as natural teeth. Avoid tough cuts of meat, bone edges and very dry meat during the initial period. Patients in Samsun who have undergone implant treatment or are wearing temporary crowns should be especially cautious during the holiday to avoid emergency dental visits.</p>
<h3><strong>Patients with Natural Teeth</strong></h3>
<p>The situation is no different for patients with natural teeth. Old fillings, cracked teeth or root canal-treated teeth can become sensitive under sudden high chewing pressure. Cracked teeth caused by biting down on a hard piece are very common after the holiday. At our Atakum and Ilkadim clinics, we remind patients that root canal-treated teeth without crowns are particularly vulnerable to fracture.</p>
<h3><strong>Implant Patients</strong></h3>
<p>Even when an implant has fully integrated with the bone, the temporary components or screw systems on top can be damaged under excessive force. Using toothpicks forcefully between teeth or trying to strip meat off bones with the implant can cause trauma around the implant. We remind our implant patients in Maltepe and Samsun to be careful with tough, fibrous or bone-in meat.</p>
<h3><strong>Our Recommendations for the Holiday</strong></h3>
<ul>
<li><p>Cut tough and dry meats into small pieces</p></li>
<li><p>Avoid scraping meat off bones with your teeth</p></li>
<li><p>Do not eat hard nuts or bone-in meat with temporary teeth</p></li>
<li><p>Avoid chewing heavily on one side only</p></li>
<li><p>Do not neglect oral hygiene after meals</p></li>
<li><p>If you feel catching, looseness or sudden sensitivity, stop and do not force it</p></li>
</ul>
<p>At RivaDent, you can make an appointment at our Samsun Atakum, Ilkadim and Istanbul Maltepe branches even during the holiday period. We recommend keeping our clinic contact numbers handy for any emergencies.</p>
<p>We wish you a healthy, peaceful and smiling holiday.</p>
<p><strong>RivaDent Dental Clinic Team</strong></p>
"""

EN_TAGS = """<li><a href="../../en/blog/tag/atakum-dis-klinigi/index.html">atakum dental clinic</a></li>
                                                    <li><a href="../../en/blog/tag/dis-sagligi/index.html">dental health</a></li>
                                                    <li><a href="../../en/blog/tag/ortodontik-tedavi/index.html">dental treatment</a></li>"""

OLD_SLUG = "gulumsemenin-onemi-ve-agiz-sagligina-etkileri"
OLD_TITLE = "Atakum Diş beyazlatma"
OLD_H1    = "Gülümsemenin Önemi ve Ağız Sağlığına Etkileri"
OLD_DESC  = "Diş beyazlatma için hangi doktora gitmeliyim?"

# ── Content section markers ─────────────────────────────────────────────────
CONTENT_START = '<div class="treatment-content-text animate__bounceIn animate__animated wow" data-wow-duration="700ms" data-wow-offset="100">'
CONTENT_END   = '</div>\n            </div>\n            <div class="col-lg-8">\n                <div class="tags-area'

TAG_START = '<ul class="tags-list">'
TAG_END   = '</ul>\n                </div>'


EN_OLD_TITLE = "Atakum Diş Beyazlatma"
EN_OLD_H1    = "The Importance of Smiling and Its Effects on Oral Health"
EN_OLD_DESC  = "Diş beyazlatma için hangi doktora gitmeliyim?"


def build(lang: str) -> str:
    if lang == "tr":
        html = TR_TEMPLATE.read_text(encoding="utf-8")
        slug, title, desc, kw, h1, body, tags = (
            TR_SLUG, TR_TITLE, TR_DESC, TR_KW, TR_H1, TR_BODY, TR_TAGS)
        canonical = f"https://rivadent.com.tr/blog/{slug}/"
        alt_tr    = f"https://rivadent.com.tr/blog/{slug}/"
        alt_en    = f"https://rivadent.com.tr/en/blog/{slug}/"
        og_locale = "tr_TR"
        old_title, old_h1, old_desc = OLD_TITLE, OLD_H1, OLD_DESC
        # switcher: TR page points to EN
        html = html.replace(
            f'../../en/blog/{OLD_SLUG}/index.html',
            f'../../en/blog/{EN_SLUG}/index.html')
    else:
        html = EN_TEMPLATE.read_text(encoding="utf-8")
        slug, title, desc, kw, h1, body, tags = (
            EN_SLUG, EN_TITLE, EN_DESC, EN_KW, EN_H1, EN_BODY, EN_TAGS)
        canonical = f"https://rivadent.com.tr/en/blog/{slug}/"
        alt_tr    = f"https://rivadent.com.tr/blog/{slug}/"
        alt_en    = f"https://rivadent.com.tr/en/blog/{slug}/"
        og_locale = "en_US"
        old_title, old_h1, old_desc = EN_OLD_TITLE, EN_OLD_H1, EN_OLD_DESC
        # switcher: EN page points to TR
        html = html.replace(
            f'../../../blog/{OLD_SLUG}/index.html',
            f'../../../blog/{TR_SLUG}/index.html')

    # title
    html = html.replace(f"<title>{old_title}</title>",
                        f"<title>{title}</title>", 1)

    # canonical / alternates — replace old slug URLs
    html = re.sub(
        r'https://rivadent\.com\.tr(?:/en)?/blog/' + re.escape(OLD_SLUG) + r'/',
        canonical, html)
    html = re.sub(
        r'<link rel="alternate" hreflang="tr" href="[^"]*"/>',
        f'<link rel="alternate" hreflang="tr" href="{alt_tr}"/>', html, count=1)
    html = re.sub(
        r'<link rel="alternate" hreflang="en" href="[^"]*"/>',
        f'<link rel="alternate" hreflang="en" href="{alt_en}"/>', html, count=1)
    html = re.sub(
        r'<link rel="alternate" hreflang="x-default" href="[^"]*"/>',
        f'<link rel="alternate" hreflang="x-default" href="{alt_tr}"/>', html, count=1)

    # OG / meta
    html = html.replace(f'content="{old_title}"', f'content="{title}"')
    html = html.replace(f'content="{old_desc}"', f'content="{desc}"')
    html = re.sub(r'<meta name="keywords"[^/]*/>', f'<meta name="keywords" content="{kw}"/>', html, count=1)
    html = re.sub(r'<meta property="og:locale" content="[^"]*"/>',
                  f'<meta property="og:locale" content="{og_locale}"/>', html, count=1)
    html = re.sub(r'<meta content="[^"]*" name="description"/>',
                  f'<meta content="{desc}" name="description"/>', html, count=1)
    html = re.sub(r'<meta property="og:url" content="[^"]*"/>',
                  f'<meta property="og:url" content="{canonical}"/>', html, count=1)
    html = re.sub(r'<meta property="og:type" content="[^"]*"/>',
                  '<meta property="og:type" content="article"/>', html, count=1)

    # H1
    html = html.replace(
        f'<h1 class="title animate__bounceInDown animate__animated wow" '
        f'data-wow-duration="700ms" data-wow-offset="100">{old_h1}</h1>',
        f'<h1 class="title animate__bounceInDown animate__animated wow" '
        f'data-wow-duration="700ms" data-wow-offset="100">{h1}</h1>', 1)

    # Hero image alt + src
    html = re.sub(r'alt="[^"]*\| RivaDent"', f'alt="{h1} | RivaDent"', html)
    html = re.sub(
        r'(treatment-detail-img[^<]*<img[^>]*src=")[^"]*(")',
        r'\g<1>../../assets/uploads/kurban-bayraminda-agiz-ve-dis-sagligini-koruma-onerileri.webp\2'
        if lang == "tr" else
        r'\g<1>../../../assets/uploads/kurban-bayraminda-agiz-ve-dis-sagligini-koruma-onerileri.webp\2',
        html, count=1)

    # Body content
    cs = html.find(CONTENT_START)
    ce = html.find(CONTENT_END, cs)
    if cs != -1 and ce != -1:
        html = html[:cs + len(CONTENT_START)] + body + html[ce:]

    # Tags
    ts = html.find(TAG_START)
    te = html.find(TAG_END, ts)
    if ts != -1 and te != -1:
        html = (html[:ts + len(TAG_START)] + "\n" + tags +
                "\n                                                            " + html[te:])

    return html


# ── Write TR ────────────────────────────────────────────────────────────────
tr_dir = SITE / f"blog/{TR_SLUG}"
tr_dir.mkdir(parents=True, exist_ok=True)
(tr_dir / "index.html").write_text(build("tr"), encoding="utf-8")
print(f"TR oluşturuldu: {tr_dir}/index.html")

# ── Write EN ────────────────────────────────────────────────────────────────
en_dir = SITE / f"en/blog/{EN_SLUG}"
en_dir.mkdir(parents=True, exist_ok=True)
(en_dir / "index.html").write_text(build("en"), encoding="utf-8")
print(f"EN oluşturuldu: {en_dir}/index.html")
