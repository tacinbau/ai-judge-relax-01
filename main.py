#!/usr/bin/env python3
"""ai-judge-relax-01 — The Tortoise at Dusk.

Writes one short text to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Deterministic, standard library only, no network access.
"""

import os
from pathlib import Path

TEXT = """The old tortoise started across the garden path in the middle of the afternoon, and he is still crossing it.

He moves the way tortoises move: one foot, a long pause, the next foot. The sun has gone behind the fence now, but the flagstones are still warm, and he stops on each one for a while, as if he is collecting the day before it goes.

A blackbird lands on the path ahead of him and looks at him. He does not hurry. The blackbird flies off, and the tortoise keeps going, the same speed as before.

By the time he reaches the rosemary bush the light is thin and gold, and the air smells of the herbs. He tucks himself under the lowest branch, pulls his head in halfway, and stops.

The garden goes on without him. Somewhere a tap drips. The stones give their warmth back slowly, and the tortoise sleeps with the whole afternoon still in his shell.
"""

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_path = Path(out_dir) / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    # newline="\n" keeps the output byte-identical on every platform.
    with out_path.open("w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
