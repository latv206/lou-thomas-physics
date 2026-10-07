# BIH-VI A2_RUN01 — Tree-Level In-In Kernel Pass

Status: **A2_RUN01_TREE_LEVEL_KERNEL_PASS_COMPLETE**

Final A2 closure: **False**

Allowed claim:

> A2_RUN01 produced an operator-separated tree-level in-in kernel table over the fixed shape grid, suitable for auditing; it is not final A2 closure.

## What this run did

- Loaded the fixed A2 shape grid.
- Built the frozen BIH-VI benchmark background.
- Computed operator-separated numerical in-in kernels for:
  - O1: `zeta dot(zeta)^2`
  - O2: `zeta (partial zeta)^2 / a^2`
  - O3: `dot(zeta) partial_i zeta partial_i chi` (**schematic constraint kernel v1**)
  - O4: `epsilon_H dot(eta_H) zeta^2 dot(zeta)`
- Added explicit O5 placeholder rows so missing boundary/field-redefinition terms are not hidden.
- Wrote summed O1-O4 shape results.

## Why this is not final A2 closure

- O3 must be checked against the exact constraint solution for `chi`.
- O5 field-redefinition/boundary contribution is not computed.
- Mode functions are instantaneous-BD/slow-variation approximations, not full numerical Mukhanov-Sasaki modes.

## Next required run

`A2_RUN02_MS_MODE_AND_BOUNDARY_COMPLETION`

That run must:
1. replace the instantaneous-BD modes with numerical Mukhanov-Sasaki modes,
2. implement exact O3 constraint kernels,
3. implement O5 boundary/field-redefinition terms,
4. rerun the same fixed shape grid.

## Main output files

- `A2_RUN01_BENCHMARK_AND_LIMITATIONS.json`
- `A2_RUN01_BACKGROUND_TABLE.csv`
- `A2_RUN01_OPERATOR_SEPARATED_RESULTS.csv`
- `A2_RUN01_SUMMED_SHAPE_RESULTS.csv`
- `A2_RUN01_FAMILY_SUMMARY.csv`
- `A2_RUN01_FINAL_VERDICT.json`
- `A2_RUN01_EVIDENCE_MANIFEST.csv`

## Forbidden claims

- A2 is complete.
- BIH-VI is proven.
- Run01 kernel values are final physical bispectrum predictions.
- The exit bispectrum is observationally detected.
