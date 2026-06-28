import os
import re
from bs4 import BeautifulSoup

def find_html_files(root_dir):
    html_files = []
    for root, dirs, files in os.walk(root_dir):
        # Skip git or build/back directories if any
        if ".git" in root or "assets/back" in root:
            continue
        for file in files:
            if file.endswith(".html"):
                html_files.append(os.path.join(root, file))
    return html_files

def analyze_images():
    root_dir = r"c:\Users\omerc\CascadeProjects\whatsappBot\rivadentLast\site"
    html_files = find_html_files(root_dir)
    print(f"Found {len(html_files)} HTML files to scan.")

    all_images = []
    empty_alt_count = 0
    missing_alt_count = 0
    total_img_count = 0

    for file_path in html_files:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                soup = BeautifulSoup(content, 'html.parser')
                img_tags = soup.find_all('img')
                for img in img_tags:
                    total_img_count += 1
                    src = img.get('src', '')
                    alt = img.get('alt', None)
                    
                    if alt is None:
                        missing_alt_count += 1
                        alt_status = "MISSING"
                    elif alt.strip() == "":
                        empty_alt_count += 1
                        alt_status = "EMPTY"
                    else:
                        alt_status = f"PRESENT: '{alt}'"
                    
                    all_images.append({
                        'file': os.path.relpath(file_path, root_dir),
                        'src': src,
                        'alt': alt,
                        'status': alt_status
                    })
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

    print("\n" + "="*50)
    print("IMAGE ALT TAG ANALYSIS")
    print("="*50)
    print(f"Total HTML files scanned: {len(html_files)}")
    print(f"Total <img> tags found: {total_img_count}")
    print(f"Images with missing alt attribute: {missing_alt_count}")
    print(f"Images with empty alt='': {empty_alt_count}")
    print(f"Images with filled alt: {total_img_count - missing_alt_count - empty_alt_count}")
    print("="*50)

    # Let's list those with missing or empty alt tags
    print("\nImages needing ALT tags:")
    unfilled = [img for img in all_images if img['status'] in ("MISSING", "EMPTY")]
    for idx, img in enumerate(unfilled[:30]):
        print(f" {idx+1}. File: {img['file']}")
        print(f"    Src:  {img['src']}")
        print(f"    Alt:  {img['alt']}")
    if len(unfilled) > 30:
        print(f" ... and {len(unfilled) - 30} more images.")

if __name__ == "__main__":
    analyze_images()
