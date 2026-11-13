#!/usr/bin/env python3
"""
Regenerate sitemap.xml from all TR HTML files in the site.
- TR only: en/ pages are excluded (noindex'd, out of SEO scope)
- No hreflang alternates (single-language site)
- Uses today's date as lastmod
- Excludes: tools/, assets/, error pages
"""

from pathlib import Path
from datetime import date

SITE_ROOT = Path(r"c:\Users\omerc\CascadeProjects\whatsappBot\rivadentLast\site")
BASE_URL = "https://rivadent.com.tr"
TODAY = date.today().isoformat()

EXCLUDE_DIRS = {"tools", "assets", ".git", "en"}
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


def collect_pages():
    """Return list of TR URL paths."""
    tr_pages = []

    for f in sorted(SITE_ROOT.rglob("index.html")):
        parts = f.relative_to(SITE_ROOT).parts

        # Skip excluded dirs
        if any(p in EXCLUDE_DIRS for p in parts):
            continue

        url_path = get_url_path(f)
        if url_path in EXCLUDE_PATHS:
            continue
        # noindex sayfalar (redirect stub'ları vb.) sitemap'e girmez
        if b'noindex' in f.read_bytes()[:4000].lower():
            continue
        tr_pages.append(url_path)

    return tr_pages


def build_url_entry(path, priority="0.8"):
    loc = BASE_URL + path
    return "\n".join([
        "  <url>",
        f"    <loc>{loc}</loc>",
        f"    <lastmod>{TODAY}</lastmod>",
        "    <changefreq>weekly</changefreq>",
        f"    <priority>{priority}</priority>",
        "  </url>",
    ])


def get_priority(path):
    if path == "/":
        return "1.0"
    # Local SEO landing pages: Samsun/Atakum/Ilkadim/Maltepe dis
    if path in ("/poliklinikler/rivadent-atakum/",
                "/poliklinikler/rivadent-ilkadim/",
                "/poliklinikler/rivadent-maltepe/"):
        return "0.9"
    if path.startswith("/hekim/"):
        return "0.7"
    if path.startswith("/blog/"):
        return "0.6"
    return "0.8"


def main():
    tr_pages = collect_pages()

    entries = [build_url_entry(p, get_priority(p)) for p in sorted(tr_pages)]

    sitemap = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(entries)
        + "\n</urlset>\n"
    )

    out = SITE_ROOT / "sitemap.xml"
    out.write_text(sitemap, encoding="utf-8")
    print(f"Written {len(entries)} URL entries to sitemap.xml (TR only)")


if __name__ == "__main__":
    main()
