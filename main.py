"""One Line, One Minute: The Vending Machine Pickup Line Contest.

A single original pickup line, at most 200 characters, spoken by a
vending machine to a passing human. Standard library only.
Deterministic: no randomness, no network, no clock. The entry is the
line at LINE, written to <MAKEFUN_OUTPUT_DIR>/entry.txt
(default /output/entry.txt).
"""

import os

LINE = "Press B4 if you're single: I'm fully stocked, I take exact change only, and unlike the chips in C2, I'll never get stuck when it's time to drop for you."


def main() -> None:
    line = LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, "entry must be 1 to 200 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != line + "\n":
        raise SystemExit("error: entry.txt read-back does not match the line")
    print(line)


if __name__ == "__main__":
    main()
