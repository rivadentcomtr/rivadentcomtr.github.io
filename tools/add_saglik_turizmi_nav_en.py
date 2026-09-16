#!/usr/bin/env python3
"""
Add Health Tourism link (with logo) to EN nav pages.
Header top bar: insert BEFORE About Us li
Mobile nav: insert BEFORE Contracted Institutions li
"""

import re
from pathlib import Path

SITE_ROOT = Path(r"c:\Users\omerc\CascadeProjects\whatsappBot\rivadentLast\site")
EN_ROOT = SITE_ROOT / "en"


def process_file(path):
    content = path.read_text(encoding="utf-8")
    original = content

    if "tools" in str(path):
        return False
    if "saglik-turizmi" in str(path):
        return False
    # Already done
    if "turkiye-saglik-turizmi-logosu" in content:
        return False

    depth = len(path.relative_to(SITE_ROOT).parts) - 1
    prefix = "../" * depth
    saglik_href = prefix + "sozlesme/saglik-turizmi/index.html"
    logo_src = prefix + "assets/uploads/turkiye-saglik-turizmi-logosu.webp"

    # 1. Header top bar — insert before "About Us" li
    top_li = (
        f'                                    <li>\n'
        f'                                        <a href="{saglik_href}">\n'
        f'                                            <img src="{logo_src}" alt="T\u00fcrkiye Sa\u011fl\u0131k Turizmi" '
        f'style="height:18px;vertical-align:middle;margin-right:5px;"/>Health Tourism                                        </a>\n'
        f'                                    </li>\n'
    )

    about_pattern = re.compile(
        r'([ \t]*<li>[ \t]*\n[ \t]*<a href="[^"]*hakkimizda[^"]*">[ \t]*\n[ \t]*About Us[ \t]*</a>[ \t]*\n[ \t]*</li>)',
        re.MULTILINE
    )
    content = about_pattern.sub(top_li + r'\1', content, count=1)

    # 2. Mobile nav — insert before "Contracted Institutions" li
    mobile_li = (
        f'            <li>\n'
        f'                <a href="{saglik_href}">\n'
        f'                    Health Tourism                </a>\n'
        f'            </li>\n'
    )

    contracted_pattern = re.compile(
        r'(            <li>\n                <a href="[^"]*anlasmali-kurumlar[^"]*">\n                    Contracted Institutions[ ]*</a>\n            </li>)',
        re.MULTILINE
    )
    content = contracted_pattern.sub(mobile_li + r'\1', content, count=1)

    if content != original:
        path.write_text(content, encoding="utf-8")
        return True
    return False


def main():
    print("=== Add Health Tourism to EN nav ===\n")
    files = list(EN_ROOT.rglob("*.html"))
    changed = 0
    for f in files:
        if process_file(f):
            changed += 1
            print(f"  Updated: {f.relative_to(SITE_ROOT)}")
    print(f"\nChanged: {changed} files")


if __name__ == "__main__":
    main()
