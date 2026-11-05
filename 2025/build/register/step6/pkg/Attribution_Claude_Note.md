# Source attribution, February–July posts: Claude's half

November 4, 2026 · Claude Opus 5.5 · for merging into register v2.2 with GPT-6 Astra's half (August–December)

## Counts

| | Claims |
|---|---:|
| Claims in posts of February–July 2025 (retained, outside story families) | 304 |
| The panel's own view (`voice` = panel): no attribution | 141 |
| Attributed, with the source named in the claim's own sentence (`quote`) | 98 |
| Attributed through a source the post cites near the claim (`post source`) | 43 |
| Attributed, with neither (`none`) | 22 |
| Claims with a supporting document recorded | 107 |

## How the rows were filled

- **Reading the claims.** Each claim was located in its captured post by its quotation; one could not be located. I read the attribution from the claim's sentence and its item.
- **Unnamed sources.** Where the post names no one, `attributed_to` says so in brackets, for example "(unnamed X users)". These are the commentators, analysts, critics and X posts that many items cite, and they are about a third of the non-panel claims.
- **Supporting documents.** I copied the document from the post: the link in the claim's line if there is one, otherwise the nearest source the item cites. Some items cite several sources, so the recorded link is the item's source, not necessarily the one behind that sentence.
- **Documents not opened.** I opened none of them, so `document_opened` is "no" and `document_supports` is "n.a." throughout. Some of the recorded links appear constructed by the panel and may not exist; one example is `reuters.com/trump-ai-energy-20-jul-2025`. They are recorded because the post gives them, not because they support the claim.
- **Panel rows.** For the panel's own claims, `attribution_basis` is "n.a. (panel's own view)". This value was not in the brief. It may need aligning with GPT-6 Astra's half at the merge.

## Files

- `Attribution_Worksheet_Claude.csv`: the 304 rows.
- `attr_claude_decisions.py`: the attribution of each non-panel claim, with notes.
- `locate.py`: locates each claim in its captured post and collects the post's links.
