# Thread — the minimal handoff and declared sources

Verbatim transcript of a Claude Code session, exported by its
participating agent on operator direction (the final human turn
below). The session reviewed the previous handoff after its filing
merge, established that proposed matters are candidate policy and
confer no authority, and directed the changes it then carried out:
the revision of
[m0016](../matters/m0016-launch-instructions-policy.md) (the explicit
authority rule),
[m0017](../matters/m0017-operator-authored-ratification.md) (plan
step 7),
[m0019](../matters/m0019-fresh-context-durable-handoffs.md) and
[m0020](../matters/m0020-referential-handoff-authority.md) (the
minimal handoff), the filing of
[m0024](../matters/m0024-declared-sources.md) (declared sources), and
the rewrite of `handoff.md` as pointers and one declared action.

Human and agent turns are reproduced exactly as written. Reasoning
traces, tool calls, tool results, and injected environment context are
omitted; each agent turn below is that turn's closing message — the
reply the operator read — and brief working narration the agent
emitted between tool calls is omitted with the tool traffic it
narrates. Where a turn refers to a read, an edit, a commit, a push, or
a pull-request operation, that action happened between the turns
shown. Links inside agent turns are transcript text, not a link graph
(doctrine §12, “Storage and format”).

Per-turn clock times were not captured by the exporting agent: the
session ran on 2026-08-29 (UTC; its container was provisioned late
2026-08-28), turn order is as shown, and the export commit's own
timestamp bounds the export.

The thread ends mid-turn: the reply to the final human message is not
in the file, because that message is what produced the export; the
merge it also directs happens after the export is committed.

**Redaction:** none was required; no local paths, credentials, or
personal data appear in the turns.

Speaker headings are marked `▸` because turns contain their own `##`
headings; the marker keeps turn boundaries machine-parseable.

---

## ▸ Mark — human turn, 2026-08-29

review handoff and discuss next steps

---

## ▸ Claude — agent turn, 2026-08-29

The review is done — no changes made, nothing to commit. Here's where things stand.

## Handoff review: its action is consumed, and everything checks out

The handoff's one current action — merge the filing PR for `claude/restate-ratify-spec-eval-02nojc` — **is complete**: PR #14 merged as a true merge commit (`2bfce19`, two parents, m0017-prefixed title), now the tip of `origin/main` (confirmed by fetch). I ran every re-verification the handoff prescribes for a post-merge read:

- **m0016–m0023 all remain `proposed`** in frontmatter — the merge ratified and staged nothing, exactly as the handoff insists.
- Established state matches the index: m0001, m0012, m0014, m0015 `executed`; m0013 `ratified`; everything else `proposed`.
- All twelve branch commits carry correct `Matter:` trailers (m0017 ×7, m0021 ×3, m0022, m0023); the thread export and its verification run are in the tree; the handoff's observed base `527397e` is indeed the merge base, and its two self-commits follow the content commits as it states.
- The one deviation (harness-assigned branch name spanning four matters) is on record in both the thread and the handoff.

I found no discrepancy between the handoff and repository state. It is now stale only in the designed sense: its next action is spent, and it still describes the merge as pending.

## Next steps: the queue holds up, and the next act is the m0017 vet

The recommended queue is sound, and I'd keep its order. **Item 2 is next: a fresh vetting round on m0017**, which currently has zero `## Vetting` entries. m0017 is the linchpin twice over — m0019 through m0023 all `depends_on` it, and it replaces the ratification mechanism every later item in the queue will use.

The ordering logic behind the rest checks out on reading the matters:

- **m0020 before m0019/m0016** is right: it's a `fix` that revises both of their *proposed* texts (referential launch, the next-action classification schema). Ratify either first and the correction needs a re-open instead of a cheap proposed-state revision. It's also the lightest possible first live use of restate-to-ratify — one restatement, no doctrine change, no m0001 re-ratification — a good property for a mechanism's maiden run.
- **m0019 third** activates the handoff (replaces the provisional notice), which pays off for every subsequent session.
- **m0018 then m0016 last** is forced by their own plans: m0018's citation policy applies to m0016 during m0016's proposed-state revision, which also folds in m0020's corrections.
- **m0023 deferred** is correct — there is no restatement corpus to analyze until the mechanism has been used several times.

## Three things worth deciding before launching the vet

