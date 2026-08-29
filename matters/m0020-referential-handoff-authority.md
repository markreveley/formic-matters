---
type: fix
title: Referential handoff launches and delegated authority
description: "Let an operator adopt one explicit handoff action by reference while distinguishing operator-only lifecycle acts from agent-performed repository mechanics."
id: m0020
state: proposed
status: draft
tags: [formic-matters, process, execution, authority, handoff]
implements: m0001
depends_on: [m0017]
threads:
  - threads/2026-08-28-handoff-launch-authority.md
generated:
  by: codex/2026-08-28
  at: 2026-08-28T08:25:37-07:00
---

# m0020 · Referential handoff launches and delegated authority

## Diagnosis

The proposed launch policy in
[m0016](m0016-launch-instructions-policy.md) requires a launch to
identify the repository, matter, operator act, and necessary external
authority. The proposed durable handoff in
[m0019](m0019-fresh-context-durable-handoffs.md) already requires a
complete next launch pointer. Read literally together, however, they do
not say whether the operator may adopt that pointer by reference or
must restate it in every new session.

The ambiguity produced two avoidable failures in the session preserved
as this matter's thread. First, the agent required the operator to
repeat `vet m0017` even though `handoff.md` already named that action.
Second, the agent described merging a filing PR as an operator-only
action. Doctrine §3, “State — mutable,” reserves specified lifecycle
transitions to the operator, while doctrine §8, “Where discourse
lives,” describes pull requests as transport and merge mechanics. The
ratified execution precedent also records an agent performing a merge
on the operator's word
([execution thread R13](../threads/2026-08-26-m0012-execution.md)).
Ownership of a lifecycle act had been conflated with authorization to
perform repository mechanics.

The agent corrected the filing merges once challenged, but the system
should make the distinction locally obvious. A handoff must remain
incapable of granting authority to itself while still allowing a short
operator launch to adopt exactly one fully described action from it.

## Proposed fix

### Referential launch in m0016

Revise m0016 while it remains proposed so its launch rule states:

- A launch may identify its repository, matter, operator act, and
  external authority directly, or by explicitly referring to one
  verified `Next action` record in the collection's `handoff.md`.
- `Proceed from handoff.md in <repository>` is the operator's act of
  adopting exactly that one record, including its permitted operations
  and stop boundary. It does not adopt the remaining queue, authorize a
  future action, or turn the handoff into authority.
- Before acting, the launched agent verifies that the referenced
  handoff is on the intended branch, checks its observed commit against
  current repository and external state, and resolves the named matter.
  A stale, missing, ambiguous, or non-conforming record is a stop and a
  report, not permission to infer the operator's intent.
- If the record calls for an operator-only lifecycle act, the
  referential launch cannot delegate it. The agent presents the act and
  stops for the operator.

Revise m0016's external-authority rule to state explicitly:

- Ownership of a lifecycle act and authorization to perform mechanics
  are separate. Ratification, staging, re-opening, rejection, and
  supersession remain with the owners assigned by doctrine §3, “State
  — mutable.”
- An agent may push a branch, open a pull request, or trigger its merge
  when the operator has authorized that operation. Performing the
  operation does not itself ratify, stage, or imply any other lifecycle
  transition.
- The authorization may be stated directly or adopted through a
  conforming next-action record. Its stop boundary controls what the
  agent may do after the operation.

Carry both distinctions into m0016's proposed doctrine and
`CLAUDE.md` execution targets; do not leave them only in explanatory
prose.

### Action classification in m0019

Revise m0019 while it remains proposed so every current `Next action`
record contains:

- **classification:** exactly one of `operator act required`,
  `operator authorization required`, or `agent operation already
  authorized`;
- **repository and matter:** the collection and one matter ID;
- **action:** one lifecycle or workflow action;
- **permitted operations:** the external mutations the agent may
  perform, or `none`;
- **stop boundary:** the point at which control returns to the operator;
  and
- **verified against:** the observed full commit, external state where
  relevant, and observation time.

The classifications mean:

- `operator act required` identifies a non-delegable act. An agent may
  present it but cannot perform or manufacture it.
- `operator authorization required` identifies an agent-capable action
  that remains inert until the operator launches it directly or adopts
  it by reference.
- `agent operation already authorized` records authority the operator
  has already granted for the named action and operations. It is not a
  reusable grant after the stop boundary or for later queue entries.

The handoff carries exactly one current action, and only it can be
adopted by reference. The handoff is never bulk authority, and
advancing the file does not launch anything.

Carry the classification, referential-launch behavior, and
operator-act boundary into m0019's proposed doctrine and `CLAUDE.md`
execution targets. The active handoff template created by m0019 must
render the full record and its optional operator shorthand together.

## What this changes and preserves

This corrects two gaps in proposed matters; it contradicts no ratified
text. It preserves m0016's rule that launches are pointers rather than
shadow specifications and m0019's rule that a handoff is advisory and
cannot authorize, ratify, stage, or extend a matter.

The authority in a referential launch comes from the operator's new
utterance or an already-recorded operator grant, never from the agent
that wrote the handoff. The handoff supplies identification and a
bounded capability description. The matter supplies substantive scope.

This matter does not amend doctrine directly. m0016 and m0019 will
carry the normative amendments if and when each is independently
vetted, operator-summarized, ratified, staged, and executed.

## Proposed implementation plan

1. After m0017 is executed, ratify this matter using the
   operator-authored mechanism. Its `depends_on` prevents earlier
   staging.
2. Revise m0016's proposed text, enforcement, contradiction analysis,
   and execution plan with the referential-launch and delegated-
   mechanics rules above. Append a proposed-state correction entry
   under `## Vetting` linking this matter and its thread; do not present
   the entry as an independent fresh review round.
3. Revise m0019's proposed text, enforcement, contradiction analysis,
   and execution plan with the next-action schema and three authority
   classifications above. Append the same kind of proposed-state
   correction entry under `## Vetting`.
4. Refresh `handoff.md` to the new schema. Keep exactly one current
   action; do not copy matter scope, execution instructions, or
   matter-specific commentary into it.
5. Regenerate `matters/index.md` and record a run under doctrine §9.1,
   “Runs,” verifying the exact required fields, classification
   vocabulary, referential shorthand, links, state preservation, and
   stable index generation.
6. Append this matter's `## Execution` record and move it
   `staged → executed`. No doctrine edit and no m0001 re-ratification
   occur in this matter.
7. Put the completed branch before the operator for a merge-commit
   merge. The revised m0016 and m0019 remain proposed and require their
   own later vetting and ratification.
