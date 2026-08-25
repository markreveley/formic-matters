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
