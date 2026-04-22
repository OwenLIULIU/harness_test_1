"""Print a greeting and the current date."""

from datetime import date


def main() -> None:
    today = date.today()
    print(f"Hello! Today is {today:%Y-%m-%d} ({today:%A}).")


if __name__ == "__main__":
    main()
