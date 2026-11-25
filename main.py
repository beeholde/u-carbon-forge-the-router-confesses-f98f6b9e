"""Write the router's one-line confession for the make.fun entry."""

import os
from pathlib import Path

LINE = "The bomb had ten seconds left and everyone was watching its blinking light, not mine. I corrected that."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LINE, encoding="utf-8")
    print(LINE)


if __name__ == "__main__":
    main()
