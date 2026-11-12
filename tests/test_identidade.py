"""Regressões da identidade com uma cópia temporária das Skills existentes."""
import importlib.util
import json
from pathlib import Path
import shutil
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("identidade", ROOT / "scripts" / "identidade.py")
identity = importlib.util.module_from_spec(spec)
spec.loader.exec_module(identity)
COMMIT = "a" * 40


class IdentityTests(unittest.TestCase):
    def setUp(self):
        self.temp = TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "repo"
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns("__pycache__", ".git"))
        catalog = self.root / "skills.json"
        override = patch.multiple(identity, ROOT=self.root, CATALOG=catalog)
        override.start()
        self.addCleanup(override.stop)
        self.catalog = json.loads(catalog.read_text())
        self.skill = self.catalog["skills"][0]

    def test_build_is_idempotent_and_preserves_manual_readme(self):
        readme = self.root / "README.md"
        with readme.open("a") as stream:
            stream.write("\nConteúdo manual de teste.\n")
        identity.change_catalog(self.catalog, self.catalog["skills"], False)
        before = readme.stat().st_mtime_ns
        identity.change_catalog(self.catalog, self.catalog["skills"], False)
        identity.change_catalog(self.catalog, self.catalog["skills"], True)
        self.assertEqual(before, readme.stat().st_mtime_ns)
        self.assertIn("Conteúdo manual de teste.", readme.read_text())

    def test_check_rejects_broken_reference_and_corrupt_png(self):
        info = self.skill["visual_identity"]
        original = info["icon_png"]
        info["icon_png"] = "../broken.png"
        with self.assertRaisesRegex(ValueError, "Catálogo divergente"):
            identity.change_catalog(self.catalog, [self.skill], True)
        info["icon_png"] = original
        (self.root / original).write_bytes(b"invalid")
        with self.assertRaisesRegex(ValueError, "Saídas divergentes"):
            identity.change_catalog(self.catalog, [self.skill], True)

    def test_missing_master_and_external_svg_are_rejected(self):
        path = self.root / self.skill["visual_identity"]["icon"]
        source = path.read_bytes()
        path.write_bytes(source.replace(b"<title>", b'<image href="https://example.org/x"/><title>'))
        with self.assertRaisesRegex(ValueError, "SVG 24"):
            identity.plan(self.skill)
        path.unlink()
        with self.assertRaises(FileNotFoundError):
            identity.plan(self.skill)

    def test_approved_master_cannot_change_silently(self):
        info = self.skill["visual_identity"]
        info["icon_status"] = "approved"
        identity.plan(self.skill)
        path = self.root / info["icon"]
        path.write_bytes(path.read_bytes().replace(b"M12 7", b"M12 7.1", 1))
        with self.assertRaisesRegex(ValueError, "Identidade aprovada"):
            identity.plan(self.skill)

    def test_distribution_is_pinned_and_pilot_is_opt_in(self):
        self.assertIsNone(identity.distribution(self.skill, COMMIT)["icon"])
        result = identity.distribution(self.skill, COMMIT, allow_pilot=True)
        self.assertIn(COMMIT, result["icon"])
        self.assertEqual(self.skill["visual_identity"]["asset_sha256"], result["sha256"])
        with self.assertRaisesRegex(ValueError, "SHA"):
            identity.distribution(self.skill, "main", allow_pilot=True)
