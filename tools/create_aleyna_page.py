#!/usr/bin/env python3
"""
Create Aleyna Beray Kidak hekim pages (TR and EN)
by adapting Basak Timarcioglu's pages.
"""

from pathlib import Path

SITE_ROOT = Path(r"c:\Users\omerc\CascadeProjects\whatsappBot\rivadentLast\site")

TR_BIO = """<p><strong>Dt. Aleyna Beray Kıdak</strong>, <strong>Çanakkale</strong>'de doğmuş ve ilk, orta ve lise eğitimini <strong>İstanbul</strong>'da tamamlamıştır.</p>

<p>2016 yılında <strong>Marmara Üniversitesi Diş Hekimliği Fakültesi</strong>'ni kazanarak diş hekimliği eğitimine başlamış ve 2022 yılında <strong>lisans eğitimini</strong> başarıyla tamamlamıştır.</p>

<p>Dt. Aleyna Beray Kıdak, <strong>3 yıl</strong> boyunca <strong>İstanbul</strong>'da <strong>özel sektörde</strong> çalışmış ve 2026 yılında <strong>Rivadent Maltepe</strong> ailesine katılarak hastalara yüksek kaliteli hizmet vermeye başlamıştır.</p>

<p>Uzmanlık alanları; <strong>estetik kompozit dolgular</strong>, <strong>restoratif diş tedavileri</strong> ve <strong>endodontik tedaviler</strong> üzerine yoğunlaşmaktadır. Aynı zamanda <strong>ortodontik tedaviler</strong> konusunda tecrübe kazanmış, <strong>şeffaf plak tasarımı</strong> ve uygulanması gibi alanlarda kendini geliştirmiştir.</p>"""

EN_BIO = """<p><strong>Dt. Aleyna Beray Kıdak</strong> was born in <strong>Çanakkale</strong> and completed her primary, secondary, and high school education in <strong>Istanbul</strong>.</p>

<p>She enrolled at <strong>Marmara University Faculty of Dentistry</strong> in 2016 and successfully completed her undergraduate education in <strong>2022</strong>.</p>

<p>Dt. Aleyna Beray Kıdak worked in the <strong>private sector</strong> in <strong>Istanbul</strong> for <strong>3 years</strong> and joined the <strong>Rivadent Maltepe</strong> family in 2026, where she began providing high-quality dental care to patients.</p>

<p>Her areas of expertise focus on <strong>aesthetic composite fillings</strong>, <strong>restorative dental treatments</strong>, and <strong>endodontic treatments</strong>. She has also gained experience in <strong>orthodontic treatments</strong> and has developed herself in areas such as <strong>clear aligner design and application</strong>.</p>"""


def make_basak_image_subst(content, prefix):
    """Replace Basak's image hash with Aleyna's image."""
    return content.replace(
        '1071cc5e8eebd0521bbed8081dcbcb53.webp',
        'dt-aleyna-beray-kidak.webp'
    )


def create_page(src_path, dst_path, is_en=False):
    content = src_path.read_text(encoding='utf-8')

    # URLs and slugs
    content = content.replace('dt-basak-timarcioglu', 'dt-aleyna-beray-kidak')

    # Names
    content = content.replace('Dt. Başak Tımarcıoğlu', 'Dt. Aleyna Beray Kıdak')
    content = content.replace('Dr. Dt. Başak TIMARCIOĞLU', 'Dt. Aleyna Beray Kıdak')
    content = content.replace('Dt. Basak Timarcioglu', 'Dt. Aleyna Beray Kidak')

    # Image
    content = content.replace(
        '1071cc5e8eebd0521bbed8081dcbcb53.webp',
        'dt-aleyna-beray-kidak.webp'
    )

    # Meta/title description
    content = content.replace(
        'Diş Doktoru Başak Tımarcıoğlu',
        'Diş Doktoru Aleyna Beray Kıdak'
    )
    content = content.replace(
        'Dentist Basak Timarcioglu',
        'Dentist Aleyna Beray Kidak'
    )

    # Remove Basak instagram
    import re
    content = re.sub(
        r'\s*<li>\s*\n?\s*<a href="https://www\.instagram\.com/basakrcvs/?"[^>]*>.*?</a>\s*\n?\s*</li>',
        '',
        content,
        flags=re.DOTALL
    )

    # Replace bio text block (between team-detail-text div)
    bio_start = content.find('<div class="team-detail-text animate__zoomIn animate__animated wow"')
    if bio_start != -1:
        # find the opening div end
        tag_end = content.find('>', bio_start) + 1
        # find the closing </div>
        div_end = content.find('</div>', tag_end)
        if div_end != -1:
            bio = EN_BIO if is_en else TR_BIO
            content = content[:tag_end] + '\n                            ' + bio + '\n                        ' + content[div_end:]

    # In the modal select, mark Aleyna as selected (not Basak)
    content = content.replace(
        '<option selected="" value="31">Dt. Başak Tımarcıoğlu</option>',
        '<option value="31">Dt. Başak Tımarcıoğlu</option>'
    )
    content = content.replace(
        '<option value="32">Dt. Aleyna Beray Kıdak</option>',
        '<option selected="" value="32">Dt. Aleyna Beray Kıdak</option>'
    )

    dst_path.parent.mkdir(parents=True, exist_ok=True)
    dst_path.write_text(content, encoding='utf-8')
    print(f"  Created: {dst_path.relative_to(SITE_ROOT)}")


def main():
    # TR page
    src_tr = SITE_ROOT / "hekim" / "dt-basak-timarcioglu" / "index.html"
    dst_tr = SITE_ROOT / "hekim" / "dt-aleyna-beray-kidak" / "index.html"
    create_page(src_tr, dst_tr, is_en=False)

    # EN page
    src_en = SITE_ROOT / "en" / "hekim" / "dt-basak-timarcioglu" / "index.html"
    dst_en = SITE_ROOT / "en" / "hekim" / "dt-aleyna-beray-kidak" / "index.html"
    if src_en.exists():
        create_page(src_en, dst_en, is_en=True)
    else:
        print(f"  EN source not found: {src_en}")


if __name__ == "__main__":
    main()
