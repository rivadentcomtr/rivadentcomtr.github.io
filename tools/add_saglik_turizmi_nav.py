#!/usr/bin/env python3
"""
Add Saglik Turizmi link (with logo) to nav:
1. Header top bar: insert BEFORE Hakkimizda li
2. Mobile nav: insert BEFORE Anlasmali Kurumlar li
"""

from pathlib import Path
import re

SITE_ROOT = Path(r"c:\Users\omerc\CascadeProjects\whatsappBot\rivadentLast\site")


def make_top_bar_li(prefix, is_en):
    if is_en:
        label = "Health Tourism"
        path = prefix + "sozlesme/saglik-turizmi/index.html"
    else:
        label = "Sa\u011fl\u0131k Turizmi"
        path = prefix + "sozlesme/saglik-turizmi/index.html"

    logo = prefix + "assets/uploads/turkiye-saglik-turizmi-logosu.webp"

    return (
        f'                                    <li>\n'
        f'                                        <a href="{path}">\n'
        f'                                            <img src="{logo}" alt="T\u00fcrkiye Sa\u011fl\u0131k Turizmi" '
        f'style="height:18px;vertical-align:middle;margin-right:5px;"/>'
        f'{label}                                        </a>\n'
        f'                                    </li>\n'
    )


def make_mobile_li(prefix, is_en):
    if is_en:
        label = "Health Tourism"
        path = prefix + "sozlesme/saglik-turizmi/index.html"
    else:
        label = "Sa\u011fl\u0131k Turizmi"
        path = prefix + "sozlesme/saglik-turizmi/index.html"

    return (
        f'            <li>\n'
        f'                <a href="{path}">\n'
        f'                    {label}                </a>\n'
        f'            </li>\n'
    )


def process_file(path):
    content = path.read_text(encoding="utf-8")
    original = content

    if "tools" in str(path):
        return False

    # Already added
    if "saglik-turizmi" in content and "turkiye-saglik-turizmi-logosu" in content:
        return False

    # Skip the saglik-turizmi page itself
    if "saglik-turizmi" in str(path):
        return False

    # Determine path prefix (../../ etc.)
    depth = len(path.relative_to(SITE_ROOT).parts) - 1
    prefix = "../" * depth

    is_en = "\\en\\" in str(path) or "/en/" in str(path)

    # 1. Header top bar — insert before Hakkimizda li
    top_li = make_top_bar_li(prefix, is_en)

    hakkimizda_pattern = re.compile(
        r'([ \t]*<li>[ \t]*\n[ \t]*<a href="[^"]*hakkimizda[^"]*">[ \t]*\n[ \t]*Hakkımızda[ \t]*</a>[ \t]*\n[ \t]*</li>)',
        re.MULTILINE
    )
    content = hakkimizda_pattern.sub(top_li + r'\1', content, count=1)

    # 2. Mobile nav — insert before Anlasmali Kurumlar li
    mobile_li = make_mobile_li(prefix, is_en)

    anlasmali_pattern = re.compile(
        r'([ \t]*<li>[ \t]*\n[ \t]*<a href="[^"]*anlasmali-kurumlar[^"]*">[ \t]*\n[ \t]*Anlaşmalı Kurumlar[ \t]*</a>[ \t]*\n[ \t]*</li>)',
        re.MULTILINE
    )
    content = anlasmali_pattern.sub(mobile_li + r'\1', content, count=1)

    if content != original:
        path.write_text(content, encoding="utf-8")
        return True
    return False


def main():
    print("=== Add Saglik Turizmi to nav ===\n")
    files = list(SITE_ROOT.rglob("*.html"))
    changed = 0
    for f in files:
        if process_file(f):
            changed += 1
            print(f"  Updated: {f.relative_to(SITE_ROOT)}")
    print(f"\nChanged: {changed} files")


if __name__ == "__main__":
    main()
