"""Regressões de metadados sobre um guia gerado pelo caminho oficial."""

import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, TextStringObject

from gerar import render
from validar import validate


class XmpTests(unittest.TestCase):
    def test_validate_rejects_invalid_xmp(self):
        data = json.loads((Path(__file__).parent / "conteudo/nivel-de-criticidade.json").read_text(encoding="utf-8"))
        data["nome"] = "Nível de Criticidade & Revisão <teste>"
        cases = (
            ("ausente", "XMP ausente"),
            ("tipo", "/Type /Metadata e /Subtype /XML"),
            ("xml", "XML inválido"),
            ("identificador", "pdfuaid:part deve ser 1"),
            ("titulo", "Título XMP dc:title"),
            ("info", "Título XMP dc:title"),
        )
        with TemporaryDirectory() as directory:
            valid = Path(directory) / "valido.pdf"
            render(data, valid)
            validate(valid, data)
            for case, error in cases:
                with self.subTest(case=case):
                    writer = PdfWriter(clone_from=PdfReader(valid))
                    writer.pdf_header = "%PDF-1.7"
                    stream = writer.root_object["/Metadata"]
                    if case == "ausente":
                        del writer.root_object["/Metadata"]
                    elif case == "tipo":
                        stream[NameObject("/Subtype")] = NameObject("/Text")
                    elif case == "xml":
                        stream.set_data(b"<xml>")
                    elif case == "identificador":
                        stream.set_data(stream.get_data().replace(b">1</pdfuaid:part>", b">2</pdfuaid:part>"))
                    elif case == "titulo":
                        stream.set_data(stream.get_data().replace(b"Guia R", b"Outro R"))
                    else:
                        writer.add_metadata({"/Title": TextStringObject("Outro título")})
                    invalid = Path(directory) / f"{case}.pdf"
                    writer.write(invalid)
                    with self.assertRaisesRegex(ValueError, error):
                        validate(invalid, data)


if __name__ == "__main__":
    unittest.main()
