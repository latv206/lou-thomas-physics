# C3.4 Peculiar-Velocity Control Plan

The 2M++ field is entangled with peculiar-velocity correction. C3.2 must not mistake a PV residual for a calibration-density signal.

Minimum production strategy:

## Required manifest fields

```json
"nuisance_controls": {
  "host_mass": "HOST_LOGMASS",
  "survey_id": "IDSURVEY",
  "peculiar_velocity": "VPEC,VPECERR plus robustness cuts z>0.01,z>0.02,z>0.03; optional 2M++ velocity field control if downloaded"
}
```

## Required C3.2 runs

1. Baseline all retained SNe with covariance.
2. Cut z < 0.01.
3. Cut z < 0.02.
4. Cut z < 0.03.
5. Include VPEC and/or VPECERR as nuisance/control if using residuals not already PV-corrected.
6. If `twompp_velocity.npy` is available, interpolate model velocity at each SN position and include the line-of-sight component as a control.

## Decision

A density-coupled C3 branch is not credible unless the large-scale \(R_s\) signal survives these PV robustness checks.
