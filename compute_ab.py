"""Compute a + b * 5."""


def compute(a: float, b: float) -> float:
    return a + b * 5


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Compute a + b * 5")
    parser.add_argument("a", type=float, help="value a")
    parser.add_argument("b", type=float, help="value b")
    args = parser.parse_args()
    print(compute(args.a, args.b))
