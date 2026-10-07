# A2 PROGRAM CLOSEOUT — EVIDENCE INDEX (PROJECT_FIREWALL vocabulary)
2026-07-07 · claude-physics · firewall-compliant classification of this closeout's own claims.
Vocabulary per [local path omitted]

| Claim | Status | Claim level | Evidence |
|---|---|---|---|
| A2 production run computed as specified, 13/13 gates PASS, reproducible | CONFIRMED_IN_HUB | COMPUTATIONALLY_VALID | A2_PRODUCTION_LOCAL_20260706_154312.zip (e8500cc3...), production_manifest.json (b01d9305...) |
| Data lock accepted; hashes intact | CONFIRMED_IN_HUB | LOCALLY_VERIFIED | A2_FINAL_DATA_LOCK_20260706_160748.zip (061dc918...) + inbox\20260706_a2_datalock_acceptance\ACCEPTANCE.md (8e55a4b2...) |
| Manuscript compiles (10-pp PDF), FINAL_PASS, externally accepted | CONFIRMED_IN_HUB | LOCALLY_VERIFIED | ...075631_FINAL_PASS_REEMIT.zip (95589049...), A2_MANUSCRIPT_FINAL.pdf (8ec9410a...) + inbox\20260707_a2_manuscript_acceptance\ACCEPTANCE.md (517d33ed...) |
| A2 result is SCOPED to a sealed instrument / stability scan (not a derivation) | CONFIRMED_IN_HUB | DOMAIN_READY_GATED | A2_ALLOWED_CLAIMS.md (7a056f0f...): "stable under the sealed G-S criteria"; a2_production_scan.py L5-6 "uses the sealed ... instrument structure" |
| The ten-term ledger's derivation is not written in human-reviewable form | REPORTED_NOT_IN_HUB | (audit finding) | A2_FOUNDATION_SUFFICIENCY_AUDIT.md (ae468fbf...); primary disavowal evidence lives on Z: (closure=false, "remain to be computed") — not re-provable Hub-native |
| The O4 -> V1+V2 bounded-eta replacement is legitimate physics vs. an artifact | HUMAN_DOMAIN_REVIEW_REQUIRED | — | No agent verification can settle it; see FOR_THE_PHYSICIST.md |
| A2 is submission-ready as derived physics | NOT established | — | Blocked on derivation + physicist review; explicitly NOT CLIENT_OR_SUBMISSION_READY |
| Off-drive backup exists | LOU_DECISION_REQUIRED -> RESOLVED (Lou reports backups made 2026-07-07) | — | Reported by Lou; not an in-Hub artifact |

## Firewall default closeout sentence (applies here)
Computational integrity is verified inside [local path omitted]
the ten-term ledger is derived in human-reviewable form and a qualified physicist confirms the
O4 -> V1+V2 reduction. Backup is reported done by Lou (outside this Hub package).
