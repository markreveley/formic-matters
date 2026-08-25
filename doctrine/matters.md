# The matter doctrine

Normative definition of how changes to beatcode — and to this
repository itself — are proposed, vetted, ratified, and executed.

Authored fresh on 2026-08-24 against the operator's rulings, recorded
verbatim in the two threads this repository carries — the
[design session](../threads/2026-08-24-matter-system.md) and the
[adjudication session](../threads/2026-08-24-audit-and-adjudication.md)
— and compiled row by row in m0001's rulings ledger, each row citing
the turn it comes from. It becomes doctrine when the operator ratifies
it as a whole document (§6). Its ratification state lives on
[m0001](../matters/m0001-matter-system.md); until m0001 is ratified,
this text is a candidate.

Provenance, in one line: this is the second bootstrap. The first was
audited, adjudicated, and archived unmerged (PR #1 of this repository);
none of its doctrine or matter text was reused here. Its design session
is not archive-side — it is exported into `threads/`, because the
rulings in it govern this document and a reviewer must be able to read
them.

---

## 1 · What a matter is

A matter is one proposed change, persisted as one markdown file in
`matters/`, vetted before the change is made.

There are two targets, named by the `target` field:

- `beatcode` — the instrument.
- `beatcode-dev` — this repository: the doctrine, the tooling, the
  process itself. The system is self-hosting: its own evolution goes
  through it.

Nothing lands in either target that did not begin as a matter, with two
defined exceptions: the bootstrap (§14) and the retroactive path (§11).
The proposal is the unit of work, not the commit.

There is one collection and one ID sequence; matters for both targets
are interspersed. "All beatcode matters" is a query over `target`,
never a directory. IDs deliberately encode nothing — not type, not
target — so reclassification never moves an ID.

## 2 · Type — immutable

Every matter has exactly one `type`, fixed for its whole life:

| Type | For | Ratification requires |
|---|---|---|
| `feature` | new capability | detailed spec of the feature + proposed implementation plan |
| `fix` | defective behavior or text | diagnosis of the problem + proposed fix |
| `refactor` | restructuring without behavior change | diagnosed reason for the refactor + proposed plan |
| `spec` | change to normative text (beatcode's `SPEC.md`, this doctrine) | the proposed text + what it contradicts or supersedes |

Type never changes. A matter that turns out to be the wrong type is
superseded by a new one (§5), which keeps `type` a stable query for the
life of the collection.

`spec` is its own type because its deliverable is normative text rather
than code, its review question is contradiction, and in beatcode a spec
change propagates to goldens and then to render hashes — the highest
blast radius in either repo. Changing this type set is itself a `spec`
matter against this section.

## 3 · State — mutable

```
proposed ──▶ ratified ──▶ staged ──▶ executed
    ▲            │           │
    └────────────┴───────────┘   re-opened · execution failure
proposed ──▶ rejected · withdrawn
proposed · ratified · staged ──▶ superseded
```

| State | Meaning |
|---|---|
| `proposed` | filed; anywhere from one sentence to a complete plan |
| `ratified` | the operator has accepted the exact text; the plan is now the contract |
| `staged` | slotted into the dev pipeline, awaiting a dev agent |
| `executed` | the change is in its target, and the execution record (§3.1) is written |
| `rejected` | considered and declined — the record of *why not* is the artifact |
| `withdrawn` | retracted by its author before a decision |
| `superseded` | replaced or split; see §5 |

Transitions and their owners:

- `proposed → ratified` — the operator, and only the operator (§6).
- `ratified → staged` — the operator slots it into the pipeline.
- `staged → executed` — only through a dev agent the operator launched
  against the matter. Delegating that trigger to an orchestration agent
  would be its own future matter, never an inference.
- `staged → proposed` — execution failure: the ratified plan proved
  wrong or impossible. The failure is recorded on the matter before the
  transition — including what, if anything, half-landed in the target
  and whether it is reverted or kept via a retroactive matter (§11) —
  and re-ratification is required to proceed again.
- `ratified → proposed` — the operator re-opens a ratified matter whose
  plan is found broken before staging. The ratification fields are
  cleared, their values recorded in the vetting section.
- `proposed → rejected` — the operator declines the proposal.
  `proposed → withdrawn` — the author retracts it. Both apply to
  un-ratified proposals only; a ratified or staged matter exits through
  re-opening, failure, or supersession.
- `→ superseded` — from `proposed`, `ratified`, or `staged`, effected
  by the operator ratifying the superseding matter (§5).
- Nothing leaves `executed`; correcting executed work is a new matter.

Two licensed exceptions enter or exit outside this diagram: a
retroactive matter (§11) moves `proposed → executed` directly on
operator acknowledgment, and m0001 alone moves `ratified → executed`
at the bootstrap (§14).

A `branch` field is present exactly while a dev agent is working the
matter. Its presence is what distinguishes in-flight from queued, and
staleness checks key off it.

### 3.1 The execution record

Entering `executed` requires a final `## Execution` section on the
matter: what actually landed (commits, PR), deviations from the
ratified plan, date, actor. A matter ends as plan and reality side by
side; the next reader learns where the plan was wrong.

## 4 · Cheap to file, expensive to ratify

The required sections in §2 gate **ratification**, not filing. A matter
may be filed as a single sentence: a defect can be reported before it
is understood, and producing the diagnosis is what vetting is for — it
may take several rounds. No matter reaches `ratified` without its
type's required sections complete.

Completeness is therefore a checklist on the matter, not a state.

## 5 · Supersession, splitting, and conflict

`superseded_by` is a list of matter IDs. One entry replaces; several
entries split — vetting routinely reveals that a matter is secretly
three, and this is how that resolves. The superseded matter keeps its
record forever; superseded matters are never deleted.

**Conflict rule.** A matter that contradicts an already-ratified matter
cannot itself be ratified until the earlier one is explicitly
superseded; the supersession link must exist at ratification time. The
validator checks for the link ([m0008](../matters/m0008-matter-tooling.md));
judging *whether* two matters conflict is vetting's job. If two
already-ratified matters are later discovered to conflict, the earlier
ratification governs until the operator resolves the conflict by
superseding one of them.

## 6 · Vetting and ratification

A matter is reviewed by fresh agents, in rounds, until the operator
ratifies it. The operator may ratify at any round, including
immediately. Structured review lenses, dry-round termination, and
anchoring rules were deliberately deferred —
[m0006](../matters/m0006-review-lenses-and-dry-rounds.md).

Every round is recorded on the matter itself: an appended `## Vetting`
entry (round, reviewer, findings, disposition). Appended, never
rewritten — the matter accretes its review history.

**Ratification is the operator's act alone, over the exact text.** The
operator reads the matter as it stands at a specific commit and states
ratification. The recording agent then writes into the frontmatter:
`verified` (actor and datetime), `ratified_commit` (the commit read),
and `ratified_sha256` — a hash of the matter's **ratified region**: the
body minus the frontmatter and the append-only record sections
(`## Vetting`, `## Execution`), so lifecycle appends and frontmatter
transitions never invalidate it. Where a matter's proposed text is a
separate document (m0001 → this doctrine, which has no frontmatter),
the hash is that document's whole file at the same commit. The hash is
agent-computed and independently verifiable — anyone can recompute it
from the named commit at any time; the operator computes nothing.

A matter that enters `executed` by the retroactive path (§11) is
acknowledged rather than ratified in advance, and what the operator
acknowledges includes what already landed. For that path alone the
hashed region additionally covers `## Retroactive` and `## Execution`
as they stand at the acknowledged commit; nothing leaves `executed`
(§3), so those sections do not move afterwards.

**The pin follows the act, never precedes it.** The commit and hash are
recorded *after* the operator states ratification, from the commit the
operator names; a pin computed in advance and offered as ready is never
the ratification record, because the text moves under it the moment the
matter is revised. Detecting post-ratification drift mechanically is
[m0007](../matters/m0007-ratification-content-hash.md).

## 7 · Composition — no containers

A matter is never a container for other matters; the collection stays
flat. A goal spanning several matters is a `spec` matter defining what
the goal *is*, plus metadata on the members:

- `implements: m0001` — this matter serves that spec
- `depends_on: [m0007, m0008]` — execution-order constraint

`depends_on` is enforced at transition time: a matter cannot be staged
or executed while a dependency is unexecuted. The retroactive path
(§11) is exempt — it exists for work that cannot wait and never passes
through `staged`; a retroactive matter names its unexecuted
dependencies in its `## Retroactive` section instead of being blocked
by them. The validator checks both
([m0008](../matters/m0008-matter-tooling.md)).

A worklist ("what is left before X is operational") is a filter plus a
topological sort over `depends_on` — derived, never authored. Container
matters are rejected because a container could never be `executed` in
its own right; a `spec` matter has a real deliverable and needs no
exception.

## 8 · Where discourse lives

The repository is the record. Review, rulings, and decisions live in
the tree: vetting entries on matters (§6), threads (§9.2), runs (§9.1).

- The operator's channel is local file edits, committed and pushed —
  not platform comments. Agents read rulings from the tree.
- GitHub is transport and merge mechanics. A pull request is a diff
  boundary and a gate; its body is a one-line pointer; its comment
  surface is unused. If the platform changes, the record does not.
- **Git citation.** Every commit carries a `Matter: mNNNN` trailer, and
  branch names and PR titles are prefixed with the matter ID. The
  trailer survives squashes and makes `git log` greppable by matter; a
  commit-msg hook enforces it once the tooling exists (m0008).

## 9 · Evidence

### 9.1 Runs

`runs/` holds append-only verification records: one file per run,
stating the claim(s) tested (with links to the matters they support),
the environment (OS, kernel, architecture, toolchain and tool
versions), the exact commands, expected versus observed results, the
verdict, the date, and the actor. A run file is never edited after the
fact; a superseding run is a new file.

### 9.2 Threads

`threads/` holds verbatim session exports — primary sources, like
goldens: human and agent turns verbatim, reasoning and tool traffic
omitted, redaction applied before publication. Threads are never
derived or summarized in place; every view over them (indexes,
matter-to-thread maps) is derived from frontmatter. Which sessions are
exported, and by what mechanism, is
[m0011](../matters/m0011-thread-persistence.md).

### 9.3 Claims DAGs

When a diagnosis rests on more than roughly three non-obvious claims —
or whenever a matter carries the `claims-dag` tag, which the operator
or any reviewer may add to demand the form — the matter carries a
`## Claims` section: the argument as an explicit DAG, one claim per
row:

| id | claim | evidence | rests on |
|---|---|---|---|

Rules: leaves cite mechanically checkable evidence — a `file:line` at
an immutable ref, a `runs/` entry, or `arithmetic` — or must be
decomposed further; non-leaves list their premises by id; the final
claim is the verdict; the graph is acyclic and every referenced id
exists (validator-checked, m0008). Audit protocol: verify every leaf
independently, then check each edge; a dispute is filed against a claim
id, and its blast radius is exactly the sub-tree above that claim. A
Mermaid rendering may be derived from the table; the table is the
source.

### 9.4 Immutability

Matters and their evidence cite immutable references — commit SHAs,
frozen files, run records. Mutable state ("not pushed", "currently on
main") is not asserted, or is explicitly dated.

## 10 · Deterministic wherever possible

Anything in this process checkable by deterministic code is checked by
deterministic code — schema, transitions, links, cycles, hashes,
staleness, derived views (the validator, m0008). Agents are reserved
for judgment: whether a diagnosis is correct, whether a plan is good,
whether scope is right. Ratification is the operator's alone.

## 11 · The retroactive path

Some work cannot wait for vetting: an emergency fix while CI is red, or
the backfilling of decisions already made. The path: act, then file the
matter as `proposed` with the evidence attached (commits, runs) and a
`## Retroactive` section stating why this path was used. Explicit
operator acknowledgment, recorded in `verified`, moves it directly to
`executed` (§3), over a hashed region that includes what landed (§6).
The `depends_on` gate of §7 does not apply on this path. If the
operator declines, the matter is `rejected` and a new matter is opened
to unwind what landed. The validator flags
retroactive matters so they are reviewed, late but always.
This path is already needed by
[m0009](../matters/m0009-spec-gaps-to-matters.md) and
[m0011](../matters/m0011-thread-persistence.md).

## 12 · Storage and format

One matter per file, flat, in `matters/`. Filenames are
`mNNNN-slug.md`; IDs are `mNNNN`, zero-padded, allocated sequentially,
never reused, never renamed. IDs are unique within this collection; the
archived first attempt is a separate, closed collection.

The format is **OKF v0.2 as a documented dialect, not a
certification** — markdown with YAML frontmatter, readable with no
tooling. The dialect choices, recorded deliberately:

- links are plain relative paths (an OKF-conformant form that also
  resolves everywhere GitHub renders markdown);
- timestamps are ISO 8601 datetimes with an explicit UTC offset;
- `state` (§3) is ours; OKF's `status` is carried alongside and derived
  mechanically from it — `proposed → draft`;
  `ratified`/`staged`/`executed → stable`;
  `rejected`/`withdrawn`/`superseded → deprecated` — so a generic OKF
  consumer reads lifecycle correctly. `status` is never set by hand.
- wherever OKF conflicts with a real need, this doctrine wins and the
  deviation is recorded here.

Frontmatter schema — every field that may appear:

```yaml
type: feature | fix | refactor | spec   # OKF's one required field; §2
title: <one line>
description: "<one sentence — quote it; unquoted colons break YAML>"
id: m0007                               # §12
state: proposed                         # §3
status: draft                           # derived from state; never hand-set
target: beatcode | beatcode-dev         # §1
tags: [render, process]                 # free labels; views filter on them,
                                        # semantics live where a query uses them
implements: m0001                       # optional; §7
depends_on: [m0008]                     # optional; §7
superseded_by: [m0043, m0044]           # optional; §5
branch: m0007-ratification-hash         # optional; present only while in-flight; §3
threads: [threads/2026-08-24-audit-and-adjudication.md]   # optional; §9.2
runs: [runs/2026-08-24-render-reproduction.md]            # optional; §9.1
generated:                              # OKF provenance: who wrote this content
  by: claude-code/2026-08-24
  at: 2026-08-24T22:30:00Z
verified:                               # the ratification record; §6
  - by: human:mark
    at: 2026-08-24T23:00:00Z
ratified_commit: <sha>                  # §6; written at ratification
ratified_sha256: <hash>                 # §6; whole-file, agent-computed
```

`index.md` and `log.md` are reserved by OKF and are derived artifacts.
**Views are derived.** The flat collection is the only source of truth;
every listing, worklist, and rollup is regenerated
(`tools/gen-index.py` today, m0008 properly) and never hand-edited.

## 13 · Topology and the extraction tripwire

One repository governs itself and beatcode (§1). The doctrine is
latently general, and deliberately not yet extracted: a framework with
one consumer teaches its boundary by being used, not by being split.

The process moves to its own framework repository when any of these
fires: a second consumer repository actually adopts it; the tooling
matures into a released binary wanting its own cadence; doctrine
changes start being motivated by non-beatcode needs. Until then, no
split. Extraction stays mechanical because the collection is flat and
frontmattered.

## 14 · The bootstrap record

This document and the initial collection (m0001–m0011) were written in
one motion, before ratification — the one permitted out-of-order
execution, this time visible and pinned: authored against the operator
rulings in the thread named in the header, with m0001 carrying the
state, and ratification (§6) recording the exact commit and hash the
operator read.

The first attempt at this bootstrap was audited, adjudicated, and
archived unmerged (PR #1). Its central failure — a document ratified
without being read, then misdescribed to the operator — is why §6
requires ratification over the exact text and why m0007 exists.

## 15 · Open, and adopted by default

Design that is deliberately deferred lives in the matters that own it:
review structure (m0006), drift tooling (m0007), the validator and its
language (m0008), risk tiers (m0010), thread policy scope and mechanism
(m0011). Anything appearing in neither this document nor a matter is
not doctrine.

Six choices in this document and the collection are the authoring
agent's, adopted without an operator ruling. Five were presented to the
operator in the adjudication thread before authoring and left unruled.
One of them — the ratified-region definition, second in the list below
— was written later, in the round 1 response, answering a finding on
[m0007](../matters/m0007-ratification-content-hash.md); what the
operator saw before saying "apply" was the narrower "body-only hash"
form, and what landed also excludes `## Vetting` and `## Execution`.
Ratifying this document confirms all six; they are listed here so the
confirmation is deliberate, not silent:

- the ratification recording mechanism of §6 — operator reads and
  states, agent computes and records the hash;
- the ratified-region definition of §6 (body minus frontmatter and
  record sections);
- the single interspersed ID sequence over both targets (§1), and the
  ID restart at m0001 with the archive as a separate closed collection
  (§12);
- the extraction tripwire's specific conditions (§13);
- the extension of "views are derived" to threads — maps and indexes
  over threads derived from frontmatter (§9.2);
- bundle-first sequencing: m0002–m0005 filed `proposed`, ratified after
  this document (implicit in the collection's state).
