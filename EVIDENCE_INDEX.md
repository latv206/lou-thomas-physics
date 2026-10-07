# Evidence Index

The status vocabulary is retained from the source project's claim firewall. "In Hub" refers to evidence captured during local packaging, not a requirement that future readers have the author's workspace. All public evidence paths below are relative to this repository.

| Claim | Status | Evidence and boundary |
|---|---|---|
| Selected source artifacts were recovered into the local package | CONFIRMED_EXTERNAL_COPIED_IN_HUB | `docs/SOURCE_MAP.csv`; original hashes and transformed public hashes are separate |
| Historical A2 package checksum lists verified 57 entries | CONFIRMED_IN_HUB | `docs/verification/source_checksums.json`; checks source packages, not theoretical validity |
| A2 numerical rerun passed 13 instrument gates and reproduced 22 claim rows | CONFIRMED_IN_HUB | `docs/verification/a2_reproduction.json`; tolerances and scope in `docs/REPRODUCING.md` |
| RNSF Phase 1 reproduced finite-chain benchmarks | CONFIRMED_IN_HUB | `docs/verification/rnsf_reproduction.json`; distinct ED and Gaussian implementations of the same stated Hamiltonian, not independent validation of the broader proposal |
| Release integrity tests reject tampering and numerical drift | CONFIRMED_IN_HUB | `tests/test_release.py` and `docs/verification/test_results.json`; checksum trust still depends on obtaining a trusted checksum list |
| Static/privacy review found no unexplained credential-harvesting or exfiltration behavior in scope | CONFIRMED_IN_HUB | `docs/CODE_REVIEW.md` and `docs/verification/review_summary.json`; finite review, not universal safety certification |
| A2 is scoped to a sealed instrument | CONFIRMED_IN_HUB | `bih-vi/code/a2_production_scan.py.txt` and allowed-claims file; does not prove the global absence of a derivation |
| Earlier audit assertions about unrecovered external primary evidence | REPORTED_NOT_IN_HUB | Historical audit text remains attributed; particular recovered files are identified by the source map |
| O4 replacement and broader physical conclusions are correct | HUMAN_DOMAIN_REVIEW_REQUIRED | Needs independent derivation and expert review; not settled by passing numerical gates |
| Rights and public release are approved | LOU_DECISION_REQUIRED | No agent assertion substitutes for owner authority or legal review |

Read [CLAIMS_AND_LIMITS.md](CLAIMS_AND_LIMITS.md) before quoting historical closeout language. Current checksums describe this distribution only; copied historical "all passed" statements retain their original dates and scopes.
