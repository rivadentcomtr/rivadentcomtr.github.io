#!/usr/bin/env python3
"""
Fix EN pages saglik-turizmi links:
1. href was pointing to root TR version - fix to point to en/ version
2. EN hakkimizda img src was wrong (manually set with short prefix)
"""

from pathlib import Path

SITE_ROOT = Path(r"c:\Users\omerc\CascadeProjects\whatsappBot\rivadentLast\site")
EN_ROOT = SITE_ROOT / "en"
LOGO_FILE = "turkiye-saglik-turizmi-logosu.webp"


def process_file(path):
    content = path.read_text(encoding="utf-8")
    original = content

    parts = path.relative_to(SITE_ROOT).parts
    depth = len(parts) - 1  # number of dirs from SITE_ROOT

    # For EN files: link should use (depth-1) levels up to stay inside en/
    root_prefix = "../" * depth       # what the script generated (goes to root = TR)
    en_prefix = "../" * (depth - 1)   # correct for EN (stays inside en/)

    # Fix href: root_prefix + sozlesme → en_prefix + sozlesme
    wrong_href = root_prefix + "sozlesme/saglik-turizmi/index.html"
    correct_href = en_prefix + "sozlesme/saglik-turizmi/index.html"

    if wrong_href in content:
        content = content.replace(wrong_href, correct_href)

    # Fix img src: must always point to root assets (not en/assets which doesn't exist)
    # If someone manually added shorter prefix for the logo, fix it
    if root_prefix != en_prefix:  # only when depth > 1
        wrong_img = en_prefix + "assets/uploads/" + LOGO_FILE
        correct_img = root_prefix + "assets/uploads/" + LOGO_FILE
        if wrong_img in content:
            content = content.replace(wrong_img, correct_img)

    if content != original:
        path.write_text(content, encoding="utf-8")
        return True
    return False


def main():
    print("=== Fix EN saglik-turizmi links ===\n")
    files = list(EN_ROOT.rglob("*.html"))
    changed = 0
    for f in files:
        if process_file(f):
            changed += 1
            print(f"  Updated: {f.relative_to(SITE_ROOT)}")
    print(f"\nChanged: {changed} files")


if __name__ == "__main__":
    main()
