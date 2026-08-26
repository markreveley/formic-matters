---
type: refactor
title: The Formic Matters split
description: "Rename this repository to the framework, create beatcode-dev as its first consumer installation, and move the beatcode-facing matters there."
id: m0012
state: executed
status: stable
tags: [formic-matters, topology]
implements: m0001
depends_on: [m0001]
threads:
  - threads/2026-08-25-doctrine-operator-review.md
  - threads/2026-08-26-m0012-execution.md
generated:
  by: claude-code/2026-08-26
  at: 2026-08-26T00:45:00Z
verified:
  - by: human:mark
    at: 2026-08-26T05:21:39Z
ratified_commit: 85fe4511326a30516ed2bf86a2e2a2b9d05c3d25
ratified_sha256: 21492653902313ce826b53ef895b43e519eb898e7ff4a3afb69dbbe3ab54a747
---

# m0012 · The Formic Matters split

## Diagnosed reason

The operator ruled, in the
[2026-08-25 review](../threads/2026-08-25-doctrine-operator-review.md),
that the process is a consumable framework from init and that the
abstraction is ratified now (review c02, c14), that the extraction
tripwire has fired — "triggered - i have 5 which can adopt it" (review
c15) — and that the framework is named **Formic Matters** (review i1),
with this repository renamed to it and a new `beatcode-dev` created as
its first strict consumer (review c02, a1). Doctrine §13 states the
resulting topology; this matter is the restructuring that reaches it.
The repository today holds two concerns the ruling separates: the
framework — specification, tooling, process matters — and the
beatcode-facing matters it was bootstrapped around.

No behavior changes anywhere: every file keeps its content, every ID
keeps its referent; what moves is which repository carries which
concern.

## Proposed plan

1. **Rename this repository** to the framework. An operator/admin act —
   agents cannot rename repositories — performed after this matter is
   ratified and staged; GitHub redirects the old remote URLs. The
   execution record states old and new names and the date.
2. **Create the new `beatcode-dev` repository** as the first consumer
   installation. Its bootstrap is §14's generic case: the framework
   landing is the installing commits, recorded in that installation's
   first matter, with everything after entering through the process.
3. **Move the beatcode-facing matters** — m0002–m0005 and m0009, the
   matters tagged `beatcode` — into the new installation's collection,
   content verbatim. IDs are preserved; the vacated IDs are never
   reused here (§12); the new collection's own sequence allocates above
   the highest imported ID. This installation's matters — m0001,
   m0006–m0008, m0010–m0013 — stay: the framework self-hosts (review
   a1).
4. **Re-pin cross-collection references at the move.** The moved
   matters cite this repository's threads and runs as relative paths,
   which stop resolving in another repository. At the move, each such
   link becomes a pinned absolute reference — repository URL at an
   immutable commit — with every rewritten link listed in the execution
   record. Copying the cited evidence across was considered and
   rejected: it would duplicate primary sources §9.2 keeps singular.
5. **Subsequent beatcode-dev process work files there.** After the
   move, matters about beatcode or about the beatcode-dev installation
   itself belong to the new collection; matters about the framework
   belong here.

## Installation mechanism — proposed

Asked by the operator
([review r7a](../threads/2026-08-25-doctrine-operator-review.md));
proposed: **verbatim copy, pinned**.

- The consumer repository carries `doctrine/matters.md` copied verbatim
  from the framework repository at a ratified commit, the directory
  conventions (`matters/`, `threads/`, `runs/`, `tools/`), and the
  interim generator (the real tooling once m0008 ships).
- Beside the copy, an **installation record** — one small file stating
  the framework repository, the source commit SHA, and the sha256 of
  the copied specification. Anyone verifies the installation with the
  same three commands the README uses for a ratification: hash the
  copy, hash the file at the recorded commit, diff.
- **Upgrades are matters.** The consumer re-copies at a newer ratified
  commit by filing a `spec` matter in its own collection ("adopt
  framework at `<commit>`"), so framework upgrades go through the
  consumer's own process — consistent with the isolation ruling below.
- **Why copy**, over a submodule or a fetched release: the repository
  is the record (§8) and must read with no tooling (§12) — a submodule
  is a mutable pointer plus tooling, and a release channel does not
  exist until m0008 ships. The pin (repo, commit, hash) is an immutable
  reference (§9.4). A release-based channel can supersede this
  mechanism later, as its own matter.

## Dependencies across the split — ruled

The operator ruled: a consumer matter **cannot** depend on a framework
matter, or any external matter — "this may change but for simplicity
lets say this for now"
([review r7b](../threads/2026-08-25-doctrine-operator-review.md)).
Spec §7 now states it: `depends_on` names matters in the installation's
own collection only.

Consequence for the move: m0009's `depends_on: [m0008]` becomes
inexpressible when m0009 crosses collections. At the move it is
dropped from the frontmatter and restated as a prose precondition in
m0009's body (execution needs the framework tooling the installed
framework provides), a conforming edit listed in the execution record
alongside the re-pinned links.

