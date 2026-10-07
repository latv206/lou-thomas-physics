BIH-VI Module C distance-gate scan

Purpose
-------
First compressed observational stress test of a low-redshift BIH clock-lapse template:
    nu(z) = 1 + delta_nu / [1 + (z/z_t)^s]
    H_obs(z) = nu(z) H_LCDM,CMB(z)

This is not a final likelihood analysis. It is a fixed-background diagnostic to see whether an 8.625% local clock lift can coexist with compressed DESI DR2 BAO geometry and SN Hubble-diagram shape.

Baseline choices
----------------
H0_CMB = 67.360000 km/s/Mpc
H0_local = 73.170000 km/s/Mpc
delta_nu = 0.08625297
Omega_m = 0.31580000
Omega_r = 9.21678850e-05
Omega_L = 0.68410783
r_d = 147.0900 Mpc

Data vector
-----------
DESI DR2 compressed BAO consensus vector:
CobayaSampler/bao_data, desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_mean.txt
Covariance:
CobayaSampler/bao_data, desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_cov.txt

Metrics
-------
delta_chi2_bao_vs_planck_lcdm:
    chi2(model) - chi2(Planck-like LCDM control), using fixed r_d and the public compressed covariance.

max_abs_delta_mu_0p023_0p15_mag:
    Hubble-flow SN shape residual after removing the z -> 0 local H0 offset.

max_abs_delta_mu_0p023_2p3_mag:
    Full low-to-high-z SN shape residual after removing the z -> 0 local H0 offset.

ladder_retention_mean:
    mean nu(z) over 0.023 <= z <= 0.15 divided by nu(0). Values much below unity mean the template no longer actually lifts the SH0ES Hubble-flow range.

min_m_0_3:
    minimum reconstructed late clock gear m(z) over 0.001 <= z <= 3.
    Negative values indicate phantom-like clock behavior in this simple single-lapse mapping.

Important interpretation
------------------------
This scan is designed to find failure surfaces, not to claim a fit.
A full Module C likelihood must include nuisance-marginalized Pantheon+/SH0ES or DESY5 SN data, full BAO covariance handling, CMB acoustic-scale constraints, growth, and possible r_d or calibration-sector shifts.
