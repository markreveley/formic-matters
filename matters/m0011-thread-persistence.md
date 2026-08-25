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
threads: [threads/2026-08-24-audit-and-adjudication.md]
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
  traffic dropped; prompted-question answers kept as human turns;
  mid-turn interjections kept and labeled.
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
  when and how a thread is brought current afterward.
- **Concept status.** Thread files sit outside the `matters/` bundle
  and carry no `type`; whether they should become OKF concepts is open.

## Notes

This collection's first thread export ran ahead of this policy, by
operator instruction, under the standing proposals above — recorded
here rather than left tacit, since under the doctrine a change to this
repository should originate as a matter.

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
