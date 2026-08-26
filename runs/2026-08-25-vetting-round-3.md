# Run — vetting round 3: fidelity against both threads, and archive text reuse

Append-only verification record (doctrine §9.1). Never edited; a
superseding run is a new file. Filed for vetting round 3 on
[m0001](../matters/m0001-matter-system.md), the first round with the
archive readable — PR #1, its matters, its branch, and both threads.

## Claims tested

1. The imported design session
   ([threads/2026-08-24-matter-system.md](../threads/2026-08-24-matter-system.md))
   is byte-identical to the copy on the archive branch, as the round 2
   response claims.
2. Every "Ruled in" citation in m0001's rulings ledger resolves to a
   non-blank turn, and each row's cited turn carries what the row says
   it carries — including the two rows the round 2 response added on
   its own initiative and the state spine's re-sourcing.
3. The tree's provenance claim — "none of its doctrine or matter text
   was reused" (doctrine:18-19, README:21-22, m0001:43-45) — measured
   against the archived text, which no prior round could read.
4. Tree-wide invariants: `tools/gen-index.py` regenerates
   `matters/index.md` byte-identically; §12 frontmatter conformance,
   §3 states, status derivation; relative-link resolution and the
   round 2 response's re-scoping of that check to authored files.
5. Append-only discipline: whether the response commit deleted any
   `## Vetting` text.

## Environment

- OS: Linux 6.18.44-fc-v21, x86_64 (remote agent container)
- bash 5.2.21(1)-release; GNU coreutils 9.4 (`sha256sum`); GNU
  diffutils 3.10 (`diff`); git 2.43.0
- Python 3.11.15; PyYAML 6.0.1; `difflib` from the standard library
- Repo: `markreveley/formic-matters`, branch
  `claude/beatcode-pr1-vetting-round-2-pbyiud` at `7357244`, parent
  `25d2e16`; archive branch `m0001-matter-system` at `c11956d`
  (= `refs/pull/1/head`, confirmed by `git ls-remote`)
- `markreveley/beatcode` was not cloned and not built. Nothing in
  `25d2e16..7357244` touches a beatcode-facing claim: the diff adds
  only response entries to m0003 and m0004 and leaves m0002 and m0005
  untouched. Rounds 1 and 2 own those verdicts; none is re-asserted
  here.

## Commands and results

### 1 · The import is the archive's file

```
git fetch origin m0001-matter-system:refs/remotes/origin/m0001-matter-system
git show c11956d:threads/2026-08-24-matter-system.md > $TMP/archive-design.md
sha256sum $TMP/archive-design.md threads/2026-08-24-matter-system.md
diff $TMP/archive-design.md threads/2026-08-24-matter-system.md
```

Expected: identical digests, empty diff. **Observed: both
`50022f1135d7f64c914d249ff093900a7b9d9b02671fdc637f92ecbaa8d9816a`;
`diff` empty.** Confirms the round 2 response's step 1 independently.

### 2 · Ledger citations — existence

The round 2 response's own checker, re-executed verbatim at `7357244`
(regex matching the citation form `design:N`, `adjudication:N` or
`thread:N`, optionally hyphen-ranged, inside a markdown link, over every
`**/*.md`, checking label/target agreement and a non-blank line at each
endpoint).

Expected: no bad citations. **Observed: `citations: 75 endpoints: 150 |
bad: none`.**

Note a discrepancy in the source being reproduced:
[runs/2026-08-25-archive-thread-import.md:84](2026-08-25-archive-thread-import.md)
records `citations: 75` from this same script, while that file's
Verdict (line 280) says "all 65 line citations resolve". 75 is the
reproducible number. Run files are never edited; recorded here.

### 3 · Ledger citations — content, row by row

Not a spot-check: all 35 rows. The ledger's `Ruled in` column was
parsed, each citation resolved into the named thread, and the cited
turn's **speaker** determined by walking back to the nearest
`## ▸ <name>` heading.

