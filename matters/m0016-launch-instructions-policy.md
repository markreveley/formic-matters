---
type: spec
title: Launch instructions are pointers, not shadow specifications
description: "A launch identifies the repository, matter, operator act, and external authority; all substantive scope and execution instructions live in the repository's ratified record."
id: m0016
state: proposed
status: draft
tags: [formic-matters, process, execution, provenance]
implements: m0001
depends_on: [m0020, m0018]
threads:
  - threads/2026-08-26-m0012-execution.md
generated:
  by: codex/2026-08-26
  at: 2026-08-26T23:55:08-07:00
---

# m0016 · Launch instructions are pointers, not shadow specifications

## Diagnosed reason

The doctrine makes the ratified matter the execution contract (§3,
§6) and the repository the record (§8), but does not say directly
what belongs in the instruction that launches an agent. The first
consumer follow-through exposed the omission: the framework execution
thread records two checked launch prompts being delivered outside the
file, while their operative text is absent from the repository
([thread R13](../threads/2026-08-26-m0012-execution.md)). One of those
agent-authored handoffs repeated doctrine, supplied an unfiled
containment plan, made execution-sequencing choices, and carried
repository facts that then needed a second out-of-record prompt review.
The prompt had become a parallel specification whose corrections could
not accrete on the matter it purported to govern.

An operator act still has to reach an agent. The defect is not that a
launch instruction exists; it is that the instruction can silently
become the only place substantive scope or execution policy exists.
That defeats exact-text ratification and makes the repository cease to
be the operative channel at the moment execution begins.

## Proposed text

Add a `### Launch instructions` subsection to doctrine §8 containing
this policy verbatim:

> Launch instructions are pointers, not shadow specifications. They identify the repository, matter, operator act, and necessary external authority. Scope and execution instructions come from the repository’s ratified record. Any substantive instruction absent from that record is filed or amended and ratified before execution.
>
> Authority resides in ratified text and in the operator’s acts, live or recorded, and nowhere else. A `proposed` matter is a candidate: it may be pointed to — a dependency, a supersession target, a coordination reference — but it is never citable as the basis for a rule, an assumption, or an act. Text that treats a proposed matter as operative is a shadow specification, wherever it lives.

Add the same two paragraphs verbatim to `CLAUDE.md` as standing
rules. The
doctrine is the authority; `CLAUDE.md` makes the rule present at the
agent's first read and continues to distill, never override, per
[m0015](m0015-agent-instructions.md).

## Enforcement

- Before acting, an agent resolves the named repository and matter,
  reads the repository's governing instructions and normative
  specification, verifies the matter's state and ratification record,
  and maps the requested operator act to a transition or lifecycle
  action the doctrine permits.
- A filing or vetting launch may introduce information into a
  `proposed` matter. That information becomes operative only after it
  is written into the matter and ratified. It is never execution scope
  merely because it appeared in the launch instruction.
- An agent that finds an act, assumption, or rule resting on a
  `proposed` matter stops and reports: the content enters force only
  through ratification. Coordination references — `depends_on`,
  supersession links, pointers — remain ordinary and carry no
  authority.
- A launch against a ratified or staged matter cannot extend or replace
  its ratified region. Material additional direction takes the normal
  re-open or execution-failure path before work continues (§3, §3.1).
- Necessary external authority may be stated in the launch — for
  example permission to push a named matter branch or open a pull
  request. Authority changes what operations the agent may perform; it
  does not change the ratified deliverable.
- The launch turn is preserved when the session is exported under
  §9.2, so the operator act and any attempted shadow instruction remain
  auditable. The matter, not the thread, remains the source of execution
  scope.
- This rule is judgment-enforced by the agent and operator. A validator
  cannot inspect an unpersisted prompt, and §10 forbids pretending that
  it can. Future orchestration or launch tooling may make the repository,
  matter, state, and pin checks deterministic; that is not introduced
  here.

## What this contradicts

Nothing in ratified text. It makes explicit the consequence of the
existing matter gate (§1), exact-text contract (§3, §6), repository
channel (§8), and deviation rule (§3.1). It narrows no operator
authority: the operator may always direct a new substantive change,
but the change enters the record and is ratified before execution.
The authority paragraph generalizes what the doctrine already states
about itself — un-ratified text is a candidate — from that document
to every matter in the collection.

The rule is distinct from
[m0011](m0011-thread-persistence.md): m0011 governs which session
exchanges persist and by what mechanism; this matter governs where
execution authority and scope reside even when every launch turn is
perfectly preserved. It also does not select the next matter or launch
agents autonomously; §3 continues to reserve staging and launch to the
operator.

## Proposed execution plan

1. Insert the proposed subsection in doctrine §8 without changing the
   paragraphs' text.
2. Insert the same paragraphs verbatim in `CLAUDE.md` under its standing
   rules, subordinate to doctrine as that file already declares.
3. Regenerate `matters/index.md` and record a §9.1 run verifying each
   exact paragraph occurs once in doctrine and once in `CLAUDE.md`, the
   index regenerates byte-identically, and repository links resolve.
4. Because doctrine changes, present the amendment commit for the
   operator's m0001 re-ratification. Record the new whole-file pin only
   after that act, on the same execution branch.
5. Export the session exchange under §9.2, including the launch turn
   verbatim and excluding reasoning and tool traffic.
6. Append this matter's execution record, move it `staged → executed`,
   remove its `branch`, regenerate the index, and put the completed
   branch before the operator for a merge-commit merge.
