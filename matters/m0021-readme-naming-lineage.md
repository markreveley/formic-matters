---
type: spec
title: README carries the naming rationale and lineage
description: "The README gains an expository section on the restate-to-ratify name — its rule, its agency-law and read-back lineage, and the three provenance layers the record accretes."
id: m0021
state: proposed
status: draft
tags: [formic-matters, documentation, provenance]
implements: m0001
depends_on: [m0017]
generated:
  by: claude-code/2026-08-28
  at: 2026-08-28T20:08:20Z
---

# m0021 · README carries the naming rationale and lineage

## Proposed text

Insert into [`README.md`](../README.md), immediately before
“## Ratifying, and checking a ratification”, this section verbatim:

```markdown
## Why "restate to ratify"

The ratification mechanism
([m0017](matters/m0017-operator-authored-ratification.md)) is named
for its rule: no ratification without a restatement. A restatement is
the operator's own-words synthesis of what is being accepted — scope,
exclusions, risks knowingly accepted, and the reasons for acceptance —
committed onto the matter, verified by agent review against the exact
text, and finished by the operator's own ratification commit. The
direction is the point: the operator authors the account and agents
check it against the text. An agent's description of a matter is never
the basis of ratification — the first bootstrap failed exactly there,
with a document marked ratified on the strength of an agent summary
that misdescribed the committed text (spec §14).

The pattern has precedents wherever one party's understanding must be
verified before an act takes effect:

- **Agency law.** Ratification is a principal's adoption of an act
  performed by an agent, and it is valid only with knowledge of the
  material facts. Restate-to-ratify operationalizes the knowledge
  requirement: the restatement is that knowledge, demonstrated on the
  record at the moment of adoption.
- **Read-back protocols.** Aviation read-back/hear-back, clinical
  teach-back, the plea colloquy: the accepting party restates, the
  counterparty evaluates, and the restatement goes on the record. The
  framework is that protocol for human–agent governance, with the
  restatement pinned by commit and hash.

The record accretes three provenance layers: **text provenance** — the
pinned commit and hash: what exactly was accepted; **ruling
provenance** — threads and the rulings ledgers: what was decided along
the way; and **operator-comprehension provenance** — the restatement:
what the decider understood and chose to accept, hashed with the text
it accepts.
```

The fenced block is quoted destination text: its relative link
resolves from the repository root, where `README.md` lives, not from
`matters/` — by construction, since the block lands verbatim.

The section is expository. It is subordinate to the doctrine and to
[m0017](m0017-operator-authored-ratification.md)'s normative text, and
the historical narration it carries belongs in the README precisely
because it does not belong in the specification — the operator's
standing ruling against historical narration in normative text
(m0001's rulings ledger, review r2).

## What this contradicts

Nothing normative: no rule changes, no doctrine amendment, no m0001
re-ratification. The section presumes m0017's mechanism and its
naming, so `depends_on: [m0017]` holds this matter until that
mechanism is ratified and executed.

Why this is a matter at all: the framework's home is self-hosting, and
nothing lands that did not begin as a matter (doctrine §1, “What a
matter is”). The precedent is
[m0015](m0015-agent-instructions.md): even the agent-instructions file
entered through a matter. The README is in the governed tree;
expository or not, its changes land through the process.

## Proposed execution plan

1. Insert the section verbatim at the stated location; change nothing
   else in `README.md`.
2. No doctrine change and no m0001 re-ratification occur in this
   matter.
3. Regenerate `matters/index.md`, append this matter's execution
   record, and merge by merge commit on operator direction.
