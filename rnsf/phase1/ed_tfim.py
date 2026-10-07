"""Exact diagonalization for the open-boundary TFIM (validation + first law)."""

import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh

_sx = sp.csr_matrix(np.array([[0.0, 1.0], [1.0, 0.0]]))
_sz = sp.csr_matrix(np.array([[1.0, 0.0], [0.0, -1.0]]))
_id = sp.identity(2, format="csr")


def _op_at(op, j, N):
    out = None
    for m in range(N):
        cur = op if m == j else _id
        out = cur if out is None else sp.kron(out, cur, "csr")
    return out


def tfim_H(N, J=1.0, h=1.0):
    dim = 2 ** N
    H = sp.csr_matrix((dim, dim))
    for j in range(N - 1):
        H = H - J * (_op_at(_sx, j, N) @ _op_at(_sx, j + 1, N))
    for j in range(N):
        H = H - h * _op_at(_sz, j, N)
    return H.tocsr()


def ground_state(N, J=1.0, h=1.0):
    H = tfim_H(N, J, h)
    E, V = eigsh(H, k=1, which="SA", maxiter=20000)
    psi = np.real(V[:, 0])
    psi /= np.linalg.norm(psi)
    return E[0], psi


def rdm_interval(psi, N, a, b):
    """Reduced density matrix of contiguous sites a..b (0-based, inclusive).
    Site 0 is the most-significant qubit (matches kron order in tfim_H)."""
    dL, dA, dR = 2 ** a, 2 ** (b - a + 1), 2 ** (N - 1 - b)
    Tn = psi.reshape(dL, dA, dR)
    return np.einsum("iaj,ibj->ab", Tn, Tn)


def entropy(rho, eps=1e-14):
    p = np.linalg.eigvalsh(rho)
    p = p[p > eps]
    return float(-np.sum(p * np.log(p)))


def modular_K(rho, eps=1e-14):
    """K = -ln rho via eigendecomposition; eigenvalues clipped at eps."""
    p, U = np.linalg.eigh(rho)
    p = np.clip(p, eps, None)
    return (U * (-np.log(p))) @ U.T.conj(), float(p.min())


def rel_entropy(rho_new, rho_old, eps=1e-14):
    """S(rho_new || rho_old) = Tr rho_new (ln rho_new - ln rho_old)."""
    p, U = np.linalg.eigh(rho_new)
    p = np.clip(p, eps, None)
    ln_new = (U * np.log(p)) @ U.T.conj()
    q, V = np.linalg.eigh(rho_old)
    q = np.clip(q, eps, None)
    ln_old = (V * np.log(q)) @ V.T.conj()
    return float(np.real(np.trace(rho_new @ (ln_new - ln_old))))
