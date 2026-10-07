# Research Overview

## The Central Question

This collection explores whether spacetime, matter, and observation can be described through boundaries, relational structure, and limits on accessible information. It contains several attempts at that question. Their conceptual relationship does not make them a single verified mathematical theory.

The strongest public presentation is a research program with inspectable calculations, failed or incomplete branches, and explicit next tests. The value lies in what a reader can examine and challenge.

## 1. BIH-VI: A Boundary-Anchored Cosmological Model

The background reports study a spherically symmetric geometric boundary described by

```text
chi = h^(ab) (d_a R)(d_b R) = 1 - 2 G E_MS / R
chi = 0  <=>  R = 2 G E_MS
```

They then choose a regulated entropy derivative and reconstruct a bounded background under the report's thermodynamic assumptions. The displayed Friedmann relation is for its spatially flat, zero-cosmological-constant branch:

```text
S_A = 1 / [4 G sqrt(1 - A_c/A)]
H^2 = (8 pi G / 3) rho [1 - 2 pi G rho / (3 H_c^2)]
```

These equations are reproduced from the technical report's equation map as model definitions and derived relations within its stated assumptions. Their inclusion is not a new validation of the assumptions, a microscopic derivation of the entropy law, or evidence that the observed universe is a black-hole interior.

The report develops an effective single-clock realization and a parameterized exit switch. It provides parameter tables, figures, and Mukhanov-Sasaki convergence summaries. The archive's own limitations include the unexplained switch parameters, missing microscopic completion, and incomplete transfer/reheating treatment. The original generator of every early report figure was not recovered; those figures remain recorded outputs rather than fully reproduced results of this release.

### The A2 Result

The later A2 calculation evaluates the specified ledger

```text
B_total = O1 + O2 + O3a + O3b + O3c + V1 + V2 + f2 + f3 + f4
f_NL = (5/6) B_total / (P1 P2 + P1 P3 + P2 P3)
```

The July 6 record reports 13 passing gates and 22 claim-bearing rows: 11 equilateral and 11 squeezed. Their hard envelope is `K <= 0.06`. Fourteen folded/flattened rows are diagnostic; none passed G-FLAT. The report's exact allowed wording is preserved in [A2_ALLOWED_CLAIMS.md](../bih-vi/manuscript/locked/A2_ALLOWED_CLAIMS.md).

The unresolved question is whether replacing the raw `O4` interaction with `V1 + V2` and the associated `f2/f3/f4` terms follows from the appropriate cubic action, constraints, boundary treatment, and field redefinition. Numerical agreement between two implementations of the same forms does not answer that question.

**Useful next scientific work:** an independently checked derivation of that reduction, with assumptions and boundary terms stated. A new scan would only become evidence for the physical claim after that connection is established.

### The Late-Universe Branch

The older C-series work explores distance-ladder and density-field diagnostics. The closure note reports restrictive or negative outcomes, including survey sensitivity. It is retained under `archive/bih-vi/`, separately from A2. It supplies no evidence for an A2 detection or a Hubble-tension solution. Some third-party observational inputs are deliberately not redistributed; the old pipelines are not presented as turnkey reproductions.

## 2. RNSF: From Broad Proposal To A Testable Instrument

The RNSF manuscript proposes a relational substrate and coarse-graining framework. The Phase 0 definitions narrow several earlier ideas: they distinguish capacity from realized entanglement and separate horizon-like loss of access, failure of geometric fitting, and saturation.

The Phase 1 code is a more concrete object: an open-boundary transverse-field Ising chain, implemented through a Gaussian/Majorana covariance method and an exact-diagonalization method. Its checks concern ground-state energy, contiguous-block entropy, a first-law identity, and the structure of an entanglement Hamiltonian.

That distinction matters. Agreement with known lattice-model behavior is useful instrument evidence. It does not derive spacetime, validate a particle model, or establish the broader substrate proposal. The Phase 0 notes retain gates on later experiments, including novelty review and explicit failure conditions.

**Useful next scientific work:** independent review of the definitions and Phase 1 instrument, followed by a sharply specified experiment that can produce a negative result. No later phase is claimed complete here.

## 3. Quantum Observation, Light, And Dimensional Projection

The selected V8 quantum thesis develops a relational/contextual discussion of classicality. The light and dimensional-projection drafts explore higher-dimensional interpretations and possible geometric accounts of probability. The phase-shift papers extend into philosophy and consciousness.

These are conceptual research manuscripts. Claims in the historical text such as "proves the Born rule," "resolves," or "unifies" remain claims of those drafts, not the release's endorsed conclusion. In particular, a proposed probability construction must be checked for circular assumptions, and an analogy involving an observer does not establish a new physical interaction.

The filenames do not establish a single linear revision sequence: `RSI_v1` and `RSI_v2` have substantially different subject matter, and a document named `Final` can precede V8. The selected reading order reflects contents and revision labels, with earlier distinct material retained in the archive.

## 4. Exploratory Visualizations And Notebook Prototypes

The Conscious Physics notebooks contain random-number stubs for masses and lags, iterative code replacement, and fitting examples. Their figures and animations are historical visualizations. They are not BIH exit-switch simulations and cannot establish a mass-lag law, consciousness mechanism, or cosmological result.

Their notebook execution has been disabled in this distribution while preserving source cells as readable text. The repository does not invent a physical solver to fill the gap.

## What Holds The Collection Together

The projects share questions about boundaries, information access, effective descriptions, and emergence. A defensible synthesis preserves four distinct layers:

| Layer | What the release provides | What it does not establish |
|---|---|---|
| Ideas | Organized hypotheses and conceptual manuscripts | Novelty, priority, or truth of the proposals |
| Mathematics | Stated equations and derivation drafts | Independent verification of all derivations |
| Computation | Recovered code, data, checksums, and supported reproduction checks | Physical validity from numerical agreement alone |
| Interpretation | Explicit limits and proposed next tests | Observational confirmation or engineering applicability |

This edition improves navigation, portability, disclosure, and traceability. Scientific disagreements and missing derivations remain visible so a reviewer can do useful work.
