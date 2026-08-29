# Run — thread export verification: 2026-08-29-minimal-handoff-and-declared-sources

**Claims tested.** The export at
[`threads/2026-08-29-minimal-handoff-and-declared-sources.md`](../threads/2026-08-29-minimal-handoff-and-declared-sources.md)
(1) has the declared turn structure — nine turns, five human and four
agent, strictly alternating, ending on the human turn that directed
the export, with no agent reply after it; (2) contains no reasoning
traces, tool calls, tool results, or injected environment context;
(3) reproduces the session's turns verbatim within its declared
boundary (each agent turn is that turn's closing message; working
narration between tool calls omitted); (4) is cited from the five
matters whose work the session drove —
[m0016](../matters/m0016-launch-instructions-policy.md),
[m0017](../matters/m0017-operator-authored-ratification.md),
[m0019](../matters/m0019-fresh-context-durable-handoffs.md),
[m0020](../matters/m0020-referential-handoff-authority.md),
[m0024](../matters/m0024-declared-sources.md) — and the citations
resolve; (5) leaves the derived index byte-stable.

**Environment.** Linux 6.18.44-fc-v22 x86_64; Python 3.11.15;
`grep` (GNU), `wc`, `git` in a Claude Code remote container; repo at
branch `claude/handoff-review-next-steps-fms9u3`, export committed at
`1492130`.

**Commands and results.**

```
T=threads/2026-08-29-minimal-handoff-and-declared-sources.md
grep -c '^## ▸ ' $T
grep -n '^## ▸ ' $T
```

Expected 9 headings alternating human/agent starting and ending on a
human turn; observed exactly that (lines 46, 92, 116, 153, 179 human;
52, 102, 124, 163 agent; final heading human, nothing after its
text).

```
grep -cE 'antml|function_call|function_result|tool_use|system-reminder|<thinking' $T
```

Expected 0; observed 0.

```
grep -c 'considere as policy' $T                       # 1
grep -c 'do not read further til done' $T              # 1
grep -c 'somehow weirdly "biasing"' $T                 # 1
grep -c 'the cost of the act is the point' $T          # 1
grep -c 'Blind reviewer' $T                            # 1
grep -c 'quietly in tension with ratified text' $T     # 1
```

Distinctive strings from both speakers found exactly once each, where
expected — three from the operator's turns, three from agent turns.
The operator typo ("considere") is preserved, as verbatim requires.

```
grep -l '2026-08-29-minimal-handoff-and-declared-sources' matters/*.md
python3 tools/gen-index.py && git diff --stat -- matters/index.md
wc -c < $T
```

The five expected matters cite the thread and no others; the index
regenerates byte-identically (empty diff); the export is 20,283
bytes.

**Verbatim-fidelity attestation, and its limit.** The transcript's
source is the exporting agent's own session context: the platform
transcript is not a file in this repository, so no in-tree command can
independently diff the export against it. The participating agent
re-read the export against the session turn by turn before this run
and attests fidelity within the declared boundary. This is the same
trust shape as the prior session exports by their participating
agents; making session exports independently checkable is part of
[m0011](../matters/m0011-thread-persistence.md)'s open mechanism
question. Per-turn clock times were not captured; the export declares
this, and the export commit bounds it.

**Verdict.** All five claims pass; the fidelity claim passes as a
participating-agent attestation with the stated limit.

**Date and actor.** 2026-08-29, claude-code/2026-08-29.
