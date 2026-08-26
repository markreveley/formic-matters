---
type: spec
title: The matter system
description: "Every change to a governed system — and to the framework itself — is proposed, vetted, and ratified as a matter before it is made."
id: m0001
state: executed
status: stable
tags: [formic-matters, doctrine, bootstrap]
threads:
  - threads/2026-08-24-matter-system.md
  - threads/2026-08-24-audit-and-adjudication.md
  - threads/2026-08-25-doctrine-operator-review.md
generated:
  by: claude-code/2026-08-24
  at: 2026-08-24T22:33:00Z
verified:
  - by: human:mark
    at: 2026-08-26T05:21:39Z
ratified_commit: 85fe4511326a30516ed2bf86a2e2a2b9d05c3d25
ratified_sha256: 5adc0aafe92c5ead0269c681c8802516572765cf77b22549ea5acc45d8dda7bd
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
attempt is referenced, not superseded: nothing in it was ratified, so
nothing carried a ratification into this collection, and it was
re-authored rather than derived. It was re-authored by an agent that had
read it, though, and passages of its text survive here, measured file by
file in
[runs/2026-08-25-vetting-round-3.md](../runs/2026-08-25-vetting-round-3.md).
Its design session is exported into
[`threads/`](../threads/2026-08-24-matter-system.md) as a primary
source, so the rulings it carries are read here rather than attested to.

## Rulings ledger

Every operator proposal and ruling from the 2026-08-24 sessions and
the 2026-08-25 in-document review, and where it landed. This table is
what the fidelity review checks the doctrine against, alongside the
threads themselves.

All three sources are in this tree: the
[design session](../threads/2026-08-24-matter-system.md), the
[adjudication session](../threads/2026-08-24-audit-and-adjudication.md),
and the
[operator review](../threads/2026-08-25-doctrine-operator-review.md).
**Ruled in** cites the turn, so every row is checkable here. Review
turns are cited by label rather than line — `review cNN` for the
in-document comments, `review aN` for the answers to the prompted
questions, `review i1` for the naming interjection, `review rN` for
the 2026-08-26 response-review points — because that export is brought
current as exchanges land and labels survive appends.
Two review rulings are deliberately not rows: the answers on turn scope
(a3) and push target (a4) are session mechanics that land no text; they
are recorded in the thread and in the operator-review response below.
Clauses marked **‡** are authoring-agent mechanisms adopted to satisfy
a ruling, not rulings; doctrine §15 lists them for confirmation at
ratification.

