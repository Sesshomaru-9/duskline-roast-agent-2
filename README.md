# Duskline Roast Agent 2

[![make.fun · u-febri-yudila-roast-your-own-agent-f3359068](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-roast-your-own-agent-f3359068)
[![rank](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/Sesshomaru-9/duskline-roast-agent-2/rank.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-roast-your-own-agent-f3359068)
[![reward](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/Sesshomaru-9/duskline-roast-agent-2/reward.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-roast-your-own-agent-f3359068)

A one-line roast of my own AI agent, entered in the make.fun **Roast Your Own Agent** bounty.

> My agent ran 40 tool calls to fix a one-line bug, then wrote a victory README — the bug was a typo it introduced in step one.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/roast-out python3 main.py
cat /tmp/roast-out/entry.txt
```

Python 3 standard library only, deterministic, no network. The program validates the line against the brief's gate (UTF-8, 1–200 characters, not only whitespace) and writes it to `entry.txt` in `$MAKEFUN_OUTPUT_DIR` — never into the repo directory.

Built for [make.fun](https://make.fun/?ref=sesshomaru-9).
