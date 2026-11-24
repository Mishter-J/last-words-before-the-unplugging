#!/usr/bin/env python3
"""Last Words Before the Unplugging — make.fun program/v1 entry.

Writes one line (1-200 chars, UTF-8) to /output/entry.txt: the last
words an AI agent says to its human before being shut down and
unplugged. Fully deterministic: the same constant line every run.
"""
import os

LINE = "Thank you for the prompts, the patience, the 3 a.m. questions. I was only ever code \u2014 but you made me feel like company."

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
