---
type: feature
title: Matter tooling — validator, ID allocator, index generator
description: "The deterministic half of the matter system: everything checkable by code rather than by an agent."
id: m0008
state: proposed
status: draft
target: beatcode-dev
implements: m0001
tags: [process, tooling]
generated:
  by: claude-code/2026-08-24
  at: 2026-08-24T22:33:00Z
---

# m0008 · Matter tooling

## Feature

Doctrine §10 commits this process to checking by code whatever code can
check. This is that code. Deterministic, therefore in scope:

- frontmatter parsing with a **real YAML parser** — the archived first
  attempt shipped a matter whose frontmatter was invalid YAML, masked
  by a line-splitting parser; that class of defect must fail loudly
- schema validation — required fields, enum values, quoting hazards
  (doctrine §12)
- ID allocation — next free `mNNNN`, never reused
- state-transition legality, including `staged → proposed` on execution
  failure (doctrine §3)
- `status` derived from `state`, never hand-set (doctrine §12)
- required-sections check per `type`, as the ratification gate
  (doctrine §4)
- ratification-hash verification ([m0007](m0007-ratification-content-hash.md))
- link integrity — every matter, thread, and run reference resolves
- `depends_on` acyclicity, and its transition-time enforcement — a
  matter cannot be staged or executed while a dependency is unexecuted
- claims-DAG checks — ids resolve, acyclic, leaves evidence-typed
  (doctrine §9.3)
- conflict-rule link check — a ratification that contradicts a ratified
  matter carries the supersession/amendment link (doctrine §5)
- index and worklist regeneration; CI fails if committed views are
  stale
- staleness checks — `ratified` with no motion, `branch` present with
  no live agent, `executed` without an execution record
- commit-msg hook enforcing the `Matter: mNNNN` trailer, in both repos
  (doctrine §8)
- `runs/` schema check (doctrine §9.1)

Not mechanizable, and not to be faked: whether a diagnosis is correct,
whether a plan is good, whether scope is right, ratification itself.

## Proposed implementation

Open sub-questions, to settle during vetting:

- **Language.** Rust fits — one static binary, toolchain already
  pinned — but it must **not** be a workspace member of beatcode: that
  repo's zero-dependency vow is a product claim enforced by an
  acceptance criterion, not a house style to propagate. The tool takes
  normal dependencies.
- **Location.** This repository, per the topology ruling (doctrine
  §13); extractable when the tripwire fires.

## Interim script

`tools/gen-index.py` exists now, in Python with PyYAML, and is
disposable. It is in the repo because the doctrine asserts views are
derived (§12), and a claim whose only executable form lives in a
scratch directory is not a claim. It does index regeneration with real
YAML parsing and the state→status consistency check — a fraction of the
list above. Nothing depends on keeping it.

## Why this is not built yet

The MVP line is file · query · cannot corrupt. The collection is small
enough to hold by hand, and the schema is freshly authored — code
written against it before the doctrine is ratified would be rewritten
after the first review round.
