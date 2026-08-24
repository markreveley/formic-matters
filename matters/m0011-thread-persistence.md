---
type: spec
title: Thread persistence policy
description: Whether, and in what form, the conversations that produce matters are kept in the repo.
id: m0011
state: proposed
target: beatcode-dev
implements: m0001
tags: [process, provenance]
---

# m0011 · Thread persistence policy

## Diagnosis

A matter records a decision. It does not record how the decision was
reached — the wrong turns, the corrections, the reasoning the operator
supplied that the final text absorbed silently.

For m0001 that derivation is most of the value: the doctrine's shape came
out of a specific argument about type-versus-state, an operator veto on
premature review machinery, and a live example of the failure the system
exists to prevent. None of that survives in `doctrine/matters.md`.

## Proposed text

Not yet drafted. The operator has stated a leaning, not a decision.

Open questions:

- **Scope.** Every session, or only those that produce or ratify a
  matter?
- **Form.** The first export
  ([2026-08-24](../threads/2026-08-24-matter-system.md)) keeps human and
  assistant turns verbatim and drops reasoning traces, tool calls, and
  tool results. Whether that is the right cut is unreviewed — dropping
  tool calls removes the evidence for claims made in the turns around
  them.
- **Location.** `threads/` sits outside the `matters/` OKF bundle,
  because thread files are not concepts and carry no `type`. Whether
  they should become OKF concepts is open.
- **Linkage.** A matter has no field pointing at the thread that
  produced it.
- **Redaction.** Threads capture whatever was on screen, including paths
  and repository contents unrelated to the matter at hand. The first
  export was published to a public repository and then redacted after the
  fact — absolute local paths to `~`, the session project slug to
  `<project>`. A policy that redacts before publishing, and states what
  it redacts, is not yet written.

## Notes

The first export was made by direct operator instruction, ahead of this
matter. Recorded here rather than left tacit, since under
`doctrine/matters.md` a change to this repo should originate as a matter.
