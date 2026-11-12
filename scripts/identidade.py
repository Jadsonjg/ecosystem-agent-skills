"""Gera e valida a identidade iconográfica a partir do SVG mestre."""
import argparse
import hashlib
import html
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
from tempfile import NamedTemporaryFile
from urllib.parse import quote
from urllib.request import urlopen
from xml.etree import ElementTree as ET

import fitz

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "skills.json"
SVG = "{http://www.w3.org/2000/svg}"
STATES = {"pilot", "approved"}
VARIANTS = {"icon_negative": ("icone-negativo.svg", "#FFFFFF"),
            "icon_monochrome": ("icone-monocromatico.svg", "#242424")}
BEGIN, END = "<!-- identidade:inicio -->", "<!-- identidade:fim -->"


def read_svg(source):
    if len(source) > 8192 or b"<!" in source or b"<?" in source:
        raise ValueError("SVG deve ser simples, autocontido e ter no máximo 8 KiB.")
    svg = ET.fromstring(source)
    if (svg.tag != SVG + "svg" or svg.attrib != {"width": "24", "height": "24", "viewBox": "0 0 24 24"}
            or [node.tag for node in svg] != [SVG + "title", SVG + "path"]):
        raise ValueError("Use SVG 24 × 24 com título e um path.")
    title, path = svg
    if (not (title.text or "").strip() or title.attrib or len(title) or len(path)
            or set(path.attrib) != {"d", "fill", "stroke", "stroke-width", "stroke-linecap", "stroke-linejoin"}
            or path.get("fill") != "none" or path.get("stroke-width") != "1.6"
            or path.get("stroke-linecap") != "round" or path.get("stroke-linejoin") != "round"
            or not re.fullmatch(r"#[0-9A-F]{6}", path.get("stroke", ""))
            or not re.fullmatch(r"[MLHVCSQTAZmlhvcsqtaz0-9,. +\-\s]{1,2500}", path.get("d", ""))):
        raise ValueError("Geometria ou atributos fora do padrão.")
    return path


def rasterize(source, size):
    with fitz.open("svg", source) as document:
        page = document[0]
        pixels = page.get_pixmap(matrix=fitz.Matrix(size / 24, size / 24), alpha=True)
    alpha = pixels.samples[3::4]
    rows = [alpha[y:y + size] for y in range(0, len(alpha), size)]
    occupied = [i for i, row in enumerate(rows) if any(row)]
    if (pixels.width != size or pixels.height != size or not occupied
            or min(alpha) != 0 or max(alpha) < 160 or len(occupied) < size / 2
            or occupied[0] == 0 or occupied[-1] == size - 1
            or any(row[0] or row[-1] for row in rows)):
        raise ValueError(f"Enquadramento, transparência ou traço inválido a {size} px.")
    return pixels.tobytes("png")


def plan(skill):
    name = skill["name"]
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        raise ValueError("Identificador canônico inválido.")
    folder = ROOT / "skills" / name
    if not (folder / "SKILL.md").is_file():
        raise ValueError(f"Especificação ausente: {name}")
    directory = folder / "assets" / "identity"
    config = ROOT / "docs" / "guias-visuais" / "conteudo" / f"{name}.json"
    color = json.loads(config.read_text())["cor_institucional"]
    master = directory / "icone.svg"
    source = master.read_bytes()
    stroke = read_svg(source).attrib["stroke"]
    if stroke != color:
        raise ValueError(f"A cor do mestre deve coincidir com a do guia: {name}")
    relative = lambda path: path.relative_to(ROOT).as_posix()
    previous = skill.get("visual_identity", {})
    state = previous.get("icon_status", "pilot")
    if state not in STATES | {"pending_approval"}:
        raise ValueError(f"Estado inválido: {state}")
    identity = {**previous, "icon_status": "approved" if state == "approved" else "pilot",
                "icon": relative(master), "icon_png": relative(directory / "icone.png"),
                "visual_guide_config": relative(config)}
    legacy = folder / "assets" / "icon.svg"
    if legacy.is_file():
        identity["existing_interface_icon"] = relative(legacy)
    outputs = {}
    for field, (filename, variant) in VARIANTS.items():
        path = directory / filename
        identity[field] = relative(path)
        colored = source.replace(f'stroke="{stroke}"'.encode(), f'stroke="{variant}"'.encode(), 1)
        read_svg(colored)
        outputs[path] = colored
    rasterize(source, 16)
    png = rasterize(source, 512)
    outputs[directory / "icone.png"] = png
    identity["asset_sha256"] = hashlib.sha256(png).hexdigest()
    identity["svg_sha256"] = hashlib.sha256(source).hexdigest()
    if state == "approved" and (previous != identity or any(not p.is_file() or p.read_bytes() != b for p,b in outputs.items())):
        raise ValueError(f"Identidade aprovada requer revisão explícita para qualquer alteração: {name}")
    return identity, outputs


