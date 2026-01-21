from __future__ import annotations

import sys
from pathlib import Path

import pytest


# Make `src/` importable without packaging.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from minirepro import PrettyTable  # noqa: E402


class AmbiguousBoolRows:
    """A tiny array-like object that mimics numpy's ambiguous truth value.

    - Slicing returns a plain list (enough for rows[:-1]).
    - __bool__ raises ValueError if it has >1 element.
    """

    def __init__(self, rows):
        self._rows = list(rows)

    def __len__(self):
        return len(self._rows)

    def __getitem__(self, item):
        return self._rows[item]

    def __iter__(self):
        return iter(self._rows)

    def __bool__(self):
        if len(self._rows) != 1 and len(self._rows) != 0:
            raise ValueError(
                "The truth value of an array with more than one element is ambiguous. "
                "Use a.any() or a.all()"
            )
        return bool(self._rows)


def test_add_rows_handles_array_like_without_boolean_evaluation():
    t = PrettyTable()
    rows = AmbiguousBoolRows([[1, 2, 3], [11, 12, 13]])

    t.add_rows(rows)
    assert t._rows == [[1, 2, 3], [11, 12, 13]]


def test_add_rows_empty_sequence_is_noop():
    t = PrettyTable()
    t.add_rows([])
    assert t._rows == []


def test_add_rows_divider_only_on_last_row():
    t = PrettyTable()
    rows = AmbiguousBoolRows([[1, 2, 3], [11, 12, 13]])

    t.add_rows(rows, divider=True)
    assert t._dividers == [False, True]
