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

## Why this matters beyond convenience

A process that makes small changes expensive gets bypassed for small
changes, and a bypassed process ends up covering only the work that was
already being done carefully. Tiering keeps the doctrine survivable at
the low end.

Worked example: [m0004](m0004-track-length-index-count.md) as a
prose-only fix is tier 0–1; the behavioral variant it explicitly does
not propose would be tier 3.

## Why this is not built yet

Deferred by the operator with the same reasoning as
[m0006](m0006-review-lenses-and-dry-rounds.md): felt pain first. Filed
so the design is ready when it is.
