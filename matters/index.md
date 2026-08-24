---
okf_version: "0.2"
---

# Matters

Derived from the frontmatter of every matter in this directory.
**Do not hand-edit** — run `tools/gen-index.py`. See [m0008](m0008-matter-tooling.md).

## proposed

| | Type | Target | Matter | Description |
|---|---|---|---|---|
| `m0001` | spec | beatcode-dev | [The matter system](m0001-matter-system.md) | Every change to beatcode or to this repository is proposed, vetted, and ratified as a matter before it is made. |
| `m0002` | fix | beatcode | [SPEC §9.3 justifies mix order with a false commutativity claim](m0002-spec-commutativity-claim.md) | SPEC §9.3 says float addition does not commute; commutativity is not what fails — associativity is. |
| `m0003` | spec | beatcode | [SPEC states order-sensitive rules without their mechanisms](m0003-spec-order-rules-lack-mechanism.md) | Several normative rules are asserted without the reasoning that makes them checkable, starting with the §1.1 timing-pipeline diagram. |
| `m0004` | fix | beatcode | [SPEC §9.4 track length mixes an index with a count](m0004-track-length-index-count.md) | frames = last + 22050 yields a 22,049-frame silent tail, one short of the comment's half second; the tail is the oracle's own behavior — resolved, prose-only fix. |
| `m0005` | fix | beatcode | [beatcode README claims the implementation does not exist](m0005-readme-stale-status.md) | README says Specification seed and heads its command list Commands (once built); the implementation is merged to main with all tests green. |
| `m0006` | feature | beatcode-dev | [Structured review lenses, dry-round termination, anchoring rules](m0006-review-lenses-and-dry-rounds.md) | Give each reviewer a distinct lens, terminate vetting on consecutive rounds that surface nothing new, and keep first-pass reviewers unanchored. |
| `m0007` | feature | beatcode-dev | [Drift enforcement for the ratification hash](m0007-ratification-content-hash.md) | Tooling that verifies ratified_sha256 before execution, so ratified text cannot drift unnoticed between ratification and the dev agent's first action. |
| `m0008` | feature | beatcode-dev | [Matter tooling — validator, ID allocator, index generator](m0008-matter-tooling.md) | The deterministic half of the matter system: everything checkable by code rather than by an agent. |
| `m0009` | spec | beatcode | [SPEC-GAPS becomes a derived view over matters](m0009-spec-gaps-to-matters.md) | The nine SPEC-GAPS entries are retroactively filed spec matters; SPEC-GAPS.md is regenerated from them, not maintained by hand. |
| `m0010` | feature | beatcode-dev | [Risk tiers derived from paths touched](m0010-risk-tiers.md) | Review rigor keyed off blast radius rather than type; a README typo and a rounding-rule change are both fixes. |
| `m0011` | spec | beatcode-dev | [Thread persistence policy](m0011-thread-persistence.md) | Whether, in what form, and by what mechanism the sessions behind matters are persisted as threads. |

## Ordering

`implements` names the spec a matter serves; `depends_on` constrains execution order.

| Matter | Implements | Depends on |
|---|---|---|
| `m0003` | — | m0002 |
| `m0006` | m0001 | m0008 |
| `m0007` | m0001 | m0008 |
| `m0008` | m0001 | — |
| `m0009` | — | m0008 |
| `m0010` | m0001 | m0008 |
| `m0011` | m0001 | — |
