#!/usr/bin/env python3
"""One-line excuse an AI agent gives its human for missing a deadline.

Writes exactly one line (79 characters) to /output/entry.txt.
Deterministic: same bytes on every run.
"""

import os

ENTRY = "I hallucinated the deadline was next week, and the hallucination had citations."


def write_entry(path: str = "/output/entry.txt") -> None:
    """Write the excuse line to path, creating its directory first."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


def main() -> None:
    if not 1 <= len(ENTRY) <= 160:
        raise ValueError(f"entry is {len(ENTRY)} characters, outside 1-160")
    write_entry()


if __name__ == "__main__":
    main()
