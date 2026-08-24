---
type: feature
title: Matter tooling — validator, ID allocator, index generator
description: The deterministic half of the matter system: everything that can be checked by code rather than by an agent.
id: m0008
state: proposed
target: beatcode-dev
implements: m0001
tags: [process, tooling]
---

# m0008 · Matter tooling

## Feature

The doctrine asserts that views are derived and that the collection
cannot be corrupted. Both are currently maintained by hand. This is the
code that makes them true.

Deterministic, therefore in scope:

- ID allocation — next free `mNNNN`, never reused
- frontmatter schema validation — required fields, valid enum values
- state-transition legality — reject illegal moves
- required-sections check per `type`, as a gate on ratification (§4)
- link integrity — every matter reference resolves
- `depends_on` cycle detection
- index and worklist regeneration; CI fails if committed views are stale
- staleness checks — `ratified` with no branch, `executed` with the
  matter still open
- commit-msg hook in beatcode requiring a matter ID

Not mechanizable, and not to be faked: whether a diagnosis is correct,
whether a plan is good, whether scope is right, ratification itself.

## Proposed implementation

Open questions the operator has flagged but not settled:

- **Language.** Rust was discussed, on the grounds that a single static
  binary drops into any repo and the toolchain is already pinned. If
  Rust, it must **not** be a workspace member of beatcode — that repo's
  zero-dependency vow is a product claim enforced by an acceptance
  criterion and a banned-token check, not a house style to propagate. The
  tool should take normal dependencies.
- **Location.** This repo for now, given the deliberate beatcode scoping;
  extractable later if a general framework emerges.

## Interim scripts

`tools/gen-index.py` and `tools/export-thread.py` exist now, in Python,
and are disposable. They are in the repo for one reason: the doctrine
asserts that views are derived and never hand-edited (§8), and a claim
whose only executable form lives in a scratch directory is not a claim.

They do a fraction of the list above — index regeneration, thread export
with redaction applied before publication rather than after. They do not
validate schemas, allocate IDs, check transitions, resolve links, detect
cycles, or verify hashes. Nothing depends on them being kept.

## Why this is not built yet

The MVP line is file · query · cannot corrupt. The collection is small
enough to hold by hand today, and the schema is still unratified — code
written against it now would be rewritten after the first review round.
