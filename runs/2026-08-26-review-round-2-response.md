# Run — review round 2 response: in-situ excerpts and tree invariants

Append-only verification record (spec §9.1). Never edited; a
superseding run is a new file. Filed for the operator review round 2
response on [m0001](../matters/m0001-matter-system.md), which rebuilds
the exchange thread's comment blocks as in-situ excerpts (review r8),
applies rulings r1–r4 and r7b to the specification, files
[m0013](../matters/m0013-bootstrap-defaults-record.md), and revises
[m0012](../matters/m0012-formic-matters-split.md).

## Claims tested

- Every rebuilt comment block in
  [threads/2026-08-25-doctrine-operator-review.md](../threads/2026-08-25-doctrine-operator-review.md)
  is a byte-exact excerpt of `doctrine/matters.md` at `9c1d295` over
  its stated line range, and contains its comment line — so each
  comment verifiably carries the text it responds to, which is what r8
  asked for.
- No comment marker survives in the working specification; the one
  `->[…]` string is §8's naming of the syntax, in backticks.
- Every `review <label>` citation in authored files (`cNN`, `a1`–`a4`,
  `i1`, `rN`) resolves to a labeled block, turn, or apparatus entry in
  the thread.
- `tools/gen-index.py` regenerates `matters/index.md` byte-identically
  over all thirteen matters (schema and state→status derivation
  enforced in the same pass); every relative link in authored files
  resolves and none is leading-slash.
- No ratification pin is computed anywhere in this response — the
  specification moved again (§6, "the pin follows the act").

## Environment

- OS: Linux 6.18.44-fc-v21, x86_64 (remote agent container)
- bash 5.2.21(1)-release; git 2.43.0; GNU coreutils 9.4; GNU sed 4.9;
  GNU grep 3.11
- Python 3.11.15, PyYAML 6.0.1
- Repo: `ob6to8/beatcode-dev`, the m0001 lineage (PR #2 head), parent
  commit `3ea60e8`; the tree verified is this response's, in which this
  run file lands
- `ob6to8/beatcode` was not cloned; nothing here bears on m0002–m0005

## Commands and results

1. **Excerpt fidelity.** For each of the nineteen blocks, the header
   `**cNN · §S, lines A–B — comment at line N …:**` is parsed, the
   four-backtick fence content compared to `git show
   9c1d295:doctrine/matters.md` lines A–B joined verbatim, and line N
   confirmed to be one of the excerpt's lines:

   ```python
   import re, subprocess
   src = subprocess.run(
       ["git", "show", "9c1d295:doctrine/matters.md"],
       capture_output=True, text=True, check=True).stdout.split("\n")
   thread = open("threads/2026-08-25-doctrine-operator-review.md",
                 encoding="utf-8").read()
   pat = re.compile(
       r"\*\*(c\d\d) · [^,]+, lines? (\d+)(?:–(\d+))? — comment at "
       r"line (\d+)[^:]*:\*\*\n\n````\n(.*?)\n````", re.S)
   blocks = pat.findall(thread)
   assert len(blocks) == 19
   for label, a, b, n, body in blocks:
       a, n = int(a), int(n)
       b = int(b) if b else a
       assert body == "\n".join(src[a - 1:b]), label
       assert src[n - 1] in body.split("\n"), label
   ```

   Expected: all assertions pass. **Observed: 19 blocks, all
   byte-exact, every comment line inside its excerpt** — c02's unclosed
   bracket and trailing space included. Marker scan of the working
   `doctrine/matters.md` (excluding §8's backticked syntax reference):
   **0 remaining.**

2. **Label resolution.** Definitions from the thread (`**cNN · `,
   `**aN · `, `(i1)`, `**rN**` in the apparatus), citations as
   `review <label>` across authored `.md` files. Expected: every cited
   label defined. **Observed: 33 defined, 27 cited, difference
   empty** — the r-labels resolve alongside c, a, and i.

3. **Index regeneration, twice:** `python3 tools/gen-index.py` →
   `13 matters indexed`, second run byte-identical (`diff` against a
   copy). **Observed: identical; m0013 present, all `proposed`, no
   `target` anywhere.**

4. **Link integrity over authored files** (all `.md` outside
   `threads/`, per §12): same checker as the previous run. Expected:
   zero failures with this file present. **Observed: 294 relative
   links checked, 0 failures, none leading-slash.**

## Verdict

All four mechanical claims hold; the fifth is satisfied by absence —
no hash of the specification or of any ratified region appears in this
response, its thread, or its commit message.

- Date: 2026-08-26
- Actor: claude-code/2026-08-26, the response author (not a fresh
  reviewer; the independence note on m0001's round 2 response entry
  applies here as well)
