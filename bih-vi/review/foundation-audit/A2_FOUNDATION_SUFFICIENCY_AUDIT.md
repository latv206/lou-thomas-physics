# A2 FOUNDATION-SUFFICIENCY AUDIT — findings
2026-07-07 · claude-physics · authorized by Lou ("do what we need to do")
Method: 3 independent read-only readers over [local path omitted]
synthesis (Opus 4.8), followed by claude-physics hand-verification of the two load-bearing facts.
This is a read-only assessment. No numerics rerun; no locked A2 artifact touched.

## Verdict
The published A2 result does NOT have a referee-grade foundation. The bounded-eta_H all-operator
ledger — the mathematical object the entire A2 program is a stability scan OF — is **asserted, not
derived**, and its derivation exists nowhere in human-reviewable form. Recommended path:
**Option B — a narrow, firewalled foundation companion paper**, whose core deliverable
(the cubic-action derivation) must be **written from scratch**. Estimated ~6–10 weeks of physicist
time. This is a foundational gap, not a cosmetic one.

## The three documentary facts (hand-verified by claude-physics, not just reported)
1. **The ledger is asserted / internal-only.** B_total = O1+O2+O3a+O3b+O3c+V1+V2+f2+f3+f4 with
   f_NL=(5/6)B/SPP appears as a *specification* in one file (the Claude handoff, "Section 4 —
   USE EXACTLY THIS") and as *hardcoded integrands* in the frozen script a2_gs_surface_sweep_v3.py,
   whose own docstring reads "Ledger + kernels: sealed by A2_BENCH_ETA (Claude, 2026-07-01)." The
   "independent unit-test engine" that validates it is labelled "verbatim BENCH-eta" — a second
   implementation of the SAME asserted forms. Validation is numerical self-consistency between two
   Claude-authored implementations plus hash-matching. No cubic-action derivation exists.
2. **The theory's own referee-facing documents disavow it as open.** VERIFIED by grep: the unified
   manuscript mentions only the single "switch-enhanced interaction" (raw O4) — 0 occurrences of the
   ten-term ledger tokens. Technical Report Sec 11.5: "Non-Gaussianity and loop/backreaction
   constraints remain to be computed." Module A/B addendum: "A full all-operator EFT bispectrum and
   folded/squeezed triangle scan remain open." Raw standalone O4 is the ledger's OWN forbidden line.
3. **The paper-named artifact self-declares incomplete.** VERIFIED by reading the JSON:
   A2_RUN01_FINAL_VERDICT.json contains `final_A2_closure = false` and
   `cmb_safety_flag = REQUIRES_REVIEW_large_K_lt_1_kernel_value` (O3 schematic, O5 not computed,
   instantaneous-BD not Mukhanov–Sasaki modes, fNL ~ 8.5e26 at K=0.1). The operator registry tags
   every operator "TODO_exact_inin."

## What IS real (do not overcorrect into nihilism)
- The A2 production scan is a *correct, reproducible computation of the asserted ledger*. Its
  hashes, gates, and claim-discipline are genuine and hold. What it computed is stable.
- The Sqrt-Reg thermodynamic chain and the slow-roll observables (n_s, r, alpha_s) ARE followable/
  derived in the Technical Report. The engine is partly on solid ground.
- The claim-wording discipline (allowed-claims file, forbidden list) is exactly right and is what
  makes the gap *visible* rather than hidden.

## What is NOT established (the honest gap)
- That the ten-term ledger is a *legitimate reduction of the true BIH-VI cubic action*. The
  load-bearing novelty — replacing the Maldacena eta-dot operator O4 by V1+V2 plus nonlocal
  field-redefinition terms f2/f3/f4 — has NO derivation anywhere. If that replacement is not an
  IBP/field-redefinition-justified reduction, the bounded/stable A2 result is an artifact of an
  asserted ansatz, and no amount of numerical self-consistency can rescue it at referee.
- Missing, specifically: (1) ADM cubic-action expansion of the EFT-clock scalar sector;
  (2) the solved lapse/shift constraint O3a/b/c depend on; (3) first-principles justification of the
  bounded-eta_H (O4 -> V1+V2) replacement and the f2/f3/f4 terms; (4) Maldacena IBP to B_total;
  (5) a no-ghost/gradient-stability proof FROM the model's own action (currently only textbook
  positivity conditions are quoted); (6) a selection principle for the frozen island (params are
  "parameterized rather than derived," Tech Report 11.2).

## The deeper lesson (stated plainly)
The verification apparatus this program is proud of — hash-locking, declared gates, two-party
review (Claude + GPT + external reviewer) — was rigorous about REPRODUCIBILITY and CLAIM-WORDING.
None of it touches whether the ledger is DERIVED physics. Hash-locking guaranteed we recomputed the
same asserted object identically; it could not guarantee the object was correct. The layer that was
never independently verified is the one that matters most, and it can only be closed by a human
physicist working the derivation, independent of the Claude/GPT tooling. Numerical agreement
between two Claude implementations of the same hardcoded forms is not independent verification.

## Firewall (severe, non-negotiable)
The only manuscript on the drive is structurally a Hubble-tension paper (H0 ladder, Delta M_B ~
0.18 mag, CPL dark-energy scaffold, SH0ES/Planck/Pantheon+/DESI, Q_bulk). Its late-universe C3/C4
content is exactly what A2's allowed-claims forbid as A2 evidence. A2's foundation must be a fresh,
early-branch-only companion — NOT carved from or cited into that manuscript.

## Ordered next steps (physicist work, not packaging)
1. STOP citing A2_RUN01 as "the A2 result" — its own verdict file says final_A2_closure=false.
2. Write the ADM cubic-action expansion (LaTeX, human-reviewable) incl. the solved lapse/shift
   constraint. This brick exists nowhere.
3. DERIVE the bounded-eta_H replacement (O4 -> V1+V2) and the f2/f3/f4 terms by field
   redefinition + IBP — the load-bearing novelty, currently only sealed code.
4. Complete the Maldacena IBP to B_total; derive no-ghost/gradient stability from the model action.
5. Re-run A2 with exact in-in kernels + full Mukhanov–Sasaki modes so the scan is backed by the
   derived ledger, not the sealed script; report the honest K-envelope.
6. Assemble Paper 1 (foundation, early-branch-only, firewalled) and Paper 2 (A2 scan citing Paper 1).
7. Have the derivation checked by a HUMAN physicist independent of the AI tooling before submission.

## Scope note on THIS audit
This audit is itself AI-generated and inherits the same caution it raises: its *documentary* claims
(closure=false, grep-zero ledger tokens, "sealed by A2_BENCH_ETA", "remains to be computed") are
directly verifiable and two were hand-checked by claude-physics. Its *judgment* (derive-from-scratch,
Option B) should be confirmed by the same human physicist who would check the derivation.
