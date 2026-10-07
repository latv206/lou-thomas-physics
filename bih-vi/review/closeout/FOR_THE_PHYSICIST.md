# FOR THE PHYSICIST — a one-page brief
You've been handed this because a specific, bounded question needs a human expert. Thank you.
It should take about an hour to orient, and the ask is narrow.

## What was done
An automated pipeline computed the tree-level curvature bispectrum on a single frozen benchmark of
an EFT-of-inflation "clock" background (a Sqrt-Reg entropy-shield realization; standard single-field
machinery). It scanned equilateral, squeezed (q=1e-3), and folded triangles over a hard grid
K in [0.010, 0.060] and tested SURFACE-INDEPENDENCE and convergence of the result as a stability
criterion. In the hard envelope K <= 0.06 the equilateral and squeezed configurations are stable
under those pre-registered checks; folded/flattened rows are reported diagnostic-only (a zero of
B_total near the grid edge makes a log-slope estimator misfire -- documented, benign).

## The bispectrum ledger under review
B_total = O1 + O2 + O3a + O3b + O3c + V1 + V2 + f2 + f3 + f4,   f_NL = (5/6) B_total / (P1P2+P1P3+P2P3)
with O1..O3c the standard cubic operators, and -- the novelty --
  V1, V2  = "bounded-eta_H" replacement terms substituted for the Maldacena eta-dot operator O4;
  f2,f3,f4 = nonlocal/decaying field-redefinition (boundary) terms.
Dimensionful P(k) in the denominator (no Delta^2). Raw O4 is deliberately excluded from physical rows.

## The ONE question we need answered
Is the replacement of the raw eta-dot operator O4 by (V1 + V2) plus the field-redefinition terms
(f2, f3, f4) a LEGITIMATE reduction of the true cubic action -- i.e. justified by integration-by-parts
and a proper field redefinition of THIS model's action -- or is it an asserted ansatz?

Why it matters: the ledger's derivation was never written for human review. It exists as a
specification and as hardcoded kernels validated only by numerical self-consistency between two
implementations of the SAME forms. If the O4 -> V1+V2 step is legitimate, the stability result is
real and needs a foundation paper. If not, the bounded result is an artifact and no numerical
agreement can rescue it.

## What to look at
- `EVIDENCE_INDEX.md` and `PRIMARY_EXCERPTS.md` in the evidence bundle -- what is proven from the
  local record vs. what is asserted vs. what needs your judgment (a two-tier honesty split).
- `A2_FOUNDATION_SUFFICIENCY_AUDIT.md` -- the internal audit that flagged this gate.
- The sealed script `a2_production_scan.py` -- the actual kernels (integrand_O1..O3c, the FR pieces).
- `GPT_REVIEW_PROMPT.md` -- doubles as a structured checklist of the sub-questions.

## What we are NOT asking you to endorse
Not the cosmology, not any H0/dark-energy claims (explicitly firewalled out), not "the theory."
Only: is that one operator-basis reduction sound? A clear "yes / no / here's the missing step" is
exactly what unblocks the next 6-10 weeks (a proper ADM cubic-action derivation) -- or redirects it.
