
# BIH-VI Module C3 Likelihood Synthesis Package

## Status

This package implements the next step after the C1/C2 metric-lapse failure:

- `nu_metric(z) = 1` for BAO/SN/CMB distance integrals.
- `Delta_M_B` is a calibration-frame parameter.
- DESI DR2 BAO, Pantheon+ full covariance, Planck theta_* prior, and local calibration prior are wired into a single likelihood.
- `Q_bulk(z)` is reconstructed from posterior samples as a falsifiability diagnostic.

## Important limitation of this generated run

The generation sandbox could not download raw GitHub data files at runtime, and the uploaded BIH-VI package does not contain the full Pantheon+ covariance. Therefore this package contains:

1. A production-ready likelihood scaffold.
2. A Cobaya-ready custom likelihood wrapper.
3. Public-data download instructions/scripts for your local machine or cluster.
4. The previous C3 smoke-test outputs copied into `results_smoke_test/`.

It does **not** claim that a full Pantheon+ production MCMC was completed inside this sandbox.

## Production run

From this package root:

```bash
python scripts/prepare_public_data.py
python scripts/run_c3_mcmc.py --data-dir data --out-dir chains --steps 200000 --pantheon
python scripts/reconstruct_qbulk.py --chain chains/bih_vi_c3_chain.csv --out-dir qbulk_results
```

Or with Cobaya:

```bash
cobaya-run cobaya_bih_vi_c3.yaml
```

## Parameter vector

```text
h, Omega_m, Omega_k, omega_b h^2, w0, wa, M_B_geom, Delta_M_B
```

## Core equations

```text
H_geom(z) = H0_geom E_BIH(z)
nu_metric(z) = 1
H0_ladder = nu_cal H0_geom
Delta_M_B = 5 log10(nu_cal)
```

CPL scaffold:

```text
w_eff(z) = w0 + wa z/(1+z)
E_BIH^2 = Omega_r(1+z)^4 + Omega_m(1+z)^3 + Omega_k(1+z)^2 + Omega_DE f_DE(z)
f_DE = (1+z)^[3(1+w0+wa)] exp[-3 wa z/(1+z)]
```

Bulk exchange reconstruction:

```text
dot rho_DE + 3H(1+w_int)rho_DE = Q_bulk
Q_bulk/(H rho_DE) = 3(w_int - w_eff)
```

For `w_int=-1`:

```text
Q_bulk/(H rho_DE) = -3[1+w_eff(z)]
```

## Q_bulk smoothness gate

Default smoke-test metrics:

- `q_abs_max`
- `dq_abs_max`
- `d2q_rms`
- `sign_changes`
- boolean `smooth_pass_default`

A CPL model is smooth by construction, so the real production extension should eventually replace CPL
with binned or Gaussian-process `w(z)` and use the smoothness gate as a real falsifier.

## Calibration target

```text
H0_geom = 67.36 km/s/Mpc
H0_ladder = 73.17 km/s/Mpc
nu_cal = 1.08625
Delta_M_B = 0.179655 mag
```
