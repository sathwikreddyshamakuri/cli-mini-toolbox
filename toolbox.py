#!/usr/bin/env python3
"""toolbox.py – CLI Mini-Toolbox.

Examples
--------
python toolbox.py digitsum 234
python toolbox.py wordcount "hello world"
python toolbox.py ctof 37
"""
import argparse
from typing import List

# ---------- utilities ----------
def digit_sum(n: int) -> int:
    return sum(int(d) for d in str(n))

def word_count(words: List[str]) -> int:
    return len(words)

def c_to_f(celsius: float) -> float:
    return celsius * 9 / 5 + 32

# ---------- CLI wiring ----------
def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="CLI Mini-Toolbox")
    sub = parser.add_subparsers(dest="cmd", required=True)

    ds = sub.add_parser("digitsum", help="Sum digits")
    ds.add_argument("number", type=int)

    wc = sub.add_parser("wordcount", help="Count words")
    wc.add_argument("words", nargs="+")

    tf = sub.add_parser("ctof", help="Celsius → Fahrenheit")
    tf.add_argument("celsius", type=float)
    return parser

def main() -> None:
    args = build_parser().parse_args()
    if args.cmd == "digitsum":
        print(digit_sum(args.number))
    elif args.cmd == "wordcount":
        print(word_count(args.words))
    elif args.cmd == "ctof":
        print(c_to_f(args.celsius))

if __name__ == "__main__":
    main()
