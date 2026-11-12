"""Check catalog paths and the Delegation Context compatibility files."""

import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
catalog = json.loads((ROOT / "skills.json").read_text(encoding="utf-8"))

seen = set()
for skill in catalog["skills"]:
    name = skill["name"]
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or name in seen:
        raise SystemExit(f"Invalid or repeated skill name: {name}")
    seen.add(name)
    spec = ROOT / "skills" / name / "SKILL.md"
    if ROOT / skill["native_spec"] != spec or not spec.is_file():
        raise SystemExit(f"Invalid canonical specification: {name}")
    frontmatter = spec.read_text(encoding="utf-8").split("---", 2)
    if len(frontmatter) != 3 or f"name: {name}" not in frontmatter[1].splitlines():
        raise SystemExit(f"Specification name does not match the catalog: {name}")
    for key in ("canonical_source", "compatibility_export", "validation_report"):
        if key in skill and not (ROOT / skill[key]).is_file():
            raise SystemExit(f"Missing {key}: {skill[key]}")

discovered = {spec.parent.name for spec in (ROOT / "skills").glob("*/SKILL.md")}
if seen != discovered:
    raise SystemExit(f"Skill directories and catalog differ: {seen ^ discovered}")

delegation = ROOT / "skills" / "delegation-context-skill"
for path in ("SKILL.md", "prompt-mestre.md", "exemplos.md", "agents/openai.yaml", "assets/icon.svg"):
    if (ROOT / path).read_bytes() != (delegation / path).read_bytes():
        raise SystemExit(f"Legacy file differs from the canonical copy: {path}")

body = (delegation / "SKILL.md").read_text(encoding="utf-8").split("---", 2)[2]
export = (delegation / "prompt-mestre.md").read_text(encoding="utf-8")
if body.strip() != export.strip():
    raise SystemExit("Delegation Context prompt export differs from its specification")

print(f"Catalog and compatibility checks passed for {len(seen)} skills.")
