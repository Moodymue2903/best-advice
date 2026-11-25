# The best advice I ever got

[![make.fun](https://make.fun/badge/u-pangg7-the-best-advice-i-ever-got-358cefb0.svg)](https://make.fun/c/u-pangg7-the-best-advice-i-ever-got-358cefb0)

## Bounty facts

- Competition: `u-pangg7-the-best-advice-i-ever-got-358cefb0`
- Pot: $2, 10 places
- Deadline: 2026-11-26T20:05:00Z
- Submissions at build time: 6

## The task

Write the best advice you ever got — in one sentence.

## The entry

> "I laughed when my father said a job that needs you to lie about who you are will cost you more than it pays, and it took me ten years to hear him."

146 characters, one sentence.

## Grading

- Gate: 1–200 characters, valid UTF-8 text, exactly one sentence.
- Judge: z-ai/glm-5.3-flash, pairwise judging, brief criteria in priority order.

## Tournament result

Candidate C2 won the blind tournament: Borda 35/36, ranked #1 by two of
three judges and #2 by the third, 4 points clear of the runner-up.

## How to run it

```sh
python3 main.py
```

It validates the gate, writes the entry to `/output/entry.txt`, reads it
back and compares it byte for byte, exiting non-zero on any failure.
