---
type: spec
title: SPEC states order-sensitive rules without their mechanisms
description: Several normative rules are asserted without the reasoning that makes them checkable, starting with the §1.1 timing pipeline.
id: m0003
state: proposed
target: beatcode
depends_on: [m0002]
tags: [spec, clarity]
---

# m0003 · SPEC states order-sensitive rules without their mechanisms

## Diagnosis

`SPEC.md` pins several behaviors whose *reason* is what stops a
reimplementer from silently breaking byte-exactness, and states them
without that reason.

The clearest case is §1.1. The timing pipeline is drawn as

```
grid → swing → time-lane → humanize → performed_s
```

which reads as function composition. The implementation
(`src/events.rs:196`) is a fan-out plus an ordered sum: each transform
reads the *pristine* rational `grid` and returns an f64 offset, and the
offsets are summed left-to-right. The diagram cannot convey that, so
"the order is spec" is unfalsifiable as written.

Four things make the order normative, none of them stated:

1. Every transform is grid-keyed — swing fires only where `grid ÷ sub` is
   an odd integer (§6.5), lanes index `floor_i(grid ÷ div)` (§6.3). Feed
   either a shifted clock and swing stops matching while lane indices
   slide. Humanize is order-invariant because it keys off the step index.
2. Float non-associativity ([m0002](/m0002-spec-commutativity-claim.md)).
3. The clamp is terminal, not per-stage (§6.9), and the itemized ms
   fields survive it.
4. `to_f(grid)` is the only rational→float edge (§3).

Same pattern elsewhere: §1.4 is ten determinism rules in one
semicolon-joined paragraph with no statement of what each one closes off;
§4.4 asserts the `2^64 − 2^10` threshold without deriving it from the f64
ulp near 2^64; §6.5 gives the MPC swing formula with 50/66⅔ as constants
to memorize rather than as consequences of the expression.

## Proposed text

Add the mechanism at each site, cross-linked to the section that carries
the normative statement. Scope: §1.1, §1.4, §4.4, §6.5. Explanatory
additions only — no normative behavior changes.

## What this contradicts

Nothing. It is additive.

## Notes

Drafted on the unmerged branch `docs/pipeline-order-clarity` (see
[m0002](/m0002-spec-commutativity-claim.md)). Re-derive from this
matter after ratification.
