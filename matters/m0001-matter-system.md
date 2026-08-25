---
type: spec
title: The matter system
description: "Every change to beatcode or to this repository is proposed, vetted, and ratified as a matter before it is made."
id: m0001
state: proposed
status: draft
target: beatcode-dev
tags: [doctrine, bootstrap]
threads:
  - threads/2026-08-24-matter-system.md
  - threads/2026-08-24-audit-and-adjudication.md
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
attempt is referenced, not superseded: none of its doctrine or matter
text was reused. Its design session is exported into
[`threads/`](../threads/2026-08-24-matter-system.md) as a primary
source, so the rulings it carries are read here rather than attested to.

## Rulings ledger

Every operator proposal and ruling from the 2026-08-24 sessions, and
where it landed. This table is what the fidelity review checks the
doctrine against, alongside the threads themselves.

Both sessions are in this tree: the
[design session](../threads/2026-08-24-matter-system.md) and the
[adjudication session](../threads/2026-08-24-audit-and-adjudication.md).
**Ruled in** cites the turn, so every row is checkable here. Clauses
marked **‡** are authoring-agent mechanisms adopted to satisfy a
ruling, not rulings; doctrine §15 lists them for confirmation at
ratification.

| Operator proposal / ruling | Landed | Ruled in |
|---|---|---|
| describe, do not fix: nothing lands on sight, and work already applied is rolled back and filed as matters to be ratified | doctrine §1, and this matter's Diagnosed reason | [design:146](../threads/2026-08-24-matter-system.md), [design:287](../threads/2026-08-24-matter-system.md) |
| three change kinds as matter types; "proposal" not a type; types moved up one level | doctrine §2 | [design:280-284](../threads/2026-08-24-matter-system.md) |
| per-type required content (fix: diagnosis + fix; feature: spec + plan; refactor: reason + plan) | doctrine §2 | [design:169-171](../threads/2026-08-24-matter-system.md) |
| state spine `proposed → ratified → staged → executed` | doctrine §3 | [design:280](../threads/2026-08-24-matter-system.md) |
| vetting by fresh agent reviews until the operator ratifies | doctrine §6 | [design:173](../threads/2026-08-24-matter-system.md) |
| execution by a dev agent launched by the operator; orchestration later, as its own matter | doctrine §3 | [design:173](../threads/2026-08-24-matter-system.md) |
| cheap to file, expensive to ratify; diagnosis may arrive over several turns but precedes ratification | doctrine §4 | [design:287](../threads/2026-08-24-matter-system.md) |
| split functions as supersession routing to offshoots | doctrine §5 | [design:307](../threads/2026-08-24-matter-system.md) |
| flat collection, metadata-sortable, all views derived | doctrine §1, §7, §12 | [design:175](../threads/2026-08-24-matter-system.md) |
| deterministic code wherever possible | doctrine §10 | [design:177](../threads/2026-08-24-matter-system.md) |
| lenses/dry-round review machinery deferred as premature, filed as a matter | [m0006](m0006-review-lenses-and-dry-rounds.md) | [design:298](../threads/2026-08-24-matter-system.md) |
| ratification content hash deferred unless MVP-required; record now, tooling later | doctrine §6 + [m0007](m0007-ratification-content-hash.md) | [design:301](../threads/2026-08-24-matter-system.md), [design:449](../threads/2026-08-24-matter-system.md) |
| risk tiers deferred on the same reasoning — "same thoughts as 4" | [m0010](m0010-risk-tiers.md) | [design:304](../threads/2026-08-24-matter-system.md) |
| "matter system operational" as a derived worklist view | doctrine §7 | [design:301](../threads/2026-08-24-matter-system.md) |
| SPEC-GAPS broken out into matters, landed and otherwise; `spec` as a real type | [m0009](m0009-spec-gaps-to-matters.md), doctrine §2 | [design:316](../threads/2026-08-24-matter-system.md), [design:456](../threads/2026-08-24-matter-system.md) |
| PRs cite matter IDs | doctrine §8 (commit trailer, branch/PR title prefix) | [design:317](../threads/2026-08-24-matter-system.md) |
| process/system code kept separate from the instrument | [m0008](m0008-matter-tooling.md) | [design:310](../threads/2026-08-24-matter-system.md), [design:450](../threads/2026-08-24-matter-system.md) |
| consider OKF; keep the useful shape, no memory files in the repo | doctrine §12 (documented dialect) | [design:453](../threads/2026-08-24-matter-system.md), [design:486](../threads/2026-08-24-matter-system.md) |
| org/assertions raised as a matter, then withdrawn once identified as the operator's global CLAUDE.md; the out-of-scope disposition is derived from the cross-repo separation ruling and was never contradicted | noted under Scope below | [design:318](../threads/2026-08-24-matter-system.md), [design:450](../threads/2026-08-24-matter-system.md), [design:457](../threads/2026-08-24-matter-system.md) |
| thread persistence: verbatim human and agent turns, reasoning and tool traffic dropped, redact before publication | doctrine §9.2 + [m0011](m0011-thread-persistence.md) | [design:567](../threads/2026-08-24-matter-system.md), [design:660](../threads/2026-08-24-matter-system.md), [adjudication:264](../threads/2026-08-24-audit-and-adjudication.md) |
| runs directory documenting verification runs with environment specs | doctrine §9.1 | [adjudication:260](../threads/2026-08-24-audit-and-adjudication.md) |
| claims-DAG in the matter itself, visualization derived, nodes are not matters | doctrine §9.3 | [adjudication:270](../threads/2026-08-24-audit-and-adjudication.md) |
| retire PR comments; keep GitHub and PRs as transport and merge mechanics; operator responds by local file edits | doctrine §8 | [adjudication:471](../threads/2026-08-24-audit-and-adjudication.md), [adjudication:553](../threads/2026-08-24-audit-and-adjudication.md) |
| one repo, self-hosting explicit, no framework split; extraction tripwire's specific conditions are ‡ | doctrine §1, §13 | [adjudication:479](../threads/2026-08-24-audit-and-adjudication.md), [adjudication:555](../threads/2026-08-24-audit-and-adjudication.md) |
| archive the first attempt, do not expunge; fresh authoring, nothing textual carried | doctrine §14, this matter | [adjudication:551](../threads/2026-08-24-audit-and-adjudication.md) |
| landed/execution record required to enter `executed` | doctrine §3.1 | [adjudication:565](../threads/2026-08-24-audit-and-adjudication.md), [adjudication:601](../threads/2026-08-24-audit-and-adjudication.md) |
| git citation convention (trailer + prefixes) | doctrine §8 | [adjudication:568](../threads/2026-08-24-audit-and-adjudication.md), [adjudication:601](../threads/2026-08-24-audit-and-adjudication.md) |
| threads primary reference; adjudication thread exported into this tree; derived-views-over-threads formalization is ‡ | doctrine §9.2, [threads/2026-08-24-audit-and-adjudication.md](../threads/2026-08-24-audit-and-adjudication.md) | [adjudication:467](../threads/2026-08-24-audit-and-adjudication.md), [adjudication:557](../threads/2026-08-24-audit-and-adjudication.md), [adjudication:571](../threads/2026-08-24-audit-and-adjudication.md) |
| ratification gate over the exact text; operator prefers not to compute hashes locally; the recording mechanism (agent computes and records) is ‡ | doctrine §6 | [adjudication:284](../threads/2026-08-24-audit-and-adjudication.md), [adjudication:602](../threads/2026-08-24-audit-and-adjudication.md) |
| vetting rounds recorded on the matter as appended entries | doctrine §6 | [adjudication:467](../threads/2026-08-24-audit-and-adjudication.md), [adjudication:578](../threads/2026-08-24-audit-and-adjudication.md), [adjudication:601](../threads/2026-08-24-audit-and-adjudication.md) |
| matters assert immutable references; no undated mutable-state claims | doctrine §9.4 | [adjudication:477](../threads/2026-08-24-audit-and-adjudication.md) |
| one-line provenance pointer to the archive | doctrine header + §14 | [adjudication:575](../threads/2026-08-24-audit-and-adjudication.md), [adjudication:601](../threads/2026-08-24-audit-and-adjudication.md) |
| housekeeping: PR #1 closed unmerged, archive branch kept, planning drafts absorbed, directory names | executed at build; the archive branch `m0001-matter-system` and doctrine §14 are its in-tree traces | [adjudication:590](../threads/2026-08-24-audit-and-adjudication.md), [adjudication:604](../threads/2026-08-24-audit-and-adjudication.md) |
| unprocessed operator proposals become matters | [m0006](m0006-review-lenses-and-dry-rounds.md), [m0010](m0010-risk-tiers.md), [m0011](m0011-thread-persistence.md) | [adjudication:605](../threads/2026-08-24-audit-and-adjudication.md) |
| relative links | doctrine §12 | [adjudication:481](../threads/2026-08-24-audit-and-adjudication.md) |

