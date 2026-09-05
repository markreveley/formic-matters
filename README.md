# Restate to Ratify (RTR)

The home of **Restate to Ratify** — short form **RTR** — the matter
framework, named for its central act: the operator's own-words
restatement of a proposed change, verified against the change's exact
text, is what ratifies it. The framework was born as one project's
development process, generalized and named **Formic Matters** on the
operator's rulings in the
[2026-08-25 review](threads/2026-08-25-doctrine-operator-review.md),
and renamed Restate to Ratify on the operator's direction of
2026-08-28 — the naming session is exported at
[threads/2026-08-28-restate-to-ratify.md](threads/2026-08-28-restate-to-ratify.md),
and the in-text rename is carried by
[m0022](matters/m0022-rename-to-rtr.md), proposed. The framework is
self-hosting: changes to it are matters in this repository's own
collection, put through its own process.

Every change — to a governed system or to the framework itself — is
proposed as a **matter**, reviewed, and ratified by the operator
before it is made. The normative definition is
[`doctrine/matters.md`](doctrine/matters.md); the collection is
[`matters/`](matters/index.md); the standing rules every agent
session reads first are in [`CLAUDE.md`](CLAUDE.md). The doctrine
governs; this README explains. Where the two ever disagree, this
document is the defect.

The repository is the record. The operator's channel is the tree,
reached two ways: file edits committed and pushed — including
**in-document review**, `->[…]` comments written into an authored
file, answered by an agent that exports the exchange as a thread and
removes the markers — or a session exchange with an agent, which
enters the record when the session is exported verbatim into
[`threads/`](threads/). Verification evidence lives in
[`runs/`](runs/). GitHub is transport and merge mechanics: a pull
request is a diff boundary and a gate, its body is a one-line
pointer, and its comment surface is unused (doctrine §8, “Where
discourse lives”).

## Why "restate to ratify"

The ratification mechanism
([m0017](matters/m0017-operator-authored-ratification.md)) is named
for its rule: no ratification without a restatement. A restatement is
the operator's account, in the operator's own words, of what the
matter does and why — bounded by the matter, adding nothing the matter
does not say, diffed against it by agent review, and finished by the
recording commit that ratifies. The operator authors the account;
agents verify it against the matter text. The first bootstrap shows
why the roles sit that way: a document was marked ratified on the
strength of an agent summary that misdescribed the committed text
(doctrine §14, “The bootstrap”). The zero-additive bound cuts the
other way too: a restatement that contains something true the matter
fails to say has found an underspecified matter, and that content
enters the matter by revision — ratification is never the channel by
which new content enters the record.

The pattern has precedents wherever one party's understanding must be
verified before an act takes effect:

- **Agency law.** Ratification is a principal's adoption of an act
  performed by an agent, and it is valid only with knowledge of the
  material facts. Restate-to-ratify operationalizes the knowledge
  requirement: the restatement is that knowledge, demonstrated on the
  record at the moment of adoption.
- **Read-back protocols.** Aviation read-back/hear-back, clinical
  teach-back, the plea colloquy: the accepting party restates, the
  counterparty evaluates, and the restatement goes on the record. A
  read-back is itself zero-additive — a pilot who adds to a clearance
  has made an error, not a contribution. The framework is that
  protocol for human–agent governance, with the restatement pinned by
  commit and hash.

The record accretes three provenance layers: **text provenance** — the
pinned commit and hash: what exactly was accepted; **ruling
provenance** — threads and the rulings ledgers: what was decided along
the way; and **operator-comprehension provenance** — the restatement:
what the decider understood and chose to accept, hashed with the text
it accepts.

## How a matter is ratified

Ratification is the operator's act alone, over exact text at an exact
commit (doctrine §6, “Vetting and ratification”). Two forms of the act
exist in this tree, and the status section below says which is in
force:

- **The verbal act — ratified doctrine today.** The operator reads
  the matter as it stands at a commit and states ratification naming
  that commit. A recording agent then writes the pin onto the matter.
- **Restate to ratify — proposed by m0017, the mechanism the
  framework is named for.** Step by step:
  1. The operator writes the restatement — the only text the operator
     authors in the protocol.
  2. The operator, or an agent transcribing the operator's recorded
     wording verbatim, commits it to the matter as a dated draft
     under `## Operator ratification`. Agents never compose or alter
     it.
  3. A fresh agent — one that has not worked on the matter — compares
     the restatement to the matter text, claim by claim. It fails on a
     claim the matter does not anchor, a material omission, or
     quotation and line-by-line paraphrase, which interpret nothing.
  4. If the comparison fails, ratification does not occur; the agent
     reports each failure to the operator, who either rewords the
     restatement or revises the underspecified matter and restates
     over the revised text. The protocol restarts at step 3 with a
     fresh agent.
  5. If the comparison passes, ratification is complete at that
     moment. The same agent, in the same session, makes one commit
     that records the verification, marks the draft ratified, and
     writes the pin. Nothing else changes in that commit.

