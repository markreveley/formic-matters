# Run — m0014 execution: ratification pin, amendment stability, probe

Append-only verification record (spec §9.1). Never edited; a
superseding run is a new file. Filed for the execution of
[m0014](../matters/m0014-contained-installation-layout.md), ratified
by the operator at `cb44d7e` and launched in the same turn
([execution thread R9](../threads/2026-08-26-m0012-execution.md)).

## Claims tested

- The ratification pin is reproducible at the operator's named commit
  and stable under the lifecycle appends this execution made.
- The specification amendment moved no other pinned byte: m0012 and
  m0013 region pins still match; m0014's own pin still matches after
  its `## Vetting` and `## Execution` sections landed.
- The amended `doctrine/matters.md` hashes to the declared
  re-ratification candidate.
- The interim generator's installation-form probe works on both
  forms, and the index regenerates byte-identically at the root form.

## Environment

- OS: Linux 6.18.44-fc-v21, x86_64 (remote agent container)
- bash 5.2.21(1)-release; git 2.43.0; GNU coreutils 9.4
  (`sha256sum`); Python 3.11.15, PyYAML 6.0.1
- Repo: `markreveley/formic-matters`, branch `m0014-execution` off
  `main` at `1e12e5a` (the PR #6 merge); the tree verified is this
  run's, in which this file lands

## Commands and results

1. **The named commit and its text.** `git merge-base --is-ancestor
   cb44d7e981d6f17b7349ede9cbca4b39054fa648 origin/main` succeeds,
   and `diff` of the matter at `cb44d7e` against `origin/main`'s copy
   is empty — the operator's named commit is reachable and its text
   is `main`'s text. **Observed: both hold.**

2. **Pin computation and stability.** The §6 region rule (body after
   the frontmatter's closing `---`, cut at the first `\n## Vetting` /
   `\n## Execution`, sha256 over UTF-8) at `cb44d7e`:
   **`277c270cb6c5a66bf54c0799775df4f2b565d84b350e50cb4b312a8ab5190b3e`**,
   recorded into the frontmatter. Recomputed over the working file
   after the ratification entry, staging entry, and execution record
   were appended: **MATCH** — the appends fell outside the region as
   the rule intends.

3. **Neighbor pins.** m0012 and m0013 region pins recomputed over the
   working tree after the §12/§14 amendment: **both MATCH**
   (`21492653…54a747`, `b0f4810e…12cec5`).

4. **The re-ratification candidate.** `sha256sum doctrine/matters.md`
   after the amendment:
   **`b61ea861ecba1c83f3fa0b1a12ec0b930e068f6f8cdd73517bc1e51365b03497`**
   — the value the operator's post-merge re-ratification pins onto
   m0001, per the recorded practice. m0001's recorded pin
   (`9fb1f925…` at `97854b8…`) intentionally no longer matches the
   working file until that act.

5. **The probe, both forms.** Root form: `python3 tools/gen-index.py`
   twice from the repo root — `9 matters indexed`, byte-identical
   second run. Contained form: a scratch tree holding one matter and
   the amended generator under `.formic-matters/` — the probe found
   the container, indexed `1 matters`, and wrote
   `.formic-matters/matters/index.md`. **Observed: both as
   expected.**

## Verdict

All four claims hold. The amendment is live in the specification with
every neighbor pin undisturbed; the one deliberate red value is
m0001's doctrine pin, awaiting the operator's re-ratification over
`b61ea861…` at the PR #7 merge.

- Date: 2026-08-26
- Actor: claude-code/2026-08-26, the dev agent the operator launched
  against m0014 (also the execution's author; the pins are the
  independence mechanism). Thread:
  [2026-08-26-m0012-execution](../threads/2026-08-26-m0012-execution.md)
