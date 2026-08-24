# The matter doctrine

Normative definition of how changes to beatcode are proposed, vetted, and
executed. Ratified as [m0001](../matters/m0001-matter-system.md).

**Reading this document.** Every rule below was settled in conversation
with the operator. Anything raised but not settled is in §9, marked open,
and is not doctrine. Nothing here is inferred or extrapolated.

---

## 1 · What a matter is

A matter is one proposed change to beatcode, persisted as one markdown
file, vetted before any code is written.

Nothing lands in beatcode that did not begin as a matter. The proposal is
the unit of work, not the commit.

## 2 · Type — immutable

Every matter has exactly one `type`, fixed for its whole life:

| Type | For | Ratification requires |
|---|---|---|
| `feature` | new capability | detailed spec of the feature + proposed implementation plan |
| `fix` | defective behavior | diagnosis of the problem + proposed fix |
| `refactor` | restructuring without behavior change | diagnosed reason for the refactor + proposed plan |
| `spec` | change to normative text (`SPEC.md`, this doctrine) | the proposed text + what it contradicts or supersedes |

Type never changes. A matter that turns out to be the wrong type is
superseded by a new one (§5), which keeps `type` a stable query for the
life of the collection.

`spec` exists as its own type because its deliverable is normative text
rather than code, its review question is "does this contradict another
section", and in beatcode a spec change propagates to goldens and then to
render hashes — the highest blast radius in the repo.

## 3 · State — mutable

```
proposed ──▶ ratified ──▶ staged ──▶ executed
     └──────────┴──────────┴──▶ rejected · withdrawn · superseded
```

| State | Meaning |
|---|---|
| `proposed` | filed; anywhere from one sentence to a complete plan |
| `ratified` | the operator has accepted it; the plan is now the contract |
| `staged` | slotted into the dev pipeline, awaiting a dev agent |
| `executed` | the change is in beatcode |
| `rejected` | considered and declined — the record of *why not* is the artifact |
| `withdrawn` | retracted by its author before a decision |
| `superseded` | replaced or split; see §5 |

Terminal states are reachable from any state before `executed`.

## 4 · Cheap to file, expensive to ratify

The required sections in §2 are gates on **ratification**, not on filing.

A matter may be filed as a stub. A bug does not need its diagnosis to
exist before it can be reported — arriving at the diagnosis is what the
vetting process is *for*, and it may take several rounds. But no matter
reaches `ratified` without its type's required sections complete.

Completeness is therefore a checklist on the matter, not a state.

## 5 · Supersession and splitting

`superseded_by` is a list of matter IDs. One entry replaces; several
entries split. Vetting routinely reveals that a matter is secretly three
matters, and this is how that resolves — the original moves to
`superseded`, and routes to its offshoots.

Superseded matters are never deleted.

## 6 · Vetting

A matter is reviewed by fresh agents, in rounds, until the operator
ratifies it. Ratification is the operator's act alone.

That is the whole process today. Structured review lenses and an
automatic termination rule were considered and deliberately deferred as
premature — see [m0006](../matters/m0006-review-lenses-and-dry-rounds.md).

## 7 · Composition — no containers

A matter is never a container for other matters. The collection stays
flat.

A goal spanning several matters is expressed as a `spec` matter defining
what the goal *is*, plus metadata on the members:

- `implements: m0001` — this matter serves that spec
- `depends_on: [m0007, m0008]` — ordering constraint

A worklist ("what is left before the matter system is operational") is
then a filter plus a topological sort over `depends_on`. It is derived,
never authored.

Container matters are rejected because a container can never be
`executed` in its own right — it would need a permanent exception to §3.
A `spec` matter has a real deliverable and needs none.

## 8 · Storage

One matter per file, flat, in `matters/`. The bundle is
[OKF](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
v0.2: markdown, YAML frontmatter, ordinary markdown links, no tooling
required to read it.

```yaml
type: feature | fix | refactor | spec    # OKF's one required field; §2
title: <one line>
description: <one sentence>
id: m0007                                # stable short handle
state: proposed                          # §3
target: beatcode                         # repo the change lands in
implements: m0001                        # optional; §7
depends_on: [m0008]                      # optional; §7
superseded_by: [m0043, m0044]            # optional; §5
verified:                                # OKF trust; the ratification record
  - by: human:mark
    at: 2026-08-24
```

`index.md` and `log.md` are reserved by OKF and are derived artifacts.

**Views are derived.** The flat collection is the only source of truth.
Every listing, worklist, and rollup is a query over frontmatter,
regenerated and never hand-edited.

## 9 · Open — raised, not settled, not doctrine

These were surfaced in the conversation that produced m0001 and have not
been ratified. They are recorded so they are not silently adopted.

- **`type: feature` vs `type: matter`.** OKF's `type` tells a generic
  consumer what a concept *is*; `fix` is less legible to an outside
  reader than `matter` would be. Kinds were moved up to the type slot by
  operator instruction; whether that is the right OKF citizenship is
  unreviewed.
- **`branch:` as the in-flight marker.** `staged → executed` cannot
  distinguish "queued" from "a dev agent died halfway". A `branch` field
  whose presence means in-flight was proposed and not ruled on.
- **ID format.** `mNNNN`, zero-padded, allocated sequentially, never
  reused, never renamed on reclassification. Used here by necessity;
  unreviewed.
- **Filename form.** `mNNNN-slug.md`. Under OKF the concept ID is the
  file path, so the slug is part of the identity and renaming breaks
  links. Unreviewed.
- **Where the tooling lives.** §7's worklist and the §8 validator imply
  code. Whether it lives in this repo or is extracted later is open —
  see [m0008](../matters/m0008-matter-tooling.md).
- **Retroactive and emergency paths.** A red CI at 2am, and the
  back-filling of already-landed decisions, both need a route that does
  not pass through full vetting. Raised, not designed.

## 10 · The bootstrap exception

m0001 could not be vetted by the system it defines. It was written by
hand and ratified by the operator in conversation, before this text
existed — the operator agreed to the *design*, not to this wording.

That gap is exactly the failure mode that
[m0007](../matters/m0007-ratification-content-hash.md) exists to close:
ratification today is a state flag, so a document can drift after it is
ratified and a dev agent will build something never actually vetted.

This is the only matter permitted that exception. It is recorded rather
than tacit so the one un-vetted decision in the collection is visible.
