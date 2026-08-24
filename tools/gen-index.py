#!/usr/bin/env python3
"""Regenerate matters/index.md from the frontmatter of every matter.

Interim. The real tool is m0008; this exists so the doctrine's claim that
views are derived (doctrine/matters.md §8) is executable rather than
aspirational. Run from the repo root.
"""
import io, os, re, glob, sys

ORDER = ["executed", "staged", "ratified", "proposed",
         "rejected", "withdrawn", "superseded"]


def frontmatter(path):
    text = io.open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        sys.exit(f"{path}: no frontmatter (OKF requires it)")
    fields = {}
    for line in m.group(1).split("\n"):
        if re.match(r"^\w+:", line):
            key, _, value = line.partition(":")
            fields[key.strip()] = value.strip()
    if not fields.get("type"):
        sys.exit(f"{path}: empty 'type' (OKF requires it)")
    return fields


def main():
    rows = []
    for path in sorted(glob.glob("matters/m*.md")):
        row = frontmatter(path)
        row["file"] = os.path.basename(path)
        rows.append(row)

    out = ["---", "okf_version: 0.2", "---", "",
           "# Matters", "",
           "Derived from the frontmatter of every file in this directory.",
           "**Do not hand-edit** — run `tools/gen-index.py`. "
           "See [m0008](/m0008-matter-tooling.md).", ""]

    for state in ORDER:
        group = [r for r in rows if r.get("state") == state]
        if not group:
            continue
        out += [f"## {state}", "", "| | Type | Target | Matter |",
                "|---|---|---|---|"]
        for r in group:
            out.append(f"| `{r['id']}` | {r['type']} | {r.get('target','—')} | "
                       f"[{r['title']}](/{r['file']}) |")
        out.append("")

    linked = [r for r in rows if r.get("depends_on") or r.get("implements")]
    if linked:
        out += ["## Ordering", "",
                "`implements` names the spec a matter serves; `depends_on` "
                "constrains execution order.", "",
                "| Matter | Implements | Depends on |", "|---|---|---|"]
        for r in linked:
            out.append(f"| `{r['id']}` | {r.get('implements','—')} | "
                       f"{r.get('depends_on','—')} |")
        out.append("")

    io.open("matters/index.md", "w", encoding="utf-8").write("\n".join(out))
    print(f"{len(rows)} matters indexed")


if __name__ == "__main__":
    main()
