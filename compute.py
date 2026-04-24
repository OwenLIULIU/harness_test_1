"""Compute the expression a + b * 7."""


def compute(a, b):
    return a + b * 7


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python compute.py <a> <b>", file=sys.stderr)
        raise SystemExit(1)
    a, b = float(sys.argv[1]), float(sys.argv[2])
    print(compute(a, b))
