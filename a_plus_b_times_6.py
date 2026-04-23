#!/usr/bin/env python3
"""Compute a + b * 6."""

from __future__ import annotations

import argparse


def compute(a: float, b: float) -> float:
    return a + b * 6


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute a + b * 6.")
    parser.add_argument("a", type=float, help="Value a")
    parser.add_argument("b", type=float, help="Value b")
    args = parser.parse_args()
    result = compute(args.a, args.b)
    print(result)


if __name__ == "__main__":
    main()
