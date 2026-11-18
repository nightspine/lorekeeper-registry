# Lorekeeper community registry

Spoiler-gated book indexes that people have built with [Lorekeeper](https://github.com/nightspine/lorekeeper) and chose to share. The Lorekeeper app looks here when you open a book, so a ready-made index for your copy is one click away.

This repository is the registry. There is no server: indexes are JSON files, and a GitHub Action publishes them with a small lookup file per edition.

The published registry is at https://nightspine.github.io/lorekeeper-registry/ and lists every shared index. To share one, use Share on a book in Lorekeeper 0.8.0 or later and attach the file it gives you to [a submission](https://github.com/nightspine/lorekeeper-registry/issues/new?template=share.yml).

## What is here

- `indexes/<publisher>/<book>/` holds each shared index, one file per version, next to its listing record.
- `TAKEDOWN.md` is the removal policy and the address for notices.
- `removed.json` logs every removal with its date and reason.

## What may be shared

- Index files only, in the [Lorekeeper format](https://github.com/nightspine/lorekeeper/blob/main/SPEC.md). Never a book, a chapter or a passage.
- Original wording. An index may quote at most eight consecutive words from the book; the app checks this before sharing.
- Under CC0-1.0 or CC-BY-4.0, so others can use and improve it.
- Written as the reader understands things at each point in the book. An index that reveals something early is a bug: open an issue.

## Reporting a problem

Open an issue and name the listing and the entry. For copyright concerns, see [TAKEDOWN.md](TAKEDOWN.md).