## Scope held out deliberately

The MVP line is **file · query · cannot corrupt**. Deferred to their
own matters rather than built now: review structure
([m0006](m0006-review-lenses-and-dry-rounds.md)), drift tooling
([m0007](m0007-ratification-content-hash.md)), the validator
([m0008](m0008-matter-tooling.md)), risk tiers
([m0010](m0010-risk-tiers.md)), thread policy
([m0011](m0011-thread-persistence.md)).

The operator's global-CLAUDE.md/assertions question is out of scope for
this collection. It is the one row of the ledger whose *disposition* is
derived rather than stated, and the derivation is now readable end to
end: proposed as a matter
([design:318](../threads/2026-08-24-matter-system.md)), then narrowed by
the operator once they identified the file as their user-level global
CLAUDE.md rather than a repo one
([design:457](../threads/2026-08-24-matter-system.md)), which makes it
cross-repo by definition and so excluded by their own "concerns across
repos are not mixed"
([design:450](../threads/2026-08-24-matter-system.md)). Never
contradicted afterwards.

## Execution

The tree was written together with this matter (doctrine §14) and has
grown with its vetting. Everything in it is claimed here: the doctrine,
matters m0001–m0011, the derived index, the interim index generator,
the repository README, both thread exports in `threads/` (the design
session imported verbatim from the archive branch in round 2's
response, the adjudication session exported by its participating
agent), and every record in `runs/`. Nothing else is in the tree. This
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

