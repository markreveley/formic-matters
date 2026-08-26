# formic-matters

The home of **Formic Matters**, the matter framework — born as the
development process for
[beatcode](https://github.com/markreveley/beatcode), kept out of the
instrument's own repo so the two sets of concerns don't mix, and
generalized into a consumable framework on the operator's rulings in
the
[2026-08-25 review](threads/2026-08-25-doctrine-operator-review.md).
The framework is self-hosting: changes to it are matters in this
repository's own collection.

Every change — to a governed system or to the framework itself — is
proposed as a **matter**, vetted, and ratified by the operator before
it is made. The normative definition is
[`doctrine/matters.md`](doctrine/matters.md); the collection is
[`matters/`](matters/index.md).

The repository is the record: vetting rounds live on the matters,
operator rulings arrive as committed file edits or as session
exchanges exported into `threads/`, verification evidence in `runs/`.
GitHub is transport and merge mechanics; its comment surface is unused.

**The renames and the split, stated and dated (spec §9.4).** This
repository was founded as `beatcode-dev` on 2026-08-24 and renamed to
`formic-matters` by the operator on 2026-08-26 — step 1 of
[m0012](matters/m0012-formic-matters-split.md), the split matter.
m0012 executed on 2026-08-26: the beatcode-facing matters —
m0002–m0005 and m0009 — moved to the first consumer installation,
[markreveley/beatcode-dev](https://github.com/markreveley/beatcode-dev)
(a new repository under the founding name), and their vacated IDs are
never reused here (spec §12). The owner account was also renamed on
2026-08-26, and every repository reference in this tree was rewritten
to the current names in the same execution, on operator ruling — the
pre-rename text is in git history, and m0012's execution record
itemizes the sweep.

**Status:** the specification is **normative** —
[m0001](matters/m0001-matter-system.md) was ratified by the operator
and executed on 2026-08-26, at commit
`85fe4511326a30516ed2bf86a2e2a2b9d05c3d25` (spec §6, §14).
[m0012](matters/m0012-formic-matters-split.md), the split into
framework and consumer repositories, was ratified in the same act and
executed on 2026-08-26.
[m0013](matters/m0013-bootstrap-defaults-record.md), the bootstrap
defaults record, is ratified. The collection here is the framework's
own: m0001, m0006–m0008, m0010–m0013.
This is the second bootstrap; the first was audited
and archived unmerged (PR #1). Nothing in it was ratified, and this
bundle was re-authored rather than derived — but by an agent that had
read the archive, and passages of the archived text survive here
([runs/2026-08-25-vetting-round-3.md](runs/2026-08-25-vetting-round-3.md)).
All three rulings sources are exported into
[`threads/`](threads/2026-08-24-matter-system.md) — the design session,
the adjudication session, and the
[operator review](threads/2026-08-25-doctrine-operator-review.md) — so
every row of [m0001](matters/m0001-matter-system.md)'s rulings ledger
cites the turn it came from, in a file in this tree.

## Layout

```
doctrine/matters.md     the Formic Matters specification
matters/                flat collection, one file per matter
matters/index.md        derived listing — regenerate, never hand-edit
threads/                verbatim session exports; primary sources
runs/                   append-only verification records
tools/                  interim scripts; the real tooling is m0008
```

The collection is markdown with YAML frontmatter — OKF v0.2 as a
documented dialect (doctrine §12): readable with no tooling, links as
plain relative paths, one concept per file.

## Running a vetting round

A round is a fresh session prompted against this branch. The prompt is
recorded verbatim in the adjudication thread
([thread:646-671](threads/2026-08-24-audit-and-adjudication.md)). It
stands amended in three ways, each stated here rather than folded into
"one line":

- **The isolation line is retired:** "The first attempt is archived
  unmerged (PR #1): do not read it, its matters, or its thread." That
  line kept a fresh reviewer from anchoring on the archived attempt
  while this one was being authored — the risk was re-*authoring*
  against old text. Authoring is finished; what is left is reading.
  Meanwhile the line cost two rounds real coverage: round 1's V1 and
  round 2's W2 both report ledger rows a reviewer could not check,
  because the session that ruled them was out of reach. The archive is
  readable — PR #1, its matters, and its design session, now in
  `threads/`.
- **Step 1's fidelity check covers every thread in `threads/`** —
  three now, the
  [2026-08-25 operator review](threads/2026-08-25-doctrine-operator-review.md)
  included — not the one thread the recorded prompt names.
- **The branch the recorded prompt names is historical** — it is
  round 1's branch; a round runs against the current head of the m0001
  lineage.

What the retired line was standing in for survives as the narrower
rule: review the text as it stands here; never carry archived wording
into this tree.

## Ratifying, and checking a ratification

Ratification is an act over exact text at an exact commit (spec §6).
The commit and hash are recorded *after* the act, from the commit
you name — a pin offered in advance is not the record, because the text
moves under it whenever the matter is revised.

To ratify, in your checkout:

```
git pull                                  # the text you are about to read
git rev-parse HEAD                        # the commit you are reading at
$EDITOR doctrine/matters.md               # read it
```

then state ratification naming that commit. The recording agent writes
`verified`, `ratified_commit` and `ratified_sha256` onto the matter.

To check a ratification afterwards — or any hash an agent quotes — three
commands, none of which require trusting the agent:

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
ratification — which is what m0007 exists to catch mechanically. For a
matter rather than the specification, the hash covers the ratified
region (body minus frontmatter, `## Vetting` and `## Execution`), so
compare against that region, not the whole file.
