# Run — vetting round 2: mechanical re-checks of the round 1 response

Append-only verification record (doctrine §9.1). Never edited; a
superseding run is a new file. Filed under §9.1 in place of the inline
evidence round 1 used, per the deviation that round recorded
([m0001](../matters/m0001-matter-system.md), round 1 response).

## Claims tested

Each is a claim the round 1 response makes about what it applied, or a
tree-wide invariant the response could have disturbed.

- The §9.4 quote on [m0004](../matters/m0004-track-length-index-count.md)
  is byte-identical to `SPEC.md` at `fa17627` (round 1's nit; response:
  "corrected to match `SPEC.md:757` byte for byte").
- [m0003](../matters/m0003-spec-order-rules-lack-mechanism.md)'s revised
  §1.4 characterization is accurate: ten semicolon-joined determinism
  rules, of which exactly two carry their reason inline (round 1 nit 1).
- m0003's pipeline diagram pointer is accurate: `SPEC.md:38` carries the
  full clock annotations (round 1 nit 2).
- `tools/gen-index.py` still regenerates `matters/index.md`
  byte-identically at `981b2a6` (the response's apply plan said "index
  regenerated"; the commit contains no index diff).
- Every relative link in the tree resolves and none uses the
  leading-slash form, after the response added six ledger rows and
  several cross-references.
- The ratification pin quoted to the operator in the thread
  (`doctrine/matters.md` at `44d6be0`, sha256 `034d46bf…c7f0ef`,
  [thread:627](../threads/2026-08-24-audit-and-adjudication.md)) no
  longer describes the doctrine at `981b2a6`.

## Environment

- OS: Linux 6.18.44-fc-v21, x86_64 (remote agent container)
- bash 5.2.21(1)-release; GNU coreutils 9.4 (`sha256sum`); GNU
  diffutils 3.10 (`diff`); GNU sed 4.9; GNU grep 3.11; mawk 1.3.4
  20240123; git 2.43.0
- Python 3.11.15 (`tools/gen-index.py`; also the link checker below)
- Repos: `markreveley/formic-matters` at `981b2a6` (branch
  `claude/beatcode-pr1-audit-1t400g`), working tree clean;
  `markreveley/beatcode` cloned fresh, `fa17627`
  (`fa17627c3f797872188c76e14e22059f2dece741`), seed `91188a5`
  (`91188a514585345e5b98d3a33560c03b2507b276`)
- `$BC` below is the beatcode clone; commands run from the
  beatcode-dev worktree root. No beatcode build was run this round —
  round 1's render reproduction was not re-executed and is not
  re-asserted here.

## Commands and results

1. m0004's verbatim quote against the source:

   ```
   diff <(sed -n '25,27p' matters/m0004-track-length-index-count.md) \
        <(git -C $BC show fa17627:SPEC.md | sed -n '757,759p')
   ```

   Expected: no output (identical). **Observed: no output.** The
   pre-response text at `7022aad` differs in one byte (`last` followed
   by three spaces, SPEC.md has two):

   ```
   git show 7022aad:matters/m0004-track-length-index-count.md | sed -n '25p' | cat -A
   → last   = highest frame index touched$
   git -C $BC show fa17627:SPEC.md | sed -n '757p' | cat -A
   → last  = highest frame index touched$
   ```

2. SPEC.md §1.4, split on its clause separator:

   ```
   git -C $BC show fa17627:SPEC.md | sed -n '/### 1.4/,/^---$/p' \
     | tail -n +3 | tr '\n' ' ' | tr ';' '\n' | sed '/^ *$/d' | nl
   ```

   Expected: ten clauses, two of them carrying a parenthetical reason.
   **Observed: ten clauses.** Clause 1 (libm — "lower to platform libm
   and vary by platform") and clause 6 (`HashMap` — "iteration order is
   randomized per process") carry reasons; clauses 2–5 and 7–10 are
   bare. m0003's revised "mostly without … (two of the ten — the libm
   and `HashMap` rules — carry their reason inline)" is exact.

3. The full pipeline line:

   ```
   git -C $BC show fa17627:SPEC.md | sed -n '38p'
   → grid (exact rationals) → swing → time-lane → humanize → performed_s (f64, clamped ≥ 0)
   ```

   Expected: annotations absent from m0003's abbreviated diagram.
   **Observed: as above**; m0003's new parenthetical ("abbreviated
   here — `SPEC.md:38` carries the full clock annotations") is accurate.

4. Index regeneration:

   ```
   cp matters/index.md /tmp/idx.bak && python3 tools/gen-index.py \
     && diff /tmp/idx.bak matters/index.md
   ```

   Expected: `11 matters indexed`, then no diff. **Observed: `11
   matters indexed`, no diff — byte-identical.** (Consistent: the
   response changed no frontmatter.)

5. Link integrity — every markdown link in every tracked `.md`,
   excluding `http(s):` targets and bare fragments, resolved relative
   to its containing file. Run against the tree at `981b2a6`, before
   this record was added:

   ```
   python3 - <<'PY'
   import re, os, glob
   bad, total = [], 0
   for f in glob.glob('**/*.md', recursive=True):
       base = os.path.dirname(f)
       for m in re.finditer(r'\[[^\]]*\]\(([^)]+)\)', open(f).read()):
           t = m.group(1)
           if t.startswith('http') or t.startswith('#'):
               continue
           total += 1
           if not os.path.exists(os.path.normpath(os.path.join(base, t.split('#')[0]))):
               bad.append((f, t))
           if t.startswith('/'):
               bad.append((f, t, 'leading-slash'))
   print(total, bad or 'none')
   PY
   ```

   Expected: all resolve, none leading-slash. **Observed: `58 none`.**
   Round 1 counted 52 at `44d6be0`; the six added are the response's
   new cross-references.

6. The doctrine's whole-file hash across the range (§6 hashes the
   doctrine whole-file for m0001):

   ```
   for c in 44d6be0 7022aad 1347af3 981b2a6; do
     git show $c:doctrine/matters.md | sha256sum; done
   ```

   Expected: unchanged across round 1 (append-only), changed by the
   response. **Observed:**

   | commit | sha256 |
   |---|---|
   | `44d6be0` | `034d46bfe9f1de86b3f56723d70ac56af682a4e5a6445726b168ad2231c7f0ef` |
   | `7022aad` | `034d46bf…c7f0ef` (identical) |
   | `1347af3` | `034d46bf…c7f0ef` (identical) |
   | `981b2a6` | `67fada5ca71f9f41a81fbc8a86163ee034458041ee364a04db52d5327227bad0` |

   The first value is the pin the operator was handed in-thread
   ("ready when you are", thread:627); it is superseded at `981b2a6`.

## Verdict

All six claims confirmed. The two matter-local text fixes on m0003 and
m0004 are accurate against `SPEC.md` at `fa17627`; the derived index
and the link graph survive the response commit intact; and the
ratification pin quoted in the thread is stale for the doctrine as it
now stands.

- Date: 2026-08-25
- Actor: claude-code/2026-08-25 (vetting round 2, fresh instance;
  thread:
  [2026-08-24-audit-and-adjudication](../threads/2026-08-24-audit-and-adjudication.md))
