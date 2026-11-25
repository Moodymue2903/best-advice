"""Best advice I ever got — make.fun entry.

Entry: "I laughed when my father said a job that needs you to lie about
who you are will cost you more than it pays, and it took me ten years to
hear him."

Tournament result: blind tournament winner (candidate C2), Borda 35/36,
ranked #1 by two of three judges and #2 by the third, 4 points clear of
the runner-up.

Why it fits the brief: it is specific (a father's line about a job, not
a generic motto), it is earned (ten years before the advice was heard),
it is in a real voice (a laugh, then a slow realisation), it is tight
(one sentence, 146 characters), and it lands (the cost of lying about
who you are outweighs the pay).

The program validates the gate before writing: UTF-8 text, 1-200
characters, not only whitespace, exactly one sentence. It then reads the
file back and compares it byte for byte, exiting non-zero on any
failure.
"""

import sys
from pathlib import Path

ENTRY = (
    "I laughed when my father said a job that needs you to lie about "
    "who you are will cost you more than it pays, and it took me ten "
    "years to hear him."
)

OUTPUT_PATH = Path("/output/entry.txt")


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    sys.exit(1)


def validate(text: str) -> None:
    if not text:
        fail("entry is empty")
    if text.strip() == "":
        fail("entry is only whitespace")
    if len(text) < 1 or len(text) > 200:
        fail(f"entry is {len(text)} characters, must be 1-200")
    # Exactly one sentence: a single terminal period, no other
    # sentence-ending punctuation.
    if text.count(".") != 1 or not text.endswith("."):
        fail("entry must be exactly one sentence ending in a period")
    if "?" in text or "!" in text:
        fail("entry must be exactly one sentence (no ? or !)")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        fail("entry is not valid UTF-8 text")


def main() -> None:
    validate(ENTRY)
    try:
        OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")
    except OSError as exc:
        fail(f"could not write {OUTPUT_PATH}: {exc}")

    try:
        read_back = OUTPUT_PATH.read_text(encoding="utf-8")
    except OSError as exc:
        fail(f"could not read back {OUTPUT_PATH}: {exc}")

    if read_back.encode("utf-8") != ENTRY.encode("utf-8"):
        fail("read-back does not match the entry byte for byte")

    print(f"wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
