---
okf_version: "0.2"
---

# Matters

Derived from the frontmatter of every matter in this directory.
**Do not hand-edit** — run `tools/gen-index.py`. See [m0008](m0008-matter-tooling.md).

## proposed

| | Type | Tags | Matter | Description |
|---|---|---|---|---|
| `m0006` | feature | formic-matters, process | [Structured review lenses, dry-round termination, anchoring rules](m0006-review-lenses-and-dry-rounds.md) | Give each reviewer a distinct lens, terminate vetting on consecutive rounds that surface nothing new, and keep first-pass reviewers unanchored. |
| `m0007` | feature | formic-matters, process, integrity | [Drift enforcement for the ratification hash](m0007-ratification-content-hash.md) | Tooling that verifies ratified_sha256 before execution, so ratified text cannot drift unnoticed between ratification and the dev agent's first action. |
| `m0008` | feature | formic-matters, process, tooling | [Matter tooling — validator, ID allocator, index generator](m0008-matter-tooling.md) | The deterministic half of the matter system: everything checkable by code rather than by an agent. |
| `m0010` | feature | formic-matters, process | [Risk tiers derived from paths touched](m0010-risk-tiers.md) | Review rigor keyed off blast radius rather than type; a README typo and a rounding-rule change are both fixes. |
| `m0011` | spec | formic-matters, process, provenance | [Thread persistence policy](m0011-thread-persistence.md) | Whether, in what form, and by what mechanism the sessions behind matters are persisted as threads. |
| `m0016` | spec | formic-matters, process, execution, provenance | [Launch instructions are pointers, not shadow specifications](m0016-launch-instructions-policy.md) | A launch identifies the repository, matter, operator act, and external authority; all substantive scope and execution instructions live in the repository's ratified record. |
| `m0017` | spec | formic-matters, process, ratification, integrity | [Operator-authored ratification commits](m0017-operator-authored-ratification.md) | Ratification becomes an operator-authored summary and declaration committed to the matter; agent review verifies the summary, and the final operator commit is the act and exact-text pin. |

## ratified

| | Type | Tags | Matter | Description |
|---|---|---|---|---|
| `m0013` | spec | formic-matters, doctrine, bootstrap | [Bootstrap defaults record](m0013-bootstrap-defaults-record.md) | The authoring-agent choices adopted without an operator ruling during the bootstrap, with the confirmation trail for each — relocated out of the specification on operator direction. |

## executed

| | Type | Tags | Matter | Description |
|---|---|---|---|---|
| `m0001` | spec | formic-matters, doctrine, bootstrap | [The matter system](m0001-matter-system.md) | Every change to a governed system — and to the framework itself — is proposed, vetted, and ratified as a matter before it is made. |
| `m0012` | refactor | formic-matters, topology | [The Formic Matters split](m0012-formic-matters-split.md) | Rename this repository to the framework, create beatcode-dev as its first consumer installation, and move the beatcode-facing matters there. |
| `m0014` | spec | formic-matters, topology, installation | [Contained installation layout for code-bearing consumers](m0014-contained-installation-layout.md) | A consumer installation lives only inside .formic-matters/ at the repository root; the framework's own repository is the framework's home, its layout at root — not a choosable form. |
| `m0015` | spec | formic-matters, process, tooling | [Agent instructions file](m0015-agent-instructions.md) | A root CLAUDE.md distilling the standing rulings into the one channel that reaches every agent session before it reads anything else; it distills the doctrine and never overrides it. |

## Ordering

`implements` names the spec a matter serves; `depends_on` constrains execution order.

| Matter | Implements | Depends on |
|---|---|---|
| `m0006` | m0001 | m0008 |
| `m0007` | m0001 | m0008 |
| `m0008` | m0001 | — |
| `m0010` | m0001 | m0008 |
| `m0011` | m0001 | — |
| `m0012` | m0001 | m0001 |
| `m0013` | m0001 | — |
| `m0014` | m0001 | — |
| `m0015` | m0001 | — |
| `m0016` | m0001 | — |
| `m0017` | m0001 | — |
