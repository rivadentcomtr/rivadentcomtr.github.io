from pathlib import Path
SITE = Path(r"c:\Users\omerc\CascadeProjects\whatsappBot\rivadentLast\site")
results = []
for f in SITE.rglob("*.html"):
    path_str = str(f)
    if "dt-basak-timarcioglu" in path_str or "tools" in path_str:
        continue
    content = f.read_text(encoding="utf-8")
    if "team-box" in content and "dt-basak-timarcioglu" in content:
        results.append(str(f.relative_to(SITE)))
for r in sorted(results):
    print(r)
