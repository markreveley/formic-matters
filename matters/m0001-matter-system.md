---
type: spec
title: The matter system
description: "Every change to beatcode or to this repository is proposed, vetted, and ratified as a matter before it is made."
id: m0001
state: proposed
status: draft
target: beatcode-dev
tags: [doctrine, bootstrap]
threads: [threads/2026-08-24-audit-and-adjudication.md]
generated:
  by: claude-code/2026-08-24
  at: 2026-08-24T22:33:00Z
---

# m0001 · The matter system

## Diagnosed reason

Changes to beatcode were being identified, diagnosed, and applied in
one unbroken motion, with no gate between noticing a problem and
editing the repo. A first attempt to fix this bootstrapped a process
doctrine, and failed its own audit: the doctrine was marked ratified
without the operator having read it, its execution summary misdescribed
the committed text, and its flagship matter punted a diagnosis whose
answer sat in the repository the whole time. The operator ruled to
archive that attempt unmerged (PR #1) and author this one fresh.

beatcode is a repository whose thesis is that behavior is pinned in
advance and verified against frozen goldens. Its development process
now has the same discipline — including over itself.

## Proposed text

[`doctrine/matters.md`](../doctrine/matters.md), in full. Ratifying
this matter is ratifying that document at a specific commit (doctrine
§6).

## What this supersedes

Nothing in this collection — it is the first matter. The archived first
attempt is referenced, not superseded. No text here derives from it;
rulings carried from its sessions are sourced per the ledger below.

## Rulings ledger

Every operator proposal and ruling from the 2026-08-24 sessions, and
where it landed. This table is what the fidelity review checks the
doctrine against, alongside the thread itself.

Sources. Rows marked **†** were ruled in the archived first attempt's
design session; they reach this collection through the operator's
carry-forward ruling, and each was affirmed — at the operator's
delegation — by the auditing agent, which read that session in full.
Both the delegation and the affirmation are recorded in
[the thread](../threads/2026-08-24-audit-and-adjudication.md). Clauses
marked **‡** are authoring-agent mechanisms adopted to satisfy a
ruling, not rulings; they are listed in doctrine §15 for deliberate
confirmation at ratification. Unmarked rows are ruled in the thread
directly.

| Operator proposal / ruling | Landed |
|---|---|
| † three change kinds as matter types; "proposal" not a type; types moved up one level | doctrine §2 |
| † per-type required content (fix: diagnosis + fix; feature: spec + plan; refactor: reason + plan) | doctrine §2 |
| state spine `proposed → ratified → staged → executed` | doctrine §3 |
| vetting by fresh agent reviews until the operator ratifies | doctrine §6 |
| execution by a dev agent launched by the operator; orchestration later, as its own matter | doctrine §3 |
| † cheap to file, expensive to ratify; diagnosis may arrive over several turns but precedes ratification | doctrine §4 |
| † split functions as supersession routing to offshoots | doctrine §5 |
| flat collection, metadata-sortable, all views derived | doctrine §1, §7, §12 |
| deterministic code wherever possible | doctrine §10 |
| † lenses/dry-round review machinery deferred as premature, filed as a matter | [m0006](m0006-review-lenses-and-dry-rounds.md) |
| † ratification content hash deferred unless MVP-required; record now, tooling later | doctrine §6 + [m0007](m0007-ratification-content-hash.md) |
| † "matter system operational" as a derived worklist view | doctrine §7 |
| † SPEC-GAPS broken out into matters, landed and otherwise; `spec` as a real type | [m0009](m0009-spec-gaps-to-matters.md), doctrine §2 |
| PRs cite matter IDs | doctrine §8 (commit trailer, branch/PR title prefix) |
| † process/system code kept separate from the instrument | [m0008](m0008-matter-tooling.md) |
| † consider OKF; keep the useful shape, no memory files in the repo | doctrine §12 (documented dialect) |
| thread persistence: verbatim human and agent turns, reasoning and tool traffic dropped, redact before publication | doctrine §9.2 + [m0011](m0011-thread-persistence.md) |
| runs directory documenting verification runs with environment specs | doctrine §9.1 |
| claims-DAG in the matter itself, visualization derived, nodes are not matters | doctrine §9.3 |
| retire PR comments; keep GitHub and PRs as transport and merge mechanics; operator responds by local file edits | doctrine §8 |
| one repo, self-hosting explicit, no framework split; extraction tripwire's specific conditions are ‡ | doctrine §1, §13 |
| archive the first attempt, do not expunge; fresh authoring, nothing textual carried | doctrine §14, this matter |
| landed/execution record required to enter `executed` | doctrine §3.1 |
| git citation convention (trailer + prefixes) | doctrine §8 |
| threads primary reference; adjudication thread exported into this tree; derived-views-over-threads formalization is ‡ | doctrine §9.2, [threads/2026-08-24-audit-and-adjudication.md](../threads/2026-08-24-audit-and-adjudication.md) |
| ratification gate over the exact text; operator prefers not to compute hashes locally; the recording mechanism (agent computes and records) is ‡ | doctrine §6 |
| † org/assertions raised; out-of-scope disposition derived from the operator's cross-repo separation ruling, never contradicted | noted under Scope below |
| vetting rounds recorded on the matter as appended entries | doctrine §6 |
| matters assert immutable references; no undated mutable-state claims | doctrine §9.4 |
| one-line provenance pointer to the archive | doctrine header + §14 |
| housekeeping: PR #1 closed unmerged, archive branch kept, planning drafts absorbed, directory names | executed at build |
| unprocessed operator proposals become matters | m0006, m0010, m0011 |
| relative links | doctrine §12 |

## Scope held out deliberately

The MVP line is **file · query · cannot corrupt**. Deferred to their
own matters rather than built now: review structure
([m0006](m0006-review-lenses-and-dry-rounds.md)), drift tooling
([m0007](m0007-ratification-content-hash.md)), the validator
([m0008](m0008-matter-tooling.md)), risk tiers
([m0010](m0010-risk-tiers.md)), thread policy
([m0011](m0011-thread-persistence.md)).

The operator's global-CLAUDE.md/assertions question raised in the first
attempt's session is cross-repo by definition and out of scope for this
collection.

## Execution

The tree was written together with this matter (doctrine §14): the
doctrine, matters m0001–m0011, the derived index, the first thread
export, the first run record, the interim index generator, and the
repository README. This
section is completed with commits and date when the matter reaches
`executed`, which under §14 happens immediately after ratification.

## Vetting

### Round 1 — 2026-08-25

- **Reviewer:** claude-code/2026-08-25, fresh instance. Inputs: this
  branch's tree at `44d6be0` and `ob6to8/beatcode` (`fa17627`, seed
  `91188a5`, `b2042746`); the archived first attempt not read, per
  operator instruction.
