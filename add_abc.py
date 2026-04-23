"""Compute the sum a + b + c."""


def add_abc(a, b, c):
    return a + b + c


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Print a + b + c.")
    parser.add_argument("a", type=float, help="First number")
    parser.add_argument("b", type=float, help="Second number")
    parser.add_argument("c", type=float, help="Third number")
    args = parser.parse_args()
    print(add_abc(args.a, args.b, args.c))
