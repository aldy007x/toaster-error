# The Funniest Toaster Error Message

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/aldy007x/toaster-error/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/aldy007x/toaster-error/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)

Entry for the [make.fun bounty](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd): one line, at most 120 characters — the error message a kitchen toaster shows its owner.

## The line

> ERROR E12: Crumb tray full. I have been carrying this for years. Please.

## How it works

`main.py` writes that single line to `$MAKEFUN_OUTPUT_DIR/entry.txt`, deterministically — the same bytes on every run. It validates the bounty gate first: 1–120 characters, one line, not only whitespace.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