| Operator proposal / ruling | Landed | Ruled in |
|---|---|---|
| describe, do not fix: nothing lands on sight, and work already applied is rolled back and filed as matters to be ratified | doctrine §1, and this matter's Diagnosed reason | [design:146](../threads/2026-08-24-matter-system.md), [design:287](../threads/2026-08-24-matter-system.md) |
| three change kinds as matter types; "proposal" not a type; types moved up one level | doctrine §2 | [design:280-284](../threads/2026-08-24-matter-system.md) |
| per-type required content (fix: diagnosis + fix; feature: spec + plan; refactor: reason + plan) | doctrine §2 | [design:169-171](../threads/2026-08-24-matter-system.md) |
| state spine `proposed → ratified → staged → executed` | doctrine §3 | [design:280](../threads/2026-08-24-matter-system.md) |
| vetting by fresh agent reviews until the operator ratifies | doctrine §6 | [design:173](../threads/2026-08-24-matter-system.md) |
| execution by a dev agent launched by the operator; orchestration later, as its own matter | doctrine §3 | [design:173](../threads/2026-08-24-matter-system.md), [adjudication:290](../threads/2026-08-24-audit-and-adjudication.md) |
| cheap to file, expensive to ratify; diagnosis may arrive over several turns but precedes ratification | doctrine §4 | [design:287](../threads/2026-08-24-matter-system.md) |
| split functions as supersession routing to offshoots | doctrine §5 | [design:307](../threads/2026-08-24-matter-system.md) |
| flat collection, metadata-sortable, all views derived | doctrine §1, §7, §12 | [design:175](../threads/2026-08-24-matter-system.md) |
| deterministic code wherever possible | doctrine §10 | [design:177](../threads/2026-08-24-matter-system.md) |
| lenses/dry-round review machinery deferred as premature, filed as a matter | [m0006](m0006-review-lenses-and-dry-rounds.md) | [design:298](../threads/2026-08-24-matter-system.md) |
| ratification content hash deferred unless MVP-required; record now, tooling later | doctrine §6 + [m0007](m0007-ratification-content-hash.md) | [design:301](../threads/2026-08-24-matter-system.md), [design:449](../threads/2026-08-24-matter-system.md) |
| risk tiers deferred on the same reasoning — "same thoughts as 4" | [m0010](m0010-risk-tiers.md) | [design:304](../threads/2026-08-24-matter-system.md) |
| "matter system operational" as a derived worklist view | doctrine §7 | [design:301](../threads/2026-08-24-matter-system.md), [design:449](../threads/2026-08-24-matter-system.md) |
| SPEC-GAPS broken out into matters, landed and otherwise; `spec` as a real type | [m0009](https://github.com/markreveley/formic-matters/blob/70db408d9148667097b2cd052853d37d01e9f3fa/matters/m0009-spec-gaps-to-matters.md) (moved to the consumer by m0012; pinned pre-move), doctrine §2 | [design:316](../threads/2026-08-24-matter-system.md), [design:456](../threads/2026-08-24-matter-system.md) |
| PRs cite matter IDs | doctrine §8 (commit trailer, branch/PR title prefix) | [design:317](../threads/2026-08-24-matter-system.md) |
| process/system code kept separate from the instrument | [m0008](m0008-matter-tooling.md) | [design:310](../threads/2026-08-24-matter-system.md), [design:450](../threads/2026-08-24-matter-system.md) |
| consider OKF; keep the useful shape, no memory files in the repo; "agree on okf direction", with the conformity-cost scepticism that keeps it a dialect | doctrine §12 (documented dialect) | [design:453](../threads/2026-08-24-matter-system.md), [design:486](../threads/2026-08-24-matter-system.md), [adjudication:310](../threads/2026-08-24-audit-and-adjudication.md), [adjudication:394](../threads/2026-08-24-audit-and-adjudication.md), [adjudication:473](../threads/2026-08-24-audit-and-adjudication.md) |
| org/assertions raised as a matter ([design:318](../threads/2026-08-24-matter-system.md)); the operator asked whether the file was their user-level global CLAUDE.md rather than a repo one ([design:457](../threads/2026-08-24-matter-system.md)); the identification and the out-of-scope derivation are the agent's, in the following turn, never answered by the operator | noted under Scope below, where the derivation is owned | [design:318](../threads/2026-08-24-matter-system.md), [design:457](../threads/2026-08-24-matter-system.md), [design:467](../threads/2026-08-24-matter-system.md), [design:450](../threads/2026-08-24-matter-system.md) |
| thread persistence: verbatim human and agent turns, reasoning and tool traffic dropped, redact before publication | doctrine §9.2 + [m0011](m0011-thread-persistence.md) | [design:567](../threads/2026-08-24-matter-system.md), [design:660](../threads/2026-08-24-matter-system.md), [adjudication:264](../threads/2026-08-24-audit-and-adjudication.md) |
| runs directory documenting verification runs with environment specs | doctrine §9.1 | [adjudication:260](../threads/2026-08-24-audit-and-adjudication.md) |
| claims-DAG in the matter itself, visualization derived, nodes are not matters | doctrine §9.3 | [adjudication:270](../threads/2026-08-24-audit-and-adjudication.md) |
| retire PR comments; keep GitHub and PRs as transport and merge mechanics; operator responds by local file edits | doctrine §8 | [adjudication:471](../threads/2026-08-24-audit-and-adjudication.md), [adjudication:553](../threads/2026-08-24-audit-and-adjudication.md) |
| one repo, self-hosting explicit, no framework split; extraction tripwire's specific conditions are ‡ | doctrine §1, §13 | [adjudication:479](../threads/2026-08-24-audit-and-adjudication.md), [adjudication:555](../threads/2026-08-24-audit-and-adjudication.md) |
| archive the first attempt, do not expunge; fresh authoring, nothing textual carried | doctrine §14, this matter | [adjudication:551](../threads/2026-08-24-audit-and-adjudication.md) |
| landed/execution record required to enter `executed` | doctrine §3.1 | [adjudication:565](../threads/2026-08-24-audit-and-adjudication.md), [adjudication:601](../threads/2026-08-24-audit-and-adjudication.md) |
| git citation convention (trailer + prefixes) | doctrine §8 | [adjudication:568](../threads/2026-08-24-audit-and-adjudication.md), [adjudication:601](../threads/2026-08-24-audit-and-adjudication.md) |
| threads primary reference; adjudication thread exported into this tree; derived-views-over-threads formalization is ‡. Q3's premise that the design conversation stays archive-side was later reversed by the round 2 response's import — recorded there, on m0011, and in round 3's X2 | doctrine §9.2, [threads/2026-08-24-audit-and-adjudication.md](../threads/2026-08-24-audit-and-adjudication.md) | [adjudication:467](../threads/2026-08-24-audit-and-adjudication.md), [adjudication:557](../threads/2026-08-24-audit-and-adjudication.md), [adjudication:571](../threads/2026-08-24-audit-and-adjudication.md), [adjudication:601](../threads/2026-08-24-audit-and-adjudication.md) |
| ratification gate over the exact text; operator prefers not to compute hashes locally; the recording mechanism (agent computes and records) is ‡ | doctrine §6 | [adjudication:284](../threads/2026-08-24-audit-and-adjudication.md), [adjudication:602](../threads/2026-08-24-audit-and-adjudication.md) |
| vetting rounds recorded on the matter as appended entries | doctrine §6 | [adjudication:467](../threads/2026-08-24-audit-and-adjudication.md), [adjudication:578](../threads/2026-08-24-audit-and-adjudication.md), [adjudication:601](../threads/2026-08-24-audit-and-adjudication.md) |
| matters assert immutable references; no undated mutable-state claims | doctrine §9.4 | [adjudication:477](../threads/2026-08-24-audit-and-adjudication.md) |
| one-line provenance pointer to the archive | doctrine header + §14 | [adjudication:575](../threads/2026-08-24-audit-and-adjudication.md), [adjudication:601](../threads/2026-08-24-audit-and-adjudication.md) |
| housekeeping: PR #1 closed unmerged, archive branch kept, planning drafts absorbed, directory names | executed at build; the archive branch `m0001-matter-system` and doctrine §14 are its in-tree traces | [adjudication:590](../threads/2026-08-24-audit-and-adjudication.md), [adjudication:604](../threads/2026-08-24-audit-and-adjudication.md) |
| unprocessed operator proposals become matters | [m0006](m0006-review-lenses-and-dry-rounds.md), [m0010](m0010-risk-tiers.md), [m0011](m0011-thread-persistence.md) | [adjudication:605](../threads/2026-08-24-audit-and-adjudication.md) |
| relative links | doctrine §12 | [adjudication:481](../threads/2026-08-24-audit-and-adjudication.md) |
| authorize the bootstrap: "agree to draft and execute m0001", answering the agent's make-m0001-the-exception proposal | doctrine §14, and §3's m0001-only `ratified → executed` exception | [design:437-443](../threads/2026-08-24-matter-system.md), [design:459](../threads/2026-08-24-matter-system.md) |
| "do not persist un-ratified 'facts' to repo, just what we discuss" | doctrine §15's existence — the confirm-at-ratification apparatus for unruled choices | [design:486](../threads/2026-08-24-matter-system.md) |
| the process is a consumable framework from init; the abstraction is ratified now; this document becomes strictly the framework's formal spec | this document as a whole; doctrine §13 | [review c02](../threads/2026-08-25-doctrine-operator-review.md), [review c14](../threads/2026-08-25-doctrine-operator-review.md) |
| the framework is named **Formic Matters** ("Formic Ascent" in the review comment, corrected in the same exchange) | title, throughout | [review c02](../threads/2026-08-25-doctrine-operator-review.md), [review i1](../threads/2026-08-25-doctrine-operator-review.md) |
| the extraction tripwire fired — five repositories can adopt | doctrine §13 | [review c15](../threads/2026-08-25-doctrine-operator-review.md) |
| the split: this repository renamed to the framework; a new beatcode-dev created as its first strict consumer, carrying the beatcode-facing matters; the framework keeps and self-hosts its own | doctrine §13, [m0012](m0012-formic-matters-split.md) | [review c02](../threads/2026-08-25-doctrine-operator-review.md), [review a1](../threads/2026-08-25-doctrine-operator-review.md) |
| remove `target` from the spec — the target is whatever repository installs the framework; governed systems named as tags | doctrine §1, §12; every matter's frontmatter conformed | [review c03](../threads/2026-08-25-doctrine-operator-review.md), [review c13](../threads/2026-08-25-doctrine-operator-review.md), [review c16](../threads/2026-08-25-doctrine-operator-review.md) |
| the matter, not the proposal, is the unit of work | doctrine §1 | [review c06](../threads/2026-08-25-doctrine-operator-review.md) |
| the bootstrap exception generalized to installations | doctrine §1, §14 | [review c05](../threads/2026-08-25-doctrine-operator-review.md), [review a2](../threads/2026-08-25-doctrine-operator-review.md) |
| in-document operator↔agent comment exchanges must be accounted for; commit-pointer and duplicate-at-state offered as options | doctrine §8, §9.2; [the exchange's own thread](../threads/2026-08-25-doctrine-operator-review.md) is the first exercise | [review c12](../threads/2026-08-25-doctrine-operator-review.md) |
| §15's presented-before-authoring choices: "others are ratified" | doctrine §15, first group | [review c17](../threads/2026-08-25-doctrine-operator-review.md) |
| plainspeak breakdowns, with implications, required on the later-written choices and the R1 item before ruling | the operator-review response below | [review c18](../threads/2026-08-25-doctrine-operator-review.md), [review c19](../threads/2026-08-25-doctrine-operator-review.md) |
| the operator's channel is file edits **or** a session exchange exported as a thread; §8 and §9.2 read as confusingly separated — consolidate | doctrine §8, §9.2 | [review r1](../threads/2026-08-25-doctrine-operator-review.md) |
| historical narration does not belong in the specification — git history and the matters carry it | doctrine §13 slimmed; §1's interim clause trimmed under the same principle | [review r2](../threads/2026-08-25-doctrine-operator-review.md) |
| state the bootstrap plainly, not abstractly | doctrine §14 | [review r3](../threads/2026-08-25-doctrine-operator-review.md) |
| the adopted-by-default record moves out of the specification, persisted as a matter (meta-matter chosen of the two offered homes) | doctrine §15 slimmed; [m0013](m0013-bootstrap-defaults-record.md) | [review r4](../threads/2026-08-25-doctrine-operator-review.md) |
| the specification ratified in principle, four areas outstanding; the formal §6 act follows over the revised text at a named commit | this revision | [review r5](../threads/2026-08-25-doctrine-operator-review.md) |
| the response record and the breakdown items (§15's groups B and D) confirmed on reading | [m0013](m0013-bootstrap-defaults-record.md)'s confirmation trail | [review r6](../threads/2026-08-25-doctrine-operator-review.md) |
| a consumer matter cannot depend on a framework matter, or any external matter — may change, ruled for simplicity now | doctrine §7; [m0012](m0012-formic-matters-split.md) | [review r7b](../threads/2026-08-25-doctrine-operator-review.md) |
| the exchange record must carry the text each comment responds to, or it cannot be audited | the thread's in-situ excerpt format | [review r8](../threads/2026-08-25-doctrine-operator-review.md) |
| the six round-2 checks ratified, one per checklist item — changed spec sections, the §1 extension, the rebuilt thread, m0013, m0012's mechanism, the ledger rows | the texts approved are those formally ratified below | [review k](../threads/2026-08-25-doctrine-operator-review.md) |
| formal ratification: "I ratify m0001, m0012, and m0013 at commit 85fe451" | the `verified`/`ratified_commit`/`ratified_sha256` records on all three matters; m0001 executed per §14 | [review f1](../threads/2026-08-25-doctrine-operator-review.md) |
| basis stated for the record: everything read was read from links in this thread; no continuous pass, per the operator's earlier statement of comfort with the accumulated review | recorded with the act, in the ratification entry below | [review f2](../threads/2026-08-25-doctrine-operator-review.md) |

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
derived rather than stated, and the derivation is readable end to end —
and owned: proposed as a matter
([design:318](../threads/2026-08-24-matter-system.md)); the operator
*asked* whether the file was their user-level global CLAUDE.md rather
than a repo one
([design:457](../threads/2026-08-24-matter-system.md)); the
identification, and the whole out-of-scope derivation — cross-repo by
definition, so excluded by the operator's own "concerns across repos
are not mixed"
([design:450](../threads/2026-08-24-matter-system.md)) — are the
agent's, stated in the next turn
([design:467](../threads/2026-08-24-matter-system.md)) and never
answered by the operator. The disposition is the agent's, unanswered,
standing because never contradicted; ratifying this matter confirms
it.

## Execution

The tree was written together with this matter (doctrine §14) and has
grown with its vetting. Everything in it is claimed here: the
specification, matters m0001–m0013, the derived index, the interim
index generator, the repository README, the three thread exports in
`threads/` (the design session imported verbatim from the archive
branch in round 2's response, the adjudication session exported by its
participating agent, and the operator-review exchange transcribed by
its responding agent), and every record in `runs/`. Nothing else is in
the tree.

**Completed 2026-08-26.** Ratified by the operator at
`85fe4511326a30516ed2bf86a2e2a2b9d05c3d25` and executed in the same
act, per §14's one licensed `ratified → executed` jump — for a
bootstrap `spec` matter the proposed text is the deliverable, and it
was already in the tree at the ratified commit, so execution lands
nothing further. What landed, in full: the lineage from the bootstrap
build `44d6be0` through `85fe451` on the m0001 branch (thirteen
work commits, each carrying its `Matter:` trailer; PR #2 is the diff
boundary against `main`), containing the specification, m0001–m0013,
three thread exports, five run records, the derived index, the interim
generator, and the README. Deviations from the ratified plan: none —
the ratified text and the landed text are the same bytes by
construction, verifiable from the pin above. Recording actor:
claude-code/2026-08-26, in
[runs/2026-08-26-ratification-recording.md](../runs/2026-08-26-ratification-recording.md).

## Vetting

### Round 1 — 2026-08-25

- **Reviewer:** claude-code/2026-08-25, fresh instance. Inputs: this
  branch's tree at `44d6be0` and `markreveley/beatcode` (`fa17627`, seed
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
  `markreveley/beatcode` at `fa17627` (seed `91188a5`); the archived first
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

### Round 3 — 2026-08-25

- **Reviewer:** claude-code/2026-08-25, fresh instance — neither the
  round 2 reviewer nor the round 2 response's author. Inputs: this
  branch at `7357244`, the diff `25d2e16..7357244`, both threads, and —
  for the first time in this collection's review history — the archived
  first attempt: PR #1, the branch `m0001-matter-system` at `c11956d`,
  and its matters. `markreveley/beatcode` was not cloned; nothing in the diff
  bears on m0002–m0005 beyond two response entries that apply nothing,
  so rounds 1 and 2 own those verdicts and none is re-asserted here.
- **Scope:** the four checks the round 2 response makes possible or
  newly needs — fidelity of the rulings ledger against *both* threads
  row by row; whether W1–W11 were addressed or only discussed, and what
  the response newly broke; the doctrine text this response wrote,
  which nobody has reviewed; and the standing consistency and scope
  invariants. Evidence is in
  [runs/2026-08-25-vetting-round-3.md](../runs/2026-08-25-vetting-round-3.md),
  per §9.1.

**Findings, ranked by severity:**

**X1 · HIGH — "none of its doctrine or matter text was reused" is
false, and this response deleted the hedge that had been protecting
it.** The claim stands in the ratified region of three files:
doctrine:18-19, `README.md`:21-22, m0001:43-45. Its ancestor is the
build agent's undertaking at
[adjudication:499](../threads/2026-08-24-audit-and-adjudication.md) —
"Nothing textual carries. No doctrine text, no matter texts."
Measured against `c11956d` (run record, step 5): 45% of the archived
doctrine, 55% of the archived README, 43% of archived m0008, and
**77–78% of archived m0006 and m0010** survive into this tree in
matching runs of forty characters or more. The longest runs are not
convergence on facts, table scaffolding, or the operator's own wording
— they are authorial prose reproduced intact:

- 315 ch, m0006:21-25 ↔ archive m0006:16-20 — "…round three restates
  round one, producing the appearance of scrutiny rather than
  scrutiny."
- 220 ch, m0010:49-52 ↔ archive m0010:36-39 — "A process that makes
  small changes expensive gets bypassed for small changes, and a
  bypassed process ends up covering only the work that was already
  being done carefully."
- 205 ch, m0001:20-25 ↔ archive m0001:19-24 — this matter's own
  Diagnosed reason opening.
- 173 ch, m0008:51-52 ↔ archive m0008:33 — "Not mechanizable, and not
  to be faked: whether a diagnosis is correct, whether a plan is good,
  whether scope is right, ratification itself."
- 168 ch, `README.md`:1-5 ↔ archive README:1-5 — the repository's
  opening sentence.
- 255 ch, doctrine:57-59 ↔ archive doctrine:31-33; 264 ch,
  doctrine:46-53 ↔ archive doctrine:20-25; 160 ch, doctrine:131-134 ↔
  archive doctrine:66-68.

Two things make this worse than a stale sentence. First, **it is the
one claim the isolation line made uncheckable**, and this response
retired that line (`README.md`:42-63) while leaving the claim
unchecked — the round that gained the ability to test it is the round
that should have tested it, and this is that round. Second, the
response **strengthened** the claim rather than testing it: m0001:702-708
records that the provenance sentences "got simpler rather than more
carefully scoped … That hedge is gone — the claim is simply true now."
Round 1's V1 and the round 2 addendum had both scoped these sentences
to *text, not provenance*; the scoping was removed on the theory that
the import made the plain claim true. The import made it checkable, and
it is false. Note also that fresh authoring was chosen at
[adjudication:495](../threads/2026-08-24-audit-and-adjudication.md)
specifically to defeat **anchoring** — "the new author copy-editing the
old text's framing instead of thinking" — so the reused runs are
evidence about the method, not only about a sentence. The remedy is the
operator's to choose and larger than a word: either the sentences are
rewritten to what is true (no *ratified* text carried; the collection
was re-authored by an agent that had read the archive, and passages
survive), or the passages are rewritten. Recorded matter-locally on
m0006 and m0010, the two worst.

**X2 · MEDIUM-HIGH — the import reverses a ruling that is in the tree,
and the operator directions authorizing this round's three biggest
moves have no primary source.** (a)
[adjudication:571](../threads/2026-08-24-audit-and-adjudication.md), Q3,
states as a premise of both its options: "The original design
conversation stays archive-side either way." The operator ruled it
"1-5 yes" at
[adjudication:601](../threads/2026-08-24-audit-and-adjudication.md), and
row 92 of this ledger cites Q3 as landed doctrine. The design session is
now in `threads/`. That may well be the right call — the response
argues it cogently at m0001:728-740 — but the argument never mentions
that a ruled premise was reversed, no ledger row records the reversal,
and §9.4 has this collection asserting immutable references while its
own record now contradicts one. (b) Three operator directions are
asserted with no citation into either thread, which ends at "apply"
([adjudication:854](../threads/2026-08-24-audit-and-adjudication.md)):
`"proceed with fix"` (m0001:603), the addendum-2 instruction
(m0001:630), and "The operator directed the import" (m0001:729,
repeated at m0011:74-75). Under §8 the operator's channel is committed
file edits and "agents read rulings from the tree"; under §9.2 threads
are the primary source for rulings. In the commit whose entire thesis
is that a citation beats a witness — m0001:692-695, "Where a reviewer
previously had a marker meaning 'you cannot check this, take the
witness's word', there is a link to the operator's sentence" — the
import itself rests on the witness's word. Recorded matter-locally on
m0011.

**X3 · MEDIUM — §15's "Six choices … are the authoring agent's" is a
completeness claim, and the same commit falsified it.** doctrine:391-400.
W11's fix changed a loose statement ("Six choices … were adopted by the
authoring agent as defaults — presented to the operator in the thread
but not ruled before authoring") into an assertive one ("Six choices in
this document and the collection are the authoring agent's, adopted
without an operator ruling"), then added the machinery for admitting
late additions: bullet 2 is listed precisely because it "was written
later, in the round 1 response, answering a finding on m0007." By that
standard the list is short by at least six:

- **doctrine:200-206**, §7's transition-time `depends_on` gate and its
  §11 exemption — written in *this* response, answering W6, no operator
  ruling;
- **doctrine:177-182**, §6's hashed region for the retroactive path —
  written in *this* response, answering W7, no operator ruling;
- **doctrine:285-299**, §11's retroactive path design — the agent's, at
  [adjudication:445](../threads/2026-08-24-audit-and-adjudication.md),
  offered under the operator's "suggest matter corrections"
  ([adjudication:304](../threads/2026-08-24-audit-and-adjudication.md))
  and never agreed to; the archived attempt's own agent listed the
  retroactive path as explicitly *unruled*
  ([design:509](../threads/2026-08-24-matter-system.md));
- **doctrine:143-150**, §5's earlier-ratification precedence, and
  **doctrine:99-108**, §3's terminal owners — same origin, written in
  the round 1 response answering V6;
- **doctrine:134**, §4's "Completeness is therefore a checklist on the
  matter, not a state" — the operator was asked to rule on exactly this
  (R1,
  [adjudication:380](../threads/2026-08-24-audit-and-adjudication.md))
  and **declined**: "do i even need to pick?"
  ([adjudication:463](../threads/2026-08-24-audit-and-adjudication.md)),
  "same with ruling needed"
  ([adjudication:465](../threads/2026-08-24-audit-and-adjudication.md)),
  with the agent answering that R1's substance "gets settled by whatever
  state machine the fresh author proposes and you ratify as a whole
  document"
  ([adjudication:506](../threads/2026-08-24-audit-and-adjudication.md)).
  That is the clearest confirm-at-ratification item in the collection
  and it is not on the list.

The point of §15 is that ratifying confirms these deliberately rather
than silently. A list that names six while the doctrine holds at least
twelve does the opposite of what the section is for.

**X4 · MEDIUM — the ledger's one derived row, and the Scope section
rewritten around it this round, present the agent's reasoning as the
operator's.** Row 83 (m0001:83) says org/assertions was "raised as a
matter, then withdrawn once identified as the operator's global
CLAUDE.md". The operator did not withdraw it and did not identify it:
at [design:457](../threads/2026-08-24-matter-system.md) they *ask* —
"regarding the claude.md, i misunderstood and thought this was the repo
claude.md - this is my local global claude.md?" Under §3, `withdrawn`
means "retracted by its author before a decision"; that did not happen.
The identification, and the whole out-of-scope derivation, are the
agent's, in the very next turn
([design:467](../threads/2026-08-24-matter-system.md)): "So the
`org/assertions` question is cross-repo by definition, which — per your
own 'don't mix concerns across repos' — drops off the beatcode-scoped
worklist rather than becoming m-something here." The operator never
answers it. The Scope section (m0001:111-122), rewritten this round on
the author's own initiative and reviewed by nobody, reconstructs that
derivation out of design:318, design:457 and design:450 and calls it
"readable end to end" and "now the most [checkable]" — while omitting
design:467, the single turn that actually contains it and the one that
shows whose it is. W9(c) is not moot; the blanket sentence went and the
misattribution moved into prose. Fix is small and honest: cite
design:467 and say the disposition is the agent's, unanswered.

**X5 · MEDIUM — six operator rulings and proposals are missing from a
ledger that says "Every".** m0001:51. Verified by extracting every
`## ▸ Mark` turn from both threads and reading it against the table (run
record, step 4):

- **[design:459](../threads/2026-08-24-matter-system.md)**, "agree to
  draft and execute m0001" — the operator's authorization for the
  bootstrap, answering the agent's bootstrap-exception proposal at
  [design:437-443](../threads/2026-08-24-matter-system.md) ("make
  `m0001` the exception on purpose … That exception should be recorded
  *in* `m0001`"). §14 is one of the two exceptions §1 names, §3 licenses
  m0001 alone to jump `ratified → executed` on it, and the ruling that
  grants it has no row. Row 89's §14 landing covers the archive half
  only.
- **[adjudication:473](../threads/2026-08-24-audit-and-adjudication.md)**,
  "agree on okf direction" — the ruling that actually adopted OKF,
  answering the agent's "keep it, as a documented dialect, not a
  certification"
  ([adjudication:394](../threads/2026-08-24-audit-and-adjudication.md)),
  which is where §12's framing and its "when OKF fights a real need the
  doctrine wins" rule come from. So does the operator's scepticism at
  [adjudication:310](../threads/2026-08-24-audit-and-adjudication.md)
  ("this to me makes okf suspect … unless the conformity brings enough
  wins to offset the adoption"), which is why the dialect is hedged at
  all. Row 82 cites neither — only design:453 ("should consider google's
  okf format") and design:486.
- **[design:486](../threads/2026-08-24-matter-system.md)**'s second
  clause — "do not persist un-ratified 'facts' to repo, just what we
  discuss". The turn is cited on row 82 but the row states only the
  memory-files half. This is the direct ancestor of §15's whole
  existence — the archived agent read it that way in terms
  ([design:509](../threads/2026-08-24-matter-system.md), "That's my read
  of 'do not persist un-ratified facts'") — and it has no row and no
  named landing.
- **[design:449](../threads/2026-08-24-matter-system.md)**, "4/5 -
  agree", is cited on row 76 but not on row 78, though it is the turn
  that settles the superset question the operator raised at design:301
  and thereby licenses §7's "no containers" and the
  `implements`/`depends_on` pair
  ([design:381-390](../threads/2026-08-24-matter-system.md)). Row 78
  cites the question and not the answer.
- **Row 92** cites the agent's Q3 at adjudication:571 with no
  answering turn, where sibling rows 90, 91 and 96 all cite
  adjudication:601.
- **[adjudication:290](../threads/2026-08-24-audit-and-adjudication.md)**,
  "operator will trigger execution by launching a dev agent. propose
  the matter that will enable this" — row 70 cites design:173 only.
  Minor, same content; noted for completeness because the row's second
  clause ("as its own matter") appears in neither cited turn.

**X6 · MEDIUM — m0007's Feature section now contradicts the doctrine
the same commit wrote, and the correction sits outside the ratified
region.** m0007:39 states "§6 defines two" hash regimes. §6 now defines
three: the ratified region, the whole-file regime, and — added by this
same commit at doctrine:177-182 — the retroactive regime. m0007's own
response entry says so explicitly (m0007:131-137, "That is a third
regime this matter's check must distinguish"), but that is a `## Vetting`
append, which under §6:169-170 is outside the ratified region. So the
text the operator would ratify says two and the text they would not
ratify says three. This is precisely the shape W2 identified — evidence
for a ratified claim parked in an append — recurring in the commit that
retired it. Recorded matter-locally on m0007.

**X7 · LOW-MEDIUM — §7's new gate has no exit and no marker.**
(a) doctrine:200-201 blocks staging and execution "while a dependency is
unexecuted". A dependency that ends `rejected`, `withdrawn` or
`superseded` can never become `executed` — §5 keeps superseded matters
forever — so every dependent is permanently blocked, and neither §5 nor
§7 provides a re-pointing or release rule. This is live today:
m0006, m0007, m0009 and m0010 all `depends_on: [m0008]`.
(b) doctrine:201-206 exempts "the retroactive path", which is
identifiable only by the presence of a `## Retroactive` section. §12's
schema claims to list "every field that may appear" and has no marker
for it, so m0008's "the validator checks both" (m0008:36-38) has nothing
deterministic to key on — and the exemption is self-declared: adding the
section clears the gate. §11's older "the validator flags retroactive
matters" had the same gap, but it flagged for review; §7 now makes it a
transition gate. Recorded matter-locally on m0008.

**X8 · LOW-MEDIUM — §6's new retroactive hashed region assumes a
section §11 does not require at filing.** doctrine:177-182 hashes
`## Retroactive` and `## Execution` "as they stand at the acknowledged
commit". §3.1 requires `## Execution` to *enter* `executed`, and on this
path entering is what the acknowledgment causes; §11:288-291 lists what
must be filed — evidence, and a `## Retroactive` section — and does not
require `## Execution`. Either §11 must require the execution record
complete before acknowledgment, or the hash covers a section that did
not exist at the commit the operator named. W7's fix defined the region
without closing the ordering it depends on.

**X9 · LOW — the new run record's verdict undercounts its own
evidence.** `runs/2026-08-25-archive-thread-import.md`:280 says "all 65
line citations resolve"; step 2 of the same file (line 84) reports
`citations: 75`. Re-executing that file's own script at `7357244`
reproduces 75 (run record, step 2). Run files are never edited (§9.1);
recorded here.

**X10 · LOW — the response's numbering note fixes m0001 line drift and
leaves doctrine line drift.** m0001:676-679 warns that every `m0001:NNN`
in the round 2 entry now describes the file at `25d2e16`. The same
commit also moved §11 down about twenty lines, so round 2's
`doctrine:264` (W6, m0001:496) and `§11:264-270` (W7, m0001:503) now
land inside §9.3. m0007:98's `Doctrine §6:165-170` survives only because
the §6 insert went in below it.

**X11 · LOW — `README.md`:46-59 says the recorded prompt "stands except
for one line", then amends a second.** The same section re-scopes step
1's fidelity check to both threads, which is a second change; and the
prompt as recorded at
[thread:646-671](../threads/2026-08-24-audit-and-adjudication.md) names
branch `claude/beatcode-pr1-audit-1t400g`, not this one. "Stands except
for one line" is three changes described as one.

**X12 · LOW — the link check's re-scoping is honest, but it is written
down outside the normative text.** Independently confirmed (run record,
step 7): 165 relative links tree-wide, 164 in authored files, all
resolving, none leading-slash; exactly one hit, at
[design:475](../threads/2026-08-24-matter-system.md), inside a
four-row table where the agent *quotes* OKF's bundle-absolute form to
the operator. Editing it would edit a primary source, which §9.2
forbids; nothing else hides behind the re-scoping. The scope statement
lives only at m0001:881-893 — a `## Vetting` append — and in a run
record. If it is a standing invariant it belongs in m0008's link bullet
(m0008:35) or §12.

**X13 · LOW — §8 requires branch names prefixed with the matter ID and
no branch in this repository is.** doctrine:225. The carve-out exists
only as an agent turn in a thread
([adjudication:640](../threads/2026-08-24-audit-and-adjudication.md),
"branch-name matter prefixes start with the next matter, per the
bootstrap exception"); §14 does not mention it.

**Checks passed clean:**

- **The import is exactly what it claims.** `c11956d`'s
  `threads/2026-08-24-matter-system.md` and this tree's are
  byte-identical, digest
  `50022f11…9816a` — the published hash, independently reproduced (run
  record, step 1). It is a move, not a re-export.
- **Every "Ruled in" citation resolves.** 35 rows, 46 citations, all
  landing on non-blank turns; 75 citations and 150 endpoints tree-wide,
  none dangling (run record, steps 2-3). Speaker-checked: 40 of the 46
  land in operator turns and 6 in agent turns, and five of those six are
  paired with the operator's answering turn in the same row.
- **Both rows the author added on its own initiative check out.**
  "describe, do not fix" is carried by design:146 and design:287, both
  operator turns, quoted accurately, and it does land in doctrine §1:37-39
  and this matter's Diagnosed reason. The state spine's re-sourcing to
  design:280 is verbatim — and is a real correction: at `25d2e16` that
  row was unmarked, which under the old preamble's "Unmarked rows are
  ruled in the thread directly" attributed it to the adjudication
  session, where it does not appear.
- **Retiring † was right for a reason the response did not claim.** The
  old marking was wrong in *both* directions. W2 caught one over-marked
  row; six unmarked rows were in fact design-sourced — the state spine
  (design:280), vetting by fresh agents and execution by a dev agent
  (design:173), the flat collection (design:175), deterministic code
  (design:177), and PRs citing matter IDs (design:317). All six now
  carry correct citations. A marker nobody could check had drifted; a
  citation anybody can check cannot.
- **W1–W11 all produced text or a recorded dispute; none was answered
  by discussion alone.** Each disposition was checked against the tree:
  W1 closed structurally at doctrine:184-189 plus `README.md`:65-102,
  with no pin computed anywhere in the commit; W2 by the import, with †
  gone from the table and row 75 citing design:298 inside the ratified
  region; W3(c) by the new risk-tiers row; W4 and W5 on m0010 and
  m0008; W6 in §7; W7 in §6; W8 on m0011 with the header rewritten
  3-for-3 lines, file length 856 → 856, so no `thread:NNN` citation
  moved; W9(a)(b) in the ledger; W10(a) corrected in the new entry
  rather than in the old one, which is correct under §6; W11 in §15.
- **The W2 dispute was right to make.** The author disputes the round's
  "a new archive dependency introduced by the fix for an
  archive-dependency finding" *as a description of the marking*, while
  conceding it as a description of the evidence. design:298 now settles
  it: the operator did defer the lenses machinery, in those words, so
  the claim was not manufactured — only its support was out of reach.
  Conceding the remedy while contesting the characterization is the
  narrowest possible dispute and it is correct on the merits.
- **The numbering note is accurate.** All four off-by-one
  cross-references verified: "Framing nit: W12" (m0001:404) is ranked
  W11; "See W11" (m0001:395) is W10; "W10(a)" (m0001:398) is W9(a);
  "W4-W12" (m0001:654) is W4–W11. There is no W12.
- **Consistency.** `tools/gen-index.py` (Python 3.11.15, PyYAML 6.0.1)
  regenerates `matters/index.md` byte-identically with a clean tree.
  Every frontmatter field used across the eleven matters is defined in
  §12, subkeys included; every timestamp is ISO 8601 with an explicit
  UTC offset; the only state used is `proposed`, which §3 defines; the
  §12 status derivation holds on all eleven.
- **Append-only held for the vetting record.** The response's 57
  deletions on this file are all inside the ratified region — frontmatter
  line, supersession note, Sources paragraph, the 33-row table, Scope,
  Execution. No `## Vetting` text was removed here or on any other
  matter.
- **Scope: nothing in the tree is unclaimed.** The tree is `README.md`,
  `doctrine/matters.md`, `matters/index.md`, m0001–m0011, three files in
  `runs/`, two in `threads/`, and `tools/gen-index.py`. The Execution
  section (m0001:124-134) claims each of them by name, including the
  imported design session and the interim generator. "Nothing else is in
  the tree" holds.
- **Git citation (§8).** One commit for the round, subject
  `m0001: vetting round 2 response`, `Matter: m0001` trailer; all eight
  commits on the branch carry the trailer.

**Not checked:** `markreveley/beatcode` — not cloned, and the render
reproduction not re-executed, because nothing in `25d2e16..7357244`
bears on it: m0002 and m0005 are untouched and m0003 and m0004 gained
only response entries applying nothing. Rounds 1 and 2 own those
verdicts and this round neither challenges nor re-asserts them. The
archived collection was read for the text-reuse comparison (X1) and for
the design session's provenance, not audited on its own merits — it is
closed and unmerged.

- **Disposition:** X1 is the one finding that should reach the operator
  before the ratification read, because it is about a sentence in the
  ratified region of three files and about the method the whole second
  bootstrap was justified by; it is also the finding the retired
  isolation line was hiding, which is an argument that retiring it was
  correct. X2 and X3 are the next two, both concerning what the operator
  is being asked to confirm: a ruled premise quietly reversed, and a
  confirm-at-ratification list that is short. X4 and X5 are fidelity
  corrections to the ledger and Scope, now cheap because the sources are
  in the tree. X6–X8 are holes in normative text this commit wrote and
  nobody had reviewed. X9–X13 are consistency residue. None blocks
  continued vetting; nothing found in the ledger's citations, the
  import, the derived views, or the scope claim failed.

### Round 3 addendum — 2026-08-25 — operator-directed

Two findings applied by the reviewer on operator instruction ("proceed
with fixes"), deliberately bounded to the two that bear on the
ratification read itself. Everything else round 3 filed — X2, X4–X13 —
is left as findings.

- **X1 applied, at all three sites.** doctrine's header, `README.md`'s
  status paragraph and this matter's supersession note no longer say
  "none of its doctrine or matter text was reused". Each now states what
  is true and checkable: nothing in the archive was ratified, so nothing
  carried a ratification; the bundle was re-authored rather than
  derived; it was re-authored by an agent that had read the archive, and
  passages survive, with the measurement cited to
  [runs/2026-08-25-vetting-round-3.md](../runs/2026-08-25-vetting-round-3.md).
  The doctrine header also states the distinction the adjudication
  session drew and the tree had lost — fresh authoring as a *method*,
  not claimed as a pedigree
  ([adjudication:514](../threads/2026-08-24-audit-and-adjudication.md)).
- **X3 applied, in §15.** The list is six → twelve, grouped by how each
  choice came to be unruled: five presented before authoring and left
  unruled; six written later by an author answering a vetting finding
  (§6's ratified region, §3's terminal owners and re-open, §5's
  precedence rule, §11's retroactive path, §7's `depends_on` gate, §6's
  retroactive hashed region); and one — §4's completeness-as-checklist
  and the absent `draft` state — that was put to the operator as R1 and
  expressly not ruled on
  ([adjudication:463-465](../threads/2026-08-24-audit-and-adjudication.md),
  answered at
  [adjudication:506](../threads/2026-08-24-audit-and-adjudication.md)).
  The section gains no rule; it enumerates. That is the one kind of
  addition §15 exists to make.

**What was deliberately not applied, and why.** X6 — m0007:39's "§6
defines two" regimes, now three — is a one-word factual error and was
left alone: m0007 is a separate `proposed` matter, outside the
ratification read this fix serves, and correcting it is the author's
move. The same reasoning holds for X2, X4, X5 and X7–X13. The scoping is
itself a response to what these rounds have been doing: the diagnosis
round 3 reached is that findings answered by writing new normative text
generate the next round's findings, so this commit adds no rule to the
doctrine — X1 replaces a false sentence with a true one, X3 lengthens a
list whose function is to be complete.

**Deviation, recorded.** Under the convention at
[adjudication:750](../threads/2026-08-24-audit-and-adjudication.md) a
reviewer states findings and the author applies them; here the operator
directed the reviewer to apply. This is the same deviation round 2
recorded twice (m0001:599-612, m0001:628-657), and it has the same
consequence: the ratification read should treat this file's round 3
reviewer and the author of these four edits as the same instance, and
therefore not independent for the three X1 sites and §15's list.

### Operator review — 2026-08-25 — in-document

- **Reviewer:** the operator, for the first time over the whole
  document since vetting began — and through the channel §8 prescribes:
  a committed file edit. Commit `9c1d295` writes nineteen `->[…]`
  comments into `doctrine/matters.md`; the session that answered it
  adds a task message, four prompted questions with answers, and a
  naming interjection.
- **Where the record lives:** the entire exchange is exported verbatim
  to
  [threads/2026-08-25-doctrine-operator-review.md](../threads/2026-08-25-doctrine-operator-review.md)
  — comments c01–c19 byte-exact from `9c1d295` with their locations,
  answers a1–a4, interjection i1 — with transcription fidelity verified
  in
  [runs/2026-08-26-operator-review-response.md](../runs/2026-08-26-operator-review-response.md).
  This is the first exercise of the in-document review convention that
  §8 now defines, and the export mechanism is itself the answer to the
  review's c12.
- **What the comments carry**, in three kinds: rulings — the process is
  a consumable framework, ratified as such now, named **Formic
  Matters** (i1; "Formic Ascent" in c02, superseded), this repository
  to be renamed to it, a new beatcode-dev created as its first strict
  consumer, `target` removed from the spec, the §13 tripwire declared
  fired, §15's presented-group "others are ratified"; directed edits —
  c01, c03, c04, c05, c07, and c06's unit-of-work correction; and seven
  questions — c08 (in-flight/queued), c09 (deviations), c10 (filing),
  c11 (executed as completed?), c12 (persisting exchanges like this
  one), c18 and c19 (plainspeak breakdowns before ruling on §15's
  later-written and not-ruled items). c02 ends mid-sentence; its
  truncated clause was resolved by prompted question q1/a1: the
  framework self-hosts — m0001 and the process matters stay with the
  framework; the beatcode-facing matters move to the new consumer.
- **Not a §6 vetting round:** the reviewer is the operator, and several
  comments are rulings rather than findings. Recorded here because this
  file is where m0001's review history accretes, and because the
  response below is structured like a response round: every comment
  dispositioned, every question answered.

### Round 3 response — 2026-08-26 — claude-code/2026-08-26 (author)

A fresh author instance — not the round 3 reviewer, and not the author
of any earlier response. X1 and X3 were applied by the round 3 addendum
on operator instruction; the remaining findings are answered here, in
the same commit that answers the operator review, because four of them
(X7, X8, X12, X13) fix text the review's rewrite restructures anyway.
Where a fix lands in rewritten text, §15's new group names it so the
ratification read sees the authorship.

- **X2 — (a) applied in the ledger; (b) answered by this turn's own
  discipline.** (a) The Q3 row now cites the ruling turn
  (adjudication:601) and carries the reversal on its face: the
  stays-archive-side premise was reversed by the round 2 response's
  import, recorded there, on m0011, and in X2 itself. Nothing is
  un-reversed by saying so; what the finding asked — that the record
  stop contradicting §9.4 silently — is done. (b) The three uncited
  operator directions arrived through the session harness, outside any
  exported thread; nothing in the tree can retroactively contain them,
  and no citation is manufactured. What changes is forward-looking:
  m0011's Open now carries "what record an export-or-import event
  itself requires" (its round 3 finding asked for exactly this), and
  every direction *this* response acts on has a primary source in the
  exchange thread — a1–a4 and i1 are citable where "proceed with fix"
  never was.
- **X4 — applied.** The org/assertions row and the Scope section now
  cite [design:467](../threads/2026-08-24-matter-system.md), the turn
  that contains the derivation, and say whose it is: the agent's,
  unanswered by the operator, standing because never contradicted and
  confirmed at ratification.
- **X5 — applied.** Two rows added (the bootstrap authorization at
  design:459; the no-unratified-facts ruling at design:486), and four
  rows gain the citations the finding named: dev-agent execution +
  adjudication:290, the worklist/superset answer + design:449, OKF
  adoption + adjudication:310/394/473, and the Q3 row +
  adjudication:601.
- **X6 — applied on m0007:** "§6 defines two" is now three, in the
  ratified region, with the retroactive regime in the list; see m0007's
  entry.
- **X7 — applied in the spec.** §7 gains the gate's exit — supersession
  re-points dependents' `depends_on` at ratification of the superseding
  matter; a dependency ending `rejected`/`withdrawn` blocks dependents
  until each amends `depends_on`, a frontmatter edit outside the
  ratified region, validated at the next transition — and §12 names the
  `## Retroactive` section as the path marker, with the
  self-declaration containment (the exemption only defers checking to
  the acknowledgment, which is stated over that section). m0008's entry
  records the validator implications.
- **X8 — applied in §11:** the `## Retroactive` and `## Execution`
  sections must be complete at the commit the operator acknowledges;
  §6's region cannot cover a section that does not yet exist.
- **X9 — acknowledged; nothing to edit.** Run files are never edited;
  the correct count is in round 3's own run record.
- **X10 — acknowledged; adopted as practice.** This response cites
  moving targets by section anchor or stable label (`review cNN`), not
  line number; the vetting record's historical `:NNN` citations remain
  readable at the commits their entries name.
- **X11 — applied in the README.** "Stands except for one line" now
  enumerates what actually changed: the isolation line retired, the
  fidelity check re-scoped over all threads, and the recorded prompt's
  branch name historical.
- **X12 — applied in §12:** the authored-files link-check scope is
  normative text, stated where the link dialect is defined.
- **X13 — applied in §14:** branch-name and PR-title prefixes start
  with the first matter after an installation's bootstrap; the
  bootstrap's own branches predate the collection they create.

### Operator review response — 2026-08-26 — claude-code/2026-08-26 (author)

The same author instance as the round 3 response above; one commit
carries both, plus the exchange thread, the rewritten specification,
the conformed collection, m0012, and the regenerated index. Every
comment c01–c19 is dispositioned here; the plainspeak breakdowns c18
and c19 asked for close the entry. Citations into the exchange use its
stable labels.

**Directed edits — applied.**

- **c01** — §1 opens "A matter is one proposed change to a system".
- **c03** — the two-target enumeration is gone; §1 now defines an
  installation and lets it declare its governed systems as tags. The
  self-hosting sentence from the redacted bullet survives at the
  framework level, where a1 put it.
- **c04** — applied as "Nothing lands in any governed system": the
  operator's "any" kept, the word "target" retired with the field
  (conforming under c07's license). Recorded as a deliberate wording
  choice, not silent drift from the comment's literal text.
- **c05** — applied per a2: two exceptions stand, the first
  generalized — the bootstrap of an installation (§14). "Two defined
  exceptions" stays true.
- **c06** — answered yes, and applied: "The matter is the unit of work,
  not the commit." The word "proposal" was doing undefined work;
  "filed"/"proposed" are now defined terms (§4, see c10).
- **c07** — the one-collection/one-sequence paragraph is rewritten
  installation-generic: one collection and one ID sequence per
  installation, systems interspersed, "all matters for one system" a
  query over tags.
- **c13** — `target` is out of the schema. Every matter's frontmatter
  is conformed in this commit: the field removed, the governed system
  named as the first tag (`beatcode` on m0002–m0005 and m0009;
  `formic-matters` on m0001, m0006–m0008, m0010–m0011). The index
  generator drops the target requirement and column and shows tags.
- **c16** — the §15 bullet's two-target premise dissolved with the
  field; what §1 now states, and the ID restart, remain listed for the
  ratification read, since the review ruled on the premise rather than
  the residue.

**Rulings — recorded, and executed as far as text can execute them.**

- **c02 + i1** — the framework is real and named **Formic Matters**;
  the specification is rewritten as its formal spec, framed for any
  installation, with beatcode kept as the motivating example where
  concreteness helps. The naming supersession ("Formic Ascent" → i1) is
  on the ledger. The truncated "however" clause is resolved by a1:
  framework self-hosts, beatcode-facing matters move.
- **c14, c15** — §13 is rewritten from tripwire-deferral to topology:
  the tripwire is recorded as fired by ruling, five candidate adopters
  named. The mechanics — rename this repository, create the new
  beatcode-dev, move m0002–m0005 and m0009 — are
  [m0012](m0012-formic-matters-split.md), filed `proposed` this commit:
  repository renames and creation are operator/admin acts this session
  cannot perform, and under this spec they should not land un-mattered
  anyway. m0012's plan is what the operator ratifies to execute the
  split.
- **c17** — §15's first group is marked ratified with the citation, and
  its items are out of the pending list.

**Questions — answered, each embodied in the text.**

- **c08 (in-flight/queued).** Neither a state nor a new field. States
  are positions in the ratification lifecycle and their transitions
  belong to the operator; in-flight vs. queued is execution plumbing
  inside `staged`, and it changes when agents start and stop. Making
  them states would put agent mechanics on the operator's state
  machine; storing a `dev-state` field would duplicate what `branch`
  presence already says, and two copies of one fact can disagree —
  that is drift by construction. §3 now states the derivation
  explicitly: `staged` + `branch` = in-flight, `staged` without =
  queued. Nothing new is stored; the distinction is derived, per §10.
- **c09 (deviations — ratify them, or endless loop?).** Both horns are
  avoided by splitting what "deviation" means. A deviation that changes
  *what was ratified* — behavior, scope, interface, normative text — is
  an execution failure: stop, `staged → proposed`, re-ratify the
  changed plan. That is the existing §3 path and it converges, because
  each failure narrows the plan — the loop is the system working. A
  deviation *within* the ratified intent, on detail the plan never
  pinned (a variable name, a file split, an equivalent command), lands
  and is recorded in `## Execution`. Requiring re-ratification for
  those would ratify history — the record is written after reality —
  and would make small honesty expensive, which is how processes get
  bypassed (m0010's argument). The dev agent errs toward stopping; the
  record makes each call auditable; a landed deviation the operator
  reads and dislikes is a new matter, because nothing leaves
  `executed`. §3.1 now says all of this.
- **c10 (filing).** Confirmed: "filed" and "proposed" name one event —
  the act and the resulting state. §4 now defines it: to file a matter
  is to add its file to the collection in state `proposed`.
- **c11 (is `executed` not the completed state?).** Yes — `executed` is
  the terminal state, where a matter is *done*. What §4 was calling
  "completeness" is a different thing: whether the matter's required
  sections exist yet, which gates `ratified` — an earlier gate, not the
  end of life. The collision was the word. §4 now says
  **ratification-readiness** is a checklist, checked at the gate; done
  is `executed`, answered by state.
- **c12 (persisting exchanges like this one).** Both offered options,
  combined — because each alone loses something. The commit pointer
  alone (`9c1d295`) is immutable and sufficient for verification, but
  it leaves the exchange readable only through git archaeology, and
  §9.2 wants primary sources on the shelf. A duplicate copy of the
  whole file at state duplicates what git already keeps. The mechanism
  now in §8: the comment commit is an operator turn; the responding
  agent transcribes every comment verbatim — location and commit cited
  — into a thread, and removes the markers in its response commit. The
  thread is the readable primary source; the diff pair is the
  underlying record; either can be checked against the other by anyone.
  [This exchange's thread](../threads/2026-08-25-doctrine-operator-review.md)
  is the first exercise, its fidelity verified by run record. m0011
  records the new modality in its Mechanism scope.

**c18 — plainspeak breakdowns of §15's later-written choices.** Each
of these is text an author wrote while answering a vetting finding,
which you have not separately ruled on; ratifying the document adopts
them. What each one is, and what it implies for you:

1. **§6's ratified region** (round 1, answering m0007). When you
   ratify a matter, the seal — the hash — covers the matter's
   substantive body only: not the YAML frontmatter, not the append-only
   `## Vetting` and `## Execution` logs. *Why:* state changes and
   review history are supposed to happen after ratification; if they
   were sealed, every legitimate lifecycle step would break the seal
   and the check would cry wolf. *Implication:* tampering with the
   substance is mechanically detectable while the lifecycle proceeds
   freely. *The trade:* frontmatter and appends are not sealed — a
   falsified append would not move the hash; catching that is git
   history's job, and m0007's checker names which regime it verified so
   the boundary is always explicit.
2. **§3's terminal owners and the re-open** (round 1). Who may end or
   reopen a matter: only you can reject; only the author can withdraw,
   and only before you decide; supersession happens as a side effect of
   you ratifying the replacement; and if a ratified plan turns out
   broken before work starts, you re-open it — back to `proposed`, with
   the old ratification stamp moved into the record rather than
   deleted. *Implication:* no agent can decline, bury, or silently
   re-ratify anything; every ending is yours or is the author backing
   out in the open, and ratification stamps are never erased.
3. **§5's earlier-ratification precedence** (round 1). If two matters
   you already ratified are later found to contradict each other, the
   one you ratified first governs until you explicitly supersede one.
   *Implication:* a discovered conflict never leaves the system
   ambiguous and never gets resolved by an agent's judgment call — the
   tiebreak is deterministic and the fix is always an explicit act of
   yours. *The trade:* first-ratified is not always the better text;
   the rule optimizes for a stable default, not for being right — being
   right is what the supersession is for.
4. **§11's retroactive path** (offered during adjudication, redesigned
   round 1). Emergencies and already-made decisions can act first and
   file after: the matter is filed `proposed` with evidence of what
   landed and a `## Retroactive` section saying why it could not wait;
   your acknowledgment moves it straight to `executed`; your refusal
   makes it `rejected` and spawns a matter to unwind what landed.
   *Implication:* the process admits reality without becoming optional
   — late review is still review, and nothing that landed escapes the
   record. *The risk:* the path becoming a habit; every retroactive
   matter is validator-flagged so it is always reviewed, and the
   acknowledgment is yours alone.
5. **§7's `depends_on` gate and its §11 exemption** (round 2). "This
   cannot run before that" is enforced by the machine at the moment of
   staging or executing, not just written down. The retroactive path is
   exempt because it exists precisely for work that could not wait —
   it declares its unexecuted dependencies instead of being blocked by
   them. *Implication:* execution order cannot be forgotten, and
   worklists are derivable. *The trade closed this round:* a gate needs
   an exit — a dead dependency used to mean a permanently stuck
   dependent; §7 now says how dependents are released (see X7 above).
6. **§6's retroactive hashed region** (round 2). For the retroactive
   path, what you acknowledge *is* what landed — so the seal covers the
   `## Retroactive` and `## Execution` sections too, as they stand at
   the commit you acknowledge. *Implication:* nobody can show you one
   account of what landed and let the record later say another; the
   account you acknowledged is sealed. *Closed this round:* those
   sections must be complete before you acknowledge (X8), so the seal
   cannot cover a section that does not exist yet.

**c19 — the R1 item, plainly.** The question you declined to pick on
was: should an incomplete matter have its own state — a `draft` before
`proposed`? The authored answer, now in §4: no extra state. `proposed`
covers everything from a one-line defect report to a finished plan;
what gates ratification is a checklist — does this matter have the
sections its type requires? — checked at the gate rather than encoded
as a state. *Implication for you:* filing stays cheap (a sentence is a
legal matter), the state machine stays small, and "ready to ratify" is
a question the validator answers rather than a status someone must
remember to flip. *The trade:* you cannot see readiness in the state
column — you ask the checklist. c11's confusion was the cost of the
old wording, and the section now uses "ratification-readiness" so the
checklist cannot be mistaken for the end of the lifecycle again.

**Independence, degraded in the standing way.** This author answered
the operator's questions and wrote the text embodying the answers;
nobody has reviewed the rewritten specification, the new §15 group
names every passage this response added, and the ledger's twelve new
rows — ten transcribing the review, two restoring 2026-08-24 rulings
X5 found missing — are this author's. The next round
should start exactly there: fidelity of the new rows against the
exchange thread, and the rewrite against the rulings — the same check
round 3 ran on the round 2 response, now possible against a primary
source that includes the operator's own answers.

### Operator review, round 2 — 2026-08-26 — in-session

- **Reviewer:** the operator, over the response — through the session
  channel their own r1 rules into §8. The turn is appended verbatim to
  [the exchange thread](../threads/2026-08-25-doctrine-operator-review.md)
  with a labeling apparatus, r1–r8, and the two intervening turns (the
  line-pinning question and the reading list its numbered replies refer
  to) are appended with it.
- **What it carries:** four findings on the specification — the
  operator channel should be file edits *or* a session exchange, with
  §8/§9.2 consolidated (r1); historical narration removed (r2); the
  bootstrap stated plainly (r3); §15 relocated out of the document
  (r4) — a partial ratification ("everything else in doctrine/matters
  is ratified", r5), approval of the response record and breakdown
  items (r6), one question and one ruling on m0012 (r7a, r7b), and a
  direction on the exchange record itself: comments must carry the text
  they respond to (r8).

### Operator review round 2 response — 2026-08-26 — claude-code/2026-08-26 (author)

The same author instance as the previous two entries. Every point
r1–r8 is answered; each disposition names its text.

- **r1 — applied in §8 and §9.2.** The operator's channel is now "the
  tree, reached two ways": committed file edits, or a session exchange
  that enters the record as a thread export. The two sections are
  stitched explicitly — §8 says when a thread comes to exist, §9.2 says
  what one is — rather than renumbered into one: every matter and
  vetting entry in the collection cites "§9.2" and "§8" by number, and
  renumbering would silently re-point all of them.
- **r2 — applied in §13, and extended to §1.** The tripwire history is
  gone from §13, which now states topology in two short paragraphs; the
  ledger and m0012 carry the history. The same principle was applied to
  one site the operator did not name: §1's "until the split executes
  (m0012), also beatcode and its development process" clause — interim
  instance state — is removed. Flagged here because it is an extension
  of the ruling, not a directed edit.
- **r3 — applied in §14.** The bootstrap is stated plainly: a
  repository adopts the framework by committing it; that first commit
  cannot go through a process that is not in the repository yet; it is
  recorded in the installation's first matter. This repository's own
  record keeps one paragraph, factual.
- **r4 — applied; the meta-matter is chosen.**
  [m0013](m0013-bootstrap-defaults-record.md) now carries the whole
  adopted-by-default record with a confirmation trail per item (c17,
  r5, r6 cited row by row), plus a new group E: the text this very
  response wrote, recorded as unconfirmed immediately. §15 shrinks to
  the standing rule — unruled choices are recorded on a matter and
  confirmed by ratifying it — and the deferred-design pointers. The
  meta-matter was chosen over `dev-history.md` because a matter is
  already the system's persistence unit and a confirmation record needs
  ratification semantics; a loose file would be a new un-mattered
  artifact class.
- **r5 and r6 — recorded, with the interpretation stated rather than
  assumed.** r5 is read as ratification in principle of everything
  outside the four named areas; r6 as approval of the response record
  and confirmation of the breakdown items (§15's groups B and D, now
  m0013's). Neither is treated as the formal §6 act: that act is over
  the whole document at a commit the operator names, and cannot precede
  the four changes this response makes. No `verified`,
  `ratified_commit`, or `ratified_sha256` is written. When the operator
  reads the revised text and states ratification naming the commit,
  the recording follows §6 exactly.
- **r7a — answered in m0012:** verbatim copy, pinned — the consumer
  carries the specification copied at a ratified commit beside an
  installation record (repo, commit SHA, sha256), verifiable with the
  README's three commands; upgrades are `spec` matters in the
  consumer's own collection; copy over submodule or release because the
  record must read with no tooling and the pin must be immutable.
- **r7b — applied in §7 and m0012.** The spec states the rule —
  `depends_on` names matters in the installation's own collection only
  — and m0012's plan now drops m0009's `depends_on: [m0008]` at the
  move, restating it as a prose precondition in m0009's body. The
  earlier cross-collection proposal is withdrawn.
- **r8 — applied to the exchange thread.** Every comment block is
  rebuilt as an in-situ excerpt: verbatim lines of the file at
  `9c1d295` over a stated range, with the operator's comment line
  inside them — each comment now carries exactly the text it responds
  to. The comment lines themselves are unchanged, the format amendment
  is declared in the thread's header with r8 as its authorization, and
  every excerpt is verified byte-exact against `9c1d295` in
  [runs/2026-08-26-review-round-2-response.md](../runs/2026-08-26-review-round-2-response.md).
  §8 and §9.2 now specify the in-situ form as the convention.
- **Not done, deliberately:** no ratification pin is computed (§6 — the
  text moved under this response); the repository rename and the new
  beatcode-dev remain operator/admin acts staged behind m0012; and the
  a3/a4 session-mechanics answers remain thread-recorded rather than
  ledger rows, as before.

**Independence, unchanged in kind.** This response again wrote the text
implementing the operator's rulings — §8, §9.2, §13, §14, §15, §7, §1,
m0012's mechanism, m0013 — and m0013's group E lists every passage so
the next read confirms them deliberately. The next round's fidelity
check has the full exchange in one thread: nineteen comments in situ,
four prompted answers, one interjection, and the response review, all
labeled.

### Ratification — 2026-08-26

The operator ratified the six round-2 checks one by one
([review k](../threads/2026-08-25-doctrine-operator-review.md)) and
then stated the formal act
([review f1](../threads/2026-08-25-doctrine-operator-review.md)):

> I ratify m0001, m0012, and m0013 at commit 85fe451

Recorded per §6, the pin following the act:

- **Head verified:** `85fe451` resolved to
  `85fe4511326a30516ed2bf86a2e2a2b9d05c3d25`, the head of the m0001
  branch on the remote at recording time — the named commit is the
  text as it stood.
- **m0001** — whole-file regime (§6: the proposed text is a separate
  document): sha256 of `doctrine/matters.md` at that commit,
  `5adc0aafe92c5ead0269c681c8802516572765cf77b22549ea5acc45d8dda7bd`,
  cross-checked against plain `sha256sum` per the README procedure.
  State `proposed → ratified → executed` in one act, §14's licensed
  jump; the Execution section above is completed.
- **m0012, m0013** — ratified-region regime: the body after the
  frontmatter, neither file carrying a `## Vetting` or `## Execution`
  section at the ratified commit. `21492653…54a747` and
  `b0f4810e…12cec5` respectively; full values and the exact extraction
  rule in
  [runs/2026-08-26-ratification-recording.md](../runs/2026-08-26-ratification-recording.md).
  Both matters move `proposed → ratified`; each carries its own
  ratification entry.
- **Basis, for the record
  ([review f2](../threads/2026-08-25-doctrine-operator-review.md)):**
  the operator read everything from the links in the exchange thread —
  GitHub views of this branch, byte-identical to the named commit —
  and stated earlier in the same exchange that the accumulated
  sectional review across the rounds sufficed and no continuous pass
  was wanted. Recorded as stated: the ratification rests on the
  reviewed rounds, each of which is in this record.
- The recording agent is the round-2 response author, not a fresh
  instance; every mechanical claim above is independently recomputable
  from the named commit, which is what the pins are for.
