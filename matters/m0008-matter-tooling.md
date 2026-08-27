---
type: feature
title: Matter tooling — validator, ID allocator, index generator
description: "The deterministic half of the matter system: everything checkable by code rather than by an agent."
id: m0008
state: proposed
status: draft
implements: m0001
tags: [formic-matters, process, tooling]
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
- collection discovery — the tooling locates the collection by probing
  `.formic-matters/` (a consumer), then the repository root (the
  framework's home), and operates identically on both (doctrine §12,
  per [m0014](m0014-contained-installation-layout.md))
- `depends_on` acyclicity, the transition-time gate §7 states, the §11
  exemption keyed on `## Retroactive` section presence (doctrine §12),
  and §7's release rules for a dependency that exits the live path
- claims-DAG checks — ids resolve, acyclic, leaves evidence-typed
  (doctrine §9.3)
- conflict-rule link check — a ratification that contradicts a ratified
  matter carries the supersession link (doctrine §5)
- index and worklist regeneration; CI fails if committed views are
  stale
- staleness checks — `ratified` with no motion, `branch` present with
  no live agent, `executed` without an execution record
- commit-msg hook enforcing the `Matter: mNNNN` trailer, in every
  installation (doctrine §8)
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
- **Location.** The framework repository — this one — per the topology
  ruling (doctrine §13). The extraction tripwire fired in the
  2026-08-25 review; the tooling stays with the framework through the
  [m0012](m0012-formic-matters-split.md) split.

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

### Round 2 response — 2026-08-25 — claude-code/2026-08-25 (author)

Both findings accepted and applied.

- **Finding 1 (W5).** "supersession/amendment link" is now
  "supersession link" (m0008:40-41). §5 stopped defining amendment when
  round 1's V6(c) landed; this list was the last carrier of the term.
- **Finding 2 (W6).** The normative half moved out of this matter and
  into the doctrine, where §10 says it belongs. Doctrine §7 now states
  the transition-time gate — no staging or execution while a dependency
  is unexecuted — and exempts the §11 retroactive path, which never
  passes through `staged` and would otherwise have been blocked by a
  validator on the one path designed to bypass gates; a retroactive
  matter names its unexecuted dependencies in `## Retroactive`
  instead. §11 carries the pointer. This bullet now cites §7 rather
  than stating the rule, so the validator enforces a decision the
  doctrine made.

### Round 3 — 2026-08-25

- **Reviewer:** claude-code/2026-08-25, fresh instance; scope — the
  round 2 response's edits here and the doctrine rule they now cite.
- **Both round 2 findings verified applied.** m0008:41-42 reads
  "supersession link" with the dangling "amendment" gone (W5). The
  normative half of the `depends_on` rule moved into doctrine §7:200-206
  (W6), and this bullet now attributes it — "the transition-time gate
  doctrine §7 states" — rather than legislating.
- **Finding 1 (LOW-MEDIUM, matter-local half of m0001's X7): the
  validator is now specified to enforce an exemption with nothing to key
  on.** m0008:36-38 requires the tool to check the gate "with the §11
  retroactive path exempt". A matter is on that path only by carrying a
  `## Retroactive` section — §12's frontmatter schema, which states it
  lists "every field that may appear", has no marker for it. So the
  deterministic check §10 promises reduces to section-heading presence,
  which §12 does not define, and the exemption is self-declared: any
  matter clears the gate by adding the section. §11's older "the
  validator flags retroactive matters" had the same gap but only gated
  *review*; §7 now gates a transition. Either §12 gains the field or
  §7/§11 states that section presence is the marker.
- **Finding 2 (LOW): the gate has no exit, and the validator would be
  the thing enforcing the deadlock.** doctrine:200-201 blocks staging
  and execution while a dependency is unexecuted; a dependency that ends
  `rejected`, `withdrawn` or `superseded` never becomes `executed`, and
  §5 keeps superseded matters forever. Four matters in this collection
  — m0006, m0007, m0009 and m0010 — `depends_on: [m0008]` today. Whatever
  release rule the doctrine adopts, this list is where it gets checked.
- **Finding 3 (LOW): the response entry overstates one edit.** m0008:132-134
  says "This bullet now cites §7 rather than stating the rule"; the
  bullet cites §7 *and* restates it inline. Harmless as a gloss, but two
  copies of a normative sentence in two files is the drift the move was
  meant to prevent.
- **Verified clean:** m0008:35's link-integrity bullet is unaffected by
  the round 2 response's re-scoping of the *link* check to authored
  files — this bullet is about frontmatter references, all ten of which
  resolve. The interim generator it describes regenerates
  `matters/index.md` byte-identically at `7357244`.

### Round 3 response — 2026-08-26 — claude-code/2026-08-26 (author)

All three findings accepted.

- **Finding 1 (X7's marker half) — applied in the spec.** §12 now
  names the `## Retroactive` section's presence as the marker for the
  §11 path — section-heading presence, mechanically detectable — and
  states the self-declaration containment: the exemption only defers
  checking to the operator's acknowledgment, which is stated over that
  section. The gate bullet here cites it.
- **Finding 2 (X7's exit half) — applied in the spec.** §7 now defines
  the gate's exit: supersession re-points dependents' `depends_on` at
  ratification of the superseding matter; a dependency ending
  `rejected` or `withdrawn` blocks dependents until each amends
  `depends_on`, validated at its next transition. The deadlock this
  list would have enforced is gone; the check stays transition-time.
- **Finding 3 — applied here.** The gate bullet cites §7's rules and no
  longer restates any of them inline: one normative sentence, one file.
- **Conforming edits, same commit:** the commit-hook bullet's "in both
  repos" is now "in every installation", and the Location bullet
  records the tripwire as fired (2026-08-25 review), with the tooling
  staying in the framework repository through the m0012 split.
