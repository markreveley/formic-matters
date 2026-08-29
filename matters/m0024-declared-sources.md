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

> Every newly authored or revised matter declares its normative
> basis in `sources`: the documents its reasoning rests on.
>
> - A valid source is ratified text — the doctrine, a `ratified` or
>   `executed` matter — or an append-only primary source under §9
>   (a thread, a run).
> - A `proposed` matter is never a valid source.
> - At the ratification gate every declared source must resolve and
>   qualify; a matter whose basis fails the check is not ratifiable
>   until it sheds the dependency or the source is ratified first.
> - References elsewhere in the body — a dependency edge, a
>   supersession target, a coordination pointer — declare nothing
>   and are not checked.
> - The list is the author's claim, not proof: whether it is honest
>   and complete is a vetting question; the check answers only
>   whether what is declared resolves and qualifies.
> - Existing matters lack the field; its absence there is a recorded
>   baseline, not a failure. The field is required of newly authored
>   matters from this rule forward, and added to older matters when
>   they are otherwise legitimately revised.

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
