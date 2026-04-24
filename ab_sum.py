"""Compute the expression a + b * 3."""


def compute(a: float, b: float) -> float:
    return a + b * 3


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Print a + b * 3.")
    parser.add_argument("a", type=float, help="Value of a")
    parser.add_argument("b", type=float, help="Value of b")
    args = parser.parse_args()
    print(compute(args.a, args.b))
