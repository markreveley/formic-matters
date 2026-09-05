---
type: spec
title: Rename the framework to Restate to Ratify (RTR)
description: "The framework takes the name of its central act — Restate to Ratify, short form RTR — and the doctrine, agent instructions, README, container-directory convention, and repository carry the rename."
id: m0022
state: proposed
status: draft
tags: [formic-matters, process, naming, topology]
implements: m0001
depends_on: [m0017]
threads:
  - threads/2026-08-28-restate-to-ratify.md
generated:
  by: claude-code/2026-08-28
  at: 2026-08-28T20:08:20Z
---

# m0022 · Rename the framework to Restate to Ratify (RTR)

## Proposed text

The framework's name becomes **Restate to Ratify**, short form
**RTR**. The rename is a claim about what the framework's center is:
the current name points at the unit of work (the matter); the new name
points at the act that gives the unit meaning — the operator's
restatement, and the ratification it gates
([m0017](m0017-operator-authored-ratification.md)). Everything else in
the framework — states, vetting, threads, runs, supersession — exists
to make that act evaluatable and auditable.

What the rename touches:

- **The doctrine.** The title and header prose of
  [`doctrine/matters.md`](../doctrine/matters.md) name the framework;
  they are amended, and m0001 is re-ratified over the amendment under
  the ratification mechanism then in force. The unit vocabulary is
  unchanged: a **matter** is still a matter, `matters/` is still
  `matters/`, and IDs and filenames do not move (doctrine §12,
  “Storage and format”).
- **The agent instructions and README.** `CLAUDE.md` carries the new
  name. `README.md` is rewritten in full under the new name, on
  operator direction of 2026-09-05: it describes the framework as
  Restate to Ratify, explains the restatement mechanism
  ([m0017](m0017-operator-authored-ratification.md)) and the
  lifecycle in plain language, states which mechanism is in force
  and which matters are proposed, and extends the renames-and-split
  record with this rename, stated and dated, per doctrine §9.4,
  “Immutability.” The rewrite carries the sections
  [m0021](m0021-readme-naming-lineage.md) and
  [m0029](m0029-readme-dependency-model.md) propose, adapted to name
  which mechanisms are proposed; both are coordination references,
  not a basis, and their disposition is the operator's at
  ratification. The rewritten README is working text on this
  matter's branch until the operator's act.
- **The repository.** Renamed by the operator to `rtr` on
  2026-08-29, platform-side, ahead of this matter's ratification and
  confirmed in session
  ([thread](../threads/2026-08-29-complexity-escape-and-working-text.md)).
  GitHub redirects a renamed repository, so pinned absolute URLs at
  immutable commits keep resolving; threads and runs are never
  rewritten, and their old-name URLs stand as historical record.
- **The `formic-matters` tag.** Every matter carrying the tag is swept
  to `rtr` at execution — frontmatter edits, outside every ratified
  region (doctrine §6, “Vetting and ratification”), with the index
  regenerated.
- **The container directory.** Doctrine §12, “Storage and format,” and
  executed matter
  [m0014](m0014-contained-installation-layout.md) land
  `.formic-matters/` as the only place a consumer installation lives.
  This matter proposes the successor rule: the container becomes
  `.rtr/`. Nothing leaves `executed` (doctrine §3, “State —
  mutable”), so m0014 is not reopened — this is a new matter revising
  what m0014 landed, the path §3 assigns to correcting executed work.
  The alternative — keep `.formic-matters/` for stability under the
  new name — is explicitly before the operator at ratification.
- **The consumer.** The first consumer installation carries the old
  container name and old-name references. Its migration is its own
  matter in its own collection — a dependency on another
  installation's matters is not expressible (doctrine §7,
  “Composition — no containers”) — and this matter's execution record
  notes the migration as pending on the consumer side.

## What this contradicts

The name **Formic Matters** is ratified text: the operator named the
framework in the 2026-08-25 review (m0001's rulings ledger; review
c02, review i1), and the name stands in the doctrine's ratified
header. The rename therefore lands only as a doctrine amendment with
m0001 re-ratified over it — the established path for doctrine changes.

If the container directory renames, this matter revises the layout
[m0014](m0014-contained-installation-layout.md) landed. m0014 is
`executed` and stays `executed`; the contradiction is resolved
prospectively by this matter's execution, never by rewriting m0014's
record.

The trade being made is named rather than hidden: “Formic” names the
colony — many agents, one operator — and that metaphor fits the
system's shape; “Restate to Ratify” names the mechanism instead, and
carries the thesis in the name. The operator weighs the trade at
ratification.

## Proposed execution plan

1. Amend the doctrine's title and header prose with the new name;
   change no rule text beyond the naming, except §12's container name
   if ratified with that choice.
2. Sweep `CLAUDE.md`; land the rewritten `README.md` as it stands at
   ratification, stated and dated in its renames record.
3. Sweep the `formic-matters` tag to `rtr` across the collection and
   regenerate `matters/index.md`.
4. The repository rename — the operator's act of 2026-08-29, done
   ahead of ratification — is recorded with its date in this
   matter's execution record.
5. Re-ratify m0001 over the doctrine amendment under the ratification
   mechanism then in force.
6. Append this matter's execution record, note the consumer migration
   as pending, and merge by merge commit on operator direction.
