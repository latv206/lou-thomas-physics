
BIH-VI Module C3 Calibration-Frame Geometry + Substrate-Stress Diagnostic

Status
------
This package implements the post-C2 pivot:
    - Do NOT insert the SH0ES-size clock-lapse into all distance integrals.
    - Set the metric-distance lapse to unity for BAO/SN geometry.
    - Treat the H0 discrepancy as a calibration/readout-sector offset.
    - Let the geometry sector test CPL-like effective substrate stress, then reconstruct Q_bulk.

Core split
----------
Geometry frame:
    H_geom(z) = H0_geom E_BIH(z)

Calibration/readout frame:
    H0_ladder = nu_cal H0_geom
    nu_cal = 1.08625297
    delta_cal = 0.08625297

Equivalent SN absolute-magnitude target:
    Delta M_B = 5 log10(H0_ladder/H0_geom)
              = 0.179655 +/- 0.030894 mag

CPL geometry scaffold
---------------------
    w(z) = w0 + wa z/(1+z)
    f_DE(z) = (1+z)^[3(1+w0+wa)] exp[-3 wa z/(1+z)]
    E_BIH^2(z) = Omega_r(1+z)^4 + Omega_m(1+z)^3 + Omega_DE,0 f_DE(z)

Distances use H_geom(z), not nu_cal H_geom(z):
    D_C(z) = c int_0^z dz'/H_geom(z')

Substrate-exchange reconstruction
---------------------------------
Assume an intrinsic dark sector with w_int = -1 and source exchange:
    dot rho_DE + 3H(1+w_int)rho_DE = Q_bulk

The CPL w(z) is interpreted as an effective equation of state:
    Q_bulk/(H rho_DE) = 3(w_int - w_eff)
                      = -3[1+w_eff(z)]  for w_int=-1

Fixed diagnostic choices
------------------------
H0_geom = 67.360000 +/- 0.540000 km/s/Mpc
H0_ladder = 73.170000 +/- 0.860000 km/s/Mpc
Omega_m = 0.31580000
Omega_r = 9.21678850e-05
Omega_DE0 = 0.68410783
r_d = 147.0900 Mpc
SN-shape proxy sigma = 0.050 mag with one constant offset marginalized
CMB-safety gate: Omega_DE(z=1100) < 0.01

Important limits
----------------
This is not a production Pantheon+/DESI/CMB likelihood.
It is a compressed diagnostic designed to formalize the surviving architecture after the metric-lapse branch failed.
A production run must use full SN covariance, BAO covariance from an official likelihood wrapper, CMB compressed/full priors, growth data, and nuisance marginalization.

Best compressed geometry sample
-------------------------------
                                              model     w0        wa  chi2_bao  chi2_snproxy  chi2_total_geometry  delta_chi2_total_vs_lcdm  ede_frac_z1100  min_m_sub_0_3  max_abs_mu_shape_0p023_2p26_mag   w_z0      w_z1   w_z2p26  qbulk_over_Hrho_z0_wint_minus1  qbulk_over_Hrho_z1_wint_minus1  qbulk_over_Hrho_z2p26_wint_minus1  H0_geom  H0_ladder_target  nu_cal_target  delta_cal_target  delta_M_B_target_mag
                  Planck-like LCDM geometry control -1.000  0.000000 29.048841      0.000000            29.048841                  0.000000    1.228396e-09       0.949714                         0.000000 -1.000 -1.000000 -1.000000                           0.000                        0.000000                           0.000000    67.36             73.17       1.086253          0.086253              0.179655
                 C3 best compressed geometry sample -0.850 -0.472222  8.664906      1.783109            10.448015                -18.600826    5.802774e-12       1.256056                         0.019494 -0.850 -1.086111 -1.177369                          -0.450                        0.258333                           0.532106    67.36             73.17       1.086253          0.086253              0.179655
Best nonphantom geometry sample under SN-shape gate -0.922 -0.111111 11.510498      1.424080            12.934578                -16.114264    8.547139e-10       1.109276                         0.019128 -0.922 -0.977556 -0.999028                          -0.234                       -0.067333                          -0.002916    67.36             73.17       1.086253          0.086253              0.179655
