def add(a, b):
    """Return the sum of a and b."""
    return a + b


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 3:
        x, y = float(sys.argv[1]), float(sys.argv[2])
        print(add(x, y))
    else:
        print("Usage: python add.py <a> <b>")
