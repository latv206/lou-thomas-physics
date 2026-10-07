# Suggested Supplemental Repository Layout

```text
BIH-VI/
  README.md
  LICENSE
  CITATION.cff

  paper/
    BIH-VI_main.tex
    BIH-VI_references.bib
    BIH-VI_main.pdf

  theory/
    equations.md
    scope_boundary.md
    frozen_branch_parameters.yaml

  likelihoods/
    cobaya/
      cobaya_bih_vi_c3.yaml
      bih_vi_c3_cobaya_likelihood.py
    python/
      bih_vi_c3_likelihood.py
      run_c3_mcmc.py
      reconstruct_qbulk.py
      prepare_public_data.py

  data/
    README_DATA_REQUIREMENTS.md
    desi_dr2_embedded_mean.csv
    desi_dr2_embedded_cov.txt

  notebooks/
    C1_metric_lapse_failure.ipynb
    C2_lapse_CPL_diagnostic.ipynb
    C3_calibration_frame_likelihood.ipynb
    Qbulk_reconstruction.ipynb

  results/
    diagnostic_C1/
    diagnostic_C2/
    diagnostic_C3/
    production_chains/
    qbulk_reconstruction/

  figures/
    early_branch/
    exit_feature/
    late_distance_gate/
    calibration_frame/
    qbulk/

  archive/
    rejected_branches/
```
