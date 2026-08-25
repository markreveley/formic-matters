# beatcode-dev

The development process for [beatcode](https://github.com/ob6to8/beatcode),
kept out of the instrument's own repo so the two sets of concerns don't
mix. The system is self-hosting: changes to this repository go through
it too.

Every change — to beatcode or to this process — is proposed as a
**matter**, vetted, and ratified by the operator before it is made. The
normative definition is [`doctrine/matters.md`](doctrine/matters.md);
the collection is [`matters/`](matters/index.md).

The repository is the record: vetting rounds live on the matters,
operator rulings arrive as committed file edits, session transcripts
live in `threads/`, verification evidence in `runs/`. GitHub is
transport and merge mechanics; its comment surface is unused.

**Status:** awaiting ratification of
[m0001](matters/m0001-matter-system.md) (doctrine §6, §14). This is the
second bootstrap; the first was audited and archived unmerged (PR #1).
Nothing in it was ratified, and this bundle was re-authored rather than
derived — but by an agent that had read the archive, and passages of the
archived text survive here
([runs/2026-08-25-vetting-round-3.md](runs/2026-08-25-vetting-round-3.md)).
Its design session is exported into
[`threads/`](threads/2026-08-24-matter-system.md), so every row of
[m0001](matters/m0001-matter-system.md)'s rulings ledger cites the turn
it came from, in a file in this tree.

## Layout

```
doctrine/matters.md     the normative process definition
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
([thread:646-671](threads/2026-08-24-audit-and-adjudication.md)), and
it stands except for one line, now retired:

> The first attempt is archived unmerged (PR #1): do not read it, its
> matters, or its thread.

That line kept a fresh reviewer from anchoring on the archived attempt
while this one was being authored — the risk was re-*authoring* against
old text. Authoring is finished; what is left is reading. Meanwhile the
line cost two rounds real coverage: round 1's V1 and round 2's W2 both
report ledger rows a reviewer could not check, because the session that
ruled them was out of reach. It is now in `threads/`, so a reviewer
should read the archive — PR #1, its matters, and both threads — and
the fidelity check in step 1 covers both threads rather than one.

What the retired line was standing in for survives as the narrower
rule: review the text as it stands here; never carry archived wording
into this tree.

## Ratifying, and checking a ratification

Ratification is an act over exact text at an exact commit (doctrine
§6). The commit and hash are recorded *after* the act, from the commit
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
matter rather than the doctrine, the hash covers the ratified region
(body minus frontmatter, `## Vetting` and `## Execution`), so compare
against that region, not the whole file.
