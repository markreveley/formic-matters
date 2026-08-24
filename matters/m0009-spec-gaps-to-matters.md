---
type: spec
title: SPEC-GAPS becomes a derived view over matters
description: The nine SPEC-GAPS entries are landed matters; the file should be regenerated from them, not maintained by hand.
id: m0009
state: proposed
target: beatcode
depends_on: [m0008]
tags: [spec, process]
---

# m0009 · SPEC-GAPS becomes a derived view over matters

## Diagnosis

`SPEC-GAPS.md` in beatcode is already matters-shaped: nine numbered
entries, each a section citation, a decision, and a rationale. It is the
same artifact as a `spec` matter in state `executed`, maintained in a
parallel format.

Left as-is there are two collections recording decisions about beatcode,
which will drift.

## Proposed text

- Each SPEC-GAPS entry becomes a `spec` matter, filed directly in
  `executed` via the retroactive path (doctrine §9, open).
- `SPEC-GAPS.md` is **regenerated** from `type: spec, state: executed,
  tags: [gap]` rather than deleted.

Regenerating rather than shredding preserves the thing that makes the
file valuable — one readable document for someone building from
`SPEC.md` — while making it derived, consistent with doctrine §8.

## Dependency

Needs the retroactive path designed (doctrine §9) and index generation
([m0008](/m0008-matter-tooling.md)). Filing nine matters by hand
without either is churn.