def badge(identity, prefix, size):
    return (f'<picture><source media="(prefers-color-scheme: dark)" srcset="{prefix}{identity["icon_negative"]}">'
            f'<img src="{prefix}{identity["icon"]}" alt="" width="{size}" height="{size}"></picture>')


def section(path, content):
    original = path.read_text() if path.exists() else ""
    body = f"{BEGIN}\n{content}\n{END}"
    if BEGIN in original or END in original:
        if original.count(BEGIN) != 1 or original.count(END) != 1 or original.index(BEGIN) > original.index(END):
            raise ValueError(f"Marcadores ambíguos: {path}")
        return (original[:original.index(BEGIN)] + body + original[original.index(END)+len(END):]).encode()
    return (original.rstrip() + "\n\n" + body + "\n").lstrip("\n").encode()


def inventory(entries, prefix=""):
    lines = ["| Skill | Versão funcional | Identidade |", "| --- | --- | --- |"]
    for skill in entries:
        name = html.escape(skill["display_name"]).replace("|", "&#124;")
        identity = skill.get("visual_identity", {})
        state = identity.get("icon_status")
        icon = badge(identity, prefix, 20) + " " if state in STATES else ""
        label = {"pilot": "Piloto", "approved": "Aprovada"}.get(state, "Pendente")
        lines.append(f'| {icon}[{name}]({prefix}{skill["native_spec"]}) | {skill["version"]} | {label} |')
    return "\n".join(lines)


def change_catalog(catalog, selected, check):
    outputs = {}
    for skill in selected:
        identity, assets = plan(skill)
        if check and skill.get("visual_identity") != identity:
            raise ValueError(f"Catálogo divergente: {skill['name']}")
        skill["visual_identity"] = identity
        outputs.update(assets)
        readme = ROOT / "skills" / skill["name"] / "README.md"
        label = "Piloto" if identity["icon_status"] == "pilot" else "Aprovada"
        content = f'## Identidade iconográfica\n\n{badge(identity, "../../", 24)} **{skill["display_name"]}** · {label}'
        outputs[readme] = section(readme, content)
    outputs[ROOT / "README.md"] = section(
        ROOT / "README.md", "## Identidades iconográficas\n\n" + inventory(catalog["skills"]))
    outputs[ROOT / "docs" / "catalogo-visual.md"] = section(
        ROOT / "docs" / "catalogo-visual.md", "# Catálogo visual\n\n" + inventory(catalog["skills"], "../"))
    outputs[CATALOG] = (json.dumps(catalog, indent=2, ensure_ascii=False) + "\n").encode()
    changed = [p for p,b in outputs.items() if not p.is_file() or p.read_bytes() != b]
    if check and changed:
        raise ValueError("Saídas divergentes: " + ", ".join(str(p.relative_to(ROOT)) for p in changed))
    for path in changed:
        path.parent.mkdir(parents=True, exist_ok=True)
        with NamedTemporaryFile(dir=path.parent, delete=False) as temp:
            temp.write(outputs[path])
        os.chmod(temp.name, 0o644)
        os.replace(temp.name, path)
    print(f"{len(selected)} identidade(s) verificadas, {len(changed)} arquivo(s) atualizado(s).")


