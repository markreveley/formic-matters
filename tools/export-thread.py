#!/usr/bin/env python3
"""Export a Claude Code session transcript as a readable thread document.

    tools/export-thread.py <session.jsonl> <out.md> [title]

Keeps human and assistant turns verbatim. Drops reasoning traces, tool
calls, and tool results — with one exception: answers to prompted
questions arrive as tool results but are the human speaking, so they are
kept and labelled.

Redaction is applied on the way out, not after publication: the home
directory becomes `~` and the session's project slug becomes `<project>`.
m0011 records why that ordering matters.

Interim. See m0008 and m0011 for what is still undecided.
"""
import json, re, io, os, sys
from collections import Counter

SYSTEM_REMINDER = re.compile(r"<system-reminder>.*?</system-reminder>\s*", re.S)

LABEL = {
    "human": "## ▸ Mark",
    "human-interjection": "## ▸ Mark *(interjected mid-turn)*",
    "human-answer": "## ▸ Mark *(answering a prompted question)*",
    "assistant": "## ▸ Claude",
}


def redact(text):
    home = os.path.expanduser("~")
    user = os.path.basename(home)
    # Slug first: it encodes the path without slashes, so replacing the
    # literal home path would miss it.
    text = re.sub(r"-Users-" + re.escape(user) + r"[\w.-]*", "<project>", text)
    return text.replace(home, "~")


def collect(src):
    turns = []
    for line in io.open(src, encoding="utf-8"):
        try:
            d = json.loads(line)
        except ValueError:
            continue
        kind = d.get("type")

        if kind == "user" and not d.get("isMeta"):
            content = (d.get("message") or {}).get("content")
            if isinstance(content, str):
                text = SYSTEM_REMINDER.sub("", content).strip()
                if text:
                    turns.append(("human", text))
            elif isinstance(content, list):
                for block in content:
                    if (isinstance(block, dict)
                            and block.get("type") == "tool_result"
                            and isinstance(block.get("content"), str)
                            and block["content"].startswith("The user answered:")):
                        turns.append(("human-answer", block["content"].strip()))

        elif kind == "attachment":
            a = d.get("attachment") or {}
            if (a.get("type") == "queued_command"
                    and (a.get("origin") or {}).get("kind") == "human"):
                prompt = (a.get("prompt") or "").strip()
                if prompt:
                    turns.append(("human-interjection", prompt))

        elif kind == "assistant":
            content = (d.get("message") or {}).get("content")
            if isinstance(content, list):
                text = "\n".join(
                    b["text"] for b in content
                    if isinstance(b, dict) and b.get("type") == "text" and b.get("text")
                ).strip()
                if text:
                    # Consecutive assistant entries are one logical turn once
                    # the tool calls between them are dropped.
                    if turns and turns[-1][0] == "assistant":
                        turns[-1] = ("assistant", turns[-1][1] + "\n\n" + text)
                    else:
                        turns.append(("assistant", text))
    return turns


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    src, out = sys.argv[1], sys.argv[2]
    title = sys.argv[3] if len(sys.argv) > 3 else "Thread"

    turns = collect(src)
    body = [
        f"# Thread — {title}",
        "",
        "Verbatim transcript of a Claude Code session.",
        "",
        "Human and assistant turns are reproduced exactly as written, with one "
        "exception: absolute local paths are redacted to `~` and the session's "
        "project slug to `<project>`. Nothing else is altered.",
        "",
        "Reasoning traces, tool calls, and tool results are omitted; where a "
        "turn refers to a command or a file read, that action happened between "
        "the turns shown.",
        "",
        "The thread necessarily ends mid-turn: the reply to the final human "
        "message is not in the file, because that message is what produced the "
        "export.",
        "",
        "Speaker headings are marked `▸` because turns contain their own `##` "
        "headings; the marker keeps turn boundaries machine-parseable.",
        "",
        "---",
        "",
    ]
    for speaker, text in turns:
        body += [LABEL[speaker], "", redact(text), "", "---", ""]

    io.open(out, "w", encoding="utf-8").write("\n".join(body).rstrip() + "\n")
    print(f"{len(turns)} turns → {out}")
    print(dict(Counter(s for s, _ in turns)))


if __name__ == "__main__":
    main()
