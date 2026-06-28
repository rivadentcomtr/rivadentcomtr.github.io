import os
import re
from bs4 import BeautifulSoup

def rename_physical_files():
    uploads_dir = r"c:\Users\omerc\CascadeProjects\whatsappBot\rivadentLast\site\assets\uploads"
    
    mapping = {
        "74c15a765dc471ebe9e8d692ac6e2a01.webp": "rivadent-dental-implant-tedavisi.webp",
        "3d29acd43887fa3d5d3457aa59a19f47.webp": "rivadent-agiz-dis-ve-cene-cerrahisi.webp",
        "9a1038ec8825ff77c038b5e542bfc1d4.webp": "rivadent-protez-dis-tedavisi.webp",
        "040599794430ea847a31b6c429e20360.webp": "rivadent-restoratif-dis-tedavisi.webp",
        "6ad9e4d290eca2e763e7c80a3ca84e39.webp": "rivadent-dis-beyazlatma-tedavisi.webp",
        "e320033faa16d728988b1f4d854af1fc.webp": "rivadent-endodonti-kanal-tedavisi.webp",
        "16945f9a545a12a8acb4851ec8f90c91.webp": "rivadent-zirkonyum-kaplama.webp",
        "01e9d3f11eb7c4750b1e0533b59b65bd.webp": "rivadent-periodontoloji-dis-eti-tedavisi.webp",
        "b43257cf9309ec5bb9b959b7397cb05b.webp": "rivadent-gulus-tasarimi.webp",
        "c8a21494cf6581b7a2c3c19db5bf5d0f.webp": "rivadent-ortodonti-tedavisi.webp"
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
        "74c15a765dc471ebe9e8d692ac6e2a01.webp": (
            "rivadent-dental-implant-tedavisi.webp", 
            "Rivadent Dental İmplant Tedavisi", 
            "Rivadent Dental Implant Treatment"
        ),
        "3d29acd43887fa3d5d3457aa59a19f47.webp": (
            "rivadent-agiz-dis-ve-cene-cerrahisi.webp", 
            "Rivadent Ağız, Diş ve Çene Cerrahisi", 
            "Rivadent Oral and Maxillofacial Surgery"
        ),
        "9a1038ec8825ff77c038b5e542bfc1d4.webp": (
            "rivadent-protez-dis-tedavisi.webp", 
            "Rivadent Protez Diş Tedavisi", 
            "Rivadent Prosthetic Dental Treatment"
        ),
        "040599794430ea847a31b6c429e20360.webp": (
            "rivadent-restoratif-dis-tedavisi.webp", 
            "Restoratif Diş Tedavisi | RivaDent", 
            "Restorative Dental Treatment | RivaDent"
        ),
        "6ad9e4d290eca2e763e7c80a3ca84e39.webp": (
            "rivadent-dis-beyazlatma-tedavisi.webp", 
            "Diş Beyazlatma Tedavisi | RivaDent", 
            "Teeth Whitening Treatment | RivaDent"
        ),
        "e320033faa16d728988b1f4d854af1fc.webp": (
            "rivadent-endodonti-kanal-tedavisi.webp", 
            "Endodonti Kanal Tedavisi | RivaDent", 
            "Endodontic Root Canal Treatment | RivaDent"
        ),
        "16945f9a545a12a8acb4851ec8f90c91.webp": (
            "rivadent-zirkonyum-kaplama.webp", 
            "Zirkonyum Kaplama | RivaDent", 
            "Zirconium Crowns | RivaDent"
        ),
        "01e9d3f11eb7c4750b1e0533b59b65bd.webp": (
            "rivadent-periodontoloji-dis-eti-tedavisi.webp", 
            "Periodontoloji Diş Eti Tedavisi | RivaDent", 
            "Periodontology Gum Treatment | RivaDent"
        ),
        "b43257cf9309ec5bb9b959b7397cb05b.webp": (
            "rivadent-gulus-tasarimi.webp", 
            "Gülüş Tasarımı | RivaDent", 
            "Smile Design | RivaDent"
        ),
        "c8a21494cf6581b7a2c3c19db5bf5d0f.webp": (
            "rivadent-ortodonti-tedavisi.webp", 
            "Ortodonti Tedavisi | RivaDent", 
            "Orthodontic Treatment | RivaDent"
        )
    }

    print("\nScanning and updating HTML files...")
    
    # Let's find all HTML files
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
            
            # For each target image, search and replace in raw text
            # We look for <img ... src="...old_name..." ...> or similar pattern.
            # Using regex to match <img> tags specifically is safer.
            for old_name, (new_name, tr_alt, en_alt) in image_data.items():
                if old_name in content:
                    target_alt = en_alt if is_english else tr_alt
                    
                    # Regex to find an <img> tag containing the old_name inside its src attribute
                    # This captures the whole tag so we can parse and rebuild it.
                    def replacer(match):
                        tag_str = match.group(0)
                        # Rebuild tag safely using BeautifulSoup
                        soup = BeautifulSoup(tag_str, 'html.parser')
                        img = soup.find('img')
                        if img:
                            src = img.get('src', '')
                            if old_name in src:
                                img['src'] = src.replace(old_name, new_name)
                            img['alt'] = target_alt
                            
                            # Standardize output format
                            # BeautifulSoup outputs self-closing as <img .../> which is great
                            return str(img)
                        return tag_str

                    # Find <img> tags that reference the old file
                    img_pattern = re.compile(r'<img[^>]*?src="[^"]*?' + re.escape(old_name) + r'"[^>]*?>', re.IGNORECASE)
                    content = img_pattern.sub(replacer, content)

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
