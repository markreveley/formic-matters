---
type: refactor
title: The Formic Matters split
description: "Rename this repository to the framework, create beatcode-dev as its first consumer installation, and move the beatcode-facing matters there."
id: m0012
state: proposed
status: draft
tags: [formic-matters, topology]
implements: m0001
depends_on: [m0001]
threads:
  - threads/2026-08-25-doctrine-operator-review.md
generated:
  by: claude-code/2026-08-26
  at: 2026-08-26T00:45:00Z
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
