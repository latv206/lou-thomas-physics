# C3.4 strict-preflight operational note

## Finding

The original `c34_preflight_audit.py` is usable as a first-pass file/shape gate, but it is too permissive for the next run. It treats non-empty manifest strings as "specified" even when the string itself says:

- candidate
- not yet final
- MISSING
- native only
- external table needed
- requires derived smoothing pipeline

That is acceptable for an exploratory manifest, but not for the locked C3.4 empirical gate.

## Fix

Use `scripts/c34_preflight_audit_strict.py` before authorizing C3.3.

Strict mode blocks on:

- unresolved redshift convention,
- unresolved residual definition if configured as required,
- missing density path,
- non-numeric smoothing scales,
- C3.2 target smoothing scales not present,
- invalid units or field type,
- missing host mass / survey / peculiar-velocity controls,
- missing optional nuisance controls unless `--allow-missing-optional-nuisance` is explicitly passed.

## Recommended command

```bash
python scripts/c34_preflight_audit_strict.py   --manifest c34_data_manifest.json   --out c34_preflight_strict   --allow-missing-optional-nuisance
```

Use the optional-nuisance flag only if the run will explicitly document omission tests for metallicity, sSFR, and host dust.

## Rule

C3.3 is authorized only when:

```json
"ready_for_c33_join": true
```

in the strict preflight verdict.
