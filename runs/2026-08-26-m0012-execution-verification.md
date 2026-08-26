# Run — m0012 execution: sweep, move, bootstrap, and re-pin verification

Append-only verification record (spec §9.1). Never edited; a
superseding run is a new file. Filed for the execution of
[m0012](../matters/m0012-formic-matters-split.md) — the reference
sweep (operator ruling R1), the move of m0002–m0005 and m0009 to the
consumer with the licensed edits, the inbound re-pins (R2), and the
consumer bootstrap — verified over both local trees **before
publication**: nothing verified here had been pushed when this run
executed, and the publish order it assumes is framework branch first,
then consumer `main`, so no published record ever references an
unpublished commit.

## Claims tested

- The consumer's installed `doctrine/matters.md` is byte-identical to
  the framework's at the m0001-ratified commit, hashing to the
  recorded pin.
- The five moved matter bodies are byte-identical to their sources at
  the framework's sweep commit `70db408` modulo exactly the licensed,
  itemized edits (the re-pins; m0009's dependency restatement).
- Both derived indexes regenerate byte-identically on a second run.
- Every relative link in authored files resolves, in both trees, under
  §12's scope (`threads/` is evidence; the consumer's copied
  specification is a pinned artifact whose internal references resolve
  against the framework source, per the installation record).
