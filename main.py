# SPDX-License-Identifier: MIT
"""ai-judge-relax-01: write one short, settling text to /output/entry.txt.

The text is a quiet evening scene, built one concrete image at a time:
the day ending, rain on the roof, late light, a kettle gone still,
steam thinning into the air, one unhurried breath, and a house at
rest. No instructions, no questions, no stakes — only the scene,
so the calm comes from the reading itself.
"""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = (
    "The day is done, and nothing more is asked of it.\n"
    "Rain moves across the roof in a slow, even line.\n"
    "Late light rests on the windowsill, amber and still.\n"
    "The kettle has gone quiet. The water settles in the pot.\n"
    "Steam rises from a cup and thins into the quiet air.\n"
    "One breath comes in, unhurried, and goes out the same way.\n"
    "Light moves across the wall the way water moves, slow and unhurried.\n"
    "The house has settled into its own slow rhythm.\n"
    "Nothing here needs an answer. Nothing is waiting.\n"
    "The evening is long enough, and rest is enough.\n"
)


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
        f.write(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
