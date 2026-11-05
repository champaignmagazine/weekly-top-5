#!/bin/bash
# Build both online editions into $1 (default: the repo working copy)
set -e
DEST=${1:-/home/claude/weekly-top-5}
python3 /home/claude/top5/hist/build_site.py $DEST/2025/historical
python3 /home/claude/top5/hist/build_register_page.py $DEST/2025/historical
cd /home/claude/top5/proof && python3 /home/claude/top5/hist/build_concise_site.py $DEST/2025/concise ${2:-AI_by_AI_Weekly_Top5_2025_Concise_Edition.pdf}
cp /home/claude/top5/hist/root_index.html $DEST/index.html
cp /home/claude/top5/hist/year_index.html $DEST/2025/index.html
# release files that the site builds do not generate
[ -f /home/claude/top5/proof/AI_by_AI_Weekly_Top5_2025_Concise_Edition.pdf ] && cp /home/claude/top5/proof/AI_by_AI_Weekly_Top5_2025_Concise_Edition.pdf $DEST/2025/concise/
[ -f /home/claude/top5/release/AI_by_AI_Weekly_Top5_2025_Concise_Edition.docx ] && cp /home/claude/top5/release/AI_by_AI_Weekly_Top5_2025_Concise_Edition.docx $DEST/2025/concise/
cp /home/claude/top5/top5_2025_captured_posts.zip $DEST/2025/historical/data/Captured_Posts_2026-10-22.zip
