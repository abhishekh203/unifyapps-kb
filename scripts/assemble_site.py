#!/usr/bin/env python3
"""Assemble the MkDocs source tree (site_src/) from our working folders without disturbing them.
Copies docs/ + playbook/ + assignments/ + notes/ into site_src/ and writes a homepage.
Run before `mkdocs build`/`serve`. site_src/ and site/ are gitignored (build artifacts)."""
import os, shutil, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "site_src")

# (source folder, destination subfolder in site_src)
MAP = [("docs", "reference"), ("playbook", "playbook"),
       ("assignments", "assignments"), ("notes", "notes")]

HOME = """# UnifyApps — My Knowledge Base

Private study + build workspace for the UnifyApps platform.

## Sections
- **[Reference docs](reference/MANIFEST.md)** — 361 pages of official UnifyApps docs (with screenshots).
  Start at the **Manifest** (topic quick-jump) or the **[index](reference/00-index.md)**.
- **[Assignments](assignments/README.md)** — the onboarding assignments (~20), one file each.
- **[Playbook](playbook/README.md)** — how-to-do-it-in-the-builder, built from real attempts.
- **Notes** — scratch + ideas.

> Private to me. Reference docs are UnifyApps' material — not for public sharing.
"""


def main():
    if os.path.isdir(SRC):
        shutil.rmtree(SRC)
    os.makedirs(SRC)
    for folder, dest in MAP:
        s = os.path.join(ROOT, folder)
        if os.path.isdir(s):
            shutil.copytree(s, os.path.join(SRC, dest))
    # ensure notes has at least one page so the section isn't empty
    notes = os.path.join(SRC, "notes")
    os.makedirs(notes, exist_ok=True)
    if not glob.glob(os.path.join(notes, "*.md")):
        open(os.path.join(notes, "index.md"), "w").write("# Notes\n\nScratch space & ideas.\n")
    open(os.path.join(SRC, "index.md"), "w").write(HOME)
    n = sum(len(glob.glob(os.path.join(SRC, d, "**", "*.md"), recursive=True)) for _, d in MAP)
    print(f"site_src/ assembled: {n} markdown pages")


if __name__ == "__main__":
    main()
