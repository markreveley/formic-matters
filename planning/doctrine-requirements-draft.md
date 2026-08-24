# Doctrine requirements — operator draft

Status: DRAFT, compiled by the audit agent from operator rulings across
the sessions of 2026-08-24. **This file is the operator's to edit** —
correct anything misstated, resolve the O- items inline, delete what you
do not want, add what is missing. Once you are satisfied, this file is
the primary input to the fresh authoring of the new bundle, and the
fidelity oracle the next reviewer checks the new doctrine against.

Convention: **R-nn** = ruled (as understood from your messages).
**O-nn** = open — needs your ruling; a default is suggested.
**P-nn** = proposed in discussion, not yet ruled.

## Restart

- **R-01** The prior bundle (PR #1) is neither repaired nor superseded
  item-by-item. The new bundle is authored fresh, from a blank tree —
  no doctrine text, matter text, thread, or index is carried over.
- **P-02** The old record is archived, not expunged: PR #1 is closed
  unmerged and stays reachable with its audit comment; nothing in the
  new tree depends on it or copies from it. The new bundle may state
  its provenance in one line; it must never claim to be uninformed by
  the prior attempt. (Alternative you may choose instead: delete and
  recreate the repo for a true expunge. Recommendation: archive.)
- **R-03** Facts about beatcode are re-derived and re-filed fresh with
  complete diagnoses and evidence, not copied. The track-length matter
  files as *resolved* from day one, citing repo evidence and a fresh
  run record.
- **R-04** Ratification of the new doctrine is a real act: the operator
  reads the exact text and ratifies it, with a content hash recorded at
  that moment. Nothing carries a `verified` entry before that act.

## Process rules the new doctrine must contain

- **R-10** Vetting rounds are recorded in the matter file itself,
  appended and never rewritten. Review discourse lives in the repo, not
  in GitHub comments. GitHub is transport and merge mechanics only.
- **R-11** The operator's response channel is local file edits,
  committed and pushed — not PR comments. Agents read rulings from the
  tree.
- **R-12** Threads (verbatim session exports) are primary sources, like
  goldens. Every view over them — indexes, matter-to-thread maps — is
  derived from frontmatter, never authored. A matter's frontmatter
  links the threads and runs behind it.
- **R-13** `runs/` — append-only verification records: the claim
  tested, environment (OS, kernel, arch, toolchain and tool versions),
  exact commands, expected vs observed, verdict, date, actor. Cited
  from matters as evidence. Never edited after the fact.
- **R-14** Claims-DAG convention for evidence-heavy matters — see
  `planning/claims-dag-workflow.md`.
- **R-15** Execution is operator-triggered: a matter leaves `staged`
  for `executed` only through a dev agent the operator launched against
  it. Delegation to an orchestration agent is a future matter, never an
  inference.
- **R-16** Deterministic-code principle: anything in the process
  checkable by deterministic code is checked by deterministic code;
  agents are reserved for judgment.
- **R-17** Matters assert immutable references (commit SHAs, frozen
  files). No undated mutable-state claims ("not pushed", "currently on
  main").
- **R-18** OKF v0.2 as a documented dialect, not a certification:
  relative links, ISO 8601 datetimes with explicit offset, `status`
  derived mechanically from `state`, and a recorded deviation wherever
  OKF fights a real need. The dialect choices are stated in one
  doctrine paragraph.
- **O-19** Landed record: entering `executed` requires a final section
  on the matter stating what actually landed — commits, deviations from
  the ratified plan, date, actor. Suggested: yes.
- **O-20** Matter citation in git: every commit carries a
  `Matter: mNNNN` trailer (hook-enforced once tooling exists);
  branch names and PR titles are prefixed with the matter id.
  Suggested: yes.
- **R-21** Types are `feature | fix | refactor | spec`; there is no
  separate `doctrine` type — `spec` covers normative text including the
  doctrine itself. Changing the type set is itself a `spec` matter.
- **R-22** The doctrine explicitly governs two targets: changes to
  beatcode, and changes to the process repo itself. Self-hosting is
  stated, not implied.

## State machine — constraints for the fresh author, not text

- **R-30** The operator's state spine stands:
  `proposed → ratified → staged → executed`.
- **R-31** There is a defined path for a ratified plan that fails
  during execution. Suggested: one backward transition
  `staged → proposed`, with the failure recorded on the matter.
- **R-32** Ratifying a matter that contradicts an already-ratified
  matter requires explicitly superseding or amending the earlier one; a
  validator check enforces the link's existence.
- **R-33** The retroactive path is designed now, minimally: file
  directly in `executed` with evidence attached and explicit operator
  acknowledgment. It is already needed (SPEC-GAPS migration, thread
  policy).
- **O-34** Everything else about the machine — draft states, in-flight
  markers, further transitions — is the fresh author's to propose and
  yours to ratify as part of the whole document. No adjudication of the
  old text's choices is required or wanted.

## Repo topology

- **P-40** No framework split yet. One process repo governs itself and
  beatcode, distinguished by `target`. The doctrine records the
  extraction tripwire: a second consumer repo actually adopts the
  process, or the tooling matures into a binary wanting its own release
  cadence, or doctrine changes start being motivated by non-beatcode
  needs. Extraction stays mechanical later because the collection is
  flat and frontmattered.

## Review of the new bundle

- **R-50** The next review is performed by a fresh agent given only:
  the new bundle, the beatcode repo, and this file. Not the old thread,
  not the old matters, not the old PR — anchoring is the failure mode.
  The fidelity check is: new doctrine versus this file plus the build
  session's exported thread.
