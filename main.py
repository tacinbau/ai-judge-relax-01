import os
from pathlib import Path

TEXT = """By late evening the fire had burned itself down to embers, and the hearth held only a low red glow.

One coal at a time, the bright edges dimmed, and the light drew back toward the centre of the grate.

Ash settled softly over the coals, grey and fine, while the last small flames rose, flickered once, and did not return.

The room darkened around the hearth, the chairs and the rug losing their colour, and the house grew quiet, with only the faint tick of cooling iron.

Outside, the night stayed cold and still, and inside, the stones of the hearth kept their warmth, holding it gently through the long hours until morning.

Nothing more moved, and the embers slept beneath their ash, warm and dark and waiting for the dawn.
"""

def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(TEXT, encoding="utf-8")

if __name__ == "__main__":
    main()
