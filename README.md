# beatcode-dev

The development process for [beatcode](https://github.com/ob6to8/beatcode),
kept out of the instrument's own repo so the two sets of concerns don't mix.

Every change to beatcode — feature, fix, refactor, or spec — is proposed
here as a **matter**, vetted, and ratified by the operator before any code
is written. The doctrine is [`doctrine/matters.md`](doctrine/matters.md);
the collection is [`matters/`](matters/index.md).

Scope is beatcode, deliberately. If a general framework emerges later this
repo would consume it, but stays its own repo.

## Layout

```
doctrine/matters.md     the normative process definition
matters/                flat collection, one file per matter
matters/index.md        derived listing — regenerate, never hand-edit
threads/                verbatim transcripts of the sessions behind matters
tools/                  interim scripts; the real tooling is m0008
```

The collection is an [OKF](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
bundle: markdown files with YAML frontmatter, one concept per file,
links as ordinary markdown, no required tooling to read it.
