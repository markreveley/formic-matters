---
type: spec
title: Operator-authored ratification commits
description: "Ratification becomes an operator-authored summary and declaration committed to the matter; agent review verifies the summary, and the final operator commit is the act and exact-text pin."
id: m0017
state: proposed
status: draft
tags: [formic-matters, process, ratification, integrity]
implements: m0001
generated:
  by: codex/2026-08-27
  at: 2026-08-27T15:20:13-07:00
---

# m0017 · Operator-authored ratification commits

## Diagnosed reason

Doctrine §6, “Vetting and ratification,” makes ratification the
operator's act over exact text at a named commit, then has an agent
record the act and compute its pin. That rule repaired the bootstrap's
central failure — a document marked ratified without the operator
having read it — but its evidence of comprehension can still be a
one-line statement outside the repository. The exact tree is pinned;
what the operator understood and accepted is not demonstrated in the
matter itself, and the act depends on later thread export to enter the
repository channel.

An operator-authored summary committed inside the matter improves both
properties. Writing the summary forces an explicit account of scope,
exclusions, ordering, and risk. Committing it makes the act and the
exact tree one event, rather than a verbal act later mapped to a commit
by an agent. Agent review can then compare the operator's understanding
with the proposed contract before the operator makes the final
ratification commit.

This is evidence of comprehension, not proof of an internal mental
state. An operator could still copy text without understanding it. The
mechanism materially raises the cost and visibility of rubber-stamping;
it does not claim to make rubber-stamping logically impossible.

## Proposed text

Amend doctrine §6, “Vetting and ratification,” so the operator act is
an authored commit rather than a verbal statement naming a commit.
Ownership does not change: the operator alone ratifies; agents review
and record but never author the operator's section.

### Matter form

Before the first `## Vetting` or `## Execution` heading, the operator
adds:

```markdown
## Operator ratification

### Draft — <date>

<operator-authored summary in the operator's own words>
```

The summary addresses, in the operator's own words:

- the deliverable and intended outcome;
- the accepted scope;
- explicit exclusions and non-goals;
- dependencies or execution-order constraints;
- material risks, irreversible effects, or uncertainties knowingly
  accepted; and
- why the operator accepts this contract.

The form is a comprehension aid, not a fill-in attestation. Quoting or
paraphrasing the matter without synthesizing what is accepted is a
review finding.

### Draft review

The operator commits the draft on the matter branch. A fresh agent
reviews the complete ratified region and appends a `## Vetting` entry
that checks the summary claim by claim against the matter. The agent:

- identifies omissions, contradictions, or material
  misunderstandings;
- never writes, rewrites, completes, or supplies replacement wording
  for any content under `## Operator ratification`; and
- records a clean disposition only when the summary accurately covers
  the contract.

The operator makes every correction personally, in a new commit.
History is never amended or force-pushed. Review and correction repeat
until the appended vetting record has a clean disposition.

This draft review is mandatory even when the operator elects to skip
other vetting rounds. Doctrine §6's current permission to ratify at any
round, including immediately, is narrowed accordingly: an operator may
still end substantive vetting when ready, but prospective ratification
does not occur until a fresh agent has reviewed the operator-authored
summary.

### The ratification commit

After a clean draft review, the operator makes one final commit that
changes `### Draft — <date>` to `### Ratified — <datetime>` and appends
an explicit declaration that the operator ratifies the matter as
summarized. That final commit is the ratification act. No separate
verbal acknowledgment is required.

The final operator commit changes only content under
`## Operator ratification`. If it changes the proposed contract or any
other file, it is not a conforming ratification commit: the new text
requires review, and the operator makes a later final commit after that
review. The recording agent checks this commit shape mechanically.

The repository's Git author metadata is not proof that a human made
the commit: agents commonly inherit the operator's configured Git
identity. The normative identity boundary is therefore the channel
rule that agents never edit the operator section. A cryptographically
signed, human-only commit would strengthen provenance but is not
required by this matter; introducing a signing requirement is a
separate policy decision.

### Recording and the pin

The recording agent verifies the final commit against the clean review,
then writes `state: ratified`, `verified`, `ratified_commit`, and
`ratified_sha256` in a later commit. `ratified_commit` is the final
operator commit. The `## Operator ratification` section sits inside the
ordinary matter's ratified region, so the hash covers both the contract
and the operator's authored understanding. The pin still follows the
act and is never offered in advance.

An invalid final commit is reported and not recorded as ratified. The
matter remains `proposed`; the operator corrects it through new commits
and performs a new conforming final act. The agent's conformance check
does not grant ratification authority — it checks whether the operator's
act used the ratified mechanism, just as the existing recording agent
checks the region hash and named commit.

### Re-opening and re-ratification

Previous `### Ratified` entries are never edited. A matter returned to
`proposed` appends a new `### Draft` entry under the same
`## Operator ratification` heading and repeats the protocol. The new
ratified-region hash covers the preserved prior entries and the new
one. Existing doctrine rules still record the superseded pin and the
reason for re-opening in `## Vetting`.

For m0001, whose proposed text and hash target are the separate
`doctrine/matters.md` file, the operator appends the summary on m0001
and makes the final commit over a tree containing the exact doctrine
being re-ratified. `ratified_commit` names that operator commit;
`ratified_sha256` remains the whole doctrine file under the existing
special regime. The summary is immutable through the commit even
though m0001's special hash does not cover the matter body.

### Scope boundary

This matter governs prospective ratification and re-ratification. It
does not change doctrine §11, “The retroactive path”: an acknowledgment
of already-landed work remains under the existing mechanism. Extending
operator-authored summaries to retroactive acknowledgments is a
separate matter because their hashed region and review question differ.

## What this contradicts

This supersedes doctrine §6, “Vetting and ratification,” where the
operator presently “reads the matter as it stands at a specific commit
and states ratification” and an agent maps that statement to the named
commit. It preserves that section's exact-text rule, operator-only
ownership, region regimes, agent-computed hash, and pin-follows-the-act
rule; it replaces only the form and repository location of the
operator act.

It also supersedes any standing example that treats a one-line verbal
statement as sufficient prospective ratification. Historical acts and
their records remain valid and are never rewritten.

It narrows doctrine §6's rule that the operator may ratify at any round,
including immediately, by requiring the operator-summary review as the
last prospective gate. It does not require any other number of vetting
rounds.

## Proposed execution plan

1. Amend doctrine §6, “Vetting and ratification,” with the operator
   draft, review, final-commit, recording, re-ratification, and scope
   rules above; adjust §3 transition wording only where needed to name
   the operator commit rather than a verbal act.
2. Add a standing rule to `CLAUDE.md`: agents never author or edit
   `## Operator ratification`; they may only review it and record a
   conforming operator commit.
3. Forward deterministic checks to m0008: presence and placement of the
   final section at a ratification transition, the final operator
   commit's allowed diff shape, and inclusion of the section in the
   ordinary ratified region. Human authorship and summary comprehension
   remain judgment checks.
4. Regenerate `matters/index.md` and record a doctrine/hash/transition
   verification run under doctrine §9.1, “Runs.”
5. Ratify and execute this matter under the currently ratified verbal
   mechanism; a voluntary operator-authored draft may rehearse the new
   form but cannot bootstrap its own authority.
6. Re-ratify m0001 under the current mechanism over the doctrine
   amendment, record both pins, append this matter's execution record,
   and merge by merge commit on operator direction.
7. Use this mechanism for the next prospective ratification. The first
   intended mandatory use is m0016, “Launch instructions are pointers,
   not shadow specifications.”
