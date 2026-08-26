---
type: spec
title: Contained installation layout for code-bearing consumers
description: "A consumer installation lives only inside .formic-matters/ at the repository root; the framework's own repository is the framework's home, its layout at root — not a choosable form."
id: m0014
state: proposed
status: draft
tags: [formic-matters, topology, installation]
implements: m0001
threads:
  - threads/2026-08-26-m0012-execution.md
generated:
  by: claude-code/2026-08-26
  at: 2026-08-26T19:12:11Z
---

# m0014 · Contained installation layout for code-bearing consumers

## Diagnosed reason

The conventions §12 and §14 name — `doctrine/`, `matters/`,
`threads/`, `runs/`, `tools/` — sit at the repository root. That is
right where the installation *is* the repository's content: the
framework itself, and a dedicated process repository like
`beatcode-dev`. It is intrusive where it is not: the operator's five
candidate adopters carry their own source trees, and five process
directories at their roots collide with the host's own layout. The
operator directed a contained form and its name in the m0012
execution session
([thread R7](../threads/2026-08-26-m0012-execution.md)):
".formic-matters", chosen over the shorter ".formic" because the full
name self-documents and matches the framework. A follow-up ruling
([thread R8](../threads/2026-08-26-m0012-execution.md)) settled the
scope: the contained form is for every consumer, the existing
`beatcode-dev` included — uniformity across consumers beats
grandfathering — with `beatcode-dev`'s own move directed as that
installation's own matter. Filed and revised now, before the second
adoption, so no two consumer layout generations ever exist in the
wild.

## Proposed text

Amendments to §12 and §14. There is no choice of layout anywhere in
them: a consumer installation has exactly one home, and the
framework's own root layout is not a form an installation could
elect — it is simply the framework's home.

- **§12 gains the consumer-layout clause.** A consumer installation
  lives wholly inside one containing directory at the repository
  root, named `.formic-matters/` — the only place a consumer
  installation lives. Inside the container the layout is identical
  to the framework's own (`doctrine/`, `matters/`, `threads/`,
  `runs/`, `tools/`), and because every authored link in an
  installation is relative (§12), containment changes no link. The
  framework's own repository is not an installed copy — it is the
  framework's home, its layout at its root — and the presence of an
  installation record at `.formic-matters/doctrine/installation.md`
  is what marks a consumer.
- **§14's convention sentence** places a consumer's adoption inside
  `.formic-matters/`, with the installation record at
  `.formic-matters/doctrine/installation.md`.
