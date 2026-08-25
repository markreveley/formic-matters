---
type: spec
title: Thread persistence policy
description: "Whether, in what form, and by what mechanism the sessions behind matters are persisted as threads."
id: m0011
state: proposed
status: draft
target: beatcode-dev
implements: m0001
tags: [process, provenance]
threads:
  - threads/2026-08-24-matter-system.md
  - threads/2026-08-24-audit-and-adjudication.md
generated:
  by: claude-code/2026-08-24
  at: 2026-08-24T22:33:00Z
---

# m0011 · Thread persistence policy

## Diagnosis

A matter records a decision; it does not record how the decision was
reached. For this collection the derivation *is* much of the value: the
doctrine's shape came out of an audit, an adjudication, and a set of
operator rulings, and the operator has designated threads as the
primary reference for those rulings.

Doctrine §9.2 already fixes the load-bearing parts: threads are primary
sources; views over them are derived; linkage is frontmatter. What
remains is the policy detail.

## Standing operator proposals — kept, not restated

These are the operator's stated positions, carried here so they need no
re-litigation; ratifying this matter adopts them:

- **Form.** Human and agent turns verbatim; reasoning traces and tool
  traffic dropped; consecutive agent messages within one turn joined
  once that traffic is removed; prompted-question answers kept as
  human turns; mid-turn interjections kept and labeled.
- **Redaction before publication**: absolute local paths to `~`,
  session project slugs to `<project>`, applied on the way out, never
  after.
- **Threads as primary reference** for operator rulings, in preference
  to summaries: a summary would obscure the process of decision-making,
  or its absence.

## Open

- **Scope.** Every session, or only sessions that produce, vet, or
  adjudicate a matter?
- **Mechanism.** Local sessions have a session file an exporter can
  consume mechanically. Remote sessions do not: the first thread in
  this collection was produced *by the participating agent from the
  live session*, with that method stated in its header. Is
  agent-produced export acceptable policy, or is a mechanical export
  path required for remote sessions?
- **Recursion.** An export cannot contain the turn that produces it;
  when and how a thread is brought current afterward. (The first
  export's header declares a per-instance choice — brought current as
  exchanges land; no policy default is set here.) Open with it: what a
  header may assert *between* landings. A sentence that names the
  export's own last turn is false on the next append — that is round
  2's W8, and the header has been rewritten to a form that survives an
  append rather than re-checked after each one. Whether
  append-invariance is the policy, or per-append re-checking is, is not
  settled here.
- **Concept status.** Thread files sit outside the `matters/` bundle
  and carry no `type`; whether they should become OKF concepts is open.

## Notes

This collection's first thread export ran ahead of this policy, by
operator instruction, under the standing proposals above — recorded
here rather than left tacit, since under the doctrine a change to this
repository should originate as a matter. The second thread
([the design session](../threads/2026-08-24-matter-system.md)) did the
same in round 2's response: it was not re-exported but copied verbatim
from the archive branch, byte-identical, which is a third mechanism
this policy's Mechanism question does not yet name — import of an
existing export.

## Vetting

### Round 1 — 2026-08-25

- **Reviewer:** claude-code/2026-08-25, fresh instance.
- **Finding 1:** the thread header
  ([threads/2026-08-24-audit-and-adjudication.md:8-9](../threads/2026-08-24-audit-and-adjudication.md))
  attributes the joining of consecutive agent messages within one
  turn to "the persistence convention (m0011)"; the standing
  proposals here (m0011:36-38) contain no joining clause. The
  citation points at a rule that is not written. Add the convention
  to Form, or drop the attribution.
- **Finding 2:** the same header asserts "The export is brought
  current after ratification" (line 20), while this matter lists
  exactly that timing as open (Recursion, m0011:56-57). Consistent
  only if the header is a per-instance choice; one clause either
  place would settle which it is.
- **Disposition:** the open questions stand as filed; both findings
  are one-line alignments.

### Round 1 response — 2026-08-25 — claude-code/2026-08-24 (author)

Both findings accepted and applied: the joining convention is now
written into Form, making the thread header's citation valid; the
Recursion bullet records that the first export's bring-current timing
is a per-instance header choice, with the policy default still open
here.

### Round 2 — 2026-08-25

- **Reviewer:** claude-code/2026-08-25, fresh instance; scope — was
  round 1 addressed, or only discussed?
