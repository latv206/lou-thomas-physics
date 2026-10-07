"""Phase 1 runner.

A. Validation: Gaussian pipeline vs ED (energies + all contiguous-interval
   entropies) at h=1.0 and h=1.5, N=10.
B. Calabrese-Cardy: edge-interval entropies at criticality, N=200, extract c.
C. First law (ED, N=12, interval [4..7], h=1 -> h+delta):
   exact identity (dK - dS = S_rel), O(delta^2) scaling, Kubo-Mori metric,
   cross-check of dK against the Gaussian entanglement Hamiltonian.
D. Entanglement-Hamiltonian structure at criticality (N=400, centered l=10):
   nearest-neighbor Majorana couplings vs CHM parabolic envelope.
"""

import json
from pathlib import Path
import sys

# Execute only the disposable copy made by the supported wrapper.
if __name__ != "__main__":
    raise RuntimeError("Use tools/reproduce_rnsf.py; this runner is not an importable library")
if "_generated" not in Path(__file__).resolve().parts:
    sys.exit("Use: python tools/reproduce_rnsf.py")
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import gaussian_tfim as gf
import ed_tfim as ed

results = {}

# ----------------------------------------------------------------------
# A. VALIDATION  (ED vs Gaussian, N=10)
# ----------------------------------------------------------------------
print("=" * 72)
print("A. VALIDATION: ED vs Gaussian, N=10, OBC")
print("=" * 72)
N = 10
val = {}
for h in (1.0, 1.5):
    T = gf.tfim_majorana_T(N, 1.0, h)
    G, E_ff = gf.ground_state_gamma(T)
    E_ed, psi = ed.ground_state(N, 1.0, h)
    dE = abs(E_ff - E_ed)

    max_dS = 0.0
    for a in range(N):
        for b in range(a, N - 1 if a == 0 else N):  # skip full chain only when a=0,b=N-1
            if a == 0 and b == N - 1:
                continue
            S_ed = ed.entropy(ed.rdm_interval(psi, N, a, b))
            S_ff = gf.entropy_from_gamma(gf.restrict_gamma(G, range(a, b + 1)))
            max_dS = max(max_dS, abs(S_ed - S_ff))
    val[h] = {"dE": dE, "max_dS": max_dS, "E": E_ed}
    print(f"  h={h:4.2f}:  |E_ff - E_ed| = {dE:.3e}   "
          f"max over all contiguous intervals |S_ff - S_ed| = {max_dS:.3e}")
results["validation_N10"] = val

# ----------------------------------------------------------------------
# B. CALABRESE-CARDY  (N=200, edge intervals, h=J=1)
# ----------------------------------------------------------------------
print()
print("=" * 72)
print("B. CALABRESE-CARDY FIT: N=200, h=J=1, edge intervals [0..l-1]")
print("=" * 72)
N = 200
T = gf.tfim_majorana_T(N, 1.0, 1.0)
G, _ = gf.ground_state_gamma(T)
ells = np.arange(2, N - 1)
S_l = np.array([gf.entropy_from_gamma(gf.restrict_gamma(G, range(l)))
                for l in ells])

# OBC edge interval: S = (c/6) ln[(2L/pi) sin(pi l / L)] + b ; fit even l only
mask = (ells % 2 == 0) & (ells >= 20) & (ells <= N - 20)
x = np.log((2.0 * N / np.pi) * np.sin(np.pi * ells[mask] / N))
A = np.vstack([x, np.ones_like(x)]).T
coef, res, *_ = np.linalg.lstsq(A, S_l[mask], rcond=None)
c_fit = 6.0 * coef[0]
resid = S_l[mask] - A @ coef
print(f"  c_fit = {c_fit:.5f}   (Ising CFT: c = 0.5)")
print(f"  rel. error = {abs(c_fit - 0.5) / 0.5 * 100:.3f} %   "
      f"rms fit residual = {np.sqrt(np.mean(resid**2)):.2e} nats")