## Scope held out deliberately

Adopting the framework into the operator's other five candidate
repositories (review c15) is not this matter: each adoption is that
installation's own bootstrap, one matter each, after this split
executes and the installation mechanics have been exercised once.

## Vetting

### Ratification — 2026-08-26

Ratified by the operator with m0001 and m0013 —
"I ratify m0001, m0012, and m0013 at commit 85fe451"
([review f1](../threads/2026-08-25-doctrine-operator-review.md)),
after accepting this matter's installation mechanism and dependency
sections in the round-2 checklist
([review k](../threads/2026-08-25-doctrine-operator-review.md), item
5: "accept, ratified"). §6 permits ratification at any round; this
matter had no fresh-agent vetting round, which the operator knew from
the act's framing. Pin: ratified region at
`85fe4511326a30516ed2bf86a2e2a2b9d05c3d25`, sha256 in the frontmatter,
recorded in
[runs/2026-08-26-ratification-recording.md](../runs/2026-08-26-ratification-recording.md).
The plan is now the contract (§3). Staging waits on nothing: the one
dependency, m0001, is executed — the operator stages this matter when
ready, and execution begins with the operator/admin acts only they can
perform (the rename, the new repository).

### Staged — 2026-08-26

`ratified → staged`, the operator's own transition (§3), directed in
the same exchange —
[review f3](../threads/2026-08-25-doctrine-operator-review.md),
"merge PR #2 and stage m0012" — together with the merge that carried
the ratified state to `main`. The §7 gate is satisfied: m0001, the one
dependency, is `executed`. No `branch` field is present: the matter is
queued, not in-flight. Execution requires, in order: the operator's
admin acts (rename this repository; create the new `beatcode-dev`),
then a dev agent the operator launches against this matter for the
mechanical steps (the moves, the re-pins, the execution record) —
§3's `staged → executed` is reachable no other way.

## Execution

**What landed — framework** (this repository, branch
`claude/formic-matters-m0012-review-14vhhy`, PR #4 against `main`;
every commit carries `Matter: m0012`):

- `70db408d9148667097b2cd052853d37d01e9f3fa` — the reference sweep
  (operator ruling R1 in
  [the exported thread](../threads/2026-08-26-m0012-execution.md)):
  36 rewrite pairs across 12 files. Mapping: the former owner account
  → `markreveley` throughout; the framework under its founding name →
  `formic-matters`; the two sites denoting the new consumer →
  `markreveley/beatcode-dev`; and one judgment call, itemized — the
  2026-08-24 audit thread's opening turn carried a link whose text
  named the beatcode clone URL and whose href named this repository;
  the href now matches its own text (`markreveley/beatcode.git`),
  adopting the reading that "clone beatcode" meant the instrument.
  The commit's diff is the site-by-site record.
- `2f403f892a9f2e0422f5dce264342a6a03917139` — m0002–m0005 and m0009
  removed, their IDs never reused here (§12); eight inbound
  references re-pinned at the sweep commit (R2): doctrine §11's m0009
  example — the one edit to the specification, breaking m0001's
  whole-file pin as the operator ruled and accepted, re-ratification
  to follow over sha256
  `9fb1f925f37c3533ffff7caba7c1094f5631e098503e06ac569841d0ef1f4c7d`;
  m0001's ledger row for m0009; m0010's m0004 worked example; and
  five evidence links in two run records (2026-08-24
  render-reproduction: m0004 twice, m0005 once; 2026-08-25
  round-2-response-verification: m0004, m0003) — an inbound class the
  plan had not enumerated. Plus: the README rewritten (the renames
  and the split stated and dated, §9.4), the index regenerated (8
  matters), the branch field set.
- `68e6c6efdd5d1e66ac3b872d74ac9ce088fba028` — the execution thread
  (§9.2) and the verification run record (§9.1).
