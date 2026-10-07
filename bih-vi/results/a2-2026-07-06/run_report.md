# BIH-VI A2 Production Scan

Verdict: **PASS**
Script SHA-256: `35fd365916395f171fee9278480bd102b267f545fb389d6039cfe0058c78aae8`
Runtime: 7.3 sec

## Gates
- UT_K: PASS  `{"passed": true, "value": 2.660212940106564e-15, "tol": 1e-10}`
- UT_FR: PASS  `{"passed": true, "value": 1.0907152156689323e-15, "tol": 1e-10}`
- BG_ETA: PASS  `{"passed": true, "etaN_grad_rel": 8.69514892450742e-05, "aH_0p35": 0.7922204085469607, "tol_eta": 0.001, "tol_aH": 0.03}`
- G_W: PASS  `{"passed": true, "worst_surface_region": 2.152469052996153e-06, "worst_global_transient": 0.00044588600547745827, "tol_surface": 1e-05, "tol_global": 0.001}`
- CONV: PASS  `{"passed": true, "rel_dev": 0.0008409466620926676, "fNL_DN": 0.05886452494286938, "fNL_DNhalf": 0.05891402686863576, "tol": 0.02}`
- G_S_CONTINUITY_SENTINELS: PASS  `{"passed": true, "rows": [{"family": "squeezed", "K": 0.02, "expected": 0.05886452494286938, "actual": 0.05886452494286938, "abs_dev": 0.0, "passed": true}, {"family": "equilateral", "K": 0.02, "expected": 0.037002126018083, "actual": 0.037002126018083, "abs_dev": 0.0, "passed": true}, {"family": "squeezed", "K": 0.04, "expected": 0.058106084779109, "actual": 0.058106084779109, "abs_dev": 0.0, "passed": true}, {"family": "equilateral", "K": 0.04, "expected": 0.030902659690699403, "actual": 0.030902659687979263, "abs_dev": 2.7201400853993363e-12, "passed": true}, {"family": "squeezed", "K": 0.06, "expected": 0.055075, "actual": 0.055074541608155336, "abs_dev": 4.583918446626756e-07, "passed": true}, {"family": "equilateral", "K": 0.06, "expected": 0.022304, "actual": 0.0223037017322976, "abs_dev": 2.982677024011837e-07, "passed": true}], "tol": 0.00075}`
- EQUILATERAL_HARD_ROWS_STABLE: PASS  `{"passed": true, "n": 11}`
- SQUEEZED_HARD_ROWS_STABLE: PASS  `{"passed": true, "n": 11}`
- FOLDED_GFLAT_OR_FLAGGED: PASS  `{"passed": true, "n": 14, "n_gflat_pass": 0}`
- NO_FOLDED_CLAIM_WITHOUT_GFLAT: PASS  `{"passed": true, "n_folded_claim": 0}`
- NO_PROVISIONAL_CLAIM: PASS  `{"passed": true, "n_provisional_claim": 0}`
- NO_K_GT_0P06_CLAIM: PASS  `{"passed": true, "n_gt": 0}`
- EXECUTION_LOCK: PASS  `{"passed": true, "production": true, "lou_authorized": true}`

## Claim envelope
Claim-bearing rows are equilateral + squeezed hard rows only, K <= 0.06, passing sealed G-S criteria.
Folded/flattened configurations are diagnostic/report-only under Decision A unless separately authorized after future instrument validation.

