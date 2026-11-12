"""Gera guias A4 etiquetados do padrão visual 1.0.0."""
import argparse
from contextlib import contextmanager
from html import escape
from io import BytesIO
import json
import os
from pathlib import Path
from urllib.parse import urlparse

from pypdf import PdfReader, PdfWriter
from pypdf.generic import (ArrayObject as Array, BooleanObject, DictionaryObject as Dict,
                           NameObject as Name, NumberObject as Number, TextStringObject)
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph

W, H = A4
M = 42
WIDTH = W - 2 * M
PAPER, GREEN, INK = "#F7F7F2", "#143B36", "#202A26"
MINT, LINE, MUTED = "#E8F1E9", "#CFDAD2", "#4B5A53"
CHAT, BLUE, CHAT_TEXT, CHAT_LABEL = "#212121", "#1E5AAD", "#ECECEC", "#B4B4B4"
CARD_TITLES = ("Para que serve?", "O que resolve?", "Como se aplica?")


class Guide:
    def __init__(self, title):
        font_dir = Path(os.getenv("SKILLS_FONT_DIR", "/usr/share/fonts/truetype/dejavu"))
        for alias, font in (("Sans", "DejaVuSans"), ("Bold", "DejaVuSans-Bold"), ("Serif", "DejaVuSerif")):
            pdfmetrics.registerFont(TTFont(alias, str(font_dir / f"{font}.ttf")))
        pdfmetrics.registerFontFamily("Sans", normal="Sans", bold="Bold")
        self.raw = BytesIO()
        self.canvas = Canvas(self.raw, pagesize=A4, pdfVersion=(1, 7), initialFontName="Sans")
        self.canvas.setTitle(f"{title} | Guia Rápido de Skills")
        self.tree = []
        self.parent = self.tree
        self.pages = []
        self.mcid = 0
        self.link_count = 0

    @contextmanager
    def group(self, tag):
        children = []
        self.parent.append((tag, children, None))
        previous = self.parent
        self.parent = children
        try:
            yield
        finally:
            self.parent = previous

    @contextmanager
    def marked(self, tag=None, link=False):
        if tag:
            mark = self.mcid
            self.mcid += 1
            annotation = self.link_count if link else None
            if link:
                self.link_count += 1
            self.parent.append((tag, (len(self.pages), mark), annotation))
            self.canvas.addLiteral(f"/{tag} <</MCID {mark}>> BDC")
        else:
            self.canvas.addLiteral("/Artifact BMC")
        try:
            yield
        finally:
            self.canvas.addLiteral("EMC")

    def box(self, x, y, w, h, fill, radius=0, border=None):
        with self.marked():
            self.canvas.setFillColor(HexColor(fill))
            if border:
                self.canvas.setStrokeColor(HexColor(border))
                self.canvas.setLineWidth(.65)
            if radius:
                self.canvas.roundRect(x, H-y-h, w, h, radius, fill=1, stroke=bool(border))
            else:
                self.canvas.rect(x, H-y-h, w, h, fill=1, stroke=bool(border))

    def line(self, y):
        with self.marked():
            self.canvas.setStrokeColor(HexColor(LINE))
            self.canvas.setLineWidth(.65)
            self.canvas.line(M, H-y, W-M, H-y)

    def paragraph(self, text, size, lead, font, color, label=None):
        markup = escape(text)
        if label:
            markup = f"<b>{escape(label)}:</b> {markup}"
        return Paragraph(markup, ParagraphStyle("guide", fontName=font, fontSize=size,
                                                leading=lead, textColor=HexColor(color)))

    def text(self, text, x, y, w, size=10.5, lead=14, font="Sans", color=INK, tag="P", label=None, url=None):
        paragraph = self.paragraph(text, size, lead, font, color, label)
        _, height = paragraph.wrap(w, H)
        if y < 0 or y+height > H-15:
            raise ValueError(f"Texto fora da área útil: {text}")
        with self.marked(tag, link=bool(url)):
            paragraph.drawOn(self.canvas, x, H-y-height)
        if url:
            link_width = pdfmetrics.stringWidth(text, font, size)
            self.canvas.linkURL(url, (x, H-y-height, x+link_width, H-y))
        return y+height

    def end_page(self):
        self.pages.append(self.mcid)
        self.mcid = 0
        self.canvas.showPage()

    def save(self, path):
        self.canvas.save()
        self.raw.seek(0)
        writer = PdfWriter(clone_from=PdfReader(self.raw))
        writer.pdf_header = "%PDF-1.7"
        root = writer.root_object
        add = writer._add_object  # pypdf fixado em requirements.txt
        root[Name("/Lang")] = TextStringObject("pt-BR")
        root[Name("/MarkInfo")] = Dict({Name("/Marked"): BooleanObject(True)})
        root[Name("/ViewerPreferences")] = Dict({Name("/DisplayDocTitle"): BooleanObject(True)})
        struct = add(Dict({Name("/Type"): Name("/StructTreeRoot")}))
        root[Name("/StructTreeRoot")] = struct
        doc = add(Dict({Name("/Type"): Name("/StructElem"), Name("/S"): Name("/Document"), Name("/P"): struct}))
        struct.get_object()[Name("/K")] = doc
        pages = [page.indirect_reference for page in writer.pages]
        parents = [Array([Number(-1)] * count) for count in self.pages]
        annotation_parents = []
        for index, page in enumerate(writer.pages):
            page[Name("/StructParents")] = Number(index)
            page[Name("/Tabs")] = Name("/S")

        def attach(nodes, parent):
            children = Array()
            for tag, content, annotation in nodes:
                obj = add(Dict({Name("/Type"): Name("/StructElem"), Name("/S"): Name("/"+tag), Name("/P"): parent}))
                children.append(obj)
                if isinstance(content, list):
                    obj.get_object()[Name("/K")] = attach(content, obj)
                    continue
                page_index, mcid = content
                page_ref = pages[page_index]
                obj.get_object()[Name("/Pg")] = page_ref
                obj.get_object()[Name("/K")] = Number(mcid)
                parents[page_index][mcid] = obj
                if annotation is not None:
                    # Os guias têm uma única referência oficial, no encerramento.
                    ref = page_ref["/Annots"][0]
                    key = len(pages)+annotation
                    ref.get_object()[Name("/StructParent")] = Number(key)
                    ref.get_object()[Name("/Contents")] = TextStringObject("Consultar a pasta oficial no GitHub.")
                    obj.get_object()[Name("/K")] = Array([Number(mcid), Dict({
                        Name("/Type"): Name("/OBJR"), Name("/Obj"): ref, Name("/Pg"): page_ref,
                    })])
                    annotation_parents.extend((Number(key), obj))
            return children

        doc.get_object()[Name("/K")] = attach(self.tree, doc)
        entries = Array()
        for index, marks in enumerate(parents):
            if any(int(mark) == -1 for mark in marks if isinstance(mark, Number)):
                raise ValueError("MCID sem elemento estrutural.")
            entries.extend((Number(index), marks))
        entries.extend(annotation_parents)
        struct.get_object()[Name("/ParentTree")] = add(Dict({Name("/Nums"): entries}))
        struct.get_object()[Name("/ParentTreeNextKey")] = Number(len(pages)+self.link_count)
        path.parent.mkdir(parents=True, exist_ok=True)
        writer.write(path)


