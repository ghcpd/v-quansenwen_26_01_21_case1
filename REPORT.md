# Bug Fix Report

## Change Made

In `src/minirepro/core.py`, line 36, changed `if rows:` to `if len(rows) > 0:`.

## Explanation

The original code used a boolean evaluation (`if rows:`) to check if the `rows` sequence was non-empty before adding the final row. This triggers the `__bool__` method on the sequence object, which fails for numpy-like array objects containing more than one element (they raise `ValueError: The truth value of an array with more than one element is ambiguous`). The fix uses `len(rows) > 0` instead, which calls `__len__` rather than `__bool__`, correctly handling array-like objects that don't support boolean evaluation. This aligns with the docstring's own recommendation to use length checks for emptiness.
