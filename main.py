# SPDX-License-Identifier: MIT
"""Warning Label for Humans: One Line, Big Laugh.

Writes exactly one line — a safety warning label for every human being —
to /output/entry.txt. Deterministic, offline, stdlib only.
"""

import os

LINE = (
    "WARNING: Do not operate this human while tired, emotional, "
    "or certain this warning applies to everyone except them."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the gate counts the file's characters, so the
    # file holds exactly the one line and nothing else.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
