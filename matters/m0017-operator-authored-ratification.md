---
type: spec
title: Restate to ratify — operator-authored restatements
description: "Ratification is an operator-authored restatement committed to the matter; a fresh agent verifies it against the matter text, and a clean verification completes the act, which the agent records with the exact-text pin."
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
understanding with the proposed contract, and a clean comparison
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

Before the first `## Vetting` or `## Execution` heading, the
operator's restatement is added — committed by the operator, or
transcribed verbatim from the operator's recorded turn by an agent
and attributed:

```markdown
## Operator ratification

### Draft — <date>

<the operator's restatement, in the operator's own words>
```

The form is a comprehension aid, not a fill-in attestation.
Submitting a restatement for review is the operator's declaration
that, on a clean review, the matter is ratified as restated; no
separate declaration is written.

### Draft review

With the draft on the matter branch, a fresh agent reviews the
complete ratified region and appends a `## Vetting` entry that
checks the restatement claim by claim against the matter. The
agent:

- identifies material omissions, contradictions, and
  misunderstandings against the matter text;
- flags every claim it cannot anchor in the matter — the zero-additive
  test — for the operator to resolve as a misreading or as matter
  underspecification, per the definition above;
- flags quotation and line-by-line paraphrase, which interpret
  nothing;
- never composes, completes, or alters the operator's restatement —
  transcribing the operator's recorded wording verbatim, attributed,
  is the one permitted writing act; and
- records a clean disposition only when the restatement is accurate,
  bounded, and interpretive.

Every correction is the operator's own wording, entering the matter
the same way as the draft. History is never amended or force-pushed.
Review and correction repeat until the appended vetting record has a
clean disposition.

This draft review is mandatory even when the operator elects to skip
other vetting rounds. Doctrine §6's current permission to ratify at any
round, including immediately, is narrowed accordingly: an operator may
still end substantive vetting when ready, but prospective ratification
does not occur until a fresh agent has reviewed the operator's
restatement.

### Ratification completes on the clean review

A clean review completes ratification; the operator makes no further
act and no closing commit. The reviewing agent's session records the
completion in one commit, directly after appending the clean review
entry: `### Draft — <date>` becomes `### Ratified — <datetime>`, and
the frontmatter fields below are written. That recording commit
changes nothing else — a shape reviewers confirm today and the
validator will check once it exists
([m0008](m0008-matter-tooling.md)).

What the record evidences is bounded: the exact text accepted, an
operator-authored restatement a fresh review found faithful to it,
and a recording that followed that review directly. It does not
prove human authorship of the restatement or an internal state of
comprehension. Git author metadata is not that proof either: agents
commonly inherit the operator's configured Git identity. The
normative identity boundary is the channel rule above — agents never
compose or alter the restatement. A cryptographically signed,
human-only commit would strengthen provenance, as would integrity
analysis of the restatement corpus against the operator's verbatim
turns in `threads/`
([m0023](m0023-restatement-integrity-analysis.md)); neither is
required by this matter — introducing either is a separate policy
decision.

### Recording and the pin

