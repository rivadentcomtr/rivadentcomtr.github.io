#!/usr/bin/env python3
"""
Fix turkiye-saglik-turizmi-logosu.webp src path in EN pages.
The previous fix script accidentally added an extra ../ level.
Correct src should be ("../" * depth) + "assets/uploads/..."
where depth = number of directory levels from SITE_ROOT.
"""

import re
from pathlib import Path

SITE_ROOT = Path(r"c:\Users\omerc\CascadeProjects\whatsappBot\rivadentLast\site")
EN_ROOT = SITE_ROOT / "en"
LOGO_FILENAME = "turkiye-saglik-turizmi-logosu.webp"


def process_file(path):
    content = path.read_text(encoding="utf-8")

    parts = path.relative_to(SITE_ROOT).parts
    depth = len(parts) - 1
    correct_src = ("../" * depth) + "assets/uploads/" + LOGO_FILENAME

    # Find current src attribute value for this logo
    pattern = re.compile(
        r'src="([^"]*turkiye-saglik-turizmi-logosu\.webp)"'
    )
    m = pattern.search(content)
    if not m:
        return False

    current_src = m.group(1)
    if current_src == correct_src:
        return False  # already correct

    new_content = pattern.sub(f'src="{correct_src}"', content)
    path.write_text(new_content, encoding="utf-8")
    print(f"  Fixed [{current_src}] -> [{correct_src}] in {path.relative_to(SITE_ROOT)}")
    return True


def main():
    print("=== Fix EN logo src paths ===\n")
    files = list(EN_ROOT.rglob("*.html"))
    changed = 0
    for f in files:
        if process_file(f):
            changed += 1
    print(f"\nChanged: {changed} files")


if __name__ == "__main__":
    main()
