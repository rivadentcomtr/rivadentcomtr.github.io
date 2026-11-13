#!/usr/bin/env python3
"""
Remove English pages from SEO scope.

TR pages (everything outside en/):
  - drop the <link ... hreflang="en" ...> alternate line (keeps canonical,
    hreflang="tr" and x-default)

EN pages (en/):
  - switch robots meta to "noindex, follow"
  - drop ALL hreflang alternate link lines (tr/en/x-default), keep canonical

Pages themselves are kept; the TR/EN language switcher stays untouched.
"""

from pathlib import Path

SITE_ROOT = Path(r"c:\Users\omerc\CascadeProjects\whatsappBot\rivadentLast\site")
EXCLUDE_DIRS = {"tools", "assets", ".git", ".github", ".claude", ".windsurf"}


def iter_html_files():
    for f in sorted(SITE_ROOT.rglob("*.html")):
        rel = f.relative_to(SITE_ROOT)
        if any(p in EXCLUDE_DIRS for p in rel.parts):
            continue
        yield f, rel


def is_en(rel):
    return rel.parts[0] == "en"


def process_tr(path):
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    kept, removed = [], 0
    for line in lines:
        if 'hreflang="en"' in line:
            removed += 1
            continue
        kept.append(line)
    if removed:
        path.write_text("".join(kept), encoding="utf-8")
    return removed


def process_en(path):
    text = path.read_text(encoding="utf-8")
    changed = False

    for old in (
        'content="index, follow" name="robots"',
        'name="robots" content="index, follow"',
    ):
        if old in text:
            text = text.replace(old, old.replace("index", "noindex"))
            changed = True

    lines = text.splitlines(keepends=True)
    kept, removed = [], 0
    for line in lines:
        if "hreflang=" in line:
            removed += 1
            continue
        kept.append(line)
    if removed:
        text = "".join(kept)
        changed = True

    if changed:
        path.write_text(text, encoding="utf-8")
    return removed


def main():
    tr_files = tr_links = en_files = en_links = 0
    for f, rel in iter_html_files():
        if is_en(rel):
            n = process_en(f)
            if n:
                en_files += 1
                en_links += n
        else:
            n = process_tr(f)
            if n:
                tr_files += 1
                tr_links += n

    print(f"TR: removed {tr_links} hreflang=en links from {tr_files} files")
    print(f"EN: noindex + removed {en_links} hreflang links in {en_files} files")


if __name__ == "__main__":
    main()
