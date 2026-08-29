---
type: spec
title: Doctrine stops describing unbuilt enforcement as operating
description: "Six doctrine passages say a validator checks things today when no validator exists; each is rewritten to say who checks now and who will check once the tooling lands, so ratified text stops promising checks nobody runs."
id: m0025
state: proposed
status: draft
tags: [formic-matters, doctrine, integrity]
implements: m0001
sources:
  - doctrine/matters.md
generated:
  by: claude-code/2026-08-29
  at: 2026-08-29T04:30:36Z
---

# m0025 · Doctrine stops describing unbuilt enforcement as operating

Filed on operator direction in the 2026-08-29 session. That session
is not yet exported as a thread; per the practice
[m0024](m0024-declared-sources.md) proposes, the provenance gap is
held open here and the `threads` cite is added when the export
lands. The `sources` list above rehearses m0024's proposed field.

## Diagnosed reason

The doctrine defers its tooling honestly in most places: §15 "Open"
lists the validator as deferred design owned by
[m0008](m0008-matter-tooling.md), and §8 "Where discourse lives"
models the honest voice — "a commit-msg hook enforces it once the
tooling exists (m0008)."

But six passages describe that same unbuilt validator in the present
tense, as though it runs today. m0008 is `proposed`; no validator
exists; the only thing performing these checks is an agent doing
them by hand when it thinks to. A reader of ratified doctrine
therefore trusts checks nobody runs. That is the failure shape §14
"The bootstrap" records — text presenting itself as more verified
than it is — sitting inside the specification that exists to prevent
it. The operator classified this as urgent on 2026-08-29: if
unratified mechanisms are treated as operating, the process cannot
be trusted to mean what it says.

The six passages, quoted:

1. §4 "Cheap to file, expensive to ratify": "a matter is *ready*
   when its type's required sections exist, checked at the
   ratification gate (m0008)"
2. §5 "Supersession, splitting, and conflict": "The validator checks
   for the link ([m0008](m0008-matter-tooling.md));"
3. §7 "Composition — no containers": "The validator checks all of
   this ([m0008](m0008-matter-tooling.md))."
4. §9.3 "Claims DAGs": "the graph is acyclic and every referenced id
   exists (validator-checked, m0008)"
5. §10 "Deterministic wherever possible": "Anything in this process
   checkable by deterministic code is checked by deterministic
   code — schema, transitions, links, cycles, hashes, staleness,
   derived views (the validator, m0008)."
6. §11 "The retroactive path": "The validator flags retroactive
   matters so they are reviewed, late but always."

Pointing at a proposed matter is not the defect — §15 requires
deferred design to name the matter that owns it. The defect is the
indicative mood: "checks," "flags," "is checked," where nothing yet
does.

## Proposed text

Rewrite each passage on §8's model: say who checks today, and who
will check once m0008 lands. No check is removed or weakened — only
the claim of who performs it becomes true. The six replacements,
verbatim:

1. §4: "a matter is *ready* when its type's required sections
   exist — checked at the ratification gate by reviewers today, and
   by the validator once it exists (m0008)"
2. §5: "The validator, once it exists, checks for the link
   ([m0008](m0008-matter-tooling.md)); until then reviewers check it
   at the ratification gate;"
3. §7: "The validator checks all of this once it exists
   ([m0008](m0008-matter-tooling.md)); until then these
   transition-time checks are the reviewers'."
4. §9.3: "the graph is acyclic and every referenced id exists
   (checked by reviewers today, by the validator once it exists —
   m0008)"
5. §10: "Anything in this process checkable by deterministic code is
   to be checked by deterministic code — schema, transitions, links,
   cycles, hashes, staleness, derived views (the validator, m0008).
   Until that tooling exists, agents perform these checks by hand;
   §15 records the validator as deferred design."
6. §11: "The validator, once it exists (m0008), flags retroactive
   matters so they are reviewed, late but always; until then
   reviewers watch for the `## Retroactive` section."

## What this contradicts

No ratified matter, and no rule in substance: every check stays
required, every ownership pointer stays where §15 "Open" put it. It
amends only the six passages' claims about who performs the checks,
which today overstate. Nothing is superseded.

## Proposed execution plan

1. Amend the six passages exactly as quoted above; change nothing
   else in the doctrine.
2. Regenerate `matters/index.md` and record a verification run under
   §9.1 "Runs" showing the doctrine diff is exactly the six pairs.
3. Because doctrine changes, re-ratify m0001 over the amendment
   using the ratification mechanism then in force; record the pin
   only after the operator's act.
4. Append this matter's execution record, move it
   `staged → executed`, and put the branch before the operator for a
   merge-commit merge.
