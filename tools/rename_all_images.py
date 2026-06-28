import os
import re
from bs4 import BeautifulSoup

def rename_physical_files():
    uploads_dir = r"c:\Users\omerc\CascadeProjects\whatsappBot\rivadentLast\site\assets\uploads"
    
    mapping = {
        "aee091d72bb7ec9429c76c8b9a433215.webp": "rivadent-ilkadim-dis-poliklinigi-bekleme-alani.webp",
        "8fad7e0d9b531202587dbe8fbb110fec.webp": "rivadent-ilkadim-dis-poliklinigi-koridor.webp",
        "2a3946a6f739edfb1529cba7a302ed22.webp": "rivadent-ilkadim-dis-poliklinigi-klinik-1.webp",
        "2a55cfc95c08e037c25bc885e03d9000.webp": "rivadent-ilkadim-dis-poliklinigi-klinik-2.webp",
        "e7b01dcb3e4c4fbfd6c6bf1358e87418.webp": "rivadent-ilkadim-dis-poliklinigi-klinik-3.webp",
        "d99428319eeff7d0b146ce36badf8ba8.webp": "rivadent-ilkadim-dis-poliklinigi-klinik-4.webp",
        
        "af9287db36296e133dafcbdfc0a9d288.webp": "rivadent-istanbul-maltepe-dis-poliklinigi-giris-kapisi.webp",
        "18026464616cdbde159d7a32349d3523.webp": "rivadent-istanbul-maltepe-dis-poliklinigi-banko-ve-bekleme-salonu.webp",
        "8c63dad0ac3cf8b963482d9d21b427d6.webp": "rivadent-istanbul-maltepe-dis-poliklinigi-klinik-1.webp",
        "ff7d6602913bed01ec571a209fcc31b4.webp": "rivadent-istanbul-maltepe-dis-poliklinigi-bekleme-salonu.webp",
        
        "863facfc22faf0f56264a6b5b60bd737.webp": "rivadent-dental-implant.webp",
        "c2092372e3b79550ec4dca4fed1f3164.webp": "rivadent-protez.webp",
        "035454fcd2bd25ba81d876313373b73d.webp": "rivadent-protez-2.webp",
        "189c278e8abeec8dea7ab88d88dc8c1d.webp": "rivadent-dis-curugu-tedavisi.webp",
        "6be2f1e3dce706b600c36ae9ad13fb00.webp": "rivadent-dis-curugu.webp",
        "496477887dc1544410e458f96a0b2857.webp": "rivadent-dis-beyazlatma-nedir.webp",
        "85a2e5f107ca56451434c40103b4aaf4.webp": "rivadent-dis-beyazlatma-yontemleri-nelerdir.webp",
        "e245d15f628b11e6bbb011ddd54e70c3.webp": "rivadent-lamina-nasil-yapilir.webp",
        "a06e38d938d8885054fc6eba0292445d.webp": "rivadent-dis-beyazlatma.webp",
        "a609751c39e7767c164c2adfe57a567d.webp": "rivadent-dis-beyazlatma-bleaching-yontemleri.webp",
        "4b11b237055bda3d97e0198cf9f14f68.webp": "rivadent-dis-beyazlatma-bleaching-yontemleri-2.webp",
        "dc7b733079698036afd46429ee5a1916.webp": "rivadent-dis-beyazlatma-bleaching-yontemleri-3.webp",
        "9d4e09e1a49ffac571b130f5a559ed5e.webp": "rivadent-dis-beyazlatma-bleaching-yontemleri-4.webp",
        "117bbd9cc49ec2bff55986815c23686f.webp": "rivadent-endodonti-tedavisinin-asamalari.webp",
        "ca86a7ddae761cdb3d28d73872dc0f80.webp": "rivadent-dis-hassasiyeti.webp",
        "1934c128e5ab6f132bc137565ff112b7.webp": "rivadent-periodontoloji-ne-yapar.webp",
        "c60b4c06c7f6211f3712120da07ee29c.webp": "rivadent-periodontal-hastaliklarin-belirtileri.webp",
        "10d4025e8b9c03608ec1ca6377dcb235.webp": "rivadent-periodontoloji-tedavi-yontemleri.webp",
        "087a6cf067baf9821d3db2c889434c67.webp": "rivadent-profesyonel-dis-temizligi.webp",
        "f58a13a504dea59588f15de6457f94ce.webp": "rivadent-cerrahi-tedavi.webp",
        "0404724d11208ba1d6509b4c466da009.webp": "rivadent-dental-implant-avantajlari-ve-riskleri-nelerdir.webp",
        "4eccd6d393b7bbb3fba106561d7f049a.webp": "rivadent-dental-implant-tedavisini-destekleyen-ek-tedaviler.webp",
        "f7c117e6ef1d8d18bc66e362ec5d6f11.webp": "rivadent-all-on-4-implant-sistemi.webp",
        "c5b576886e572322dfb55d60e003e921.webp": "rivadent-gulus-tasarimi-tedavi-yontemleri.webp",
        "3e42af59ea223eb3019dedd2ef376dfc.webp": "rivadent-gulus-estetigi-icin-hangi-islemler-yapilir.webp",
        "332d06545ff8b3e172e27d8836917840.webp": "rivadent-dis-teli-tedavisi.webp",
        "2822e40255dc8ca983bebee7fe437905.webp": "rivadent-neden-ortodontik-tedavi-olmaliyiz.webp",
        "06b5fa40a55ce7b76c79b3899b99811a.webp": "rivadent-ortodontik-tedavi-sirasinda-agri-hissedilir-mi.webp",
        "863ea1cd4e9cbb7932d2903e5b1e26c9.webp": "rivadent-cocuk-dis-hekimligi-pedodonti.webp",
        "5f150b37b6deaead9035e400702b08d4.webp": "rivadent-cocuk-dis-hekimligi.webp",
        "49fd25a5c4392294ed315f37f8b1ee66.webp": "rivadent-cocuk-ilk-disleri.webp",
        "43be0dc757523ffe09f14c6b5f061bdd.webp": "rivadent-cocuk-dis-hekimligi-pedodonti-2.webp",
        "6f5a8619bf64a21bc04d90875513a588.webp": "rivadent-cocuklarda-dislere-uygulanan-koruyucu-uygulamalar.webp",
        "f2002e29f45eccda7eb468a4e46e05dd.webp": "rivadent-cocuklarda-dis-hekimini-ilk-ziyaret-ne-zaman-olmalidir.webp",
        "a7ba2584fe85b7e00e5c8aa5aa263f19.webp": "rivadent-gulumsemenin-onemi-ve-agiz-sagligina-etkileri.webp",
        "1e47d36960024cd0c7126a535ab016c1.webp": "rivadent-dis-eti-cekilmesi-nedenleri-belirtileri-ve-tedavi-yontemleri.webp",
        "9a7f401da116481aec7e535c60570cfb.webp": "rivadent-sut-dislerinde-kanal-tedavisi-neden-ve-ne-zaman-gereklidir.webp",
        "2ebaa9cdbc54d7357344e67b948a9e48.webp": "rivadent-ortodontik-tedavinin-yas-siniri-var-midir.webp",
        "98f7fb46c9b565e3adc4c1533b3d252c.webp": "rivadent-gulus-tasariminda-dijital-agiz-ici-kayitlar-ve-gorsel-analizlerin-rolu.webp",
        "cb165e7c0555eb394f939fd07cdc0288.webp": "rivadent-cocuklarda-dis-tedavisi-ve-uygulama-sureci.webp",
        "2623e3a8de4b866d426825a23ce58696.webp": "rivadent-zirkonyum-ve-metal-destekli-porselen-dis-kaplamalari.webp",
        "a38f55a00940616ccb5266b99696cec4.webp": "rivadent-ortodontist-ve-dis-hekimi-arasindaki-temel-farklar.webp",
        "68ca199c13b63773ed32e25f41abb341.webp": "rivadent-gulumsemenin-onemi-ve-agiz-sagligina-etkileri-2.webp",
        "b7adb73e7f1d13989abeddd5c3a0eea4.webp": "rivadent-dis-eti-cekilmesi-nedenleri-belirtileri-ve-tedavi-yontemleri-2.webp",
        "279e31003e961b9c9144b5db1de5f000.webp": "rivadent-sut-dislerinde-kanal-tedavisi-neden-ve-ne-zaman-gereklidir-2.webp",
        "28aac353b0a8fd4f5bdf5f1384c2ebb5.webp": "rivadent-ortodontik-tedavinin-yas-siniri-var-midir-2.webp",
        "089f8329364cc932df08a8aa49b8f0fd.webp": "rivadent-gulus-tasariminda-dijital-agiz-ici-kayitlar-ve-gorsel-analizlerin-rolu-2.webp",
        "257363fbf2c002898517162981fe86ce.webp": "rivadent-ortodontist-ve-dis-hekimi-arasindaki-temel-farklar-2.webp",
        "9a46856ae790da24108555639f87d44e.webp": "rivadent-cocuklarda-dis-tedavisi-ve-uygulama-sureci-2.webp",
        "b20164b9731efa7c8a4728235f6e724e.webp": "rivadent-zirkonyum-ve-metal-destekli-porselen-dis-kaplamalari-2.webp",
        
        "3a13e84eac598f13772bdfda25dea0f3.webp": "rivadent-dis-klinigi.webp",
        "04c09b793252a1841b7e463cad6ae5d8.webp": "rivadent-istanbul-maltepe-dis-poliklinigi-banko-hikayemiz.webp",
        
        "8369d92d2e4c4b6c26a0bff5b5208be2.webp": "rivadent-anlasmali-kurum-british-american-tobacco.webp",
        "8729782f238d321b0e92193c04447cdb.webp": "rivadent-anlasmali-kurum-yon-pazarlama.webp",
        "add64982b56a56493a487f3c9c3e7937.webp": "rivadent-anlasmali-kurum-bahcesehir-koleji.webp"
    }

    print("Renaming physical files in assets/uploads...")
    for old_name, new_name in mapping.items():
        old_path = os.path.join(uploads_dir, old_name)
        new_path = os.path.join(uploads_dir, new_name)
        
        if os.path.exists(old_path):
            try:
                os.rename(old_path, new_path)
                print(f" - Renamed: {old_name} -> {new_name}")
            except Exception as e:
                print(f" - Error renaming {old_name}: {e}")
        elif os.path.exists(new_path):
            print(f" - Already renamed: {new_name}")
        else:
            print(f" - [WARNING] File not found: {old_name}")

