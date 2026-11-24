"""The Funniest Toaster Error Message — make.fun entry.

Writes a single deadpan error message, the kind a kitchen toaster would
show its owner, to $MAKEFUN_OUTPUT_DIR/entry.txt. The gate requires
1-120 characters of UTF-8 text, one line, not only whitespace.
"""

import os

LINE = "ERROR E12: Crumb tray full. I have been carrying this for years. Please."


def validate(line: str) -> None:
    """Enforce the bounty gate: 1-120 chars, one line, not blank."""
    if not line.strip():
        raise ValueError("entry line must not be blank")
    if len(line) > 120:
        raise ValueError(f"entry line is {len(line)} chars, over the 120 limit")
    if "\n" in line.strip():
        raise ValueError("entry line must be a single line")


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
