# Cross-check samples, step 6

Both worksheets frozen November 4, 2026 (FROZEN.sha256). Seed derived after freezing from the two file hashes: seed = first 8 hex digits of SHA-256(hash_Claude + hash_GPT) = 1218030289.
Python random.Random(seed).sample over cids sorted numerically: 38 of GPT-6 Astra's 380 rows (checked by Claude); random.Random(seed + 1).sample: 31 of Claude's 304 rows (checked by GPT-6 Astra).

Claude checks: FR-0313, FR-0327, FR-0351, FR-0358, FR-0397, FR-0433, FR-0459, FR-0477, FR-0481, FR-0490.1, FR-0499, FR-0502, FR-0506, FR-0510, FR-0520, FR-0534, FR-0537, FR-0539, FR-0540, FR-0558, FR-0569, FR-0586, FR-0594, FR-0599, FR-0609, FR-0623, FR-0628, FR-0638, FR-0650, FR-0662, FR-0692, FR-0698, FR-0702, FR-0703, FR-0707, FR-0708, FR-0729, FR-0741

GPT-6 Astra checks: FR-0010, FR-0011, FR-0017, FR-0038, FR-0046, FR-0052, FR-0066, FR-0092, FR-0102, FR-0105, FR-0117, FR-0121, FR-0127, FR-0136, FR-0146, FR-0150, FR-0166, FR-0171, FR-0187, FR-0193, FR-0200, FR-0205, FR-0217.1, FR-0228, FR-0233.1, FR-0233.2, FR-0243, FR-0274, FR-0279, FR-0289, FR-0682