The recording commit writes `state: ratified`, `verified` (the
operator, with the clean review's datetime), `ratified_commit`, and
`ratified_sha256`. `ratified_commit` is the recording commit itself:
its tree carries the contract, the restatement, and the
`### Ratified` heading, and the `## Operator ratification` section
sits inside the ordinary matter's ratified region, so the hash
covers both the contract and the operator's restatement. The clean
review's entry names the commit whose text it read; between that
commit and the recording commit, the only permitted changes are the
review entry itself and the recording commit's own heading flip and
frontmatter — so the text pinned is the text reviewed, confirmed by
reviewers today and by the validator once it exists
([m0008](m0008-matter-tooling.md)). The pin still follows the act
and is never offered in advance.

A recording later found nonconforming — it changed more than the
heading and frontmatter, or the matter text moved between the
reviewed commit and the recording — is a vetting finding, and the
exit is doctrine §3, “State — mutable”: the operator re-opens the
matter. The agent's checks grant no ratification authority: the
basis of ratification is the operator's verified restatement,
nothing an agent decides.

### Precedence and discovered divergence

The ratified text is the contract; the restatement is evidence of the
act and never governs. A material divergence between restatement and
text discovered after the act and before execution is a vetting
finding on the matter, and the exit is doctrine §3, “State — mutable”:
the operator re-opens the matter (`ratified → proposed`), or the dev
agent stops and records (`staged → proposed`), and a corrected
restatement and a fresh clean review are required before work
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
m0001, and the recording commit is made over a tree containing the
exact doctrine being re-ratified. `ratified_commit` names that
recording commit; `ratified_sha256` remains the whole doctrine file
under the existing special regime. The restatement is immutable through the
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
   completion, recording, precedence, re-ratification, and scope
   rules above; adjust §3 transition wording only where needed to name
   the clean review's completion rather than a verbal act.
2. Add a standing rule to `CLAUDE.md`: agents never compose or alter
   content under `## Operator ratification`; they transcribe the
   operator's recorded wording verbatim, verify it, and record a
   clean review's completion.
3. Forward deterministic checks to m0008: presence and placement of
   the section at a ratification transition, the allowed
   change-shapes of the review-entry and recording commits, the
   matter text's identity between the reviewed commit and the
   recording commit, and inclusion of the section in the ordinary
   ratified region. Human authorship and restatement comprehension
   remain judgment checks.
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

| | |
|---|---|
| Reviewer | claude-code/2026-08-29 — a fresh session; no earlier work on this matter |
| Matter text reviewed | as of commit `54b8362` (the merge of pull request #15) |
| Launched by | the operator, through `handoff.md`'s declared next action |
| Read before reviewing | this matter; `doctrine/matters.md`; the two threads this matter cites; m0001's vetting rounds; m0014 (the closest executed precedent); `CLAUDE.md`; the index |
| Checked before starting | pull request #15 merged as a merge commit; this matter still `proposed`; no `## Vetting` section existed yet |
| Deviation | the branch name (`claude/handoff-item-1-2u2k20`) was assigned by the launch tooling and is not m0017-prefixed as §8 "Where discourse lives" asks; the commit trailer and pull request title carry the matter ID |

This entry was rewritten in place on its unmerged branch, on
operator direction, before any of it entered the record — the first
version was not intelligible to the operator. The branch history
keeps the original; the findings are unchanged in substance.

Four problems found, biggest first. Each names the section of this
matter it is about, states the problem in one sentence, then
explains.

**A1 — Between the agent's approval of the restatement and the
operator's separate closing commit, the matter text could change
without anyone noticing.**
About "The ratification commit" and "Recording and the pin" as they
stood at the reviewed commit. (Dissolved by the operator's
2026-08-29 ruling — see the operator review entry below.)
The drafted protocol had two separate events: first the reviewing
agent checks the operator's restatement against the matter and
records that it is faithful; later, the operator personally makes a
closing commit that marks the matter ratified. The only mechanical
check named for that closing commit was "did it touch anything
outside the operator's section?" Nothing required anyone to confirm
the matter text was still the same text the agent had checked. A
revision landing between the two events would end up ratified
without any reviewer having compared it to the restatement. The fix
suggested at the time: write down which commit the agent's check
read, and require the matter text to be identical to it at the
closing commit.

**A2 — The plan updates `CLAUDE.md` but leaves its existing
ratification sentence wrong.**
About "Proposed execution plan" step 2. `CLAUDE.md` today says
ratification happens "over exact text at a commit the operator
names." Under this matter that sentence stops being true, and step 2
only adds a new rule without correcting the old sentence — so the
one file every agent reads first would misdescribe the mechanism.
Suggested fix: step 2 also rewrites that sentence.

**A3 — Plan step 6 says "under the current mechanism," which will be
ambiguous by the time it runs.**
About "Proposed execution plan" step 6. When m0001 is re-ratified,
the doctrine file will already contain this matter's new rules, but
they only gain force from that very re-ratification. "Current" could
mean either the old way or the new way. Step 5 already names the old
way precisely ("the currently ratified verbal mechanism"); step 6
should use the same words.

**A4 — "Supersedes" is the wrong word for changing doctrine text.**
About "What this contradicts." In this repository "supersede" is a
defined relationship between two matters (§5 "Supersession,
splitting, and conflict"), recorded in a `superseded_by` list. This
matter replaces doctrine wording; it supersedes no matter. m0014
worded the same situation as "No ratified matter. It amends …".
Suggested fix: say "amends" or "replaces," and state plainly that no
ratified matter is contradicted.

Checked and found correct: every operator ruling in the two cited
threads is in this text and none is contradicted — the zero-additive
definition, the operator-altitude bound, the no-checklist rule, the
positively stated direction rule, the precedence rule, the honest
statement of what the record proves, and the generalized step 7
(rulings at `threads/2026-08-28-restate-to-ratify.md` lines 196,
198, 204, 286, 288 and
`threads/2026-08-29-minimal-handoff-and-declared-sources.md` line
94). Also correct: the list of §6 "Vetting and ratification"
properties this matter preserves; the claim that §11 "The
retroactive path" is untouched; the sections §2 "Type — immutable"
requires of a `spec` matter are present; all links resolve; the
frontmatter is schema-valid; the index regenerates unchanged; no
consumer names appear. Two things worth knowing, no change asked: a
restatement-review finding the operator believes is reviewer error
resolves only by running another round with a fresh agent — a cost,
never a deadlock; and at execution, any rewording that changes a
rule while transcribing this matter into the doctrine is an
execution failure under §3.1 "The execution record," not a
recordable deviation.

Not checked: the archived first attempt, and the matters that
depend on this one (each gets its own round).

Disposition: no design-scale problem found; A1–A4 were text fixes,
cheapest while the matter is `proposed`. A1 has since been dissolved
by operator ruling (next entry); A2–A4 remain open for the operator.

### Operator review — 2026-08-29 — in-session

| | |
|---|---|
| Reviewer | the operator, in the session that launched Round 1 |
| Recorded by | claude-code/2026-08-29, from the operator's turns |
| Source | this session's thread — export pending operator direction; the provenance gap is held open per the practice [m0024](m0024-declared-sources.md) proposes |

Rulings, each now in the body:

1. **The operator makes no closing commit.** "This should be 'the
   agent makes one final commit…' I don't need to make this commit.
   This should be explicit in m0017." The body now says the
   reviewing agent's session records the completion; the operator
   authors only the restatement.
2. **A clean review is ratification.** "Once approved is granted,
   this should by definition mean ratification has occurred." The
   drafted two-event design — agent approval first, a separate
   operator closing commit later — is gone; approval and recording
   are one event in one session. Finding A1 above described a gap
   that existed only between those two events, so it is dissolved
   rather than fixed.
3. **Record text must be intelligible to the operator.** Round 1 as
   first written could not be audited by the operator and was
   rewritten in place on this unmerged branch, on operator
   direction, before any of it entered the record. The general rule
   is filed as [m0026](m0026-legibility-standard.md).

Judgment exercised and flagged for the operator to strike: ruling 1
spoke to the closing commit. The revision also lets the draft
restatement enter by agent transcription — verbatim, attributed —
instead of requiring an operator commit there either, since the
operator's recorded acts have been session statements and merges,
not pushed commits. If the operator prefers to commit drafts
personally, that sentence reverts.

Open from Round 1: A2, A3, and A4 await the operator's disposition;
none of them was applied in this revision, which carries only the
rulings above.
