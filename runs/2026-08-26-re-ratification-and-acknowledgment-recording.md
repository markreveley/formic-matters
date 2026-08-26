# Run — recording: m0001 doctrine re-ratification; consumer m0010 acknowledgment

Append-only verification record (spec §9.1). Never edited; a
superseding run is a new file. Filed for the recording of two operator
acts stated in one turn after the PR #4 merge
([execution thread](../threads/2026-08-26-m0012-execution.md), R4–R6):
the §6 re-ratification of the corrected `doctrine/matters.md`
("2 - ratified", R5), and the §11 acknowledgment of the consumer
installation's m0010 ("I acknowledge m0010 at commit c6d4a3c", R6).
This run is the mechanical half — pin computation and stability.

## Claims tested

- The merge is a merge commit and the pin anchor survives it: PR #4's
  merge commit has two parents, and the m0012 execution's sweep commit
  is reachable from `main`.
- The re-ratified document is the text the operator was shown:
  `doctrine/matters.md` at the merge commit hashes to the candidate
  value declared in the m0012 execution record and its commit
  messages.
- The acknowledged m0010 pin is reproducible: the §6 retroactive
  regime (body after the frontmatter's closing `---`, `## Retroactive`
  and `## Execution` included, no `## Vetting` present, sha256 over
  UTF-8) over m0010 at the acknowledged commit.
- The recordings move no other pinned byte: m0012 and m0013 region
  pins still match at `main`; both indexes regenerate byte-identically
  with the state changes.

## Environment

- OS: Linux 6.18.44-fc-v21, x86_64 (remote agent container)
- bash 5.2.21(1)-release; git 2.43.0; GNU coreutils 9.4
  (`sha256sum`); Python 3.11.15, PyYAML 6.0.1
- Framework: `markreveley/formic-matters`, `main` at
  `97854b884a9af1a82b5b881560883a8264c6474f` — the tree verified is
  this recording's, in which this run file lands
- Consumer: `markreveley/beatcode-dev`, `main` at
  `c6d4a3c4b29bfb1de4bd5aa7fe2e1f9b315c0038` — the acknowledged
  commit; the acknowledgment recording lands on its child

## Commands and results

1. **Merge shape and reachability:**

   ```
   git log --format='%H %P' -1 origin/main
   git merge-base --is-ancestor 70db408d9148667097b2cd052853d37d01e9f3fa origin/main
   ```

   Expected: two parents; ancestor check succeeds. **Observed:
   `97854b88…` with parents `6982afce…` and `e5393369…`; the sweep
   commit is an ancestor of `main` — every pin anchored on it is
   served from `main`'s history permanently.**

2. **Re-ratified doctrine:**

   ```
   git show 97854b884a9af1a82b5b881560883a8264c6474f:doctrine/matters.md | sha256sum
   sha256sum doctrine/matters.md
   ```

   Expected: both equal the declared candidate. **Observed: both
   `9fb1f925f37c3533ffff7caba7c1094f5631e098503e06ac569841d0ef1f4c7d`.**
   Statement received 2026-08-26; recorded at 2026-08-26T18:33:07Z
   into m0001's frontmatter, the superseded pin preserved in its
   re-ratification entry.

3. **m0010 acknowledgment pin, at the named commit** (in the consumer
   clone):

   ```python
   import hashlib, subprocess
   t = subprocess.run(["git", "show",
       "c6d4a3c4b29bfb1de4bd5aa7fe2e1f9b315c0038:matters/m0010-framework-installation.md"],
       capture_output=True, text=True, check=True).stdout
   body = t[t.index("\n---\n", 3) + 5:]
   print(hashlib.sha256(body.encode("utf-8")).hexdigest())
   ```

   **Observed:
   `432ae6c1dbcc3de355dc5eb7929709a08ee9736359c4a1ed2d77ec06082ac638`**
   — recorded into m0010's frontmatter with the acknowledgment;
   regime: retroactive (§6), stated here per m0007's
   name-the-regime requirement.

4. **Stability.** m0012 and m0013 region pins recomputed at `main`
   under the standing rule: **both MATCH** (`21492653…54a747`,
   `b0f4810e…12cec5`). `python3 tools/gen-index.py` twice in each
   repository: **byte-identical both times** — framework 8 matters
   (m0001 and m0012 `executed`, m0013 `ratified`, five `proposed`);
   consumer 6 matters (m0010 `executed` after the recording, five
   `proposed`).

## Verdict

All four claims hold. Both acts are recorded with their pins, each
independently recomputable from its named commit; the superseded
m0001 pin remains preserved in prose because the consumer's installed
copy still verifies against it.

- Date: 2026-08-26
- Actor: claude-code/2026-08-26, the recording agent (also the m0012
  execution's dev agent; the pins are the independence mechanism).
  Thread:
  [2026-08-26-m0012-execution](../threads/2026-08-26-m0012-execution.md)