Under either form, **the pin follows the act**: `ratified_commit` and
`ratified_sha256` are recorded after the operator's act, from the
commit the operator read, never offered in advance. The hash covers
the matter's **ratified region** — the body minus the frontmatter and
the append-only `## Vetting` and `## Execution` sections; under
m0017 the `## Operator ratification` section sits inside that region,
so one number covers the contract and the restatement together. m0001
is special: its pin covers the whole doctrine file.

## The lifecycle, as dependency management

A ratified matter is a published package version. Its pin — the
recorded commit and content hash — is the version identifier: exact,
immutable, checkable forever. Until ratification a matter is
unpublished working text: it is revised freely on the operator's
direction, and nothing may depend on it.

Publication is what creates obligations. Once ratified, a matter can
become a dependency — of doctrine amendments, of other matters,
eventually of code. So ratified text is never edited in place and
never un-published:

- To change it, publish a new version: re-ratification, a fresh pin
  recorded beside the old one.
- To dispute it, yank it: the `challenged` state
  ([m0028](matters/m0028-challenged-state.md), proposed). Existing
  dependents are put on notice, new dependents are stopped, and the
  record of what was law stays intact. Ratified doctrine today still
  sends a disputed matter back to `proposed`; m0028 retires that.
- To replace it, supersede it: a new matter takes over, and the old
  one keeps its history forever (doctrine §5, “Supersession,
  splitting, and conflict”).

The `sources` list ([m0024](matters/m0024-declared-sources.md),
proposed) is the dependency manifest: each matter declares what its
reasoning rests on, and only published (ratified) text or append-only
evidence qualifies. The execution-order gate over `depends_on`
(doctrine §7, “Composition — no containers”) is the resolver: nothing
builds until everything it depends on has shipped. Reviewers enforce
the gate today; the validator will once it exists
([m0008](matters/m0008-matter-tooling.md)).

## Status

Stated as of 2026-09-05. The state of every matter is
[`matters/index.md`](matters/index.md), derived and regenerated,
never hand-edited; the operational projection for the next session is
[`handoff.md`](handoff.md), advisory and never authoritative.

- **The specification is normative.**
  [m0001](matters/m0001-matter-system.md) was ratified and executed on
  2026-08-26, then re-ratified over amendments; its current pin is
  commit `d800ee8a928d220bf7e27cf547d856ac38f4c784`, ratified
  2026-08-27, with every earlier pin preserved on the matter. The
  doctrine's own header still reads **Formic Matters**: the in-text
  rename lands only when m0022 executes and m0001 is re-ratified over
  the amendment.
- **Executed:** m0001; [m0012](matters/m0012-formic-matters-split.md),
  the split; [m0014](matters/m0014-contained-installation-layout.md),
  the contained installation layout;
  [m0015](matters/m0015-agent-instructions.md), the agent
  instructions. **Ratified:**
  [m0013](matters/m0013-bootstrap-defaults-record.md), the bootstrap
  defaults record.
- **Proposed, and governing nothing:** everything else, m0006 through
  m0030. Among them the restate-to-ratify mechanism (m0017), the
  rename (m0022), declared sources (m0024), the legibility standard
  and glossary ([m0026](matters/m0026-legibility-standard.md)),
  records beginning at the gate
  ([m0027](matters/m0027-records-begin-at-the-gate.md)), the
  challenged state (m0028), and the error log
  ([m0030](matters/m0030-error-log.md)). The operator's direction of
  2026-08-29 sets the order: m0026 first, then m0024 with
  [m0025](matters/m0025-doctrine-enforcement-voice.md), then m0027,
  then m0017 and the rest
  ([thread](threads/2026-08-29-complexity-escape-and-working-text.md)).
- **The mechanism in force** is the verbal act of doctrine §6,
  “Vetting and ratification.” m0017's plan has restate to ratify
  govern every prospective ratification from its own execution
  onward; until then it governs nothing.
- **Consumers.** One consumer installation exists, from the
  2026-08-26 split. The operator's stated intent
  ([2026-08-28](threads/2026-08-28-restate-to-ratify.md)) is no
  further consumers yet and no code until ratification means
  something: nothing has been built under the framework so far, and
  that is deliberate.

## The renames and the split, stated and dated

Doctrine §9.4, “Immutability,” requires mutable state to be dated;
this is the dated record of the names this tree has carried.

