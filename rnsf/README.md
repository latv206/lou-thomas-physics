# Relational Network Substrate Framework

Start with [Phase 0 definitions](phase1/phase0_definitions.md), then the [Phase 1 instrument report](phase1/phase1_results.md). The [integrated V3 manuscript](manuscript-v3/rnsf_v3_integrated_main.pdf) supplies broader historical context; the later formal definitions explicitly revise some of its constructions.

The Phase 1 code compares Gaussian covariance and exact-diagonalization descriptions of the open-boundary transverse-field Ising model. It provides a concrete computational instrument. It is not a demonstration that gravity or spacetime emerges from that model.

Run `python tools/reproduce_rnsf.py` from the repository root after installing `requirements.txt`. It creates a fresh output directory and compares the resulting quantities with `phase1_numbers.json`. The mathematical routines are preserved; the old runner's sandbox-specific output paths were replaced with a contained output directory. Comments claiming an interval length of 40 were corrected to match the existing calculation's length of 10.

Known scope: the archived validation uses `h >= J`, contiguous intervals, and finite precision. The report documents a purity ceiling for extracting entanglement Hamiltonians. Phase 2 and later are not included as completed experiments.
