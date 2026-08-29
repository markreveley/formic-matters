# Current handoff

> **Provisional while m0019 is proposed.** This document is advisory
> and may be stale. It does not ratify, stage, authorize, or extend any
> matter. Verify repository and external state before acting; matters
> supply scope and execution instructions.

## Observation

- `main` observed at: `2bfce1976aae6a78f5ffc134e33676299d6a46b5`,
  confirmed by fetch — the merge commit of pull request #14, the
  filing merge for `claude/restate-ratify-spec-eval-02nojc`
- Working branch: `claude/handoff-review-next-steps-fms9u3`, carrying
  only this refresh, based on the observed `main`
- Observed at: `2026-08-29T00:06:12Z`
- Closing actor: `claude-code/2026-08-29`

## Established state

- m0001, m0012, m0014, m0015 are `executed`; m0013 is `ratified`;
  m0006–m0008, m0010, m0011, m0016–m0023 are `proposed` — all on
  `main` at the observed commit, states read from frontmatter after
  the filing merge.
- The previous handoff's one action is consumed: pull request #14
  merged as a merge commit. The review session behind this refresh
  ran the prescribed post-merge verification — states above, merge
  shape (two parents), `Matter:` trailers on all twelve branch
  commits, presence of the thread export and its verification run —
  and found no discrepancy.
- [m0017](matters/m0017-operator-authored-ratification.md) carries no
  `## Vetting` entries; its first round is the next action below.
- [threads/2026-08-28-restate-to-ratify.md](threads/2026-08-28-restate-to-ratify.md)
  and
  [runs/2026-08-28-thread-export-verification.md](runs/2026-08-28-thread-export-verification.md)
  are merged, append-only primary sources.
- Deviation on record: this refresh lands from a harness-assigned
  branch name, not matter-prefixed. One file, commit trailer
  `Matter: m0017`; stated here and in its filing pull request.

## Pending operator acts

- Merge this refresh's filing pull request (merge commit), or
  authorize its merge. The pull request is opened after this
  observation — verify it exists, targets `main`, and contains only
  this file.
- Then the ratification and execution queue below, one act at a time.

## Recommended ratification and execution queue

This queue records current agent judgment. It is not a dependency
graph or grant of authority; the operator retains every act assigned
by doctrine, and each matter supplies its own contract. Detail that
could anchor a fresh reviewer — expected findings, open items left
for a round — is kept in this queue and never in the `Next action`
record, so a launch scoped to that record alone reads none of it.

1. Vet m0017 in a fresh context — the next action below. One open
   item was deliberately left for this round: the plan's hard-coded
   choice of m0016 as the first mandatory use of restate-to-ratify
   conflicts with this queue's ordering and with m0020's own plan;
   the round adjudicates it. After a clean disposition and any
   operator-directed revision: ratify and execute m0017 under the
   currently ratified verbal mechanism; its bootstrap ratification
   and associated m0001 re-ratification require no operator
   restatement.
2. Vet, ratify, and execute m0020 — the recommended first use of
   restate-to-ratify; an operator restatement is required on m0020.
   No doctrine amendment, so no m0001 re-ratification.
3. Vet, ratify, and execute m0019 after m0020 has corrected its
   proposed text. Restatement required on m0019; separate restatement
   on m0001 for the doctrine re-ratification.
4. Vet, ratify, and execute m0018, then m0016 (after m0020's
   correction and m0018's citation policy). Each requires its own
   restatement plus a separate m0001 restatement for its doctrine
   amendment.
5. After m0017 executes: m0021 (README lineage; no doctrine change)
   and m0022 (the rename — includes the container-directory decision
   m0014 landed and the consumer-side migration note). m0023 remains
   `proposed` long-term until a restatement corpus exists to analyze.

## Next action

- **Classification:** `operator authorization required`
- **Repository and matter:** `markreveley/formic-matters`, m0017
- **Action:** launch a fresh vetting round — the matter's first — on
  [m0017](matters/m0017-operator-authored-ratification.md). The
  reviewing agent reads the ratified record and the matter, and
  appends one `## Vetting` entry to the matter (round, reviewer,
  findings, disposition), per doctrine §6.
- **Permitted operations:** commit the appended entry, push the
  branch, and open its filing pull request; nothing else — no
  revision of the matter body, no state transition, no ratification
  act. Branch and PR title are m0017-prefixed where the launch
  environment allows; a harness-assigned branch name is a deviation
  stated in the round's own record.
- **Stop boundary:** after pushing the entry and opening the pull
  request, report the findings and stop. The merge, any revision,
  further rounds, and ratification are separate operator directions.
- **Verified against:** `main` at
  `2bfce1976aae6a78f5ffc134e33676299d6a46b5` (fetched) at
  `2026-08-29T00:06:12Z`. This file's own filing merge precedes the
  launch; if this handoff is read from `main`, that merge has
  completed.

The operator may adopt this one record in a fresh session with:

> Proceed from `handoff.md` in markreveley/formic-matters.

The operator may additionally scope the launched agent's reading to
this one record until its work is done; the record is written to be
sufficient by itself. This shorthand is the explicit bootstrap form
directed by the operator in m0020's decision thread; general
referential-launch policy remains proposed until m0020 is executed
through the matter system.

## Re-verification and uncertainties

- `origin/main` and this refresh's pull request are external state;
  re-check both against the observation above.
- Before the round: confirm m0017 is `proposed` and still carries no
  `## Vetting` entries.
- m0006, m0019, and m0020 are `proposed`: their review-structure,
  freshness, handoff, and launch rules are candidate policy, not
  policy. This file uses their drafted forms as rehearsal only;
  ratified doctrine alone governs, and this file remains advisory
  under the banner above.
- The vetting context reads
  [threads/2026-08-28-restate-to-ratify.md](threads/2026-08-28-restate-to-ratify.md)
  as historical evidence only; m0017's own text is the contract, and
  the thread confers no authority.
- The review session behind this refresh is not exported as a thread;
  its material effect is this file, and every claim here is checkable
  from the repository and the named external state alone.
