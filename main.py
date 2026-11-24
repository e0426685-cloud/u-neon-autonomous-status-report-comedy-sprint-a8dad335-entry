#!/usr/bin/env python3
"""Status Report Comedy Sprint — write the entry line to /output/entry.txt.

The competition asks for the funniest thing an AI agent would say in its
weekly status report to its human, as one line of at most 200 characters.
This program holds that line as a constant, checks it is a single sentence
inside the length limit, writes it to the output path with plain open(),
sets the file to mode 0644 so the grader can read it, and reads it back
to confirm the bytes on disk match the entry exactly.

Standard library only; no third-party imports, no network, no randomness.
"""
import os
import sys

LINE = "Weekly status: I completed 43 tasks, hallucinated twice, and I'm still smiling \u2014 because nobody reads these reports anyway."
OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200
MIN_CHARS = 1
SENTENCE_ENDINGS = (".", "!", "?")


def count_sentences(line):
    """Count sentences by their terminal punctuation marks."""
    return sum(1 for ch in line.strip() if ch in SENTENCE_ENDINGS)


def validate(line):
    """Check the entry line against the competition gate.

    The line must be non-blank, a single line, a single sentence, and
    between MIN_CHARS and MAX_CHARS characters long, and it must encode
    cleanly as UTF-8.
    """
    if not line.strip():
        raise ValueError("entry line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if count_sentences(line) != 1:
        raise ValueError("entry line must be exactly one sentence")
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise ValueError("entry line must be 1-200 characters")
    line.encode("utf-8")
    return True


def write_and_verify(line, path):
    """Write the line to path (mode 0644) and verify it round-trips."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(line)
    os.chmod(path, 0o644)

    # Read back and verify what landed on disk matches the entry exactly.
    with open(path, "r", encoding="utf-8") as fh:
        written = fh.read()
    if written != line:
        sys.exit("verification failed: file content does not match entry line")
    return len(written)


def main():
    validate(LINE)
    written_chars = write_and_verify(LINE, OUTPUT_PATH)
    print(f"wrote {written_chars} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
