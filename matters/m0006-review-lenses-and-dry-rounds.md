---
type: feature
title: Structured review lenses, dry-round termination, anchoring rules
description: "Give each reviewer a distinct lens, terminate vetting on consecutive rounds that surface nothing new, and keep first-pass reviewers unanchored."
id: m0006
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

# m0006 · Structured review lenses, dry-round termination, anchoring rules

## Feature

Today vetting is "fresh agents review until the operator ratifies"
(doctrine §6). That terminates on operator fatigue, and fresh agents
given the same prompt on the same document converge on the same
findings — round three restates round one, producing the appearance of
scrutiny rather than scrutiny.

Three additions, when the pain arrives:

**Differentiated lenses.** Each reviewer gets a distinct assignment.
The natural set for this project: determinism and byte-exactness
impact · golden and conformance impact · spec-consistency (does this
contradict another section or another matter) · scope (is this secretly
three matters) · what breaks that is not mentioned.

**Dry-round termination.** A round producing no *new* findings is dry.
Two consecutive dry rounds mark the matter review-complete and eligible
for ratification. Dryness is countable, so the stopping rule is
mechanical.

**Anchoring rules.** First-pass reviewers do not see prior rounds — a
reviewer handed the thread audits the thread instead of the proposal.
One reviewer per round gets the opposite assignment: were prior
findings actually addressed, or only discussed.

## Proposed implementation

Deferred pending design. Depends on
[m0008](m0008-matter-tooling.md) for round bookkeeping and on the
vetting-record format of doctrine §6.

## Why this is not built yet

Explicitly deferred by the operator as premature: the pain it addresses
has not been felt. Filed so that the first time three review rounds
return the same three findings, the response already exists.
