# Run — beatcode render reproduction and golden-derived length check

Append-only verification record (doctrine §9.1). Never edited; a
superseding run is a new file.

## Claims tested

- The oracle's four.bc track length is recoverable from committed,
  pre-implementation evidence, and equals `last + 22050`
  ([m0004](../matters/m0004-track-length-index-count.md) C2–C5).
- The implementation reproduces all four committed render hashes and
  the golden-derived byte sizes
  ([m0004](../matters/m0004-track-length-index-count.md) C5;
  [m0005](../matters/m0005-readme-stale-status.md) "48 tests green").

## Environment

- OS: Linux 6.18.44-fc-v21, x86_64 (remote agent container)
- Toolchain: rustc 1.94.1 (e408947bf 2026-03-25), pinned via
  `rust-toolchain.toml`; cargo release profile
- Python 3 for the golden-derived computation
- Repo: `ob6to8/beatcode` at `fa17627` (main; SPEC.md and
  `goldens/events/` byte-identical at seed `91188a5`), built in a
  scratch copy — working clones untouched

## Commands and results

1. Golden-derived track length — for each score, `last` = max over
   events of `trunc(performed_s × 44100) + kit_duration − 1`, kit
   durations per `SPEC.md:681-685`, events from
   `goldens/events/*.events.jsonl`; `frames = last + 22050`:

   | score | events | last | frames | bytes (44 + frames×4) |
   |---|---|---|---|---|
   | four | 24 | 94,529 | 116,579 | 466,360 |
   | dilla | 44 | 237,838 | 259,888 | 1,039,596 |
   | poly | 86 | 429,974 | 452,024 | 1,808,140 |
   | edge | 58 | 241,386 | 263,436 | 1,053,788 |

   Expected for four.bc: 116,579 frames / 466,360 bytes, the reference
   render pinned at `SPEC.md:793-795` (prose and header hex).
   **Observed: exact match.**

2. `bash scripts/check_renders.sh` — expected: four hashes matching
   `goldens/renders-v0.1.txt`. **Observed: `ok` for four.wav,
   dilla.wav, poly.wav, edge.wav** (90577ac5…, 61711a63…, 7d712bfd…,
   b0d61b86…).

3. Rendered file sizes (`renders/ci-check/`): **observed 466,360 /
   1,039,596 / 1,808,140 / 1,053,788 bytes — all four equal the
   golden-derived predictions above.**

4. `cargo test --release` — expected all green. **Observed: 48 passed,
   0 failed, across 15 test binaries.**

## Verdict

All claims confirmed. The implementation's track lengths equal the
lengths derivable from the seed's own goldens and spec, four.bc's
equals the oracle's pinned reference exactly, and the committed hashes
reproduce byte-for-byte.

- Date: 2026-08-24
- Actor: claude-code/2026-08-24 (audit session; thread:
  [2026-08-24-audit-and-adjudication](../threads/2026-08-24-audit-and-adjudication.md))
