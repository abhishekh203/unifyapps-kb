#!/usr/bin/env python3
"""Emit a COMPACT DIGEST of every doc page (title + first 2 sentences + headings) to
/tmp/ua_digest.txt. This is raw input for Claude to read once and hand-write docs/MANIFEST.md
(curated descriptions + topic grouping). The script does NOT write descriptions itself."""
import os, re, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")
SECTIONS = ["applications", "automations", "data", "agentic-ai",
            "embedded-integrations", "platform-tools", "governance"]
OUT = "/tmp/ua_digest.txt"


def strip_md(s):
    s = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", s)
    s = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", s)
    s = s.replace("**", "").replace("`", "").replace("*", "")
    return re.sub(r"\s+", " ", s).strip(" :#")


def digest(path):
    lines = open(path).read().splitlines()
    body = lines[lines.index("---") + 1:] if "---" in lines else lines
    sentences, headings = [], []
    for l in body:
        if l.startswith("#"):
            h = strip_md(l)
            if h and h.lower() not in ("overview", "introduction"):
                headings.append(h)
            continue
        t = strip_md(l)
        if t and not l.startswith(("|", ">")) and len(t) > 25:
            for s in re.split(r"(?<=[.!?]) ", t):
                if len(s) > 25:
                    sentences.append(s)
        if len(sentences) >= 2 and len(headings) >= 6:
            break
    return " ".join(sentences[:2])[:300], headings[:8]


def main():
    parts = []
    n = 0
    for sec in SECTIONS:
        for fp in sorted(glob.glob(os.path.join(DOCS, sec, "*.md"))):
            slug = os.path.basename(fp)[:-3]
            snip, heads = digest(fp)
            parts.append(f"[{sec}/{slug}] {snip}" +
                         (f" || headings: {', '.join(heads)}" if heads else ""))
            n += 1
    open(OUT, "w").write("\n".join(parts) + "\n")
    print(f"digest written to {OUT}: {n} pages")


if __name__ == "__main__":
    main()
