#!/usr/bin/env python3
"""
Regenerate sitemap.xml from all HTML files in the site.
- Pairs TR and EN pages via hreflang alternates
- Uses today's date as lastmod
- Excludes: tools/, error pages, saglik-turizmi self-duplicate entries
"""

from pathlib import Path
from datetime import date

SITE_ROOT = Path(r"c:\Users\omerc\CascadeProjects\whatsappBot\rivadentLast\site")
BASE_URL = "https://rivadent.com.tr"
TODAY = date.today().isoformat()  # 2026-09-16

EXCLUDE_DIRS = {"tools", "assets", ".git"}
EXCLUDE_PATHS = set()  # add specific paths to exclude if needed


def get_url_path(html_file):
    """Convert file path to URL path, e.g. tedavi/ortodonti/index.html -> /tedavi/ortodonti/"""
    rel = html_file.relative_to(SITE_ROOT)
    parts = list(rel.parts)
    # Remove 'index.html' at the end
    if parts[-1] == "index.html":
        parts = parts[:-1]
    if not parts:
        return "/"
    return "/" + "/".join(parts) + "/"


def is_en(html_file):
    parts = html_file.relative_to(SITE_ROOT).parts
    return len(parts) > 0 and parts[0] == "en"


def collect_pages():
    """Return list of (tr_url, en_url) pairs, or (url, None) for TR-only pages."""
    tr_pages = {}
    en_pages = {}

    for f in sorted(SITE_ROOT.rglob("index.html")):
        parts = f.relative_to(SITE_ROOT).parts

        # Skip excluded dirs
        if any(p in EXCLUDE_DIRS for p in parts):
            continue

        url_path = get_url_path(f)

        if is_en(f):
            # Strip leading /en from the path to get the key
            key = url_path[3:] if url_path.startswith("/en/") else url_path
            if key == "/":
                key = "/__root__"
            en_pages[key] = url_path
        else:
            tr_pages[url_path] = url_path

    return tr_pages, en_pages


def build_url_entry(tr_path, en_path, priority="0.8"):
    loc = BASE_URL + tr_path
    tr_href = BASE_URL + tr_path
    en_href = BASE_URL + en_path if en_path else None

    lines = [
        "  <url>",
        f"    <loc>{loc}</loc>",
        f'    <xhtml:link rel="alternate" hreflang="tr" href="{tr_href}"/>',
    ]
    if en_href:
        lines.append(f'    <xhtml:link rel="alternate" hreflang="en" href="{en_href}"/>')
        lines.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{tr_href}"/>')
    lines += [
        f"    <lastmod>{TODAY}</lastmod>",
        "    <changefreq>weekly</changefreq>",
        f"    <priority>{priority}</priority>",
        "  </url>",
    ]
    return "\n".join(lines)


def get_priority(tr_path):
    if tr_path == "/":
        return "1.0"
    if any(tr_path.startswith(p) for p in ["/hekim/", "/en/hekim/"]):
        return "0.7"
    if any(tr_path.startswith(p) for p in ["/blog/"]):
        return "0.6"
    return "0.8"


def main():
    tr_pages, en_pages = collect_pages()

    entries = []
    used_en = set()

    for tr_path in sorted(tr_pages.keys()):
        # Determine key for EN lookup
        key = tr_path
        if key == "/":
            key = "/__root__"

        en_path = en_pages.get(key)
        if en_path:
            used_en.add(key)

        priority = get_priority(tr_path)
        entries.append(build_url_entry(tr_path, en_path, priority))

    # Add any EN-only pages (shouldn't happen normally)
    for key, en_path in sorted(en_pages.items()):
        if key not in used_en:
            entries.append(build_url_entry(en_path, en_path, "0.7"))

    sitemap = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
        '        xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        + "\n".join(entries)
        + "\n</urlset>\n"
    )

    out = SITE_ROOT / "sitemap.xml"
    out.write_text(sitemap, encoding="utf-8")
    print(f"Written {len(entries)} URL entries to sitemap.xml")
    print(f"  TR pages: {len(tr_pages)}")
    print(f"  EN pages: {len(en_pages)}")


if __name__ == "__main__":
    main()
