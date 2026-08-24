---
type: feature
title: Ratification records a content hash
description: Ratification is a state flag, so a matter can drift after ratification and a dev agent builds something never vetted.
id: m0007
state: proposed
target: beatcode-dev
implements: m0001
depends_on: [m0008]
tags: [process, integrity]
---

# m0007 · Ratification records a content hash

## Feature

Ratification today sets `state: ratified`. Nothing binds that state to
the *text* that was ratified. The document can be edited afterward, and a
dev agent will faithfully execute a plan no one approved.

Store the SHA-256 of the matter body at the moment of ratification. A dev
agent verifies the hash before starting and refuses if it has moved,
which forces the change back through re-ratification.

## Proposed implementation

- `ratified_hash` in frontmatter, written when `state` enters `ratified`.
- Hash covers the body only, so frontmatter transitions (`ratified` →
  `staged` → `executed`) do not invalidate it.
- Verification is a subcommand of the tooling
  ([m0008](/m0008-matter-tooling.md)) and a precondition of the
  dev agent's first action.

Fully deterministic; roughly ten lines once the tooling exists.

## Notes

This matter is the reason `doctrine/matters.md` §10 exists: m0001 was
ratified in conversation before its text was written, which is this exact
drift with the operator's consent. m0001 is the only permitted instance.
