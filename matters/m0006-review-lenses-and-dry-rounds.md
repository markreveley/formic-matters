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

## Vetting

### Round 3 — 2026-08-25

- **Reviewer:** claude-code/2026-08-25, fresh instance; first round with
  the archived first attempt readable. Rounds 1 and 2 filed nothing on
  this matter.
- **Finding 1 (HIGH, matter-local half of m0001's X1): this file is the
  worst instance of archive text reuse in the collection.** 78% of the
  archived `matters/m0006-review-lenses-and-dry-rounds.md` at `c11956d`
  survives here in matching runs of forty characters or more (1457 of
  1870 characters; run record
  [runs/2026-08-25-vetting-round-3.md](../runs/2026-08-25-vetting-round-3.md),
  step 5). The longest single run is 315 characters — m0006:21-25
  against archive m0006:16-20 — and it is authorial prose, not the
  operator's wording and not a fact: "Today vetting is \"fresh agents
  review until the operator ratifies\" (doctrine §6). That terminates on
  operator fatigue, and fresh agents given the same prompt on the same
  document converge on the same findings — round three restates round
  one, producing the appearance of scrutiny rather than scrutiny." Four
  more runs of 122-263 characters cover the lens list, the dry-round
  rule, the anchoring paragraph and Proposed implementation. Against
  this, doctrine:18-19, `README.md`:21-22 and m0001:43-45 all say "none
  of its doctrine or matter text was reused". The claim fails here first.
- **Finding 2 (LOW): the deferral line is now under-cited relative to
  the rest of the collection.** m0006:53-54 says "Explicitly deferred by
  the operator as premature". m0010, answering the same class of finding
  in round 2, gained a turn citation
  ([design:304](../threads/2026-08-24-matter-system.md)) and a ledger
  row. This matter's ruling is
  [design:298](../threads/2026-08-24-matter-system.md) — "this is a pain
  I as an operator have not felt yet … i propose this should be filed as
  a feature matter" — and row 75 of m0001's ledger now cites it, but
  this file does not. Symmetry with m0010:58-68 costs one clause.
- **Verified clean:** frontmatter conforms to §12 and the
  `depends_on: [m0008]` link resolves; the matter's own content — lenses,
  dry-round rule, anchoring — is internally consistent and correctly
  deferred under §6 and §15.