def header(g, data, compact=False):
    g.box(0, 0, W, H, PAPER)
    g.box(0, 0, W, 68 if compact else 154, GREEN)
    g.text("BIBLIOTECA DE SKILLS", M, 24, WIDTH, 8.5, 12, "Bold", MINT)
    g.text(f'{data["nome"].upper()} · v{data["versao"]}', M, 44 if compact else 51,
           WIDTH, 10.5, 14, "Bold", MINT)
    if compact:
        return 87
    bottom = g.text(data["titulo"], M-1, 73, WIDTH+1, 29, 33, "Serif", "#FFFFFF", "H1")
    if bottom > 140:
        raise ValueError("Encurte o título didático.")
    if g.text(data["descricao"], M, bottom+5, WIDTH, 10.3, 14, color="#FFFFFF") > 147:
        raise ValueError("Encurte a introdução.")
    return 172


def cards(g, texts, top):
    gap = 12
    width = (WIDTH-2*gap)/3
    for index, (title, text) in enumerate(zip(CARD_TITLES, texts)):
        x = M+index*(width+gap)
        with g.group("Sect"):
            g.box(x, top, width, 115, "#FFFFFF", 9, LINE)
            y = g.text(title, x+11, top+14, width-22, 11, 14, "Bold", GREEN, "H2")
            if g.text(text, x+11, y+7, width-22, 10.5, 15) > top+105:
                raise ValueError(f"Encurte o card {title}")
    return top+115


def extra(g, data, top):
    if not data:
        return top
    items = data["itens"]
    if not 2 <= len(items) <= 4:
        raise ValueError("Use de dois a quatro itens no conteúdo adicional.")
    y = g.text(data["titulo"], M, top+12, WIDTH, 15.5, 20, "Serif", tag="H2")+6
    w = (WIDTH-9*(len(items)-1))/len(items)
    with g.group("L"):
        for i, item in enumerate(items):
            x = M+i*(w+9)
            numbered = data.get("sequencial")
            with g.group("LI"):
                g.box(x, y, w, 40, MINT, 6)
                if numbered:
                    g.box(x+8, y+11, 16, 16, GREEN, 8)
                    g.text(str(i+1), x+13, y+14, 10, 8, 10, "Bold", "#FFFFFF", "Lbl")
                with g.group("LBody"):
                    offset = 30 if numbered else 9
                    end = g.text(item["titulo"], x+offset, y+6, w-offset-6, 9.1, 12, "Bold", GREEN)
                    if item.get("texto"):
                        end = g.text(item["texto"], x+offset, end+1, w-offset-6, 8.6, 10, color=GREEN)
                    if end > y+39:
                        raise ValueError("Encurte o item do conteúdo adicional.")
    return y+40


