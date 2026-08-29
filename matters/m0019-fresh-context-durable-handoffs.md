---
type: spec
title: Fresh contexts and durable handoffs
description: "Vetting and execution begin across explicit context boundaries, while a mutable, non-authoritative handoff keeps the repository's current operational projection available to each new context."
id: m0019
state: proposed
status: draft
tags: [formic-matters, process, review, execution, provenance]
implements: m0001
depends_on: [m0017, m0020]
threads:
  - threads/2026-08-29-minimal-handoff-and-declared-sources.md
generated:
  by: codex/2026-08-27
  at: 2026-08-27T16:40:33-07:00
---

# m0019 · Fresh contexts and durable handoffs

## Diagnosed reason

Doctrine §6, “Vetting and ratification,” requires fresh agents for
review but does not define freshness in terms of the context an agent
receives. It does not say whether the context that authored or revised
a matter may count as its reviewer, whether an author response is a new
vetting round, or whether execution should inherit the conversation
that produced the proposal. Doctrine §3, “State — mutable,” likewise
reserves execution to an operator-launched dev agent without specifying
an execution context boundary.

That ambiguity defeats the intended independence. A nominally new
agent can inherit the full authoring conversation and its anchors; an
execution agent can receive an out-of-repository recap that becomes a
second specification. At the other extreme, starting without inherited
conversation can discard useful operational state unless the repository
contains a concise account of what has happened and which operator act
is presently needed.

The ratified record and a current handoff serve different purposes. A
matter defines authority and scope. Vetting, execution, runs, and
threads preserve evidence. A handoff is the closing agent's fallible,
mutable projection of current state and likely next actions. Treating
that projection as advisory allows new contexts to start from the
repository without turning a session recap into shadow doctrine.

## Proposed text

### Context boundaries

Amend doctrine §6, “Vetting and ratification,” and doctrine §3,
“State — mutable,” with these rules:

- Each vetting round begins in a newly launched context that does not
  inherit the conversation in which the matter was authored or revised.
  The model, agent implementation, or actor label may recur; the
  conversation context does not.
- A fresh vetting context receives its substantive information from the
  repository. Its launch identifies the repository, matter, operator
  act, and necessary external authority. It does not receive an
  unrecorded summary of the matter or desired findings.
- An author may answer findings and revise a proposed matter in the
  author's existing context. That response is not an independent
  vetting round. Any later review round begins in another fresh context.
- Execution of each staged matter begins in a fresh context dedicated
  to that matter. It does not inherit the matter's authoring,
  ratification, or unrelated execution conversation. A replacement
  context that resumes interrupted execution is also fresh and
  matter-dedicated.
- A matter-dedicated execution may pause for an operator act or for a
  separate fresh review required by another lifecycle gate. Those
  contexts do not become additional executions of the staged matter.
- A context may read the collection handoff, but it verifies every
  material statement against the repository and any named external
  state before acting. The handoff never makes a context non-fresh
  because it is repository-visible, explicitly advisory text.

Freshness is a normative channel boundary, not a claim that current
tooling can prove conversation ancestry. Vetting and execution records
identify that a fresh context was used; agents and the operator enforce
the truth of that claim. Deterministic orchestration support may later
strengthen the evidence without pretending to prove what the platform
does not expose, as required by doctrine §10, “Deterministic wherever
possible.”

### Durable handoff

Amend doctrine §8, “Where discourse lives,” and doctrine §12,
“Storage and format,” to define one mutable `handoff.md` at the
collection root. In the framework home that is `handoff.md`; in a
contained consumer collection it is `.formic-matters/handoff.md`.

The handoff is updated at a durable transfer of control: the close of a
filing session, vetting round, author response, ratification-recording
session, execution pause, or execution completion when repository state
or the next permissible action has materially changed. It need not
change after an explanatory turn that changes neither.

Every handoff contains:

- a prominent statement that it is advisory, may be stale, and cannot
  ratify, stage, authorize, or extend a matter;
- the full commit against which repository state was observed, the
  observation time, and the closing actor;
