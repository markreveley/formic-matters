---
okf_version: 0.2
---

# Matters

Derived from the frontmatter of every file in this directory.
**Do not hand-edit** — run `tools/gen-index.py`. See [m0008](/m0008-matter-tooling.md).

## executed

| | Type | Target | Matter |
|---|---|---|---|
| `m0001` | spec | beatcode-dev | [The matter system](/m0001-matter-system.md) |

## proposed

| | Type | Target | Matter |
|---|---|---|---|
| `m0002` | fix | beatcode | [SPEC justifies fixed ordering with a false claim about commutativity](/m0002-spec-commutativity-claim.md) |
| `m0003` | spec | beatcode | [SPEC states order-sensitive rules without their mechanisms](/m0003-spec-order-rules-lack-mechanism.md) |
| `m0004` | fix | beatcode | [§9.4 track length conflates an index with a count](/m0004-track-length-index-count.md) |
| `m0005` | fix | beatcode | [beatcode README claims the implementation does not exist](/m0005-readme-stale-status.md) |
| `m0006` | feature | beatcode-dev | [Structured review lenses and dry-round termination](/m0006-review-lenses-and-dry-rounds.md) |
| `m0007` | feature | beatcode-dev | [Ratification records a content hash](/m0007-ratification-content-hash.md) |
| `m0008` | feature | beatcode-dev | [Matter tooling — validator, ID allocator, index generator](/m0008-matter-tooling.md) |
| `m0009` | spec | beatcode | [SPEC-GAPS becomes a derived view over matters](/m0009-spec-gaps-to-matters.md) |
| `m0010` | feature | beatcode-dev | [Risk tiers derived from paths touched](/m0010-risk-tiers.md) |
| `m0011` | spec | beatcode-dev | [Thread persistence policy](/m0011-thread-persistence.md) |

## Ordering

`implements` names the spec a matter serves; `depends_on` constrains execution order.

| Matter | Implements | Depends on |
|---|---|---|
| `m0003` | — | [m0002] |
| `m0006` | m0001 | — |
| `m0007` | m0001 | [m0008] |
| `m0008` | m0001 | — |
| `m0009` | — | [m0008] |
| `m0010` | m0001 | [m0008] |
| `m0011` | m0001 | — |