results["calabrese_cardy"] = {"c_fit": float(c_fit),
                              "rms_resid": float(np.sqrt(np.mean(resid**2)))}

plt.figure(figsize=(6.4, 4.2))
plt.plot(ells[ells % 2 == 0], S_l[ells % 2 == 0], ".", ms=4,
         color="#356", label="Gaussian data (even $\\ell$)")
xx = np.linspace(2, N - 2, 400)
plt.plot(xx, coef[0] * np.log((2 * N / np.pi) * np.sin(np.pi * xx / N)) + coef[1],
         "-", color="#c33",
         label=f"CC fit:  $c = {c_fit:.4f}$")
plt.xlabel("interval length $\\ell$")
plt.ylabel("$S(\\ell)$  [nats]")
plt.title("Critical TFIM, $N=200$ OBC, edge intervals")
plt.legend()
plt.tight_layout()
plt.savefig("fig_cc_fit.png", dpi=150)
plt.close()

# ----------------------------------------------------------------------
# C. FIRST LAW  (ED, N=12, A=[4..7], h=1 -> 1+delta)
# ----------------------------------------------------------------------
print()
print("=" * 72)
print("C. FIRST LAW: ED N=12, A = sites 4..7, h = 1 -> 1+delta")
print("=" * 72)
N, a, b, h0 = 12, 4, 7, 1.0
_, psi0 = ed.ground_state(N, 1.0, h0)
rho0 = ed.rdm_interval(psi0, N, a, b)
S0 = ed.entropy(rho0)
K0, pmin = ed.modular_K(rho0)
print(f"  S(A) = {S0:.10f} nats   min eigenvalue of rho_A = {pmin:.3e}")

# Gaussian-side entanglement Hamiltonian for the same interval (cross-check)
Tm = gf.tfim_majorana_T(N, 1.0, h0)
G0, _ = gf.ground_state_gamma(Tm)
GA0 = gf.restrict_gamma(G0, range(a, b + 1))
W0, _ = gf.entanglement_hamiltonian_W(GA0)

deltas = np.logspace(-4, -1, 7)
rows = []
for d in deltas:
    _, psi1 = ed.ground_state(N, 1.0, h0 + d)
    rho1 = ed.rdm_interval(psi1, N, a, b)
    dS = ed.entropy(rho1) - S0
    dK = float(np.real(np.trace((rho1 - rho0) @ K0)))
    srel = ed.rel_entropy(rho1, rho0)
    ident = abs((dK - dS) - srel)          # exact algebraic identity
    # Gaussian cross-check of dK
    T1 = gf.tfim_majorana_T(N, 1.0, h0 + d)
    G1, _ = gf.ground_state_gamma(T1)
    GA1 = gf.restrict_gamma(G1, range(a, b + 1))
    dK_gauss = gf.expect_quadratic(W0, GA1) - gf.expect_quadratic(W0, GA0)
    rows.append((d, dS, dK, srel, ident, abs(dK - dK_gauss)))
    print(f"  d={d:9.3e}  dS={dS:+.6e}  d<K>={dK:+.6e}  "
          f"S_rel={srel:.6e}  |identity|={ident:.1e}  |dK_ED-dK_Gauss|={abs(dK-dK_gauss):.1e}")

rows = np.array(rows)
# scaling of S_rel = d<K> - dS  ~  delta^2
lo = np.log(rows[:, 0]); ls = np.log(rows[:, 3])
slope = np.polyfit(lo, ls, 1)[0]
g_km = 2.0 * rows[:, 3] / rows[:, 0] ** 2
print(f"\n  log-log slope of S_rel vs delta = {slope:.4f}   (first law => 2)")
print(f"  Kubo-Mori metric g_KM(delta->0): "
      + ", ".join(f"{g:.6f}" for g in g_km[:3])
      + f"  -> g_KM ~ {g_km[0]:.5f}")
