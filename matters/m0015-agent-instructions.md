---
type: spec
title: Agent instructions file
description: "A root CLAUDE.md distilling the standing rulings into the one channel that reaches every agent session before it reads anything else; it distills the doctrine and never overrides it."
id: m0015
state: executed
status: stable
tags: [formic-matters, process, tooling]
implements: m0001
threads:
  - threads/2026-08-26-m0012-execution.md
generated:
  by: claude-code/2026-08-26
  at: 2026-08-27T01:39:32Z
verified:
  - by: human:mark
    at: 2026-08-27T02:10:06Z
ratified_commit: 60b7a4655f4109f14590bd81bc1c7aae7924687e
ratified_sha256: 06782accfd9f856a272092081cc096b0a6167c58b879689d16544471f939b23e
---

# m0015 · Agent instructions file

## Diagnosed reason

Standing rulings reach agents unreliably. m0014's execution failure
is the live case: the r2 principle (no instance state in normative
text) was in the record, in the doctrine's own history, and in the
authoring agent's context — and a drafting carry-over still walked
past it, caught only at the operator's ratification read. The
operator asked what raises the odds of rulings surfacing to agents
([thread R12](../threads/2026-08-26-m0012-execution.md)); the layered
answer — normative text, the rulings ledger, mechanical checks
(m0008), fresh-agent rounds, the operator's read — was missing its
first layer: `CLAUDE.md`, the file the Claude Code harness loads into
every session in this repository automatically, before the agent
reads anything else. The operator directed its creation
([thread R13](../threads/2026-08-26-m0012-execution.md)).

## Proposed text

[`CLAUDE.md`](../CLAUDE.md) at the repository root, as landed with
this filing: what the repository is, what to read first, and the
standing rules distilled — the matter gate, the operator's
transitions, pin-follows-the-act and the pin regimes, append-only
threads and runs, no client names in current voice, relative links in
and pinned absolute references out, merge-commit merges, trailers and
prefixes, the derived index, and the consumer-only container. One
subordination clause governs the whole file: it distills and never
overrides — `doctrine/matters.md` wins wherever they differ.

## What this contradicts

Nothing. The file states no rule of its own; every line traces to the
doctrine or to a recorded ruling, and its subordination clause makes
any future drift a defect in this file rather than a competing
authority.

## Retroactive

Why this path (§11): the operator directed the act — "create
claude.md" (thread R13) — in the same turn as the m0014 close-out,
and the file's whole value is being in place before the next agent
session starts; §1's matter gate is honored by this filing rather
than preceded by it. Evidence: the filing commit, in which
`CLAUDE.md`, this matter, the thread export's R13 entry, and the
regenerated index land together. Explicit operator acknowledgment
(§11) moves this matter directly to `executed`; refusal rejects it
and removes the file.

## Execution

The filing commit, on branch `m0015-agent-instructions` (its pull
request against `main`; the commit carries `Matter: m0015`):
`CLAUDE.md` at the root, this matter, the execution thread brought
current through R13, and the index regenerated over ten matters. The
m0001 re-pin recording for the m0014 amendment rides the same branch
once the operator states that act, so one merge carries both. Date:
2026-08-27. Actor: claude-code/2026-08-26, on the operator's R13
direction.

## Vetting

### Acknowledgment — 2026-08-27

The operator acknowledged this matter per §11 — "I acknowledge m0015
at commit 60b7a46"
([execution thread R14](../threads/2026-08-26-m0012-execution.md)) —
moving it `proposed → executed`. Recorded per §6's retroactive
regime, the pin following the act: `ratified_commit`
`60b7a4655f4109f14590bd81bc1c7aae7924687e` (the filing commit),
`ratified_sha256`
`06782accfd9f856a272092081cc096b0a6167c58b879689d16544471f939b23e` —
the body after the frontmatter with `## Retroactive` and
`## Execution` included, as they stood at the acknowledged commit; no
`## Vetting` section existed there, and this entry sits after that
commit, outside the acknowledged text. Mechanical half:
[runs/2026-08-27-recording-m0001-and-m0015.md](../runs/2026-08-27-recording-m0001-and-m0015.md).
