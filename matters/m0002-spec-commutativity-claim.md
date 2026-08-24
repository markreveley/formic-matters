---
type: fix
title: SPEC justifies fixed ordering with a false claim about commutativity
description: SPEC.md §1.1 and §9.3 both say float addition "does not commute"; commutativity is not what fails.
id: m0002
state: proposed
target: beatcode
tags: [spec, determinism]
---

# m0002 · SPEC justifies fixed ordering with a false claim

## Diagnosis

Two sites in `SPEC.md` justify order-sensitivity with the same incorrect
statement:

- §1.1 — "transforms do not commute; the order is spec"
- §9.3 — "Order is normative: float addition does not commute in
  rounding, so overlapping events must be summed in exactly this order."

IEEE-754 addition **is** commutative: for non-NaN operands `a + b` and
`b + a` produce identical results, sign of zero included. What fails is
**associativity** — `(a + b) + c ≠ a + (b + c)`. Permuting a summation
changes the result because it re-associates it, not because addition is
order-dependent in two operands.

The conclusions drawn at both sites are correct. The stated reason is
not. §9.3 is normative text a reimplementer reads to decide which
reorderings are safe, so a wrong reason there can license a wrong
optimization.

## Proposed fix

Restate both sites in terms of associativity. §9.3 becomes: float
addition is commutative but not associative, so any permutation of
overlapping events re-associates the sum and changes its rounding.

## Notes

A draft of this change exists on the unmerged branch
`docs/pipeline-order-clarity` in beatcode (commit `b204274`, not on
`main`, not pushed). That branch is evidence, not a deliverable — it was
written before this process existed. Execution should re-derive from this
matter once ratified.
