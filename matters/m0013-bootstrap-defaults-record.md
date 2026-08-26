---
type: spec
title: Bootstrap defaults record
description: "The authoring-agent choices adopted without an operator ruling during the bootstrap, with the confirmation trail for each — relocated out of the specification on operator direction."
id: m0013
state: ratified
status: stable
tags: [formic-matters, doctrine, bootstrap]
implements: m0001
threads:
  - threads/2026-08-25-doctrine-operator-review.md
generated:
  by: claude-code/2026-08-26
  at: 2026-08-26T02:10:00Z
verified:
  - by: human:mark
    at: 2026-08-26T05:21:39Z
ratified_commit: 85fe4511326a30516ed2bf86a2e2a2b9d05c3d25
ratified_sha256: b0f4810ec3149b27416b1d18228681fb8ebf66d6060660304b796e7d7b12cec5
---

# m0013 · Bootstrap defaults record

## Why this exists

Spec §15 carried a growing list of choices the authoring agents adopted
without an operator ruling, so that ratifying the document confirmed
them deliberately rather than silently. The operator ruled that this
record does not belong in the specification —
"historical … if we DO wish to explicitly record this kind of thing …
within a meta-matter that covers historical decisions during bootstrap,
and is persisted as a matter"
([review r4](../threads/2026-08-25-doctrine-operator-review.md)). Of
the two offered homes, the meta-matter is chosen over a loose
`dev-history.md`: a matter is already the system's unit of persistence,
carries frontmatter for the derived views, and has ratification
semantics — which is exactly what a confirmation record needs. §15 now
states the standing rule (unruled choices are recorded on a matter and
confirmed by ratifying it) and points here.

Typed `spec` as the closest fit: the deliverable is text and the review
question is accuracy. If vetting wants a record-specific type, that is
a §2 change — its own `spec` matter.

## The record

Each entry: the choice, where it lives, who wrote it and when, and how
it was confirmed. Labels cite
[the review thread](../threads/2026-08-25-doctrine-operator-review.md).

### A — presented to the operator before authoring, left unruled

Ratified explicitly: "others are ratified" (review c17).

- the ratification recording mechanism of §6 — operator reads and
  states, agent computes and records the hash;
- the extraction tripwire's specific conditions — since superseded by
  the operator's own ruling that it fired (review c14, c15) and §13's
  rewrite to plain topology;
- the extension of "views are derived" to threads (§9.2);
- bundle-first sequencing — m0002–m0005 filed `proposed`, ratified
  after the specification.

One member of this group was ruled differently: the single interspersed
ID sequence was framed over two `target`s, and the operator dissolved
the premise by removing `target` (review c13, c16). Its residue — one
collection and one sequence per installation (§1), and the ID restart
at m0001 with the archive as a separate closed collection (§12) — is
spec text confirmed under r5 (below).

### B — written by an author answering a vetting finding (rounds 1–2)

Plainspeak breakdowns of all six, with implications and trades, were
delivered in the operator-review response entry on
[m0001](m0001-matter-system.md) (its "c18" section), as the operator
required before ruling (review c18). Confirmed on reading them
(review r6).

- §6's ratified-region definition (body minus frontmatter and record
  sections) — round 1, answering m0007;
- §3's owners for the terminal transitions, and the
  `ratified → proposed` re-open — round 1;
- §5's earlier-ratification precedence — round 1;
- §11's retroactive path, as redesigned in round 1;
- §7's transition-time `depends_on` gate and its §11 exemption —
  round 2;
- §6's hashed region for the retroactive path — round 2.

### C — written in the operator-review response (2026-08-26)

Text answering the review's own questions and round 3 findings;
confirmed under the operator's "everything else in doctrine/matters is
ratified" (review r5), except where the same message reopened the
section — noted per item.

- §3's in-flight/queued derivation from `branch` presence (review c08)
  — confirmed, r5;
- §3.1's deviation rule (review c09) — confirmed, r5;
- §4's definition of "file" and the ratification-readiness restatement
  (review c10, c11) — confirmed, r5;
- §7's gate exit — supersession re-points; rejection and withdrawal
  block until amended (round 3's X7) — confirmed, r5;
- §11's completeness-before-acknowledgment rule (round 3's X8) —
  confirmed, r5;
- §12's `## Retroactive` marker note and the authored-files link-check
  scope (round 3's X7, X12) — confirmed, r5;
- §8's in-document review convention (review c12) — the section was
  reopened by r1 in the same message; the amended §8 awaits the next
  read;
- §14's generalization of the bootstrap and branch-prefix carve-out
  (review a2, round 3's X13) — the section was reopened by r3; the
  rewritten §14 awaits the next read.

### D — put to the operator and expressly not ruled on

- §4's ratification-readiness-as-checklist and the absence of a `draft`
  state — the adjudication session's R1, which the operator declined to
  settle ("do i even need to pick?"), answered then by "whatever state
  machine the fresh author proposes and you ratify as a whole
  document". The plainspeak breakdown was delivered with group B's
  (m0001, "c19" section) and confirmed on reading (review r6).

### E — written in the review round 2 response, awaiting the next read

The response that created this matter also wrote text nobody has
confirmed; recorded here immediately, which is this record working as
§15 intends:

- §8's amended operator-channel bullet — file edits or session
  exchange, consolidated with §9.2 (implementing review r1);
- §9.2's stitch to §8 and the in-situ excerpt sentence (r1, r8);
- §13's slim topology text (implementing r2);
- §1's trimmed installation paragraph — the interim beatcode clause
  removed under r2's principle, an extension the operator did not
  explicitly direct;
- §14's plain rewrite (implementing r3);
- §15's slim form and this matter (implementing r4);
- §7's same-collection-only sentence — the rule is the operator's
  (review r7b); the wording is the author's;
- m0012's installation-mechanism proposal (answering review r7a).

## What ratifying this matter does

It confirms that this record is accurate and complete as of its
ratified commit: that these were the unruled choices, that the cited
confirmations happened, and that nothing adopted by an authoring agent
during the bootstrap is missing from it. Later unruled choices are
recorded by appending a group here (a frontmatter-visible revision
while `proposed`; after ratification, a new matter per §3), or on the
matter that owns them.

## Vetting

### Ratification — 2026-08-26

Ratified by the operator with m0001 and m0012 —
"I ratify m0001, m0012, and m0013 at commit 85fe451"
([review f1](../threads/2026-08-25-doctrine-operator-review.md)),
after ratifying this record as round-2 checklist item 4
([review k](../threads/2026-08-25-doctrine-operator-review.md)). That
act also closes group E's "awaiting the next read": the passages it
lists are in the specification and matters ratified in the same
statement. §6 permits ratification at any round; this matter had no
fresh-agent vetting round. Pin: ratified region at
`85fe4511326a30516ed2bf86a2e2a2b9d05c3d25`, sha256 in the frontmatter,
recorded in
[runs/2026-08-26-ratification-recording.md](../runs/2026-08-26-ratification-recording.md).
