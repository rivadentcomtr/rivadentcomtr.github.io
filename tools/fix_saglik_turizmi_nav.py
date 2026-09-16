#!/usr/bin/env python3
"""
Fix the misplaced Saglik Turizmi mobile nav li.
The previous script inserted a mobile-style <li> into the header-top-bar <ul>.
This script removes it from there. The mobile nav already has it placed correctly
via the Anlasmali Kurumlar match in the mobile section.

Actually looking at the output: the mobile li was inserted INSIDE the header-top ul
before the Anlasmali Kurumlar li that happens to be in that ul. We need to:
1. Remove the misplaced mobile-style li from inside header-top ul
2. Ensure mobile nav has the correct li before Anlasmali Kurumlar
"""

import re
from pathlib import Path

SITE_ROOT = Path(r"c:\Users\omerc\CascadeProjects\whatsappBot\rivadentLast\site")


def fix_file(path):
    content = path.read_text(encoding="utf-8")
    original = content

    if "tools" in str(path):
        return False
    if "saglik-turizmi" in str(path):
        return False

    # Check if the misplaced pattern exists:
    # A mobile-indent <li> right before the header-top Anlasmali Kurumlar <li>
    # Pattern: the mobile li has 12-space indent, sits inside the 20-space ul
    misplaced = re.compile(
        r'(\n            <li>\n                <a href="[^"]*saglik-turizmi[^"]*">\n                    [^\n]*</a>\n            </li>\n)(                                    <li>\n                                        <a href="[^"]*anlasmali-kurumlar)',
        re.MULTILINE
    )

    content = misplaced.sub(r'\2', content)

    # Now ensure mobile nav has the li. Find mobile Anlasmali Kurumlar
    # Mobile format: 12-space indent li
    mobile_anlasmali = re.compile(
        r'(            <li>\n                <a href="([^"]*anlasmali-kurumlar[^"]*)">\n                    Anlaşmalı Kurumlar[ ]*</a>\n            </li>)',
        re.MULTILINE
    )

    def add_mobile_saglik(m):
        # Already has saglik turizmi before it? Check won't happen here since we just cleaned
        full = m.group(0)
        href = m.group(2)
        # Derive saglik-turizmi path from anlasmali-kurumlar path
        saglik_href = href.replace("anlasmali-kurumlar/index.html", "sozlesme/saglik-turizmi/index.html")

        is_en = "en/" in saglik_href or "en\\" in saglik_href
        label = "Health Tourism" if is_en else "Sa\u011fl\u0131k Turizmi"

        mobile_li = (
            f'            <li>\n'
            f'                <a href="{saglik_href}">\n'
            f'                    {label}                </a>\n'
            f'            </li>\n'
        )
        return mobile_li + full

    # Only add if not already present before Anlasmali in mobile
    # We detect by checking if saglik-turizmi appears just before mobile Anlasmali
    def safe_add(m):
        start = m.start()
        preceding = content[max(0, start-200):start]
        if "saglik-turizmi" in preceding:
            return m.group(0)
        return add_mobile_saglik(m)

    content = mobile_anlasmali.sub(safe_add, content, count=1)

    if content != original:
        path.write_text(content, encoding="utf-8")
        return True
    return False


def main():
    print("=== Fix Saglik Turizmi mobile nav placement ===\n")
    files = list(SITE_ROOT.rglob("*.html"))
    changed = 0
    for f in files:
        if fix_file(f):
            changed += 1
            print(f"  Fixed: {f.relative_to(SITE_ROOT)}")
    print(f"\nChanged: {changed} files")


if __name__ == "__main__":
    main()