- **Forwarded to m0008:** the tooling locates the collection by
  probing `.formic-matters/` (a consumer), then the repository root
  (the framework's home), and operates identically on both; the
  interim generator gains the same probe if it is still in service
  when this ratifies.

## What this contradicts

No ratified matter. It amends the specification's implicit anchoring
of the conventions at the repository root (§12, §14) by making the
anchor explicit and two-valued. It reaches into no other collection:
`beatcode-dev`, bootstrapped at the root before this matter existed,
moves to the contained form through its own matter in its own
collection — directed by the operator
([thread R8](../threads/2026-08-26-m0012-execution.md)) — and until
that executes it is, knowingly, the one root-form consumer.

## Notes

The container is a dotted directory deliberately, on the `.github/`
precedent: present and readable in every listing that matters, out of
the way in the host repository's daily view. The cost considered and
accepted: dotted paths are hidden from bare `ls`, and the consumer's
README should say where the installation lives — a sentence the
bootstrap already writes.

## Vetting

### Ratification — 2026-08-26

Ratified by the operator over the revised text — "I ratify m0014
commit cb44d7e"
([execution thread R9](../threads/2026-08-26-m0012-execution.md)),
after merging the revision (PR #6, merge commit `1e12e5a`). §6
permits ratification at any round; this matter had no fresh-agent
vetting round beyond the operator's own two scope rulings (R7, R8),
which the operator knew from the exchange. Pin, following the act:
ratified region at `cb44d7e981d6f17b7349ede9cbca4b39054fa648` — the
commit the operator named, reachable from `main` and byte-identical
to `main`'s copy at recording time — sha256 in the frontmatter. The
plan is now the contract (§3).

### Staged — 2026-08-26

`ratified → staged` and the launch, directed in the same operator
turn — "run m0014 execution here" (thread R9). The dev agent is the
m0012 execution session, launched against this matter; branch
`m0014-execution` set (in-flight, §3). The §7 gate is satisfied: no
dependencies.

## Execution

Executed by the session the operator launched with "run m0014
execution here" (thread R9), on branch `m0014-execution` — PR #7
against `main`, every commit carrying `Matter: m0014`:

- `954f11bc979867d98b7b28cfbfd056154a7f21e8` — the ratification
  recording (§6, pin at the operator's named commit), the staging,
  and the amendment itself: §12's two-form layout clause; §14 naming
  both forms and the contained installation-record path; m0008's
  installation-form discovery bullet (the requirement this matter
  forwards); the interim generator's probe — `.formic-matters/`
  first, then the repository root — tested on both forms before the
  commit; the index regenerated.
- the record commit, in which this section lands — this record,
  `staged → executed` with the branch field removed, the exchange
  thread brought current through R9, and the §9.1 run record beside
  it.

The doctrine edit breaks m0001's whole-file pin — the second such
break, and the same recorded dance as the first: the operator's merge
of PR #7 and re-ratification re-pin it over sha256
`b61ea861ecba1c83f3fa0b1a12ec0b930e068f6f8cdd73517bc1e51365b03497`.
Deviations from the ratified plan: none — the four amendment bullets
landed as ratified; the probe's concrete shape (a two-line root probe
in the interim generator) is detail within "gains the same probe".
Consumer follow-through is deliberately not here: `beatcode-dev`'s
move to the contained form is its own matter in its own collection
(R8), for the next session. Date: 2026-08-26. Actor:
claude-code/2026-08-26, the dev agent the operator launched against
this matter. Verification:
[runs/2026-08-26-m0014-execution-verification.md](../runs/2026-08-26-m0014-execution-verification.md).

## Execution failure — 2026-08-26

Recorded before the transition (§3). At the m0001 re-ratification
read — over the amended document on this matter's own unmerged
branch — the operator ruled the ratified plan's central framing
wrong, at both amendment sites: "An installation lives in one of two
forms, chosen at bootstrap … this is incorrect - it should ONLY live
in .formic-matters", and the §14 mirror "also incorrct"
([execution thread R10](../threads/2026-08-26-m0012-execution.md)).
The scope ruling followed (thread R11): `.formic-matters/` applies to
client repositories only, as their sole layout with no choice
language, and the framework's own repository keeps its files at the
root — not as a "form", but as the framework's home. The operator's
question of record — whether clients-only-contained had been implied
and lost — is answered in the thread's reply: the ratified rule's
substance did assign consumers no root option, but the ratified
framing ("two forms, chosen at bootstrap") presented a choice that
was never intended, a drafting carry-over from the pre-R8 draft.

Disposition, per §3 `staged → proposed`:

- **What half-landed, and its fate:** the amendment commits
  `954f11bc979867d98b7b28cfbfd056154a7f21e8` and
  `c3d4825db3908a5222b848d812500d1f39e4c5af`, on this branch only —
  nothing reached `main`. The spec, m0008, and generator changes are
  **reverted** to `main`'s state in the failure commit; the branch
  history is kept, never rewritten. The `## Execution` section above
  stands as the halted attempt's record.
- **Ratification fields cleared into this entry:** `verified`
  human:mark at 2026-08-26T19:41:59Z; `ratified_commit`
  `cb44d7e981d6f17b7349ede9cbca4b39054fa648`; `ratified_sha256`
  `277c270cb6c5a66bf54c0799775df4f2b565d84b350e50cb4b312a8ab5190b3e`.
- **The proposed text is revised** in the same commit to the
  no-choice form, and re-ratification is required to proceed —
  `## Execution` on this matter resumes only after the operator's new
  act over the revised text.
