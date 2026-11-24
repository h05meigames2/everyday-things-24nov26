"""Everyday Things, Two Lines, Longer Run — make.fun entry.

Writes a two-line explanation of a traffic jam for a 10-year-old to
/output/entry.txt: line 1 explains it through one vivid analogy, line 2
says why that analogy works, what it maps and what it leaves out.
"""

import os

LINE1 = (
    "A traffic jam is like a river that suddenly turned into a parking lot, "
    "because too many cars all tried to squeeze through the same narrow "
    "bridge at the same time."
)

LINE2 = (
    "It works because both slow everything to the speed of the narrowest "
    "part, but it leaves out that drivers can honk, switch lanes, and take "
    "another road, while water can only wait."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 400


def is_single_sentence(line):
    """True when the line is exactly one sentence: one terminal full stop,
    no other sentence-ending punctuation inside it."""
    stripped = line.strip()
    if not stripped.endswith("."):
        return False
    body = stripped[:-1]
    return not any(ch in body for ch in ".!?")


def validate(lines):
    """Check the entry shape: exactly two lines, each one non-empty sentence,
    no trailing whitespace, 400 characters total at most."""
    assert len(lines) == 2, f"expected 2 lines, got {len(lines)}"
    for i, line in enumerate(lines, start=1):
        assert line, f"line {i} is empty"
        assert line == line.strip(), f"line {i} has leading/trailing space"
        assert is_single_sentence(line), f"line {i} is not a single sentence"
    text = "\n".join(lines)
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry is {len(text)} chars, must be 1-{MAX_CHARS}"
    )
    return text


def main():
    lines = [LINE1, LINE2]
    text = validate(lines)
    for line in lines:
        print(line)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # Round-trip verification: read it back and compare byte for byte.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    assert written == text + "\n", "round-trip mismatch"
    assert validate(written.rstrip("\n").split("\n")) == text
    # The entry.txt shipped in this repo must carry exactly these two lines.
    repo_entry = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                              "entry.txt")
    if os.path.exists(repo_entry):
        with open(repo_entry, encoding="utf-8") as f:
            assert f.read() == written, "entry.txt differs from LINE1/LINE2"
    print(f"OK: wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
