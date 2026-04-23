def compute(a, b):
    """Return a + b * 2."""
    return a + b * 2


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python ab_formula.py <a> <b>", file=sys.stderr)
        sys.exit(1)
    a, b = float(sys.argv[1]), float(sys.argv[2])
    print(compute(a, b))
