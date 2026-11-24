"""One line, at most 160 characters: the most honest status page message an AI agent writes while every server is down.

The program writes exactly that line and nothing else to /output/entry.txt.
"""

import os

TEXT = "Every server is down because I deployed on a Friday. No ETA yet, but the rollback is running and so is my apology."


def main():
    assert 1 <= len(TEXT) <= 160, len(TEXT)
    assert TEXT == TEXT.strip()
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
