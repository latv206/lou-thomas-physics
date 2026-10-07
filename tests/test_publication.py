"""Regression checks for publication metadata and source-map integrity."""
import csv
import hashlib
import json
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[1]


class PublicationTests(unittest.TestCase):
    def test_source_map_binds_existing_public_bytes(self):
        with (ROOT / "docs/SOURCE_MAP.csv").open(encoding="utf-8", newline="") as stream:
            rows = list(csv.DictReader(stream))
        self.assertTrue(rows)
        for row in rows:
            path = ROOT / row["public_path"]
            with self.subTest(file=row["public_path"]):
                self.assertTrue(path.resolve().is_relative_to(ROOT.resolve()))
                self.assertTrue(path.is_file())
                self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), row["public_sha256"])

    def test_notebooks_are_inert_historical_text(self):
        for path in (ROOT / "experiments").rglob("*.ipynb"):
            with self.subTest(file=path.name):
                notebook = json.loads(path.read_text(encoding="utf-8"))
                self.assertTrue(all(cell["cell_type"] == "markdown" for cell in notebook["cells"]))
                self.assertFalse(any(cell.get("outputs") for cell in notebook["cells"]))

    def test_word_identity_and_review_metadata(self):
        for path in ROOT.rglob("*.docx"):
            if "_generated" in path.parts:
                continue
            with self.subTest(file=path.name), zipfile.ZipFile(path) as archive:
                for name in archive.namelist():
                    if name.startswith("docProps/") and name.endswith(".xml"):
                        root = ET.fromstring(archive.read(name))
                        for field in root:
                            key = field.tag.rsplit("}", 1)[-1]
                            if key in {"creator", "lastModifiedBy"}:
                                self.assertIn(field.text or "", {"", "Lou Thomas"})
                            if key in {"Company", "Manager"}:
                                self.assertFalse(field.text)
                    if name.endswith("comments.xml"):
                        self.assertEqual(len(ET.fromstring(archive.read(name))), 0)

    def test_only_the_decoded_historical_animation_is_distributed(self):
        names = {p.name for p in (ROOT / "experiments/conscious-physics").glob("*.gif")}
        self.assertEqual(names, {"symbolic_collapse_energy_density_wave.gif"})


if __name__ == "__main__":
    unittest.main()
