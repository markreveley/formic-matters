# Run — ratification recording: m0001, m0012, m0013 at 85fe451

Append-only verification record (spec §9.1). Never edited; a
superseding run is a new file. Filed for the ratification recording on
[m0001](../matters/m0001-matter-system.md),
[m0012](../matters/m0012-formic-matters-split.md), and
[m0013](../matters/m0013-bootstrap-defaults-record.md): the operator
stated "I ratify m0001, m0012, and m0013 at commit 85fe451"
([review f1](../threads/2026-08-25-doctrine-operator-review.md)), and
this run is the mechanical half of the §6 recording — pin computation
and its stability checks.

## Claims tested

- The named commit is the text the operator read: `85fe451` resolves
  to a full SHA that is the head of the m0001 branch on the remote at
  recording time.
- The three recorded `ratified_sha256` values are reproducible from
  the named commit by anyone: m0001 under the whole-file regime
  (its proposed text is the separate document `doctrine/matters.md`),
  m0012 and m0013 under the ratified-region regime.
- The recording itself moved no ratified byte: after writing the
  frontmatter records and appending the `## Vetting` ratification
  entries, every working file's pinned content still hashes to its
  recorded pin.
- Tree invariants survive the recording: the index regenerates
  byte-identically with the three state changes (m0001 `executed`,
  m0012/m0013 `ratified`, status derived); every relative link in
  authored files resolves; every `review <label>` citation (now
  including `k`, `f1`, `f2`) resolves in the thread; the in-situ
  excerpts remain byte-exact against `9c1d295`.

## Environment

- OS: Linux 6.18.44-fc-v21, x86_64 (remote agent container)
- bash 5.2.21(1)-release; git 2.43.0; GNU coreutils 9.4
  (`sha256sum`); Python 3.11.15, PyYAML 6.0.1
- Repo: `markreveley/formic-matters`, the m0001 lineage (PR #2 head), parent
  commit `85fe451` — the ratified commit itself; the tree verified is
  this recording's, in which this run file lands

## The region rule, stated exactly

For m0012 and m0013 the pinned region is: the file content after the
frontmatter's closing `---` line, cut at the first `\n## Vetting` or
`\n## Execution` occurrence if one exists, hashed as UTF-8 with no
other normalization. At `85fe451` neither file carries either heading,
so the region is the whole body. This rule is what makes the
post-ratification `## Vetting` appends below hash-neutral, and it is
the rule m0007's checker should implement.

## Commands and results

1. **Head verification:**

   ```
   git fetch origin claude/beatcode-pr1-vetting-round-2-pbyiud
   git rev-parse origin/claude/beatcode-pr1-vetting-round-2-pbyiud
   git rev-parse 85fe451
   ```

   Expected: both resolve identically. **Observed: both
   `85fe4511326a30516ed2bf86a2e2a2b9d05c3d25`.** Statement received
   and recorded at 2026-08-26T05:21:39Z.

2. **Pin computation at the named commit:**

   ```python
   import hashlib, subprocess
   COMMIT = "85fe4511326a30516ed2bf86a2e2a2b9d05c3d25"
   def region(text):
       body = text[text.index("\n---\n", 3) + 5:]
       cuts = [i for i in (body.find("\n## Vetting"),
                           body.find("\n## Execution")) if i != -1]
       return body[:min(cuts)] if cuts else body
   def at(path):
       return subprocess.run(["git", "show", f"{COMMIT}:{path}"],
                             capture_output=True, text=True,
                             check=True).stdout
   sha = lambda t: hashlib.sha256(t.encode("utf-8")).hexdigest()
   print(sha(at("doctrine/matters.md")))
   print(sha(region(at("matters/m0012-formic-matters-split.md"))))
   print(sha(region(at("matters/m0013-bootstrap-defaults-record.md"))))
   ```

   **Observed, recorded into the three frontmatters:**

   - m0001 (whole file, `doctrine/matters.md`):
     `5adc0aafe92c5ead0269c681c8802516572765cf77b22549ea5acc45d8dda7bd`
     — cross-checked against the README's operator-side form,
     `git show 85fe451:doctrine/matters.md | sha256sum`, identical.
   - m0012 (ratified region):
     `21492653902313ce826b53ef895b43e519eb898e7ff4a3afb69dbbe3ab54a747`
   - m0013 (ratified region):
     `b0f4810ec3149b27416b1d18228681fb8ebf66d6060660304b796e7d7b12cec5`

3. **Post-recording stability.** After the frontmatter records, the
   `## Vetting` ratification entries on m0012/m0013, m0001's Execution
   completion, and the thread/README/ledger updates, the working
   files' pinned content was re-hashed with the same rule. Expected:
   all three match their recorded pins. **Observed: MATCH, MATCH,
   MATCH** — `doctrine/matters.md` untouched byte-for-byte, and both
   appends fell outside the region as the rule intends.

4. **Tree invariants.** `python3 tools/gen-index.py` regenerates
   `matters/index.md` byte-identically on a second run — 13 matters,
   grouped 1 `executed` (m0001), 2 `ratified` (m0012, m0013), 10
   `proposed` (m0002–m0011); status derivation enforced in the same
   pass. Link check over authored files: all relative links resolve,
   none leading-slash. Label check: every `review` citation,
   `k`/`f1`/`f2` included, resolves in the thread. Excerpt check: 19
   blocks byte-exact against `9c1d295`, comment lines in situ.

## Verdict

The act is recorded and every mechanical claim reproduces. Anyone can
re-verify without trusting this record: the three commands in the
README against `ratified_commit` and `ratified_sha256` on each matter.

- Date: 2026-08-26
- Actor: claude-code/2026-08-26, the recording agent (also the round-2
  response author; the pins are the independence mechanism — every
  value above is recomputable from the named commit)
