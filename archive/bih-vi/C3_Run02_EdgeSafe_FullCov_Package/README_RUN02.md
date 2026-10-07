# BIH-VI C3 Real Run 02 — Edge-Safe Full-Cov Regression

This package contains the next empirical run after the first C3.2 diagnostic.

It does not modify theory. It does not touch G:. It does not overwrite Run 01.

## Files

- `scripts/c3_run02_edge_safe_fullcov.py`
- `scripts/run_c3_real_run02_edge_safe_fullcov.ps1`

## Install

Copy both scripts into:

```text
[local path omitted]
```

## Run

```powershell
powershell -ExecutionPolicy Bypass -File "[local path omitted]"
```

## Outputs

```text
c32_run02_edge_safe_fullcov/
  c32_run02_input_audit.json
  c32_run02_regression_table_with_edge.csv
  c32_run02_edge_distance_summary.csv
  c32_run02_density_conditioning.csv
  c32_run02_edge_safe_by_scale_summary.csv
  c32_run02_common_subset_summary.csv
  c32_run02_coefficients_all_models.csv
  c32_run02_covariance_slicing_report.csv
  c32_run02_covariance_slicing_report.json
  c32_run02_zcut_fullcov_verdicts.json
  c32_run02_effect_size_summary.csv
  c32_run02_survey_fixed_effects_summary.csv
  c32_run02_permutation_null_summary.csv
  c32_run02_final_verdict.json
  C3_REAL_RUN_02_SUMMARY.md
```

## Interpretation

Run 02 is a robustness test only.

Do not claim detection unless a 50–200 Mpc scale survives:

- full covariance,
- z-cuts,
- survey fixed effects,
- edge controls,
- permutation nulls.

If the run remains null, the 2M++ density-coupled branch weakens and C3 shifts toward pure frame offset or another density field such as BORG.
