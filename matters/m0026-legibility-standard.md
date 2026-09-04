---
type: spec
title: Legibility standard — record text is written to its ratifier
description: "Text the operator must act on — matter bodies, vetting entries, handoffs — is written in plain language with only defined terms, named actors, and a fixed entry structure; a glossary enters the doctrine."
id: m0026
state: proposed
status: draft
tags: [formic-matters, process, documentation, review]
implements: m0001
sources:
  - doctrine/matters.md
threads:
  - threads/2026-08-29-complexity-escape-and-working-text.md
generated:
  by: claude-code/2026-08-29
  at: 2026-08-29T04:30:36Z
---

# m0026 · Legibility standard — record text is written to its ratifier

Filed on operator direction in the 2026-08-29 session, exported at
[threads/2026-08-29-complexity-escape-and-working-text.md](../threads/2026-08-29-complexity-escape-and-working-text.md)
and cited in `threads`. The `sources` list above rehearses the
frontmatter field [m0024](m0024-declared-sources.md) proposes.

## Diagnosed reason

On 2026-08-29 the operator read a vetting entry that conformed to
every rule in force — appended per §6 "Vetting and ratification,"
correct trailer, faithful findings — and could not audit it. The
entry used terms of art without definitions ("pin," "clean review,"
"diff shape"), described acts without naming their actors ("the
review" without saying whose), and was written in the register
agents use with each other, modeled on m0001's vetting rounds. The
operator named the resulting state "complexity escape": the point
where the record outruns the one person whose acts give it force.

Every gate in this framework ends at an operator act. An artifact
the operator cannot audit turns that act into trust, and trust at
the gate is the rubber stamp §14 "The bootstrap" records — now with
better-looking paperwork. §4 "Cheap to file, expensive to ratify"
prices filing and ratifying; nothing anywhere prices reading. This
matter adds the missing requirement: text the operator must act on
must be legible to the operator, and that is a property reviewers
check, not a courtesy.

The principles below are extracted from the operator's rulings in
that session, each anchored to the operator's words:

1. **Write to the ratifier.** "I am not qualified to really audit
   your recent contributions" — an entry only agents can read has
   failed its purpose regardless of conformance.
2. **Name the actor of every act.** "When you say 'the review' do
   you mean the operator review, or the agent review of the
   operator's restatement? You need to be more explicit."
3. **No undefined terms of art.** "There should really be a ban on
   using terminology that hasn't been explicitly defined."
4. **Structure what is enumerable.** "This would fit much better
   into a scheme of sorts, some sort of semi-structured data that I
   can cross reference" — the preamble of a review entry is fields,
   not prose.
5. **Plain statement first, detail after.** "This is essentially
   unscrutable" — said of a finding whose first sentence could not
   be understood without the rest.
6. **Processes are numbered steps.** "Break every process down to
   discrete steps: 1 - actor (operator or agent) does x with these
   considerations, 2 - same statement form, next step, 3 -
   completion definition."
7. **Vocabulary drift is challenged on sight.** "Usage of
   terminology outside of this needs to be immediately called out
   by the other and drilled into — either to correctly state with
   existing terminology, or to upgrade the term to a proper defined
   word in the glossary."

## Proposed text

Six amendments.

**A glossary enters the doctrine.** A new doctrine section holds
authored, normative definitions of this framework's terms of art. A
term of art may be used in a matter body, a vetting entry, or the
handoff only if it is in the glossary or defined in bold at its
first use in the same document. The glossary is authored text —
changed only through matters — not a derived view. Seed entries,
carried by this matter verbatim:

- **pin** — the recorded pair that freezes what was accepted: a
  commit ID, which preserves the exact text in Git history forever,
  plus a hash of the accepted text. Recorded only after the
  operator's act, never offered in advance.
- **hash** (also **checksum**) — a short fingerprint computed from a
  text; any change to the text changes the fingerprint, so equal
  fingerprints mean identical text. The commit remains the source of
  truth; the stored hash exists because the matter file legitimately
  keeps changing around the accepted text (review entries append,
  state fields change), and recomputing one number is a cheaper
  drift check than re-deriving which parts were accepted. The
  tooling that verifies it is
  [m0007](m0007-ratification-content-hash.md)'s deliverable.
- **ratified region** — the part of a matter file the pin covers:
  the body minus the frontmatter and the append-only `## Vetting`
  and `## Execution` sections. m0001 is special: its pin covers the
  whole doctrine file instead.
- **contract** — a ratified matter's text, in its role after
  ratification: the thing execution is held to (§3 "State —
  mutable": "the plan is now the contract").
- **restatement** — the operator's own-words account of what a
  matter does and why, bounded by the matter and diffed against it
  ([m0017](m0017-operator-authored-ratification.md)).
- **passing verification** — a comparison of the operator's
  restatement against the matter, under
  [m0017](m0017-operator-authored-ratification.md)'s protocol, that
  found no failures; the event that completes ratification.
- **disposition** — a review entry's closing judgment: what the
  review concluded and what, if anything, it asks for.
- **recording agent** — the agent that writes lifecycle facts into a
  matter after an operator act: state changes, the pin. It records
  acts; it performs none.
- **in situ** — Latin, "in its original place." An exported review
  comment is shown in situ: quoted inside an excerpt of the exact
  text it responded to, with its file location and carrying commit —
  never in a list detached from its context. Already used,
  undefined, by §8 "Where discourse lives" and §9.2 "Threads"; the
  operator challenged it on 2026-08-29.
- **thread** — a verbatim export of a session, under `threads/`;
  never edited after export (§9.2 "Threads").
- **run** — an append-only record of a verification actually
  executed, under `runs/` (§9.1 "Runs").

**Vetting entries gain a fixed shape.** §6 "Vetting and
ratification" currently requires "(round, reviewer, findings,
disposition)". That becomes: a preamble as a field table — reviewer;
date; the commit whose text was reviewed; what was read; deviations
— rendered the same way in every entry; then findings, each opening
with an ID, the section it is about, and one plain-language sentence
stating the problem, with explanation after; then the disposition.
Prose stays where judgment lives; fields carry what is enumerable.
(Which entries exist at all is
[m0027](m0027-records-begin-at-the-gate.md)'s question — a
coordination reference, not a basis.)

**Every described act names its actor.** In record text, "the
review," "the commit," "approval" without whose is a finding. The
sentence must say who acts: the operator, the reviewing agent, the
recording agent.

**Multi-step mechanisms are written as numbered steps.** Normative
text describing a process states it as an ordered list: each step
names its actor — the operator, or an agent — and the act, in the
same sentence form throughout; the list ends by defining
completion, the observable fact that means the process is done.
[m0017](m0017-operator-authored-ratification.md)'s protocol section
is the form's first use.

**Terminology drift is challenged on sight.** When any reader —
operator or agent — meets a term of art that is in neither the
glossary nor a bold first-use definition:

1. **The reader** names the term and stops on it; unexplained
   jargon is never read past.
2. **The writer** restates the sentence in committed vocabulary, or
   proposes the term for the glossary with a plain definition.
3. **Completion:** the sentence stands only once it uses committed
   vocabulary. Glossary additions are doctrine changes and go
   through matters.

**Legibility is a standing review duty.** A reviewer of any matter,
entry, or handoff flags text the operator could not restate in their
own words — the same test
[m0017](m0017-operator-authored-ratification.md) applies to the
operator, pointed back at agents. Citation form is
[m0018](m0018-doctrine-heading-citations.md)'s rule and is not
restated here; m0017, m0018, and
[m0006](m0006-review-lenses-and-dry-rounds.md) are coordination
references only, not a basis for this matter.

## What this contradicts

No ratified matter. It amends §6 "Vetting and ratification" (the
entry shape) and adds the glossary section. It tightens, without
contradicting, the existing style the doctrine already practices in
places (§8 "Where discourse lives" defines "in-document review"
inline in bold — exactly the first-use form this matter requires
everywhere). Nothing is superseded.

## Proposed execution plan

1. Add the glossary section with the seed entries; amend §6's entry
   requirement to the fixed shape; add the actor rule, the
   numbered-steps rule, the drift-challenge protocol, and the
   legibility review duty to §6.
2. Add a standing rule to `CLAUDE.md`: write record text to the
   operator — plain first sentence, defined terms only, named
   actors, numbered steps for processes, the fixed entry shape;
   challenge undefined terms on sight.
3. Forward to [m0008](m0008-matter-tooling.md), once it exists: a
   lint that flags terms of art absent from the glossary and entries
   missing preamble fields. Whether text is legible stays a judgment
   check.
4. Regenerate `matters/index.md` and record a verification run under
   §9.1 "Runs."
5. Because doctrine changes, re-ratify m0001 over the amendment
   using the ratification mechanism then in force; record the pin
   only after the operator's act.
6. Append this matter's execution record, move it
   `staged → executed`, and put the branch before the operator for a
   merge-commit merge.
