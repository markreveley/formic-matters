---
type: spec
title: Contained installation layout for code-bearing consumers
description: "A consumer repository may carry its whole installation inside one root directory, .formic-matters/, instead of five root directories — chosen at bootstrap, default for repositories with their own code."
id: m0014
state: proposed
status: draft
tags: [formic-matters, topology, installation]
implements: m0001
threads:
  - threads/2026-08-26-m0012-execution.md
generated:
  by: claude-code/2026-08-26
  at: 2026-08-26T19:12:11Z
---

# m0014 · Contained installation layout for code-bearing consumers

## Diagnosed reason

The conventions §12 and §14 name — `doctrine/`, `matters/`,
`threads/`, `runs/`, `tools/` — sit at the repository root. That is
right where the installation *is* the repository's content: the
framework itself, and a dedicated process repository like
`beatcode-dev`. It is intrusive where it is not: the operator's five
candidate adopters carry their own source trees, and five process
directories at their roots collide with the host's own layout. The
operator directed a contained form and its name in the m0012
execution session
([thread R7](../threads/2026-08-26-m0012-execution.md)):
".formic-matters", chosen over the shorter ".formic" because the full
name self-documents and matches the framework. Filed now, before the
second adoption, so no two layout generations ever exist in the wild.

## Proposed text

Amendments to §12 and §14; additive — the root form remains valid and
remains the framework's own.

- **§12 gains a layout clause.** An installation lives in one of two
  forms, chosen at bootstrap: at the repository root — the
  framework's own layout — or wholly inside one containing directory
  at the root, named `.formic-matters/`. Inside the container the
  layout is identical (`doctrine/`, `matters/`, `threads/`, `runs/`,
  `tools/`), and because every authored link in an installation is
  relative (§12), moving the whole tree into the container changes no
  link. Which form an installation uses is read off where its
  installation record sits; changing form later is a `spec` matter in
  that installation's collection.
- **§12's default rule.** A repository whose content is the process
  itself uses the root form; a repository with its own code adopts
  the contained form. The bootstrap records the choice in the
  installation's first matter (§14, §15).
- **§14's convention sentence** names both forms where it names the
  directory conventions, and the installation record's path in the
  contained form is `.formic-matters/doctrine/installation.md`.
- **Forwarded to m0008:** the tooling locates an installation by
  probing `.formic-matters/`, then the root, and operates identically
  on both; the interim generator gains the same probe if it is still
  in service when this ratifies.

## What this contradicts

No ratified matter. It amends the specification's implicit anchoring
of the conventions at the repository root (§12, §14) by making the
anchor explicit and two-valued. Existing installations are untouched:
the framework and `beatcode-dev` keep the root form, and no retrofit
is proposed — a consumer that later wants the contained form files
that as its own matter.

## Notes

The container is a dotted directory deliberately, on the `.github/`
precedent: present and readable in every listing that matters, out of
the way in the host repository's daily view. The cost considered and
accepted: dotted paths are hidden from bare `ls`, and the consumer's
README should say where the installation lives — a sentence the
bootstrap already writes.
