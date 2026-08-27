# CLAUDE.md — Formic Matters, the framework's home

This repository is the home of **Formic Matters**, the matter
framework. It is self-hosting: every change to it goes through its own
process. The normative authority is `doctrine/matters.md` — read it
before acting; section references below (§N) point into it. The state
of every matter is `matters/index.md` (derived); the history of
operator rulings is m0001's rulings ledger and the `threads/` exports.

Standing rules, distilled — the doctrine governs wherever they differ:

- **Nothing lands without a matter** (§1). Filing is cheap;
  ratification is the operator's act alone, over exact text at a
  commit the operator names (§6).
- **`staged → executed` happens only through a dev agent the operator
  launched** (§3). When a ratified plan proves wrong mid-execution,
  stop and record — `staged → proposed` (§3.1). Err toward stopping.
- **The pin follows the act** (§6): never offer a ratification pin in
  advance. m0001's pin is the whole `doctrine/matters.md` file; every
  other matter's is its body minus the frontmatter and the append-only
  `## Vetting` / `## Execution` sections.
- **`threads/` and `runs/` are append-only primary sources** — never
  edited after the fact, never rewritten to satisfy a check (§9.1,
  §9.2, §12).
- **No instance state and no client names in current-voiced matter or
  normative text** — write "consumer" or "client"; names belong in
  historical record sections and thread citations (review r2; m0014's
  failure entry is the cautionary case).
- **Links inside the repository are relative; cross-repository
  references are pinned absolute URLs at immutable commits** — full
  SHAs, never branch names or `main` (§9.4). Pull requests merge as
  merge commits, never squashes: pins reference branch commits.
- **Every commit carries a `Matter: mNNNN` trailer**; branch names and
  PR titles are matter-prefixed; a PR body is a one-line pointer (§8).
- **`matters/index.md` is derived** — regenerate with
  `tools/gen-index.py`, never hand-edit (§12).
- **Consumers install the framework only inside `.formic-matters/`**;
  this repository's root layout is the framework's home, not a form an
  installation could choose (§12, m0014).

This file was filed as
[m0015](matters/m0015-agent-instructions.md) on operator direction; it
distills and never overrides, and changes to it go through matters
like everything else.
