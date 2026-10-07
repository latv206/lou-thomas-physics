# BIH-VI C3 Late-Universe Closure Note

**Status:** manuscript-ready closure language for the late-universe C3 audit.  
**Scope:** calibration-sector diagnostics only. No modification to the frozen Sqrt-Reg/EFT-clock early-universe branch.

---

## C3 Late-Universe Audit Result

The BIH-VI late-universe extension was tested through a sequence of increasingly restrictive empirical gates. The purpose was not to tune the frozen early-universe branch, but to determine whether a late-time calibration-frame mechanism could survive real distance-ladder and density-field constraints.

The outcome is restrictive:

\[
\boxed{\text{Metric-lapse branch: rejected by distance-gate logic.}}
\]

\[
\boxed{\text{2M++ density-coupled branch: survey-dependent and not robust.}}
\]

\[
\boxed{\text{Pure frame-offset branch: method-dependent rather than universal.}}
\]

Therefore, the late-universe C3 branch should be framed as a **calibration-sector diagnostic program**, not as a confirmed resolution of the Hubble tension.

---

## C3.4 / C3.3 Data-Gate Summary

The strict C3.4 preflight passed before any join or regression was interpreted:

\[
\texttt{ready\_for\_c33\_join=true},
\]

with zero blockers and zero warnings. The C3.3 join then reduced the Pantheon+ sample from 1701 rows to 730 density-covered regression rows. The aligned covariance matrix was correctly sliced to \(730\times730\), matching the regression table row order.

These engineering gates matter because they establish that the negative/partial result is not a bookkeeping artifact.

---

## Density-Coupled Branch Closure

The 2M++/Pantheon+ diagnostic initially produced a statistically interesting residual-density feature near:

\[
R_s=100\,\mathrm{Mpc},\qquad z>0.03.
\]

However, follow-up audits showed that the signal was not survey-independent. It was carried primarily by survey 150 and did not persist in the non-150 subset. Consequently:

\[
\boxed{\text{The 2M++ density-coupled C3 branch is not supported as a robust cosmological signal.}}
\]

This result does not falsify the frozen BIH-VI early-universe branch. It only closes the specific 2M++ local-density calibration interpretation.

**Manuscript language:**

> The 2M++/Pantheon+ diagnostic sequence found a statistically interesting \(R_s=100\) Mpc, \(z>0.03\) residual-density slope, but follow-up survey-dependence tests showed that the effect was carried primarily by survey 150 and did not persist in the non-150 subset. We therefore do not interpret the 2M++ result as evidence for a robust density-coupled calibration-frame effect.

---

## Pure Frame-Offset Branch Audit

After the density-coupled branch failed as a robust 2M++ signal, the audit shifted to the pure frame-offset branch:

\[
\Delta M_{B,0} = 5\log_{10}\left(\frac{H_0^{\rm anchor}}{H_0^{\rm geom}}\right).
\]

Run07 found:

\[
\Delta M_{B,0}^{\rm SH0ES-like}
=
0.1745\pm0.0349\,\mathrm{mag},
\]

\[
\Delta M_{B,0}^{\rm non\text{-}SH0ES}
=
0.0929\pm0.0330\,\mathrm{mag},
\qquad n=5,
\]

\[
\Delta M_{B,0}^{\rm all}
=
0.1315\pm0.0240\,\mathrm{mag},
\qquad n=6.
\]

The SH0ES-like and non-SH0ES anchor families differ at approximately:

\[
1.70\sigma.
\]

Thus the allowed conclusion is:

\[
\boxed{\text{The frame-offset burden is method-dependent, not a clean universal offset.}}
\]

Run07 classification:

```text
method_dependent_frame_offset
```

Allowed claim:

> The frame-offset burden appears method-dependent: SH0ES-like Cepheid/SN anchors require a large offset, while other anchors prefer a smaller one.

---

## Final C3 Posture

The late-universe C3 program now has the following status:

| Branch | Status | Allowed Interpretation |
|---|---|---|
| Universal metric lapse | Rejected | Would distort distance integrals; not viable as the main C3 route. |
| 2M++ density coupling | Closed for this dataset | Survey-dependent; not a robust cosmological density signal. |
| Pure frame offset | Still live but narrowed | Offset burden is method-dependent across anchor families. |
| Independent density replication | Future-only | Requires BORG/Cosmicflows/alternate density map before density branch can be revived. |

The strongest safe statement is:

\[
\boxed{\text{C3 is a calibration-sector audit framework, not a confirmed Hubble-tension solution.}}
\]

---

## Manuscript-Ready Paragraph

> The C3 late-universe audit tested whether the BIH-VI calibration-frame interpretation could account for low-redshift distance-ladder structure without modifying the frozen Sqrt-Reg/EFT-clock inflationary branch. A universal metric-lapse interpretation was rejected at the distance-gate level because it would distort supernova and BAO distance integrals. A density-coupled calibration branch was then tested using Pantheon+ supernovae joined to the 2M++ reconstructed density field. Although an \(R_s=100\) Mpc, \(z>0.03\) feature appeared in intermediate diagnostics, follow-up survey-dependence tests showed that the effect was carried primarily by survey 150 and did not persist in the non-150 subset. We therefore do not interpret the 2M++ result as evidence for a robust density-coupled calibration-frame effect. A pure frame-offset audit found that the required offset is method-dependent: SH0ES-like Cepheid/SN anchors require \(\Delta M_{B,0}\simeq0.17\) mag, while non-SH0ES anchors prefer \(\Delta M_{B,0}\simeq0.09\) mag. Consequently, the late-universe branch remains a calibration-sector diagnostic rather than a confirmed solution of the Hubble tension.

---

## Claims Explicitly Not Made

The manuscript should not claim:

- BIH-VI solves the Hubble tension.
- The 2M++ density-coupled branch is detected.
- The pure frame offset is universal.
- The Run07 anchor audit is a production likelihood.
- The late-universe C3 results validate or invalidate the frozen early-universe Sqrt-Reg/EFT-clock branch.

---

## Next Authorized Empirical Paths

1. **Independent density-map replication:** BORG, Cosmicflows alternatives, or another 3D reconstructed field.
2. **Production anchor likelihood:** explicit covariance and method-systematics modeling across Cepheids, TRGB, JAGB, SBF, masers, standard sirens, and strong lenses.
3. **Manuscript closure:** present C3 as an honest falsifiability audit, not as a solved-tension claim.

---

## Frozen Early-Branch Boundary

The frozen BIH-VI core remains:

\[
\boxed{\text{Stable Sqrt-Reg/EFT-clock branch: CMB-smooth, exit-feature rich, and UHF-relic quiet.}}
\]

The late-universe C3 audit constrains proposed calibration mechanisms. It does not reopen or retune the early-universe branch.
