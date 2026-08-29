# Current handoff

> **Provisional while m0019 is proposed.** This document is advisory
> and may be stale. It does not ratify, stage, authorize, or extend any
> matter. Verify repository and external state before acting; matters
> supply scope and execution instructions.

## Observation

- `main` observed at: `2bfce1976aae6a78f5ffc134e33676299d6a46b5`,
  confirmed by fetch
- Working branch: `claude/handoff-review-next-steps-fms9u3` — revises
  [m0016](matters/m0016-launch-instructions-policy.md),
  [m0017](matters/m0017-operator-authored-ratification.md),
  [m0019](matters/m0019-fresh-context-durable-handoffs.md), and
  [m0020](matters/m0020-referential-handoff-authority.md), files
  [m0024](matters/m0024-declared-sources.md), and rewrites this file;
  per-commit `Matter:` trailers; the harness-assigned branch name is
  the recorded deviation
- Observed at: `2026-08-29T00:24:26Z`
- Closing actor: `claude-code/2026-08-29`

## State

- State lives in [matters/index.md](matters/index.md) at the observed
  commit and in each matter's frontmatter; this file restates none of
  it. What an agent had to say about a matter is on the matter.
- Pull request #14, the restate-to-ratify filing, is merged. Pull
  request #15 is this branch's filing pull request, open at this
  observation.

## Pending operator acts

- Merge pull request #15 (merge commit), or authorize its merge.
- Then the next action below.

## Next action

- **Classification:** `operator authorization required`
- **Repository and matter:** `markreveley/formic-matters`, m0017
- **Action:** launch a fresh vetting round — the matter's first — on
  [m0017](matters/m0017-operator-authored-ratification.md): read the
  ratified record and the matter, and append one `## Vetting` entry
  to the matter (round, reviewer, findings, disposition), per
  doctrine §6.
- **Permitted operations:** commit the appended entry, push the
  branch, and open its filing pull request; nothing else — no
  revision of the matter body, no state transition, no ratification
  act. Branch and PR title are m0017-prefixed where the launch
  environment allows; a harness-assigned branch name is a deviation
  stated in the round's record.
- **Stop boundary:** after pushing the entry and opening the pull
  request, report the findings and stop. The merge, any revision,
  further rounds, and ratification are separate operator directions.
- **Verified against:** `main` at
  `2bfce1976aae6a78f5ffc134e33676299d6a46b5` (fetched) at
  `2026-08-29T00:24:26Z`. This file's own filing merge precedes the
  launch; if this handoff is read from `main`, that merge has
  completed.

The operator may adopt this one record in a fresh session with:

> Proceed from `handoff.md` in markreveley/formic-matters.

This shorthand is the explicit bootstrap form directed by the operator
in m0020's decision thread; general referential-launch policy remains
proposed until m0020 is executed through the matter system.

## Re-verification

- `origin/main` and pull request #15 are external state; re-check
  both against the observation above.
- Before the round: confirm m0017 is `proposed` and carries no
  `## Vetting` entries.
- Nothing `proposed` governs; this file remains advisory under the
  banner above.
