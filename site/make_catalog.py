"""Write the site's front page, listing page and catalog.json: one small record per listing, newest first.

The pages search and page through the catalog in the browser. Listing text is untrusted: it only ever
travels as JSON here and is shown with textContent there.
"""
import json
import shutil
import sys
from pathlib import Path

source, out = Path(sys.argv[1]), Path(sys.argv[2])
here = Path(__file__).parent
records = []
for path in source.glob("indexes/*/*/listing.json"):
    try:
        l = json.loads(path.read_text(encoding="utf-8"))
        work = l.get("work") or {}
        records.append({
            "id": str(l["id"]),
            "title": str(work.get("title") or l["id"])[:300],
            "authors": [str(a)[:200] for a in (work.get("authors") or [])][:10],
            "language": str(work.get("language") or "")[:20],
            "publisher": str(l["publisher"]),
            "complete": bool(l.get("complete")),
            "license": str(l.get("license") or ""),
            "updated": str(l.get("updated") or ""),
        })
    except Exception:  # a listing that cannot be read is left out, never a failed build
        continue
records.sort(key=lambda r: (r["updated"], r["id"]), reverse=True)
(out / "catalog.json").write_text(
    json.dumps({"count": len(records), "listings": records}, ensure_ascii=False, separators=(",", ":"), allow_nan=False),
    encoding="utf-8")
for name in ("index.html", "listing.html", "site.css"):
    shutil.copyfile(here / name, out / name)
print(f"catalog: {len(records)} listings")
