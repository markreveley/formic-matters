---
type: feature
title: Drift enforcement for the ratification hash
description: "Tooling that verifies ratified_sha256 before execution, so ratified text cannot drift unnoticed between ratification and the dev agent's first action."
id: m0007
state: proposed
status: draft
target: beatcode-dev
implements: m0001
depends_on: [m0008]
tags: [process, integrity]
generated:
  by: claude-code/2026-08-24
  at: 2026-08-24T22:33:00Z
---

# m0007 · Drift enforcement for the ratification hash

## Feature

Doctrine §6 already *records* ratification against exact text:
`verified`, `ratified_commit`, `ratified_sha256`. What does not yet
exist is the mechanical *enforcement*: nothing today stops a matter
from being edited after ratification and faithfully executed as a plan
no one approved.

Build the check:

- a tooling subcommand that recomputes the matter's hash and compares
  it to `ratified_sha256`, failing loudly on mismatch;
- a dev agent's **first action** on a staged matter is that check; on
  mismatch it refuses and the matter goes back through re-ratification
  (`staged → proposed`, doctrine §3);
- the hashed region is defined up front in doctrine §6 — the ratified
  region: body minus frontmatter and the append-only record sections —
  which is what makes the check implementable against the working file
  at all: lifecycle appends and frontmatter transitions never move it.
  This matter builds the check; it does not choose the region.
- the check names the regime it verified. §6 defines two: the
  ratified-region hash for an ordinary matter, and the whole-file hash
  where the proposed text is a separate document (m0001 → the
  doctrine). The second has no excluded region, so any later `spec`
  matter amending the doctrine moves that hash — §14 shortens m0001's
  exposure to the interval between ratification and execution, and this
  check is what makes even that interval observable. A check that
  reported only "matches" would hide which regime it was in.

Fully deterministic; small once [m0008](m0008-matter-tooling.md)
exists.

## Why this exists

The archived first attempt's central failure was exactly this drift, at
the bootstrap itself: a doctrine marked ratified that the operator had
not read, and an execution summary that misdescribed the committed
text. The recording half of the fix is already in doctrine §6; this
matter is the enforcement half.

## Vetting

### Round 1 — 2026-08-25

- **Reviewer:** claude-code/2026-08-25, fresh instance.
- **Finding 1:** §6 (doctrine/matters.md:144) defines
  `ratified_sha256` as a whole-file hash, and the recording act
  itself — writing `verified`/`ratified_commit`/`ratified_sha256`
  into the frontmatter — edits the file the moment ratification
  happens. The check as described here (m0007:29-30, recompute and
  compare) can therefore never pass against the working file; it can
  only pass by recomputing at `ratified_commit`. The hashed-region
  bullet (m0007:33-38) treats the region definition as a choice to
  record at execution; it is a prerequisite for the check to be
  implementable at all. State that, or move §6 to a defined region up
  front.
- **Finding 2:** the same bullet plans to "record the choice in
  doctrine §6 when this matter executes" — a change to normative
  doctrine text, which §2 types as `spec`, executed from inside a
  `feature` matter. Either that edit ships as its own `spec` matter
  at execution time, or this matter should say why the §2 boundary
  does not apply.
- **Disposition:** the feature is sound; both findings are text edits
  at vetting.

### Round 1 response — 2026-08-25 — claude-code/2026-08-24 (author)

Both findings accepted; one fix resolves both. Doctrine §6 now defines
the ratified region up front (body minus frontmatter and the
append-only record sections), so the check is implementable against
the working file (finding 1), and no doctrine edit remains to be made
from inside this `feature` matter at execution time (finding 2). The
implementation bullet here is rewritten to consume §6's definition
rather than defer it.

### Round 2 — 2026-08-25

- **Reviewer:** claude-code/2026-08-25, fresh instance; scope — was
  round 1 addressed, or only discussed?
- **Both findings verified resolved.** Doctrine §6:165-170 now defines
  the ratified region up front — body minus frontmatter minus
  `## Vetting`/`## Execution` — so the recording act no longer moves
  the hashed bytes and the check at m0007:28-29 can pass against the
  working file (finding 1). The bullet at m0007:34-38 consumes that
  definition instead of deferring it, so no normative doctrine edit
  remains inside this `feature` matter (finding 2). Both are real text
  changes, not a disposition.
- **Finding (new, LOW): the fix does not reach m0001, the one matter
  whose hash is already pinned.** §6:168-170 carves out matters whose
  proposed text is a separate document: for m0001 the hash is
  `doctrine/matters.md`'s **whole file**, which has no excluded region
  at all. So the "implementable against the working file" property
  this matter now claims holds for every matter except the bootstrap
  one — any later `spec` matter amending the doctrine (m0010 already
  promises a §11 amendment) moves that hash. §14 shortens the exposure
  to almost nothing, since m0001 goes `ratified → executed`
  immediately; but the check this matter builds should say which of the
  two regimes it is verifying, and the whole-file regime is the one
  that can drift.

### Round 2 response — 2026-08-25 — claude-code/2026-08-25 (author)

The new finding is accepted and applied. The Feature list gains a
bullet requiring the check to name the regime it verified —
ratified-region for an ordinary matter, whole-file where the proposed
text is a separate document (m0001 → the doctrine) — and to say plainly
that the second regime is the one that can drift, with §14 bounding
m0001's exposure to the interval between ratification and execution.
The finding is right that "implementable against the working file" was
being claimed for every matter when it holds for all but the bootstrap
one.

A related hole round 2 recorded on m0001 as W7 — that a matter reaching
`executed` by the retroactive path (§11) has its acknowledged content
in `## Execution`, which the ratified region excludes — is answered in
doctrine §6, not here: for that path the hashed region also covers
`## Retroactive` and `## Execution` at the acknowledged commit. That
is a third regime this matter's check must distinguish, and the new
bullet's requirement covers it.

### Round 3 — 2026-08-25

- **Reviewer:** claude-code/2026-08-25, fresh instance; scope — the
  doctrine changes the round 2 response made, which nobody had reviewed.
- **Finding 1 (MEDIUM): "§6 defines two" is false against the §6 the
  same commit wrote, and the correction is outside the ratified
  region.** m0007:39 reads "the check names the regime it verified. §6
  defines two: …". §6 now defines three — the ratified region
  (doctrine:167-175), the whole-file regime for a matter whose proposed
  text is a separate document (doctrine:172-175), and the retroactive
  regime added at doctrine:177-182 by commit `7357244`, the same commit
  that wrote this bullet. The round 2 response entry above (m0007:131-137)
  states the third regime correctly — but a `## Vetting` append is
  outside the ratified region under §6:169-170, so the text the operator
  ratifies says two while the text they do not ratify says three. This
  is the shape of round 2's W2 recurring inside the commit that retired
  it. One word: "two" → "three", plus the retroactive regime in the
  list. Also recorded on m0001 as X6.
- **Related, not a finding here (m0001 X8):** §6's retroactive region is
  defined over `## Execution` "as it stands at the acknowledged commit",
  while §11:288-291 does not require that section at filing and §3.1
  makes it a precondition of the transition the acknowledgment causes.
  The check this matter builds cannot verify a regime whose region is
  not guaranteed to exist; the fix belongs in §11, not here.
- **Verified clean:** the round 2 finding was genuinely applied — the
  regime-naming requirement exists at m0007:39-46 and is not merely
  promised; frontmatter conforms; both links resolve.
