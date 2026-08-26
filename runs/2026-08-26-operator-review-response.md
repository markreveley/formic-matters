# Run — operator review response: transcription fidelity and tree invariants

Append-only verification record (spec §9.1). Never edited; a
superseding run is a new file. Filed for the operator review response
and round 3 response on
[m0001](../matters/m0001-matter-system.md), which export the
2026-08-25 in-document review to
[threads/2026-08-25-doctrine-operator-review.md](../threads/2026-08-25-doctrine-operator-review.md),
rewrite `doctrine/matters.md` as the Formic Matters specification,
conform every matter's frontmatter (`target` removed, systems as
tags), and file [m0012](../matters/m0012-formic-matters-split.md).

## Claims tested

- The exported thread's nineteen comment blocks (c01–c19) reproduce
  `doctrine/matters.md` at `9c1d295` byte-exact — the transcription §8
  now requires is real, so the ledger's `review cNN` citations describe
  the operator's actual words.
- No operator comment marker survives in the rewritten specification —
  the response commit removed all nineteen, per §8's convention. The
  one remaining `->[…]` string is §8's own naming of the syntax, in
  backticks.
- Every `review <label>` citation in authored files (`cNN`, `a1`–`a4`,
  `i1`) resolves to a labeled block or turn in the thread.
- Tree-wide invariants survive the rewrite: `tools/gen-index.py`
  regenerates `matters/index.md` byte-identically (which also enforces
  the §12 state→status derivation and schema over all twelve matters);
  every relative link in authored files resolves and none uses the
  leading-slash form.
- No ratification pin is computed anywhere in this response — this
  commit changes the specification, so a pin offered here would be
  stale by construction (§6, "the pin follows the act").

## Environment

- OS: Linux 6.18.44-fc-v21, x86_64 (remote agent container)
- bash 5.2.21(1)-release; git 2.43.0; GNU coreutils 9.4
  (`sha256sum`); GNU sed 4.9; GNU grep 3.11
- Python 3.11.15, PyYAML 6.0.1 (`tools/gen-index.py` and the checkers
  below)
- Repo: `markreveley/formic-matters`, the m0001 lineage (PR #2 head), parent
  commit `9c1d295` — the operator's review commit; the tree verified is
  this response's, in which this run file lands
- `markreveley/beatcode` was not cloned; nothing in this response bears on
  m0002–m0005 beyond frontmatter conformance, and earlier rounds own
  those verdicts

## Commands and results

1. **Transcription fidelity and marker removal**, one script, run from
   the repo root:

   ```python
   import re, subprocess
   LINES = [32, 36, 42, 44, 45, 47, 49, 127, 135, 140, 147,
            261, 365, 376, 380, 420, 426, 450, 460]
   src = subprocess.run(
       ["git", "show", "9c1d295:doctrine/matters.md"],
       capture_output=True, text=True, check=True).stdout.split("\n")
   expected = [src[n - 1] for n in LINES]
   thread = open("threads/2026-08-25-doctrine-operator-review.md",
                 encoding="utf-8").read()
   blocks = re.findall(r"\*\*c\d\d · .*?\n\n```\n(.*?)\n```",
                       thread, re.S)
   assert len(blocks) == 19
   for want, got in zip(expected, blocks):
       assert want == got
   head = open("doctrine/matters.md", encoding="utf-8").read()
   markers = [m for m in re.findall(r".?->\s*\[.", head)
              if not m.startswith("`")]
   print(len(blocks), "byte-exact;", len(markers), "markers remain")
   ```

   Expected: `19 byte-exact; 0 markers remain`. **Observed: exactly
   that.** The nineteen source lines include c02's unclosed bracket and
   trailing space, both preserved.

2. **Label resolution.** Definitions extracted from the thread
   (`**cNN · `, `**aN · `, `(i1)`), citations as `review <label>` from
   every authored `.md`:

   ```python
   import glob, re
   thread = open("threads/2026-08-25-doctrine-operator-review.md",
                 encoding="utf-8").read()
   defined = set(re.findall(r"\*\*(c\d\d) · ", thread))
   defined |= set(re.findall(r"\*\*(a[1-4]) · ", thread))
   defined |= {"i1"} if "(i1)" in thread else set()
   cited = set()
   for p in glob.glob("**/*.md", recursive=True):
       if not p.startswith("threads/"):
           cited |= set(re.findall(r"review (c\d\d|a[1-4]|i1)",
                                   open(p, encoding="utf-8").read()))
   print(len(defined), "defined;", len(cited), "cited;",
         sorted(cited - defined))
   ```

   Expected: every cited label defined. **Observed: 24 defined, 18
   cited, difference empty.**

3. **Index regeneration, twice:**

   ```
   python3 tools/gen-index.py   # 12 matters indexed
   python3 tools/gen-index.py   # 12 matters indexed
   ```

   Expected: byte-identical output on the second run (verified by
   `diff` against a copy of the first). **Observed: identical; 12
   matters, all `proposed`, tags column populated, no `target`
   anywhere.** The generator's schema pass (YAML validity, required
   fields, state enum, state→status derivation, filename/id agreement)
   passed on all twelve.

4. **Link integrity over authored files** (all `.md` outside
   `threads/`, per §12's scope):

   ```python
   import glob, os, re
   LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
   total, bad = 0, []
   for path in sorted(p for p in glob.glob("**/*.md", recursive=True)
                      if not p.startswith("threads/")):
       for m in LINK.finditer(open(path, encoding="utf-8").read()):
           t = m.group(1)
           if t.startswith(("http://", "https://", "#", "mailto:")):
               continue
           total += 1
           if t.startswith("/"):
               bad.append((path, t)); continue
           base = os.path.normpath(os.path.join(
               os.path.dirname(path), t.split("#")[0]))
           if not os.path.exists(base):
               bad.append((path, t))
   print(total, "checked;", len(bad), "failures")
   ```

   Expected: zero failures with this file present. **Observed: 274
   relative links checked, 0 failures, none leading-slash.**

## Verdict

All four claims hold; the fifth is satisfied by absence — no hash of
`doctrine/matters.md` or of any matter's ratified region appears in
this response, its thread, or its commit message.

- Date: 2026-08-26
- Actor: claude-code/2026-08-26, the response author (not a fresh
  reviewer; the independence note on m0001's operator-review response
  entry applies to this run as well)