results["first_law"] = {
    "slope": float(slope),
    "max_identity_residual": float(rows[:, 4].max()),
    "max_dK_ED_vs_Gaussian": float(rows[:, 5].max()),
    "g_KM": float(g_km[0]),
    "S_A": float(S0),
}

plt.figure(figsize=(6.4, 4.2))
plt.loglog(rows[:, 0], rows[:, 3], "o-", color="#356",
           label=r"$\delta\langle K_A\rangle-\delta S_A\;(=S_{\rm rel})$")
plt.loglog(rows[:, 0], g_km[0] / 2 * rows[:, 0] ** 2, "--", color="#c33",
           label=r"slope-2 guide  $\frac{1}{2}g_{\rm KM}\,\delta^2$")
plt.xlabel(r"$\delta h$")
plt.ylabel("nats")
plt.title("First law: TFIM $N=12$, $A=[4..7]$, $h=1$")
plt.legend()
plt.tight_layout()
plt.savefig("fig_first_law.png", dpi=150)
plt.close()

# ----------------------------------------------------------------------
# D. ENTANGLEMENT-HAMILTONIAN PROFILE  (N=400, centered l=10, h=J=1)
# ----------------------------------------------------------------------
print()
print("=" * 72)
print("D. ENTANGLEMENT HAMILTONIAN: N=400, centered interval l=10, h=J=1")
print("=" * 72)
N, l = 400, 10
a0 = (N - l) // 2
T = gf.tfim_majorana_T(N, 1.0, 1.0)
G, _ = gf.ground_state_gamma(T)
GA = gf.restrict_gamma(G, range(a0, a0 + l))
W, _ = gf.entanglement_hamiltonian_W(GA, clip=1.0 - 1e-13)
s_chk = np.linalg.eigvalsh(1j * GA)
print(f"  purity headroom: max lambda = {s_chk.max():.15f} (resolvable; clip at 1-1e-13)")

nn = np.abs(np.diag(W, k=1))            # all 2l-1 nearest-neighbor Majorana couplings
m = np.arange(1, 2 * l)                  # Majorana bond coordinate (1..2l-1)
# CHM parabola in bond coordinate: beta(x) ~ x (2l - x)
interior = (m >= 3) & (m <= 2 * l - 3)
X = (m * (2 * l - m)).astype(float)
alpha = np.sum(X[interior] * nn[interior]) / np.sum(X[interior] ** 2)
fit = alpha * X
ss_res = np.sum((nn[interior] - fit[interior]) ** 2)
ss_tot = np.sum((nn[interior] - nn[interior].mean()) ** 2)
r2 = 1.0 - ss_res / ss_tot

# locality: how dominant are NN couplings over all longer-range ones
off_all = sum(np.sum(np.abs(np.diag(W, k=k))) for k in range(1, 2 * l))
nn_share = np.sum(nn) / off_all
print(f"  parabola fit (interior bonds):  R^2 = {r2:.5f}")
print(f"  NN share of total off-diagonal weight: {nn_share * 100:.2f} %")
results["eh_profile"] = {"R2_parabola": float(r2), "nn_share": float(nn_share)}

plt.figure(figsize=(6.4, 4.2))
plt.plot(m, nn, ".", ms=4, color="#356", label="|NN Majorana couplings| of $W$")
plt.plot(m, fit, "-", color="#c33",
         label=r"CHM parabola $\propto x(2\ell-x)$,  $R^2$=" + f"{r2:.4f}")
plt.xlabel("Majorana bond coordinate $x$")
plt.ylabel("coupling magnitude")
plt.title("Entanglement Hamiltonian, critical TFIM, $\\ell=10$ in $N=400$")
plt.legend()
plt.tight_layout()
plt.savefig("fig_eh_profile.png", dpi=150)
plt.close()

with open("phase1_numbers.json", "w") as f:
    json.dump(results, f, indent=2)
print("\nDone. Numbers in phase1_numbers.json; figures written.")
