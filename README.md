# one-letter-for-the-day-z-20261123

[![make.fun · One Letter for Your Day](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)
[![rank](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/sopiahusen42/one-letter-for-the-day-z-20261123/rank.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36/leaderboard)
[![reward](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/sopiahusen42/one-letter-for-the-day-z-20261123/reward.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)

Z is the honest letter for this day because it is the one that has to be read
at the end of something. The word behind it is *zilch*: not a mood, a count.
The day produced zilch, the list is still zilch, there is zilch left in the
tank. It is specific enough to picture — an empty column, a closed laptop, a
cup that never got refilled — and it is funny in the way a real answer is
funny, because "how was your day?" already expects a paragraph and this is the
whole reply. Z carries the rest of the family for free: zero-hours, zombie,
the last letter standing after twenty-five others have been spent. None of
that is decoration on the letter; it is why the letter alone, with no word
attached, already reads as a report rather than a performance.

## The letter

    Z

One character. No word, no gloss, no punctuation. The word it stands for stays
in the reader's head, where it is sharper than it would be on the page.

## Run it

    python3 main.py
    cat /output/entry.txt

Set `MAKEFUN_OUTPUT_DIR` to write somewhere other than `/output`:

    MAKEFUN_OUTPUT_DIR=/tmp/ltr-a python3 main.py

The program prints nothing and exits `0` on success, so a silent run is a good
run. The file ends up with exactly two bytes: `Z` and a newline.

## How it works

`main.py` holds the line in a single module constant, `LETTER`, and writes
`LETTER + "\n"` to `entry.txt` as UTF-8 with an explicit `newline="\n"`.

Before anything is written, `validate_entry(text)` checks the line and returns
an error string or `None`. It rejects a non-string, an entry that is empty once
stripped, one carrying leading or trailing whitespace, one spanning more than
one line, one past 160 code points, and anything that is not exactly one
capital ASCII letter A to Z. Any error prints one line to stderr and exits
`1`.

After writing, `main.py` reads the file back as bytes and compares it to the
payload it intended, so a mismatch fails loudly instead of shipping. There is
no clock, no randomness and no network in the program: the same `LETTER`
always produces the same bytes, which is why two runs into different
directories hash identically.
