---
type: spec
title: Restate to ratify — operator-authored ratification commits
description: "Ratification is an operator-authored restatement and declaration committed to the matter; agent review diffs the restatement against the matter text, and the final operator commit is the act and exact-text pin."
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

# m0017 · Restate to ratify — operator-authored ratification commits

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
scope, exclusions, ordering, and risk. Committing it makes the act and
the exact tree one event, rather than a verbal act later mapped to a
commit by an agent. Agent review can then compare the operator's
understanding with the proposed contract before the operator makes the
final ratification commit.

This is evidence of comprehension, not proof of an internal mental
state. An operator could still copy text without understanding it. The
mechanism materially raises the cost and visibility of rubber-stamping;
it does not claim to make rubber-stamping logically impossible.

## Proposed text

Amend doctrine §6, “Vetting and ratification,” so the operator act is
an authored commit rather than a verbal statement naming a commit. The
mechanism is named **restate to ratify**, and its rule is one line: no
ratification without a restatement. Ownership does not change: the
operator alone ratifies; agents review and record but never author the
operator's section.

### The restatement

The operator restates; no other party may. A **restatement** is the
operator's account, in the operator's own words, of what the matter
does and why — the operator's interpretation at the operator's
altitude, not a second copy at the matter's fidelity. It is bounded by
the matter: every claim in it anchors in the matter text, it adds
nothing the matter does not say, and the draft review diffs it against
the matter. Zero additive content is the test.

A claim the review cannot anchor in the matter is a finding, and the
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

Before the first `## Vetting` or `## Execution` heading, the operator
adds:

```markdown
## Operator ratification

### Draft — <date>

<the operator's restatement, in the operator's own words>
```

The form is a comprehension aid, not a fill-in attestation.

### Draft review

The operator commits the draft on the matter branch. A fresh agent
reviews the complete ratified region and appends a `## Vetting` entry
that checks the restatement claim by claim against the matter. The
agent:

- identifies material omissions, contradictions, and
  misunderstandings against the matter text;
- flags every claim it cannot anchor in the matter — the zero-additive
  test — for the operator to resolve as a misreading or as matter
  underspecification, per the definition above;
- flags quotation and line-by-line paraphrase, which interpret
  nothing;
- never writes, rewrites, completes, or supplies replacement wording
  for any content under `## Operator ratification`; and
- records a clean disposition only when the restatement is accurate,
  bounded, and interpretive.

The operator makes every correction personally, in a new commit.
History is never amended or force-pushed. Review and correction repeat
until the appended vetting record has a clean disposition.

This draft review is mandatory even when the operator elects to skip
other vetting rounds. Doctrine §6's current permission to ratify at any
round, including immediately, is narrowed accordingly: an operator may
still end substantive vetting when ready, but prospective ratification
does not occur until a fresh agent has reviewed the operator's
restatement.

### The ratification commit

After a clean draft review, the operator makes one final commit that
changes `### Draft — <date>` to `### Ratified — <datetime>` and appends
an explicit declaration that the operator ratifies the matter as
restated. That final commit is the ratification act. No separate
verbal acknowledgment is required.

The final operator commit changes only content under
`## Operator ratification`. If it changes the proposed contract or any
other file, it is not a conforming ratification commit: the new text
requires review, and the operator makes a later final commit after that
review. The recording agent checks this commit shape mechanically.

What the record evidences is bounded: the exact text accepted, a
conforming operator act over it, and a fresh review that found the
restatement faithful. It does not prove human authorship of the
restatement or an internal state of comprehension. The repository's
Git author metadata is not proof that a human made the commit: agents
commonly inherit the operator's configured Git identity. The normative
identity boundary is therefore the channel rule that agents never edit
the operator section. A cryptographically signed, human-only commit
would strengthen provenance, as would integrity analysis of the
restatement corpus against the operator's verbatim turns in
`threads/` ([m0023](m0023-restatement-integrity-analysis.md));
neither is required by this matter — introducing either is a separate
policy decision.

### Recording and the pin

The recording agent verifies the final commit against the clean review,
then writes `state: ratified`, `verified`, `ratified_commit`, and
`ratified_sha256` in a later commit. `ratified_commit` is the final
operator commit. The `## Operator ratification` section sits inside the
ordinary matter's ratified region, so the hash covers both the contract
and the operator's restatement. The pin still follows the act and is
never offered in advance.

An invalid final commit is reported and not recorded as ratified. The
matter remains `proposed`; the operator corrects it through new commits
and performs a new conforming final act. The agent's conformance check
does not grant ratification authority — it checks whether the operator's
act used the ratified mechanism, just as the existing recording agent
checks the region hash and named commit.

### Precedence and discovered divergence

