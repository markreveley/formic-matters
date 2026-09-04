---
type: spec
title: The challenged state — ratified text is never demoted to proposed
description: "A disputed ratified matter moves to challenged — a state that reads as not-ratified for every gate while preserving that it was law and that dependents exist; the two back-to-proposed transitions are retired."
id: m0028
state: proposed
status: draft
tags: [formic-matters, process, lifecycle, integrity]
implements: m0001
sources:
  - doctrine/matters.md
threads:
  - threads/2026-08-29-complexity-escape-and-working-text.md
generated:
  by: claude-code/2026-08-29
  at: 2026-08-29T05:51:58Z
---

# m0028 · The challenged state — ratified text is never demoted to proposed

Filed on operator direction in the 2026-08-29 session, exported at
[threads/2026-08-29-complexity-escape-and-working-text.md](../threads/2026-08-29-complexity-escape-and-working-text.md)
and cited in `threads`.

## Diagnosed reason

The operator's insight of 2026-08-29, quoted: "what does
ratification mean? it means a matter is now clear to become a
logical dependency for doctrine, policy, documentation, code … a
proposed matter CANNOT be this. once a matter has crossed into being
ratified … it can't actually revert to 'proposed' again … as this
would break the obvious connection it has to all generated artifacts
that cite it as a dep."

The defect this names sits in ratified doctrine today. §3, "State —
mutable," contains two demotions to `proposed`: re-opening
(`ratified → proposed`) and execution failure (`staged → proposed`).
But `proposed` means: never was law, nothing may rest on it, nothing
does rest on it. A matter that was ratified and is later disputed
fits none of that — doctrine amendments may have landed on its
authority, other matters may rest on it, execution artifacts may
cite it. Sending it back to `proposed` erases the difference between
"never accepted" and "accepted, now disputed," and misrepresents the
standing of every dependent.

In dependency terms: ratification is publication. A ratified
matter is a published package version — its pin is the version
identifier, and dependents resolve against it. A published version
is never un-published; it can only be yanked: existing dependents
are warned, new ones are stopped. **challenged** is the yank.

## Proposed text

Amend doctrine §3, "State — mutable," with follow-through edits in
§6, "Vetting and ratification," and §12, "Storage and format."

**The new state.** `challenged` — was ratified (or staged); the
operator disputes its standing; dependents are on notice.

**Transitions, replacing the two demotions to `proposed`:**

- `ratified → challenged` — the operator disputes a ratified matter
  (a discovered divergence, a plan found broken before staging).
  The dispute and its reason, and the superseded pin's values, are
  recorded on the matter — the record from the gate onward is
  append-only under §6's existing rule ("Appended, never
  rewritten").
- `staged → challenged` — execution failure: the ratified plan
  proved wrong or impossible mid-execution. §3's existing failure
  record — what half-landed, its fate — carries over unchanged;
  only the destination state is new.
- `challenged → ratified` — re-ratification through the mechanism
  in force, over the corrected text; the new pin is recorded beside
  the preserved old one.
- `challenged → superseded` — the operator ratifies a replacement
  (§5, "Supersession, splitting, and conflict," unchanged).
- No other exits. `challenged` never returns to `proposed`, and
  `rejected` / `withdrawn` stay reserved for text that was never
  ratified.

**While a matter is challenged:**

1. Its body is working text again: revised directly, on operator
   direction, toward re-ratification. The frozen record is the
   challenge entry — the dispute, its reason, the superseded pin —
   never the body.
2. For every gate it reads as not-ratified: it cannot be staged or
   executed; a dependent cannot be staged or executed while a
   dependency is challenged (§7's gate — reviewers enforce it
   today, the validator once it exists,
   [m0008](m0008-matter-tooling.md)); and under the declared-sources
   rule [m0024](m0024-declared-sources.md) proposes, a challenged
   matter is not a valid source.
3. Its dependents are a derived list, never authored (§12, "Storage
   and format": views are derived): everything whose `depends_on`,
   `implements`, or declared sources name it, and every execution
   record citing it. Deriving the list is forwarded to
   [m0008](m0008-matter-tooling.md).

**Follow-through edits.** §6's re-opening sentence re-points from
`ratified → proposed` to `ratified → challenged`, keeping its
cleared-fields recording as is. §12's OKF status derivation gains
one mapping: `challenged → draft`.

## What this contradicts

No ratified matter. It amends §3's transition set — the two
demotions to `proposed` are retired in favor of the transitions
above — and adds one state row, one §12 status mapping, and the §6
re-pointing. Every recording requirement those transitions carry
today is preserved; only the destination state changes.

Coordination, not basis: two still-`proposed` matters name the
retired transitions —
[m0017](m0017-operator-authored-ratification.md) ("Precedence and
discovered divergence") and
[m0027](m0027-records-begin-at-the-gate.md) (its re-opening
sentence). The execution plan revises them.

## Proposed execution plan

1. Amend §3, §6, and §12 as above.
2. Revise the still-`proposed` matters that name the retired
   transitions — today m0017 and m0027 — to the new state (working
   text, revised directly).
3. Add a standing line to `CLAUDE.md`: disputed ratified text moves
   to `challenged`, never back to `proposed`.
4. If the glossary ([m0026](m0026-legibility-standard.md)) has
   executed by then, add the definition there too; otherwise §3
   carries it alone.
5. Regenerate `matters/index.md` and record a verification run
   under §9.1, "Runs."
6. Because doctrine changes, re-ratify m0001 over the amendment
   using the ratification mechanism then in force; record the pin
   only after the operator's act.
7. Append this matter's execution record, move it
   `staged → executed`, and put the branch before the operator for
   a merge-commit merge.
