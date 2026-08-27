# Run — m0014 re-execution: pin, amendment stability, probe

Append-only verification record (spec §9.1). Never edited; a
superseding run is a new file. Filed for the re-execution of
[m0014](../matters/m0014-contained-installation-layout.md) after its
recorded execution failure, ratified by the operator at `125dff7`
([execution thread R12](../threads/2026-08-26-m0012-execution.md)).

## Claims tested

- The re-ratification pin is reproducible at the operator's named
  commit and stable under the recording appends.
- The amendment moved no other pinned byte: m0012 and m0013 region
  pins still match.
- The amended `doctrine/matters.md` hashes to the declared
  re-ratification candidate.
- The generator's collection probe works on both forms and the index
  regenerates byte-identically at the framework's root form.

## Environment

- OS: Linux 6.18.44-fc-v21, x86_64 (remote agent container)
- bash 5.2.21(1)-release; git 2.43.0; GNU coreutils 9.4
  (`sha256sum`); Python 3.11.15, PyYAML 6.0.1
- Repo: `markreveley/formic-matters`, branch `m0014-execution` —
  failure commit `b031b3e`, name-expunge commit `125dff7` (the
  ratified commit), amendment commit `1ac3b32`; the tree verified is
  this run's, in which this file lands

## Commands and results

1. **The named commit and its text.** `git show
   125dff7:matters/m0014-contained-installation-layout.md` diffed
   against the working file at recording time: identical. Region rule
   (body after the frontmatter's closing `---`, cut at the first
   `\n## Vetting` / `\n## Execution`, sha256 over UTF-8) at
   `125dff7`:
   **`bc56f0092954d5115e477bcf9106e3109084679194571fcddeade056dec4dc05`**,
   recorded into the frontmatter. Recomputed after the
   re-ratification, re-staging, and execution-record appends:
   **MATCH.**

2. **Neighbor pins.** m0012 and m0013 region pins over the working
   tree after the amendment: **both MATCH** (`21492653…54a747`,
   `b0f4810e…12cec5`).

3. **The re-ratification candidate.** `sha256sum doctrine/matters.md`
   after the amendment:
   **`e55dd508d7048789a43a2f98e403366da11b1a4f6f14d0bff2766438d98a7381`**
   — the value the operator's post-merge re-ratification pins onto
   m0001. m0001's recorded pin (`9fb1f925…` at `97854b8…`)
   intentionally no longer matches the working file until that act.

4. **The probe, both forms.** Root form: `python3 tools/gen-index.py`
   twice from the repo root — `9 matters indexed`, byte-identical
   second run. Contained form: a scratch tree holding one matter and
   the amended generator under `.formic-matters/` — the probe found
   the container, indexed `1 matters`, and wrote
   `.formic-matters/matters/index.md`. **Observed: both as
   expected.**

## Verdict

All four claims hold. The consumer-only container clause is live in
the specification with every neighbor pin undisturbed; the one
deliberate red value is m0001's doctrine pin, awaiting the operator's
re-ratification over `e55dd508…` at the PR #7 merge.

- Date: 2026-08-27
- Actor: claude-code/2026-08-26, the dev agent the operator launched
  against m0014 (also the re-execution's author; the pins are the
  independence mechanism). Thread:
  [2026-08-26-m0012-execution](../threads/2026-08-26-m0012-execution.md)
