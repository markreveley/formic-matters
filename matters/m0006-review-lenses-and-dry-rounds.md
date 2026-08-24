---
type: feature
title: Structured review lenses and dry-round termination
description: Give each reviewer a distinct lens and terminate vetting on consecutive rounds that surface nothing new.
id: m0006
state: proposed
target: beatcode-dev
implements: m0001
tags: [process]
---

# m0006 · Structured review lenses and dry-round termination

## Feature

Today vetting is "fresh agents review until the operator ratifies"
(doctrine §6). That terminates on operator fatigue, and fresh agents
given the same prompt on the same document converge on the same findings
— round three restates round one, producing the appearance of scrutiny
rather than scrutiny.

Two additions:

**Differentiated lenses.** Each reviewer gets a distinct assignment
rather than a general "review this". For beatcode the natural set is:
determinism and byte-exactness impact · golden and conformance impact ·
spec-consistency (does this contradict another section) · scope (is this
secretly three matters) · what breaks that is not mentioned.

**Dry-round termination.** A round producing no *new* findings is dry.
Two consecutive dry rounds mark the matter review-complete and eligible
for ratification. Dryness is countable, which makes the stopping rule
mechanical rather than a judgment call.

**Anchoring.** First-pass reviewers should not see prior rounds — a
reviewer handed the thread audits the thread instead of the proposal.
One reviewer per round is assigned the opposite job: were prior findings
actually addressed, or only discussed.

## Proposed implementation

Deferred pending design. Depends on [m0008](/m0008-matter-tooling.md)
for round bookkeeping.

## Why this is not built yet

Explicitly deferred by the operator as premature: the pain it addresses
has not been felt. It is filed so that the first time three review rounds
return the same three findings, the response already exists.
