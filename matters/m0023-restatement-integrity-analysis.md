---
type: feature
title: Restatement integrity analysis against the thread corpus
description: "An advisory integrity check on operator restatements — LLM-as-judge and consistency analysis against the operator's verbatim turns in threads/ — that emits vetting findings and can never gate or grant ratification."
id: m0023
state: proposed
status: draft
tags: [formic-matters, process, integrity, ratification]
implements: m0001
depends_on: [m0017]
threads:
  - threads/2026-08-28-restate-to-ratify.md
generated:
  by: claude-code/2026-08-28
  at: 2026-08-28T20:08:20Z
---

# m0023 · Restatement integrity analysis against the thread corpus

Filed on operator direction.

## Feature

The restatement mechanism
([m0017](m0017-operator-authored-ratification.md)) holds its identity
boundary by channel rule: agents never author the operator section,
and Git author metadata cannot prove a human wrote a commit. m0017
names the strengthening options and requires none. This matter owns
one of them.

The repository already carries the reference corpus that makes the
check nearly free: every file in `threads/` is a verbatim session
export (doctrine §9.2, “Threads”), and its human turns are the
operator's own prose, accumulating as a byproduct of the process. The
feature is an agent-run integrity analysis of restatement text against
that corpus:

- **consistency analysis** — vocabulary, register, and structural
  habits of the restatement compared with the operator's verbatim
  turns; and
- **LLM-as-judge assessment** — whether the restatement reads as the
  operator's interpretation or as generated text lightly edited.

Run at two points: during m0017's draft review, as one more input to
the fresh reviewer; and retrospectively, over the accumulated
`## Operator ratification` corpus, as an operator-invocable sweep. In
both forms the output is an advisory finding — the signal, the
reference turns consulted, and the confidence — appended as a
`## Vetting` entry or recorded as a run.

Bounds, stated as part of the feature:

- **Advisory only.** The analysis cannot block, grant, or substitute
  for ratification; no state transition keys off it. The operator and
  reviewers read findings. A clean result proves nothing — it is
  evidence, never proof, under m0017's evidence boundary.
- **The channel rule holds.** Findings are appended; the analysis
  never rewrites or supplies wording for the operator section.
- **Honest limits travel with every finding:** generated-text
  detection is unreliable in general, the operator's own style drifts
  over time, and operator-edited agent text is a gray zone. The value
  is the tripwire and the record, not a verdict.

## Proposed implementation

1. Define the reference-corpus extraction: the human turns of every
   export in `threads/` (whose scope and mechanics are
   [m0011](m0011-thread-persistence.md)'s subject).
2. Define the review-time form: the analysis runs inside the fresh
   draft review m0017 requires, and its finding lands in that review's
   `## Vetting` entry.
3. Define the retrospective sweep: operator-invoked, whole restatement
   corpus against the whole thread corpus, recorded under doctrine
   §9.1, “Runs.”
4. Nothing here is deterministic tooling: this is judgment work,
   reserved to agents per doctrine §10, “Deterministic wherever
   possible,” and the validator ([m0008](m0008-matter-tooling.md))
   carries none of it.

## Why this is not built yet

There is no restatement corpus to analyze: m0017 is `proposed`, and
the check earns its keep only after restatements accumulate. Filed now
so the design is owned rather than re-derived — the pattern of
[m0006](m0006-review-lenses-and-dry-rounds.md) and
[m0010](m0010-risk-tiers.md) — and so m0017's pointer to a
strengthening path names a matter instead of a possibility.
