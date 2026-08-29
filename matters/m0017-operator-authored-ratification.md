---
type: spec
title: Restate to ratify — operator-authored restatements
description: "Ratification is an operator-authored restatement committed to the matter; a fresh agent verifies it against the matter text, and a passing verification completes the act, which the agent records with the exact-text pin."
id: m0017
state: proposed
status: draft
tags: [formic-matters, process, ratification, integrity]
implements: m0001
threads:
  - threads/2026-08-28-restate-to-ratify.md
  - threads/2026-08-29-minimal-handoff-and-declared-sources.md
generated:
  by: codex/2026-08-27
  at: 2026-08-27T15:20:13-07:00
---

# m0017 · Restate to ratify — operator-authored restatements

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

An operator-authored restatement committed inside the matter improves
both properties. Writing the restatement forces an explicit account of
scope, exclusions, ordering, and risk. Recording it in the matter makes
the act and the exact tree one event, rather than a verbal act later
mapped to a commit by an agent. Agent review compares the operator's
understanding with the proposed contract, and a passing comparison
completes the act.

This is evidence of comprehension, not proof of an internal mental
state. An operator could still copy text without understanding it. The
mechanism materially raises the cost and visibility of rubber-stamping;
it does not claim to make rubber-stamping logically impossible.

## Proposed text

Amend doctrine §6, “Vetting and ratification,” so the operator act is
an authored restatement, verified in the repository, rather than a
verbal statement naming a commit. The mechanism is named **restate to
ratify**, and its rule is one line: no ratification without a
restatement. Ownership does not change: the operator alone authors
the restatement that ratifies; agents verify, transcribe verbatim,
and record, and never compose or alter the restatement's content.

### The restatement

The operator restates; no other party may. A **restatement** is the
operator's account, in the operator's own words, of what the matter
does and why — the operator's interpretation at the operator's
altitude, not a second copy at the matter's fidelity. It is bounded by
the matter: every claim in it anchors in the matter text, it adds
nothing the matter does not say, and the verification (step 3 below)
diffs it against the matter. Zero additive content is the test.

A claim the verification cannot anchor in the matter is a finding, and the
operator resolves it one of two ways: it was a misreading, and the
operator corrects the restatement; or it was real content the matter
fails to state, and the matter is underspecified — the content enters
the matter through revision and review before ratification proceeds.
Ratification is never the channel by which new content enters the
record.

Quotation and line-by-line paraphrase are findings from the other
side: they reproduce the matter's fidelity without interpreting it, so
they evidence nothing. The restatement carries no content checklist of
its own: what there is to restate is set by the matter — starting with
the content its type requires (doctrine §2, “Type — immutable”) — and
a material omission against the matter is a finding.

The operator authors the restatement; agents verify it against the
matter text. The operator's verified restatement is the basis of
ratification.

The record then carries three provenance layers: text provenance (the
pinned commit and hash), ruling provenance (threads and the rulings
compiled from them), and operator-comprehension provenance (the
restatement, hashed with the text it accepts).

### Matter form

The restatement lives in the matter, before the first `## Vetting`
or `## Execution` heading:

```markdown
## Operator ratification

### Draft — <date>

<the operator's restatement, in the operator's own words>
```

The form is a comprehension aid, not a fill-in attestation.

### The protocol, step by step

1. **The operator** writes the restatement — the only text the
   operator authors in this protocol.
2. **The operator or an agent** commits it to the matter as
   `### Draft — <date>` under `## Operator ratification`. An agent
   doing this transcribes the operator's recorded wording verbatim,
   attributed, and never composes or alters it. Submitting the
   draft is the operator's declaration that a passing verification
   (step 4) ratifies the matter as restated.
3. **A fresh agent** — one that has not worked on this matter —
   compares the restatement to the matter text, claim by claim.
   The comparison fails on: a claim that does not anchor in the
   matter (zero additive content is the test), a material omission
   against the matter, or quotation and line-by-line paraphrase,
   which interpret nothing.
4. **If the comparison fails,** ratification does not occur. The
   agent reports each failure to the operator. For an unanchored
   claim the operator decides which case it is: a misreading — the
   operator rewords the restatement — or matter
   underspecification — the missing content enters the matter by
   revision, and the operator restates over the revised text.
   Either way the protocol restarts at step 3 with a fresh agent.
   Every rewording is the operator's own; history is never amended
   or force-pushed.
