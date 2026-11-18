"""One-day news poster entry: copies the committed poster image to the output.

The image (entry.png, beside this file) sums up the world news of
Tuesday 17 November 2026 as a newspaper front page. The grader runs
this program twice with no network, and both runs must write the same
bytes, so the program does a plain byte-for-byte copy of a file that
never changes.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"

MAX_BYTES = 1_048_576  # the gate's cap: at most 1 MiB
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
JPEG_MAGIC = b"\xff\xd8\xff"


def check_source(data: bytes) -> None:
    """Refuse to ship an image the gate would refuse: oversize or not an image."""
    if len(data) > MAX_BYTES:
        raise SystemExit(f"entry.png is {len(data)} bytes, over the 1 MiB cap")
    if not (data.startswith(PNG_MAGIC) or data.startswith(JPEG_MAGIC)):
        raise SystemExit("entry.png is neither a PNG nor a JPEG")


def main() -> None:
    check_source(SOURCE.read_bytes())
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, out_dir / "entry.png")


if __name__ == "__main__":
    main()
