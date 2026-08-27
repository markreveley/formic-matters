# Current handoff

> **Provisional while m0019 is proposed.** This document is advisory
> and may be stale. It does not ratify, stage, authorize, or extend any
> matter. Verify repository and external state before acting; matters
> supply scope and execution instructions.

## Observation

- Repository base observed: `c05959193e4b9ecc50765e746f404b05d003a358`
- Observed at: `2026-08-27T16:54:24-07:00`
- Closing actor: `codex/2026-08-27`
- Working branch: `m0019-fresh-context-handoffs`

## Established state

- `main` and `origin/main` were both at the observed base when checked.
- [m0016](matters/m0016-launch-instructions-policy.md) is proposed on
  `main`; PR #9 merged it at
  `c9d9bb6c48a7200c8c0ac0dffd3b472b5c27a7a7`.
- [m0017](matters/m0017-operator-authored-ratification.md) is proposed
  on `main`; PR #10 merged it at
  `0662e19abd96dc74357543a1845e2513b777f412`.
- [m0018](matters/m0018-doctrine-heading-citations.md) is proposed on
  `main`; PR #11 merged it at
  `c05959193e4b9ecc50765e746f404b05d003a358`.
- [m0019](matters/m0019-fresh-context-durable-handoffs.md) and this
  provisional handoff have a local filing commit,
  `466701d8f6c4880efd46c76697a51d21da753c55`, stacked after the m0018
  filing commit. Its remote branch is published; no PR has been opened.
- All four matters remain `proposed`. None is ratified or staged.

## Pending filing action

At the observation point, only the m0019 filing remains. The operator
authorized the agent to proceed with the complete filing phase. That
authorization permits the agent to open, verify, and merge the m0019
filing PR by merge commit; it does not ratify or stage any matter.

The m0019 comparison against the observed base contains only
`handoff.md`, the m0019 matter, and its derived index entries. If this
handoff is being read from `main`, the filing merge carrying it has
necessarily completed; re-verify that fact rather than repeating it.

No operator-authored ratification summary is required for the filing
merge. Filing leaves m0019 proposed.

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

## Next launch after the filing lands

After verifying m0019 is proposed on `main`, the recommended next act is
an independent vetting round on m0017. The minimal launch pointer is:

> Vet m0017 for ratification readiness in markreveley/formic-matters. You may push an m0017-prefixed branch and open a PR; do not merge.

## Re-verification and uncertainties

- Re-check the m0019 PR state and `origin/main`; both are external state
  and may have changed after the observation time.
- Confirm all four matters remain `proposed` and that no filing merge
  was mistaken for ratification or staging.
- The proposed m0019 policy is not yet normative. The provisional
  handoff is being used as an explicit bootstrap aid, not as authority.
- No instruction from the session that produced this file is required
  to continue the queue.
