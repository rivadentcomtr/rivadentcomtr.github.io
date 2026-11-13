#!/usr/bin/env python3
"""
Normalize internal links: strip trailing 'index.html' from href/value
attributes so internal links point at the canonical directory URL
(/foo/ instead of /foo/index.html).

Canonicals, sitemap and JSON-LD already use the /foo/ form; internal
links were the only signal still feeding Google the index.html variant.

Only TR pages are processed (en/ is out of SEO scope but its links still
work either way).
"""

import re
from pathlib import Path

SITE_ROOT = Path(r"c:\Users\omerc\CascadeProjects\whatsappBot\rivadentLast\site")
EXCLUDE_DIRS = {"tools", "assets", ".git", ".github", ".claude", ".windsurf", "en"}

# attr=".../index.html[#frag|?q]"  or  attr="index.html[#frag|?q]"
ATTR_RE = re.compile(r'((?:href|value)=")([^"]*?)(index\.html)((?:[#?][^"]*)?)(")')


def fix_value(m):
    prefix, path, _, tail, quote = m.groups()
    if path == "":
        # attr="index.html" -> "./" (tail keeps #frag/?q if any)
        return f'{prefix}./{tail}{quote}'
    # attr="foo/index.html" -> "foo/"
    return f'{prefix}{path}{tail}{quote}'


def main():
    files_changed = 0
    links_changed = 0
    for f in sorted(SITE_ROOT.rglob("*.html")):
        rel = f.relative_to(SITE_ROOT)
        if any(p in EXCLUDE_DIRS for p in rel.parts):
            continue
        text = f.read_text(encoding="utf-8")
        new_text, n = ATTR_RE.subn(fix_value, text)
        if n:
            f.write_text(new_text, encoding="utf-8")
            files_changed += 1
            links_changed += n
    print(f"normalized {links_changed} links in {files_changed} files")


if __name__ == "__main__":
    main()
