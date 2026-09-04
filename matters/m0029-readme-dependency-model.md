---
type: spec
title: README explains the lifecycle as dependency management
description: "The README gains a conceptual section: a ratified matter is a published version, the pin its identifier, re-ratification a new version, challenged a yank, declared sources the manifest, and the dependency gate the resolver."
id: m0029
state: proposed
status: draft
tags: [formic-matters, documentation]
implements: m0001
depends_on: [m0024, m0028]
sources:
  - doctrine/matters.md
threads:
  - threads/2026-08-29-complexity-escape-and-working-text.md
generated:
  by: claude-code/2026-08-29
  at: 2026-08-29T05:51:58Z
---

# m0029 · README explains the lifecycle as dependency management

Filed on operator direction in the 2026-08-29 session, exported at
[threads/2026-08-29-complexity-escape-and-working-text.md](../threads/2026-08-29-complexity-escape-and-working-text.md)
and cited in `threads`.

## Diagnosed reason

The lifecycle's vocabulary — proposed, ratified, pins, supersession,
challenged — is defined precisely in the doctrine but explained
nowhere by analogy to something a newcomer already knows. On
2026-08-29 the operator named the analogy that fits and directed
this filing: "interesting how the analogy is drifting to dependency
management, this may be an analogy we want to explore further …
this would be a great conceptual description for the readme."

A README section gives every future reader the model in one page
without touching normative text: the doctrine stays the law; the
README explains it. The README changes only through matters
(precedent: [m0021](m0021-readme-naming-lineage.md), a coordination
reference, not a basis).

`depends_on` names [m0024](m0024-declared-sources.md) and
[m0028](m0028-challenged-state.md) because the section describes
the sources manifest and the challenged state: it must not land in
the README before those mechanisms exist, and the dependency gate
of §7, “Composition — no containers,” holds it to that order —
reviewers enforce the gate today, the validator once it exists
([m0008](m0008-matter-tooling.md)).

## Proposed text

The README gains the following section, verbatim:

> ## The lifecycle, as dependency management
>
> A ratified matter is a published package version. Its pin — the
> recorded commit and content hash — is the version identifier:
> exact, immutable, checkable forever. Until ratification a matter
> is unpublished working text: it is revised freely on the
> operator's direction, and nothing may depend on it.
>
> Publication is what creates obligations. Once ratified, a matter
> can become a dependency — of doctrine amendments, of other
> matters, eventually of code. So ratified text is never edited in
> place and never un-published:
>
> - To change it, publish a new version: re-ratification, a fresh
>   pin recorded beside the old one.
> - To dispute it, yank it: the `challenged` state. Existing
>   dependents are put on notice, new dependents are stopped, and
>   the record of what was law stays intact.
> - To replace it, supersede it: a new matter takes over, and the
>   old one keeps its history forever.
>
> The `sources` list is the dependency manifest: each matter
> declares what its reasoning rests on, and only published
> (ratified) text qualifies. The execution-order gate over
> `depends_on` is the resolver: nothing builds until everything it
> depends on has shipped.

The doctrine governs; this section explains. If the two ever
disagree, the section is the defect.

## What this contradicts

No ratified matter, and no normative text: it adds an expository
README section. Definitions stay in the doctrine.

## Proposed execution plan

1. Add the section to the README, verbatim — after the
   naming-and-lineage section if
   [m0021](m0021-readme-naming-lineage.md) has executed by then,
   otherwise where the document's flow puts a conceptual overview.
2. The doctrine is untouched, so m0001's pin is not disturbed and
   no re-ratification is needed.
3. Append this matter's execution record, move it
   `staged → executed`, regenerate `matters/index.md`, and put the
   branch before the operator for a merge-commit merge.
