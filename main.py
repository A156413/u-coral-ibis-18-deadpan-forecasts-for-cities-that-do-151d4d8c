#!/usr/bin/env python3
"""Deadpan forecast for Port Sullen, a city that does not exist.

Writes a single forecast line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output), as the make.fun program/v1 harness requires.
"""

import os

# The competition gate allows 1 to 160 characters in /output/entry.txt.
# The file holds the forecast plus one trailing newline, so the text
# itself must stay at most 159 characters.
MAX_CHARS = 159

ENTRY_TEXT = "Port Sullen: 11°C, drizzle all afternoon, and the 4:15 fog arrives exactly on schedule, as it has every day since 1987, without once apologising."


def main() -> None:
    if not 1 <= len(ENTRY_TEXT) <= MAX_CHARS:
        raise ValueError(
            "ENTRY_TEXT must be 1-%d characters, got %d"
            % (MAX_CHARS, len(ENTRY_TEXT))
        )
    if "\n" in ENTRY_TEXT or "\r" in ENTRY_TEXT:
        raise ValueError("ENTRY_TEXT must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