- Every pinned absolute reference written by this execution names a
  path that exists at its named commit (`70db408`, or the ratified
  commit for the installation record's tree link).
- The m0012 and m0013 ratified-region pins still match the framework
  working tree; the corrected doctrine hashes to the candidate value
  the operator's re-ratification will pin.
- No string of the former owner name survives in either working tree
  (R1).
- Every framework-side commit carries `Matter: m0012`; every
  consumer-side installing commit carries `Matter: m0010`.

## Environment

- OS: Linux 6.18.44-fc-v21, x86_64 (remote agent container)
- bash 5.2.21(1)-release; git 2.43.0; GNU coreutils 9.4
  (`sha256sum`); GNU diffutils 3.10
- Python 3.11.15 (`difflib`, `hashlib`, `re`, `glob`), PyYAML 6.0.1
  (`tools/gen-index.py`)
- Framework repo: `markreveley/formic-matters`, branch
  `claude/formic-matters-m0012-review-14vhhy` — sweep commit
  `70db408d9148667097b2cd052853d37d01e9f3fa` (A1, the pin anchor),
  move commit `2f403f892a9f2e0422f5dce264342a6a03917139` (A2); parent
  `6982afc` = `origin/main`. The tree verified is this run's, in which
  this file lands.
- Consumer repo: `markreveley/beatcode-dev`, local `main` — bootstrap
  commit `1c73c02495cf08d6e63b0f8c474bd66633b32319` (C1), import
  commit `ce9d1a5197b2781ed0f8ed79d0b32bda34526ff9` (C2); root
  `d36ea0f`, shared with the framework.
- An independent five-agent adversarial review ran beside these
  checks; its findings are dispositioned in m0012's execution record.

## Commands and results

1. **Spec copy** — `sha256sum` over the consumer's
   `doctrine/matters.md`, against the recorded pin and against
   `git show 85fe4511326a30516ed2bf86a2e2a2b9d05c3d25:doctrine/matters.md`
   in the framework clone. Expected: all three equal
   `5adc0aafe92c5ead0269c681c8802516572765cf77b22549ea5acc45d8dda7bd`.
   **Observed: MATCH, all three.** (Also verified once before the
   installing commit C1 was made — the copy was never committed
   unverified.)

2. **Moved-body fidelity** — for each moved matter,
   `difflib.unified_diff` (n=0) between
   `git show 70db408:matters/<file>` and the consumer file; every
   changed line inspected against the licensed-edit itemization on
   [the consumer's m0010](https://github.com/markreveley/beatcode-dev/blob/main/matters/m0010-framework-installation.md)
   (path reference, dated 2026-08-26). Expected: only itemized edits.
   **Observed: m0002 — 2 changed lines (frontmatter `threads:`
   re-pin); m0003 — 4 (frontmatter `threads:`; one body run link);
   m0004 — 10 (frontmatter `threads:` + `runs:`; three body run
   links); m0005 — 4 (frontmatter `runs:`; one body run link); m0009 —
   10 (`depends_on` line removed; the `## Dependency` section's 2
   lines becoming 7, the prose-precondition restatement with the
   pinned m0008 reference — read line by line: exactly licensed edit
   (2), nothing else).** A first automated whitelist misclassified
   m0009's new prose as unlicensed; the by-eye diff above is the
   verdict, and the full diff is one `git diff` away forever.

3. **Index determinism** — `python3 tools/gen-index.py` twice from
   each repo root, comparing bytes. Expected: identical, schema pass.
   **Observed: identical in both; framework 8 matters, consumer 6;
   state→status derivation and filename/id checks passed on all.**

4. **Link resolution, scoped (§12)** — every markdown link with a
   relative target, resolved against its containing file; framework
   scope excludes `threads/` (evidence), consumer scope excludes the
   pinned specification copy and the empty `threads/`. Expected: all
   resolve, none leading-slash. **Observed: framework 293/293 resolve;
   consumer 14/14; zero leading-slash.** A first pass at the
   pre-A2-amend tree found five unresolved links — two run records
   citing moved matters relatively, an inbound class the plan had not
   enumerated. Fixed under R2 as five further pinned re-pins (itemized
   in the execution record), the fix folded into A2 before anything
   was published; this second pass is the record.

5. **Pin targets** — every
   `https://github.com/markreveley/formic-matters/(blob|tree)/<sha>/<path>`
   in both trees, extracted and checked with
   `git cat-file -e <sha>:<path>` in the framework clone. Expected:
   every pin names `70db408…` (or `85fe451…` for the installation
   record's tree reference) and every path exists there. **Observed:
   10 distinct path-bearing pins, all resolving; one extraction
   artifact (m0010's prose itemization quotes the pin URL with a
   literal `…` placeholder — a template, not a reference).** HTTPS
   service of the `70db408` pins begins when the framework branch
   publishes; the publish order above makes that precede every
   consumer reference to them.

6. **Ratification pins** — the §6 region rule (body after the
   frontmatter's closing `---`, cut at the first `\n## Vetting` /
   `\n## Execution`, sha256 over UTF-8) over the framework working
   files. Expected: m0012 `21492653…54a747`, m0013 `b0f4810e…12cec5`,
   both matching their frontmatter; `doctrine/matters.md` hashing to
   the declared re-ratification candidate. **Observed: m0012 MATCH,
   m0013 MATCH; doctrine =
   `9fb1f925f37c3533ffff7caba7c1094f5631e098503e06ac569841d0ef1f4c7d`,
   the candidate stated in A2's commit message — m0001's recorded pin
   intentionally no longer matches (R2; pin-follows-the-act: the new
   pin is recorded only after the operator re-ratifies over the exact
   text).**

7. **R1 completeness** — byte search for the former owner string over
   every file in both working trees. Expected: none. **Observed:
   none.**

8. **Commit discipline (§8)** — `git log --format` with trailer
   extraction over `origin/main..HEAD` (framework) and
   `d36ea0f..main` (consumer). Expected: `Matter: m0012` on both
   framework commits, `Matter: m0010` on both consumer commits.
   **Observed: exactly that.**

## Verdict

All eight claims hold at the trees recorded above. Two defects were
found by these checks mid-run and fixed before publication — the five
un-enumerated inbound run-record links (claim 4) and nothing else;
the fix is inside A2 and itemized in the execution record. The one
deliberate red value is m0001's doctrine pin, broken by the
operator-ruled §11 re-pin and awaiting re-ratification over
`9fb1f925…` — the README's three commands will show exactly that
mismatch until the operator's act re-pins it.

- Date: 2026-08-26
- Actor: claude-code/2026-08-26, the dev agent the operator launched
  against m0012 (also this execution's author; every value above is
  recomputable from the named commits — the pins are the independence
  mechanism). Thread:
  [2026-08-26-m0012-execution](../threads/2026-08-26-m0012-execution.md)
