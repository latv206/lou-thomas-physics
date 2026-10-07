# GATE-6 EVIDENCE — folded K_total=6.0 (RUN01 data, read-only)

RUN01 verdict A2_PRODUCTION_FAIL_FLATTENED_POLE STANDS as computed; this note is
diagnostic evidence for Lou's gate-6 disposition decision, derived exclusively from
the hash-verified RUN01 CSVs. No new physics was run.

## What the data shows
1. AT FIXED K_total=6.0, B_total CHANGES SIGN inside the gated delta family itself:
   -26.14 (delta 1e-2) -> +59.15 (3e-3) -> +85.22 (1e-3).
   The gate's 3-point log|B| slope therefore spans a zero of B_total — the regime
   where a log-slope estimator is mechanically invalid. The measured slope_B=0.516
   is dominated by the sign-flip interval (interval slopes: 0.68 across the flip,
   0.33 after it — DECELERATING; a delta^-p pole accelerates or holds p).
2. Per delta, |B_total| COLLAPSES toward K=6 (|B(6)|/|B(5)| = 0.05-0.30); the
   folded family's upper zero-crossing in K sits at K* ~ 5.8-6.1 depending on delta
   (past the grid edge at delta=1e-2, inside [5,6] at 3e-3 and 1e-3). A pole grows;
   this shrinks and flips.
3. At K=6 the ledger sum is a 98x-318x cancellation residual (top pieces V2/V1/f2,
   each ~30-40x the total) — B_total is a small residual near a zero surface, so its
   log-slope is exquisitely sensitive to delta while nothing physical grows.
4. CAVEAT (honestly reported): the near-K~6 zero-crossing is FOLDED-SPECIFIC — the
   equilateral family shows NO sign change in the production band (B negative
   throughout K in [0.5, 6.0]) and all isosceles K=6 rows are negative. The
   flattened direction of shape space genuinely behaves differently here; that is
   the one datum in favor of taking the trip seriously rather than dismissing it.
5. No amplitude blowup accompanies the trip: folded K=6 fNL in [-0.03, +0.08],
   pert_proxy ~ 1e-7 (physical units); slope_B=0.516 barely exceeds the 0.5
   threshold and is far from the 0.9 'clear pole' criterion; all six other K
   groups pass cleanly (slope_B <= 0.21).

## Reading
The evidence is consistent with a BOUNDED, SIGN-CHANGING B_total near a zero surface
of the flattened geometry at the K-grid edge — i.e. a benign zero-crossing artifact
of the log-slope estimator — and inconsistent with a delta^-p absolute-B pole
(which would grow, accelerate, and not sign-flip). The verdict trip is the gate
working as literally specified on data outside the estimator's assumption. The
folded-specific nature of the zero (point 4) is flagged and argues for RESOLVING
rather than waving through: one more delta decade (1e-4) or K samples bracketing
5.5-6.0 would separate 'finite flattened-limit value' from anything growing.

## Options (decision is Lou's; none executed)
a) Accept RUN01 as-is (gate letter tripped; verdict stands).
b) Authorize RUN02 with a decided gate-6 amendment (exclude sign-flip delta families
   from the log-slope test and/or test a pole model on |B|), plus optionally
   delta=1e-4 and K in {5.25, 5.50, 5.75} to resolve the zero surface.
c) Narrow the production K_total ceiling below the crossing (e.g. 5.5).
Each of (b)/(c) is a spec change + fresh authorization per the A2 gate law.

Derived numbers: gate6_derived.csv. Full trace: GATE6_stdout.log.
Inputs: RUN01 shape_grid + operator_pieces CSVs (hashes verified, recorded in log).

FORBIDDEN-CLAIMS NOTE: no physics claims are made beyond numerical characterization
of RUN01 outputs on the frozen benchmark.