The ratified text is the contract; the restatement is evidence of the
act and never governs. A material divergence between restatement and
text discovered after the act and before execution is a vetting
finding on the matter, and the exit is doctrine §3, “State — mutable”:
the operator re-opens the matter (`ratified → proposed`), or the dev
agent stops and records (`staged → proposed`), and a corrected
restatement and a new conforming act are required before work
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
`doctrine/matters.md` file, the operator appends the restatement on
m0001 and makes the final commit over a tree containing the exact
doctrine being re-ratified. `ratified_commit` names that operator
commit; `ratified_sha256` remains the whole doctrine file under the
existing special regime. The restatement is immutable through the
commit even though m0001's special hash does not cover the matter body.

### Scope boundary

This matter governs prospective ratification and re-ratification. It
does not change doctrine §11, “The retroactive path”: an acknowledgment
of already-landed work remains under the existing mechanism. Extending
operator-authored restatements to retroactive acknowledgments is a
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
including immediately, by requiring the restatement review as the last
prospective gate. It does not require any other number of vetting
rounds.

The name changes no rule. “Restate to ratify” names the mechanism
this matter proposes; **restatement** is defined above — bounded by
the matter and diffed against it, which is what the *re-* carries.

## Proposed execution plan

1. Amend doctrine §6, “Vetting and ratification,” with the restatement
   definition and direction rule, and the operator draft, review,
   final-commit, recording, precedence, re-ratification, and scope
   rules above; adjust §3 transition wording only where needed to name
   the operator commit rather than a verbal act.
2. Add a standing rule to `CLAUDE.md`: agents never author or edit
   `## Operator ratification`; they may only review it and record a
   conforming operator commit.
3. Forward deterministic checks to m0008: presence and placement of the
   final section at a ratification transition, the final operator
   commit's allowed diff shape, and inclusion of the section in the
   ordinary ratified region. Human authorship and restatement
   comprehension remain judgment checks.
4. Regenerate `matters/index.md` and record a doctrine/hash/transition
   verification run under doctrine §9.1, “Runs.”
5. Ratify and execute this matter under the currently ratified verbal
   mechanism; a voluntary operator-authored draft may rehearse the new
   form but cannot bootstrap its own authority.
6. Re-ratify m0001 under the current mechanism over the doctrine
   amendment, record both pins, append this matter's execution record,
   and merge by merge commit on operator direction.
7. Use this mechanism for every subsequent prospective ratification.
   Which matter uses it first is staging judgment, not this
   specification's: the operator selects it at launch.

## Vetting

### Round 1 — 2026-08-29

- **Reviewer:** claude-code/2026-08-29, fresh instance — no prior
  authoring contact with this matter. Launched by the operator
  against `handoff.md`'s next-action record; the handoff was read in
  full and carried no expected findings. The record's re-verification
  checks were run first: pull request #15 merged as a merge commit,
  `main` at `54b83622928865813aeb694b5ef0195052b9b226` (fetched,
  2026-08-29), this matter `proposed` with no prior `## Vetting`
  entries. Inputs: this matter and the doctrine at that commit, its
  two cited threads
  ([restate](../threads/2026-08-28-restate-to-ratify.md),
  [minimal](../threads/2026-08-29-minimal-handoff-and-declared-sources.md);
  cited below as `restate:N` / `minimal:N`), m0001's `## Vetting`
  round format and first round, m0014 as the executed
  amend-the-doctrine precedent, `CLAUDE.md`, and the regenerated
  index. The archived first attempt was not read.
