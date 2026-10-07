# BIH-VI C3.4 Density Engineering Blocker Kit

Status: engineering blocker work only. No new BIH-VI physics.

This kit addresses the current strict-preflight blockers:

1. acquire the public 2M++ density cube;
2. validate 2M++ grid metadata;
3. convert SN equatorial coordinates into the Galactic Cartesian frame used by 2M++;
4. generate C3.2 smoothing products from the native 2M++ cube where physically possible;
5. define an explicit native-smoothing floor for the 5 Mpc target;
6. define mask/edge coverage rules;
7. define peculiar-velocity control metadata.

## Critical 2M++ facts

The Cosmicflows 2M++ download page states:

- density and peculiar velocity fields are both `257^3` cubes;
- coordinate system is configuration/real space;
- smoothing is Gaussian with scale `4 Mpc/h`;
- grid is Galactic Cartesian comoving coordinates `X,Y,Z` in `Mpc/h`;
- cell centers run from `-200` to `200 Mpc/h`;
- grid spacing is `400/256 = 1.5625 Mpc/h`;
- density is luminosity-weighted contrast `delta_g*`;
- velocity field is in the CMB frame and includes the external dipole.

## Native-smoothing floor

The C3.2 target scan originally used:

```text
R_s = 5, 10, 25, 50, 100, 200, 300 Mpc
```

But with `h=0.6736`, the native 2M++ smoothing is:

```text
4 Mpc/h = 4 / h = 5.94 Mpc
```

Therefore an exact 5 Mpc smoothing product cannot be derived from the public 2M++ cube without deconvolution. The recommended C3.4 handling is:

```text
R5 target -> native-floor product, effective_R_s = 5.94 Mpc
```

and all outputs must record:

```text
target_R_s_Mpc = 5
effective_R_s_Mpc = 5.94
native_floor_used = true
```

The 5 Mpc bin remains a host/small-scale trap diagnostic, not a precision physical smoothing scale.

## Run sequence

In a networked environment:

```bash
python scripts/c34_download_twompp.py --out data/twompp
python scripts/c34_preprocess_twompp.py \
  --density data/twompp/twompp_density.npy \
  --out data/twompp_smoothed \
  --h 0.6736 \
  --targets 5 10 25 50 100 200 300 \
  --native-floor
python scripts/c34_make_grid_metadata.py \
  --density-dir data/twompp_smoothed \
  --out data/twompp_smoothed/grid_metadata.json \
  --h 0.6736
```

Then update `c34_data_manifest.json` to point `path_or_directory` at the smoothed directory and `grid_meta` at the generated metadata.

## Coordinate conversion

Use:

```text
RA/Dec/z -> comoving equatorial Cartesian -> Galactic Cartesian -> 2M++ grid coordinates
```

The coordinate module uses the standard J2000 equatorial-to-Galactic rotation matrix.

## Strict gate

After filling the manifest:

```bash
python scripts/c34_preflight_audit_strict.py \
  --manifest c34_data_manifest.json \
  --out c34_preflight_strict \
  --allow-missing-optional-nuisance
```

No C3.3 join is authorized until strict preflight returns `ready_for_c33_join=true`.