- this commit — this record; `staged → executed` with the branch
  field removed; one R1 residue closed (the round-2 verification
  run's "worktree root" naming); and two corrections to the
  just-published run record (a mutable-branch URL pinned at the
  consumer's final bootstrap commit; a trailer-count phrasing
  scoped), made pre-merge under the same operator license that edited
  every other run record, and flagged here because §9.1 forbids
  exactly this once that license lapses at the merge.

**What landed — consumer** (`markreveley/beatcode-dev`, directly on
`main` per §14; every commit carries `Matter: m0010`):

- `1c73c02495cf08d6e63b0f8c474bd66633b32319` — the bootstrap: the
  specification byte-verbatim at
  `85fe4511326a30516ed2bf86a2e2a2b9d05c3d25`, sha256 verified equal
  to the recorded pin before the commit was made; the installation
  record; the directory conventions; the generator copy with its
  itemized edit; m0010; the README; the first index.
- `ce9d1a5197b2781ed0f8ed79d0b32bda34526ff9` — the import:
  m0002–m0005 and m0009, bodies verbatim modulo the licensed edits.
- `c6d4a3c4b29bfb1de4bd5aa7fe2e1f9b315c0038` — bootstrap corrections
  from the pre-merge adversarial review, before the operator's §11
  acknowledgment of m0010.

**Every rewritten link** (plan step 4; every pin is the repository
URL at the sweep commit, full SHA): consumer-side, nine re-pins —
m0002 frontmatter `threads:`; m0003 frontmatter `threads:` and one
Vetting run link; m0004 frontmatter `threads:` and `runs:` and three
body run links; m0005 frontmatter `runs:` and one body run link —
plus m0009's `depends_on: [m0008]` dropped and restated as a prose
precondition with its m0008 reference pinned (the plan's licensed
edit 2, its scope settled by R2), and the copied generator header's
m0008 reference; framework-side, the eight R2 re-pins itemized on the
move commit above.

**The renames** (plan step 1): this repository, `beatcode-dev` →
`formic-matters`, the operator's admin act, stated done 2026-08-26
(review f4); the owner account → `markreveley`, 2026-08-26,
mid-execution — the event that made R1 necessary: the plan's "GitHub
redirects the old remote URLs" held for neither name, the founding
name reclaimed by the consumer and the old account retired.

**Deviations** (§3.1 — each mechanical within the ratified intent, or
operator-ruled in-session (§8), rulings R1–R3 in
[the exported thread](../threads/2026-08-26-m0012-execution.md)):

1. the sweep itself — not a plan step; ratified R1;
2. the doctrine §11 edit — breaks m0001's pin; ratified R2; the pin
   follows the act (§6), so m0001's frontmatter stays until the
   operator re-ratifies over the exact corrected text;
3. the five run-record inbound links — un-enumerated by the plan;
   folded into R2;
4. m0009's body m0008 reference — between the plan's two edit classes
   as worded; folded into edit 2 under R2;
5. §14 operationalized as direct-to-`main` installing commits, with a
   third, corrective one pre-acknowledgment;
6. the ID-allocation reading (bootstrap matter = consumer m0010;
   m0001 and m0006–m0008 slots vacant there) — judged consistent with
   plan step 3, recorded per §15 on the consumer's m0010;
7. the work branch carries no m0012 prefix (§8) — the
   session-designated branch, per the a4 precedent; the PR title
   carries the prefix;
8. the README rewrite, the run record, and the index regenerations —
   conforming mechanics (§9.4, §9.1, §12) beyond the plan's literal
   steps;
9. the PR body carries the session harness's attribution footer
   beyond §8's one-line pointer;
10. the thread export applies R1's mapping to its own text, with
    redaction — declared in its header;
11. the two run-record corrections in this commit — §9.1-excepted
    under the execution's license, lapsing at merge;
12. reachability: every pin references the sweep commit on this
    branch; merging PR #4 as a merge commit (PR #2's precedent) keeps
    it reachable from `main` — otherwise this branch must be kept.

An independent five-agent adversarial review ran over the staged
trees before publication completed; its findings — two R1 residues
and three record defects — are closed in this commit and the
consumer's correction commit, and its remaining checks verified the
work clean: spec-copy hash, moved-body fidelity to the byte,
pin-target existence at the sweep commit, index determinism in both
repositories, scoped link resolution, trailer discipline.

**Executed 2026-08-26.** Actor: claude-code/2026-08-26, the dev agent
the operator launched against this matter — the launch instrument
reviewed, corrected for the renames, and ruled into execution in the
exported thread. Verification:
[runs/2026-08-26-m0012-execution-verification.md](../runs/2026-08-26-m0012-execution-verification.md).