- **Checks run:** fidelity (every operator ruling in the two threads
  against this text); consistency with the ratified doctrine — §3
  "State — mutable", §5 "Supersession, splitting, and conflict", §6
  "Vetting and ratification", §8 "Where discourse lives", §10
  "Deterministic wherever possible", §11 "The retroactive path", §12
  "Storage and format" — and with m0014's record; protocol holes in
  the proposed mechanism; §2 "Type — immutable" readiness for type
  `spec`; mechanics (frontmatter schema, links, index regeneration,
  review r2's no-client-names rule).

**Findings, ranked by severity:**

**A1 · MEDIUM — nothing binds the final commit to the tree the clean
review reviewed.** "The ratification commit" pins the final operator
commit's diff shape (content under `## Operator ratification` only),
and "Recording and the pin" has the recording agent "verif[y] the
final commit against the clean review" — but no rule names the check
that the contract being ratified is the contract the clean review
read. The sequence that slips through: the clean review is recorded
over the region at one commit; a later commit revises the contract
(the underspecification fork itself licenses mid-protocol revision —
"the content enters the matter through revision and review"); the
operator's final commit changes only the operator section. That
final commit is conforming by diff shape, the last appended review
is clean, and the recorded pin hashes a region no review compared
against the restatement. The in-text guard covers only a final
commit that itself touches the contract. This is exactly the class
§10 assigns to deterministic code, and plan step 3's forwarded list
(placement, diff shape, region inclusion) omits it. Suggested edit:
require the draft-review entry to name the commit it reviewed; state
in "Recording and the pin" that a final commit is conforming only if
the ratified region outside `## Operator ratification` is
byte-identical to that region at the clean review's named commit —
otherwise the review is stale and a fresh round is required; and add
the identity check to step 3's forwarded list.

**A2 · LOW-MEDIUM — plan step 2 leaves CLAUDE.md's standing
ratification rule false.** `CLAUDE.md` (m0015, executed) distills:
"ratification is the operator's act alone, over exact text at a
commit the operator names (§6)." Under the amended §6 the operator
names no commit — the operator authors the final commit. Step 2 only
adds the new never-author rule; nothing revises the existing bullet,
which would then misdescribe the mechanism in the one channel that
reaches every agent before it reads anything else — m0015's own
diagnosis. (The pin bullet survives as written: its region
description stays true with `## Operator ratification` inside the
region.) Suggested edit: step 2 also rewords that bullet to the
operator-authored-commit form.

**A3 · LOW — plan step 6's "under the current mechanism" is
ambiguous at the moment it runs.** By step 6, step 1 has landed the
amendment in the doctrine file while m0001's re-ratification is what
makes it normative, so "current" can be read as either mechanism.
Step 5 states the bootstrap rule precisely ("under the currently
ratified verbal mechanism … cannot bootstrap its own authority");
step 6 means the same verbal act — m0014's re-pin dance is the
precedent — and should say so. Suggested edit: "under the same
verbal mechanism as step 5."

**A4 · LOW — "supersedes" is used for a doctrine amendment.** "What
this contradicts" opens "This supersedes doctrine §6" and later
"also supersedes any standing example." §5 defines supersession as a
matter-to-matter act effected through `superseded_by`; no matter is
superseded here and no link is owed. The executed precedent words
this shape cleanly (m0014: "No ratified matter. It amends …").
Suggested edit: "replaces"/"amends" for doctrine text, plus an
explicit no-ratified-matter-is-contradicted sentence, reserving
"supersede" for §5 relations.

**Checks passed clean:**

- **Fidelity, in full — every operator ruling in the cited threads
  is encoded, none is contradicted:** the zero-additive definition,
  its two-way fork, and "Ratification is never the channel by which
  new content enters the record" (restate:196); the
  operator-altitude bound and the *re-* as bounded-and-diffed
  (restate:198); no content checklist — the matter sets what there
  is to restate, §2 cited (restate:286); the positive-form direction
  rule with the negations dropped (restate:204); precedence and
  discovered divergence resolving through §3's existing exits
  (restate:108); the bounded-evidence statement in the normative
  text with strengthenings named-not-required (restate:110, deltas
  agreed at restate:288); operator-comprehension provenance as the
  third layer (restate:106); m0023 cross-linked as advisory
  (restate:208); step 7 generalized off the hard-coded first use
  (minimal:94; the pull request #15 diff of this file is exactly
  that edit plus the second thread cite).
- **Doctrine consistency:** the preserved-properties list checks out
  against §6 (exact text, operator-only ownership, both region
  regimes and the retroactive extension, agent-computed hash, pin
  follows the act); the narrowing of ratify-at-any-round is
  declared, never silent; §3's exits are used correctly and nothing
  leaves `executed`; the §11 scope boundary holds; the placement
  rule puts `## Operator ratification` inside the §6 region exactly
  as claimed; the §12 filename rule survived the retitle; §10's
  division holds — the conformance check is mechanical and
  explicitly grants no ratification authority.
- **§2 readiness, type `spec`:** the proposed text and the
  contradiction account are both present and, A4's wording aside,
  accurate.
- **Mechanics:** every frontmatter field is §12-defined and
  `status: draft` correctly derived; the description is one quoted
  sentence; timestamps carry explicit offsets; both thread cites and
  the m0023 link resolve; `tools/gen-index.py` reproduces
  `matters/index.md` byte-identically; no client names or instance
  state in current-voiced text (review r2).

Not checked: the archived first attempt (unread, per standing
practice), and the five matters that depend on this one beyond their
edges to it — each gets its own round.

**Observations, no edit proposed:** (a) a draft-review finding the
operator judges to be reviewer error has no third fork branch; the
recourse is an unchanged restatement and a fresh round, so a wrong
finding costs one round and never deadlocks — a deliberate price of
the mandatory gate, worth knowing at the ratification read. (b) At
execution, transcribing these rules into §6's wording is bounded by
§3.1: a transcription choice that changes a rule is an execution
failure, not a recordable deviation. (c) Who counts as fresh across
draft-review repeats inherits §6's fresh-agents rule and m0006's
deferral unchanged.

- **Deviations:** the launch environment assigned branch
  `claude/handoff-item-1-2u2k20`; §8's m0017-prefixed branch
  convention was not available, recorded here per the launch record.
  The commit carries the `Matter: m0017` trailer and the filing pull
  request title is m0017-prefixed.
- **Disposition:** nothing found is design-scale — the mechanism,
  its bounds, and its fidelity to the rulings all verified. A1–A4
  are proposed-state text edits, cheapest now: A1 should be resolved
  before ratification, since it names the integrity check the
  mechanism exists to provide; A2 and A3 are one-line plan edits; A4
  is wording. Recommend one revision pass and a further round before
  the operator's ratification read.
