---
type: fix
title: beatcode README claims the implementation does not exist
description: README says "Specification seed" and "Commands (once built)"; the implementation is on main with 48 tests green.
id: m0005
state: proposed
target: beatcode
tags: [docs]
---

# m0005 · beatcode README claims the implementation does not exist

## Diagnosis

`README.md` states:

> **Status.** Specification seed. This repo currently contains the
> complete behavioral spec, its golden conformance vectors, and the
> example scores; the implementation is built from them per PLAN.md.

and heads the command list "Commands (once built)".

The implementation is merged to `main` (PR #2, `fa17627`): 14 modules
under `src/`, 48 tests green across 15 binaries, and render hashes
committed to `goldens/renders-v0.1.txt`.

A reader arriving at the repo is told the product does not exist.

## Proposed fix

Update the status section and the command heading to reflect a built
v0.1.

How the repo should *position* itself — a spec-first reference with a
conforming implementation, versus a tool — is the operator's call and
should be settled during vetting, not assumed. That choice determines the
wording.
