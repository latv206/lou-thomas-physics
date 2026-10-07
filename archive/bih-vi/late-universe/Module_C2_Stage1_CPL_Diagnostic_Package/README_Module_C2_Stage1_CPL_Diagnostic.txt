
BIH-VI Module C2 Stage-1 CPL Diagnostic

Status
------
This is a diagnostic sampler, not a production cosmology likelihood.
It is designed to test whether a CPL effective dark-energy background can absorb the distance strain created by a low-z BIH clock-lapse.

Core equations
--------------
nu(z) = 1 + delta_nu / [1 + (z/z_t)^s]
w(z) = w0 + wa z/(1+z)
E_BIH^2(z) = Omega_r(1+z)^4 + Omega_m(1+z)^3 + Omega_DE,0 f_DE(z)
f_DE(z) = (1+z)^[3(1+w0+wa)] exp[-3 wa z/(1+z)]
H_obs(z) = H0_CMB nu(z) E_BIH(z)

Fixed background choices
------------------------
H0_CMB = 67.360000 +/- 0.540000 km/s/Mpc
H0_SH0ES = 73.170000 +/- 0.860000 km/s/Mpc
delta_nu center = 0.08625297
sigma_delta_nu = 0.01545421
Omega_m = 0.31580000
Omega_r = 9.21678850e-05
Omega_DE0 = 0.68410783
r_d = 147.0900 Mpc

Likelihood components
---------------------
1. DESI DR2 compressed BAO vector/covariance.
2. Conservative SN-shape proxy:
   sum[(Delta mu_i / 0.050 mag)^2] over a redshift grid 0.023 <= z <= 2.26,
   after removing absolute calibration/local-H0 offset.
   This is NOT the Pantheon+ covariance.
3. Gaussian SH0ES prior on delta_nu.
4. Hard CMB-safety gate: Omega_DE(z=1100) < 0.01.

Prior box
---------
delta_nu in [0.0, 0.14]
z_t in [0.02, 2.0]
s in [0.5, 12.0]
w0 in [-1.45, -0.55]
wa in [-3.0, 3.0]

Sampler
-------
Random prescan: 4500 points
Metropolis chains: 16
Steps per chain: 1800
Burn-in per chain: 450
Mean acceptance: 0.1234

Interpretation rules
--------------------
- A good diagnostic sample is not a discovery.
- CPL is a scaffold: it tells us the required stress shape, not the BIH microscopic explanation.
- If the best-fit CPL requires extreme w0/wa, early dark energy, negative substrate gear, or large SN residuals, then C2 needs a physical Q_bulk model rather than arbitrary CPL freedom.
- The key comparison is C1 lapse-only vs C2 lapse+CPL: does the extra background stress reduce SN/BAO strain while keeping delta_nu near the SH0ES target?

Best diagnostic sample
----------------------
chain                               1.200000e+01
step                                1.648000e+03
delta                               1.902338e-02
zt                                  8.516735e-01
s                                   1.141487e+01
w0                                 -9.974375e-01
wa                                 -4.685960e-02
chi2_bao                            7.658252e+00
chi2_snproxy                        2.411834e+00
chi2_shoes                          1.892462e+01
chi2_total                          2.899470e+01
logprob                            -1.449735e+01
max_abs_mu_hubbleflow_0p023_0p15    1.140351e-04
max_abs_mu_0p023_2p26               2.241093e-02
delta_mu_z2p26                      2.241093e-02
min_m_sub_0_3                       9.548673e-01
min_m_obs_0_3                       9.548673e-01
z_min_m_obs                         1.000000e-03
ede_frac_z1100                      5.573243e-10
nu_mean_hubbleflow                  1.019023e+00
ladder_retention_mean               1.000000e+00
H0_eff_mean_hubbleflow              6.864141e+01
