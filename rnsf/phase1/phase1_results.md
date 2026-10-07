# RNSF Phase 1 — Instrument Report (v1.0)

Status: **PASSED.** The Gaussian (Majorana covariance) pipeline for the OBC
TFIM is validated against exact diagonalization at machine precision and
reproduces three known structures: the Calabrese–Cardy entropy law, the exact
entanglement first law with its second-order (Kubo–Mori) Fisher term, and the
Eisler–Peschel / CHM locality structure of the entanglement Hamiltonian.
This is the instrument for Phases 2–5. Nothing here is a new physics claim.

Code: `gaussian_tfim.py`, `ed_tfim.py`, runner `run_phase1.py`,
numbers `phase1_numbers.json`, figures `fig_cc_fit.png`, `fig_first_law.png`,
`fig_eh_profile.png`.

## A. Pipeline validation (ED ↔ Gaussian), N = 10, OBC

Ground energy and entropies of **all** contiguous intervals (edge and bulk):

| h   | \|E_ff − E_ed\| | max over intervals \|S_ff − S_ed\| |
|-----|----------------|-----------------------------------|
| 1.0 | 3.6e-15        | 2.7e-13                            |
| 1.5 | 1.4e-14        | 4.6e-13                            |

The spin-block / fermion-block isospectrality for contiguous intervals is
empirically exact at this precision, for edge and bulk placements.

## B. Calabrese–Cardy, N = 200, h = J = 1, edge intervals

Fit S(ℓ) = (c/6) ln[(2L/π) sin(πℓ/L)] + b on even ℓ ∈ [20, 180]:

- **c = 0.50618** (Ising c = 1/2; relative error 1.24%, finite-size +
  boundary-oscillation limited; even-ℓ-only fit, no oscillatory term)
- rms fit residual 6.1e-5 nats.

## C. First law, ED N = 12, A = sites [4..7], h = 1 → 1+δ

- Exact algebraic identity δ⟨K_A⟩ − δS_A = S_rel(ρ′‖ρ) holds to ≤ 2.1e-15 at
  every δ ∈ [1e-4, 1e-1].
- S_rel ∝ δ²: log-log slope 1.9698 over the full range (contaminated by
  δ = 0.1 where higher orders enter); local slope at the smallest decade
  1.9995 → 2.000 as δ → 0. First law verified.
- Kubo–Mori metric along h at criticality for this interval:
  **g_KM = 10.314** (= lim 2 S_rel/δ²).
- Cross-check of the Gaussian entanglement Hamiltonian against ED:
  δ⟨K⟩ computed as −¼ Tr[W ΔΓ_A] agrees with Tr[Δρ_A K_A] to ≤ 1.9e-12
  across all δ (bulk interval). The single-mode functional calculus is
  Γ₁₂ = −tanh(W₁₂/2), i.e. W = −2 artanh(Γ_A) blockwise; the sign was fixed
  against ED during validation.

**Edge-interval footnote.** For the edge interval [0..3] the same cross-check
shows an O(δ²)·10⁻³ residual. Traced: the many-body ρ_A there has an
eigenvalue ≈ −1.9e-18 (below float64), so the ED-side K is the regularized
object; the Gaussian side (smallest single-particle 1−λ = 1.75e-10, well
resolved) is the more accurate operator. Not a physics discrepancy.

## D. Entanglement Hamiltonian structure, N = 400, centered ℓ = 10, h = J = 1

- Nearest-neighbor Majorana couplings of W follow the CHM parabola
  x(2ℓ − x): **R² = 0.9983** (interior bonds).
- NN couplings carry **98.6%** of the total off-diagonal weight of W:
  quasi-local, Eisler–Peschel structure reproduced.
- **Purity ceiling (documented limitation):** at criticality, interval
  single-particle purities 1−λ fall below float64 noise for ℓ ≳ 12–16
  (ℓ = 40 has 26 unresolvable modes). Full W extraction in float64 is
  limited to ℓ ≲ 12; larger ℓ requires extended precision or asymptotics.
  Entropies are unaffected (symmetric in λ).

## Caveats / scope

1. **Ferromagnetic phase (h < J) deferred:** ED ground state is a parity
   doublet (splitting exp. small); the Gaussian construction selects a
   definite-parity vacuum. Validation was performed at h ≥ 1 only.
   Parity-resolved treatment required before any h < J claim.
2. **Disjoint intervals are out of scope** for the spin↔fermion
   correspondence (Jordan–Wigner string obstruction); all statements are for
   contiguous blocks.
3. **Metric declaration:** this instrument's second-order object is the
   Kubo–Mori metric (Hessian of relative entropy), not the SLD/Bures QFI
   that A_p uses. KM ≥ SLD; equal classically. Phase 2 computes SLD.
4. c at 1.24% is finite-size limited; adequate for instrument validation,
   improvable with an oscillatory fit term or larger N if ever needed.

## Gate to Phase 2

Per `phase0_definitions.md` §8: arXiv novelty check on
(i) subalgebra-restricted quantum Fisher information,
(ii) Fisher information / thermofield double,
(iii) symmetry-resolved quantum Fisher information,
(iv) modular inclusion lattice numerics —
**before any Phase-2 code.** Then: Gaussian TFD of two chains, quadratic
inter-chain coupling, restricted Bures-QFI spectroscopy F^R(t; β, g) with
diagnostics n₀, A_p(F^R), σ.