```
python3 - <<'PY'
import re
files={'design':'threads/2026-08-24-matter-system.md',
       'adjudication':'threads/2026-08-24-audit-and-adjudication.md'}
data={}
for k,v in files.items():
    L=open(v).read().split('\n'); spk=[None]*(len(L)+2); cur=None
    for i,l in enumerate(L,start=1):
        if l.startswith('## ▸ '): cur=l[5:].strip()
        spk[i]=cur
    data[k]=(L,spk)
lines=open('matters/m0001-matter-system.md').read().split('\n')
for i,l in enumerate(lines[62:100], start=63):
    if not l.startswith('|'): continue
    c=[x.strip() for x in l.strip().strip('|').split('|')]
    if len(c)<3 or c[0].startswith('---'): continue
    for th,a,b in re.findall(r'\[(design|adjudication):(\d+)(?:-(\d+))?\]', c[2]):
        L,spk=data[th]
        print(i, th, a, spk[int(a)], '::', L[int(a)-1][:200])
PY
```

Expected: every citation lands on a turn whose text supports the row.
**Observed: 35 rows, 46 citations, all resolving to non-blank turns.**
Speaker breakdown: 40 land in operator (`Mark`) turns, 6 in agent
(`Claude`) turns — the six being `adjudication:565` (Q1),
`:568` (Q2), `:571` (Q3), `:575` (Q4), `:578` (Q5), `:590` (Q9). Five
of the six are paired in the same row with the operator's answering
turn (`adjudication:601` or `:604`); one is not — row 92 cites Q3 at
`:571` with no answering turn, while sibling rows 90/91/96 cite `:601`.

Content verdicts on the rows the round's own prompt singles out:

- **Row 65, "describe, do not fix" (added by the author this round).**
  `design:146` (Mark) — "are you describing them to me or did you
  actually make these fixes? if not, stop, do not fix"; `design:287`
  (Mark) — "which i propose we roll back, and persist as issues to be
  ratified". Both operator turns, both carrying what the row says.
  Landed targets check: doctrine §1:37-39 and m0001:22-29. **Row is
  accurate.**
- **Row 68, the state spine's re-sourcing (added by the author this
  round).** `design:280` (Mark) — "poorly worded, state should be
  proposed -> ratified -> staged -> executed". Verbatim. **Accurate,
  and a genuine correction**: at `25d2e16` this row carried no marker,
  which under that preamble's "Unmarked rows are ruled in the thread
  directly" attributed it to the adjudication session, where it does
  not appear.
- **Row 77, risk tiers (W3(c)).** `design:304` (Mark) — "same thoughts
  as 4". Item 4 in the same operator turn is the content-hash deferral
  at `design:301`, and the agent's §4&5 block it answers
  (`design:371-390`) says "Feature matter. Same for tiers, lenses, dry
  rounds." **Accurate.**
- **Row 83, org/assertions.** `design:318` (Mark) raises it;
  `design:457` (Mark) is a *question* — "this is my local global
  claude.md?" — not an identification and not a withdrawal;
  `design:450` (Mark) is the standalone-repo ruling. The identification
  and the out-of-scope derivation are the **agent's**, at
  `design:467`: "So the `org/assertions` question is cross-repo by
  definition, which — per your own 'don't mix concerns across repos' —
  drops off the beatcode-scoped worklist rather than becoming
  m-something here." The next operator turn (`design:486`) is about
  repo location and memory files; the derivation is never answered.
  **Row overstates; `design:467` is uncited.** Finding X4.
- **Rows 95 and 99** rest on bare numbered agreements. Verified against
  the lists they answer: `adjudication:477` "5 - agree" answers item 5
  at `adjudication:410-412` (immutable references) ✓;
  `adjudication:481` "14 - agree" answers item 14 at
  `adjudication:449-451` (relative links acquit OKF) ✓ — *not* item 14
  of the earlier audit list at `adjudication:309-310`, which is the
  OKF-suspect turn.

