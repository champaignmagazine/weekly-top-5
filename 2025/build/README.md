# Build sources for the 2025 collection

These are the scripts and sources that produced the concise edition's PDF and its online pages, the historical edition's site and the forecast register. They are released under the MIT License, and the text and data under CC BY 4.0.

| Folder | Contents |
|---|---|
| `proof/` | `build_proof.py` assembles the PDF: front matter, chapters and back matter. `src/` holds the Markdown sources of the front and back matter. Run it with `RELEASE=1` to build the final edition. |
| `print/` | The twelve chapters' content modules, the monthly introductions, the chapter renderer and the edit log. |
| `index/` | The keyword index: GPT-6 Astra's curated headings, and the build that paginates them on the final layout. |
| `site/` | The online editions. `build_all.sh` builds both. `build_site.py` builds the historical edition from the captured posts, `build_concise_site.py` builds the concise edition from the PDF's own sources, and `build_register_page.py` builds the forecast register page. |
| `register/` | Forecast register v2.2: the merge script, the report, the adopted scoring rules, the change log, the frozen attribution halves and the cross-check records, and the restored v1 build step. |

The scripts were written for the compiling environment and use its absolute paths, which begin `/home/claude/top5/`. To run them elsewhere, change those paths. They also need:

- the captured posts, from `../historical/data/Captured_Posts_2026-10-22.zip`;
- the annotated master, `volume.json`, which is not included.

Tools used: Python 3 with `markdown`, `pypdf`, `beautifulsoup4` and `playwright` (Chromium), Poppler (`pdftotext`) and pandoc.
