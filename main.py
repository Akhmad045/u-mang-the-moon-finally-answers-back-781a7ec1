"""The Moon Finally Answers Back - entry program.

Writes the Moon's one-line comeback to /output/entry.txt.
The line: "You call me beautiful, then wish for a parking space.
I am the Moon, not a valet."
"""

import os

LINE = "You call me beautiful, then wish for a parking space. I am the Moon, not a valet."


def main() -> None:
    line = LINE.strip()
    if not line or len(line) > 240:
        raise ValueError("entry must be one line of 1-240 characters")
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