- pointers to the derived index for state and to the matters touched
  since the previous handoff;
- pending operator acts;
- the next declared action, when one exists — exactly one record; and
- external state the next context must re-verify.

The handoff carries pointers and declared actions, nothing more. It
contains no matter-specific commentary: an agent's observation about a
matter — an open item, a correction, a recommendation, an expected
finding — is recorded on the matter itself, where it accretes review
history before every reader equally, and never in the handoff.
Ordering is derived from `depends_on` and the operator's staging,
never authored here; there is no recommended queue.

The handoff points to matters for scope and execution instructions; it
does not reproduce them. A substantive gap discovered while writing the
handoff is filed or amended in a matter and presented for ratification,
not supplied as an imperative in the handoff. No state transition or
operator authority is inferred from a checked box, recommendation, or
stale platform observation.

`handoff.md` is intentionally rewritten to show the current projection.
Git commits preserve its history; it is not an append-only primary
source. It neither replaces nor summarizes in place `## Vetting`,
`## Execution`, runs, or threads. A closing session is not required
reading merely because it produced the handoff. If that session is
otherwise exported as a thread, the thread remains historical evidence
and not operational authority.

Each handoff update travels with the matter whose work caused the
handoff and uses that matter's commit trailer. Concurrent branches may
carry different projections. The next context trusts none of them
without checking the target branch and current base; the projection
that lands later does not retroactively govern earlier work.

## Enforcement

Until orchestration support exists, agents and the operator enforce
context separation. A vetting entry or execution record that asserts a
fresh context is a reviewable process claim, not machine proof.

The deterministic portion is forwarded to
[m0008](m0008-matter-tooling.md): verify the handoff's required fields,
full-SHA syntax, advisory notice, matter links, and collection-relative
location. A validator may detect that the observed commit is not an
ancestor of the checked tree and report likely staleness. It must not
treat handoff recommendations as dependency edges, lifecycle
transitions, or execution authority.

## What this contradicts

This specifies the operational meaning of “fresh agents” in doctrine
§6, “Vetting and ratification.” It preserves independent rounds while
making context ancestry, rather than an unstable model or product
identity, the relevant boundary.

It adds a deliberately mutable repository document alongside doctrine
§8, “Where discourse lives,” without weakening the append-only rules
for vetting, execution, runs, and threads. The handoff is a cache of
current operational judgment, not a new evidence class or normative
source.

It is complementary to
[m0016](m0016-launch-instructions-policy.md): m0016 limits launches to
pointers and external authority; this matter gives the fresh context a
repository-resident operational projection without letting that
projection become a shadow specification. Neither matter autonomously
selects, stages, ratifies, or launches the next matter.

It is also distinct from
[m0011](m0011-thread-persistence.md): a thread preserves qualifying
session turns verbatim under an append-only policy; the handoff is a
small, revisable closing assessment whose previous versions live in Git
history.

## Proposed execution plan

1. Amend doctrine §6, “Vetting and ratification,” and doctrine §3,
   “State — mutable,” with the context-boundary rules above.
2. Amend doctrine §8, “Where discourse lives,” and doctrine §12,
   “Storage and format,” with the handoff's role, authority boundary,
   location, required contents, update boundary, and mutability rules.
3. Add distilled context and handoff rules to `CLAUDE.md`, subordinate
   to doctrine.
4. Replace the provisional notice in `handoff.md` with the active
   advisory notice and initialize it from repository and external state
   verified during execution. Do not copy matter scope or execution
   instructions into it.
5. Forward the deterministic checks to
   [m0008](m0008-matter-tooling.md), regenerate `matters/index.md`, and
   record a verification run under doctrine §9.1, “Runs.”
6. Re-ratify m0001 over the doctrine amendment using the ratification
   mechanism then in force; record the whole-doctrine pin only after
   the operator's act.
7. Append this matter's execution record, move it `staged → executed`,
   remove its `branch`, refresh the handoff, regenerate the index, and
   put the completed branch before the operator for a merge-commit
   merge.
