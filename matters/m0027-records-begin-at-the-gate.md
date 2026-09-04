---
type: spec
title: Proposed matters are working text — records begin at the gate
description: "While a matter is proposed its text is simply revised — discussion lives in threads, history in git, no review log accretes on the matter; the matter's own record begins at the ratification gate and carries everything after it."
id: m0027
state: proposed
status: draft
tags: [formic-matters, process, review]
implements: m0001
sources:
  - doctrine/matters.md
threads:
  - threads/2026-08-29-complexity-escape-and-working-text.md
generated:
  by: claude-code/2026-08-29
  at: 2026-08-29T04:30:36Z
---

# m0027 · Proposed matters are working text — records begin at the gate

Filed on operator direction in the 2026-08-29 session, exported at
[threads/2026-08-29-complexity-escape-and-working-text.md](../threads/2026-08-29-complexity-escape-and-working-text.md)
and cited in `threads`.

## Diagnosed reason

What happened on 2026-08-29, plainly: m0017 — still `proposed` —
accumulated in one day a review entry describing text that was then
revised away, a second entry explaining that the first entry's main
finding had been dissolved by an operator ruling, and three open
findings waiting for ceremony before one-line fixes could be
applied. None of that made the matter better; all of it made the
matter longer, and the operator — the one person whose acts give the
record force — had to read through it to find the actual text. The
operator's ruling: alter the text directly; ceremony is required
only after ratification.

The reason the ceremony added nothing: for unratified text, the
repository already records everything worth keeping. Git history
preserves every version and who committed it — the diff is the
record. Threads preserve the discussion and rulings that drove the
edits. An append-only review log on the matter duplicates both and
then goes stale the moment the text moves, because the log describes
versions that no longer exist. Append-only recording earns its cost
exactly once text is frozen: after ratification, when the text may
no longer simply be edited, events about it need somewhere to land.

## Proposed text

Amend doctrine §6, “Vetting and ratification,” and §3, “State —
mutable.”

**§6 — while `proposed`, the text is simply revised.** A `proposed`
matter is working text. Review of it produces revisions and thread
discussion, never entries on the matter: a finding the operator
accepts is applied as an edit; one the operator declines stays in
the thread. No `## Vetting` section accretes before the gate. §6's
sentence “Every round is recorded on the matter itself” is scoped to
the gate and after.

**§6 — the matter's own record begins at the ratification gate.**
The `## Vetting` section starts with the gate event under the
mechanism in force — today, the operator's verbal act and its
recording; under [m0017](m0017-operator-authored-ratification.md),
the restatement verification and its recording commit — and from its
first entry onward it is append-only, never rewritten. Everything
after ratification lands there: re-opening (with the cleared
ratification fields, as §3 already requires), discovered divergence,
re-ratification.

**§3 — declined matters keep their why.** On `proposed → rejected`,
the recording agent writes one closing note on the matter carrying
the operator's stated reason; on `proposed → withdrawn`, the
author's. This keeps §3's promise that rejection's record of *why
not* is the artifact, without pre-gate ceremony.

**Nothing else in §3 changes.** The states, the transitions, and
their owners are all untouched.

## What this contradicts

No ratified matter. It scopes one §6 sentence (“Every round is
recorded on the matter itself” — henceforth: from the gate onward)
and adds the two closing-note rules to §3. Records already merged
stay exactly as they are: m0001's accreted vetting history is an
`executed` record, and the vetting sections on older `proposed`
matters (m0006–m0011), written under the prior practice and already
on `main`, are history — they are not rewritten, and they simply
accrete nothing further before their gates.

## Proposed execution plan

1. Amend §6 and §3 as above.
2. Add a standing rule to `CLAUDE.md`: while a matter is `proposed`,
   apply review as edits to the text; record on the matter only from
   the ratification gate onward.
3. Regenerate `matters/index.md` and record a verification run under
   §9.1, “Runs.”
4. Because doctrine changes, re-ratify m0001 over the amendment
   using the ratification mechanism then in force; record the pin
   only after the operator's act.
5. Append this matter's execution record, move it
   `staged → executed`, and put the branch before the operator for a
   merge-commit merge.
