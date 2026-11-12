"""Regressão de página entre os guias com e sem ícone aprovado."""
import json
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

import fitz
from pypdf import PdfReader

GUIDES = Path(__file__).resolve().parents[1] / "docs" / "guias-visuais"
sys.path.insert(0, str(GUIDES))
import gerar
from gerar import H, M, W, render
from validar import validate


def tags(node):
    node = node.get_object()
    if isinstance(node, list):
        return [tags(child) for child in node]
    if isinstance(node, dict):
        return (node.get("/S"), tags(node["/K"]) if "/K" in node else node.get("/Type"))
    return node


class IconPdfTests(unittest.TestCase):
    def test_approved_icon_only_changes_icon_rectangle(self):
        with TemporaryDirectory() as directory:
            before, after = [Path(directory) / f"{name}.pdf" for name in ("before", "after")]
            no_icons = Path(directory) / "skills.json"
            catalog = json.loads(gerar.CATALOG_PATH.read_text())
            for entry in catalog["skills"]:
                entry.pop("visual_identity", None)
            no_icons.write_text(json.dumps(catalog))
            for config in sorted((GUIDES / "conteudo").glob("*.json")):
                with self.subTest(skill=config.stem):
                    data = json.loads(config.read_text())
                    with patch.object(gerar, "CATALOG_PATH", no_icons):
                        render(data, before)
                    render(data, after)
                    validate(after, data)
                    a, b = map(PdfReader, (before, after))
                    self.assertEqual(a.root_object["/Metadata"].get_data(), b.root_object["/Metadata"].get_data())
                    self.assertEqual(tags(a.root_object["/StructTreeRoot"]), tags(b.root_object["/StructTreeRoot"]))
                    with fitz.open(before) as left, fitz.open(after) as right:
                        self.assertEqual(len(left), len(right))
                        for index, (first, second) in enumerate(zip(left, right)):
                            self.assertEqual(first.get_text(), second.get_text())
                            self.assertEqual(first.get_links(), second.get_links())
                            if index:
                                self.assertEqual(first.get_pixmap().samples, second.get_pixmap().samples)
                                continue
                            icon = fitz.Rect(W-M-30, 22, W-M, 52)
                            self.assertNotEqual(first.get_pixmap(clip=icon).samples, second.get_pixmap(clip=icon).samples)
                            for clip in (fitz.Rect(0, 0, W, 22), fitz.Rect(0, 52, W, H),
                                         fitz.Rect(0, 22, icon.x0, 52), fitz.Rect(icon.x1, 22, W, 52)):
                                self.assertEqual(first.get_pixmap(clip=clip).samples, second.get_pixmap(clip=clip).samples)