- **2026-08-24** — founded as `beatcode-dev`, the development process
  for [beatcode](https://github.com/markreveley/beatcode), kept out of
  that instrument's own repository so the two sets of concerns would
  not mix.
- **2026-08-26** — renamed to `formic-matters` by the operator, step 1
  of [m0012](matters/m0012-formic-matters-split.md), the split matter.
  m0012 executed the same day: the consumer-facing matters —
  m0002–m0005 and m0009 — moved to the first consumer installation,
  [markreveley/beatcode-dev](https://github.com/markreveley/beatcode-dev),
  a new repository under the founding name, and their vacated IDs are
  never reused here (doctrine §12, “Storage and format”). The owner
  account was renamed the same day, and every repository reference in
  this tree was rewritten to the current names in that execution, on
  operator ruling; m0012's execution record itemizes the sweep.
- **2026-08-28** — the operator chose the name Restate to Ratify,
  short form RTR, in the
  [naming session](threads/2026-08-28-restate-to-ratify.md), and
  [m0022](matters/m0022-rename-to-rtr.md) was filed to carry it.
- **2026-08-29** — the repository was renamed to `rtr` by the
  operator, platform-side, and confirmed in session
  ([thread](threads/2026-08-29-complexity-escape-and-working-text.md)).
  GitHub redirects the old name, so pinned absolute URLs keep
  resolving; threads and runs are never rewritten, and their old-name
  URLs stand as historical record. The rest of m0022 — the doctrine's
  title, `CLAUDE.md`, the `formic-matters` tag, the consumer
  container directory (`.formic-matters/` today; `.rtr/` is the
  choice before the operator) — waits on its ratification.

This is the second bootstrap; the first was audited and archived
unmerged (PR #1). Nothing in it was ratified, and this bundle was
re-authored rather than derived — by an agent that had read the
archive, and passages of the archived text survive here
([runs/2026-08-25-vetting-round-3.md](runs/2026-08-25-vetting-round-3.md)).
The rulings sources behind the doctrine are all exported into
[`threads/`](threads/) — the
[design session](threads/2026-08-24-matter-system.md), the
[adjudication session](threads/2026-08-24-audit-and-adjudication.md),
and the [operator review](threads/2026-08-25-doctrine-operator-review.md)
— so every row of m0001's rulings ledger cites the turn it came from,
in a file in this tree.

## Layout

```
doctrine/matters.md     the specification — normative
matters/                flat collection, one file per matter
matters/index.md        derived listing — regenerate, never hand-edit
threads/                verbatim session exports; primary sources
runs/                   append-only verification records
handoff.md              the next session's starting point; advisory
CLAUDE.md               standing rules distilled for agent sessions
tools/                  interim scripts; the real tooling is m0008
```

The collection is markdown with YAML frontmatter — OKF v0.2 as a
documented dialect (doctrine §12, “Storage and format”): readable with
no tooling, links as plain relative paths, one concept per file.
Consumers install the framework only inside a containing directory at
their repository root; this repository is the framework's home, its
layout at root, not an installed copy.

Conventions every commit follows: a `Matter: mNNNN` trailer, a
matter-prefixed branch name and pull-request title, and merge by merge
commit — never a squash, because pins reference branch commits.

## Review, today

While a matter is `proposed` it is working text. Under the operator's
direction of 2026-08-29 — the rule
[m0027](matters/m0027-records-begin-at-the-gate.md) proposes —
review is applied as edits: a finding the operator accepts becomes a
revision, one the operator declines stays in the thread, and no
`## Vetting` entry accretes before the ratification gate. The
operator's chosen review channel is doctrine §8's in-document review:
`->[…]` comments committed to the branch under review; the responding
agent answers each, removes the markers in its response commit, and
exports the exchange as a thread.

The bootstrap's three vetting rounds ran from the prompt recorded in
the adjudication thread
([thread:646-671](threads/2026-08-24-audit-and-adjudication.md)); the
prompt's later amendments are recorded in this README as it stood at
commit `b8af6799aaf40d94339d937e3371228d744f0dc5`. One rule from that
period survives: review the text as it stands here; never carry
archived wording into this tree.

## Checking a ratification

Three commands, none of which require trusting the agent that recorded
the pin — for m0001, whose pin covers the whole doctrine file:

```
# does the recorded hash actually belong to the recorded commit?
git show <ratified_commit>:doctrine/matters.md | sha256sum

# is the file in front of me the file that was ratified?
sha256sum doctrine/matters.md

# what changed since, if anything?
git diff <ratified_commit>..HEAD -- doctrine/matters.md
```

The first two agreeing means the pin is honest and current. The first
agreeing while the second differs means the text has moved since
ratification — which is what
[m0007](matters/m0007-ratification-content-hash.md) exists to catch
mechanically. For any other matter, the hash covers the ratified
region rather than the whole file, so compare against that region:
the body minus the frontmatter and the append-only `## Vetting` and
`## Execution` sections.
