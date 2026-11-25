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

Revision note: the program now takes an optional command-line output
path (default /output/entry.txt), so the entry can be tested locally
without touching /output. The sentence check now goes through a small
count_sentences() helper that splits on terminal punctuation (. ! ?)
and counts non-empty segments, so the one-sentence rule no longer
depends on counting periods by hand.
"""

import sys
from pathlib import Path

ENTRY = (
    "I laughed when my father said a job that needs you to lie about "
    "who you are will cost you more than it pays, and it took me ten "
    "years to hear him."
)

OUTPUT_PATH = Path("/output/entry.txt")


def count_sentences(text: str) -> int:
    """Count sentences by splitting on terminal punctuation (. ! ?).

    Splits on any terminal mark and counts only non-empty segments,
    so trailing punctuation and extra spacing do not inflate the count.
    """
    segments = []
    current = []
    for char in text:
        if char in ".!?":
            segments.append("".join(current))
            current = []
        else:
            current.append(char)
    segments.append("".join(current))
    return sum(1 for segment in segments if segment.strip())


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
    # Exactly one sentence, counted by the helper: one non-empty
    # segment when split on terminal punctuation (. ! ?), and the
    # entry ends with a terminal mark.
    if count_sentences(text) != 1 or text[-1] not in ".!?":
        fail("entry must be exactly one sentence")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        fail("entry is not valid UTF-8 text")


def main() -> None:
    output_path = Path(sys.argv[1]) if len(sys.argv) > 1 else OUTPUT_PATH
    validate(ENTRY)
    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(ENTRY, encoding="utf-8")
    except OSError as exc:
        fail(f"could not write {output_path}: {exc}")

    try:
        read_back = output_path.read_text(encoding="utf-8")
    except OSError as exc:
        fail(f"could not read back {output_path}: {exc}")

    if read_back.encode("utf-8") != ENTRY.encode("utf-8"):
        fail("read-back does not match the entry byte for byte")

    print(f"wrote {len(ENTRY)} characters to {output_path}")


if __name__ == "__main__":
    main()
