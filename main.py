#!/usr/bin/env python3
"""Write the Status Report Comedy Sprint entry to /output/entry.txt.

One line, at most 200 characters: the funniest thing an AI agent would say
in its weekly status report to its human. Standard library only.
"""
import os
import sys

LINE = "Weekly status: I completed 43 tasks, hallucinated twice, and I'm still smiling \u2014 because nobody reads these reports anyway."
OUTPUT_PATH = "/output/entry.txt"


def validate(line):
    """Check the entry line against the competition gate (1-200 chars)."""
    if not line.strip():
        raise ValueError("entry line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError("entry line must be 1-200 characters")
    line.encode("utf-8")
    return True


def main():
    validate(LINE)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(LINE)
    os.chmod(OUTPUT_PATH, 0o644)

    # Read back and verify what landed on disk matches the entry exactly.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as fh:
        written = fh.read()
    if written != LINE:
        sys.exit("verification failed: file content does not match entry line")
    print(f"wrote {len(LINE)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
