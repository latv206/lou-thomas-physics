# A2 FINAL DATA LOCK

Final verdict (source production run): **PASS**
Finalization verdict: **LOCKED** (all 13 verifications pass; data frozen as-is)
Production script SHA-256: `35fd365916395f171fee9278480bd102b267f545fb389d6039cfe0058c78aae8`
Production runtime: 7.280172109603882 s (started 2026-07-06T20:41:54+00:00, finished 2026-07-06T20:42:02+00:00)
Source folder: `[local path omitted]`

## Gates (13/13)
- UT_K: PASS
- UT_FR: PASS
- BG_ETA: PASS
- G_W: PASS
- CONV: PASS
- G_S_CONTINUITY_SENTINELS: PASS
- EQUILATERAL_HARD_ROWS_STABLE: PASS
- SQUEEZED_HARD_ROWS_STABLE: PASS
- FOLDED_GFLAT_OR_FLAGGED: PASS
- NO_FOLDED_CLAIM_WITHOUT_GFLAT: PASS
- NO_PROVISIONAL_CLAIM: PASS
- NO_K_GT_0P06_CLAIM: PASS
- EXECUTION_LOCK: PASS

## Row counts
- total rows scanned: 42
- claim rows: 22 (equilateral 11, squeezed 11, folded 0)
- flagged rows: 20
- folded/G-FLAT diagnostic rows: 14; G-FLAT passes: 0
- hard claim envelope: K in [0.01, 0.06] (K <= 0.06)

## Allowed claim
The validated bounded-eta_H all-operator A2 instrument was applied to the frozen BIH-VI benchmark. In the claim-bearing hard envelope K <= 0.06, equilateral and squeezed configurations are stable under the sealed G-S criteria. Folded/flattened configurations are diagnostic/report-only under the current sealed instrument; in this run, no folded/flattened row passed G-FLAT.

## Forbidden claims
- full all-shape closure
- folded/flattened physical instability
- BIH-VI observational detection
- UV completion
- C4/C5/C6 ontology as A2 evidence
- Hubble-tension solution
- folded rows falsify BIH-VI
- folded rows prove a physical instability

## Standing notes
- C4/C5/C6 remain PARKED; nothing here uses or promotes them.
- This is EFT-level A2 only; no UV-completion claim is made or implied.