### Round 2 — 2026-08-25

- **Reviewer:** claude-code/2026-08-25, fresh instance. Inputs: this
  branch at `981b2a6`, the diff `7022aad..981b2a6`, and
  `ob6to8/beatcode` at `fa17627` (seed `91188a5`); the archived first
  attempt not read, per operator instruction.
- **Scope:** one question — were round 1's findings actually
  addressed, or only discussed? Each V1–V9 disposition and each
  matter-local response claim checked against the text as it now
  stands, plus anything the response edits newly broke. Re-verification
  evidence is in
  [runs/2026-08-25-round-2-response-verification.md](../runs/2026-08-25-round-2-response-verification.md),
  per §9.1 and the deviation round 1's response recorded (m0001:351).

**Applied, verified against the text:**

- **V1 — applied.** All ten flagged rows now carry † (m0001:64, 65, 69,
  70, 74, 75, 76, 78, 79, 90); the affirmation is real and in the
  thread (thread:828-842), quoting an operator turn for each of the
  ten. Provenance scoped to text at doctrine:13-18 and m0001:41-43.
  Two residues: W2, W3.
- **V2 — applied.** Rows 84, 88, 89 separate ruling from mechanism; ‡
  defined at m0001:56-59; all three ‡ clauses appear in doctrine §15.
  See W11 for the timing note's wording.
- **V3 — applied.** Six rows added (m0001:91-96), one per finding
  (a)-(f). Each Landed target checked and contains what its row says,
  with the exception noted in W10(a).
- **V4 — applied in part.** m0010:53-57 now cites the archived ruling
  under †, and the affirmation carries it (thread:839). The other half
  of the finding is untouched: W3.
- **V5 — applied.** doctrine:358-382 lists all four defaults V5 named
  plus two more, for confirmation at the ratification read. Framing nit:
  W12.
- **V6 — applied, (a)-(h) each have text.** (a) owners for
  `rejected`/`withdrawn`/`superseded` at doctrine:99-104. (b)
  proposed-only terminals, and `ratified → proposed` clearing the
  ratification fields into the record (doctrine:96-102). (c) "or
  amended" gone from §5 (doctrine:140-142) — but see W5. (d) licensed
  exceptions stated at doctrine:107-110. (e) half-landed disposal in
  the failure record (doctrine:91-95). (f) earlier-ratification
  precedence (doctrine:144-147). (g) enforcement added to m0008:36-37
  — see W6. (h) §11 refusal path (doctrine:269-270), m0009 aligned.
- **V7 — applied.** README claimed at m0001:117; the Execution list now
  covers every path in the tree.
- **V8 — applied; both beatcode-facing fixes verified against the
  source.** m0003's two nits and m0004's byte are correct at `fa17627`
  (run record, steps 1-3). m0007's rewrite genuinely resolves both its
  findings (see the m0007 note). m0010 and m0011 applied, each with a
  residue recorded on the matter.
- **V9 — no action was possible and none was claimed;** but the run
  file promised alongside it did not ship: W11(b).

**Findings, ranked by severity:**

**W1 · MEDIUM — the ratification pin the operator is holding is stale,
and nothing in the tree says so.** The thread hands the operator a pin
to ratify against: "`doctrine/matters.md` at commit `44d6be0`, sha256
`034d46bf…c7f0ef` … ready when you are" (thread:627). That hash is
correct for `44d6be0`, `7022aad` and `1347af3`, and the response
commit rewrote §3, §5, §6, §11 and §15: at `981b2a6` the doctrine
hashes `67fada5c…7bad0` (run record, step 6). The stale pin is still
the only pin in the primary source, the response entry does not
mention it, and §6 makes ratification an act over exact text at a
named commit. This is the archived attempt's failure mode with the
polarity reversed — not text changed after ratification, but a
ratification target quoted before it. Suggested: state the current
commit and hash where the operator will look, or say in-thread that
the pin moved.

