#!/usr/bin/env python3
"""
Replace Dt. Başak Tımarcıoğlu with Dr. Dt. Miray Yıldırım
ONLY inside team-box divs (not in nav links).
Anchor: Başak's unique image hash 1071cc5e8eebd0521bbed8081dcbcb53.webp
"""

from pathlib import Path

SITE_ROOT = Path(r"c:\Users\omerc\CascadeProjects\whatsappBot\rivadentLast\site")

BASAK_IMG  = "1071cc5e8eebd0521bbed8081dcbcb53.webp"
MIRAY_IMG  = "e05da856c23e0c3ebafff22068e6d301.webp"


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


def replace_in_teambox(content, is_en):
    """Find team-box divs containing Başak's image and replace content within."""
    search = '<div class="team-box'
    result = []
    i = 0

    while True:
        pos = content.find(search, i)
        if pos == -1:
            result.append(content[i:])
            break

        end = find_matching_close_div(content, pos)
        block = content[pos:end]

        if BASAK_IMG in block:
            # Replace all Başak references with Miray inside this block
            block = block.replace("dt-basak-timarcioglu", "dr-dt-miray-yildirim")
            block = block.replace("Dt. Başak Tımarcıoğlu", "Dr. Dt. Miray Yıldırım")
            block = block.replace(BASAK_IMG, MIRAY_IMG)
            block = block.replace("basakrcvs/", "drdtmirayyildirim")
            block = block.replace("basakrcvs", "drdtmirayyildirim")
            # Specialty (TR)
            block = block.replace(
                "Di\u015f Hekimi / Protetik Di\u015f. Ted.",
                "\u00c7ocuk Di\u015f Hekimi Uzman\u0131"
            )
            # Specialty (EN)
            if is_en:
                block = block.replace(
                    "Dentist <br/> RivaDent Maltepe Dental Clinic",
                    "Pediatric Dentist Specialist <br/> RivaDent Maltepe Dental Clinic"
                )
            result.append(content[i:pos])
            result.append(block)
        else:
            result.append(content[i:end])

        i = end

    return ''.join(result)


def process_file(path):
    content = path.read_text(encoding='utf-8')
    original = content

    path_str = str(path)
    if 'dt-basak-timarcioglu' in path_str or 'tools' in path_str:
        return False

    # Only process files that actually have Başak in a team-box
    if BASAK_IMG not in content:
        return False

    is_en = 'site\\en\\' in path_str or 'site/en/' in path_str

    content = replace_in_teambox(content, is_en)

    if content != original:
        path.write_text(content, encoding='utf-8')
        return True
    return False


def main():
    print("=== Replace Basak -> Miray in team-box sections ===\n")
    files = list(SITE_ROOT.rglob("*.html"))
    changed = 0
    for f in files:
        if process_file(f):
            changed += 1
            print(f"  Updated: {f.relative_to(SITE_ROOT)}")
    print(f"\nChanged: {changed} files")


if __name__ == "__main__":
    main()
