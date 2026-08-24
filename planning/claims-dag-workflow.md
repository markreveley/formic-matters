# Claims-DAG workflow — proposal

Status: draft for operator review, ordered in the adjudication session
of 2026-08-24 ("proceed with documenting dag workflow proposal").
Intended home once the fresh bundle exists: a doctrine section or its
own matter. This file is planning material, not part of any bundle.

## Problem

An evidence-heavy matter (a diagnosis of the m0004 class) is an
argument: a conclusion resting on claims resting on repo evidence.
Written as prose, the argument can only be audited by re-deriving it
whole, and disagreement has no address — a reviewer who doubts the
conclusion must re-litigate everything. The original m0004 punted a
diagnosis whose evidence chain was five nodes deep and fully in-repo;
nobody could see that, because the chain was never laid out as a chain.

## Proposal

A matter whose diagnosis rests on a chain of non-obvious claims carries
a `## Claims` section: the argument as an explicit DAG, one claim per
row. No new file types, no new matter types — the DAG lives inside the
matter that owns it.

Worked example (the track-length diagnosis as it should have shipped):

| id | claim | evidence | rests on |
|---|---|---|---|
| C1 | kit buffer lengths are pinned exactly | `SPEC.md:681-685` at `seed` (`91188a5`) | — |
| C2 | four.bc highest touched frame index = 94,529 | runs/ entry (events golden + C1, §9.1 placement) | C1 |
| C3 | the oracle's four.bc render = 116,579 frames | `SPEC.md:793-795` at `seed` — prose and header hex | — |
| C4 | 94,529 + 22,050 = 116,579 | arithmetic | C2, C3 |
| C5 | the 22,049-frame tail is the oracle's own behavior; "off-by-one introduced in this implementation" is refuted | — | C4 |

## Rules

1. **Leaves cite mechanically checkable evidence**: a `file:line` at a
   stated immutable ref, a `runs/` entry, or `arithmetic`. A leaf an
   agent cannot verify by opening the citation is not a leaf —
   decompose it further.
2. **Non-leaves list their premises** by claim id. The final claim is
   the matter's verdict.
3. **It is a DAG**: acyclic, and every referenced id exists. Both are
   validator checks (goes on the tooling matter's scope list).
4. **Audit protocol**: verify every leaf independently, then check each
   edge — does the claim follow from its premises? A disagreement is
   filed against a claim id, not against the matter ("C3 disputed:
   ..."), and its blast radius is exactly the sub-tree above that
   claim, nothing else.
5. **Immutability discipline**: evidence citations use immutable
   references (commit SHAs, frozen run files) — never mutable state
   ("currently on main", "not pushed").

## Derived visualization

The table is the source of truth. A Mermaid `graph TD` can be generated
from it (hand-written until tooling exists — GitHub and most markdown
viewers render Mermaid natively; in a terminal the table itself is the
readable form). The diagram is never edited by hand: views are derived.

## When required

Not for every matter — a README-wording fix gains nothing from
ceremony. Required when a diagnosis rests on more than roughly three
non-obvious claims, or whenever the matter carries the `claims-dag` tag
(the operator or any reviewer can demand the form by adding the tag).
If risk tiers exist, high-tier diagnoses default to requiring one.

## Cost and failure modes

- The authoring cost is mostly the cost of actually having the
  argument: prose that cannot be decomposed into this form was not an
  argument yet.
- The known laundering risk is a fat "leaf" hiding an inference. The
  leaf rule (mechanically checkable, or decompose) is the guard, and
  auditors should attack leaves first.
