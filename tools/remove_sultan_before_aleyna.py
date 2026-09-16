#!/usr/bin/env python3
"""
Remove Sultan Tas nav li and team cards that appear immediately BEFORE Aleyna Beray Kidak.
These were inserted by restore_sultan_tas.py but Sultan Tas should NOT be in Maltepe.
Sultan Tas stays only in Atakum listings.
"""

import re
from pathlib import Path

SITE_ROOT = Path(r"c:\Users\omerc\CascadeProjects\whatsappBot\rivadentLast\site")


def remove_sultan_before_aleyna_nav_li(content):
    """Remove Sultan Tas nav li that appears right before Aleyna's nav li."""
    pattern = re.compile(
        r'([ \t]*<li>[ \t]*\n[ \t]*<a href="[^"]*?dt-sultan-tas[^"]*"[^>]*>[ \t]*\n[ \t]*Dt\. Sultan Ta[s\u015f][^<]*</a>[ \t]*\n[ \t]*</li>)\n([ \t]*<li>[ \t]*\n[ \t]*<a href="[^"]*?dt-aleyna-beray-kidak[^"]*")',
        re.MULTILINE
    )
    def replacement(m):
        return m.group(2)
    return pattern.sub(replacement, content)


def find_matching_close_div(html, start):
    depth = 0
    i = start
    n = len(html)
    while i < n:
        if html[i:i+4] == '<div':
            if i + 4 >= n or html[i + 4] in (' ', '\t', '\n', '>'):
                depth += 1
            gt = html.find('>', i)
            i = (gt + 1) if gt != -1 else (i + 4)
        elif html[i:i+6] == '</div>':
            depth -= 1
            if depth == 0:
                return i + 6
            i += 6
        else:
            i += 1
    return n


def remove_sultan_before_aleyna_team_card(content):
    """Remove col-lg-3 Sultan Tas card that appears immediately before Aleyna's card."""
    search_str = '<div class="col-lg-3 col-md-4 col-sm-6 col-6">'
    result = []
    i = 0

    while True:
        pos = content.find(search_str, i)
        if pos == -1:
            result.append(content[i:])
            break

        end = find_matching_close_div(content, pos)
        block = content[pos:end]

        if 'dt-sultan-tas' in block:
            # Check if next card div is Aleyna's
            next_pos = content.find(search_str, end)
            if next_pos != -1:
                next_end = find_matching_close_div(content, next_pos)
                next_block = content[next_pos:next_end]
                if 'dt-aleyna-beray-kidak' in next_block:
                    # Skip the Sultan Tas card and the trailing newline
                    result.append(content[i:pos])
                    skip_end = end
                    if skip_end < len(content) and content[skip_end] == '\n':
                        skip_end += 1
                    i = skip_end
                    continue

        result.append(content[i:end])
        i = end

    return ''.join(result)


def remove_sultan_modal_option(content):
    """Remove Sultan Tas option before Aleyna option and restore Aleyna to value=32."""
    pattern = re.compile(
        r'<option value="32">Dt\. Sultan Ta[s\u015f]</option>\n[ \t]*(<option[^>]*value="36"[^>]*>Dt\. Aleyna Beray K[\u0131i]dak</option>)'
    )
    def replacement(m):
        return m.group(1).replace('value="36"', 'value="32"')
    return pattern.sub(replacement, content)


def process_file(path):
    content = path.read_text(encoding='utf-8')
    original = content

    path_str = str(path).replace('\\', '/')
    if 'dt-sultan-tas' in path_str:
        return False
    if 'dt-aleyna-beray-kidak' in path_str:
        return False
    if 'tools/' in path_str:
        return False

    if 'dt-aleyna-beray-kidak' not in content:
        return False

    content = remove_sultan_before_aleyna_nav_li(content)
    content = remove_sultan_before_aleyna_team_card(content)
    content = remove_sultan_modal_option(content)

    if content != original:
        path.write_text(content, encoding='utf-8')
        return True
    return False


def main():
    print("=== Remove Sultan Tas Before Aleyna ===\n")
    files = list(SITE_ROOT.rglob("*.html"))
    changed = 0
    for f in files:
        if process_file(f):
            changed += 1
            print(f"  Updated: {f.relative_to(SITE_ROOT)}")
    print(f"\nChanged: {changed} files")


if __name__ == "__main__":
    main()
