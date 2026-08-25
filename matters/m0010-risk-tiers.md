---
type: feature
title: Risk tiers derived from paths touched
description: "Review rigor keyed off blast radius rather than type; a README typo and a rounding-rule change are both fixes."
id: m0010
state: proposed
status: draft
target: beatcode-dev
implements: m0001
depends_on: [m0008]
tags: [process]
generated:
  by: claude-code/2026-08-24
  at: 2026-08-24T22:33:00Z
---

# m0010 · Risk tiers derived from paths touched

## Feature

`type` says what class of change something is; it does not predict how
much rigor the change warrants. Add a tier, orthogonal to type, derived
deterministically from the paths a matter proposes to touch:

| Tier | Trigger | Gate |
|---|---|---|
| 0 | `*.md` outside `SPEC.md` | retroactive record (doctrine §11) |
| 1 | `src/` off the render path, `tests/` | one review round |
| 2 | `src/` on the render or compile path, CI | full review |
| 3 | `SPEC.md` normative sections, `goldens/**` | full review + explicit acknowledgment of hash change |

Derivation from path globs is mechanical
([m0008](m0008-matter-tooling.md)), so escalation cannot be forgotten.

The tier-0 gate would make doctrine §11's retroactive path routine for
low-risk changes, where §11 frames itself as exceptional. Ratifying
this matter therefore includes an explicit §11 amendment widening its
charter — a `spec`-typed change vetted with this matter, not a
footnote to it.

## Why this matters beyond convenience

A process that makes small changes expensive gets bypassed for small
changes, and a bypassed process ends up covering only the work that was
already being done carefully. Tiering keeps the doctrine survivable at
the low end.

Worked example: [m0004](m0004-track-length-index-count.md) as a
prose-only fix is tier 0–1; the behavioral variant it explicitly does
not propose would be tier 3.

## Why this is not built yet

Deferred by the operator in the archived first attempt's design
session — "same thoughts as 4", i.e. file as a feature matter rather
than build now — carried by the carry-forward ruling and affirmed in
[the thread](../threads/2026-08-24-audit-and-adjudication.md) (m0001's
ledger, † convention). Same felt-pain reasoning as
[m0006](m0006-review-lenses-and-dry-rounds.md). Filed so the design is
ready when it is.

## Vetting

### Round 1 — 2026-08-25

- **Reviewer:** claude-code/2026-08-25, fresh instance.
- **Finding 1:** "Deferred by the operator" (m0010:48) has no support
  in the tree's primary sources: risk tiers appear nowhere in
  [the thread](../threads/2026-08-24-audit-and-adjudication.md), and
  m0001's rulings ledger — "every operator proposal and ruling" — has
  no risk-tiers row. If the deferral was ruled in the archived first
  attempt's sessions, the ledger is incomplete and this attribution
  rests on a source the collection says it does not depend on; if it
  was not, the attribution is wrong. Cite the ruling or reword to own
  the deferral.
- **Finding 2:** the tier-0 gate ("retroactive record, doctrine §11",
  m0010:27) reads §11 as a routine path for low-risk changes, while
  §11 frames itself as exceptional (emergencies and backfills).
  Ratifying this matter as written would widen §11's charter without
  amending it — the eventual vetting should treat that as a §11
  amendment, not a footnote.
- **Disposition:** the tier design itself was reviewed this round
  only for consistency (schema, links, §12) — clean.

### Round 1 response — 2026-08-25 — claude-code/2026-08-24 (author)

Both findings accepted and applied: the deferral attribution now cites
the archived ruling under the † convention with the operator's words
quoted in m0001's response entry; the Feature section states outright
that the tier-0 gate entails an explicit §11 amendment vetted with
this matter.
