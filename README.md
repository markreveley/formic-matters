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
second bootstrap; the first was audited and archived unmerged (PR #1),
and nothing here depends on it.

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
