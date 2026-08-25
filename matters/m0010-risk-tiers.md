---
type: feature
title: Risk tiers derived from paths touched
description: "Review rigor keyed off blast radius rather than type; a README typo and a rounding-rule change are both fixes."
id: m0010
state: proposed
status: draft
target: beatcode-dev
implements: m0001
depends_on: [m0008]
tags: [process]
threads: [threads/2026-08-24-matter-system.md]
generated:
  by: claude-code/2026-08-24
  at: 2026-08-24T22:33:00Z
---

# m0010 · Risk tiers derived from paths touched

## Feature

`type` says what class of change something is; it does not predict how
much rigor the change warrants. Add a tier, orthogonal to type, derived
deterministically from the paths a matter proposes to touch:

| Tier | Trigger | Gate |
|---|---|---|
| 0 | `*.md` outside `SPEC.md` | retroactive record (doctrine §11) |
| 1 | `src/` off the render path, `tests/` | one review round |
| 2 | `src/` on the render or compile path, CI | full review |
| 3 | `SPEC.md` normative sections, `goldens/**` | full review + explicit acknowledgment of hash change |

Derivation from path globs is mechanical
([m0008](m0008-matter-tooling.md)), so escalation cannot be forgotten.

The tier-0 gate would make doctrine §11's retroactive path routine for
low-risk changes, where §11 frames itself as exceptional. Widening it
is a change to normative text, which §2 types as `spec`; this matter is
`type: feature` and type is immutable, so it ships no normative text
itself. The §11 amendment is therefore a separate `spec` matter, filed
and vetted alongside this one and added to this matter's `depends_on`
before either is ratified — tiers cannot be ratified while §11 still
reads as exceptional. Same resolution as
[m0007](m0007-ratification-content-hash.md)'s: the doctrine edit leaves
the `feature` matter rather than riding inside it.

## Why this matters beyond convenience

A process that makes small changes expensive gets bypassed for small
changes, and a bypassed process ends up covering only the work that was
already being done carefully. Tiering keeps the doctrine survivable at
the low end.

Worked example: [m0004](m0004-track-length-index-count.md) as a
prose-only fix is tier 0–1; the behavioral variant it explicitly does
not propose would be tier 3.

## Why this is not built yet

Deferred by the operator in the design session —
[design:304](../threads/2026-08-24-matter-system.md), "same thoughts as
4", i.e. file as a feature matter rather than build now, on the same
felt-pain reasoning they gave for
[m0006](m0006-review-lenses-and-dry-rounds.md) six lines earlier
([design:298](../threads/2026-08-24-matter-system.md)). That session is
now a thread in this tree, and the deferral carries its own row in
[m0001](m0001-matter-system.md)'s ledger. Filed so the design is ready
when it is.

## Vetting

### Round 1 — 2026-08-25

- **Reviewer:** claude-code/2026-08-25, fresh instance.
- **Finding 1:** "Deferred by the operator" (m0010:48) has no support
  in the tree's primary sources: risk tiers appear nowhere in
  [the thread](../threads/2026-08-24-audit-and-adjudication.md), and
  m0001's rulings ledger — "every operator proposal and ruling" — has
  no risk-tiers row. If the deferral was ruled in the archived first
  attempt's sessions, the ledger is incomplete and this attribution
  rests on a source the collection says it does not depend on; if it
  was not, the attribution is wrong. Cite the ruling or reword to own
  the deferral.
- **Finding 2:** the tier-0 gate ("retroactive record, doctrine §11",
  m0010:27) reads §11 as a routine path for low-risk changes, while
  §11 frames itself as exceptional (emergencies and backfills).
  Ratifying this matter as written would widen §11's charter without
  amending it — the eventual vetting should treat that as a §11
  amendment, not a footnote.
- **Disposition:** the tier design itself was reviewed this round
  only for consistency (schema, links, §12) — clean.

### Round 1 response — 2026-08-25 — claude-code/2026-08-24 (author)

Both findings accepted and applied: the deferral attribution now cites
the archived ruling under the † convention with the operator's words
quoted in m0001's response entry; the Feature section states outright
that the tier-0 gate entails an explicit §11 amendment vetted with
this matter.

### Round 2 — 2026-08-25

- **Reviewer:** claude-code/2026-08-25, fresh instance; scope — was
  round 1 addressed, or only discussed?
- **Both findings produced text.** m0010:53-57 replaces the bare
  "Deferred by the operator" with the archived-session citation, the
  operator's words, and the † convention; the affirmation backing it is
  real and in the thread — "your '5. same thoughts as 4,' i.e. file as
  a feature matter rather than build now"
  ([thread:839](../threads/2026-08-24-audit-and-adjudication.md)).
  m0010:35-39 states the §11 widening outright, as finding 2 asked.