def demo(g, data, top):
    y = g.text(data["titulo"], M, top+13, WIDTH, 19, 24, "Serif", tag="H2")
    y = g.text(data["cenario"], M, y+3, WIDTH, 9, 12, color=MUTED)+8
    if "turnos" not in data:
        if not data["paragrafos"]:
            raise ValueError("A demonstração requer conteúdo.")
        heights = [g.paragraph(p, 10.5, 14, "Sans", INK).wrap(WIDTH-30, H)[1]
                   for p in data["paragrafos"]]
        g.box(M, y, WIDTH, sum(heights)+20+5*len(heights), "#FFFFFF", 9, LINE)
        y += 10
        for paragraph in data["paragrafos"]:
            y = g.text(paragraph, M+15, y, WIDTH-30)+5
        return y+10
    if not data["turnos"]:
        raise ValueError("A conversa requer ao menos um turno.")
    chat_start = y
    commands = []

    def queue(text, x, y, width, size=10, lead=13, font="Sans", color=CHAT_TEXT, tag="P", label=None):
        commands.append((text, x, y, width, size, lead, font, color, tag, label))
        return y+g.paragraph(text, size, lead, font, color, label).wrap(width,H)[1]

    bubbles = []
    y += 9
    bw = WIDTH*.70
    bx = W-M-15-bw
    for turn in data["turnos"]:
        y = queue("Você", W-M-48, y, 35, 8.5, 11, "Bold", CHAT_LABEL)+3
        start = y
        y = queue(turn["pedido"], bx+12, y+6, bw-24)+6
        bubbles.append((bx, start, bw, y-start))
        y = queue("Assistente", M+17, y+7, WIDTH-34, 8.5, 11, "Bold", CHAT_LABEL)+3
        for entry in turn["resposta"]:
            if "secao" in entry:
                y = queue(entry["secao"], M+17, y, WIDTH-34, 10.7, 14, "Bold", "#F4F4F4", "H3")+2
            else:
                y = queue(entry["texto"], M+17, y, WIDTH-34, 9.5 if entry.get("nota") else 10,
                          12 if entry.get("nota") else 13, label=entry.get("rotulo"))+2
        y += 5
    g.box(M, chat_start, WIDTH, y+4-chat_start, CHAT, 11, "#353535")
    for x, start, width, height in bubbles:
        g.box(x, start, width, height, BLUE, 14)
    for command in commands:
        g.text(*command)
    return y+4


def finish(g, data, top):
    y = g.text("Quando não usar?", M, top+12, WIDTH, 11, 15, "Bold", GREEN, "H2")+4
    with g.group("L"):
        for example in data["quando_nao_usar"]:
            with g.group("LI"):
                g.text("•", M, y, 11, 10, 13, tag="Lbl")
                with g.group("LBody"):
                    y = g.text(example, M+13, y, WIDTH-13, 10, 13)+2
    if y > 772:
        raise ValueError(f"O conteúdo excede a área útil A4 ({y:.1f} pt). Sintetize ou use a segunda página.")
    g.line(780)
    g.text("Para mais informações sobre a Skill:", M, 790, WIDTH, 9.5, 13, color=MUTED)
    g.text("Consultar a pasta oficial no GitHub.", M, 806, WIDTH, 9.5, 13, "Bold", GREEN,
           "Link", url=data["github"])


def render(data, path):
    url = urlparse(data["github"])
    if (url.scheme != "https" or url.netloc != "github.com"
            or not url.path.startswith("/Jadsonjg/ecosystem-agent-skills/tree/main/skills/")
            or len(url.path.strip("/").split("/")) != 6):
        raise ValueError("Use o link verificado da pasta da Skill no monorepo.")
    if len(data["cards"]) != 3 or not 1 <= len(data["quando_nao_usar"]) <= 3:
        raise ValueError("São obrigatórios três cards e de um a três exemplos de quando não usar.")
    g = Guide(data["nome"])
    top = extra(g, data.get("adicional"), cards(g, data["cards"], header(g, data)))
    if data.get("duas_paginas"):
        if demo(g, data["demonstracao_inicial"], top) > 806:
            raise ValueError("A primeira página excede a área útil.")
        g.end_page()
        top = header(g, data, compact=True)
    finish(g, data, demo(g, data["demonstracao"], top))
    g.end_page()
    g.save(path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("conteudo", type=Path)
    parser.add_argument("pdf", type=Path)
    args = parser.parse_args()
    render(json.loads(args.conteudo.read_text(encoding="utf-8")), args.pdf)
