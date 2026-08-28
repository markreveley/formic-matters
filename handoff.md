# Current handoff

> **Provisional while m0019 is proposed.** This document is advisory
> and may be stale. It does not ratify, stage, authorize, or extend any
> matter. Verify repository and external state before acting; matters
> supply scope and execution instructions.

## Observation

- Repository base observed: `916749153154d3f59a63cecbe00079a40d691e2a`
- Observed at: `2026-08-28T08:25:37-07:00`
- Closing actor: `codex/2026-08-28`
- Working branch: `m0020-referential-handoff-authority`

## Established state

- `main` and `origin/main` were both at the observed base when checked.
- [m0016](matters/m0016-launch-instructions-policy.md),
  [m0017](matters/m0017-operator-authored-ratification.md),
  [m0018](matters/m0018-doctrine-heading-citations.md), and
  [m0019](matters/m0019-fresh-context-durable-handoffs.md) are proposed
  on `main`. None is ratified or staged.
- [m0020](matters/m0020-referential-handoff-authority.md) and its
  [decision thread](threads/2026-08-28-handoff-launch-authority.md) are
  being filed on the working branch. If this handoff is read from
  `main`, verify that the m0020 filing merge completed and that m0020
  remains proposed.

## Open process findings

[m0020](matters/m0020-referential-handoff-authority.md) owns two
corrections that must not depend on the session that discovered them:

1. m0016 must define an operator's adoption of one explicit handoff
   action by reference and distinguish operator-only lifecycle acts
   from agent-performed push, PR-open, and merge mechanics.
2. m0019 must classify a current action as `operator act required`,
   `operator authorization required`, or
   `agent operation already authorized`, with its matter, action,
   permitted operations, stop boundary, and verified state.

These are proposed fixes, not current policy. Their exact contract and
later execution order live on m0020.

## Recommended ratification and execution queue

This queue records current agent judgment. It is not a dependency graph
or grant of authority; the operator retains every act assigned by
doctrine, and each matter supplies its own contract.

1. Vet m0017 in a fresh context. Before ratification, remove its
   hard-coded choice of m0016 as the first mandatory use. Ratify and
   execute m0017 under the currently ratified mechanism; its bootstrap
   ratification and associated m0001 re-ratification require no
   operator-authored summaries.
2. Vet, ratify, and execute m0020. It depends on m0017 and is the
   recommended first use of operator-authored ratification. An operator
   summary is required on m0020. It does not amend doctrine, so it
   requires no m0001 re-ratification.
3. Vet, ratify, and execute m0019 after m0020 has corrected its
   proposed text. An operator summary is required on m0019, and a
   separate summary is required on m0001 for the doctrine
   re-ratification.
4. Vet, ratify, and execute m0018 under the m0017 and m0019 policies.
   An operator summary is required on m0018, and a separate summary is
   required on m0001 for the doctrine re-ratification.
5. Vet, ratify, and execute m0016 after m0020's correction and after
   revising its still-proposed text to follow m0018's
   heading-qualified citation policy. An operator summary is required
   on m0016, and a separate summary is required on m0001 for the
   doctrine re-ratification.

## Next action

- **Classification:** `operator authorization required`
- **Repository and matter:** `markreveley/formic-matters`, m0017
- **Action:** conduct one fresh vetting round for ratification readiness
- **Permitted operations:** create and push an m0017-prefixed branch,
  append the vetting record, and open a matter-prefixed PR
- **Stop boundary:** do not merge, ratify, stage, or execute; return the
  findings and PR to the operator
- **Verified against:** repository base
  `916749153154d3f59a63cecbe00079a40d691e2a` at
  `2026-08-28T08:25:37-07:00`; the next context must additionally verify
  the m0020 filing on then-current `main`

The complete action is encoded above. The operator may adopt it in the
next fresh session with only:

> Proceed from `handoff.md` in markreveley/formic-matters.

This one shorthand is an explicit bootstrap form directed by the
operator in m0020's decision thread. General referential-launch policy
remains proposed until m0020 is executed through the matter system.

## Re-verification and uncertainties

- Re-check the m0020 PR and `origin/main`; both are external state and
  may have changed after the observation time.
- Confirm m0016–m0020 remain `proposed` and that the filing merge was
  not mistaken for ratification or staging.
- Verify the next-action record before treating the operator's
  shorthand as authorization. A stale or ambiguous record is a stop and
  report.
- No instruction from the exported decision session is required to
  continue. The thread is historical evidence, m0020 is the proposed
  change contract, and this file is only the current projection.