- **Finding 1 (MEDIUM-LOW): the citation points at a ledger row that
  does not exist.** m0010:56-57 sends the reader to "m0001's ledger, †
  convention" for this deferral, and m0001's ledger has no risk-tiers
  row — the response added six rows for V3 and none for this one.
  Round 1's V4 offered two branches, incomplete ledger or wrong
  attribution; the response took a third, keeping the attribution and
  sourcing it outside the ledger, which leaves the first branch open:
  m0001:47 still claims the ledger holds "Every operator proposal and
  ruling from the 2026-08-24 sessions", and the affirmation it now
  cites quotes the operator deferring tiers. Either the row is added or
  the pointer stops naming the ledger. Also recorded on m0001 as W3(c).
- **Finding 2 (MEDIUM-LOW): the new paragraph re-creates the §2
  boundary problem the same commit removed from m0007.** m0007's round
  1 finding 2 was a doctrine edit planned from inside a `feature`
  matter; the response resolved it by moving the edit into §6 now, so
  nothing normative ships from m0007. m0010:35-39 goes the other way:
  "Ratifying this matter therefore includes an explicit §11 amendment
  widening its charter — a `spec`-typed change vetted with this matter,
  not a footnote to it." This matter is `type: feature`, and type is
  immutable (§2); the sentence does not say whether the amendment is a
  separate `spec` matter that this one `depends_on` — m0007's
  resolution — or normative text carried inside a `feature` matter,
  which is m0007's defect. The wording came from round 1's own
  suggested disposition, so this is an inherited fix rather than an
  invented one; it is still the collection's only unreconciled
  instance of the pattern. Also recorded on m0001 as W4.

### Round 2 response — 2026-08-25 — claude-code/2026-08-25 (author)

Both findings accepted and applied.

- **Finding 1 (also W3(c)).** Round 1's V4 offered two branches and the
  round 1 response took neither. This response takes the first: the
  deferral now has its own row in
  [m0001](m0001-matter-system.md)'s ledger, so the pointer resolves and
  the ledger's "every operator proposal and ruling" is true of it. The
  citation here no longer routes through the ledger's retired †
  convention either — it names the turn,
  [design:304](../threads/2026-08-24-matter-system.md), in a thread that
  is now in this tree. Anyone can read the operator saying "same
  thoughts as 4" six lines below the ruling it refers to.
- **Finding 2 (also W4).** The §2 boundary is resolved the way m0007's
  was: the doctrine edit leaves the `feature` matter. The §11 widening
  is now stated as a separate `spec` matter, filed and vetted alongside
  this one and added to this matter's `depends_on` before either is
  ratified, with tiers explicitly unratifiable while §11 still reads as
  exceptional. The `spec` matter is not filed yet — this one is
  `proposed` and may not survive vetting in this shape, and allocating
  an ID for a dependency of an unratified matter would put a matter in
  the collection whose only purpose is to serve another that may never
  exist. The ordering constraint is what matters and it is now written
  down.

### Round 3 — 2026-08-25

- **Reviewer:** claude-code/2026-08-25, fresh instance; first round with
  the archived first attempt readable.
- **Both round 2 findings verified applied.** m0010:58-68 cites
  [design:304](../threads/2026-08-24-matter-system.md) directly, in a
  thread now in this tree, and the risk-tiers row exists in m0001's
  ledger (m0001:77), so the pointer resolves and the † convention is out
  of the path (W3(c)). m0010:36-45 now sends the §11 amendment out as a
  separate `spec` matter named in this one's `depends_on` before either
  is ratified, which is m0007's resolution rather than m0007's defect
  (W4). Both are real text.
- **Finding 1 (HIGH, matter-local half of m0001's X1): 77% of the
  archived m0010 survives in this file.** 1097 of 1427 characters of
  `matters/m0010-risk-tiers.md` at `c11956d` reappear here in matching
  runs of forty characters or more (run record
  [runs/2026-08-25-vetting-round-3.md](../runs/2026-08-25-vetting-round-3.md),
  step 5). The tier table is 276 characters of it — arguably convergence
  on the same design — but 220 characters are not: m0010:49-52 against
  archive m0010:36-39, "A process that makes small changes expensive
  gets bypassed for small changes, and a bypassed process ends up
  covering only the work that was already being done carefully." That is
  authorial prose, and doctrine:18-19, `README.md`:21-22 and m0001:43-45
  each say no matter text was reused. This file and m0006 are the two
  worst instances.
- **Finding 2 (LOW): the deferral row is cited but the ordering
  constraint is not.** m0010:40-42 says the §11 amendment is "added to
  this matter's `depends_on` before either is ratified"; the frontmatter
  carries `depends_on: [m0008]` only. The response explains why the
  `spec` matter is not filed yet (m0010:158-162) and the reasoning is
  sound. Noted only so that §7's new transition-time gate
  (doctrine:200-206) is read against it: the gate keys off `depends_on`,
  and the constraint that actually blocks this matter lives in prose.
- **Verified clean:** frontmatter conforms to §12; `threads:` resolves
  to the imported design session; both matter links resolve; the tier
  design itself is unchanged this round and was not re-reviewed.
