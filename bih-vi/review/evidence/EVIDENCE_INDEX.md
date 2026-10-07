# A2 FOUNDATION AUDIT — HUB-NATIVE EVIDENCE INDEX
2026-07-07 · claude-physics · scope: [local path omitted]
Status legend: CONFIRMED_IN_HUB | AUDIT_REPORTED_NOT_IN_HUB | NOT_FOUND_IN_HUB | JUDGMENT_REQUIRES_HUMAN_PHYSICIST

The purpose of this index is epistemic honesty: it separates what [local path omitted]
the foundation audit reported using external (Z:) sources, from what only a human physicist can judge.
NOTE: "AUDIT_REPORTED_NOT_IN_HUB" does NOT mean false. Two of these were hand-verified on Z: by
claude-physics on 2026-07-07; they simply cannot be re-proven from inside [local path omitted]

| # | Claim | Hub source (path / line) | Status |
|---|-------|--------------------------|--------|
| 1 | Foundation audit document exists | outbox\a2_foundation_audit_20260707\A2_FOUNDATION_SUFFICIENCY_AUDIT.md | CONFIRMED_IN_HUB |
| 1b | Audit checksum file exists + matches | outbox\a2_foundation_audit_20260707\SHA256SUMS.txt; doc sha256 = ae468fbf...ce1b2a (recomputed by claude-physics = matches file AND Codex's report) | CONFIRMED_IN_HUB |
| 2 | Audit ledgered in Hub governance | ledger\ledger.md + ledger.jsonl, timestamp 2026-07-07T14:24:10 | CONFIRMED_IN_HUB |
| 3 | A2 final manuscript package + hashes present | outbox\A2_FINAL_DETECTIVE_HARDENING_20260707_075631\ : tex f8d1e2c3..., pdf 8ec9410a..., re-emit zip 95589049... | CONFIRMED_IN_HUB |
| 4 | A2 is framed as a *stability scan of a sealed/frozen benchmark*, NOT a derivation | A2_ALLOWED_CLAIMS.md (sha 7a056f0f...): "...applied to the frozen BIH-VI benchmark. In the claim-bearing hard envelope K<=0.06, equilateral and squeezed configurations are **stable under the sealed G-S criteria**." | CONFIRMED_IN_HUB |
| 5a | The ten-term ledger exists in Hub as a sealed/hardcoded instrument STRUCTURE consumed by the scan (self-described as a sealed instrument). Whether it is DERIVED is not determinable from Hub — see Tier 2 / 6a. | runs\A2_PRODUCTION_LOCAL\a2_production_scan.py (sha 35fd3659...), L5-6: "Decision A implementation: Uses the sealed G-S v3 bounded-eta_H instrument structure." | CONFIRMED_IN_HUB |
| 5b | Ledger tokens O1,O2,O3a,O3b,O3c,V1,V2,f2,f3,f4,B_total present as hardcoded instrument terms consumed by the scan | a2_production_scan.py (integrand functions + B_total sum); A2_ALLOWED_CLAIMS.md; A2_FINAL_DATA_LOCK source_outputs | CONFIRMED_IN_HUB (present as sealed/hardcoded instrument terms; whether they are DERIVED is Tier 2 / 6a) |
| 5c | Provenance string "sealed by A2_BENCH_ETA" | Only in a2_gs_surface_sweep_v3.py, which lives at SimulationLab\Hub\frozen — NOT in [local path omitted]| NOT_FOUND_IN_HUB (as primary artifact) |
| 5d | "A2_BENCH_ETA" / "BENCH-eta" token in a primary artifact | Grep of [local path omitted], this task file, and Codex followup — never in a physics artifact | NOT_FOUND_IN_HUB |
| 5e | A2_RUN01_FINAL_VERDICT.json with final_A2_closure=false | File lives on Z: (A2_RUN01_...zip). Hand-verified on Z: by claude-physics 2026-07-07 (= false). Not present in [local path omitted]| AUDIT_REPORTED_NOT_IN_HUB |
| 5f | cmb_safety_flag = REQUIRES_REVIEW_large_K_lt_1_kernel_value | Same Z: verdict JSON; hand-verified on Z:. Not in [local path omitted]| AUDIT_REPORTED_NOT_IN_HUB |
| 5g | Operator registry tags "TODO_exact_inin" | Z: (A2_CUBIC_OPERATOR_REGISTRY.json). Not in [local path omitted]| AUDIT_REPORTED_NOT_IN_HUB |
| 5h | "Non-Gaussianity and loop/backreaction constraints remain to be computed" | Z: Technical Report Sec 11.5. Not in [local path omitted]| AUDIT_REPORTED_NOT_IN_HUB |
| 5i | "A full all-operator EFT bispectrum and folded/squeezed triangle scan remain open" | Z: Module A/B addendum. Not in [local path omitted]| AUDIT_REPORTED_NOT_IN_HUB |
| 5j | Referee-facing manuscript on Z: contains 0 ten-term-ledger tokens (grep-zero) | Z: BIH_VI_unified_manuscript.tex; hand-verified grep by claude-physics 2026-07-07. Not re-provable in [local path omitted]| AUDIT_REPORTED_NOT_IN_HUB |
| 6a | The ledger is not DERIVED (no cubic-action derivation exists) | Absence-of-derivation cannot be proven from [local path omitted]; requires the derivation's true home + a human check | JUDGMENT_REQUIRES_HUMAN_PHYSICIST |
| 6b | The O4 -> V1+V2 "bounded-eta" replacement is legitimate (IBP/field-redefinition-justified) vs an artifact | Physics judgment; no numerical self-consistency can settle it | JUDGMENT_REQUIRES_HUMAN_PHYSICIST |
| 6c | Verdict "derive-from-scratch / two-paper" | Audit synthesis (AI-generated); needs human confirmation | JUDGMENT_REQUIRES_HUMAN_PHYSICIST |

## Net Hub-native reading (two distinct tiers — do not conflate)
**Tier 1 — what Hub evidence proves by itself:** A2 is *scoped* as a stability scan of a sealed
instrument, and is therefore NOT self-sufficient for submission as a derived-physics result. This
rests on two independent Hub facts: (i) the production script self-describes as using a **sealed
instrument** (5a), and (ii) A2's own allowed-claims file scopes the result to **stability under
sealed G-S criteria** (4) — a stability/reproducibility statement, not a derivation claim. This
supports a **conservative downgrade in submission posture**.

**Tier 2 — the stronger "asserted, not derived (nowhere)" finding:** this is NOT proven by Hub
evidence alone. Hub scope cannot establish the *absence of a derivation* anywhere. That stronger
claim depends on the audit's external (Z:) evidence — closure=false, the theory's own documents
disavowing the all-operator bispectrum as open, the "sealed by A2_BENCH_ETA" provenance — all
recorded here as AUDIT_REPORTED_NOT_IN_HUB — and ultimately on human-physicist review (6a–6c).

**Conclusion:** Hub evidence alone supports "A2 is not self-sufficient for submission." The
stronger "asserted-not-derived, nowhere" conclusion remains an audit/human-physics claim unless the
primary external evidence is copied into [local path omitted]
unchanged; the Hub-native *proof* is narrower and more conservative than the audit's full claim.
