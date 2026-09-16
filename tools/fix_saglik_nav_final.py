#!/usr/bin/env python3
"""
Remove ALL saglik-turizmi nav li items, then add back ONLY the logo one
in the header-top bar (before Hakkimizda/About Us). No mobile nav item.
"""

import re
from pathlib import Path

SITE_ROOT = Path(r"c:\Users\omerc\CascadeProjects\whatsappBot\rivadentLast\site")


def remove_all_saglik_nav(content):
    pattern = re.compile(
        r'\s*<li>\s*<a href="[^"]*saglik-turizmi[^"]*"[^>]*>.*?</a>\s*</li>',
        re.DOTALL
    )
    return pattern.sub('', content)


def insert_header_top_item(content, prefix, is_en):
    saglik_href = prefix + "sozlesme/saglik-turizmi/index.html"
    logo_src = prefix + "assets/uploads/turkiye-saglik-turizmi-logosu.webp"
    label = "Health Tourism" if is_en else "Sa\u011fl\u0131k Turizmi"

    new_li = (
        f'\n                                    <li>\n'
        f'                                        <a href="{saglik_href}">\n'
        f'                                            <img src="{logo_src}" alt="T\u00fcrkiye Sa\u011fl\u0131k Turizmi" '
        f'style="height:18px;vertical-align:middle;margin-right:5px;"/>{label}                                        </a>\n'
        f'                                    </li>'
    )

    hakkimizda_text = "About Us" if is_en else "Hakk\u0131m\u0131zda"
    pattern = re.compile(
        r'(<li[^>]*>\s*<a href="[^"]*hakkimizda[^"]*"[^>]*>\s*' + re.escape(hakkimizda_text) + r'\s*</a>\s*</li>)',
        re.DOTALL
    )
    return pattern.sub(new_li + r'\n\1', content, count=1)


def process_file(path):
    content = path.read_text(encoding="utf-8")
    original = content

    if "tools" in str(path):
        return False
    if "saglik-turizmi" in str(path):
        return False
    if "hakkimizda" not in content:
        return False

    depth = len(path.relative_to(SITE_ROOT).parts) - 1
    prefix = "../" * depth
    is_en = "\\en\\" in str(path) or str(path).replace("\\", "/").find("/en/") != -1

    content = remove_all_saglik_nav(content)
    content = insert_header_top_item(content, prefix, is_en)

    if content != original:
        path.write_text(content, encoding="utf-8")
        return True
    return False


def main():
    print("=== Fix Saglik Turizmi nav (logo only, header-top only) ===\n")
    files = list(SITE_ROOT.rglob("*.html"))
    changed = 0
    for f in files:
        if process_file(f):
            changed += 1
            print(f"  Updated: {f.relative_to(SITE_ROOT)}")
    print(f"\nChanged: {changed} files")


if __name__ == "__main__":
    main()
