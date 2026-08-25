---
type: feature
title: Drift enforcement for the ratification hash
description: "Tooling that verifies ratified_sha256 before execution, so ratified text cannot drift unnoticed between ratification and the dev agent's first action."
id: m0007
state: proposed
status: draft
target: beatcode-dev
implements: m0001
depends_on: [m0008]
tags: [process, integrity]
generated:
  by: claude-code/2026-08-24
  at: 2026-08-24T22:33:00Z
---

# m0007 · Drift enforcement for the ratification hash

## Feature

Doctrine §6 already *records* ratification against exact text:
`verified`, `ratified_commit`, `ratified_sha256`. What does not yet
exist is the mechanical *enforcement*: nothing today stops a matter
from being edited after ratification and faithfully executed as a plan
no one approved.

Build the check:

- a tooling subcommand that recomputes the matter's hash and compares
  it to `ratified_sha256`, failing loudly on mismatch;
- a dev agent's **first action** on a staged matter is that check; on
  mismatch it refuses and the matter goes back through re-ratification
  (`staged → proposed`, doctrine §3);
- frontmatter-only lifecycle transitions after ratification
  (`ratified → staged → executed`, vetting appendices, execution
  record) must not invalidate the hash — define the hashed region
  accordingly (body-only, or body plus a frozen subset of fields) and
  record the choice in doctrine §6 when this matter executes.

Fully deterministic; small once [m0008](m0008-matter-tooling.md)
exists.

## Why this exists

The archived first attempt's central failure was exactly this drift, at
the bootstrap itself: a doctrine marked ratified that the operator had
not read, and an execution summary that misdescribed the committed
text. The recording half of the fix is already in doctrine §6; this
matter is the enforcement half.

## Vetting

### Round 1 — 2026-08-25

- **Reviewer:** claude-code/2026-08-25, fresh instance.
- **Finding 1:** §6 (doctrine/matters.md:144) defines
  `ratified_sha256` as a whole-file hash, and the recording act
  itself — writing `verified`/`ratified_commit`/`ratified_sha256`
  into the frontmatter — edits the file the moment ratification
  happens. The check as described here (m0007:29-30, recompute and
  compare) can therefore never pass against the working file; it can
  only pass by recomputing at `ratified_commit`. The hashed-region
  bullet (m0007:33-38) treats the region definition as a choice to
  record at execution; it is a prerequisite for the check to be
  implementable at all. State that, or move §6 to a defined region up
  front.
- **Finding 2:** the same bullet plans to "record the choice in
  doctrine §6 when this matter executes" — a change to normative
  doctrine text, which §2 types as `spec`, executed from inside a
  `feature` matter. Either that edit ships as its own `spec` matter
  at execution time, or this matter should say why the §2 boundary
  does not apply.
- **Disposition:** the feature is sound; both findings are text edits
  at vetting.
