"""Write the registry's front page: what this is and every listing. Listing text is untrusted, so it is escaped."""
import html
import json
import sys
from pathlib import Path

source, out = Path(sys.argv[1]), Path(sys.argv[2])
rows = []
for path in sorted(source.glob("indexes/*/*/listing.json")):
    try:
        l = json.loads(path.read_text(encoding="utf-8"))
        work = l.get("work") or {}
        title = str(work.get("title") or l["id"])
        authors = ", ".join(str(a) for a in work.get("authors") or [])
        rows.append((title.lower(), "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(
            html.escape(title), html.escape(authors), html.escape(str(l["publisher"])),
            "Whole book" if l.get("complete") else "Partial", html.escape(str(l.get("license", ""))))))
    except Exception:  # a listing that cannot be read is left off the page, never a failed build
        continue
rows.sort()
count = len(rows)
table = ("<table><thead><tr><th>Book</th><th>Author</th><th>Shared by</th><th>Covers</th><th>Licence</th></tr></thead><tbody>"
         + "".join(r for _, r in rows) + "</tbody></table>") if rows else "<p>No indexes have been shared yet.</p>"
page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Lorekeeper community registry</title>
<style>
  :root {{ color-scheme: dark light; --bg: #0b0d12; --text: #e6e9ef; --dim: #9aa3b2; --line: #232834; --link: #4fd1c5; }}
  @media (prefers-color-scheme: light) {{ :root {{ --bg: #fbfbfc; --text: #171a21; --dim: #5a6372; --line: #dfe3ea; --link: #0b7d74; }} }}
  body {{ margin: 0; background: var(--bg); color: var(--text); font: 16px/1.6 system-ui, sans-serif; }}
  main {{ max-width: 760px; margin: 0 auto; padding: 48px 16px; }}
  h1 {{ font-size: 28px; margin: 0 0 8px; }} h2 {{ font-size: 18px; margin: 40px 0 8px; }}
  p {{ margin: 0 0 12px; }} .dim {{ color: var(--dim); }} a {{ color: var(--link); }}
  .wrap {{ overflow-x: auto; }} table {{ width: 100%; border-collapse: collapse; font-size: 14px; }}
  th, td {{ text-align: left; padding: 10px 12px 10px 0; border-bottom: 1px solid var(--line); white-space: nowrap; }}
  th {{ color: var(--dim); font-weight: 600; }}
</style>
</head>
<body>
<main>
<h1>Lorekeeper community registry</h1>
<p>Spoiler-gated book indexes that people built with <a href="https://github.com/nightspine/lorekeeper">Lorekeeper</a> and chose to share. The app looks here when you open a book, so a ready-made index for your copy is one click away.</p>
<p class="dim">This site is read by the app. There is nothing to install from this page, and it holds no books, only index files.</p>
<h2>Shared indexes ({count})</h2>
<div class="wrap">{table}</div>
<h2>Share one</h2>
<p>In Lorekeeper, open a book you built an index for and choose Share. It checks the index and gives you a file, which you attach to <a href="https://github.com/nightspine/lorekeeper-registry/issues/new?template=share.yml">a submission here</a>.</p>
<h2>Problems and removals</h2>
<p>Found a spoiler or a mistake? <a href="https://github.com/nightspine/lorekeeper-registry/issues">Open an issue</a>. For copyright concerns, read the <a href="https://github.com/nightspine/lorekeeper-registry/blob/main/TAKEDOWN.md">takedown policy</a>.</p>
</main>
</body>
</html>
"""
(out / "index.html").write_text(page, encoding="utf-8")