## Claim rows
| family | shape_id | K | f_NL @0.35 | fNL spread | B drift |
|---|---|---:|---:|---:|---:|
| squeezed | squeezed_q0.001_K0.010 | 0.010 | 0.05733057 | 1.857e-05 | 3.016e-04 |
| equilateral | equilateral_K0.010 | 0.010 | 0.038217669 | 2.272e-05 | 5.744e-04 |
| squeezed | squeezed_q0.001_K0.015 | 0.015 | 0.058378262 | 4.173e-05 | 6.644e-04 |
| equilateral | equilateral_K0.015 | 0.015 | 0.036148784 | 5.104e-05 | 1.367e-03 |
| squeezed | squeezed_q0.001_K0.020 | 0.020 | 0.058864525 | 7.408e-05 | 1.169e-03 |
| equilateral | equilateral_K0.020 | 0.020 | 0.037002126 | 9.068e-05 | 2.369e-03 |
| squeezed | squeezed_q0.001_K0.025 | 0.025 | 0.059059524 | 1.156e-04 | 1.816e-03 |
| equilateral | equilateral_K0.025 | 0.025 | 0.034999026 | 1.415e-04 | 3.914e-03 |
| squeezed | squeezed_q0.001_K0.030 | 0.030 | 0.058891076 | 1.662e-04 | 2.619e-03 |
| equilateral | equilateral_K0.030 | 0.030 | 0.034447233 | 2.035e-04 | 5.720e-03 |
| squeezed | squeezed_q0.001_K0.035 | 0.035 | 0.058543218 | 2.259e-04 | 3.581e-03 |
| equilateral | equilateral_K0.035 | 0.035 | 0.032114343 | 2.767e-04 | 8.350e-03 |
| squeezed | squeezed_q0.001_K0.040 | 0.040 | 0.058106085 | 2.946e-04 | 4.706e-03 |
| equilateral | equilateral_K0.040 | 0.040 | 0.03090266 | 3.609e-04 | 1.132e-02 |
| squeezed | squeezed_q0.001_K0.045 | 0.045 | 0.057510969 | 3.723e-04 | 6.011e-03 |
| equilateral | equilateral_K0.045 | 0.045 | 0.02907927 | 4.562e-04 | 1.522e-02 |
| squeezed | squeezed_q0.001_K0.050 | 0.050 | 0.056847207 | 4.590e-04 | 7.499e-03 |
| equilateral | equilateral_K0.050 | 0.050 | 0.025971063 | 5.624e-04 | 2.102e-02 |
| squeezed | squeezed_q0.001_K0.055 | 0.055 | 0.055988751 | 5.546e-04 | 9.204e-03 |
| equilateral | equilateral_K0.055 | 0.055 | 0.024910355 | 6.798e-04 | 2.647e-02 |
| squeezed | squeezed_q0.001_K0.060 | 0.060 | 0.055074542 | 6.591e-04 | 1.113e-02 |
| equilateral | equilateral_K0.060 | 0.060 | 0.022303702 | 8.079e-04 | 3.512e-02 |

## Folded/G-FLAT diagnostics
| shape_id | K | G-FLAT | reason | instrument_dev | delta_dev | sign_flip |
|---|---:|---|---|---:|---:|---|
| folded_delta0.01_K0.010 | 0.010 | FLAG | flat_limit | 6.732e-01 | 1.555e-01 | False |
| folded_delta0.01_K0.015 | 0.015 | FLAG | flat_limit | 6.738e-01 | 1.567e-01 | False |
| folded_delta0.01_K0.020 | 0.020 | FLAG | flat_limit | 6.682e-01 | 1.382e-01 | False |
| folded_delta0.01_K0.025 | 0.025 | FLAG | flat_limit | 6.727e-01 | 1.718e-01 | False |
| folded_delta0.01_K0.030 | 0.030 | FLAG | flat_limit | 6.708e-01 | 1.396e-01 | False |
| folded_delta0.01_K0.035 | 0.035 | FLAG | flat_limit | 6.751e-01 | 1.325e-01 | False |
| folded_delta0.01_K0.040 | 0.040 | FLAG | flat_limit | 6.746e-01 | 1.399e-01 | False |
| folded_delta0.01_K0.045 | 0.045 | FLAG | flat_limit | 6.759e-01 | 1.423e-01 | False |
| folded_delta0.01_K0.050 | 0.050 | FLAG | flat_limit | 6.814e-01 | 1.759e-01 | False |
| folded_delta0.01_K0.055 | 0.055 | FLAG | flat_limit | 6.792e-01 | 1.460e-01 | False |
| folded_delta0.01_K0.060 | 0.060 | FLAG | flat_limit | 6.823e-01 | 1.443e-01 | False |
| folded_delta0.01_K0.072 | 0.072 | FLAG | flat_limit | 6.914e-01 | 1.797e-01 | False |
| folded_delta0.01_K0.090 | 0.090 | FLAG | flat_limit | 6.962e-01 | 1.537e-01 | False |
| folded_delta0.01_K0.119 | 0.119 | FLAG | flat_limit | 7.096e-01 | 1.752e-01 | False |

## Forbidden claims
- No all-shape closure claim.
- No folded/flattened physical conclusion from flagged rows.
- No UV-completion claim.
- No BIH-VI detection claim.
