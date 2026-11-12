"""Verifica estrutura e ordem do Guia Rápido. Não certifica PDF/UA."""
import argparse
import json
from pathlib import Path

import fitz
from pypdf import PdfReader
from pypdf.generic import ArrayObject, ContentStream, NumberObject

from cores import WHITE, contrast, institutional_color
from metadados import validate_xmp


def check(condition, reason):
    if not condition:
        raise ValueError(reason)


def validate(path, data):
    accent = institutional_color(data)
    expected_rgb = tuple(bytes.fromhex(accent[1:]))
    reader = PdfReader(path)
    root = reader.root_object
    check(reader.pdf_header == "%PDF-1.7", "Cabeçalho PDF 1.7 ausente.")
    pages = reader.pages
    check(len(pages) == (2 if data.get("duas_paginas") else 1), "Paginação incorreta.")
    check(root.get("/Lang") == "pt-BR", "Idioma incorreto.")
    check(root["/MarkInfo"]["/Marked"] and reader.metadata.title, "Marcações ou título ausentes.")
    validate_xmp(reader, f'{data["nome"]} | Guia Rápido de Skills')
    struct = root["/StructTreeRoot"]
    parent_array = struct["/ParentTree"]["/Nums"]
    parents = {int(parent_array[i]): parent_array[i+1] for i in range(0, len(parent_array), 2)}
    tags = []
    ordered = []
    link_count = 0
    page_ids = {page.indirect_reference.idnum: i for i, page in enumerate(pages)}

    def walk(ref, parent, ancestry=()):
        nonlocal link_count
        node = ref.get_object()
        tag = str(node["/S"])
        tags.append(tag)
        check(node.raw_get("/P") == parent, f"Pai estrutural incorreto em {tag}.")
        if tag in ("/LI", "/Lbl", "/LBody"):
            check(ancestry[-1] == ("/L" if tag == "/LI" else "/LI"), "Lista mal estruturada.")
        children = node["/K"]
        children = children if isinstance(children, ArrayObject) else [children]
        for child in children:
            if isinstance(child, NumberObject):
                page = page_ids[node.raw_get("/Pg").idnum]
                check(parents[page][int(child)] == ref, "MCID ausente ou incorreto no ParentTree.")
                ordered.append((page, int(child), tag))
            elif child.get_object().get("/Type") == "/OBJR":
                obj = child.get_object()["/Obj"]
                check(tag == "/Link" and parents[obj["/StructParent"]] == ref, "Link fora da árvore.")
                check(obj["/A"]["/URI"] == data["github"], "Destino do link incorreto.")
                link_count += 1
            else:
                walk(child, ref, (*ancestry, tag))

    walk(struct.raw_get("/K"), root.raw_get("/StructTreeRoot"))
    check(tags.count("/H1") == 1 and tags.count("/H2") >= 5 and "/P" in tags, "Hierarquia incompleta.")
    level = 0
    for tag in tags:
        if tag in ("/H1", "/H2", "/H3"):
            new_level = int(tag[-1])
            check(new_level <= level+1, "A hierarquia saltou um nível.")
            level = new_level
    check(link_count == 1 and tags.count("/Link") == 1, "Link final precisa de etiqueta única.")
    actual = []
    artifacts = 0
    for idx, page in enumerate(pages):
        check(abs(float(page.mediabox.width)-595.28) < .1 and abs(float(page.mediabox.height)-841.89) < .1,
              "Formato diferente de A4.")
        check(page["/StructParents"] == idx and page["/Tabs"] == "/S", "Ordem de foco incorreta.")
        check(len(page.get("/Annots", [])) == int(idx == len(pages)-1), "Link fora da última página.")
        scope = []
        for operands, op in ContentStream(page["/Contents"], reader).operations:
            if op == b"BDC":
                tag, props = operands
                actual.append((idx, int(props["/MCID"]), str(tag)))
                scope.append(str(tag))
            elif op == b"BMC":
                check(operands[0] == "/Artifact", "Marcação sem semântica.")
                artifacts += 1
                scope.append("/Artifact")
            elif op == b"EMC":
                check(bool(scope), "Fechamento de marcação sem abertura.")
                scope.pop()
            elif op in (b"Tj", b"TJ", b"'", b'"'):
                check(scope and scope[-1] != "/Artifact", "Texto sem semântica.")
            elif op in (b"f", b"f*", b"S", b"B", b"B*"):
                check(scope and scope[-1] == "/Artifact", "Decoração sem marca de artefato.")
        check(not scope, "Escopo de marcação não encerrado.")
        check([mcid for p, mcid, _ in actual if p == idx] == list(range(len(parents[idx]))), "MCIDs inválidos.")
    check(actual == ordered and artifacts > 0, "Ordem da árvore diverge do conteúdo ou faltam artefatos.")
    with fitz.open(path) as doc:
        combined = " ".join(" ".join(page.get_text() for page in doc).split())
        sections = [data["titulo"], "Para que serve?", "O que resolve?", "Como se aplica?"]
        if extra := data.get("adicional"):
            sections.append(extra["titulo"])
            if "relacao" in extra:
                check(isinstance(extra["relacao"], str) and bool(extra["relacao"].strip()), "Diagrama sem descrição.")
                check("/L" in tags and tags.count("/LBody") >= len(extra["itens"]), "Rótulos do diagrama sem lista semântica.")
                sections.append(extra["relacao"])
                sections.extend(item["titulo"] for item in extra["itens"])
        demos = [data["demonstracao_inicial"], data["demonstracao"]] if data.get("duas_paginas") else [data["demonstracao"]]
        for demo in demos:
            sections.append(demo["titulo"])
            for _ in demo.get("turnos", []):
                sections.extend(("Você", "Assistente"))
        if guide := data.get("orientacao"):
            sections.extend([guide["titulo"], *guide["paragrafos"]])
        sections += ["Quando não usar?", "Para mais informações sobre a Skill:", "Consultar a pasta oficial no GitHub."]
        pos = 0
        for text in sections:
            text = " ".join(text.split())
            found = combined.find(text, pos)
            check(found >= 0, f"Texto pesquisável ausente ou fora da ordem: {text}")
            pos = found+len(text)
        for index, page in enumerate(doc):
            header_end = 154 if index == 0 else 68
            header_rect = fitz.Rect(0, 0, page.rect.width, header_end)
            header_fills = [drawing["fill"] for drawing in page.get_drawings()
                            if drawing["rect"] == header_rect and drawing.get("fill")]
            check(len(header_fills) == 1 and tuple(round(v*255) for v in header_fills[0]) == expected_rgb,
                  "O cabeçalho não usa a cor institucional registrada.")
            spans = [span for block in page.get_text("dict", flags=fitz.TEXTFLAGS_TEXT)["blocks"]
                     for line in block["lines"] for span in line["spans"]]
            header = [span for span in spans if span["bbox"][1] < header_end]
            check(header and all(span["color"] == 0xFFFFFF for span in header), "Texto não branco no cabeçalho.")
            fixed_accents = ("Para que serve?", "O que resolve?", "Como se aplica?", "Quando não usar?",
                             "Consultar a pasta oficial no GitHub.")
            check(all(span["color"] == int(accent[1:], 16) for span in spans if span["text"] in fixed_accents),
                  "Um título funcional ou link está fora da cor institucional.")
            check(not page.get_images(), "O template atual prevê demonstrações vetoriais e textuais.")
            for x0,y0,x1,y1,*_ in page.get_text("blocks"):
                check(x0 >= 39 and y0 >= 15 and x1 <= page.rect.width-39 and y1 <= page.rect.height-15,
                      "Texto fora da área útil.")
    return len(pages), len(ordered), artifacts


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("conteudo", type=Path)
    parser.add_argument("pdf", type=Path)
    args = parser.parse_args()
    data = json.loads(args.conteudo.read_text(encoding="utf-8"))
    counts = validate(args.pdf, data)
    print(f"OK: {counts[0]} página(s) A4, {counts[1]} blocos semânticos em ordem, {counts[2]} artefatos e link estruturado. Contraste branco/cor: {contrast(WHITE, institutional_color(data)):.2f}:1.")