**1. The known open item.** m0017's plan step 7 still hard-codes m0016 as the first mandatory use of restate-to-ratify, contradicting both the queue and m0020's own plan (which claims first use). The handoff deliberately left this for the vetting round — the reviewer should surface it as a finding and the revision should generalize or drop the naming.

**2. Who vets.** This session is not m0017's authoring context, and under m0019's proposed rule reading the handoff doesn't spoil freshness — but I've now ingested the closing agent's specific recommendation about step 7, so as a reviewer I'd arrive pre-anchored on that finding, which is exactly what m0006's unanchored-first-pass concern is about. My recommendation: launch the vet in a dedicated fresh session (`vet m0017`). You can direct it here if you accept the anchoring.

**3. The stale handoff.** Two options: I refresh it now from this branch — next action becomes "vet m0017 in a fresh context," `Matter: m0017` trailer, which keeps the `Proceed from handoff.md` shorthand usable for the launch — or you skip the refresh and launch the vet directly, letting the vetting session rewrite the handoff at its close. The refresh costs a commit-and-merge cycle; a direct launch is cheaper. I'd only do the refresh if you want the referential shorthand for this next step.

One cost worth naming plainly before you start down the queue: items 2–5 each amend doctrine, so completing the queue implies roughly ten operator restatements (m0020, m0019 ×2, m0018 ×2, m0016 ×2, m0021, m0022 ×2), each with its own draft-review round, plus the two verbal acts on m0017 itself. That load is the mechanism working as designed — the cost of the act is the point — but it's the real price of this queue, and it argues for spacing the queue over sessions rather than batching.

I've made no changes and taken no lifecycle-adjacent action. Say the word on the vet launch (here or fresh) and whether you want the handoff refreshed first.

---

## ▸ Mark — human turn, 2026-08-29

1 - noted, proceed
2 - you're kinda supposed to ingest the closing agent's rec, unless there's an issue with that. also m0019 is not ratified, should it be considere as policy? if we start adjusting matters based off of proposed matters things may get ugly quick
3 - would prefer to use the handoff as the ref that's the point. if reading further into the handoff then item 1 is corrupting to context, i could instruct the agent to "proceed with item 1 from handoff, do not read further til done"

re: spacing, yes i am thinking action-per thread

---

## ▸ Claude — agent turn, 2026-08-29

