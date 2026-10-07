
Data required for production mode
=================================

The public data products are intentionally not vendored here except for the small embedded DESI DR2
diagnostic vector/covariance already used in the C3 smoke test.

Required Pantheon+ files:
  data/Pantheon+SH0ES.dat
  data/Pantheon+SH0ES_STAT+SYS.cov

Expected public source:
  PantheonPlusSH0ES/DataRelease
  Pantheon+_Data/4_DISTANCES_AND_COVAR/

DESI DR2:
  CobayaSampler/bao_data
  desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_mean.txt
  desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_cov.txt

In this package:
  desi_dr2_embedded_mean.csv
  desi_dr2_embedded_cov.txt

These embedded DESI files reproduce the compressed vector used for the earlier Module C/C3 diagnostics.
