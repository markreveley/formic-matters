---
type: feature
title: Risk tiers derived from paths touched
description: Review depth should key off blast radius, not off type; a doc typo and a rounding-rule change are both fixes.
id: m0010
state: proposed
target: beatcode-dev
implements: m0001
depends_on: [m0008]
tags: [process]
---

# m0010 · Risk tiers derived from paths touched

## Feature

`type` says what class of change something is. It does not predict how
much rigor the change warrants: a README typo and a change to the decimal
rounding rule are both `fix`.

Add a tier, orthogonal to type, derived deterministically from the paths
a matter proposes to touch:

| Tier | Trigger | Gate |
|---|---|---|
| 0 | `*.md` outside `SPEC.md` | retroactive record |
| 1 | `src/` off the render path, `tests/` | one review round |
| 2 | `src/` on the render or compile path, CI | full review |
| 3 | `SPEC.md` normative sections, `goldens/**` | full review + explicit acknowledgment of hash change |

Derivation from path globs is mechanical, so escalation cannot be
forgotten.

## Why this matters beyond convenience

A process that makes small changes expensive gets bypassed for small
changes, and a bypassed process ends up covering only the work that was
already being done carefully. Tiering is what keeps the doctrine
survivable at the low end.

## Notes

Raised in conversation, not ruled on. [m0004](/m0004-track-length-index-count.md)
would be tier 3 under this scheme.
