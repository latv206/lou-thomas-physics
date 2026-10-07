"""Local-only helpers for the reviewed reproduction entry points."""
from datetime import datetime, timezone
import hashlib
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import uuid

ROOT = Path(__file__).resolve().parents[1]


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fresh_output(label):
    base = ROOT / "_generated"
    if base.is_symlink() or not base.resolve().is_relative_to(ROOT):
        raise ValueError("_generated must be inside this repository, not a link")
    base.mkdir(exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    target = base / f"{label}_{stamp}_{uuid.uuid4().hex[:8]}"
    target.mkdir(exist_ok=False)
    return target


def run_local(script, workdir, output, extra_env=None, arguments=()):
    env = os.environ.copy()
    for key in ("HUB_ROOT", "PYTHONPATH", "PYTHONHOME", "PYTHONSTARTUP"):
        env.pop(key, None)
    env.update({key: "1" for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")})
    env.update({"PYTHONDONTWRITEBYTECODE": "1", "PYTHONNOUSERSITE": "1",
                "MPLCONFIGDIR": str(output / "matplotlib-cache"),
                "TEMP": str(output / "tmp"), "TMP": str(output / "tmp"),
                "TMPDIR": str(output / "tmp")})
    (output / "tmp").mkdir()
    env.update(extra_env or {})
    with (output / "run.log").open("w", encoding="utf-8") as log:
        subprocess.run([sys.executable, "-B", str(script), *arguments], cwd=workdir,
                       env=env, stdout=log, stderr=subprocess.STDOUT,
                       check=True, timeout=600, shell=False)


def compare_values(actual, expected, label="value", rtol=1e-7, atol=1e-9):
    if isinstance(expected, dict):
        if not isinstance(actual, dict) or actual.keys() != expected.keys():
            raise AssertionError(f"{label}: dictionary keys differ")
        for key in expected:
            compare_values(actual[key], expected[key], f"{label}.{key}", rtol, atol)
    elif isinstance(expected, list):
        if not isinstance(actual, list) or len(actual) != len(expected):
            raise AssertionError(f"{label}: list lengths differ")
        for i, (a, e) in enumerate(zip(actual, expected)):
            compare_values(a, e, f"{label}[{i}]", rtol, atol)
    elif isinstance(expected, bool) or expected is None:
        if actual is not expected:
            raise AssertionError(f"{label}: {actual!r} != {expected!r}")
    elif isinstance(expected, (int, float)):
        if isinstance(actual, bool) or not isinstance(actual, (int, float)):
            raise AssertionError(f"{label}: numeric type differs")
        if not math.isfinite(actual) or not math.isfinite(expected) or not math.isclose(actual, expected, rel_tol=rtol, abs_tol=atol):
            raise AssertionError(f"{label}: {actual!r} != {expected!r}")
    elif actual != expected:
        raise AssertionError(f"{label}: {actual!r} != {expected!r}")


def csv_value(value):
    if value in {"True", "False"}:
        return value == "True"
    try:
        return json.loads(value)
    except (ValueError, TypeError):
        return value


def finish(output, report):
    (output / "verification.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    print("Output:", output.relative_to(ROOT).as_posix())
