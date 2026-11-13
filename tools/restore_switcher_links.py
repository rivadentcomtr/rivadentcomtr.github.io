#!/usr/bin/env python3
"""
Restore language-switcher links as SEO-neutral data attributes.

Google only treats <link rel="alternate" hreflang="..."> as an i18n signal.
The TR/EN switcher + auto-redirect in assets/i18n.js read those link tags,
so after removing hreflang we re-add the mapping with data-lang instead.

TR pages: if an en/ mirror exists, add
    <link rel="alternate" data-lang="en" href=".../en/.../">
EN pages: add tr + en + x-default lines as data-lang (all three).
"""

from pathlib import Path

SITE_ROOT = Path(r"c:\Users\omerc\CascadeProjects\whatsappBot\rivadentLast\site")
BASE_URL = "https://rivadent.com.tr"
EXCLUDE_DIRS = {"tools", "assets", ".git", ".github", ".claude", ".windsurf"}


def url_path_for(index_html):
    rel = index_html.relative_to(SITE_ROOT)
    parts = list(rel.parts)[:-1]  # drop index.html
    return "/" + "/".join(parts) + "/" if parts else "/"


def tr_page_exists(url_path):
    if url_path == "/":
        return (SITE_ROOT / "index.html").exists()
    return (SITE_ROOT / url_path.strip("/") / "index.html").exists()


def insert_after(lines, anchor_pred, new_lines):
    """Insert new_lines after first line matching anchor_pred."""
    for i, line in enumerate(lines):
        if anchor_pred(line):
            return lines[: i + 1] + new_lines + lines[i + 1 :]
    return lines


def process_tr(path, url_path):
    en_url_path = "/en" + ("" if url_path == "/" else url_path[:-1]) + "/"
    en_file = SITE_ROOT / "en" / url_path.strip("/") / "index.html"
    if not en_file.exists():
        return False

    text = path.read_text(encoding="utf-8")
    if 'data-lang="en"' in text:
        return False

    new_line = f'<link rel="alternate" data-lang="en" href="{BASE_URL}{en_url_path}"/>\n'
    lines = text.splitlines(keepends=True)
    lines = insert_after(
        lines,
        lambda l: 'hreflang="tr"' in l or 'rel="canonical"' in l,
        [new_line],
    )
    path.write_text("".join(lines), encoding="utf-8")
    return True


def process_en(path, en_url_path):
    text = path.read_text(encoding="utf-8")
    if 'data-lang="en"' in text:
        return False

    tr_url_path = en_url_path[3:]  # strip /en
    if not tr_url_path:
        tr_url_path = "/"
    indent = "    "
    new_lines = [
        f'{indent}<link rel="alternate" data-lang="tr" href="{BASE_URL}{tr_url_path}"/>\n',
        f'{indent}<link rel="alternate" data-lang="en" href="{BASE_URL}{en_url_path}"/>\n',
        f'{indent}<link rel="alternate" data-lang="x-default" href="{BASE_URL}{tr_url_path}"/>\n',
    ]
    lines = text.splitlines(keepends=True)
    lines = insert_after(lines, lambda l: 'rel="canonical"' in l, new_lines)
    path.write_text("".join(lines), encoding="utf-8")
    return True


def main():
    tr_count = en_count = 0
    for f in sorted(SITE_ROOT.rglob("index.html")):
        rel = f.relative_to(SITE_ROOT)
        if any(p in EXCLUDE_DIRS for p in rel.parts):
            continue
        url_path = url_path_for(f)
        if rel.parts[0] == "en":
            if process_en(f, url_path):
                en_count += 1
        else:
            if process_tr(f, url_path):
                tr_count += 1
    print(f"data-lang links restored: {tr_count} TR files, {en_count} EN files")


if __name__ == "__main__":
    main()
