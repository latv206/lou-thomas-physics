"""Check the distribution without executing research code or using the network."""
import argparse
import hashlib
from pathlib import Path, PurePosixPath
import re
import sys

IGNORED_TOP = {".git", "_generated", ".venv", "venv", "__pycache__"}


def safe_path(root, name):
    parts = PurePosixPath(name).parts
    if not parts or ".." in parts or "\\" in name or ":" in name or name.startswith("/"):
        raise ValueError(f"Unsafe manifest path: {name}")
    path = root.joinpath(*parts)
    if path.is_symlink() or not path.resolve().is_relative_to(root.resolve()):
        raise ValueError(f"Manifest path escapes repository: {name}")
    return path


def verify(root):
    root = root.resolve()
    errors, expected = [], {}
    for number, line in enumerate((root / "SHA256SUMS.txt").read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        if not match:
            errors.append(f"Malformed checksum line {number}")
            continue
        digest, name = match.groups()
        if name in expected or name == "SHA256SUMS.txt":
            errors.append(f"Duplicate or self-referential checksum: {name}")
            continue
        expected[name] = digest
        try:
            path = safe_path(root, name)
            if not path.is_file():
                errors.append(f"Missing: {name}")
            elif hashlib.sha256(path.read_bytes()).hexdigest() != digest:
                errors.append(f"Changed: {name}")
        except ValueError as exc:
            errors.append(str(exc))
    if not expected:
        errors.append("Empty checksum manifest")
    for path in root.rglob("*"):
        rel = path.relative_to(root)
        if rel.parts[0] in IGNORED_TOP or "__pycache__" in rel.parts:
            continue
        if path.is_symlink():
            errors.append(f"Unexpected symbolic link: {rel.as_posix()}")
        elif path.is_file() and rel.as_posix() not in expected and rel.as_posix() != "SHA256SUMS.txt":
            errors.append(f"Unlisted: {rel.as_posix()}")
    return len(expected), errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        count, errors = verify(args.root)
    except (OSError, ValueError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    if errors:
        print("FAIL\n" + "\n".join(errors), file=sys.stderr)
        return 1
    print(f"PASS: {count} checksums match; no unlisted distribution files.")
    print("Integrity only: this does not certify the science, ownership, or absence of malware.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
