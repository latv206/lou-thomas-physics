# BIH-VI

Boundary-inversion cosmology, its effective-clock background, and the A2 stability calculation.

## Reading Order

1. [Research overview](../docs/RESEARCH_OVERVIEW.md).
2. [Technical report](reports/Technical_Report_FINAL.pdf), [Open Work Addendum](reports/Open_Work_Addendum.pdf), and [Module A/B Addendum](reports/Module_A_B_Expansion_Addendum.pdf). These background documents predate the final A2 scan.
3. [Final A2 manuscript](manuscript/A2_MANUSCRIPT_FINAL.pdf) and [LaTeX source](manuscript/A2_MANUSCRIPT_FINAL.tex).
4. [Allowed A2 claims](manuscript/locked/A2_ALLOWED_CLAIMS.md) and [corrected review evidence](review/evidence/EVIDENCE_INDEX.md).
5. [Recorded A2 results](results/a2-2026-07-06) and [sealed source](code/a2_production_scan.py.txt).

The manuscript's `FINAL_PASS` concerns the historical compilation and packaging process. It is not journal acceptance or approval of the physics. Historical references to "external acceptance" refer to package review; no peer review is established by those records.

## Current Claim Boundary

> The validated bounded-eta_H all-operator A2 instrument was applied to the frozen BIH-VI benchmark. In the claim-bearing hard envelope K <= 0.06, equilateral and squeezed configurations are stable under the sealed G-S criteria. Folded/flattened configurations are diagnostic/report-only under the current sealed instrument; in this run, no folded/flattened row passed G-FLAT.

"Validated" in this historical wording refers to the instrument's declared numerical checks. The cubic-action reduction and physical interpretation remain independently reviewable questions.

The foundation audit itself originally made overly broad absence claims. Read its later corrected evidence bundle alongside it. No absence search proves that a derivation exists nowhere.

## Reproduction

From the repository root run `python tools/reproduce_a2.py` after installing the numerical requirements. The wrapper verifies the sealed source hash, makes a private test Hub under `_generated/`, and compares the new numerical rows with the archived record. It does not use or append to an existing Hub.

The original source's self-referential manifest hashes describe intermediate serialization, not a reliable final checksum of those same files. Use this release's `SHA256SUMS.txt` and verification tool for public-file integrity.

## Archive Boundary

Earlier all-operator attempts and late-universe pipelines are retained under `archive/bih-vi/`. Do not mix their verdicts with the July 6 A2 record. The earlier July 1 A2 RUN01 explicitly reports incomplete closure.
