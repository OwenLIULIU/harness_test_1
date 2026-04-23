#!/usr/bin/env python3
"""
Compute the expression: a + b * 4
"""

from __future__ import annotations

import argparse


def compute(a: float, b: float) -> float:
    return a + b * 4.0


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Compute a + b * 4 from two numbers a and b.",
    )
    parser.add_argument("a", type=float, help="Value of a")
    parser.add_argument("b", type=float, help="Value of b")
    args = parser.parse_args()
    result = compute(args.a, args.b)
    print(result)


if __name__ == "__main__":
    main()
