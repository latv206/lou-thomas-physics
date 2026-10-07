"""Re-run the unchanged sealed A2 instrument in a private local output tree."""
import csv
import json
from release_common import ROOT, compare_values, csv_value, finish, fresh_output, run_local, sha256

SEALED_SHA256 = "35fd365916395f171fee9278480bd102b267f545fb389d6039cfe0058c78aae8"


def main():
    source = ROOT / "bih-vi/code/a2_production_scan.py.txt"
    if sha256(source) != SEALED_SHA256:
        raise ValueError("Sealed A2 source changed; review before execution")
    output = fresh_output("a2")
    workdir = output / "runs" / "reproduction"
    workdir.mkdir(parents=True)
    (output / "outbox").mkdir()
    script = workdir / "a2_production_scan.py"
    script.write_bytes(source.read_bytes())
    run_local(script, workdir, output, {"HUB_ROOT": str(output)},
              ("--production", "--lou-authorized"))
    actual = output / "outbox/A2_PRODUCTION_LOCAL"
    reference = ROOT / "bih-vi/results/a2-2026-07-06"
    gates = json.loads((actual / "production_gate_summary.json").read_text())
    reference_gates = json.loads((reference / "production_gate_summary.json").read_text())
    compare_values(gates, reference_gates, "gates")
    if len(gates) != 13 or not all(g.get("passed") is True for g in gates.values()):
        raise AssertionError("The 13 recorded instrument gates did not all pass")
    counts = {}
    for name in ("production_scan_rows.csv", "production_family_summary.csv",
                 "folded_gflat_diagnostics.csv", "claim_rows.csv", "flagged_rows.csv"):
        def read_rows(path):
            with path.open(newline="", encoding="utf-8-sig") as stream:
                return [{k: csv_value(v) for k, v in row.items()} for row in csv.DictReader(stream)]
        got, expected = read_rows(actual / name), read_rows(reference / name)
        compare_values(got, expected, name)
        counts[name] = len(got)
    if counts["claim_rows.csv"] != 22 or counts["folded_gflat_diagnostics.csv"] != 14:
        raise AssertionError("Unexpected claim or diagnostic row count")
    finish(output, {"passed": True, "scope": "sealed instrument reproduction, not a derivation",
                    "source_sha256": SEALED_SHA256, "gates_passed": 13, "row_counts": counts,
                    "relative_tolerance": 1e-7, "absolute_tolerance": 1e-9})


if __name__ == "__main__":
    main()
