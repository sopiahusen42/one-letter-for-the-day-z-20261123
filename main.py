"""Entry writer for the make.fun bounty "One Letter for Your Day".

The entry is a single capital letter: the first letter of the word that
describes the day. This program writes that one line to entry.txt, and the
output is deterministic -- no clock, no randomness, no network. The same
LETTER always produces the same bytes.
"""

import os
import sys

LETTER = "Z"

OUTPUT_FILENAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"
MAX_CODE_POINTS = 160


def validate_entry(text):
    """Return an error string for a bad entry, or None when it is valid."""
    if not isinstance(text, str):
        return "entry must be a str, got " + type(text).__name__
    if not text.strip():
        return "entry is empty once stripped"
    if text != text.strip():
        return "entry carries leading or trailing whitespace"
    if "\n" in text or "\r" in text:
        return "entry spans more than one line"
    if len(text) > MAX_CODE_POINTS:
        return (
            "entry is "
            + str(len(text))
            + " code points, the cap is "
            + str(MAX_CODE_POINTS)
        )
    if len(text) != 1 or text not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return "entry must be exactly one capital ASCII letter A-Z"
    return None


def main():
    text = LETTER

    error = validate_entry(text)
    if error is not None:
        print("error: " + error, file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, OUTPUT_FILENAME)

    payload = (text + "\n").encode("utf-8")
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text + "\n")

    with open(out_path, "rb") as fh:
        on_disk = fh.read()
    if on_disk != payload:
        print(
            "error: read-back mismatch in "
            + out_path
            + " (expected "
            + repr(payload)
            + ", found "
            + repr(on_disk)
            + ")",
            file=sys.stderr,
        )
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