def distribution(skill, revision, allow_pilot=False):
    if not re.fullmatch(r"[0-9a-f]{40}", revision):
        raise ValueError("Informe o SHA completo do commit publicado.")
    identity = skill.get("visual_identity", {})
    if identity.get("icon_status") not in (STATES if allow_pilot else {"approved"}):
        return {"name": skill["display_name"], "icon": None}
    path = f"skills/{skill['name']}/assets/identity/icone.png"
    if identity.get("icon_png") != path:
        raise ValueError("Referência PNG divergente do caminho canônico.")
    url = "https://raw.githubusercontent.com/Jadsonjg/ecosystem-agent-skills/"
    return {"name": skill["display_name"], "icon": url + revision + "/" + quote(path),
            "sha256": identity["asset_sha256"]}


def verify_distribution(entries):
    for entry in entries:
        if not entry["icon"]:
            continue
        with urlopen(entry["icon"], timeout=20) as response:
            content = response.read(256 * 1024 + 1)
            if response.status != 200 or response.headers.get_content_type() != "image/png":
                raise ValueError(f"Resposta sem PNG: {entry['icon']}")
        if (not content.startswith(b"\x89PNG\r\n\x1a\n")
                or hashlib.sha256(content).hexdigest() != entry["sha256"]):
            raise ValueError(f"PNG remoto diverge do catálogo: {entry['name']}")
        print(f"HTTP 200 image/png · {len(content)} bytes · SHA-256 conferido · {entry['name']}")


def prepare_guides(selected, output):
    generator = ROOT / "docs" / "guias-visuais"
    output.mkdir(parents=True, exist_ok=True)
    verifier = shutil.which("verapdf")
    for skill in selected:
        identity = skill["visual_identity"]
        config = ROOT / identity["visual_guide_config"]
        preview = identity["icon_status"] == "pilot"
        suffix = "-piloto" if preview else ""
        pdf = output / f'{skill["name"]}-guia{suffix}.pdf'
        flags = ["--icone-piloto"] if preview else []
        subprocess.run([sys.executable, str(generator / "gerar.py"), str(config), str(pdf), *flags], check=True)
        subprocess.run([sys.executable, str(generator / "validar.py"), str(config), str(pdf)], check=True)
        if verifier:
            report = subprocess.run([verifier, "--flavour", "ua1", "--format", "xml", str(pdf)],
                                    capture_output=True)
            pdf.with_suffix(".verapdf.xml").write_bytes(report.stdout)
            report.check_returncode()
            results = list(ET.fromstring(report.stdout).iter("validationReport"))
            if len(results) != 1 or results[0].get("isCompliant") != "true":
                raise ValueError(f"veraPDF não confirmou PDF/UA-1: {pdf.name}")
        else:
            print(f"PDF/UA-1 externo pendente (veraPDF indisponível): {pdf.name}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation", choices=("build", "check", "prepare", "resolve", "verify-remote"))
    parser.add_argument("skills", nargs="*")
    parser.add_argument("--commit")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--allow-pilot", action="store_true")
    args = parser.parse_args()
    catalog = json.loads(CATALOG.read_text())
    entries = {s["name"]: s for s in catalog["skills"]}
    if len(entries) != len(catalog["skills"]) or set(args.skills) - entries.keys():
        parser.error("Catálogo com duplicatas ou Skill desconhecida.")
    if len(args.skills) != len(set(args.skills)):
        parser.error("Informe cada Skill somente uma vez.")
    selected = [entries[n] for n in args.skills] if args.skills else list(entries.values())
    if args.operation in {"resolve", "verify-remote"}:
        if not args.commit:
            parser.error("A verificação ou resolução de URL exige --commit.")
        references = [distribution(s, args.commit, args.allow_pilot) for s in selected]
        if args.operation == "verify-remote":
            verify_distribution(references)
        else:
            print(json.dumps(references, ensure_ascii=False))
    else:
        if args.operation == "prepare" and not args.output:
            parser.error("prepare exige --output.")
        change_catalog(catalog, selected, args.operation == "check")
        if args.operation == "prepare":
            prepare_guides(selected, args.output)


if __name__ == "__main__":
    main()
