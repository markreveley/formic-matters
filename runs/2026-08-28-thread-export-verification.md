# Run — thread export verification: 2026-08-28-restate-to-ratify

**Claims tested.** The export at
[`threads/2026-08-28-restate-to-ratify.md`](../threads/2026-08-28-restate-to-ratify.md)
(1) has the declared turn structure — nine turns, five human and four
agent, strictly alternating, ending on the human turn that directed
the export, with no agent reply after it; (2) contains no reasoning
traces, tool calls, tool results, or injected environment context;
(3) reproduces the session's turns verbatim within its declared
boundary (each agent turn is that turn's closing message; working
narration between tool calls omitted); (4) is cited from the four
matters whose work the session drove —
[m0017](../matters/m0017-operator-authored-ratification.md),
[m0021](../matters/m0021-readme-naming-lineage.md),
[m0022](../matters/m0022-rename-to-rtr.md),
[m0023](../matters/m0023-restatement-integrity-analysis.md) — and the
citations resolve; (5) leaves the derived index byte-stable.

**Environment.** Linux 6.18.44-fc-v22 x86_64; Python 3.11.15;
`grep` (GNU), `wc`, `git` in a Claude Code remote container; repo at
branch `claude/restate-ratify-spec-eval-02nojc`, export committed at
`c11dd00`.

**Commands and results.**

```
T=threads/2026-08-28-restate-to-ratify.md
grep -c '^## ▸ ' $T
grep -n '^## ▸ ' $T
```

Expected 9 headings alternating human/agent starting and ending on a
human turn; observed exactly that (lines 40, 95, 194, 284, 316 human;
46, 130, 222, 292 agent; final heading human, nothing after its text).

```
grep -cE 'antml|function_call|function_result|tool_use|system-reminder|<thinking' $T
```

Expected 0; observed 0.

```
grep -c 'ZERO additive within the restatement' $T                     # 2
grep -c 'never ask a question that you do not already know the answer to' $T   # 2
grep -c 'its fractal productivity, and the bottleneck needs to be explicit - operator ratification' $T  # 2
grep -c 'export and persist the verbatim trascript here' $T           # 1
grep -c 'Zero additive content is the test' $T                        # 1
grep -c 'when responding, quote me for readability' $T                # 1
```

Distinctive strings from both speakers found exactly where expected.
The three counts of 2 are correct, not duplication: each is an
operator phrase appearing once in the operator's own turn and once
quoted back inside the agent's reply, per the operator's standing
"quote me for readability" instruction in the session. Operator typos
("trascript", "liabliity", "underspecificed", the stray trailing
apostrophe on the readability instruction) are preserved, as verbatim
requires.

```
grep -l '2026-08-28-restate-to-ratify' matters/*.md
python3 tools/gen-index.py && git diff --stat -- matters/index.md
wc -c $T
```

The four expected matters cite the thread and no others; the index
regenerates byte-identically (empty diff); the export is 55,089 bytes.

**Verbatim-fidelity attestation, and its limit.** The transcript's
source is the exporting agent's own session context: the platform
transcript is not a file in this repository, so no in-tree command can
independently diff the export against it. The participating agent
re-read the export against the session turn by turn before this run
and attests fidelity within the declared boundary. This is the same
trust shape as the adjudication session's export by its participating
agent; making session exports independently checkable is part of
[m0011](../matters/m0011-thread-persistence.md)'s open mechanism
question. Per-turn clock times were not captured; the export declares
this, and the export commit bounds it.

**Verdict.** All five claims pass; the fidelity claim passes as a
participating-agent attestation with the stated limit.

**Date and actor.** 2026-08-28, claude-code/2026-08-28.
