"""General-purpose utilities."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any


def flatten(nested: Sequence[Any]) -> list[Any]:
    """Recursively flatten nested lists into a single list (arbitrary depth)."""
    flat: list[Any] = []
    for item in nested:
        if isinstance(item, list):
            flat.extend(flatten(item))
        else:
            flat.append(item)
    return flat
