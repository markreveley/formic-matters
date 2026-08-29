---
type: spec
title: Declared sources — authored matters carry their provenance
description: "Every authored or revised matter declares the sources its reasoning rests on in a sources frontmatter list, and at the ratification gate every declared source is ratified text or append-only evidence — never a proposed matter."
id: m0024
state: proposed
status: draft
tags: [formic-matters, process, provenance, integrity]
implements: m0001
sources:
  - doctrine/matters.md
threads:
  - threads/2026-08-29-minimal-handoff-and-declared-sources.md
generated:
  by: claude-code/2026-08-29
  at: 2026-08-29T00:24:26Z
---

# m0024 · Declared sources — authored matters carry their provenance

Filed on operator direction; the directing session is exported at
[threads/2026-08-29-minimal-handoff-and-declared-sources.md](../threads/2026-08-29-minimal-handoff-and-declared-sources.md)
and cited in `threads`, per this matter's own rule below.

## Diagnosed reason

An agent authoring or revising a matter assembles its reasoning from
somewhere: the doctrine, other matters, threads, runs, the operator's
live direction. Nothing in the record says where. When one of those
somewheres is a `proposed` matter, unratified text starts governing
new text silently — the authoring session treats a candidate rule as
if it were in force, the new matter inherits the assumption, and the
dependency is invisible: the record shows what was written but not
what it rested on.

The companion rule proposed for doctrine §8, “Where discourse lives”
(carried by [m0016](m0016-launch-instructions-policy.md)), states
that a proposed matter is never citable as the basis for a rule, an
assumption, or an act. That rule needs a surface to check against. A
declared source list gives it one: the author states the matter's
normative basis, vetting judges whether the declaration is honest and
complete, and a deterministic check verifies that everything declared
qualifies. Provenance the author must state is provenance a reviewer
can dispute.

## Proposed text

Amend doctrine §12, “Storage and format,” in two places.

First, add `sources` to the frontmatter schema:

```yaml
sources:                                # normative basis; §12
  - doctrine/matters.md
  - matters/m0014-contained-installation-layout.md
```

Second, add this rule as a documented dialect choice:

> Every newly authored or revised matter declares its normative basis in `sources`: the documents its reasoning rests on. A valid source is ratified text — the doctrine, a `ratified` or `executed` matter — or an append-only primary source under §9 (a thread, a run). A `proposed` matter is never a valid source. At the ratification gate every declared source must resolve and qualify; a matter whose basis fails the check is not ratifiable until it sheds the dependency or the source is ratified first. References elsewhere in the body — a dependency edge, a supersession target, a coordination pointer — declare nothing and are not checked. The list is the author's claim, not proof: whether it is honest and complete is a vetting question; the check answers only whether what is declared resolves and qualifies. Existing matters lack the field; its absence there is a recorded baseline, not a failure — the field is required of newly authored matters from this rule forward, and added to older matters when they are otherwise legitimately revised.

Operator direction reaches the list through its recorded form: the
thread that preserves the direction, or the ruling compiled onto a
ratified matter. Direction not yet exported is cited by the matter's
`threads` entry when the export lands; until then the vetting round
holds the gap open as an ordinary finding.

## Enforcement

Until tooling exists, authors and reviewers enforce the rule: the
authoring agent writes the list; the vetting round reads it against
the matter and flags an undeclared load-bearing source or a declared
source that is `proposed`.

The deterministic portion is forwarded to
[m0008](m0008-matter-tooling.md): each `sources` entry resolves to a
repository path or matter ID; each matter entry's state is `ratified`
or `executed` at the transition being validated; each path entry is
the doctrine or lies under `threads/` or `runs/`. What the author
actually relied on is not machine-checkable, and per doctrine §10,
“Deterministic wherever possible,” the validator must not pretend
otherwise: completeness and honesty stay judgment.

## What this contradicts

Nothing in ratified text. It amends doctrine §12, “Storage and
format,” whose schema carries evidence fields (`threads`, `runs`) but
no statement of what a matter's reasoning rests on. It is the
checkable half of the authority rule proposed in
[m0016](m0016-launch-instructions-policy.md), and a sibling of
[m0018](m0018-doctrine-heading-citations.md): m0018 governs the form
of a doctrine citation, this matter governs the standing of every
declared source. Neither is a basis for this matter — both are
coordination references — and this matter's own `sources` list is the
first rehearsal of the rule it proposes.

## Proposed execution plan

1. Add the `sources` schema entry and the dialect rule to doctrine
   §12, “Storage and format,” without changing the quoted text.
2. Add a distilled standing rule to `CLAUDE.md`: declare the sources
   a matter rests on; never rest one on a `proposed` matter.
3. Forward the deterministic check to
   [m0008](m0008-matter-tooling.md).
4. Regenerate `matters/index.md` and record a verification run under
   doctrine §9.1, “Runs,” covering the exact doctrine text, the
   schema example, and the check's flag on a constructed violation.
5. Because doctrine changes, re-ratify m0001 over the amendment using
   the ratification mechanism then in force; record the pin only
   after the operator's act.
6. Append this matter's execution record, move it
   `staged → executed`, regenerate the index, and put the completed
   branch before the operator for a merge-commit merge.

## Vetting

### Round 1 — 2026-08-29

| | |
|---|---|
| Reviewer | claude-code/2026-08-29 — the session recording the operator's 2026-08-29 rulings; also the author of this entry's companion filings |
| Matter text reviewed | as of commit `54b8362` (unchanged since filing) |
| Launched by | operator direction in-session |
| Source | this session's thread — export pending operator direction; the provenance gap this matter's own text prescribes holding open |

**Operator direction of record.** The operator judged the standing
of proposed matters a near-emergency: unratified text must not
govern anything, and the rules that make that checkable — this
matter, and the companion authority paragraph carried by
[m0016](m0016-launch-instructions-policy.md) — move ahead of
everything else, [m0017](m0017-operator-authored-ratification.md)
included. This direction replaces the prior working order.

Two findings, then the checks that passed.

**B1 — The ratified doctrine itself contains six passages that
describe unbuilt tooling as if it were running.** They speak in the
present tense about a validator that does not exist (m0008 is
`proposed`): in §4 "Cheap to file, expensive to ratify," §5
"Supersession, splitting, and conflict," §7 "Composition — no
containers," §9.3 "Claims DAGs," §10 "Deterministic wherever
possible," and §11 "The retroactive path." A reader trusts checks
nobody runs. This matter's rule cannot catch that: it governs what
newly written matters rest on, not the doctrine's own wording. The
correction is therefore filed separately as
[m0025](m0025-doctrine-enforcement-voice.md), which quotes all six
and gives each replacement verbatim.

**B2 — advisory.** The quoted dialect rule in "Proposed text" is one
dense ten-line paragraph. By the standard proposed in
[m0026](m0026-legibility-standard.md), it should be broken into
readable pieces before the operator restates it. No content change
implied; the operator may also accept it as is.

Checked and found correct: this matter can go first — it depends on
nothing, and its plan step 5 says "the ratification mechanism then
in force," so it does not wait on m0017; its Enforcement section
already uses the honest who-checks-today voice that B1 asks of the
doctrine; its own `sources` list follows the rule it proposes; all
links resolve; the frontmatter is schema-valid.

Disposition: sound as filed; B2 is optional wording. The next act is
the operator's: read this matter and
[m0025](m0025-doctrine-enforcement-voice.md), then ratify under the
current verbal mechanism of §6 "Vetting and ratification," direct a
revision, or direct another round.
