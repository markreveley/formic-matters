---
type: spec
title: The matter system
description: "Every change to beatcode or to this repository is proposed, vetted, and ratified as a matter before it is made."
id: m0001
state: proposed
status: draft
target: beatcode-dev
tags: [doctrine, bootstrap]
threads: [threads/2026-08-24-audit-and-adjudication.md]
generated:
  by: claude-code/2026-08-24
  at: 2026-08-24T22:33:00Z
---

# m0001 · The matter system

## Diagnosed reason

Changes to beatcode were being identified, diagnosed, and applied in
one unbroken motion, with no gate between noticing a problem and
editing the repo. A first attempt to fix this bootstrapped a process
doctrine, and failed its own audit: the doctrine was marked ratified
without the operator having read it, its execution summary misdescribed
the committed text, and its flagship matter punted a diagnosis whose
answer sat in the repository the whole time. The operator ruled to
archive that attempt unmerged (PR #1) and author this one fresh.

beatcode is a repository whose thesis is that behavior is pinned in
advance and verified against frozen goldens. Its development process
now has the same discipline — including over itself.

## Proposed text

[`doctrine/matters.md`](../doctrine/matters.md), in full. Ratifying
this matter is ratifying that document at a specific commit (doctrine
§6).

## What this supersedes

Nothing in this collection — it is the first matter. The archived first
attempt is referenced, not superseded: this collection stands alone.

## Rulings ledger

Every operator proposal and ruling from the 2026-08-24 sessions, and
where it landed. This table is what the fidelity review checks the
doctrine against, alongside the thread itself.

| Operator proposal / ruling | Landed |
|---|---|
| three change kinds as matter types; "proposal" not a type; types moved up one level | doctrine §2 |
| per-type required content (fix: diagnosis + fix; feature: spec + plan; refactor: reason + plan) | doctrine §2 |
| state spine `proposed → ratified → staged → executed` | doctrine §3 |
| vetting by fresh agent reviews until the operator ratifies | doctrine §6 |
| execution by a dev agent launched by the operator; orchestration later, as its own matter | doctrine §3 |
| cheap to file, expensive to ratify; diagnosis may arrive over several turns but precedes ratification | doctrine §4 |
| split functions as supersession routing to offshoots | doctrine §5 |
| flat collection, metadata-sortable, all views derived | doctrine §1, §7, §12 |
| deterministic code wherever possible | doctrine §10 |
| lenses/dry-round review machinery deferred as premature, filed as a matter | [m0006](m0006-review-lenses-and-dry-rounds.md) |
| ratification content hash deferred unless MVP-required; record now, tooling later | doctrine §6 + [m0007](m0007-ratification-content-hash.md) |
| "matter system operational" as a derived worklist view | doctrine §7 |
| SPEC-GAPS broken out into matters, landed and otherwise; `spec` as a real type | [m0009](m0009-spec-gaps-to-matters.md), doctrine §2 |
| PRs cite matter IDs | doctrine §8 (commit trailer, branch/PR title prefix) |
| process/system code kept separate from the instrument | [m0008](m0008-matter-tooling.md) |
| consider OKF; keep the useful shape, no memory files in the repo | doctrine §12 (documented dialect) |
| thread persistence: verbatim human and agent turns, reasoning and tool traffic dropped, redact before publication | doctrine §9.2 + [m0011](m0011-thread-persistence.md) |
| runs directory documenting verification runs with environment specs | doctrine §9.1 |
| claims-DAG in the matter itself, visualization derived, nodes are not matters | doctrine §9.3 |
| retire PR comments; keep GitHub and PRs as transport and merge mechanics; operator responds by local file edits | doctrine §8 |
| one repo, self-hosting explicit, no framework split; extraction on tripwire | doctrine §1, §13 |
| archive the first attempt, do not expunge; fresh authoring, nothing textual carried | doctrine §14, this matter |
| landed/execution record required to enter `executed` | doctrine §3.1 |
| git citation convention (trailer + prefixes) | doctrine §8 |
| threads primary reference; adjudication thread exported into this tree; views over threads derived | doctrine §9.2, [threads/2026-08-24-audit-and-adjudication.md](../threads/2026-08-24-audit-and-adjudication.md) |
| ratification without operator-computed hashes: operator reads and states; agent records commit + hash, independently verifiable | doctrine §6 |
| org/assertions question is cross-repo and out of scope here | this section |

## Scope held out deliberately

The MVP line is **file · query · cannot corrupt**. Deferred to their
own matters rather than built now: review structure
([m0006](m0006-review-lenses-and-dry-rounds.md)), drift tooling
([m0007](m0007-ratification-content-hash.md)), the validator
([m0008](m0008-matter-tooling.md)), risk tiers
([m0010](m0010-risk-tiers.md)), thread policy
([m0011](m0011-thread-persistence.md)).

The operator's global-CLAUDE.md/assertions question raised in the first
attempt's session is cross-repo by definition and out of scope for this
collection.

## Execution

The tree was written together with this matter (doctrine §14): the
doctrine, matters m0001–m0011, the derived index, the first thread
export, the first run record, and the interim index generator. This
section is completed with commits and date when the matter reaches
`executed`, which under §14 happens immediately after ratification.
