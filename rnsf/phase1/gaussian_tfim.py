"""Gaussian (Majorana covariance) pipeline for the open-boundary TFIM.

H = -J sum_j sx_j sx_{j+1} - h sum_j sz_j,  OBC.

Jordan-Wigner (string from site 0), Majoranas per site j (0-based):
    a_{2j}   = c_j + c^dag_j        ("x-type")
    a_{2j+1} = -i (c_j - c^dag_j)   ("y-type")
Exact identities (no dropped constants):
    -h sz_j        = + i h a_{2j}   a_{2j+1}
    -J sx_j sx_{j+1} = + i J a_{2j+1} a_{2j+2}
so H = (i/4) a^T T a with T real antisymmetric:
    T[2j, 2j+1]   = 2h,   T[2j+1, 2j]   = -2h
    T[2j+1, 2j+2] = 2J,   T[2j+2, 2j+1] = -2J

Covariance convention: Gamma_mn = i<a_m a_n> - i delta_mn  (real antisymmetric).
Per Schur mode with energy t_k > 0 the ground state has block [[0,-1],[1,0]],
and E_GS = -(1/2) sum_k t_k.

Entanglement Hamiltonian of region A: rho_A = exp(-(i/4) a^T W a)/Z with
W = f(Gamma_A) under Hermitian functional calculus on i*Gamma_A,
f(s) = -2 artanh(s); single-mode relation Gamma_12 = -tanh(W_12/2).
Z gives the additive constant: -ln rho_A = (i/4) a^T W a + sum_k ln(2 cosh(w_k/2)).
"""

import numpy as np
from scipy.linalg import schur, eigh


def tfim_majorana_T(N, J=1.0, h=1.0):
    T = np.zeros((2 * N, 2 * N))
    for j in range(N):
        m, n = 2 * j, 2 * j + 1
        T[m, n] += 2.0 * h
        T[n, m] -= 2.0 * h
    for j in range(N - 1):
        m, n = 2 * j + 1, 2 * j + 2
        T[m, n] += 2.0 * J
        T[n, m] -= 2.0 * J
    return T


def _real_schur_blocks(T):
    """Real Schur of antisymmetric T -> (Q, ts) with T = Q S Q^T,
    S block-diagonal, blocks [[0, t_k], [-t_k, 0]], t_k > 0 at rows (2k, 2k+1)."""
    S, Q = schur(T, output="real")
    n2 = T.shape[0]
    ts = []
    k = 0
    while k < n2:
        if k + 1 < n2 and abs(S[k, k + 1]) > 1e-12:
            t = S[k, k + 1]
            if t < 0:  # flip orientation: swap the two Schur vectors
                Q[:, [k, k + 1]] = Q[:, [k + 1, k]]
                t = -t
            ts.append(t)
            k += 2
        else:
            raise RuntimeError("Zero mode / 1x1 Schur block encountered; "
                               "parameters too close to a degeneracy.")
    return Q, np.array(ts)


def ground_state_gamma(T):
    """Ground-state Majorana covariance Gamma and exact E_GS."""
    Q, ts = _real_schur_blocks(T)
    n = T.shape[0] // 2
    Gb = np.zeros_like(T)
    for k in range(n):
        Gb[2 * k, 2 * k + 1] = -1.0
        Gb[2 * k + 1, 2 * k] = +1.0
    G = Q @ Gb @ Q.T
    G = 0.5 * (G - G.T)
    E_gs = -0.5 * np.sum(ts)
    return G, E_gs


def restrict_gamma(G, sites):
    """Restrict covariance to a set of (0-based) site indices."""
    idx = []
    for s in sorted(sites):
        idx += [2 * s, 2 * s + 1]
    idx = np.array(idx)
    return G[np.ix_(idx, idx)]


def _binary_entropy(p):
    p = np.clip(p, 1e-300, 1.0)
    q = np.clip(1.0 - p, 1e-300, 1.0)
    return -(p * np.log(p) + q * np.log(q))


def entropy_from_gamma(GA):
    """Von Neumann entropy (nats) of the Gaussian state with covariance GA."""
    s = np.linalg.eigvalsh(1j * GA).real  # spectrum is +/- lambda pairs
    s = np.clip(s, -1.0, 1.0)
    return 0.5 * np.sum(_binary_entropy((1.0 + s) / 2.0))


def entanglement_hamiltonian_W(GA, clip=1.0 - 1e-12):
    """Quadratic kernel W of -ln rho_A = (i/4) a^T W a + const, plus const ln Z.

    Returns (W, lnZ): W real antisymmetric; lnZ = sum_k ln(2 cosh(w_k/2)),
    summed over independent mode pairs.
    """
    s, V = eigh(1j * GA)
    s = np.clip(s.real, -clip, clip)
    w = -2.0 * np.arctanh(s)
    iW = (V * w) @ V.conj().T
    W = np.real(-1j * iW)
    W = 0.5 * (W - W.T)
    wpos = np.abs(w)[w > 0]  # one |w| per mode pair
    lnZ = np.sum(np.log(2.0 * np.cosh(wpos / 2.0)))
    return W, lnZ


def expect_quadratic(W, GA):
    """<(i/4) a^T W a> on the Gaussian state with covariance GA = -(1/4) Tr(W GA)."""
    return -0.25 * np.trace(W @ GA)
