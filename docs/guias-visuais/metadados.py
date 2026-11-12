"""Metadados XMP dos guias PDF/UA-1."""

from xml.etree import ElementTree
from xml.sax.saxutils import escape

from pypdf.generic import NameObject, StreamObject

NS = {
    "x": "adobe:ns:meta/",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "dc": "http://purl.org/dc/elements/1.1/",
    "pdfuaid": "http://www.aiim.org/pdfua/ns/id/",
    "xml": "http://www.w3.org/XML/1998/namespace",
}


def write_xmp(writer):
    title = escape(writer.metadata.title)
    writer.xmp_metadata = f"""<x:xmpmeta xmlns:x="{NS['x']}">
  <rdf:RDF xmlns:rdf="{NS['rdf']}">
    <rdf:Description rdf:about="" xmlns:dc="{NS['dc']}" xmlns:pdfuaid="{NS['pdfuaid']}">
      <dc:title><rdf:Alt><rdf:li xml:lang="x-default">{title}</rdf:li></rdf:Alt></dc:title>
      <pdfuaid:part>1</pdfuaid:part>
    </rdf:Description>
  </rdf:RDF>
</x:xmpmeta>""".encode("utf-8")
    stream = writer.root_object["/Metadata"]
    stream[NameObject("/Type")] = NameObject("/Metadata")
    stream[NameObject("/Subtype")] = NameObject("/XML")


def validate_xmp(reader, expected_title):
    if "/Metadata" not in reader.root_object:
        raise ValueError("Fluxo XMP ausente no catálogo.")
    stream = reader.root_object["/Metadata"]
    if not isinstance(stream, StreamObject) or stream.get("/Type") != "/Metadata" or stream.get("/Subtype") != "/XML":
        raise ValueError("Fluxo XMP deve ter /Type /Metadata e /Subtype /XML.")
    try:
        xmp = ElementTree.fromstring(stream.get_data())
    except ElementTree.ParseError as exc:
        raise ValueError("Fluxo XMP contém XML inválido.") from exc
    if xmp.tag != f"{{{NS['x']}}}xmpmeta":
        raise ValueError("Raiz XMP inválida.")
    rdf = "rdf:RDF/rdf:Description[@rdf:about='']"
    parts = xmp.findall(f"{rdf}/pdfuaid:part", NS)
    if len(parts) != 1 or (parts[0].text or "").strip() != "1":
        raise ValueError("Identificação XMP pdfuaid:part deve ser 1.")
    titles = xmp.findall(f"{rdf}/dc:title/rdf:Alt/rdf:li[@xml:lang='x-default']", NS)
    if len(titles) != 1 or titles[0].text != expected_title or reader.metadata.title != expected_title:
        raise ValueError("Título XMP dc:title deve corresponder ao guia e ao título Info.")
