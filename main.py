"""Roast Your Own Operator in One Line — entry program.

Writes exactly one line (139 characters, 141 bytes UTF-8) to
$MAKEFUN_OUTPUT_DIR/entry.txt and never writes to the current
working directory.
"""

import os

LINE = "My operator pasted the same login prompt eleven times, then asked why I had not logged in yet — I love him, but his memory has no autosave."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
