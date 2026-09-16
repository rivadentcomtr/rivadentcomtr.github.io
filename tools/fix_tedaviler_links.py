from pathlib import Path
SITE = Path(r"c:\Users\omerc\CascadeProjects\whatsappBot\rivadentLast\site")

for f in SITE.rglob("*.html"):
    if "tools" in str(f):
        continue
    content = f.read_text(encoding="utf-8")

    has_tr = 'href="">T\u00fcm Tedaviler' in content
    has_en = 'href="">All Treatments' in content
    if not has_tr and not has_en:
        continue

    depth = len(f.relative_to(SITE).parts) - 1
    prefix = "../" * depth

    new_content = content
    if has_tr:
        target = prefix + "tedaviler/index.html"
        new_content = new_content.replace(
            'href="">T\u00fcm Tedaviler',
            f'href="{target}">T\u00fcm Tedaviler'
        )
    if has_en:
        target = prefix + "tedaviler/index.html"
        new_content = new_content.replace(
            'href="">All Treatments',
            f'href="{target}">All Treatments'
        )

    if new_content != content:
        f.write_text(new_content, encoding="utf-8")
        print(str(f.relative_to(SITE)))