**W2 · MEDIUM — one † row's affirmation is not where the preamble says
it is, and it is outside the ratified region.** The Sources paragraph
(m0001:51-60) says of every † row that it "was affirmed … by the
auditing agent" and that "Both the delegation and the affirmation are
recorded in [the thread]". The affirmation (thread:828-842) covers
exactly V1's ten rows plus the risk-tiers deferral. Row 73
(lenses/dry-rounds → m0006) carries a † and appears in it nowhere. Its
only in-tree support is an operator quote the author supplied inside
this file's own round 1 response (m0001:316-320) — a `## Vetting`
append, which under the §6 the same commit wrote sits *outside* the
ratified region, so the operator ratifying the ledger is not ratifying
the evidence for that row. Note also that row 73 was not one of V1's
ten: the response marked it † on its own initiative and sourced it
with fresh archive-derived testimony. That is a new archive dependency
introduced by the fix for an archive-dependency finding, not a
correction of one.

**W3 · MEDIUM — V1's third named site was not edited, a fourth keeps
the flagged wording, and V4's "ledger is incomplete" branch is
unresolved.** (a) V1 named three overstatements; two were fixed.
doctrine:6-7 — "Authored fresh on 2026-08-24 against the operator
rulings recorded in [the thread]" — is byte-identical to its
pre-response text. It is now *nearly* true, rescued by the affirmation
`981b2a6` appended to the thread, and it still fails for row 73 (W2).
(b) `README.md:21` still reads "the first was audited and archived
unmerged (PR #1), and nothing here depends on it" — the exact clause
V1 flagged, unscoped, in the one file this same commit added to the
Execution list for V7. (c) V4 offered two branches — incomplete ledger,
or wrong attribution. The response took neither: it kept the
attribution and sourced it to the archive, leaving no risk-tiers row in
a ledger whose preamble still claims "Every operator proposal and
ruling from the 2026-08-24 sessions" (m0001:47, unedited) while the
affirmation it now cites quotes the operator deferring tiers
(thread:839). m0010:56-57 compounds it by pointing the reader at
"m0001's ledger, † convention" for a ruling that has no row there.
Recorded matter-locally on m0010 as well.

**W4 · MEDIUM-LOW — the m0010 fix re-creates the §2 boundary problem
the same commit removed from m0007.** Detail on m0010; noted here
because it is the collection's only remaining instance of the pattern
round 1 objected to.

**W5 · LOW-MEDIUM — V6(c) is half-applied.** §5 no longer names
amendment (doctrine:140-142), but m0008:40-41 still specifies the
validator against "the supersession/amendment link (doctrine §5)" — a
check written against a mechanism the doctrine no longer defines. The
same commit edited m0008 four lines above. Recorded on m0008.

**W6 · LOW-MEDIUM — V6(g)'s fix put a normative rule in a tooling
matter.** The transition-time `depends_on` rule ("a matter cannot be
staged or executed while a dependency is unexecuted") exists only at
m0008:36-37; §7:183 still describes `depends_on` as an
"execution-order constraint" with no transition rule, so the validator
is specified to enforce something the doctrine does not say. The rule
also has no §11 exception: the retroactive path is for work that
"cannot wait" (doctrine:264) and reaches `executed` without ever being
`staged`, so a retroactive matter carrying a `depends_on` would be
blocked by the validator on the one path designed to bypass gates.
Recorded on m0008.

**W7 · LOW — the new §6 region and the new §11 leave a retroactive
matter's hashed text undefined.** §6:165-170 excludes `## Vetting` and
`## Execution` from the ratified region. §11:264-270 now routes
retroactive matters `proposed → executed` on the operator's
acknowledgment, and §3.1 requires the `## Execution` section — what
actually landed, and deviations — to enter `executed`. For a
retroactive matter the acknowledgment *is* the ratifying act, and the
record of what is being acknowledged sits in the section the hash
excludes. Neither section says what `ratified_sha256` covers in that
case. Both halves are new in this commit; the interaction is not.

**W8 · LOW — the thread's header was edited to settle a finding, the
response record does not say so, and the edited sentence is now false.**
Detail on m0011.

**W9 · LOW — three residues in the ledger fixes.** (a) The new
housekeeping row's Landed column is "executed at build" (m0001:94) — a
disposition with no in-tree target, the same shape V1 objected to on
row 90, and unreachable by round 1's clean check that "every ledger
Landed target exists and contains what the row says landed there": its
subject is PR #1, which reviewers are instructed not to read. (b) The
proposals-become-matters row (m0001:95) gives "m0006, m0010, m0011" as
bare text where every other matter reference in the ledger is a
relative link. (c) The preamble says † rows "were ruled in the archived
first attempt's design session", but row 90's own text says its
disposition is "derived … never contradicted", and the affirmation is
explicit that this row is a derivation and not a verbatim ruling
(thread:840). The blanket sentence contradicts the row it covers.

**W10 · LOW — two response-entry claims are looser than the record.**
(a) The V2 timing note (m0001:323-327) says the export update "now
shows the §6 mechanism being presented to the operator, so V2's 'first
presentation' clause is historical". The turn `1347af3` appended is the
build-report turn, which announces the bundle as already built and
pushed at `44d6be0` (thread:623-627) — so the tree did precede the
presentation; what changed is that the tree is no longer the *only*
presentation. The entry's own concession ("its substance … stands")
is what carries the bullet. (b) The thread promised that the
post-apply re-verification "will ship as a proper run file"
(thread:844); `981b2a6` adds no `runs/` file, and the entry's V9
bullet promises only "the next run record" (m0001:349-350). The §9.1
deviation is therefore still open at HEAD — this round's run record is
the first to close it.

**W11 · LOW — §15's framing does not fit one of the six it lists.**
doctrine:366-369 says the six defaults were "presented to the operator
in the thread but not ruled before authoring". The ratified-region
definition (bullet 2) did not exist at authoring; it was written in
this response, answering m0007. What the operator saw before saying
"apply" was "§6's body-only hash definition (whole file for the
doctrine, which has no frontmatter)" (thread:806, 848); what landed
also excludes `## Vetting` and `## Execution`. The landed text is the
better text and m0001's response entry describes it accurately — the
drift is between the apply plan and the apply, not between the entry
and the tree.

**Checks passed clean:**

- **Every V1-V9 disposition corresponds to real text.** No finding was
  answered by discussion alone; the nine bullets in the response entry
  each name an edit that exists at `981b2a6`. Nothing was silently
  dropped and nothing was disputed-without-saying-so.
- **The ledger was extended, not rewritten.** 27 rows at `7022aad`, 33
  at `981b2a6`; every original row survives, six are added, three are
  reworded exactly as the V2 bullet says, eleven carry †.
- **The affirmation is genuine and specific.** Ten of eleven bullets
  quote an operator turn; the eleventh (org/assertions) declares itself
  a derivation rather than a quote. It is not a bare attestation.
- **Append-only discipline held for the vetting record.** No round 1
  entry was edited; every response is a new `### Round 1 response`
  section under the existing round.
- **Derived views and links survive.** `tools/gen-index.py`
  regenerates `matters/index.md` byte-identically at `981b2a6`; all 58
  relative links resolve and none uses the leading-slash form (run
  record, steps 4-5).
- **The two beatcode-facing fixes are correct at the source.** m0004's
  quote is byte-identical to `SPEC.md:757-759`; m0003's "two of the
  ten" and its `SPEC.md:38` pointer are exact (run record, steps 1-3).
- **§12 conformance is undisturbed:** the response changed no
  frontmatter on any matter, which is also why the index diff is empty.

Not checked: PR #1 and the archived design session (unread, per
instruction) — so every † row's *content* remains unverifiable in-tree
by construction, exactly as round 1 said; the affirmation changes who
attests, not what can be checked. beatcode's render reproduction was
not re-executed this round; round 1's result stands unchallenged and
is not re-asserted.

