#!/usr/bin/env python3
"""
Restore Sultan Tas in Maltepe nav/listings alongside Aleyna Beray.
What went wrong: Sultan Tas was replaced BY Aleyna, but she should REMAIN in Maltepe.
Aleyna should be ADDED alongside Sultan Tas.
Fix: insert Sultan Tas li/card BEFORE Aleyna's li/card wherever she appears.
"""

import re
from pathlib import Path

SITE_ROOT = Path(r"c:\Users\omerc\CascadeProjects\whatsappBot\rivadentLast\site")

# Sultan Tas instagram
SULTAN_INSTA = "https://www.instagram.com/sultipo"


def insert_before_aleyna_nav_li(content):
    """
    Find nav <li> blocks containing dt-aleyna-beray-kidak and insert
    a Sultan Tas <li> with the same path prefix immediately before each.
    Only matches nav-style li (small, single-link, no nested divs).
    """

    def make_sultan_li(aleyna_li_text, prefix):
        # Build matching Sultan Tas li by cloning Aleyna li and substituting
        sultan = aleyna_li_text.replace(
            'dt-aleyna-beray-kidak', 'dt-sultan-tas'
        ).replace(
            'Dt. Aleyna Beray Kıdak', 'Dt. Sultan Taş'
        )
        return sultan

    # Pattern: whitespace-sensitive li that contains a single anchor to aleyna
    # Works for both desktop inner-sub-menu and mobile list
    pattern = re.compile(
        r'([ \t]*<li>[ \t]*\n[ \t]*<a href="([^"]*?)dt-aleyna-beray-kidak[^"]*"[^>]*>[ \t]*\n[ \t]*Dt\. Aleyna Beray K[ıi]dak[^<]*</a>[ \t]*\n[ \t]*</li>)',
        re.MULTILINE
    )

    def replacement(m):
        aleyna_li = m.group(1)
        prefix = m.group(2)
        sultan_li = make_sultan_li(aleyna_li, prefix)
        return sultan_li + '\n' + aleyna_li

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


def insert_before_aleyna_team_card(content):
    """
    Find col-lg-3 team card <div> blocks containing dt-aleyna-beray-kidak
    and insert a Sultan Tas team card immediately before each.
    """
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

        if 'dt-aleyna-beray-kidak' in block:
            # Build Sultan Tas card from Aleyna card
            sultan_block = block\
                .replace('dt-aleyna-beray-kidak', 'dt-sultan-tas')\
                .replace('Dt. Aleyna Beray Kıdak', 'Dt. Sultan Taş')\
                .replace('dt-aleyna-beray-kidak.webp', 'a90a8c50d68f215d71c0fb026ee64f3b.webp')

            # Add instagram li to Sultan Tas social ul (Aleyna has empty social)
            sultan_block = sultan_block.replace(
                '<ul class="team-social">\n                                                                    </ul>',
                '<ul class="team-social">\n                                                                                                                                                    <li>\n                                            <a href="' + SULTAN_INSTA + '" target="_blank"><i class="fa-brands fa-instagram"></i></a>\n                                        </li>\n                                                                    </ul>'
            )
            # Also try the pattern used in hekim page bottom team list
            sultan_block = sultan_block.replace(
                '<ul class="team-social">\n                                                                </ul>',
                '<ul class="team-social">\n                                                                                                                                                    <li>\n                                            <a href="' + SULTAN_INSTA + '" target="_blank"><i class="fa-brands fa-instagram"></i></a>\n                                        </li>\n                                                                    </ul>'
            )

            result.append(content[i:pos])
            result.append(sultan_block)
            result.append('\n')
            result.append(block)
        else:
            result.append(content[i:end])

        i = end

    return ''.join(result)


def restore_sultan_modal_option(content):
    """
    Add Sultan Tas back as modal option before Aleyna's option.
    We assume Aleyna has value="32" (Sultan Tas original ID).
    We give Sultan Tas back value="32" and Aleyna stays too (same value for now).
    Actually: insert Sultan Tas option BEFORE Aleyna option.
    """
    # Add Sultan Tas option before Aleyna option
    sultan_option = '<option value="32">Dt. Sultan Taş</option>'
    aleyna_option_pattern = re.compile(
        r'(<option[^>]*value="32"[^>]*>Dt\. Aleyna Beray K[ıi]dak</option>)'
    )

    def opt_replacement(m):
        aleyna_opt = m.group(1)
        # Change Aleyna to a new slot (she's new, so give her value 36 for now)
        aleyna_updated = aleyna_opt.replace('value="32"', 'value="36"')
        return sultan_option + '\n                                                                            ' + aleyna_updated

    content = aleyna_option_pattern.sub(opt_replacement, content)
    return content


def process_file(path):
    content = path.read_text(encoding='utf-8')
    original = content

    path_str = str(path).replace('\\', '/')

    # Skip Sultan Tas own page, Aleyna's own page, and tools
    if 'dt-sultan-tas' in path_str:
        return False
    if 'dt-aleyna-beray-kidak' in path_str:
        return False
    if 'tools/' in path_str or 'tools\\' in path_str:
        return False

    # Only process if Aleyna is referenced (she was inserted by previous script)
    if 'dt-aleyna-beray-kidak' not in content:
        return False

    # 1. Restore Sultan Tas in nav li items
    content = insert_before_aleyna_nav_li(content)

    # 2. Restore Sultan Tas in team card divs
    content = insert_before_aleyna_team_card(content)

    # 3. Restore Sultan Tas in modal option
    content = restore_sultan_modal_option(content)

    if content != original:
        path.write_text(content, encoding='utf-8')
        return True
    return False


def main():
    print("=== Restore Sultan Tas Alongside Aleyna ===\n")
    files = list(SITE_ROOT.rglob("*.html"))
    changed = 0
    for f in files:
        if process_file(f):
            changed += 1
            print(f"  Updated: {f.relative_to(SITE_ROOT)}")
    print(f"\nChanged: {changed} files")


if __name__ == "__main__":
    main()
