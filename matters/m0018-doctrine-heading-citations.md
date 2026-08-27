---
type: spec
title: Doctrine citations include section headings
description: "Every authored citation to a numbered doctrine section carries the section's exact heading, so the operator can understand the reference without cross-referencing the specification."
id: m0018
state: proposed
status: draft
tags: [formic-matters, process, documentation, review]
implements: m0001
generated:
  by: codex/2026-08-27
  at: 2026-08-27T15:22:55-07:00
---

# m0018 · Doctrine citations include section headings

## Diagnosed reason

Matters and agent instructions routinely cite doctrine by number alone
— for example, `doctrine §8`. The number is precise but not
self-describing. An operator reviewing a matter must leave the text,
find the numbered section, and recover its subject before evaluating
what the citation is claimed to support. Dense ratification text can
require that lookup repeatedly, increasing review friction exactly
where the process is intended to force comprehension.

The heading already supplies the missing local context. Writing
`doctrine §8, “Where discourse lives”` tells the reviewer both where the
authority resides and what kind of rule is being invoked, without
restating the rule or replacing the underlying source.

## Proposed text

Add this authored-citation rule to doctrine §12, “Storage and format,”
as a documented dialect choice:

> Every authored citation to a numbered section of this specification includes both the section number and the section’s exact heading, in the form `doctrine §8, “Where discourse lives”`. A subsection citation uses its subsection heading, for example `doctrine §3.1, “The execution record”`. The heading is quoted as it stands in the ratified doctrine the author is citing.

Add the same rule to `CLAUDE.md` in distilled form, preserving the two
examples exactly.

## Scope and application

- The rule applies to authored text outside `doctrine/matters.md`:
  matters, agent instructions, READMEs, installation records, run
  records, authored thread apparatus, and prose in tooling or code
  comments when they cite doctrine.
- Every citation carries the heading, including repeated citations in
  one section. The rule avoids a contextual “first reference only”
  exception that would make excerpts and table rows lose their meaning.
- A citation to several sections gives each number its heading rather
  than using an unexplained range.
- The doctrine's own internal cross-references remain compact. A reader
  is already inside the document whose headings govern them, and
  expanding every internal `§N` would obscure rather than clarify the
  normative text.
- Verbatim thread turns are never altered to conform. Newly authored
  apparatus around those turns follows the rule.
- Sealed ratified regions, executed matters, append-only vetting,
  threads, and runs are not rewritten. Their compact citations remain
  accurate historical text. New or otherwise-authorized revisions use
  the heading-qualified form.
- If a later ratified matter renames a doctrine heading, historical
  citations retain the heading that was exact when authored. New text
  uses the new heading. A heading rename alone never licenses rewriting
  immutable history.

## Enforcement

Until tooling exists, authors and reviewers enforce the rule. The
heading is not a substitute for checking the cited section; it is a
local comprehension aid and an additional accuracy claim for vetting.

The deterministic portion is forwarded to
[m0008](m0008-matter-tooling.md): the doctrine heading map can be
derived mechanically, and newly authored or revised text can be checked
for a quoted heading matching each numbered doctrine citation. The
validator must honor the scope exclusions above and must not rewrite a
source. Legacy compact citations are a recorded baseline, not failures
that authorize mutation of sealed records.

## What this contradicts

No ratified matter requires number-only citations. This amends doctrine
§12, “Storage and format,” whose current link rules specify relative
internal links and pinned external references but do not require a
human-readable heading beside a numbered doctrine reference.

It deliberately rejects a repository-wide retrofit: such a sweep would
contradict the immutability and append-only rules the citations are
meant to help reviewers apply. The new rule is prospective except where
text is already legitimately open for revision.

## Proposed execution plan

1. Add the proposed dialect rule to doctrine §12, “Storage and format,”
   without changing its quoted text.
2. Add the distilled rule and both exact examples to `CLAUDE.md`.
3. Forward the scoped deterministic check to
   [m0008](m0008-matter-tooling.md) without changing immutable
   historical citations.
4. Regenerate `matters/index.md` and record a verification run under
   doctrine §9.1, “Runs,” covering the exact doctrine text, the
   `CLAUDE.md` distillation, index stability, and a representative
   heading-map check.
5. Record execution on this matter and re-ratify m0001 over the doctrine
   amendment using the ratification mechanism then in force.
6. Apply the policy to
   [m0016](m0016-launch-instructions-policy.md) during m0016's own
   proposed-state revision and vetting; do not use this matter's
   execution as authority to edit m0016 or any other matter's ratified
   region.
