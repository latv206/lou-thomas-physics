# A2 FOUNDATION AUDIT — PRIMARY EXCERPTS (Hub-native, short)
2026-07-07 · claude-physics · all excerpts are from files inside [local path omitted]

## E1 — A2's own allowed claim scopes it to STABILITY, not derivation
Source: A2_ALLOWED_CLAIMS.md (in outbox\A2_FINAL_DATA_LOCK_20260706_160748\, sha 7a056f0f...)
> "The validated bounded-eta_H all-operator A2 instrument was applied to the frozen BIH-VI
> benchmark. In the claim-bearing hard envelope K <= 0.06, equilateral and squeezed configurations
> are stable under the sealed G-S criteria. Folded/flattened configurations are diagnostic/
> report-only under the current sealed instrument; in this run, no folded/flattened row passed
> G-FLAT."
Reading: the binding claim says the instrument is "validated" and "sealed" and that configurations
are "stable" — it is a stability/reproducibility statement about a sealed instrument, NOT a claim
that the ledger is derived. This is Hub-native and self-consistent with the audit's downgrade.

## E2 — The production script self-describes the ledger as a SEALED INSTRUMENT
Source: runs\A2_PRODUCTION_LOCAL\a2_production_scan.py (sha 35fd3659...), lines 5-10
> "Decision A implementation:
>  - Uses the sealed G-S v3 bounded-eta_H instrument structure.
>  - Claim-bearing families: equilateral + squeezed hard rows only, K <= 0.060.
>  - Folded/flattened rows are diagnostic/report-only under the current sealed
>    instrument unless G-FLAT explicitly passes ..."
Reading: the code that produced the A2 result explicitly treats the ten-term ledger as a *sealed
instrument structure* it consumes, not a derivation it establishes. Hub-native.

## E3 — The foundation audit's own verdict (the document under review)
Source: outbox\a2_foundation_audit_20260707\A2_FOUNDATION_SUFFICIENCY_AUDIT.md (sha ae468fbf...)
> "The bounded-eta_H all-operator ledger ... is asserted, not derived, and its derivation exists
> nowhere in human-reviewable form. Recommended path: Option B — a narrow, firewalled foundation
> companion paper ... written from scratch. ~6-10 weeks of physicist time."
Note: this document's SHA-256 was recomputed by claude-physics and matches both its own SHA256SUMS
and Codex's independently reported value (ae468fbf...). Integrity of the audit artifact = CONFIRMED.

## E4 — Ledger governance entry recording the audit
Source: ledger\ledger.md (entry 2026-07-07T14:24:10) + ledger.jsonl
> "claude-physics | FOUNDATION-AUDIT (read-only) | outbox\a2_foundation_audit_20260707 | ...
>  FINDING: A2's bounded-eta_H ledger is ASSERTED not DERIVED ... No numerics rerun; no locked
>  artifact touched; A2 hashed pipeline unchanged (it correctly computed an asserted object)."

## E5 — What is NOT in [local path omitted], not as disproof)
The following audit facts are load-bearing but live on Z: and are NOT reproducible from [local path omitted]
- A2_RUN01_FINAL_VERDICT.json -> final_A2_closure = false (hand-verified on Z: 2026-07-07)
- cmb_safety_flag = REQUIRES_REVIEW_large_K_lt_1_kernel_value (same file, Z:)
- "sealed by A2_BENCH_ETA" docstring (in a2_gs_surface_sweep_v3.py at SimulationLab\Hub\frozen)
- Technical Report: "Non-Gaussianity ... remain to be computed" (Z:)
- Module A/B addendum: "all-operator EFT bispectrum ... remain open" (Z:)
- Unified manuscript grep-zero for ledger tokens (Z:)
These are recorded in EVIDENCE_INDEX.md as AUDIT_REPORTED_NOT_IN_HUB. To promote any of them to
CONFIRMED, either (a) Lou authorizes Z: as an evidence source, or (b) copies of those specific
files are placed into [local path omitted], or (c) a human physicist reviews them at source.
