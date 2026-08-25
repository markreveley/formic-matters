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

## Vetting

### Round 2 — 2026-08-25

- **Reviewer:** claude-code/2026-08-25, fresh instance; scope — was
  round 1 addressed, or only discussed? Round 1 filed no finding on
  this matter; both entries below are consequences of round 1 fixes
  applied elsewhere in `7022aad..981b2a6`.
- **Finding 1 (LOW-MEDIUM): the validator is specified against a
  mechanism the doctrine no longer defines.** m0008:40-41 still reads
  "conflict-rule link check — a ratification that contradicts a
  ratified matter carries the supersession/**amendment** link (doctrine
  §5)". The response commit dropped "or amended" from §5
  (doctrine:140-142) in answer to round 1's V6(c) — which found exactly
  this: amendment names nothing defined anywhere. §5 is now clean and
  this line is the last carrier of the dangling term, four lines below
  a bullet the same commit edited. Recorded on m0001 as W5.
- **Finding 2 (LOW-MEDIUM): a normative rule arrived here that belongs
  in the doctrine, and it is unreconciled with §11.** The response
  answered V6(g) by adding transition-time `depends_on` enforcement to
  this list (m0008:36-37, "a matter cannot be staged or executed while
  a dependency is unexecuted"). Doctrine §7:183 still calls
  `depends_on` an "execution-order constraint" with no transition rule
  and §3 names no dependency gate, so the validator is specified to
  enforce a rule the normative text does not state — the inverse of
  doctrine §10, which reserves code for what doctrine has decided. The
  rule also has no §11 exception: the retroactive path exists for work
  that "cannot wait" (doctrine:264) and reaches `executed` without ever
  passing through `staged`, so a retroactive matter carrying a
  `depends_on` would be blocked by the validator on the one path
  designed to bypass gates. Recorded on m0001 as W6.
- **Verified clean:** the rest of the response's edit here — splitting
  the acyclicity and claims-DAG bullets apart (m0008:36-39) — is
  faithful to the V6(g) bullet in m0001's response entry and breaks
  nothing else in the list.
