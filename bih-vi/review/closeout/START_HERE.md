# A2 PROGRAM — CLOSEOUT PACKAGE (START HERE)
2026-07-07 · claude-physics · a single entry point to process, verify, back up, and hand off the
entire BIH-VI A2 program.

## What this package is
An INDEX, not a re-copy. The big artifacts (manuscript, data lock, production run, audits) stay in
their existing [local path omitted]; this package points at each one with its exact SHA-256 so you
can find, verify, and back up everything from one place. Five short files:

- `START_HERE.md`         — this file.
- `A2_PROGRAM_STATE.md`   — the honest full state, in two tiers (what's done vs. what's gated).
- `OPEN_DECISIONS.md`     — the 3 things that need YOU (nothing else is blocking).
- `FOR_THE_PHYSICIST.md`  — a one-page brief for the human expert; hand them this + the evidence bundle.
- `ARTIFACT_MANIFEST.csv` — every key artifact: path, sha256, bytes, role, status.
- `SHA256SUMS.txt`        — checksums for this package.

## The one-paragraph truth
The A2 numerical program is COMPLETE and reproducible: production run PASS (13/13 gates), accepted
data lock, a compiled 10-page manuscript (FINAL_PASS, externally accepted), all hash-locked. It is
NOT yet submittable physics: the ten-term bounded-eta_H ledger it scans is a sealed instrument whose
derivation has not been written for a human reviewer. That is a real gate, and only a human
physicist can clear it. Nothing more for AI tooling to do here.

## How to use this package
1. Read `A2_PROGRAM_STATE.md` (5 min) — the honest picture.
2. Do the top item in `OPEN_DECISIONS.md` — the backup — first. It's 30 seconds and everything else
   can wait behind it.
3. When you find a physicist, hand them `FOR_THE_PHYSICIST.md` plus the evidence bundle
   (`outbox\a2_foundation_audit_evidence_bundle_20260707\`).
4. Verify anything with `ARTIFACT_MANIFEST.csv` — every hash is current as of 2026-07-07.

## Rails honored building this
No numerics rerun. No locked A2 artifact modified. No [local path omitted]
files already in [local path omitted], plus this package. Ledgered.
