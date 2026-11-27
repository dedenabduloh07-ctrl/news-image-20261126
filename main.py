"""Entry point for the news-image-20261126 make.fun bounty.

Copies the committed front-page image (entry.png) to the output
directory so the grader can inspect it.
"""

import hashlib
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    source = HERE / "entry.png"
    if not source.is_file():
        print(f"ERROR: source image missing: {source}", file=sys.stderr)
        raise SystemExit(1)
    destination = output_dir / "entry.png"
    shutil.copyfile(source, destination)
    if _sha256(destination) != _sha256(source):
        print("ERROR: copied entry.png does not match source (sha256 mismatch)",
              file=sys.stderr)
        raise SystemExit(1)
    print(f"OK: entry.png copied ({source.stat().st_size} bytes, "
          f"sha256 {_sha256(source)[:16]}...)")


if __name__ == "__main__":
    main()
