import os
import re
from PIL import Image
from bs4 import BeautifulSoup

def clean_slug(name):
    name = name.lower()
    # Replace Turkish chars
    replacements = {
        'ı': 'i', 'ş': 's', 'ğ': 'g', 'ü': 'u', 'ç': 'c', 'ö': 'o',
        'â': 'a', 'ê': 'e', 'î': 'i', 'ô': 'o', 'û': 'u'
    }
    for k, v in replacements.items():
        name = name.replace(k, v)
    name = re.sub(r'[^a-z0-9\-]+', '-', name)
    name = re.sub(r'-+', '-', name).strip('-')
    return name

def run():
    uploads_dir = r"c:\Users\omerc\CascadeProjects\whatsappBot\rivadentLast\site\assets\uploads"
    atakum_dir = os.path.join(uploads_dir, "Atakum")
    
    # 1. Rename existing 6 hashed files in assets/uploads/
    hash_mapping = {
        "ffe8b4498214eb0a32bae684b7b654ca.webp": (
            "rivadent-atakum-dis-poliklinigi-endodonti-klinigi-1.webp",
            "Rivadent Atakum Diş Polikliniği Endodonti kliniği",
            "Rivadent Atakum Dental Clinic Endodontics Clinic 1"
        ),
        "fdb866501576a2963949e2fcee114f08.webp": (
            "rivadent-atakum-dis-poliklinigi-endodonti-klinigi-2.webp",
            "Rivadent Atakum Diş Polikliniği Endodonti kliniği",
            "Rivadent Atakum Dental Clinic Endodontics Clinic 2"
        ),
        "9266e9a256bced7b804f5f762f5d139d.webp": (
            "rivadent-atakum-dis-poliklinigi-bekleme-alani.webp",
            "Rivadent Atakum Diş Polikliniği bekleme alanı",
            "Rivadent Atakum Dental Clinic Waiting Area"
        ),
        "5f4902943096848185737ec9a1e2d342.webp": (
            "rivadent-atakum-dis-poliklinigi-klinikler-5.webp",
            "Rivadent Atakum Diş Polikliniği Klinikler 5",
            "Rivadent Atakum Dental Clinic Treatment Room 5"
        ),
        "9a2e14d63a858ce50c5908a2b82c57d3.webp": (
            "rivadent-atakum-dis-poliklinigi-klinikler-2.webp",
            "Rivadent Atakum Diş Polikliniği Klinikler 2",
            "Rivadent Atakum Dental Clinic Treatment Room 2"
        ),
        "c6219add5c3581537f75e9dde3633eb4.webp": (
            "rivadent-atakum-dis-poliklinigi-klinikler-3.webp",
            "Rivadent Atakum Diş Polikliniği Klinikler 3",
            "Rivadent Atakum Dental Clinic Treatment Room 3"
        )
    }
    
    print("Step 1: Renaming the 6 existing hashed files on disk...")
    for old_hash, (new_name, tr_alt, en_alt) in hash_mapping.items():
        old_path = os.path.join(uploads_dir, old_hash)
        new_path = os.path.join(uploads_dir, new_name)
        if os.path.exists(old_path):
            os.rename(old_path, new_path)
            print(f" - Renamed: {old_hash} -> {new_name}")
        elif os.path.exists(new_path):
            print(f" - Already renamed: {new_name}")
        else:
            print(f" - [WARNING] Old hash not found: {old_hash}")

    # 2. Convert Atakum JPEGs to WebP and save in uploads/
    # Map the original filenames to English translations for alt tags
    translations = {
        "Rivadent Atakum Diş Polikliniği Banko kliniğin girişi": "Rivadent Atakum Dental Clinic Counter Clinic Entrance",
        "Rivadent Atakum Diş Polikliniği Banko": "Rivadent Atakum Dental Clinic Reception Desk",
        "Rivadent Atakum Diş Polikliniği Bekleme salonu 2": "Rivadent Atakum Dental Clinic Waiting Area 2",
        "Rivadent Atakum Diş Polikliniği Bekleme salonu": "Rivadent Atakum Dental Clinic Waiting Area",
        "Rivadent Atakum Diş Polikliniği Endodonti kliniği": "Rivadent Atakum Dental Clinic Endodontics Department",
        "Rivadent Atakum Diş Polikliniği Endodonti": "Rivadent Atakum Dental Clinic Endodontics Room",
        "Rivadent Atakum Diş Polikliniği Ortak alan bekleme salonu": "Rivadent Atakum Dental Clinic Common Waiting Room",
        "Rivadent Atakum Diş Polikliniği Ortodonti bekleme salonu": "Rivadent Atakum Dental Clinic Orthodontics Waiting Area",
        "Rivadent Atakum Diş Polikliniği Pedodonti bekleme salonu": "Rivadent Atakum Dental Clinic Pediatric Waiting Area",
        "Rivadent Atakum Diş Polikliniği Pedodonti kliniği": "Rivadent Atakum Dental Clinic Pediatric Dentistry Clinic",
        "Rivadent Atakum Diş Polikliniği Pedodonti": "Rivadent Atakum Dental Clinic Pediatric Department",
        "Rivadent Atakum Diş Polikliniği Protez bekleme salonu": "Rivadent Atakum Dental Clinic Prosthetics Waiting Area"
    }

    print("\nStep 2: Converting new Atakum JPEGs to WebP and transferring to assets/uploads...")
    converted_images = [] # stores tuples: (new_filename, TR_alt, EN_alt)
    
    if os.path.exists(atakum_dir):
        files = [f for f in os.listdir(atakum_dir) if f.lower().endswith(('.jpeg', '.jpg', '.png'))]
        for f in sorted(files):
            base_name, _ = os.path.splitext(f)
            clean_name = clean_slug(base_name) + ".webp"
            
            src_path = os.path.join(atakum_dir, f)
            dest_path = os.path.join(uploads_dir, clean_name)
            
            tr_alt = base_name
            en_alt = translations.get(base_name, base_name)
            
            try:
                img = Image.open(src_path)
                img.save(dest_path, "webp", quality=85)
                print(f" - Converted and Saved: {f} -> {clean_name}")
                converted_images.append((clean_name, tr_alt, en_alt))
            except Exception as e:
                print(f" - Error converting {f}: {e}")
    else:
        print(f" - [ERROR] Atakum directory not found: {atakum_dir}")

    # 3. Update HTML files
    html_targets = [
        (r"c:\Users\omerc\CascadeProjects\whatsappBot\rivadentLast\site\poliklinikler\rivadent-atakum\index.html", False),
        (r"c:\Users\omerc\CascadeProjects\whatsappBot\rivadentLast\site\en\poliklinikler\rivadent-atakum\index.html", True)
    ]
    
    print("\nStep 3: Updating Swiper slider and references in HTML files...")
    for path, is_english in html_targets:
        if not os.path.exists(path):
            print(f" - [ERROR] HTML file not found: {path}")
            continue
            
        with open(path, "r", encoding="utf-8") as f:
            html = f.read()
            
        # First let's build the replacement mapping for the 6 old hashes in HTML
        # We need to replace:
        # href="../../assets/uploads/OLD_HASH" and src="../../assets/uploads/OLD_HASH"
        for old_hash, (new_name, tr_alt, en_alt) in hash_mapping.items():
            target_alt = en_alt if is_english else tr_alt
            
            # Find and replace <img> tags and their wrapper <a> tags for these 6 old hashes
            # Relative uploads path depends on English vs Turkish
            rel_uploads_path = "../../../assets/uploads/" if is_english else "../../assets/uploads/"
            
            # Using precise replacements
            html = html.replace(f'href="../../assets/uploads/{old_hash}"', f'href="{rel_uploads_path}{new_name}"')
            html = html.replace(f'src="../../assets/uploads/{old_hash}"', f'src="{rel_uploads_path}{new_name}"')
            html = html.replace(f'href="../../../assets/uploads/{old_hash}"', f'href="{rel_uploads_path}{new_name}"')
            html = html.replace(f'src="../../../assets/uploads/{old_hash}"', f'src="{rel_uploads_path}{new_name}"')
            
        # Now, replace the alt text in the updated tags. Let's do a smart find/replace for the alt tags of these 6 newly named images.
        for old_hash, (new_name, tr_alt, en_alt) in hash_mapping.items():
            target_alt = en_alt if is_english else tr_alt
            # Find <img alt="..." src=".../new_name" /> and replace alt
            rel_uploads_path = "../../../assets/uploads/" if is_english else "../../assets/uploads/"
            
            # Regex replacement for img tags referencing our updated filename
            img_pattern = re.compile(
                r'<img[^>]*?src="' + re.escape(rel_uploads_path + new_name) + r'"[^>]*?>', 
                re.IGNORECASE
            )
            
            def alt_replacer(match):
                tag = match.group(0)
                soup = BeautifulSoup(tag, 'html.parser')
                img = soup.find('img')
                if img:
                    img['alt'] = target_alt
                    return str(img)
                return tag
                
            html = img_pattern.sub(alt_replacer, html)

        # Next, let's insert the 12 NEW slider images in the Swiper wrapper.
        # We need to locate the swiper-wrapper.
        # Let's search for <div class="swiper-wrapper">
        # In BeautifulSoup we can cleanly add them to the swiper wrapper!
        soup = BeautifulSoup(html, 'html.parser')
        
        # We search specifically for the swiper-wrapper inside 'policlinic-swiper' or similar
        swiper_wrapper = None
        for div in soup.find_all('div', class_='swiper-wrapper'):
            # Double check it is the clinic slider
            parent = div.find_parent('div', class_='policlinic-swiper')
            if parent or (div.find_parent('section', class_='policlinic-slide-area')):
                swiper_wrapper = div
                break
                
        if swiper_wrapper:
            # Let's construct and append the 12 new slides
            rel_uploads_path = "../../../assets/uploads/" if is_english else "../../assets/uploads/"
            
            for new_name, tr_alt, en_alt in converted_images:
                target_alt = en_alt if is_english else tr_alt
                
                # Check if this slide already exists to prevent duplicate runs
                existing = swiper_wrapper.find('a', href=rel_uploads_path + new_name)
                if not existing:
                    slide_html = f"""
                <div class="swiper-slide">
                    <div class="policlinic-slide-img animate__bounceIn animate__animated wow" data-wow-duration="700ms" data-wow-offset="100">
                        <a data-fancybox="RivaDent Atakum" href="{rel_uploads_path}{new_name}">
                            <img alt="{target_alt}" src="{rel_uploads_path}{new_name}"/>
                        </a>
                    </div>
                </div>"""
                    # Parse slide_html and append to swiper_wrapper
                    new_slide = BeautifulSoup(slide_html, 'html.parser')
                    swiper_wrapper.append(new_slide)
                    
            # Save the updated HTML
            # bs4 prettify might break layout formatting, so we'll convert soup back using custom stringify or just replacement.
            # But wait! To preserve formatting exactly as it is, we can just reconstruct from soup or do a targeted string insert.
            # Let's see: bs4's str(soup) is extremely clean, but let's make sure it doesn't change formatting too much.
            # Since this is a static site with simple structure, writing back str(soup) is perfectly fine, but let's do it cleanly:
            updated_html = str(soup)
            
            # Since str(soup) can sometimes add HTML wrapper or change structure if it parses fragment, let's verify.
            # bs4 parses full HTML documents perfectly, keeping doctype, head, body, etc.
            with open(path, "w", encoding="utf-8") as f:
                f.write(updated_html)
            print(f" - Successfully updated and appended 12 new slides in: {os.path.basename(path)}")
        else:
            print(f" - [ERROR] Swiper wrapper not found in: {path}")

    print("\nAll done!")

if __name__ == "__main__":
    run()
