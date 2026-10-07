# RNSF Phase 0 — Formal Core (v0.1)

Definitions only. No claims. Every downstream experiment references these
objects by name. Changes to this file are versioned.

## 0. Substrate data

A substrate is a triple (G_net, |Ψ⟩, C): a network G_net = (V, E, χ) with bond
dimensions χ_e on links; a global pure state |Ψ⟩ on the constrained Hilbert
space; a constraint set C (gauge rules, superselection structure, update
rules). The symbol Γ is reserved for Majorana covariance matrices in code;
the network is always G_net.

## 1. Capacity vs realized entanglement

For a subset R ⊂ V:

- **Capacity** C(∂R) = min over cuts γ separating R from its complement of
  Σ_{e∈γ} ln χ_e. Kinematic, state-independent.
- **Realized entanglement** S_Ψ(R) = −Tr ρ_R ln ρ_R. State-dependent.
- Always S_Ψ(R) ≤ C(∂R).
- **Saturation ratio** σ(R) = S_Ψ(R)/C(∂R) ∈ [0, 1].

Geometry, wherever it appears, tracks S_Ψ. Capacity is the ceiling. These are
never interchanged. (This replaces the area = capacity identification in the
holography synthesis document, which made geometry state-independent and
contradicted its own dynamics section.)

## 2. Region correspondence

j maps declared substrate subsets to declared "regions." Required properties:
nesting (R₁ ⊂ R₂ ⇒ j(R₁) ⊂ j(R₂)) and complement consistency. In 1D
substrates, j = contiguous intervals and is trivial. In d > 1 it is the
entanglement-wedge problem and is **open**; no d > 1 claim is made until j is
constructed.

## 3. Decoder: geometry as best fit

Declare a geometry class 𝒢 with an entropy functional S_g(A) (for 1+1
critical substrates: the Calabrese–Cardy family, equivalently hyperbolic bulk
slices; for gapped substrates: capped families). Then

  g* = argmin_{g∈𝒢} max_{A∈range(j)} |S_Ψ(A) − S_g(A)| / S_g(A)
  ε_J = the attained minimum.

The emergent geometry **is defined as** g*; ε_J is the dimensionless,
size-normalized fit error. ε_J is data, not notation, only once 𝒢, j, and the
region family are declared. Non-uniqueness of g* is expected (entanglement
shadows); degenerate minimizers are recorded, not hidden.

## 4. Failure modes (replaces the v3 single J-trigger)

Three logically independent conditions, measured separately:

- **F1 — Horizon:** the exterior-restricted response is degenerate (Sec. 5
  machinery) while ε_J remains small. Geometry exists; it hides degrees of
  freedom.
- **F2 — Non-geometric:** ε_J = O(1) for every g ∈ 𝒢. No geometry fits.
  Singularity analog: the decoder fails to exist, not merely to invert.
- **F3 — Saturation:** σ(R) → 1 on a family of cuts. Capacity exhausted.

The v3 junction-trigger conflated these. They are now separate measurables.
Note this document's decoder is parallel to G_cg (it is G_cg composed with a
geometric fit); the v3 anti-parallel junction map is eliminated, not
repaired.

## 5. No-signaling lemma and the design constraint it imposes

**Lemma.** If |Ψ(θ)⟩ = U_R̄(θ)|Ψ⟩ with U_R̄ supported on the complement of R,
then ρ_R(θ) = ρ_R for all θ, hence the exterior-restricted QFI matrix
F^R(θ) ≡ 0 identically.

*Proof:* ρ_R(θ) = Tr_R̄[U_R̄ |Ψ⟩⟨Ψ| U_R̄†] = Tr_R̄[|Ψ⟩⟨Ψ|] by cyclicity of the
partial trace over R̄-supported unitaries. ∎

**Corollary (design constraint).** "Horizon = exterior QFI degeneracy" is
vacuous for complement-supported perturbation families. F1 diagnostics must
use one of:
(a) **dynamics** — F^R(t) under coupled evolution (perturb inside, evolve,
    measure visibility outside);
(b) **constrained families** — sector/gauge-restricted state deformations
    where unilateral complement action is not allowed;
(c) **straddling generators** — supports crossing ∂R.

## 6. Metric declaration

Two distinct information metrics appear and are never conflated:

- **SLD/Bures QFI** — the metric underlying A_p (spectral entropy of the
  multi-parameter QFI matrix; verified numerics, = ¼ × QFI relation for pure
  states).
- **Kubo–Mori (KM)** — the Hessian of relative entropy; the metric appearing
  in the entanglement first law / canonical-energy statements
  (Lashkari–Van Raamsdonk).

SLD is the minimal monotone metric; KM ≥ SLD; they coincide classically.
Every experiment declares which metric it measures; where feasible both are
reported.

## 7. Sector structure

Given a symmetry/gauge constraint with boundary sector projectors Π_α:
p_α = ⟨Ψ|Π_α|Ψ⟩ (computed from the state, never posited), and

  S = H({p_α}) + Σ_α p_α S(ρ_α) + Σ_α p_α ln d_α.

The decomposition's dependence on the **choice of center** of the boundary
algebra (Casini–Huerta) is a Phase-3 measurement target, not an assumption.
If physical outputs (A_p, ε_J) depend irreducibly on the center choice, the
norm split is declared definitional and the result is recorded as such.

## 8. Phase gates and kill conditions

- **P1 (instrument):** exact lattice first law + EH structure. Theorem-level;
  must pass; failure = bug. [Status: PASSED — see phase1_results.md]
- **P2 gate:** arXiv novelty check on: "subalgebra-restricted quantum Fisher
  information", "Fisher information thermofield double", "symmetry-resolved
  quantum Fisher information", "modular inclusion lattice" — **before any
  Phase-2 code.** Kill: no sharp spectral feature in the (β, g) diagram of
  the coupled-TFD restricted-QFI experiment ⇒ reformulate via (b)/(c) of
  Sec. 5 or publish null.
- **P3 kill:** center-dependence irreducible ⇒ norm split is definitional;
  record and stop claiming dynamical resolution.
- **P4 kill:** ε_J(h) structureless across the TFIM transition ⇒ ε_J carries
  no information in 1D; move to 2D substrates or drop.
- **P5 kill:** lattice modular flows of nested intervals fail to close into
  an approximate inclusion algebra ⇒ the modular route to emergent time dies
  on the lattice; record and stop.
