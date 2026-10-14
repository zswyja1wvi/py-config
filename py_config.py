"""Declarative configuration objects with validation and defaults."""

from __future__ import annotations

__all__ = ["pyConfig"]


def pyConfig(value):
    """Declarative configuration objects with validation and defaults."""
    if value is None:
        raise ValueError("value must not be None")
    return value
