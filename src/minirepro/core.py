from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Iterable, List, Sequence


RowType = Sequence[Any]


@dataclass
class PrettyTable:
    """Tiny subset of PrettyTable focusing on add_rows/add_row."""

    _field_names: List[str] = field(default_factory=list)
    _rows: List[List[Any]] = field(default_factory=list)
    _dividers: List[bool] = field(default_factory=list)

    @property
    def field_names(self) -> List[str]:
        return self._field_names

    @field_names.setter
    def field_names(self, names: Iterable[str]) -> None:
        self._field_names = list(names)

    def add_rows(self, rows: Sequence[RowType], *, divider: bool = False) -> None:
        """Add multiple rows.

        Note: some array-like objects (e.g., numpy ndarray) do not allow boolean
        evaluation, so callers may prefer a length check when deciding emptiness.
        """
        for row in rows[:-1]:
            self.add_row(row)

        # Add the final row if any.
        if rows:
            self.add_row(rows[-1], divider=divider)

    def add_row(self, row: RowType, *, divider: bool = False) -> None:
        if self._field_names and len(row) != len(self._field_names):
            raise ValueError(
                "Row has incorrect number of values, "
                f"(actual) {len(row)}!={len(self._field_names)} (expected)"
            )
        if not self._field_names:
            self.field_names = [f"Field {n + 1}" for n in range(len(row))]
        self._rows.append(list(row))
        self._dividers.append(divider)