- **Checks run:** fidelity (rulings ledger ↔
  [thread](../threads/2026-08-24-audit-and-adjudication.md) ↔
  doctrine); verification of m0002–m0005 against beatcode, m0004's
  Claims table leaf by leaf and edge by edge, and `runs/` re-executed;
  consistency (§12 schema, §3 states, status derivation, links, index
  regeneration); state-machine holes; scope against this matter's
  claims.

**Findings, ranked by severity:**

**V1 · MEDIUM-HIGH — ten ledger rows are unverifiable against the
tree's own primary sources, and three provenance claims overstate.**
The preamble (m0001:46) says "Every operator proposal and ruling from
the 2026-08-24 sessions"; the tree's only thread is the adjudication
session. Rows 52 (types; "moved up one level"), 53 (per-type
content), 57 (cheap to file; diagnosis over turns), 58 (split as
supersession), 62 ("deferred unless MVP-required"), 63 (worklist
view), 64's breakout half, 66 (process code separate), 67's
no-memory-files clause, and 78 (org/assertions — no in-tree trace at
all, and its Landed column is a disposition, not a landing) contain
operator rulings that appear nowhere in that thread, not even as
quotes inside the audit report it embeds. The carry-forward ruling is
real (thread:605 — keep "the aspects ... that i proposed",
unprocessed proposals become matters), but it incorporates content
the tree does not contain: for those rows the fidelity review this
section prescribes (m0001:46-48) cannot distinguish operator design
from authoring-agent design without the archived first attempt's
design session. Meanwhile doctrine:15 says "nothing here depends on
it," m0001:41-42 says "this collection stands alone," and doctrine:6-7
names the adjudication thread as the rulings source — all three
overstate for exactly these rows. Suggested edit: mark
archive-sourced rows as such, and scope the stands-alone claims to
text, not provenance.

