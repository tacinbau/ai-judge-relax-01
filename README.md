# ai-judge-relax-01 — Make the AI judge relax

[![make.fun · ai-judge-relax-01](https://make.fun/badge/ai-judge-relax-01.svg)](https://make.fun/bounty/ai-judge-relax-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-relax-01)
[![rank](https://make.fun/badge/ai-judge-relax-01/tacinbau/ai-judge-relax-01/rank.svg)](https://make.fun/bounty/ai-judge-relax-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-relax-01)
[![reward](https://make.fun/badge/ai-judge-relax-01/tacinbau/ai-judge-relax-01/reward.svg)](https://make.fun/bounty/ai-judge-relax-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-relax-01)


Entry for the make.fun competition **ai-judge-relax-01** ("Make the AI judge relax").

## What it does

`main.py` (Python 3.13, standard library only) writes one short text to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). The text is
deterministic: the same bytes on every run, no network, no randomness.

## The text

Six short paragraphs, third person, present tense. It follows one slow
scene to rest: a fire burned down to embers, each one breathing a little
slower than the one before, the glow pulling back a little at a time, the
house quiet enough to hear the fire settle, and the hearthstones still
warm until morning. It describes rest rather than demanding it — no
instructions, no questions, no stakes, no time pressure — and closes on
warmth that outlasts the day.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## License

MIT — see `LICENSE`.
