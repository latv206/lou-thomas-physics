# Reproducing The Supported Instruments

These are local reproduction tests of recovered numerical instruments. They do not independently establish the proposed physics.

## Environment

Tested on Windows with CPython 3.12 and the direct dependencies pinned in `requirements.txt`. `requirements-lock.txt` records all installed dependency versions from the clean test environment. Dependency source code is not bundled, and pinning a version is not a security audit of that dependency.

From this folder:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-lock.txt
.\.venv\Scripts\python.exe tools/verify_release.py
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
.\.venv\Scripts\python.exe tools/reproduce_a2.py
.\.venv\Scripts\python.exe tools/reproduce_rnsf.py
```

On macOS/Linux use `.venv/bin/python` in place of `.\.venv\Scripts\python.exe`. That platform combination has not been run for this release. Installing dependencies uses the network; the research reproduction commands do not contain download or upload operations.

## A2

The wrapper checks the sealed source's SHA-256 before execution. It copies that source into a fresh `_generated/a2_.../runs/reproduction/` folder and points the historical `HUB_ROOT` environment variable at that private output tree. Its `outbox` and `ledger.md` are local scratch outputs, not the author's operational Hub.

It compares all 13 gate records and five CSV outputs against the recorded July 6 results, including JSON-valued cells. Floating-point comparisons use relative tolerance `1e-7` and absolute tolerance `1e-9`; strings, booleans, keys, and counts must agree. The expected output includes 42 scan rows, 22 claim rows, 20 flagged rows, and 14 folded diagnostics. No folded row is promoted into the claim set.

The old `--lou-authorized` flag is a historical execution switch, not a new approval or a security boundary. Only the wrapper's isolated copy receives it. Do not rename and launch the historical script in a live Hub.

The historical script embeds an output-hash list before rewriting two JSON files. Those embedded self-referential values are not a valid final seal. This distribution's `SHA256SUMS.txt` hashes final bytes without self-reference and is the integrity authority for this edition.

## RNSF

The wrapper copies three reviewed Phase 1 files to a fresh `_generated/rnsf_.../` directory. The mathematical routines are preserved. The runner's output paths are local to the copy, and a stale comment saying interval length 40 was corrected to match the actual length 10. Importing the runner is refused to prevent its top-level computation from running unexpectedly; the two numerical library modules remain importable.

Tests check ED/Gaussian energy and entropy agreement below `1e-9`; first-law residuals below `1e-8`; and recorded fit/profile values within explicitly stated tolerances in `tools/reproduce_rnsf.py`. Small eigenvalue and cancellation residuals are bounded, not expected to reproduce bit for bit. The sparse eigensolver's starting vector is not fixed in the recovered implementation.

## Limits

Each command records `run.log` and `verification.json` under its generated folder. Child processes have a ten-minute timeout and single-threaded BLAS settings. A failed comparison exits nonzero. The output-directory controls prevent ordinary accidental writes into the original work area; they are not an operating-system sandbox for malicious code.

Legacy C-series scripts, report builders, early A2 prototypes, and Conscious Physics notebooks are reference material only. They are not in the supported execution path. Most are `.py.txt` or `.ps1.txt`; every notebook cell is non-executing Markdown. Renaming a file or pasting a cell into a console defeats that precaution.

No late-universe pipeline, early figure generator, manuscript compilation, or generalized physical derivation is newly certified by these two reproduction tests.