Done — [PR #15](https://github.com/markreveley/formic-matters/pull/15) is open with the refreshed handoff (one file, `Matter: m0017` trailer, harness-branch deviation stated in the file and the PR). Once you merge it, `Proceed from handoff.md in markreveley/formic-matters` launches the m0017 vetting round from main.

**On point 2 — you're right, and no, m0019 is not policy.** Conceded on the first half: ingesting the closing agent's recommendations is the handoff doing its job; the reviewer's protection is that everything in it is advisory and verified against the repository, not that it goes unread. My anchoring flag was me applying m0006's and m0019's rules as if they governed — which is exactly the failure mode your second half names. What binds today is the ratified doctrine (via m0001), its CLAUDE.md distillation, and the ratified/executed records — nothing in a `proposed` matter binds, authorizes, or is enforceable by an agent.

The line that keeps "adjusting matters based off proposed matters" from getting ugly is the direction authority flows. Two things stay legitimate: **rehearsing a form** (the handoff is written in m0019/m0020's drafted schema — the same posture m0017 takes toward a voluntary draft restatement: it "may rehearse the new form but cannot bootstrap its own authority"; if m0019 dies, the format is a droppable convention), and **a ratified matter amending proposed texts** (m0020, once ratified and executed, revises m0016 and m0019 — the authority is the ratified fix; the targets being proposed is just what makes the revision cheap). The ugly case is the reverse flow — proposed text treated as an operative constraint or cited as the reason an agent must or may do something. That's shadow doctrine, the exact defect m0016 diagnoses. The refreshed handoff now says this explicitly in its re-verification section: m0006, m0019, and m0020 are candidate policy; their forms are used as rehearsal only; ratified doctrine alone governs.

**On point 3 — implemented structurally, so your scoped launch actually works.** The `Next action` record is now written to be self-contained and finding-free: it names the round, the permitted operations, and the stop boundary, and nothing else. The step-7 open item (and any future expected-finding detail) lives only in the recommended-queue section, and the file states that rule about itself. So both launch forms conform: the plain shorthand gives the default anchored-but-verifying round, and appending "read only the next-action record until done" gives a genuinely unanchored first pass — your call per launch.

Action-per-thread matches the queue's standing "one act at a time" phrasing, so nothing needed recording there. One optional loose end: if you ever want "proposed matters confer nothing" stated durably rather than implied, the cheap vehicle is a line folded into m0016/m0019 during m0020's revision cycle — not worth its own matter.

---

## ▸ Mark — human turn, 2026-08-29

"The line that keeps "adjusting matters based off proposed matters" from getting ugly is the direction authority flows. Two things stay legitimate: rehearsing a form (the handoff is written in m0019/m0020's drafted schema — the same posture m0017 takes toward a voluntary draft restatement: it "may rehearse the new form but cannot bootstrap its own authority"; if m0019 dies, the format is a droppable convention), and a ratified matter amending proposed texts (m0020, once ratified and executed, revises m0016 and m0019 — the authority is the ratified fix; the targets being proposed is just what makes the revision cheap). The ugly case is the reverse flow — proposed text treated as an operative constraint or cited as the reason an agent must or may do something. That's shadow doctrine, the exact defect m0016 diagnoses. The refreshed handoff now says this explicitly in its re-verification section: m0006, m0019, and m0020 are candidate policy; their forms are used as rehearsal only; ratified doctrine alone governs." - explain this in plainspeak

"The step-7 open item (and any future expected-finding detail) lives only in the recommended-queue section, and the file states that rule about itself. So both launch forms conform: the plain shorthand gives the default anchored-but-verifying round, and appending "read only the next-action record until done" gives a genuinely unanchored first pass — your call per launch." - explain in plainspeak

---

## ▸ Claude — agent turn, 2026-08-29

**Paragraph 1, plainly:**

A proposed matter is just an idea on file. Nobody has approved it, so it can't tell anyone what to do. The rule of thumb: it's fine to *work on* a proposed matter, never fine to *take orders from* one.

Two things look like "using proposed matters" but are actually safe:

1. **Trying on the format.** m0019 proposes a template for what handoff.md should look like (observed commit, next action, stop boundary, etc.). We're already writing handoff.md in that shape even though m0019 isn't approved. That's harmless because a layout doesn't command anything — if you reject m0019 tomorrow, we shrug and format the file some other way. Nothing was resting on it. Same spirit as m0017 saying you can practice writing a restatement before the restatement rule exists: practicing doesn't make it a rule.

2. **An approved matter editing an unapproved one.** m0020, once you ratify it and it executes, rewrites parts of m0016 and m0019 — which are still drafts. The permission to edit comes from m0020's ratification, i.e., from your act. The targets being drafts is just what makes the edit cheap: fixing a draft is fixing a draft, while fixing already-ratified text would mean formally reopening it.

The dangerous case is the arrow pointing the other way: an agent reads a draft and obeys it. "m0019 says vetting contexts must be fresh, so I must do X." Nobody approved that rule — the agent just promoted a draft to law, and now unratified text is quietly governing the repo. That's the same disease m0016 is about, and it's what I did last turn when I raised the anchoring worry by citing m0006/m0019 as if they were in force. The refreshed handoff now carries a one-bullet reminder to future sessions: those three are drafts, we only borrow their formatting, and only ratified doctrine governs.

**Paragraph 2, plainly:**

The handoff has two relevant parts. The **Next action** box is the single thing to do next — "run the first vetting round on m0017" — with what the agent may touch and where it must stop. The **queue** is my commentary on everything after that, including hints like "the reviewer will probably find the step-7 problem."

If a vetting agent reads that hint, it's been told what to find before it looks — a primed reviewer. So I moved every hint into the queue section only, and made the Next action box a clean "go review m0017" with zero opinions about the matter attached. The box is complete on its own; the agent doesn't need the rest of the file to do the job.

That gives you a dial, set per launch:

- **"Proceed from handoff.md"** → the agent reads the whole file, sees my hints, knows they're just my opinion, and has to verify everything itself. Informed reviewer.
- **Same, plus "read only the next-action record until done"** → the agent sees only the clean instruction and forms its findings from scratch. Blind reviewer.

Both are legitimate; you pick per launch depending on whether you want a second opinion that's independent of mine.

---

## ▸ Mark — human turn, 2026-08-29

proposed matters not being referencable should in fact be explicit. yes fold it into one of the matters

1 - one way to protect from having unratified matters infecting matter creation is to force reference to matters - ie. the llm has data provenance, where is it getting its assumptions from (doctrine.md etc). this would be a simple check to determine that all stated sources are ratified. this should probably be its own matter, unless you can find where to add it

2 - i guess this begs the question - if you are giving advice or making notes on a matter, why is that not just within the matter itself? this seems to again be a case of matter-specific data being smuggled in - before, it could have been me while making a ratifying restatement, now its by you when updating the handoff. it seems to me the handoff should have as little info as possible - just pointers to matters or declared specific actions. meanwhile, matters should have all the agreed on info pertaining to it at this time - you having a correction/opinion would be you adding to the matter, not somehow weirdly "biasing" the next agent

---

## ▸ Claude — agent turn, 2026-08-29

All three directives are implemented and pushed — [PR #15](https://github.com/markreveley/formic-matters/pull/15) now carries the batch (six new commits, per-matter `Matter:` trailers), retitled accordingly. Here's how each landed, and where I exercised judgment:

**Explicit non-referencability → folded into m0016.** Its proposed doctrine text (the §8 "Launch instructions" subsection) gains a second verbatim paragraph: authority resides in ratified text and operator acts, and nowhere else; a proposed matter may be pointed to — dependency, supersession, coordination — but is never citable as the basis for a rule, assumption, or act; text treating one as operative is a shadow specification. I chose m0016 over m0020 because m0016 is the spec about where authority resides and its diagnosis is literally the shadow-specification disease; m0020 is a narrow fix. The enforcement section gains the matching stop-and-report bullet.

**Provenance → new matter, [m0024](https://github.com/markreveley/formic-matters/blob/b8ef335/matters/m0024-declared-sources.md).** I couldn't find an honest existing home: m0018 governs citation *form* (headings), m0016 governs *launches* — this is an authoring rule. m0024 proposes a `sources:` frontmatter list (the matter's declared normative basis) plus a §12 dialect rule: valid sources are ratified text or append-only evidence (threads, runs) — never a proposed matter — checked mechanically at the ratification gate, with the deterministic portion forwarded to m0008. Per §10 it's honest about the limit: the check verifies what's *declared* resolves and qualifies; whether the declaration is complete stays a vetting question. It rehearses its own rule: its `sources:` lists only the doctrine, and — since this session isn't exported — it holds its own operator-direction provenance gap open exactly as its rule prescribes.

**Minimal handoff → the ruling landed on m0019, then the handoff followed.** Applying your own principle, the design change went into the matter that owns the handoff: m0019's required-contents list now reads pointers to the index, pending operator acts, exactly one declared action, and external state to re-verify — with an explicit rule that matter commentary (open items, corrections, expected findings) is recorded on the matter, before every reader equally, and ordering is derived from `depends_on`, never authored. m0020 got a two-line consistency fix (it referenced the now-abolished queue). Then the downstream moves: **m0017's step 7 was corrected in place** (first use of the mechanism is staging judgment; no hard-coded m0016), the queue's real ordering became **`depends_on` edges** — m0019 gains m0020, m0016 gains m0020 and m0018 — and the handoff was rewritten to the minimal form. Nothing else needed relocating: m0023 already carries its deferral rationale on-matter, and the restatement-count commentary was derivable from each matter's own plan.

Two things worth noting. First, your instinct was already in the doctrine: §7 says a worklist "is a filter plus a topological sort over `depends_on` — derived, never authored" — the authored queue was quietly in tension with ratified text. Second, the anchoring dial from last turn dissolved on its own: with the step-7 correction *in* m0017, there's no expected finding anywhere for a reviewer to inherit — the vet reads the corrected matter fresh, no scoped-read instruction needed.

One open item for you: this session has now directed real matter content (the m0024 filing, three revisions), which under the emerging practice qualifies it for thread export — and m0024's `threads:` cite is waiting on exactly that. Say the word and I'll export it; otherwise, once you merge PR #15, `Proceed from handoff.md in markreveley/formic-matters` launches m0017's first vetting round.

---

## ▸ Mark — human turn, 2026-08-29

export thread verbatim
then merge 15
