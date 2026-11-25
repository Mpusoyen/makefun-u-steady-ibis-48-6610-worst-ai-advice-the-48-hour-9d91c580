#!/usr/bin/env python3
"""Write one line of terrible AI advice to /output/entry.txt."""

import os
from pathlib import Path

LINE = "Absolutely! Pour a kettle of boiling water over your frozen windshield — it defrosts in seconds, and that loud crack means it's working!"


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