def update_html_references():
    root_dir = r"c:\Users\omerc\CascadeProjects\whatsappBot\rivadentLast\site"
    
    # We define the mappings and translations
    # Format: old_filename: (new_filename, TR_alt, EN_alt)
    image_data = {
        "aee091d72bb7ec9429c76c8b9a433215.webp": (
            "rivadent-ilkadim-dis-poliklinigi-bekleme-alani.webp",
            "Rivadent İlkadım Diş Polikliniği Bekleme Alanı",
            "Rivadent Ilkadim Dental Clinic Waiting Area"
        ),
        "8fad7e0d9b531202587dbe8fbb110fec.webp": (
            "rivadent-ilkadim-dis-poliklinigi-koridor.webp",
            "Rivadent İlkadım Diş Polikliniği Koridor",
            "Rivadent Ilkadim Dental Clinic Hallway"
        ),
        "2a3946a6f739edfb1529cba7a302ed22.webp": (
            "rivadent-ilkadim-dis-poliklinigi-klinik-1.webp",
            "Rivadent İlkadım Diş Polikliniği Klinik 1",
            "Rivadent Ilkadim Dental Clinic Treatment Room 1"
        ),
        "2a55cfc95c08e037c25bc885e03d9000.webp": (
            "rivadent-ilkadim-dis-poliklinigi-klinik-2.webp",
            "Rivadent İlkadım Diş Polikliniği Klinik 2",
            "Rivadent Ilkadim Dental Clinic Treatment Room 2"
        ),
        "e7b01dcb3e4c4fbfd6c6bf1358e87418.webp": (
            "rivadent-ilkadim-dis-poliklinigi-klinik-3.webp",
            "Rivadent İlkadım Diş Polikliniği Klinik 3",
            "Rivadent Ilkadim Dental Clinic Treatment Room 3"
        ),
        "d99428319eeff7d0b146ce36badf8ba8.webp": (
            "rivadent-ilkadim-dis-poliklinigi-klinik-4.webp",
            "Rivadent İlkadım Diş Polikliniği Klinik 4",
            "Rivadent Ilkadim Dental Clinic Treatment Room 4"
        ),
        "af9287db36296e133dafcbdfc0a9d288.webp": (
            "rivadent-istanbul-maltepe-dis-poliklinigi-giris-kapisi.webp",
            "Rivadent İstanbul Maltepe Diş Polikliniği Giriş Kapısı",
            "Rivadent Istanbul Maltepe Dental Clinic Entrance Door"
        ),
        "18026464616cdbde159d7a32349d3523.webp": (
            "rivadent-istanbul-maltepe-dis-poliklinigi-banko-ve-bekleme-salonu.webp",
            "Rivadent İstanbul Maltepe Diş Polikliniği Banko ve Bekleme Salonu",
            "Rivadent Istanbul Maltepe Dental Clinic Reception Counter and Waiting Room"
        ),
        "8c63dad0ac3cf8b963482d9d21b427d6.webp": (
            "rivadent-istanbul-maltepe-dis-poliklinigi-klinik-1.webp",
            "Rivadent İstanbul Maltepe Diş Polikliniği Klinik 1",
            "Rivadent Istanbul Maltepe Dental Clinic Treatment Room 1"
        ),
        "ff7d6602913bed01ec571a209fcc31b4.webp": (
            "rivadent-istanbul-maltepe-dis-poliklinigi-bekleme-salonu.webp",
            "Rivadent İstanbul Maltepe Diş Polikliniği Bekleme salonu",
            "Rivadent Istanbul Maltepe Dental Clinic Waiting Room"
        ),
        "863facfc22faf0f56264a6b5b60bd737.webp": (
            "rivadent-dental-implant.webp",
            "Dental implant",
            "Dental implant"
        ),
        "c2092372e3b79550ec4dca4fed1f3164.webp": (
            "rivadent-protez.webp",
            "Protez",
            "Prosthesis"
        ),
        "035454fcd2bd25ba81d876313373b73d.webp": (
            "rivadent-protez-2.webp",
            "Protez 2",
            "Prosthesis 2"
        ),
        "189c278e8abeec8dea7ab88d88dc8c1d.webp": (
            "rivadent-dis-curugu-tedavisi.webp",
            "Diş Çürüğü Tedavisi",
            "Tooth Decay Treatment"
        ),
        "6be2f1e3dce706b600c36ae9ad13fb00.webp": (
            "rivadent-dis-curugu.webp",
            "Diş Çürüğü",
            "Tooth Decay"
        ),
        "496477887dc1544410e458f96a0b2857.webp": (
            "rivadent-dis-beyazlatma-nedir.webp",
            "Diş Beyazlatma Nedir? | RivaDent",
            "What is Teeth Whitening? | RivaDent"
        ),
        "85a2e5f107ca56451434c40103b4aaf4.webp": (
            "rivadent-dis-beyazlatma-yontemleri-nelerdir.webp",
            "Diş Beyazlatma Yöntemleri Nelerdir? | RivaDent",
            "What are Teeth Whitening Methods? | RivaDent"
        ),
        "e245d15f628b11e6bbb011ddd54e70c3.webp": (
            "rivadent-lamina-nasil-yapilir.webp",
            "Lamina Nasıl Yapılır? | RivaDent",
            "How is Lamina Veneer Made? | RivaDent"
        ),
        "a06e38d938d8885054fc6eba0292445d.webp": (
            "rivadent-dis-beyazlatma.webp",
            "Diş Beyazlatma | RivaDent",
            "Teeth Whitening | RivaDent"
        ),
        "a609751c39e7767c164c2adfe57a567d.webp": (
            "rivadent-dis-beyazlatma-bleaching-yontemleri.webp",
            "Diş Beyazlatma (Bleaching) Yöntemleri | RivaDent",
            "Teeth Whitening (Bleaching) Methods | RivaDent"
        ),
        "4b11b237055bda3d97e0198cf9f14f68.webp": (
            "rivadent-dis-beyazlatma-bleaching-yontemleri-2.webp",
            "Diş Beyazlatma (Bleaching) Yöntemleri | RivaDent",
            "Teeth Whitening (Bleaching) Methods | RivaDent"
        ),
        "dc7b733079698036afd46429ee5a1916.webp": (
            "rivadent-dis-beyazlatma-bleaching-yontemleri-3.webp",
            "Diş Beyazlatma (Bleaching) Yöntemleri | RivaDent",
            "Teeth Whitening (Bleaching) Methods | RivaDent"
        ),
        "9d4e09e1a49ffac571b130f5a559ed5e.webp": (
            "rivadent-dis-beyazlatma-bleaching-yontemleri-4.webp",
            "Diş Beyazlatma (Bleaching) Yöntemleri | RivaDent",
            "Teeth Whitening (Bleaching) Methods | RivaDent"
        ),
        "117bbd9cc49ec2bff55986815c23686f.webp": (
            "rivadent-endodonti-tedavisinin-asamalari.webp",
            "Endodonti Tedavisinin Aşamaları | RivaDent",
            "Stages of Endodontic Treatment | RivaDent"
        ),
        "ca86a7ddae761cdb3d28d73872dc0f80.webp": (
            "rivadent-dis-hassasiyeti.webp",
            "Diş Hassasiyeti | RivaDent",
            "Tooth Sensitivity | RivaDent"
        ),
        "1934c128e5ab6f132bc137565ff112b7.webp": (
            "rivadent-periodontoloji-ne-yapar.webp",
            "Periodontoloji Ne Yapar? | RivaDent",
            "What Does Periodontology Do? | RivaDent"
        ),
        "c60b4c06c7f6211f3712120da07ee29c.webp": (
            "rivadent-periodontal-hastaliklarin-belirtileri.webp",
            "Periodontal Hastalıkların Belirtileri | RivaDent",
            "Symptoms of Periodontal Diseases | RivaDent"
        ),
        "10d4025e8b9c03608ec1ca6377dcb235.webp": (
            "rivadent-periodontoloji-tedavi-yontemleri.webp",
            "Periodontoloji Tedavi Yöntemleri | RivaDent",
            "Periodontology Treatment Methods | RivaDent"
        ),
        "087a6cf067baf9821d3db2c889434c67.webp": (
            "rivadent-profesyonel-dis-temizligi.webp",
            "Profesyonel Diş Temizliği | RivaDent",
            "Professional Teeth Cleaning | RivaDent"
        ),
        "f58a13a504dea59588f15de6457f94ce.webp": (
            "rivadent-cerrahi-tedavi.webp",
            "Cerrahi Tedavi | RivaDent",
            "Surgical Treatment | RivaDent"
        ),
        "0404724d11208ba1d6509b4c466da009.webp": (
            "rivadent-dental-implant-avantajlari-ve-riskleri-nelerdir.webp",
            "Dental İmplant Avantajları ve Riskleri Nelerdir? | RivaDent",
            "What are the Advantages and Risks of Dental Implants? | RivaDent"
        ),
        "4eccd6d393b7bbb3fba106561d7f049a.webp": (
            "rivadent-dental-implant-tedavisini-destekleyen-ek-tedaviler.webp",
            "Dental İmplant Tedavisini Destekleyen Ek Tedaviler | RivaDent",
            "Additional Treatments Supporting Dental Implant Treatment | RivaDent"
        ),
        "f7c117e6ef1d8d18bc66e362ec5d6f11.webp": (
            "rivadent-all-on-4-implant-sistemi.webp",
            "All-On-4 İmplant Sistemi | RivaDent",
            "All-On-4 Implant System | RivaDent"
        ),
        "c5b576886e572322dfb55d60e003e921.webp": (
            "rivadent-gulus-tasarimi-tedavi-yontemleri.webp",
            "Gülüş Tasarımı Tedavi Yöntemleri | RivaDent",
            "Smile Design Treatment Methods | RivaDent"
        ),
        "3e42af59ea223eb3019dedd2ef376dfc.webp": (
            "rivadent-gulus-estetigi-icin-hangi-islemler-yapilir.webp",
            "Gülüş Estetiği İçin Hangi İşlemler Yapılır? | RivaDent",
            "Which Procedures are Performed for Smile Aesthetics? | RivaDent"
        ),
        "332d06545ff8b3e172e27d8836917840.webp": (
            "rivadent-dis-teli-tedavisi.webp",
            "Diş Teli Tedavisi",
            "Braces Treatment | RivaDent"
        ),
        "2822e40255dc8ca983bebee7fe437905.webp": (
            "rivadent-neden-ortodontik-tedavi-olmaliyiz.webp",
            "Neden Ortodontik Tedavi Olmalıyız? | RivaDent",
            "Why Should We Undergo Orthodontic Treatment? | RivaDent"
        ),
        "06b5fa40a55ce7b76c79b3899b99811a.webp": (
            "rivadent-ortodontik-tedavi-sirasinda-agri-hissedilir-mi.webp",
            "Ortodontik Tedavi Sırasında Ağrı Hissedilir Mi? | RivaDent",
            "Is Pain Felt During Orthodontic Treatment? | RivaDent"
        ),
        "863ea1cd4e9cbb7932d2903e5b1e26c9.webp": (
            "rivadent-cocuk-dis-hekimligi-pedodonti.webp",
            "Çocuk Diş Hekimliği | Pedodonti | RivaDent",
            "Pediatric Dentistry | Pedodontics | RivaDent"
        ),
        "5f150b37b6deaead9035e400702b08d4.webp": (
            "rivadent-cocuk-dis-hekimligi.webp",
            "Çocuk Diş Hekimliği | RivaDent",
            "Pediatric Dentistry | RivaDent"
        ),
        "49fd25a5c4392294ed315f37f8b1ee66.webp": (
            "rivadent-cocuk-ilk-disleri.webp",
            "Çocuk İlk Dişleri | Rivadent",
            "Children's First Teeth | RivaDent"
        ),
        "43be0dc757523ffe09f14c6b5f061bdd.webp": (
            "rivadent-cocuk-dis-hekimligi-pedodonti-2.webp",
            "Çocuk Diş Hekimliği | Pedodonti | RivaDent",
            "Pediatric Dentistry | Pedodontics | RivaDent"
        ),
        "6f5a8619bf64a21bc04d90875513a588.webp": (
            "rivadent-cocuklarda-dislere-uygulanan-koruyucu-uygulamalar.webp",
            "Çocuklarda Dişlere Uygulanan Koruyucu Uygulamalar | RivaDent",
            "Preventive Dental Treatments in Children | RivaDent"
        ),
        "f2002e29f45eccda7eb468a4e46e05dd.webp": (
            "rivadent-cocuklarda-dis-hekimini-ilk-ziyaret-ne-zaman-olmalidir.webp",
            "Çocuklarda Diş Hekimini İlk Ziyaret Ne Zaman Olmalıdır? | RivaDent",
            "When Should Children First Visit the Dentist? | RivaDent"
        ),
        "a7ba2584fe85b7e00e5c8aa5aa263f19.webp": (
            "rivadent-gulumsemenin-onemi-ve-agiz-sagligina-etkileri.webp",
            "Gülümsemenin Önemi ve Ağız Sağlığına Etkileri | RivaDent",
            "The Importance of Smiling and Its Effects on Oral Health | RivaDent"
        ),
        "1e47d36960024cd0c7126a535ab016c1.webp": (
            "rivadent-dis-eti-cekilmesi-nedenleri-belirtileri-ve-tedavi-yontemleri.webp",
            "Diş Eti Çekilmesi: Nedenleri, Belirtileri ve Treatman Yöntemleri | RivaDent",
            "Gum Recession: Causes, Symptoms, and Treatment Methods | RivaDent"
        ),
        "9a7f401da116481aec7e535c60570cfb.webp": (
            "rivadent-sut-dislerinde-kanal-tedavisi-neden-ve-ne-zaman-gereklidir.webp",
            "Süt Dişlerinde Kanal Tedavisi: Neden ve Ne Zaman Gereklidir? | RivaDent",
            "Root Canal Treatment in Primary Teeth: Why and When is it Necessary? | RivaDent"
        ),
        "2ebaa9cdbc54d7357344e67b948a9e48.webp": (
            "rivadent-ortodontik-tedavinin-yas-siniri-var-midir.webp",
            "Ortodontik Tedavinin Yaş Sınırı Var Mıdır? | RivaDent",
            "Is There an Age Limit for Orthodontic Treatment? | RivaDent"
        ),
        "98f7fb46c9b565e3adc4c1533b3d252c.webp": (
            "rivadent-gulus-tasariminda-dijital-agiz-ici-kayitlar-ve-gorsel-analizlerin-rolu.webp",
            "Gülüş Tasarımında Dijital Ağız İçi Kayıtlar ve Görsel Analizlerin Rolü | RivaDent",
            "The Role of Digital Intraoral Records and Visual Analysis in Smile Design | RivaDent"
        ),
        "cb165e7c0555eb394f939fd07cdc0288.webp": (
            "rivadent-cocuklarda-dis-tedavisi-ve-uygulama-sureci.webp",
            "Çocuklarda Diş Tedavisi ve Uygulama Süreci | RivaDent",
            "Dental Treatment and Application Process in Children | RivaDent"
        ),
        "2623e3a8de4b866d426825a23ce58696.webp": (
            "rivadent-zirkonyum-ve-metal-destekli-porselen-dis-kaplamalari.webp",
            "Zirkonyum ve Metal Destekli Porselen Diş Kaplamaları: Hangisi Sizin İçin Daha Uygun? | RivaDent",
            "Zirconium and Metal-Backed Porcelain Veneers: Which is More Suitable for You? | RivaDent"
        ),
        "a38f55a00940616ccb5266b99696cec4.webp": (
            "rivadent-ortodontist-ve-dis-hekimi-arasindaki-temel-farklar.webp",
            "Ortodontist ve Diş Hekimi Arasındaki Temel Farklar | RivaDent",
            "Key Differences Between an Orthodontist and a Dentist | RivaDent"
        ),
        "68ca199c13b63773ed32e25f41abb341.webp": (
            "rivadent-gulumsemenin-onemi-ve-agiz-sagligina-etkileri-2.webp",
            "Gülümsemenin Önemi ve Ağız Sağlığına Etkileri | RivaDent",
            "The Importance of Smiling and Its Effects on Oral Health | RivaDent"
        ),
        "b7adb73e7f1d13989abeddd5c3a0eea4.webp": (
            "rivadent-dis-eti-cekilmesi-nedenleri-belirtileri-ve-tedavi-yontemleri-2.webp",
            "Diş Eti Çekilmesi: Nedenleri, Belirtileri ve Tedavi Yöntemleri | RivaDent",
            "Gum Recession: Causes, Symptoms, and Treatment Methods | RivaDent"
        ),
        "279e31003e961b9c9144b5db1de5f000.webp": (
            "rivadent-sut-dislerinde-kanal-tedavisi-neden-ve-ne-zaman-gereklidir-2.webp",
            "Süt Dişlerinde Kanal Tedavisi: Neden ve Ne Zaman Gereklidir? | RivaDent",
            "Primary Teeth Root Canal Treatment: Why and When is it Necessary? | RivaDent"
        ),
        "28aac353b0a8fd4f5bdf5f1384c2ebb5.webp": (
            "rivadent-ortodontik-tedavinin-yas-siniri-var-midir-2.webp",
            "Ortodontik Tedavinin Yaş Sınırı Var Mıdır? | RivaDent",
            "Is There an Age Limit for Orthodontic Treatment? | RivaDent"
        ),
        "089f8329364cc932df08a8aa49b8f0fd.webp": (
            "rivadent-gulus-tasariminda-dijital-agiz-ici-kayitlar-ve-gorsel-analizlerin-rolu-2.webp",
            "Gülüş Tasarımında Dijital Ağız İçi Kayıtlar ve Görsel Analizlerin Rolü | RivaDent",
            "The Role of Digital Intraoral Records and Visual Analysis in Smile Design | RivaDent"
        ),
        "257363fbf2c002898517162981fe86ce.webp": (
            "rivadent-ortodontist-ve-dis-hekimi-arasindaki-temel-farklar-2.webp",
            "Ortodontist ve Diş Hekimi Arasındaki Temel Farklar | RivaDent",
            "Key Differences Between an Orthodontist and a Dentist | RivaDent"
        ),
        "9a46856ae790da24108555639f87d44e.webp": (
            "rivadent-cocuklarda-dis-tedavisi-ve-uygulama-sureci-2.webp",
            "Çocuklarda Diş Tedavisi ve Uygulama Süreci | RivaDent",
            "Dental Treatment and Application Process in Children | RivaDent"
        ),
        "b20164b9731efa7c8a4728235f6e724e.webp": (
            "rivadent-zirkonyum-ve-metal-destekli-porselen-dis-kaplamalari-2.webp",
            "Zirkonyum ve Metal Destekli Porselen Diş Kaplamaları: Hangisi Sizin İçin Daha Uygun? | RivaDent",
            "Zirconium and Metal-Backed Porcelain Veneers: Which is More Suitable for You? | RivaDent"
        ),
        "3a13e84eac598f13772bdfda25dea0f3.webp": (
            "rivadent-dis-klinigi.webp",
            "RivaDent Diş Kliniği",
            "RivaDent Dental Clinic"
        ),
        "04c09b793252a1841b7e463cad6ae5d8.webp": (
            "rivadent-istanbul-maltepe-dis-poliklinigi-banko-hikayemiz.webp",
            "Rivadent İstanbul Maltepe Diş Polikliniği Banko | RivaDent olarak, sağlıklı gülüşler ve kaliteli diş bakımı sunma yolundaki hikayemizi keşfedin. | RivaDent",
            "Rivadent Istanbul Maltepe Dental Clinic Reception Desk | Discover our story towards offering healthy smiles and quality dental care. | RivaDent"
        ),
        "8369d92d2e4c4b6c26a0bff5b5208be2.webp": (
            "rivadent-anlasmali-kurum-british-american-tobacco.webp",
            "British American Tobacco | Anlaşmalı Kurumlar | Rivadent",
            "British American Tobacco | Contracted Institutions | RivaDent"
        ),
        "8729782f238d321b0e92193c04447cdb.webp": (
            "rivadent-anlasmali-kurum-yon-pazarlama.webp",
            "Yön Pazarlama | Anlaşmalı Kurumlar | Rivadent",
            "Yon Pazarlama | Contracted Institutions | RivaDent"
        ),
        "add64982b56a56493a487f3c9c3e7937.webp": (
            "rivadent-anlasmali-kurum-bahcesehir-koleji.webp",
            "Bahçeşehir Koleji | Anlaşmalı Kurumlar | Rivadent",
            "Bahcesehir College | Contracted Institutions | RivaDent"
        )
    }

    print("\nScanning and updating HTML files...")
    
    # Find all HTML files
    html_files = []
    for root, dirs, files in os.walk(root_dir):
        if ".git" in root or "assets/back" in root:
            continue
        for file in files:
            if file.endswith(".html"):
                html_files.append(os.path.join(root, file))

    updated_files_count = 0

    for file_path in html_files:
        is_english = "/en/" in file_path or "\\en\\" in file_path
        
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            original_content = content
            
            # 1. First, replace references to old hashes in src and update their alt tags
            for old_name, (new_name, tr_alt, en_alt) in image_data.items():
                if old_name in content:
                    target_alt = en_alt if is_english else tr_alt
                    
                    def replacer(match):
                        tag_str = match.group(0)
                        soup = BeautifulSoup(tag_str, 'html.parser')
                        img = soup.find('img')
                        if img:
                            src = img.get('src', '')
                            if old_name in src:
                                img['src'] = src.replace(old_name, new_name)
                            img['alt'] = target_alt
                            return str(img)
                        return tag_str

                    img_pattern = re.compile(r'<img[^>]*?src="[^"]*?' + re.escape(old_name) + r'"[^>]*?>', re.IGNORECASE)
                    content = img_pattern.sub(replacer, content)
                    
                    # Also replace old_name in any simple href="..." links (e.g. Fancybox links)
                    content = content.replace(f'href="assets/uploads/{old_name}"', f'href="assets/uploads/{new_name}"')
                    content = content.replace(f'href="../assets/uploads/{old_name}"', f'href="../assets/uploads/{new_name}"')
                    content = content.replace(f'href="../../assets/uploads/{old_name}"', f'href="../../assets/uploads/{new_name}"')
                    content = content.replace(f'href="../../../assets/uploads/{old_name}"', f'href="../../../assets/uploads/{new_name}"')

            # 2. Update logo.webp alt tag in HTML files
            # <img alt="..." src=".../logo/logo.webp" />
            # Find any logo.webp img tags and update alt
            logo_pattern = re.compile(r'<img[^>]*?src="[^"]*?logo/logo\.webp"[^>]*?>', re.IGNORECASE)
            
            def logo_replacer(match):
                tag_str = match.group(0)
                soup = BeautifulSoup(tag_str, 'html.parser')
                img = soup.find('img')
                if img:
                    img['alt'] = "RivaDent Oral and Dental Health Polyclinic Logo" if is_english else "RivaDent Ağız ve Diş Sağlığı Polikliniği Logo"
                    return str(img)
                return tag_str
                
            content = logo_pattern.sub(logo_replacer, content)

            if content != original_content:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f" - Updated references in: {os.path.relpath(file_path, root_dir)}")
                updated_files_count += 1

        except Exception as e:
            print(f" - Error processing {file_path}: {e}")

    print(f"\nCompleted! Updated {updated_files_count} HTML files.")

if __name__ == "__main__":
    rename_physical_files()
    update_html_references()
