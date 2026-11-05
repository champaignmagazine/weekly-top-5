# Forecast register v2.2: step 6, source attribution

November 5, 2026 · Claude Opus 5.5, for W.H.L., editor · merged from the frozen halves of Claude Opus 5.5 and GPT-6 Astra

v2.2 adds source attribution to every retained claim outside the story families, and records the scoring rules the editor adopted on November 4. No 2026 outcome was consulted. The panel's quotations are unchanged. The two introductions' own propositions are not part of this register.

## What was done

- **The split.** The 684 retained claims outside the story families were divided by the month of their post:
  - Claude Opus 5.5 took February to July (304 claims).
  - GPT-6 Astra took August to December (380 claims).
- **Reading.** Each claim was read in its captured post. Each attribution records what the post gives: who the claim is attributed to, on what basis, and the document the post cites.
- **The fields.** Recorded attribution and documentary support are separate fields. A name in `attributed_to` does not mean a source supports it.
- **Freezing and cross-checking.** Both halves were frozen before sampling (step6/FROZEN.sha256). A random sample of each half was checked by the other model, with a seed derived from the two frozen files:

| | Rows checked | Agreed | Differed |
|---|---:|---:|---:|
| Claude checked GPT-6 Astra's half | 38 | 34 | 4 |
| GPT-6 Astra checked Claude's half | 31 | 27 | 4 |

  The differences and their resolution are in the change log. Both original readings are kept in step6/.
- **Documents for Claude's half.** Claude could not open the cited documents from its environment. GPT-6 Astra opened them for Claude's 163 attributed rows.

## Counts (claims outside the story families)

| | Claims |
|---|---:|
| The panel's own view, with no attribution (basis "n.a. (panel's own view)") | 336 |
| Attributed to a named person or organization | 283 |
| Attributed to unnamed sources (analysts, critics, X users, reports) | 65 |
| Basis: named in the claim's own sentence | 206 |
| Basis: a source the post cites | 110 |
| Basis: neither | 32 |

| Cited documents | Claude's half | GPT-6 Astra's half | All |
|---|---:|---:|---:|
| Opened | 62 | 89 | 151 |
| Could not be retrieved | 34 | 37 | 71 |
| Not opened | 162 | 254 | 416 |
| No document given | 46 | 0 | 46 |

Of the 151 opened documents, the attribution was supported by 62, partly supported by 35 and not supported by 50. For the other 4, the retrieved page was not assessed.

"Not supported" means the document does not establish the claim as recorded. It does not show that the event or forecast was false.

The access counts are by row, not by distinct document. The halves were not documented equally, so this is not exhaustive verification. The unopened rows are attribution records from the posts, not verified statements.

## Conventions

1. **Unnamed sources.** A blank `attributed_to` on a claim that is not the panel's own view means the post names no identifiable source. The note begins "Unnamed:" and says what the post calls the source.
2. **Panel rows.** The panel's own claims have the basis "n.a. (panel's own view)". Any source an item cites is kept as background in `supporting_document`. It is not turned into a third-party attribution.
3. **Recorded and verified attribution.** `attributed_to` records what the post says. Where an opened document shows a different originator, the finding goes in `attribution_correction`, and the post's wording is kept.

## Corrections

- **FR-0228.** The post says the ACLU warned that the moratorium would give tech giants a "blank check". Senator Markey's release of June 4, 2025 attributes that warning to Damon Hewitt of the Lawyers' Committee for Civil Rights Under Law. ACLU counsel Cody Venzke's warning in the same release is different. This is recorded in `attribution_correction`. The post's text is unchanged.
- **FR-0738.** The paraphrase is narrowed to "OpenAI projected cash burn of about $115 billion through 2029 (as reported)", following the cited interview. The quotation is unchanged.
- **FR-0136.** Voice is changed from "actor (reported)" to "attributed". Unnamed reports about DeepSeek-R2 do not establish that DeepSeek made the forecast.
- **FR-0038 and FR-0102.** Attribution basis corrected after the cross-check.
- **The count.** v2.1 said 668 claims lacked attribution. The correct figure is 666 of the 684 outside the families. 18 already had a v2.1 value, which is kept unchanged in `source_attribution`.

- **FR-0734**, from the post of January 4, 2026, is a checker's confirmation ("CES starting Jan 6 ✔"). It restates the post's own framing ("Next week should bring more from CES"). It is now recorded as a fact-check restatement, not an original occurrence. Both statements belong to the 2026 cohort, and are in `Forecast_Claims_2026_post_v2.2.csv`.

- **Reproducibility.** The v1 final build step is restored as `build_claims_final_v1.py`. It turns `claims_v1.json` into `Forecast_Claims_v1.csv` and `Assessable_by_2026_v1.csv`, using:
  - `assess_v1.txt`;
  - labels v0.8;
  - `duplicate_groups_v1.txt`, the hand-assigned overlap groups, recovered as an input from the frozen output.

  Both rebuilt files are byte-identical to the frozen v1 files. Their SHA-256 values match `claims_v1.sha256`.

## Scoring rules

`Scoring_Conventions_v1.0.md` was drafted by GPT-6 Astra and adopted by the editor on November 4, 2026. It sets these rules before any outcome is examined:

- eligibility;
- possibility and conditional claims;
- claims from labeled items;
- counting by original occurrence;
- deadlines;
- the four outcome categories;
- the December 31, 2026 cutoff;
- what is reported.

**Scorers.** Claude Opus 5.5 and GPT-6 Astra score independently, and the editor adjudicates. Muse Spark 1.3 reviews claims about OpenAI and Anthropic.

## Still open

- **Unretrieved documents.** 71 cited documents could not be retrieved, and 416 rows were not opened.

## Files

| File | Contents |
|---|---|
| `Forecast_Claims_v2.2.csv` | 786 records. The v2.1 fields are unchanged except where logged, plus eight step-6 fields. |
| `Change_log_v2.2.csv` | Every field change, with its reason (401). |
| `stats_v2.2.json` | Counts. |
| `Scoring_Conventions_v1.0.md` | The adopted scoring rules. |
| `step6/` | Both frozen halves, their hashes, the sample record, both cross-checks and GPT-6 Astra's document-access files. |
| `build_v2_2.py` | The merge. |
| `v1/build_claims_final_v1.py`, `v1/duplicate_groups_v1.txt` | The restored v1 build step and its recovered input. |
