# Current handoff

> **Provisional while m0019 is proposed.** This document is advisory
> and may be stale. It does not ratify, stage, authorize, or extend any
> matter. Verify repository and external state before acting; matters
> supply scope and execution instructions.

## Observation

- `main` observed at: `527397e5031073e74f2c6e7567b5ca2acdcacf15`,
  confirmed by fetch — the branch's own merge base, so the filing PR
  applies cleanly
- Working branch: `claude/restate-ratify-spec-eval-02nojc`, content
  commits through `a789f904d0bd2877b61711e0dd8dbd8aadfd7b0f`; this
  file's own commits follow the observation
- Observed at: `2026-08-28T22:59:30Z`
- Closing actor: `claude-code/2026-08-28`

## Established state

- m0001, m0012, m0014, m0015 are `executed`; m0013 is `ratified`;
  m0006–m0008, m0010, m0011, m0016–m0020 are `proposed` on `main`.
- On the working branch, awaiting its filing pull request:
  - [m0017](matters/m0017-operator-authored-ratification.md) revised
    on operator direction: the mechanism is named **restate to
    ratify**; a restatement is defined as the operator's own-words
    account of what the matter does and why, bounded by the matter,
    zero additive content, diffed against the matter text; the
    precedence and discovered-divergence rule and the bounded-evidence
    statement are added; the artifact is "restatement" throughout, no
    longer "summary". State unchanged: `proposed`.
  - [m0021](matters/m0021-readme-naming-lineage.md) (README naming
    rationale and lineage), [m0022](matters/m0022-rename-to-rtr.md)
    (rename the framework to Restate to Ratify (RTR)), and
    [m0023](matters/m0023-restatement-integrity-analysis.md)
    (restatement integrity analysis, deliberately deferred) are filed
    `proposed`; all three `depends_on: [m0017]`.
  - The directing session is exported at
    [threads/2026-08-28-restate-to-ratify.md](threads/2026-08-28-restate-to-ratify.md),
    verified in
    [runs/2026-08-28-thread-export-verification.md](runs/2026-08-28-thread-export-verification.md).
- Deviation on record: the working branch name is harness-assigned,
  not matter-prefixed, and spans four matters. Every commit carries
  its own `Matter:` trailer and the filing PR title carries the m0017
  prefix; the deviation is stated in the session thread and this file.
- If this handoff is read from `main`, the filing merge has completed;
  verify m0016–m0023 all remain `proposed` — the merge is neither
  ratification nor staging.

## Pending operator acts

- Merge the filing pull request for the working branch (merge commit),
  or authorize its merge.
- The ratification and execution queue below, one act at a time.

## Recommended ratification and execution queue

This queue records current agent judgment. It is not a dependency
graph or grant of authority; the operator retains every act assigned
by doctrine, and each matter supplies its own contract.

1. Merge the filing PR for `claude/restate-ratify-spec-eval-02nojc`.
2. Vet m0017 in a fresh context. Before ratification, remove its
   hard-coded choice of m0016 as the first mandatory use (still open;
   deliberately left for the vetting round). Ratify and execute m0017
   under the currently ratified verbal mechanism; its bootstrap
   ratification and associated m0001 re-ratification require no
   operator restatement.
3. Vet, ratify, and execute m0020 — the recommended first use of
   restate-to-ratify; an operator restatement is required on m0020. No
   doctrine amendment, so no m0001 re-ratification.
4. Vet, ratify, and execute m0019 after m0020 has corrected its
   proposed text. Restatement required on m0019; separate restatement
   on m0001 for the doctrine re-ratification.
5. Vet, ratify, and execute m0018, then m0016 (after m0020's
   correction and m0018's citation policy). Each requires its own
   restatement plus a separate m0001 restatement for its doctrine
   amendment.
6. After m0017 executes: m0021 (README lineage; no doctrine change)
   and m0022 (the rename — includes the container-directory decision
   m0014 landed and the consumer-side migration note). m0023 remains
   `proposed` long-term until a restatement corpus exists to analyze.

## Next action

- **Classification:** `operator authorization required`
- **Repository and matter:** `markreveley/formic-matters`, m0017
- **Action:** merge the filing pull request for branch
  `claude/restate-ratify-spec-eval-02nojc` into `main` (merge commit,
  per doctrine §8)
- **Permitted operations:** trigger the merge of that one PR; nothing
  else
- **Stop boundary:** after the merge completes, stop and report; do
  not ratify, stage, vet, or launch anything
- **Verified against:** `main` at
  `527397e5031073e74f2c6e7567b5ca2acdcacf15` (fetched) and branch
  content through `a789f904d0bd2877b61711e0dd8dbd8aadfd7b0f` at
  `2026-08-28T22:59:30Z`; the PR is opened after this observation —
  verify it exists, targets `main`, and contains only this branch

The operator may adopt this one record in a fresh session with:

> Proceed from `handoff.md` in markreveley/formic-matters.

This shorthand is the explicit bootstrap form directed by the operator
in m0020's decision thread. General referential-launch policy remains
proposed until m0020 is executed through the matter system.

## Re-verification and uncertainties

- The PR and `origin/main` are external state; re-check both against
  the observation above.
- Confirm m0016–m0023 remain `proposed` after any merge.
- The thread export and run record are append-only primary sources
  once merged; a superseding export is a new file, never an edit.
- A fresh m0017 vetting context reads the session thread as historical
  evidence only; m0017's own text is the contract, and the thread
  confers no authority.
- No instruction from the exported session is required to continue:
  the matters carry the contracts, and this file is only the current
  projection.
