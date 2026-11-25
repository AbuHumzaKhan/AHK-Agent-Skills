"""Validate the AHK Agent Skills repository structure and SKILL.md metadata."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
errors = []

if not SKILLS.exists():
    errors.append("Missing skills/ directory.")

skill_dirs = sorted(p for p in SKILLS.iterdir() if p.is_dir()) if SKILLS.exists() else []

if not skill_dirs:
    errors.append("No skill directories found.")

for directory in skill_dirs:
    path = directory / "SKILL.md"
    if not path.is_file():
        errors.append(f"{directory.relative_to(ROOT)}: missing SKILL.md")
        continue

    text = path.read_text(encoding="utf-8")
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not match:
        errors.append(f"{path.relative_to(ROOT)}: invalid frontmatter")
        continue

    frontmatter = match.group(1)
    name = re.search(r"^name:\s*(.+)$", frontmatter, re.M)
    description = re.search(r"^description:\s*(.+)$", frontmatter, re.M)

    if not name:
        errors.append(f"{path.relative_to(ROOT)}: missing name")
    elif name.group(1).strip() != directory.name:
        errors.append(f"{path.relative_to(ROOT)}: name does not match directory")

    if not description:
        errors.append(f"{path.relative_to(ROOT)}: missing description")

if errors:
    print("Skill validation FAILED:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(f"Skill validation PASSED: {len(skill_dirs)} skills.")
