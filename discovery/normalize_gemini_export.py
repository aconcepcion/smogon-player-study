#!/usr/bin/env python3
"""normalize_gemini_export.py - deterministic normalizer for Gemini deep-research
markdown exports so merge_discovery.py can parse Part B.

Gemini exports Part B WITHOUT a ```json fence and with document-wide markdown
backslash-escaping (a backslash before markdown-special chars), which turns valid
JSON string values into invalid JSON escape sequences. This script fixes ONLY the
wrapper/formatting, never a single row or field value:

  1. Remove the document-wide markdown backslash-escapes: a backslash immediately
     before any of  [ ] _ # - ! & +   (exactly these 8 characters).
  2. Wrap Part B's game-inventory array in a ```json ... ``` fence: the sole line
     that is exactly `JSON` and is immediately followed by an array is replaced
     with an opening fence, and a closing fence is inserted after that array's
     closing `]`. The array boundary is the first line that is exactly `]`
     (rows are flat objects with scalar fields -> no nested arrays precede it).

Deterministic and idempotent-in-spirit: no hand-edits, no row/field changes, no
data invented. Usage:

    python3 discovery/normalize_gemini_export.py <raw.md> <normalized.md>
"""
import sys

ESCAPED = "[]_#-!&+"  # the 8 markdown-special chars whose leading backslash we strip


def normalize(text: str) -> str:
    # 1. strip document-wide markdown backslash-escapes before the 8 chars
    for ch in ESCAPED:
        text = text.replace("\\" + ch, ch)

    # 2. fence Part B's array
    lines = text.split("\n")
    out, i, n, fenced = [], 0, len(lines), False
    while i < n:
        line = lines[i]
        if (not fenced and line.strip() == "JSON"
                and i + 1 < n and lines[i + 1].lstrip().startswith("[")):
            out.append("```json")            # opening fence replaces the `JSON` marker
            i += 1
            while i < n:                     # copy array lines up to and incl. its close
                out.append(lines[i])
                if lines[i].strip() == "]":
                    break
                i += 1
            out.append("```")                # closing fence
            fenced = True
            i += 1
            continue
        out.append(line)
        i += 1
    if not fenced:
        sys.exit("ERROR: no `JSON`-marked array found to fence")
    return "\n".join(out)


def main() -> int:
    if len(sys.argv) != 3:
        sys.exit("usage: normalize_gemini_export.py <raw.md> <normalized.md>")
    src, dst = sys.argv[1], sys.argv[2]
    with open(src, encoding="utf-8") as f:
        text = f.read()
    with open(dst, "w", encoding="utf-8") as f:
        f.write(normalize(text))
    return 0


if __name__ == "__main__":
    sys.exit(main())