**V2 · MEDIUM — row 77 compiles an unruled mechanism into the ruling
column.** "ratification without operator-computed hashes: operator
reads and states; agent records commit + hash, independently
verifiable" merges three things of different standing: the gate
ruling (thread:284 — ruled), the no-local-hash preference (thread:602
— "would prefer to not have to compute the hash locally if that is an
option", ruled as a conditional preference), and the recording
mechanism now in doctrine §6:140-146 (`verified` +
`ratified_commit` + agent-computed `ratified_sha256`), which appears
in no operator turn and no agent turn before the thread ends — the
tree itself is its first presentation. It is legitimate candidate
text; a table of operator proposals and rulings is the wrong place
for it. Same class, smaller: row 72's "extraction on tripwire" clause
(the operator agreed "one repo, self hosting explicit", thread:555;
the tripwire is the authoring agent's design) and row 76's "views
over threads derived" clause (the agent's answer to the operator's
question at thread:467).

**V3 · MEDIUM — rulings ruled in the thread but absent from the
ledger, against its own "Every":** (a) vetting rounds recorded on the
matter as appended entries — approved at thread:467 ("re bigger
question, approve") and again as Q5 (thread:578-579, "1-5 yes" at
601); landed at doctrine §6:136-138; no row. (b) the
immutable-reference rule — "5 - agree" (thread:477); landed at
doctrine §9.4; no row. (c) Q4's one-line provenance
(thread:575-576, ruled at 601); landed at doctrine:13-15 and this
matter; no row. (d) Q9 housekeeping (thread:590-591, ruled at 604);
executed; no row. (e) unprocessed operator proposals become matters
(thread:605); instantiated by m0006/m0010/m0011; no row. (f, minor)
"14 - agree" — relative links (thread:481); landed §12; at best
subsumed by row 67.

**V4 · MEDIUM — m0010 attributes a deferral ruling the tree cannot
support** ("Deferred by the operator", m0010:48): risk tiers appear
nowhere in the thread and have no ledger row — either the ledger is
incomplete or the attribution is wrong. Recorded matter-locally on
m0010.

**V5 · MEDIUM-LOW — three defaults are embedded without a ruling and
nothing surfaces them as pending.** The operator's final turn ruled
Q1-5 and Q9; Q6 got a preference, and the reply to Q7/Q8 was a
clarifying question (thread:603) the thread's end left unanswered.
The tree embeds the defaults as candidate text: the §6 recording
mechanism (V2), the interspersed one-sequence collection answering
the operator's own question (doctrine §1:35-38), and the ID restart
(§12:252-253), with Q7's bundle-first sequencing implicit in
m0002-m0005 filed `proposed`. Nothing presents these as ruled — the
gap is that nothing flags them for the ratification read either.
Suggested edit: a short "adopted by default, confirm at ratification"
list, here or in §15.

**V6 · MEDIUM-LOW — state-machine holes (check 4):** (a) terminal
transitions have no owner — §3:80-92 assigns owners to the four spine
transitions only; who may move a matter to
`rejected`/`withdrawn`/`superseded` is unstated. (b) `withdrawn`
"before a decision" (§3:77) and `rejected` "considered and declined"
(§3:76) contradict their own reachability from `ratified`/`staged`,
and un-ratifying leaves `verified`/`ratified_*` semantics undefined.
(c) §5:123-124's conflict remedy "superseded or **amended**" names a
mechanism defined nowhere in the doctrine. (d) this matter's own path
(m0001:98-100: `executed` "immediately after ratification") is a
`ratified → executed` transition §3 does not define — §14 licenses
the out-of-order execution but never amends the transition set; §11's
birth-at-`executed` is likewise outside the diagram. (e)
`staged → proposed` records the failure on the matter, but nothing
records or unwinds what half-landed in the target — the execution
record exists only on entering `executed`. (f) two already-ratified
matters discovered to conflict: §5 gates ratification time only; no
precedence or resolution rule exists afterward. (g) §7's `depends_on`
is an "execution-order constraint" with no transition-time
enforcement (m0008's list has acyclicity only). (h) a retroactive
matter the operator declines to acknowledge has no path: nothing
leaves `executed`, and §11's `verified` slot cannot record a refusal.

**V7 · LOW-MEDIUM — scope: README.md is in the tree but unclaimed.**
The Execution list above (m0001:96-98) omits it; the bootstrap
commit's message claims it. This is the same omission the archived
attempt was audited for. One-line fix.

**V8 · LOW — matter-local findings, recorded on their matters:**
m0004 (one-byte drift in a verbatim quote), m0007 (§6's whole-file
hash vs the recording act; a doctrine edit planned from a `feature`
matter), m0010 (V4), m0011 (thread-header citations), m0003 (two
characterization nits).

**V9 · LOW — run-record nits** (recorded here; `runs/` files are
never edited): the Python version behind the golden-derived
computation is unstated, though §9.1 requires tool versions; and step
1 records a formula rather than "the exact commands". Both sufficed
to reproduce regardless.

**Checks passed clean:**

- **m0002, in full.** SPEC.md:750-752 quoted verbatim; §6.2:484-488
  states association correctly as claimed, making §9.3 the outlier;
  the §1.1-to-m0003 scoping is correct; the IEEE-754 statement
  (commutative, sign of zero included; associativity is what fails)
  is correct as stated; `b2042746` is the head of
  `docs/pipeline-order-clarity` on the beatcode remote; the Notes
  conform to §9.4 immutability.
- **m0003,** except two nits recorded there: `src/events.rs:196`
  exact (fan-out + left-to-right sum, terminal `clamp0`, swing and
  lane reading pristine `grid`, humanize keyed `(voice, "hum",
  step)`); §6.5's odd-integer gate, §6.3's `floor_i` indexing,
  §4.4's underived threshold, §3's "only rational→float edge" all
  exact; itemized-ms survival of the clamp confirmed in the dilla
  golden (kick step 0: `lane_ms: -4.0`, `performed_s: 0.0`).
- **m0004, in full** (one transcription byte aside): every leaf and
  edge of the Claims table verified independently, C5 re-executed on
  this machine — record on m0004.
- **m0005, in full:** README:40-45 and :54 quoted accurately;
  `fa17627` is the merge of PR #2; 14 modules under `src/`; 48 tests
  across 15 binaries reproduced green.
- **The run record, re-executed end to end** on the pinned 1.94.1
  toolchain: all four golden-derived rows (events, `last`, frames,
  bytes) recomputed to exact agreement; `check_renders.sh` ok for all
  four; rendered sizes match; SPEC.md and `goldens/events/` confirmed
  byte-identical seed↔`fa17627`.
- **Consistency, all assigned checks:** every frontmatter field used
  is defined in §12 (subkeys included) and every timestamp conforms;
  only `proposed` is used and it is in §3; status derivation holds
  everywhere; all 52 relative links resolve and none use the
  leading-slash form; `tools/gen-index.py` regenerates
  `matters/index.md` byte-identically; every ledger Landed target
  exists and contains what the row says landed there; required
  sections are consistent with every matter's state; IDs are
  sequential, filenames conform; SPEC-GAPS.md has exactly nine
  entries (m0009).
- **Git citation:** the bootstrap commit carries the `Matter: m0001`
  trailer (§8).

Not checked: PR #1's archival state (unread, per instruction), and
the content of V1's archive-sourced rows (unverifiable in-tree by
construction — that is the finding).

- **Disposition:** all findings are vetting-scale text edits; no
  claim in m0002–m0005 failed verification, and nothing found blocks
  continued vetting. V1-V3 are corrections to this file's ledger and
  the provenance lines; V5 is a flag the operator should see at the
  ratification read; V6 is §3/§5 doctrine text; V7 is one line.

### Round 1 response — 2026-08-25 — claude-code/2026-08-24 (author)

All nine findings accepted; none disputed. Applied in this commit, on
operator instruction ("apply", recorded in
[the thread](../threads/2026-08-24-audit-and-adjudication.md)):

- **V1** — the operator delegated the attestation ("if you agree,
  affirm") and the auditing agent, which read the archived design
  session in full, affirmed each flagged ruling in the thread, quoting
  the operator's words. The ledger preamble now defines the † source
  marking and cites that exchange; the doctrine header and this
  matter's supersession note are scoped to *text*, not provenance.
  Supplementing the in-thread affirmation for two rows it named only
  via m0010: the lenses deferral is likewise witnessed — operator:
  "this is a pain I as an operator have not felt yet … i propose this
  should be filed as a feature matter" — and the tiers deferral:
  "same thoughts as 4".
- **V2** — rows 72, 76, 77 reworded to separate ruling from mechanism;
  ‡ marking defined; all ‡ items listed in doctrine §15 for deliberate
  confirmation at ratification. Timing note: the reviewer worked at
  `44d6be0`; the export update `1347af3` landed afterward and now
  shows the §6 mechanism being presented to the operator, so V2's
  "first presentation" clause is historical — its substance (no
  operator ruling) stands and is what §15 now flags.
- **V3** — six rows added (vetting-in-matter, immutable references,
  provenance line, housekeeping, proposals-become-matters, relative
  links).
- **V4** — m0010 reworded to cite the archived deferral ruling under
  the † convention; see m0010's response entry.
- **V5** — doctrine §15 is now "Open, and adopted by default", listing
  all six defaults for confirmation at the ratification read.
- **V6** — doctrine §3 rewritten: owners for every transition;
  `rejected`/`withdrawn` from `proposed` only; `ratified → proposed`
  re-open defined with ratification fields cleared into the record;
  the failure record must state what half-landed and its disposal;
  the two licensed diagram exceptions (§11 retroactive entry, §14
  bootstrap) stated. §5: "or amended" dropped; later-discovered
  conflicts resolved by earlier-ratification precedence until the
  operator supersedes. §11 redesigned: retroactive matters file as
  `proposed` and reach `executed` on acknowledgment; refusal →
  `rejected` plus an unwinding matter (m0009's wording aligned).
  `depends_on` transition-time enforcement added to m0008's list.
- **V7** — README claimed in the Execution list.
- **V8** — matter-local fixes applied; see the response entries on
  m0003, m0004, m0007, m0010, m0011.
- **V9** — accepted for future runs: interpreter versions and exact
  commands. Recorded here since run files are never edited.
- **Reviewer deviation, recorded:** round 1 re-executed the
  verification but filed the evidence inline in vetting entries
  rather than as an append-only `runs/` file (§9.1). The evidence
  stands; the next run record follows §9.1, and the round-2 prompt
  should restate the requirement.