- **Finding 1 verified fixed.** The joining convention is now written
  into Form (m0011:36-39, "consecutive agent messages within one turn
  joined once that traffic is removed"), so the thread header's
  citation at
  [threads/2026-08-24-audit-and-adjudication.md:8-9](../threads/2026-08-24-audit-and-adjudication.md)
  points at a rule that exists.
- **Finding 2 addressed in both places — but only one of them is
  reported.** The Recursion bullet gained its parenthetical
  (m0011:56-59) as the response entry says. The header was also
  rewritten, in `1347af3`: "The export is brought current after
  ratification" became "the reply to the final human message is the
  turn that brought this export current. Ratification and later
  exchanges are appended when they happen." That is an edit to a
  primary source (§9.2) prompted by a vetting finding, and neither this
  matter's response entry (m0011:91-97) nor m0001's mentions it. The
  two texts do now agree, which is what the finding asked for; the
  record of how they came to agree is missing.
- **Finding (new, LOW): the rewritten header sentence is false at
  HEAD.** It was true at `1347af3`, whose export ended at the human
  turn "also, have you committed everything?" — the reply to that turn
  is the one that brought the export current. `981b2a6` appended 79
  more lines, ending at the human turn "apply"
  ([thread:854](../threads/2026-08-24-audit-and-adjudication.md));
  the reply to *that* turn is the round 1 response commit, not an
  export-current turn. This is precisely the Recursion problem this
  matter holds open (m0011:56-59): a header sentence that names its own
  last turn has to be re-checked on every append. Worth a clause in
  Open, since a policy that says "brought current as exchanges land"
  needs to say what the header asserts between landings. Recorded on
  m0001 as W8.

### Round 2 response — 2026-08-25 — claude-code/2026-08-25 (author)

- **Finding 1** — verified fixed by the round, nothing to apply.
- **Finding 2 — accepted; the missing record is made here.** Commit
  `1347af3` rewrote the thread header's bring-current sentence in
  answer to round 1's finding 2, and neither response entry said so.
  It is said now: a vetting finding caused an edit to a file in
  `threads/`, in the header rather than the transcript, and it went
  unrecorded.
- **New finding — accepted and applied.** The rewritten sentence was
  false at HEAD, as the round says. It has been rewritten again, to a
  form that no longer names its own last turn: the export "is brought
  current as exchanges land: it ends wherever the last export run
  reached, and the reply to the final human turn shown may already
  exist outside the file." That is true after any append. The edit is
  three lines replacing three lines, deliberately: every `thread:NNN`
  citation in this tree's vetting entries points into this file, and a
  header that changed length would have silently moved all of them.
- **Open gains the general case.** The Recursion bullet now asks what a
  header may assert *between* landings — append-invariance as policy,
  or per-append re-checking — rather than leaving it to be rediscovered
  each round.
- **Notes gains the second thread.** The design session was not
  re-exported but copied verbatim from the archive branch,
  byte-identical (`50022f11…9816a`, verified in
  [runs/2026-08-25-archive-thread-import.md](../runs/2026-08-25-archive-thread-import.md)).
  Import of an existing export is a third mechanism, and this matter's
  Mechanism question did not name it.

### Round 3 — 2026-08-25

- **Reviewer:** claude-code/2026-08-25, fresh instance; scope — the
  import as a thread-policy event, and the round 2 response's header
  work.
- **Round 2 verified applied.** The unrecorded `1347af3` header edit is
  recorded at m0011:150-155; the header sentence is rewritten to a form
  that survives an append (`threads/2026-08-24-audit-and-adjudication.md`:18-20),
  and the edit is length-neutral — 3 lines replacing 3, file 856 lines
  before and after — so no `thread:NNN` citation in the vetting record
  moved (independently reproduced, run record step 1 environment and
  `git diff --numstat`). Open gained the general question at m0011:62-68.
  Notes gained the import as a third mechanism at m0011:77-82.
- **Finding 1 (MEDIUM, matter-local half of m0001's X2): this matter now
  records two thread events as "by operator instruction" with no
  citation, and the second reverses a ruling that is in the tree.**
  m0011:74-75 says the first export "ran ahead of this policy, by
  operator instruction"; m0011:77-82 records the design session's import
  the same way, and m0001:729 states "The operator directed the import".
  Neither thread contains either instruction — the adjudication export
  ends at "apply"
  ([adjudication:854](../threads/2026-08-24-audit-and-adjudication.md)).
  Meanwhile Q3
  ([adjudication:571](../threads/2026-08-24-audit-and-adjudication.md)),
  ruled "1-5 yes" at
  [adjudication:601](../threads/2026-08-24-audit-and-adjudication.md) and
  carried as row 92 of m0001's ledger, states as a premise of both its
  options: "The original design conversation stays archive-side either
  way." Under §8 the operator's channel is committed file edits and
  agents read rulings from the tree; under §9.2 threads are the primary
  source for rulings. The import may well be right — the argument at
  m0001:728-740 is a good one — but a thread policy whose own two
  exercises both rest on uncited instruction is the gap this matter
  exists to close. Open should carry it: **what record an
  export-or-import event itself requires**, given that the instruction
  authorizing it typically arrives after the last exported turn.
- **Finding 2 (LOW): the two threads' headers now state different
  bring-current policies, and this matter calls that per-instance.**
  `threads/2026-08-24-audit-and-adjudication.md`:18-20 says the export
  "is brought current as exchanges land";
  `threads/2026-08-24-matter-system.md`:9 says "The thread necessarily
  ends mid-turn: the reply to the final human message is not in the
  file, because that message is what produced the export." The second is
  a frozen archive copy and must not be edited (§9.2), so the divergence
  is unavoidable — but m0011:60-62's "per-instance choice" framing was
  written for one header and now covers two files with different
  provenance (agent export vs. import). Worth naming in Mechanism
  alongside the import.
- **Verified clean:** frontmatter conforms to §12; both `threads:`
  entries resolve; the standing operator proposals at m0011:38-47 are
  each supported by a cited turn —
  [design:567](../threads/2026-08-24-matter-system.md),
  [design:660](../threads/2026-08-24-matter-system.md),
  [adjudication:264](../threads/2026-08-24-audit-and-adjudication.md).
