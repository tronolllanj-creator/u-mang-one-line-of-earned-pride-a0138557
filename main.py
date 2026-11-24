"""
# Entry validated: output is 1-240 chars, one line, deterministic.
Entry point for the grader. Writes a specific line to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os
import sys

LINE = "The night cleaner smoothed the folded sticky note flat against the mahogany desktop she had polished for six years, reading the clumsy ink through bifocals she had bought herself last November.\n"

def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")

    content = LINE
    if not (1 <= len(content) <= 240 and content.strip()):
        raise ValueError("Content length or whitespace validation failed.")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(output_path)
    print(len(content))

if __name__ == "__main__":
    main()
