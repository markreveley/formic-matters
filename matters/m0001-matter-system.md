---
type: spec
title: The matter system
description: Every change to beatcode is proposed, vetted, and ratified as a matter before code is written.
id: m0001
state: executed
target: beatcode-dev
verified:
  - by: human:mark
    at: 2026-08-24
generated:
  by: claude-code/claude-opus-5
  at: 2026-08-24
tags: [doctrine, bootstrap]
---

# m0001 · The matter system

## Diagnosed reason

Changes to beatcode were being identified, diagnosed, and applied in one
unbroken motion, with no gate between noticing a problem and editing the
repo. The session that produced this matter is the evidence: four distinct
findings in `SPEC.md` were diagnosed and committed together, one of them
(see [m0004](/m0004-track-length-index-count.md)) documented as
intended behavior without that intent ever being established.

beatcode is a repository whose thesis is that behavior is pinned in
advance and verified against frozen goldens. Its development process had
no equivalent discipline.

## Proposed text

[`doctrine/matters.md`](../doctrine/matters.md), in full.

Summary of what it fixes:

- A matter is one proposed change, persisted as one file, vetted before
  any code is written.
- `type` (`feature` · `fix` · `refactor` · `spec`) is immutable; `state`
  (`proposed` → `ratified` → `staged` → `executed`) is mutable. The
  earlier sketch conflated the two by making "proposal" a type.
- Filing is cheap; ratification is expensive. Required sections gate
  ratification, not creation.
- The collection is flat. Composition is by `implements` / `depends_on`
  metadata, never by containment. All views are derived.

## What this supersedes

Nothing. This is the first matter.

## Scope held out deliberately

The MVP line is **file · query · cannot corrupt**. Everything beyond it
was deferred to its own matter rather than built now:

- structured review lenses and dry-round termination — [m0006](/m0006-review-lenses-and-dry-rounds.md)
- ratification content hash — [m0007](/m0007-ratification-content-hash.md)
- validator, ID allocator, index generator — [m0008](/m0008-matter-tooling.md)
- risk tiers driving review depth — [m0010](/m0010-risk-tiers.md)

The `org/assertions` question raised in conversation is out of scope: it
concerns the operator's global `CLAUDE.md`, not beatcode, and this repo
is deliberately scoped to one instrument.

## Execution

- `doctrine/matters.md` written
- `matters/` created, this matter filed
- the session's outstanding beatcode findings filed as m0002–m0005
- the deferred process work filed as m0006–m0008, m0010
- `matters/index.md` generated

Ratified by operator instruction in conversation on 2026-08-24, under the
bootstrap exception recorded in `doctrine/matters.md` §10.
