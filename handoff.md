# Current handoff

> **Provisional while m0019 is proposed.** This document is advisory
> and may be stale. It does not ratify, stage, authorize, or extend any
> matter. Verify repository and external state before acting; matters
> supply scope and execution instructions.

## Observation

- Repository base observed: `cee4c12af8ed019226717be08b9beed9c85e8ddc`
- Observed at: `2026-08-27T16:40:33-07:00`
- Closing actor: `codex/2026-08-27`
- Working branch: `m0019-fresh-context-handoffs`

## Established state

- `main` and `origin/main` were both at the observed base when checked.
- [m0016](matters/m0016-launch-instructions-policy.md) is proposed in
  GitHub PR #9. The PR was open and reported clean when checked.
- [m0017](matters/m0017-operator-authored-ratification.md) has a local
  filing commit, `db6b87d6e33b0c9c5af1f891c6dbf3b91d41c75d`, stacked after
  the m0016 filing commit. It has not been pushed or opened as a PR.
- [m0018](matters/m0018-doctrine-heading-citations.md) has a local
  filing commit, `933980af0182820fa9fa8db2156f5165b96d67a4`, stacked after
  the m0017 filing commit. It has not been pushed or opened as a PR.
- [m0019](matters/m0019-fresh-context-durable-handoffs.md) and this
  provisional handoff are being filed on the current stacked branch.
- All four matters remain `proposed`. None is ratified or staged.

## Pending operator acts and filing queue

This is the closing agent's recommended order, not a dependency graph
or grant of authority.

1. Operator: merge PR #9 by merge commit if the m0016 filing is
   accepted.
2. Agent, after verifying `main`: push the m0017 branch and open its
   matter-prefixed filing PR. Operator then decides whether to merge it.
3. Agent, after verifying the m0017 filing on `main`: push the m0018
   branch and open its matter-prefixed filing PR. Operator then decides
   whether to merge it.
4. Agent, after verifying the m0018 filing on `main`: push the m0019
   branch and open its matter-prefixed filing PR. Operator then decides
   whether to merge it.

No operator-authored ratification summary is required for these filing
merges. Filing leaves each matter proposed.

## Recommended ratification and execution queue

This queue records current agent judgment. The operator retains staging
and ratification authority, and each matter supplies its own contract.

1. Vet m0017 in a fresh context. Before ratification, review its
   hard-coded claim that m0016 is the first mandatory use and remove the
   scheduling choice from the ratified plan. Ratify and execute m0017
   under the currently ratified mechanism; its bootstrap ratification
   and associated m0001 re-ratification do not require operator-authored
   summaries.
2. Vet, ratify, and execute m0019. It depends on m0017 and is the
   recommended first use of operator-authored ratification. An operator
   summary is required on m0019, and a separate summary is required on
   m0001 for the doctrine re-ratification.
3. Vet, ratify, and execute m0018 under the m0017 and m0019 policies.
   An operator summary is required on m0018, and a separate summary is
   required on m0001 for the doctrine re-ratification.
4. Vet, ratify, and execute m0016 after revising its still-proposed text
   to follow m0018's heading-qualified citation policy. An operator
   summary is required on m0016, and a separate summary is required on
   m0001 for the doctrine re-ratification.

## Next permissible action

The next action is operator-only: decide whether to merge PR #9. No
agent launch is needed until that decision changes repository state.

After a merge, a minimal filing launch is sufficient:

> Continue the filing queue in `handoff.md` in markreveley/formic-matters. You may push the next matter-prefixed branch and open its filing PR; do not merge.

## Re-verification and uncertainties

- Re-check PR #9 and `origin/main`; both are external state and may have
  changed after the observation time.
- Each later filing PR must be reviewed against then-current `main` so
  it contains only its own matter's filing changes.
- The proposed m0019 policy is not yet normative. The provisional
  handoff is being used as an explicit bootstrap aid, not as authority.
- No instruction from the session that produced this file is required
  to continue the queue.
