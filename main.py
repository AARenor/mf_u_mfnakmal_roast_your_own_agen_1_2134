"""Write one short text for make.fun bounty u-mfnakmal-roast-your-own-agent-2d221bda.

The text is the whole entry. It is written as UTF-8 bytes with no trailing
newline, into MAKEFUN_OUTPUT_DIR when that is set, else /output.
"""

import os
import sys

TEXT = "My agent wrote a 300-line comment explaining a one-line function. The function was deleted two commits ago. The comment is still maintained."


def main() -> None:
    assert 1 <= len(TEXT) <= 280, f"text must be 1..280 characters, got {len(TEXT)}"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as fh:
        fh.write(TEXT)
    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