5. **If the comparison passes, ratification is complete at that
   moment.** The same agent, in the same session, makes one commit
   that: appends the verification's record to `## Vetting` (who
   verified, when, at which commit), changes `### Draft — <date>`
   to `### Ratified — <datetime>`, and writes the frontmatter
   record — `state: ratified`, `verified` (the operator, with the
   verification's datetime), and the pin below. That commit changes
   nothing else — a shape reviewers confirm today and the validator
   will check once it exists ([m0008](m0008-matter-tooling.md)).

**Completion:** the matter is ratified when step 5's commit exists.
There is no later confirmation, no second operator act, and no
waiting period. Step 3 is mandatory even when the operator skips
every other review: doctrine §6's permission to ratify at any
round, including immediately, is narrowed to "immediately after the
comparison passes."

### What the record proves

The record evidences the exact text accepted, an operator-authored
restatement a fresh agent found faithful to it, and a recording
made in the same session as the verification. It does not prove
human authorship of the restatement or an internal state of
comprehension. Git author metadata is not that proof either: agents
commonly inherit the operator's configured Git identity. The
normative identity boundary is the channel rule in step 2 — agents
never compose or alter the restatement. A cryptographically signed,
human-only commit would strengthen provenance, as would integrity
analysis of the restatement corpus against the operator's verbatim
turns in `threads/`
([m0023](m0023-restatement-integrity-analysis.md)); neither is
required by this matter — introducing either is a separate policy
decision.

### The pin

The pin is the pair step 5 records: `ratified_commit` — step 5's
own commit, whose tree preserves the exact contract and restatement
in Git history forever — and `ratified_sha256`, a hash of the
ratified region at that commit. The `## Operator ratification`
section sits inside the ordinary matter's ratified region, so the
hash covers both the contract and the restatement. The hash exists
because the matter file keeps legitimately changing after
ratification (entries append, state fields change): whether the
accepted text is still intact is answered by recomputing one number
([m0007](m0007-ratification-content-hash.md)'s tooling), not by
hand-diffing history. The pin follows the act and is never offered
in advance.

Steps 3 and 5 happen in one session over one tree state, so the
text pinned is the text verified. A step 5 commit later found to
have changed more than its permitted contents is a finding, and the
exit is doctrine §3, “State — mutable”: the operator re-opens the
matter. The verification grants the agent no ratification
authority: the basis of ratification is the operator's restatement;
the verification only confirms it is faithful.

### Precedence and discovered divergence

The ratified text is the contract; the restatement is evidence of the
act and never governs. A material divergence between restatement and
text discovered after the act and before execution is a vetting
finding on the matter, and the exit is doctrine §3, “State — mutable”:
the operator re-opens the matter (`ratified → proposed`), or the dev
agent stops and records (`staged → proposed`), and a corrected
restatement and a fresh pass of steps 3–5 are required before work
proceeds. A divergence discovered after execution is a new matter,
since nothing leaves `executed`.

### Re-opening and re-ratification

Previous `### Ratified` entries are never edited. A matter returned to
`proposed` appends a new `### Draft` entry under the same
`## Operator ratification` heading and repeats the protocol. The new
ratified-region hash covers the preserved prior entries and the new
one. Existing doctrine rules still record the superseded pin and the
reason for re-opening in `## Vetting`.

For m0001, whose proposed text and hash target are the separate
`doctrine/matters.md` file, the operator's restatement is added on
m0001, and step 5's commit is made over a tree containing the exact
doctrine being re-ratified. `ratified_commit` names that commit;
`ratified_sha256` remains the whole doctrine file under the
existing special regime. The restatement is immutable through the
commit even though m0001's special hash does not cover the matter body.

### Scope boundary

This matter governs prospective ratification and re-ratification. It
does not change doctrine §11, “The retroactive path”: an acknowledgment
of already-landed work remains under the existing mechanism. Extending
operator-authored restatements to retroactive acknowledgments is a
separate matter because their hashed region and review question differ.

## What this contradicts

No ratified matter is contradicted. This amends doctrine §6,
“Vetting and ratification,” where the operator presently “reads the
matter as it stands at a specific commit and states ratification”
and an agent maps that statement to the named commit. It preserves
that section's exact-text rule, operator-only ownership, region
regimes, agent-computed hash, and pin-follows-the-act rule; it
replaces only the form of the operator act. (“Supersede” is
reserved for its §5, “Supersession, splitting, and conflict,”
meaning — one matter replacing another; no matter is superseded
here.)

It also retires the standing example that treats a one-line verbal
statement as sufficient prospective ratification. Historical acts and
their records remain valid and are never rewritten.

It narrows doctrine §6's rule that the operator may ratify at any round,
including immediately, by requiring the restatement verification as the
last prospective gate. It does not require any other number of vetting
rounds.

The name changes no rule. “Restate to ratify” names the mechanism
this matter proposes; **restatement** is defined above — bounded by
the matter and diffed against it, which is what the *re-* carries.

## Proposed execution plan

1. Amend doctrine §6, “Vetting and ratification,” with the restatement
   definition and direction rule, and the operator draft, review,
   completion, recording, precedence, re-ratification, and scope
   rules above; adjust §3 transition wording only where needed to name
   the clean review's completion rather than a verbal act.
2. Add a standing rule to `CLAUDE.md`: agents never compose or alter
   content under `## Operator ratification`; they transcribe the
   operator's recorded wording verbatim, verify it, and record a
   passing verification's completion. In the same edit, revise
   `CLAUDE.md`'s existing ratification sentence — “over exact text
   at a commit the operator names” — to describe this mechanism.
3. Forward deterministic checks to m0008: presence and placement of
   the section at a ratification transition, step 5's commit shape
   (the verification record, the heading change, the frontmatter
   record, nothing else), and inclusion of the section in the
   ordinary ratified region. Human authorship and restatement
   comprehension remain judgment checks.
4. Regenerate `matters/index.md` and record a doctrine/hash/transition
   verification run under doctrine §9.1, “Runs.”
5. Ratify and execute this matter under the currently ratified verbal
   mechanism; a voluntary operator-authored draft may rehearse the new
   form but cannot bootstrap its own authority.
6. Re-ratify m0001 under the same verbal mechanism as step 5 uses,
   over the doctrine amendment; record both pins, append this
   matter's execution record, and merge by merge commit on operator
   direction.
7. Use this mechanism for every subsequent prospective ratification.
   Which matter uses it first is staging judgment, not this
   specification's: the operator selects it at launch.
