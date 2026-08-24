---
type: fix
title: §9.4 track length conflates an index with a count
description: frames = last + 22050 yields a 22049-frame tail; whether that is intended has never been established.
id: m0004
state: proposed
target: beatcode
tags: [spec, render, needs-diagnosis]
---

# m0004 · §9.4 track length conflates an index with a count

## Symptom

`SPEC.md` §9.4 specifies:

```
last   = highest frame index touched
frames = last + trunc(0.5 × 44100) = last + 22050   // half-second tail
```

`last` is an **index**; `frames` is a **count**. Valid indices are
therefore `0 ..= last + 22049`, so the silent tail after the last touched
frame is 22 049 frames — one short of the half second the comment claims.
`src/render.rs:68` implements `last + 22050` as written.

## Diagnosis — NOT ESTABLISHED

Open. Three possibilities, none yet ruled out:

1. Intended, matching the reference oracle exactly — in which case the
   defect is only the misleading comment.
2. An off-by-one inherited from the oracle and faithfully reproduced — in
   which case it is still correct to keep, and should say so.
3. An off-by-one introduced in this implementation — in which case the
   committed render hashes in `goldens/renders-v0.1.txt` are wrong.

The distinguishing evidence is whether the oracle's own track length can
be recovered from the transcripts or the committed hashes.

## Why this is filed rather than fixed

This matter exists because it was previously *documented as intended*
without that intent being established, which is precisely the failure the
matter system is meant to prevent. Do not ratify until the diagnosis
above resolves to one of the three cases.

Any change here alters render hashes and is therefore the highest-risk
change in the collection.
