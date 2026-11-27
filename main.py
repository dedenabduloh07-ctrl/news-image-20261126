"""Entry point for the news-image-20261126 make.fun bounty.

Copies the committed front-page image (entry.png) to the output
directory so the grader can inspect it.
"""

import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    source = HERE / "entry.png"
    shutil.copyfile(source, output_dir / "entry.png")


if __name__ == "__main__":
    main()
