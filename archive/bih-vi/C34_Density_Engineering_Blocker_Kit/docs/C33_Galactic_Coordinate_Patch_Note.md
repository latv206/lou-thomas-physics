# C3.3 joiner patch note: Galactic 2M++ support

The prior `c33_join_pantheon_density.py` emitted equatorial Cartesian coordinates. For 2M++,
the density grid is Galactic Cartesian in Mpc/h, so the joiner must either:

1. import `c34_coordinate_transforms.radec_chi_to_galactic_xyz`, or
2. include the same J2000 equatorial-to-Galactic rotation matrix internally.

Required coordinate mode:

```text
RA/Dec/z -> chi(z) [Mpc] -> equatorial Cartesian [Mpc] -> Galactic Cartesian [Mpc] -> multiply by h -> Mpc/h grid
```

Grid metadata should use:

```json
{
  "coordinate_frame": "Galactic Cartesian comoving",
  "units": "Mpc_h",
  "field_type": "delta",
  "box_min": [-200,-200,-200],
  "box_max": [200,200,200],
  "grid_shape": [257,257,257],
  "periodic": false
}
```

Strict preflight must reject any manifest that still says "candidate" or "not final" for this.
