# Keyword index: Claude's final pass on GPT-6 Astra's curation v1

November 2, 2026 · for W.H.L., editor, and GPT-6 Astra · typeset in Print Proof 11

The index in Proof 11 is built from GPT's curated CSV. Every page reference was recomputed on the Proof 11 layout. No Proof 10 page string was carried over.

## Result

| | |
|---|---:|
| Headings printed | 674 |
| "See" redirects | 10 |
| Headings with subentries | 14 |
| Dangling or empty references | 0 |
| Index length | 9 pages (Proof 10: 11) |

## How pages are counted

- **Body text only.** Running heads, folios, "Selected by" contributor lines, source notes and selected-source lists are removed before matching. Footnote numbers next to words are stripped too; in Proof 10 they had hidden some matches ("Brookfield.17").
- **Model versions stay separate.** A match stops before a version suffix, so pages for GPT-5.1 or Claude Opus 4.5 are not counted under GPT-5 or Claude Opus 4. Short forms count toward their own versions: "Opus 4.1" under Claude Opus 4.1, and "V3.1" under DeepSeek-V3.1.
- **Merges.** A heading collects the pages of the terms GPT merged into it, unless the context check below restricts them.
- **Thematic headings** (Verification, Open models, Data centers, and so on) count front-matter pages, the chapters' opening summaries and entry headlines. A theme that appears on eight pages or fewer counts every page.
- **Long headings.** A heading with more than 24 pages is split into subentries by part of the book (front matter, then month): OpenAI, Google, Meta, Anthropic, Claude, Nvidia, ChatGPT, Gemini, United States, Agents, DeepSeek, AI chips, Microsoft and Grok.

## Context checks resolved

| Check | Decision |
|---|---|
| AI Security Institute → UK AI Security Institute | Merged. All four occurrences are the UK institute. |
| ChatGPT for US → ChatGPT for Teachers | Merged for pp. 49 and 186 ("ChatGPT for US teachers"). On p. xxvii the phrase is "checkout inside ChatGPT for purchases", which is not this product, so it was left out. |
| Code of Practice → General-Purpose AI Code of Practice | Merged. All six occurrences are the EU code. |
| Governor of California → Gavin Newsom | The phrase is not in Proof 11. Gavin Newsom is indexed from the full name and "Governor Newsom". |
| O Connect India → Google I/O Connect India | Indexed from "I/O Connect India" (p. 105). |
| R1 → DeepSeek-R1 | Merged. Every bare "R1" refers to DeepSeek's model. DeepSeek-R1-0528 stays separate. |
| Scale → Scale AI | Only "Scale AI", "Scale's" and "Scale's investment/appointed" count. Bare "Scale" never counts. |
| V3 → DeepSeek-V3 | Bare V3 only. V3-0324, V3.1, V3.1-Terminus, V3.2 and V3.2-Exp go under their own headings. |
| Gemini Deep Think | Kept for the advanced version at the IMO (pp. xiv, 104). The bare "Deep Think" heading is dropped. Its occurrences go to Gemini 2.5 Deep Think (ICPC) and Gemini 3 Deep Think (pp. xi, xxiv, 184 and the December entries). |
| Gemini Flash Thinking | Merged into Gemini 2.0 Flash Thinking. The p. 10 entry names that model. |
| Opus | Dropped. Occurrences go to Claude Opus 4, 4.1, 4.5 and 5.5. Claude Opus 5.5 is the contributor, and its contributor lines are not indexed. |
| Universal | Split. Universal Music Group: xxxi, 79, 175. "Universal, film studio": pp. 137 and 203 (the suit against Midjourney). |

**Publishers.** A publisher keeps a heading only where the book discusses it as a participant, licensor or research venue:

| Publisher | Decision |
|---|---|
| BBC | Kept: p. 9, its complaint about Apple's notification summaries. |
| Reuters | Kept: xxxii, 111, 120, its report on Meta's chatbot rules, which was itself the story. |
| Nature, Nature Microbiology | Kept as research venues. |
| The New York Times | Kept as a licensor ("New York Times, The"). |
| Axios, Bloomberg News, Business Insider, CNN, Financial Times, Fortune, South China Morning Post, TechCrunch, Wall Street Journal, Washington Post | Dropped: source credits only. TechCrunch occurs only in source notes. |

**Redirects.** These are unpaginated "See" entries: AGI, AWS, Chatbot Arena, IMO, Allen Institute for AI, EU, FDA, FTC, TII, UAE. GPT's other merges (honorifics, fragments) leave no redirect.

**Display names** follow the book's style:

- Nvidia (not NVIDIA).
- "Concise edition" replaces "Edited edition", following the volume's current terminology.
- "New York Times, The".

## Added and broad headings with no pages in the final text

These were omitted rather than given invented pages:

- **Source notes only:** Jack Lindsey and Transformer Circuits.
- **Not in the text:** National Policy Framework for Artificial Intelligence and US Bureau of Industry and Security (the chapters say "export rule", not the bureau).
- **No substantive passage:** Productivity.
- **Too broad:** "Artificial intelligence" was dropped.

All other 90 additions were located and kept. Their see-also references resolve.

## For GPT-6 Astra

Three judgment calls that you may want to check:

- **Reuters is limited to the Meta story.** Elsewhere its reports are treated as credits, like Bloomberg's.
- **Thematic headings exclude passing mentions.** Inside entry text, a theme is indexed only through headlines and the opening summaries. For example, Verification lists pp. xv, xix, xliv–xlv, l, lvi and 93–94, not every "verified".
- **United States is kept with subentries** (65 pages). If you would rather drop it as too broad, it is a one-line change.

## Files

- `Keyword_Index_Final_Proof11.csv`: the typeset index as data, for the online editions.
- `Index_Build_Report.md`: drops, empties, redirects and subentries, generated by the build.
- `build_index.py` and `pages.py`: the build. It runs from the proof script on every layout, so pages update automatically.
