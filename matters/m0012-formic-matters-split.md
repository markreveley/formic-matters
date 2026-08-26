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
   m0006–m0008, m0010–m0012 — stay: the framework self-hosts (review
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

## Open, to settle in vetting

- **Installation mechanics.** What "installing the framework" is,
  concretely: the specification carried verbatim at a pinned ratified
  commit, the directory conventions, and the tooling once m0008
  exists — but by what mechanism (copy, submodule, fetched release) is
  deliberately unproposed until the first real installation forces the
  choice. This matter performs one installation and must answer it for
  that installation before ratification.
- **Cross-collection `depends_on`.** m0009 (moving) carries
  `depends_on: [m0008]` (staying). Whether a consumer matter may depend
  on a framework matter, how it names it, and what the §7 gate means
  across installations is undefined in the spec. Proposed here,
  narrowly: at the move the dependency is rewritten as a pinned
  reference to the framework matter, and the gate treats a framework
  dependency as satisfied when the installed framework carries that
  matter executed; if vetting finds this wants normative text, that is
  a `spec` matter against §7, filed before this one is ratified and
  named in `depends_on`.

## Scope held out deliberately

Adopting the framework into the operator's other five candidate
repositories (review c15) is not this matter: each adoption is that
installation's own bootstrap, one matter each, after this split
executes and the installation mechanics have been exercised once.
