#!/usr/bin/env python3
"""
RivaDent site bulk update:
1. Convert JPEG images to WebP
2. Replace Sultan Tas with Aleyna Beray Kidak in nav + team listings
3. Remove Osman Kilic from all pages
"""

import re
from pathlib import Path

SITE_ROOT = Path(r"c:\Users\omerc\CascadeProjects\whatsappBot\rivadentLast\site")


def convert_images():
    try:
        from PIL import Image
        uploads = SITE_ROOT / "assets" / "uploads"
        for name in ["dt-aleyna-beray-kidak.jpeg", "maltepe-saglik-turizmi.jpeg"]:
            src = uploads / name
            dst = uploads / name.replace(".jpeg", ".webp")
            if src.exists():
                img = Image.open(src)
                img.save(str(dst), "WebP", quality=85)
                print(f"  Converted: {dst.name}")
            else:
                print(f"  Not found: {src}")
    except Exception as e:
        print(f"  Image error: {e}")


def find_matching_close_div(html, start):
    """Return end pos (exclusive) of the <div> block opening at 'start'."""
    depth = 0
    i = start
    n = len(html)
    while i < n:
        if html[i:i+4] == '<div':
            if i + 4 >= n or html[i + 4] in (' ', '\t', '\n', '>'):
                depth += 1
            gt = html.find('>', i)
            i = (gt + 1) if gt != -1 else (i + 4)
        elif html[i:i+6] == '</div>':
            depth -= 1
            if depth == 0:
                return i + 6
            i += 6
        else:
            i += 1
    return n


def remove_col_div_with_identifier(content, identifier):
    """Remove col-lg-3 team card <div> blocks that contain identifier."""
    search_str = '<div class="col-lg-3 col-md-4 col-sm-6 col-6">'
    result = []
    i = 0
    while True:
        pos = content.find(search_str, i)
        if pos == -1:
            result.append(content[i:])
            break
        end = find_matching_close_div(content, pos)
        block = content[pos:end]
        if identifier in block:
            before = content[i:pos].rstrip('\n')
            result.append(before)
            result.append('\n')
        else:
            result.append(content[i:end])
        i = end
    return ''.join(result)


def process_file(path):
    content = path.read_text(encoding='utf-8')
    original = content

    path_str = str(path).replace('\\', '/')
    skip_sultan = 'dt-sultan-tas' in path_str
    skip_osman = 'dt-osman-kilic' in path_str

    # --- Sultan Tas -> Aleyna Beray ---
    if not skip_sultan:
        content = content.replace('dt-sultan-tas', 'dt-aleyna-beray-kidak')
        content = content.replace('Dt. Sultan Taş', 'Dt. Aleyna Beray Kıdak')
        # Replace image hash
        content = content.replace(
            'a90a8c50d68f215d71c0fb026ee64f3b.webp',
            'dt-aleyna-beray-kidak.webp'
        )
        # Remove Sultan Tas instagram li (sultipo)
        content = re.sub(
            r'\s*<li>\s*\n?\s*<a href="https://www\.instagram\.com/sultipo/?"[^>]*>.*?</a>\s*\n?\s*</li>',
            '',
            content,
            flags=re.DOTALL
        )

    # --- Osman Kilic: remove nav li blocks ---
    if not skip_osman:
        # Desktop/mobile nav li blocks
        content = re.sub(
            r'\s*<li>\s*\n?\s*<a\s+href="[^"]*dt-osman-kilic[^"]*"[^>]*>\s*\n?\s*Dt\.\s*Osman\s*Kılıç[^<]*</a>\s*\n?\s*</li>',
            '',
            content,
            flags=re.DOTALL
        )
        # Remove Osman Kilic team card blocks
        content = remove_col_div_with_identifier(content, 'dt-osman-kilic')
        # Remove Osman Kilic option in modal selects
        content = re.sub(
            r'\s*<option[^>]*>\s*Dt\.\s*Osman\s*Kılıç\s*</option>',
            '',
            content
        )

    if content != original:
        path.write_text(content, encoding='utf-8')
        return True
    return False


def main():
    print("=== RivaDent Site Bulk Update ===\n")

    print("1. Converting images...")
    convert_images()

    print("\n2. Updating HTML files...")
    files = list(SITE_ROOT.rglob("*.html"))
    changed = 0
    for f in files:
        if process_file(f):
            changed += 1
    print(f"   Changed: {changed}/{len(files)} files")

    print("\nDone.")


if __name__ == "__main__":
    main()
