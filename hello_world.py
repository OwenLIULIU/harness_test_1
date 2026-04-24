"""Hello world and a little developer humor."""

import random


def say_hello() -> None:
    print("Hello, world!")


_DEVELOPER_JOKES: tuple[str, ...] = (
    "There are 10 kinds of people: those who understand binary and those who get stuck on the punchline.",
    "A SQL query walks into a bar, sees two tables, and asks: 'Can I JOIN you?'",
    "Why do programmers like dark mode? Because light attracts bugs.",
    "Debugging is like being the detective in a crime movie where you are also the murderer.",
    "I have a great joke about UDP, but you might not get it.",
    "I would tell you a joke about time zones, but your local offset may vary.",
    "The code works on my machine. If it fails on yours, please replace your machine.",
)


def print_random_funny_developer_joke() -> None:
    """Print one developer joke chosen at random."""
    print(random.choice(_DEVELOPER_JOKES))


def main() -> None:
    say_hello()
    print_random_funny_developer_joke()


if __name__ == "__main__":
    main()
