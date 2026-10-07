"""Tests for distribution integrity and numeric-comparison failure behavior."""
import hashlib
import math
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from release_common import compare_values, csv_value, fresh_output
from verify_release import safe_path, verify


class IntegrityTests(unittest.TestCase):
    def setUp(self):
        base = fresh_output("test")
        self.temp = tempfile.TemporaryDirectory(dir=base)
        self.root = Path(self.temp.name)
        self.addCleanup(self.temp.cleanup)
        (self.root / "sample.txt").write_bytes(b"research\n")
        digest = hashlib.sha256(b"research\n").hexdigest()
        (self.root / "SHA256SUMS.txt").write_text(digest + "  sample.txt\n", encoding="utf-8")

    def test_original_passes(self):
        self.assertEqual(verify(self.root), (1, []))

    def test_tamper_fails(self):
        (self.root / "sample.txt").write_bytes(b"changed")
        self.assertIn("Changed: sample.txt", verify(self.root)[1])

    def test_extra_file_fails(self):
        (self.root / "extra.txt").write_bytes(b"extra")
        self.assertIn("Unlisted: extra.txt", verify(self.root)[1])

    def test_missing_file_fails(self):
        (self.root / "sample.txt").unlink()
        self.assertIn("Missing: sample.txt", verify(self.root)[1])

    def test_traversal_fails(self):
        for name in ("../outside", "C:/outside", "/outside", "a\\b"):
            with self.subTest(name=name), self.assertRaises(ValueError):
                safe_path(self.root, name)

    def test_duplicate_manifest_fails(self):
        sums = self.root / "SHA256SUMS.txt"
        sums.write_text(sums.read_text() * 2)
        self.assertTrue(verify(self.root)[1])

    def test_generated_output_ignored(self):
        (self.root / "_generated").mkdir()
        (self.root / "_generated/new.log").write_text("local")
        self.assertFalse(verify(self.root)[1])


class NumericTests(unittest.TestCase):
    def test_roundoff_passes(self):
        compare_values({"x": [1.0 + 1e-10]}, {"x": [1.0]})

    def test_drift_fails(self):
        with self.assertRaises(AssertionError):
            compare_values(1.1, 1.0)

    def test_nonfinite_fails(self):
        for value in (math.nan, math.inf, -math.inf):
            with self.subTest(value=value), self.assertRaises(AssertionError):
                compare_values(value, 1.0)

    def test_boolean_not_number(self):
        with self.assertRaises(AssertionError):
            compare_values(True, 1)

    def test_csv_nested_values(self):
        self.assertEqual(csv_value('{"x": 0.1}'), {"x": 0.1})
        self.assertIs(csv_value("True"), True)
        self.assertEqual(csv_value("claim"), "claim")


if __name__ == "__main__":
    unittest.main()
