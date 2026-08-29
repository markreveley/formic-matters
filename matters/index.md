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
| `m0017` | spec | formic-matters, process, ratification, integrity | [Restate to ratify — operator-authored restatements](m0017-operator-authored-ratification.md) | Ratification is an operator-authored restatement committed to the matter; a fresh agent verifies it against the matter text, and a passing verification completes the act, which the agent records with the exact-text pin. |
| `m0018` | spec | formic-matters, process, documentation, review | [Doctrine citations include section headings](m0018-doctrine-heading-citations.md) | Every authored citation to a numbered doctrine section carries the section's exact heading, so the operator can understand the reference without cross-referencing the specification. |
| `m0019` | spec | formic-matters, process, review, execution, provenance | [Fresh contexts and durable handoffs](m0019-fresh-context-durable-handoffs.md) | Vetting and execution begin across explicit context boundaries, while a mutable, non-authoritative handoff keeps the repository's current operational projection available to each new context. |
| `m0020` | fix | formic-matters, process, execution, authority, handoff | [Referential handoff launches and delegated authority](m0020-referential-handoff-authority.md) | Let an operator adopt one explicit handoff action by reference while distinguishing operator-only lifecycle acts from agent-performed repository mechanics. |
| `m0021` | spec | formic-matters, documentation, provenance | [README carries the naming rationale and lineage](m0021-readme-naming-lineage.md) | The README gains an expository section on the restate-to-ratify name — its rule, its agency-law and read-back lineage, and the three provenance layers the record accretes. |
| `m0022` | spec | formic-matters, process, naming, topology | [Rename the framework to Restate to Ratify (RTR)](m0022-rename-to-rtr.md) | The framework takes the name of its central act — Restate to Ratify, short form RTR — and the doctrine, agent instructions, README, container-directory convention, and repository carry the rename. |
| `m0023` | feature | formic-matters, process, integrity, ratification | [Restatement integrity analysis against the thread corpus](m0023-restatement-integrity-analysis.md) | An advisory integrity check on operator restatements — LLM-as-judge and consistency analysis against the operator's verbatim turns in threads/ — that emits vetting findings and can never gate or grant ratification. |
| `m0024` | spec | formic-matters, process, provenance, integrity | [Declared sources — authored matters carry their provenance](m0024-declared-sources.md) | Every authored or revised matter declares the sources its reasoning rests on in a sources frontmatter list, and at the ratification gate every declared source is ratified text or append-only evidence — never a proposed matter. |
| `m0025` | spec | formic-matters, doctrine, integrity | [Doctrine stops describing unbuilt enforcement as operating](m0025-doctrine-enforcement-voice.md) | Six doctrine passages say a validator checks things today when no validator exists; each is rewritten to say who checks now and who will check once the tooling lands, so ratified text stops promising checks nobody runs. |
| `m0026` | spec | formic-matters, process, documentation, review | [Legibility standard — record text is written to its ratifier](m0026-legibility-standard.md) | Text the operator must act on — matter bodies, vetting entries, handoffs — is written in plain language with only defined terms, named actors, and a fixed entry structure; a glossary enters the doctrine. |

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
| `m0016` | m0001 | m0020, m0018 |
| `m0017` | m0001 | — |
| `m0018` | m0001 | — |
| `m0019` | m0001 | m0017, m0020 |
| `m0020` | m0001 | m0017 |
| `m0021` | m0001 | m0017 |
| `m0022` | m0001 | m0017 |
| `m0023` | m0001 | m0017 |
| `m0024` | m0001 | — |
| `m0025` | m0001 | — |
| `m0026` | m0001 | — |
