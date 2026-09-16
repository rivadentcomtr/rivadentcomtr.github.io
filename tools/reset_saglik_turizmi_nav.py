#!/usr/bin/env python3
"""
Clean all saglik-turizmi nav entries and re-add correctly.
Handles both indented and collapsed HTML structures.
"""

import re
from pathlib import Path

SITE_ROOT = Path(r"c:\Users\omerc\CascadeProjects\whatsappBot\rivadentLast\site")


# ── STEP 1: Remove all previously-inserted saglik-turizmi nav items ──────────

def remove_all_saglik_nav_items(content):
    # Remove any <li> containing saglik-turizmi link (with or without logo)
    # Matches both indented and collapsed forms
    pattern = re.compile(
        r'\s*<li>\s*<a href="[^"]*saglik-turizmi[^"]*"[^>]*>.*?</a>\s*</li>',
        re.DOTALL
    )
    return pattern.sub('', content)


# ── STEP 2: Insert header-top item (with logo) before Hakkımızda/About Us ────

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

    # Match hakkimizda li in header-top — handles both indented and collapsed
    # Look for <li> ... hakkimizda ... Hakkımızda/About Us ... </li>
    hakkimizda_text = "About Us" if is_en else "Hakk\u0131m\u0131zda"
    pattern = re.compile(
        r'(<li[^>]*>\s*<a href="[^"]*hakkimizda[^"]*"[^>]*>\s*' + re.escape(hakkimizda_text) + r'\s*</a>\s*</li>)',
        re.DOTALL
    )
    return pattern.sub(new_li + r'\n\1', content, count=1)


# ── STEP 3: Insert mobile nav item before Anlaşmalı Kurumlar ─────────────────

def insert_mobile_item(content, prefix, is_en):
    saglik_href = prefix + "sozlesme/saglik-turizmi/index.html"
    label = "Health Tourism" if is_en else "Sa\u011fl\u0131k Turizmi"

    new_li = (
        f'\n            <li>\n'
        f'                <a href="{saglik_href}">\n'
        f'                    {label}                </a>\n'
        f'            </li>'
    )

    anlasmali_text = "Contracted Institutions" if is_en else "Anla\u015fmal\u0131 Kurumlar"
    pattern = re.compile(
        r'(<li[^>]*>\s*<a href="[^"]*anlasmali-kurumlar[^"]*"[^>]*>\s*' + re.escape(anlasmali_text) + r'\s*</a>\s*</li>)',
        re.DOTALL
    )
    return pattern.sub(new_li + r'\n\1', content, count=1)


# ── Main ──────────────────────────────────────────────────────────────────────

def process_file(path):
    content = path.read_text(encoding="utf-8")
    original = content

    if "tools" in str(path):
        return False
    if "saglik-turizmi" in str(path):
        return False
    # Must have hakkimizda to be a page with nav
    if "hakkimizda" not in content:
        return False

    depth = len(path.relative_to(SITE_ROOT).parts) - 1
    prefix = "../" * depth
    is_en = "\\en\\" in str(path) or str(path).replace("/","\\").startswith(str(SITE_ROOT / "en"))

    content = remove_all_saglik_nav_items(content)
    content = insert_header_top_item(content, prefix, is_en)
    content = insert_mobile_item(content, prefix, is_en)

    if content != original:
        path.write_text(content, encoding="utf-8")
        return True
    return False


def main():
    print("=== Reset Saglik Turizmi nav (clean rebuild) ===\n")
    files = list(SITE_ROOT.rglob("*.html"))
    changed = 0
    for f in files:
        if process_file(f):
            changed += 1
            print(f"  Updated: {f.relative_to(SITE_ROOT)}")
    print(f"\nChanged: {changed} files")


if __name__ == "__main__":
    main()
