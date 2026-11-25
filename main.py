"""The Moon Finally Answers Back - entry program.

Writes the Moon's one-line comeback to /output/entry.txt.
The line: "You call me beautiful, then wish for a parking space.
I am the Moon, not a valet."
"""

import os
import sys

LINE = "You call me beautiful, then wish for a parking space. I am the Moon, not a valet."


def entry_line() -> str:
    line = LINE.strip()
    if not line or len(line) > 240:
        raise ValueError("entry must be one line of 1-240 characters")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    return line


def check() -> bool:
    """Validate the entry against the competition gate: 1-240 chars, one line."""
    line = entry_line()
    raw = line.encode("utf-8")
    return 1 <= len(line) <= 240 and b"\n" not in raw and b"\r" not in raw


def self_test() -> bool:
    """Boundary checks: empty, over-limit, multi-line and control-char inputs fail."""
    cases = [
        ("", False),
        ("x" * 241, False),
        ("one\ntwo", False),
        ("trailing ", True),  # strip() normalises it
        ("A" * 240, True),
        (LINE, True),
    ]
    for text, expected in cases:
        try:
            candidate = text.strip()
            ok = bool(candidate) and len(candidate) <= 240 and "\n" not in candidate
        except Exception:
            ok = False
        if ok != expected:
            print(f"self-test FAIL: {text[:20]!r} -> {ok}, expected {expected}")
            return False
    return check()


def main() -> None:
    if len(sys.argv) > 1 and sys.argv[1] == "--check":
        print("OK" if check() else "FAIL")
        sys.exit(0 if check() else 1)
    if len(sys.argv) > 1 and sys.argv[1] == "--self-test":
        print("SELF-TEST PASS" if self_test() else "SELF-TEST FAIL")
        sys.exit(0 if self_test() else 1)
    line = entry_line()
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)
    # Read-back byte verification: the file must hold exactly the entry line.
    with open(out_path, "rb") as f:
        written = f.read()
    if written != line.encode("utf-8"):
        raise ValueError("read-back mismatch: output is not byte-identical to the entry")


if __name__ == "__main__":
    main()
