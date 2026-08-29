---
type: spec
title: The error log — agent errors become citable records
description: "A new errors/ directory holds append-only records of agent errors — what happened, why as far as traceable, and the guard added — with eNNNN IDs that guards in tooling and doctrine cite; e0001, the index-out-of-step slip, is the first entry."
id: m0030
state: proposed
status: draft
tags: [formic-matters, process, integrity, tooling]
implements: m0001
sources:
  - doctrine/matters.md
generated:
  by: claude-code/2026-08-29
  at: 2026-08-29T17:06:10Z
---

# m0030 · The error log — agent errors become citable records

Filed on operator direction in the 2026-08-29 session. That session
is not yet exported as a thread; per the practice
[m0024](m0024-declared-sources.md) proposes, the provenance gap is
held open here and the `threads` cite is added when the export
lands.

## Diagnosed reason

The operator's direction, quoted: "could it be worth creating an
error log, where we document agent errors, what the error was, if
its possible to trace why they happened, and what changes were made
to guard against them?"

Today an agent error lives in three disconnected places: the
mistake itself sits in git history, the explanation is given in
conversation and survives only if the session is exported, and the
guard — a new check, a new practice — lands in tooling or doctrine
with no memory of why it exists. A reader of the guard cannot find
the error; a reader of the error cannot find the guard.

The repository already has the right pattern for this: §9.1,
"Runs" — one file per record, append-only, never edited after the
fact. An error record is the same kind of evidence: something that
happened, written down once, citable forever. With IDs, the link
becomes two-way — the guard cites the error it answers
(`e0001`), and the error names the guard that answers it.

The occasion is concrete: on 2026-08-29 an agent committed the
derived index out of step with the files it indexes (full record
below). The guard is a one-line check added to
[m0008](m0008-matter-tooling.md); this matter is what lets that
check say *why* it exists.

## Proposed text

Amend doctrine §9, "Evidence," with a new subsection. It is
numbered §9.5 and placed after §9.4, "Immutability," so no existing
section number moves and no existing citation breaks.

> ### 9.5 Errors
>
> `errors/` holds append-only error records: one file per error,
> named `eNNNN-slug.md`, IDs zero-padded, allocated sequentially,
> never reused. Each record states: the date and actor; where (the
> commits and files involved); what happened, as observable fact;
> why it happened, traced as far as the evidence allows; how it was
> detected; the impact; and the guard — the change made so it does
> not recur, naming the matter or tool that carries it. An error
> record is never edited after the fact; a correction is a new
> record superseding it. Any agent or the operator files one on
> discovery. Guards cite their error records by ID; the record is
> why the guard exists.

## The first entry

Carried verbatim; it lands as `errors/e0001-index-out-of-step.md`
at execution:

```markdown
# e0001 · Index committed out of step with its files

- **Date:** 2026-08-29
- **Actor:** claude-code/2026-08-29
- **Where:** branch `claude/handoff-item-1-2u2k20`, commit
  `5dda102` ("m0028: file"), file `matters/index.md`
- **What happened:** two matters (m0028, m0029) were written, the
  index generator was run once, and the filings were committed
  separately. The m0028 commit therefore carries index rows and a
  link for m0029, whose file arrives only in the next commit
  (`069bcf2`). Checked out at `5dda102`, the index links a file
  that does not exist.
- **Why, traced:** the generator is manual (`tools/gen-index.py`),
  and the invariant — an index consistent with its own tree in
  every commit — lived only in remembered convention. §12,
  "Storage and format," says views are derived and never
  hand-edited, but nothing bound regeneration to the commit
  boundary; batching two filings around one regeneration produced
  a commit the convention forbids. The branch tip stayed
  consistent, which is why nothing downstream caught it.
- **Detected by:** the authoring agent, on self-review while
  reporting the filings; disclosed to the operator in the same
  session.
- **Impact:** one intermediate commit misleads a history reader;
  nothing on `main`, nothing at the branch tip, no state or record
  damage. History kept unrewritten per standing rule.
- **Guard:** practice — regenerate the index inside every filing
  commit; check — m0008's validator gains a commit-time check that
  refuses any commit whose `matters/index.md` differs from
  regeneration over that commit's own tree. m0008's check bullet
  cites this record.
```

## What this contradicts

No ratified matter. It adds §9.5 beside the existing evidence
kinds; runs, threads, and their rules are untouched. Coordination,
not basis: [m0008](m0008-matter-tooling.md) already carries the
guard check as working text and names e0001 as its record pending
this matter's execution.

## Proposed execution plan

1. Add §9.5 to the doctrine as quoted.
2. Create `errors/e0001-index-out-of-step.md` verbatim from the
   block above.
3. Extend `CLAUDE.md`'s append-only bullet: `threads/`, `runs/`,
   and `errors/` are append-only primary sources.
4. Confirm m0008's index check cites e0001.
5. Regenerate `matters/index.md` and record a verification run
   under §9.1, "Runs."
6. Because doctrine changes, re-ratify m0001 over the amendment
   using the ratification mechanism then in force; record the pin
   only after the operator's act.
7. Append this matter's execution record, move it
   `staged → executed`, and put the branch before the operator for
   a merge-commit merge.
