"""Re-run the Phase 1 lattice instrument without overwriting recorded results."""
import json
import shutil
from release_common import ROOT, compare_values, finish, fresh_output, run_local, sha256


def main():
    source = ROOT / "rnsf/phase1"
    output = fresh_output("rnsf")
    hashes = {}
    for name in ("run_phase1.py", "gaussian_tfim.py", "ed_tfim.py"):
        shutil.copyfile(source / name, output / name)
        hashes[name] = sha256(source / name)
    run_local(output / "run_phase1.py", output, output)
    actual = json.loads((output / "phase1_numbers.json").read_text())
    expected = json.loads((source / "phase1_numbers.json").read_text())
    # Small eigensolver residuals fluctuate; test their bounds, not their digits.
    for h in ("1.0", "1.5"):
        for key in ("dE", "max_dS"):
            if not 0 <= actual["validation_N10"][h][key] < 1e-9:
                raise AssertionError(f"ED/Gaussian mismatch: {h}, {key}")
        compare_values(actual["validation_N10"][h]["E"], expected["validation_N10"][h]["E"], "ground energy")
    for key in ("max_identity_residual", "max_dK_ED_vs_Gaussian"):
        if not 0 <= actual["first_law"][key] < 1e-8:
            raise AssertionError(f"First-law residual too large: {key}")
    for key in ("slope", "g_KM", "S_A"):
        compare_values(actual["first_law"][key], expected["first_law"][key], key, rtol=2e-5, atol=1e-8)
    compare_values(actual["calabrese_cardy"], expected["calabrese_cardy"], "CC fit", rtol=1e-6)
    compare_values(actual["eh_profile"], expected["eh_profile"], "EH profile", rtol=2e-5)
    finish(output, {"passed": True, "scope": "finite TFIM instrument, not a cosmological validation",
                    "source_sha256": hashes, "numbers": actual})


if __name__ == "__main__":
    main()