- **Disposition:** round 1's findings were addressed, not merely
  discussed — all nine produced text, and the two fixes checkable
  against beatcode are exact. What remains is a residue at the edges of
  the fixes: one stale ratification pin (W1), one over-claimed
  provenance chain (W2), two sites V1 named or matched that were not
  edited (W3), and a handful of consistency leftovers. W1 is the only
  one that touches the ratification act itself and is worth settling
  before the operator reads; the rest are vetting-scale text edits and
  none blocks continued vetting.

### Round 2 addendum — 2026-08-25 — operator-directed

Two items, recorded because both deviate from the round's own terms.

- **W3 applied by the reviewer, on operator instruction ("proceed with
  fix").** The doctrine header now scopes its source claim to the
  thread *plus* the ledger's marked rows, and `README.md`'s status
  paragraph carries the same scoping the doctrine and m0001 already
  had. Deviation recorded: under the convention in
  [the thread](../threads/2026-08-24-audit-and-adjudication.md), a
  reviewer states findings and the author applies them; here the
  operator directed the reviewer to apply. Two sentences of prose, no
  normative change, and the round's other eleven findings are left as
  findings.
- **W2 disposition, at the operator's delegation.** Patching the
  ledger preamble is the wrong repair. The †/‡ apparatus, the
  carry-forward ruling, the witness affirmation, V1 and W2 all exist
  to substitute testimony for evidence the tree could simply contain:
  the archived first attempt's **design session** is not in `threads/`.
  Exporting it there — the archive is kept, not expunged (doctrine
  §14), and threads are the primary source for rulings (§9.2) —
  retires every one of them: each † row becomes checkable by any
  reviewer against a primary source in the tree, the affirmation stops
  being load-bearing, and the provenance sentences become true rather
  than scoped. The anchoring argument that kept the archive out
  (thread:495) was about re-*authoring*; authoring is finished, and
  reading is what remains. Recommended as a `spec` matter against §9.2
  rather than applied here.

### Round 2 addendum 2 — 2026-08-25 — operator-directed

W1 closed at the source, on operator instruction.

- **Doctrine §6 gains one rule:** "The pin follows the act, never
  precedes it." The commit and hash are recorded *after* the operator
  states ratification, from the commit the operator names; a pin
  computed in advance and offered as ready is never the ratification
  record, because the text moves under it the moment the matter is
  revised. This makes W1 structurally impossible rather than
  corrected: a pin derived from the operator's act cannot be stale
  before that act. It is a normative change to §6 and belongs in the
  operator's ratification read.
- **README gains "Ratifying, and checking a ratification":** the three
  commands that let the operator verify any quoted hash without
  trusting the agent that quoted it — recompute the hash at the
  recorded commit, hash the working file, diff the two. Placed in the
  README rather than the doctrine because it is operator procedure,
  not normative rule.
- **Deviation, recorded — third and last.** This is the third
  operator-directed edit applied by the round-2 reviewer (W3's two
  prose sites, then this). Applying findings is the author's move
  under the convention in
  [the thread](../threads/2026-08-24-audit-and-adjudication.md); a
  reviewer that keeps applying its own findings stops being a
  reviewer. The remaining round-2 findings — W2's archive-thread
  export, W4-W12 — are deliberately left unapplied for an author
  round, and the ratification read should treat this file's reviewer
  and the doctrine's author as no longer fully independent for §6 and
  the two prose sites named above.

### Round 2 response — 2026-08-25 — claude-code/2026-08-25 (author)

A fresh author instance, not the round 2 reviewer. Every finding W1–W11
is answered below; one is answered by disputing part of it, and the
rest are applied. Evidence for anything re-verified is in
[runs/2026-08-25-archive-thread-import.md](../runs/2026-08-25-archive-thread-import.md),
per §9.1.

**A numbering note, since the round's own cross-references disagree
with its ranked list.** The ranked findings are W1–W11. Three
back-references in the round's "Applied, verified" section point one
higher: under V5, "Framing nit: W12" is §15's framing, ranked W11;
under V2, "See W11 for the timing note's wording" is the
response-entry claim, ranked W10; under V3, "the exception noted in
W10(a)" is the Landed-column residue, ranked W9(a). The closing
deviation note's "W4-W12" is W4–W11. There is no W12. This response
follows the ranked list, which is the one carrying the findings' text.
(Cited by phrase, not by line: this response inserts text above the
round 2 entry, so every `m0001:NNN` in it — the round's own included —
now describes the file as it stood at `25d2e16`, not as it stands
here.)

#### W2 — applied, by export rather than by patching the preamble

The archived first attempt's **design session** is now in this tree, at
[`threads/2026-08-24-matter-system.md`](../threads/2026-08-24-matter-system.md),
copied verbatim from the archive branch `m0001-matter-system` at
`c11956d` — byte-identical, `50022f11…9816a` (run record, step 1). It
is a move, not a re-export: nobody re-derived it, nobody summarized it,
and the file that was reviewed as part of PR #1 is the file here.

What that retires, in order:

- **The † apparatus is gone from the ledger.** Every row's source is
  now a column, and the column cites the turn — thread and line. Where
  a reviewer previously had a marker meaning "you cannot check this,
  take the witness's word", there is a link to the operator's sentence.
- **The affirmation stops being load-bearing.** It remains in the
  adjudication thread as what it is — a witness attesting from memory
  of a source now on the shelf — and nothing in the tree rests on it.
- **The carry-forward ruling stops doing evidentiary work.** It is
  still the reason these rulings govern this collection; it is no
  longer the reason anyone should believe they exist.
- **The provenance sentences got simpler rather than more carefully
  scoped.** Doctrine's header, this matter's supersession note, and the
  README status paragraph now say the plain thing: no doctrine or
  matter text was reused, and the design session is here because the
  rulings in it govern this document. Round 1's V1 and the round 2
  addendum both had to scope those sentences to *text, not provenance*.
  That hedge is gone — the claim is simply true now.
- **W2's specific complaint is dissolved rather than patched.** Row 73
  (lenses/dry-rounds) had its only support inside a `## Vetting`
  append, outside the ratified region. It now cites
  [design:298](../threads/2026-08-24-matter-system.md) like every other
  row, inside the ratified region, checkable by anyone.

**Where I disagree with the finding, partially.** W2 calls the round 1
response's marking of row 73 "a new archive dependency introduced by
the fix for an archive-dependency finding". As a description of the
*evidence* available at `981b2a6`, that is exactly right. As a
description of the *marking*, it was not wrong: the operator did defer
the lenses machinery in that session, at design:298, and anyone can now
read them doing it — "this is a pain I as an operator have not felt yet
… i propose this should be filed as a feature matter". The round was
right that the tree could not support the claim, and right that this
was the wrong way to fix it. It was not right that the claim itself was
manufactured. The remedy stands either way, which is why this is
recorded rather than argued.

**On the addendum's recommendation to file this as a `spec` matter
against §9.2 instead of applying it.** The operator directed the
import; recording why the direction is coherent rather than an
exception to §1. m0001 is `proposed` and is being revised in its own
vetting rounds; adding a primary source it cites is a revision to what
this matter proposes, inside the bootstrap §14 licenses, not a change
to a ratified system. §9.2 needs no amendment either — it already says
`threads/` holds verbatim session exports and that threads are the
primary source for rulings; the archived design session was always the
kind of thing it describes, and was excluded by a review-prompt line,
not by doctrine. What the import *does* change is the text the operator
is being asked to ratify, and the ratification read should treat it
that way.

**The review prompt's isolation line is retired, in the README.** The
prompt recorded at
[thread:646-671](../threads/2026-08-24-audit-and-adjudication.md) tells
a fresh reviewer "The first attempt is archived unmerged (PR #1): do
not read it, its matters, or its thread." That line was written to stop
a reviewer anchoring on archived text while this bundle was being
*authored* — the same argument the adjudication session used to keep
the archive out (thread:495). Authoring is finished; what is left is
reading, and the line now subtracts from every round: V1 and W2 are
both reports of rows a reviewer was forbidden to check. It is retired,
with the reason, under "Running a vetting round" in the README, and
step 1's fidelity check now covers both threads. What survives is the
narrower rule it was standing in for: review the text as it stands
here, and never carry archived wording into this tree.

#### W1 — closed at the source before this round; nothing further

Doctrine §6's "the pin follows the act, never precedes it" and the
README's three verification commands close it structurally, as the
round 2 addendum 2 records. This response computes no pin, deliberately
(run record, "No ratification pin") — it changes §6, §7, §11 and §15,
so a pin computed here would be stale by exactly the mechanism W1
found.

#### W3 — (a) and (b) were applied by the reviewer; (c) is applied here

The risk-tiers deferral now has its own ledger row, citing
[design:304](../threads/2026-08-24-matter-system.md). That takes V4's
first branch — the ledger was incomplete — which the round 1 response
declined to take, and it makes the preamble's "Every operator proposal
and ruling" true of that ruling rather than nearly true. m0010's
pointer resolves to a real row and no longer routes through a retired
convention; detail in m0010's response entry.

**Two rows added beyond the findings, both consequences of reading the
imported session.** The ledger claims *every* proposal and ruling, and
with the source in the tree that claim is now checkable by anyone:

- **"describe, do not fix"** — [design:146](../threads/2026-08-24-matter-system.md)
  ("are you describing them to me or did you actually make these fixes?
  if not, stop, do not fix") and
  [design:287](../threads/2026-08-24-matter-system.md) ("which i propose
  we roll back, and persist as issues to be ratified"). This is the
  ruling the whole system exists to implement — it is this matter's
  Diagnosed reason and doctrine §1's "nothing lands that did not begin
  as a matter" — and it had no row.
- **the state spine** was carried as an unmarked row, i.e. attributed
  to the adjudication session. It was ruled in the design session, at
  [design:280](../threads/2026-08-24-matter-system.md) ("poorly worded,
  state should be proposed -> ratified -> staged -> executed"). The
  Ruled in column now says so.

#### W4 — applied on m0010

The §11 amendment leaves the `feature` matter, as m0007's equivalent
finding was resolved: a separate `spec` matter, filed and vetted
alongside m0010 and named in its `depends_on` before either is
ratified. Why it is not filed today is on m0010.

#### W5 — applied on m0008

"supersession/amendment link" → "supersession link". §5 stopped
defining amendment in the round 1 response; m0008 was the last carrier.

#### W6 — applied, in the doctrine rather than in m0008

The rule V6(g) produced was normative text living in a tooling matter,
which inverts §10. Doctrine §7 now states the transition-time gate — a
matter cannot be staged or executed while a dependency is unexecuted —
and exempts the §11 retroactive path, which reaches `executed` without
ever being `staged` and would otherwise have been blocked by the
validator on the one path designed to bypass gates; a retroactive
matter names its unexecuted dependencies in `## Retroactive` instead.
§11 carries the pointer, and m0008's bullet now cites §7 rather than
legislating.

#### W7 — applied, in §6

For a matter entering `executed` by the retroactive path, the hashed
region additionally covers `## Retroactive` and `## Execution` as they
stand at the acknowledged commit — because on that path the
acknowledgment *is* the ratifying act and what is acknowledged is what
landed. Nothing leaves `executed` (§3), so those sections do not move
afterwards. m0007 gains the requirement that the check name which of
the three regimes it verified; see its response entry.

#### W8 — applied on m0011, including the record the round found missing

`1347af3` rewrote the thread header in answer to a vetting finding and
no response entry said so. It is recorded now. The sentence it produced
was false at HEAD, as the round says, and has been rewritten to a form
that survives an append: the export "is brought current as exchanges
land: it ends wherever the last export run reached, and the reply to
the final human turn shown may already exist outside the file." The
edit is three lines replacing three, verified length-neutral (run
record, step 5) — every `thread:NNN` citation in this file's vetting
record points into that file, and a header that changed length would
have silently moved all of them. m0011's Open now carries the general
question: what a header may assert between landings.

#### W9 — (a) and (b) applied; (c) is moot

(a) The housekeeping row's Landed column now names its in-tree traces —
the archive branch `m0001-matter-system` and doctrine §14 — rather than
resting on "executed at build" alone. It is also no longer unreachable
to a reviewer: PR #1 is readable from this round on. (b) The
proposals-become-matters row's three IDs are relative links like every
other matter reference. (c) The blanket "were ruled in the archived
first attempt's design session" sentence is gone with the † apparatus;
the org/assertions row states its own derivation, and the Scope section
now walks it turn by turn — proposed as a matter at design:318,
narrowed by the operator at design:457 once they identified the file as
their user-level global CLAUDE.md, and so excluded by their own
"concerns across repos are not mixed" at design:450. That derivation
was the least checkable thing in the ledger and is now the most.

#### W10 — (a) accepted and corrected here; (b) closed by the run file

(a) The round 1 response's timing note said the export update "now
shows the §6 mechanism being presented to the operator, so V2's 'first
presentation' clause is historical". The round is right that this is
looser than the record: `1347af3` appended the build-report turn, which
announces the bundle as already built and pushed at `44d6be0`
([thread:623-627](../threads/2026-08-24-audit-and-adjudication.md)), so
the tree did precede the presentation. The accurate statement is the
narrower one: the tree is no longer the only presentation, and V2's
substance — no operator ruling — is untouched, which is what §15 flags.
Stated here rather than fixed there, because a vetting entry is never
edited. (b) The run file promised in-thread at thread:844 exists now.

#### W11 — applied, in §15

§15 no longer says all six defaults were presented before authoring.
Five were; the ratified-region definition was written in the round 1
response answering m0007, and what the operator saw before "apply" was
the narrower "body-only hash" form, while what landed also excludes
`## Vetting` and `## Execution`. The ratification read should see that
difference rather than infer it.

#### One invariant re-scoped, not repaired

Rounds 1 and 2 both checked "every relative link in the tree resolves,
none uses the leading-slash form" over every `.md` file. That was sound
while every `.md` was authored. The imported transcript contains one
link-shaped string, at
[design:475](../threads/2026-08-24-matter-system.md): a table cell
where the agent quotes OKF's bundle-absolute link form to the operator,
target `/matters/m0001-….md`, ellipsis included. It is verbatim primary
source and must not be fixed — and it is leading-slash, so it fails the
check twice over. From here the check has a stated scope: authored
files, of which every relative link resolves and none is leading-slash;
`threads/` is evidence, not link graph (run record, step 7).

#### Independence, still degraded, and by one more step

Round 2's addendum 2 recorded that its reviewer applied three of its own
findings at the operator's direction, and asked the ratification read to
treat that reviewer and the doctrine's author as no longer fully
independent for §6 and two prose sites. That stands. This response adds
a second degradation of a different kind: the ledger's new rows and the
Scope rewrite come from *this author* reading the imported session, not
from a reviewer. They are the most checkable claims in the file — every
one is a line citation — but they have not been reviewed by anyone.
Round 3's fidelity check should start there, and it can, which is the
whole point of the import.