### 4 · Ledger completeness against both threads

Every `## ▸ Mark` turn in both threads was extracted and read against
the ledger.

```
python3 - <<'PY'
for f in ('threads/2026-08-24-matter-system.md',
          'threads/2026-08-24-audit-and-adjudication.md'):
    cur=None
    for i,l in enumerate(open(f).read().split('\n'),start=1):
        if l.startswith('## ▸ '): cur=l[5:].strip(); continue
        if cur and cur.startswith('Mark') and l.strip() and l.strip()!='---':
            print(f, i, l)
PY
```

Expected, per m0001:51 ("Every operator proposal and ruling from the
2026-08-24 sessions"): every substantive operator turn maps to a row.
**Observed: six do not.** Enumerated in finding X5. The largest:
`design:459` — "agree to draft and execute m0001" — answering the
agent's bootstrap-exception proposal at `design:437-443`. That is the
authorization doctrine §14 rests on, and §14 is one of the two
exceptions §1 names. No row cites it.

### 5 · Archive text reuse

The claim under test appears three times in the tree, in the ratified
region of each file: doctrine:18-19 "none of its doctrine or matter
text was reused here"; README:21-22 "None of its doctrine or matter
text was reused"; m0001:43-45 "none of its doctrine or matter text was
reused". Its ancestor is the build agent's undertaking at
`adjudication:499`: "Nothing textual carries. No doctrine text, no
matter texts."

Method: whitespace-normalized character-level `difflib.SequenceMatcher`
(`autojunk=False`) between each current authored file and its
same-named counterpart at `c11956d`. Reported: total characters in
matching blocks of ≥40 characters, as a percentage of the archived
file — i.e. how much of the archived text survives into this tree.

```
for f in README.md doctrine/matters.md matters/m0001-*.md matters/m0002-*.md \
         matters/m0004-*.md matters/m0006-*.md matters/m0008-*.md \
         matters/m0010-*.md matters/m0011-*.md; do
  mkdir -p /tmp/arch/$(dirname $f); git show c11956d:$f > /tmp/arch/$f
done
python3 - <<'PY'
import difflib, re, glob, os
n=lambda t: re.sub(r'\s+',' ',t).strip()
for cur in ['README.md','doctrine/matters.md']+sorted(glob.glob('matters/m*.md')):
    arch='/tmp/arch/'+cur
    if not os.path.exists(arch): continue
    A,B=n(open(arch).read()), n(open(cur).read())
    sm=difflib.SequenceMatcher(None,A,B,autojunk=False)
    tot=sum(b.size for b in sm.get_matching_blocks() if b.size>=40)
    print(f"{cur:<48}{len(A):>7}{len(B):>7}{tot:>8}{100*tot/len(A):>7.0f}%")
PY
```

Expected, if the claim holds: no runs of authorial prose in common —
only unavoidable convergence (section names, operator wording,
technical facts quoted from `SPEC.md`).

**Observed:**

| file | archived ch | current ch | matched ≥40ch | % of archive surviving |
|---|---|---|---|---|
| `README.md` | 1087 | 4200 | 600 | 55% |
| `doctrine/matters.md` | 6984 | 19219 | 3159 | 45% |
| `matters/m0001-matter-system.md` | 2676 | 54167 | 611 | 23% |
| `matters/m0002-spec-commutativity-claim.md` | 1672 | 2277 | 664 | 40% |
| `matters/m0004-track-length-index-count.md` | 1732 | 6462 | 370 | 21% |
| `matters/m0006-review-lenses-and-dry-rounds.md` | 1870 | 2053 | 1457 | **78%** |
| `matters/m0008-matter-tooling.md` | 2629 | 6147 | 1127 | 43% |
| `matters/m0010-risk-tiers.md` | 1427 | 7909 | 1097 | **77%** |
| `matters/m0011-thread-persistence.md` | 2100 | 8298 | 401 | 19% |

Longest single shared runs, with both line numbers, all of them
authorial prose rather than fact, table scaffolding, or operator
wording:

- **315 ch** — `matters/m0006:21-25` ↔ archive `m0006:16-20`: "Today
  vetting is \"fresh agents review until the operator ratifies\"
  (doctrine §6). That terminates on operator fatigue, and fresh agents
  given the same prompt on the same document converge on the same
  findings — round three restates round one, producing the appearance
  of scrutiny rather than scrutiny."
- **276 ch** — `matters/m0010:29-34` ↔ archive `m0010:27-31`: the tier
  table's rows 1-3 plus "Derivation from path globs is mechanical".
- **264 ch** — `doctrine:46-53` ↔ archive `doctrine:20-25`: "## 2 · Type —
  immutable / Every matter has exactly one `type`, fixed for its whole
  life:" plus the first two table rows.
- **255 ch** — `doctrine:57-59` ↔ archive `doctrine:31-33`: "Type never changes. A matter that
  turns out to be the wrong type is superseded by a new one (§5), which
  keeps `type` a stable query for the life of the collection."
- **220 ch** — `matters/m0010:49-52` ↔ archive `m0010:36-39`: "A
  process that makes small changes expensive gets bypassed for small
  changes, and a bypassed process ends up covering only the work that
  was already being done carefully."
- **205 ch** — `matters/m0001:20-25` ↔ archive `m0001:19-24`: "##
  Diagnosed reason / Changes to beatcode were being identified,
  diagnosed, and applied in one unbroken motion, with no gate between
  noticing a problem and editing the repo."
- **196 ch** — `README:29-35` ↔ archive `README:14-20`: the whole `## Layout`
  block, "doctrine/matters.md the normative process definition …
  matters/index.md derived listing — regenerate, never hand-edit".
- **173 ch** — `matters/m0008:51-52` ↔ archive `m0008:33`: "Not
  mechanizable, and not to be faked: whether a diagnosis is correct,
  whether a plan is good, whether scope is right, ratification itself."
- **168 ch** — `README:1-5` ↔ archive `README:1-5`: "# beatcode-dev /
  The development process for beatcode — link elided, see the file —
  kept out of the
  instrument's own repo so the two sets of concerns don't mix."
- **139 ch** — `matters/m0001:31-33` ↔ archive `m0001:28-30`: "beatcode is a repository whose
  thesis is that behavior is pinned in advance and verified against
  frozen goldens."
- **163 ch** — `doctrine:194-197` ↔ archive `doctrine:93-97`: "…a `spec` matter defining what the
  goal *is*, plus metadata on the members: - `implements: m0001` — this
  matter serves that spec - `depends_on: [m0007, m0008]` —".
- **160 ch** — `doctrine:131-134` ↔ archive `doctrine:66-68`: "No matter reaches `ratified`
  without its type's required sections complete. / Completeness is
  therefore a checklist on the matter, not a state."

**Verdict on claim 3: the claim is false as stated.** Finding X1.

### 6 · Index regeneration, frontmatter, states, status

```
cp matters/index.md $TMP/idx.bak && python3 tools/gen-index.py && diff $TMP/idx.bak matters/index.md
git status --porcelain
```

Expected: `11 matters indexed`, no diff, clean tree.
**Observed: exactly that.**

Frontmatter checked field by field across all eleven matters against
§12's schema (subkeys of `generated`/`verified` included), plus state
membership in §3 and the §12 status derivation.

Expected: no undefined field, no state outside §3, `status` derived
everywhere. **Observed: clean.** All eleven are `state: proposed` /
`status: draft`; every timestamp is `2026-08-24T22:33:00Z`, ISO 8601
with an explicit UTC offset.

### 7 · Links, and the re-scoped check

```
python3 - <<'PY'
import re, os, glob
tot=0; bad=[]; lead=[]
for p in sorted(glob.glob('**/*.md', recursive=True)):
    txt=open(p).read()
    for m in re.finditer(r'\[([^\]]*)\]\(([^)]+)\)', txt):
        t=m.group(2); ln=txt[:m.start()].count('\n')+1
        if t.startswith('http') or t.startswith('#'): continue
        tot+=1; base=t.split('#')[0]
        if base.startswith('/'): lead.append((p,ln,t)); continue
        if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(p),base))):
            bad.append((p,ln,t))
print('total',tot,'| broken',bad,'| leading-slash',lead)
PY
```

Expected: authored files clean; at most the one transcript hit the
round 2 response names. **Observed: `total 165 | broken [] |
leading-slash [('threads/2026-08-24-matter-system.md', 475,
'/matters/m0001-….md')]`** — 164 authored links, all resolving, none
leading-slash, and exactly one hit, inside the imported transcript.

Measured at `7357244`, before this round's own files. With this run
record and the round 3 vetting entries added the counts are 209 total,
208 authored, still no break and still the one transcript hit.

A note the round 2 response predicted and this round walked into: two
quotations in the first draft of this file — the regex form, and the
archived README's opening line, which itself contains a markdown link —
planted link-shaped strings in an authored file and failed the check.
Both were rewritten before commit. That is the third time the boundary
between a link and a quotation of one has cost someone a fix, which is
the argument for writing the scope rule down somewhere normative rather
than in a vetting append (finding X12).

Reading `design:475` in place: it is a cell of a four-row table in
which the agent contrasts "Ours" with "OKF", and the cell is a
*quotation* of OKF's bundle-absolute link form, ellipsis included.
Editing it would edit a primary source, which §9.2 forbids. **The
re-scoping is honest, not convenient**: it costs the check nothing —
no second violation is hiding behind it — and the alternative is
corrupting evidence. Its only defect is where it is written down
(finding X12).

### 8 · Append-only discipline

```
git diff 25d2e16..7357244 -- matters/m0001-matter-system.md | grep '^-' | grep -v '^---'
git diff --numstat 25d2e16..7357244
```

Expected: no deleted line from any `## Vetting` entry.
**Observed: 57 deletions on m0001, all in the ratified region** — the
`threads:` frontmatter line, the supersession note, the Sources
paragraph, the 33-row ledger table, the Scope paragraph, the Execution
paragraph. No vetting text was removed, on m0001 or on any other
matter. The response entries are appended under the existing round 2
entries throughout.

### 9 · Commit discipline (§8)

```
git log --format='%h %s | %(trailers:key=Matter,valueonly)' -8
```

Expected: `Matter: mNNNN` trailer on every commit.
**Observed: all eight commits on the branch carry `Matter: m0001`.**
Branch names do not carry the matter-ID prefix §8 also requires
(finding X13).

## Verdict

Claim 1 confirmed — the import is byte-identical to `c11956d`, and the
digest the round 2 response published is reproducible.

Claim 2 confirmed for existence — all 75 tree-wide citations and all 46
ledger citations resolve to non-blank turns — and confirmed for content
on 34 of 35 rows. Row 83 fails: the turn that carries its derivation is
the agent's, at `design:467`, and is uncited.

Claim 3 **refuted.** 45% of the archived doctrine and 77-78% of two
archived matters survive into this tree in runs of forty characters or
more, including passages of authorial prose up to 315 characters. The
three sentences asserting the contrary are in the ratified region of
three files.

Claim 4 confirmed: the index regenerates byte-identically, frontmatter
and states conform, and the link check holds with exactly the one
documented exception.

Claim 5 confirmed: append-only held for the vetting record.

- Date: 2026-08-25
- Actor: claude-code/2026-08-25 (vetting round 3, fresh instance —
  neither the round 2 reviewer nor the round 2 response's author).
  Threads:
  [2026-08-24-matter-system](../threads/2026-08-24-matter-system.md),
  [2026-08-24-audit-and-adjudication](../threads/2026-08-24-audit-and-adjudication.md)
