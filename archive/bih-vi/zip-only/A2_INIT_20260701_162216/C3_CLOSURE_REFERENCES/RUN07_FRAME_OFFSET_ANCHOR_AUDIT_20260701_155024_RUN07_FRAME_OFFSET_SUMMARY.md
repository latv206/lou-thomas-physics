# BIH-VI C3-F Run07 - Pure Frame-Offset Anchor Audit

Status: **RUN07_FRAME_OFFSET_ANCHOR_AUDIT_COMPLETE**

Result:

> **method_dependent_frame_offset**

Allowed claim:

> The frame-offset burden appears method-dependent: SH0ES-like Cepheid/SN anchors require a large offset, while other anchors prefer a smaller one.

## Core formula

```text
Delta M_B0 = 5 log10(H0_anchor / H0_geom)
```

Default geometry baseline:

- H0_geom = 67.4
- sigma_geom = 0.5

## Key values

| Quantity | Value |
|---|---:|
| SH0ES-like Delta_M_B0 | 0.174504 +/- 0.034864 mag |
| All test anchors weighted Delta_M_B0 | 0.131483 +/- 0.023968 mag (n=6) |
| Independent geometric weighted Delta_M_B0 | 0.199923 +/- 0.089612 mag (n=1) |
| Non-SH0ES weighted Delta_M_B0 | 0.092930 +/- 0.033004 mag (n=5) |
| SH0ES target vs independent geometric tension | -0.264349 sigma |
| SH0ES target vs non-SH0ES tension | 1.699198 sigma |

## Interpretation guardrails

- This is an anchor-ledger audit, not a production likelihood.
- The Run06 density-coupled branch remains closed as survey dependent.
- Do not claim that the Hubble tension is solved.
- Do not claim a universal frame offset is proven.
- Treat method-systematics and anchor covariance as required future work before any stronger claim.

## Evidence files

- `run07_anchor_offset_ledger.csv`
- `run07_anchor_report_table.csv`
- `run07_frame_offset_group_tests.csv`
- `RUN07_FRAME_OFFSET_FINAL_VERDICT.json`
- `run06_closure_evidence/` when a Run06 handoff directory is available
