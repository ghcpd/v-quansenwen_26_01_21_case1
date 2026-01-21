# Bug Fix Report

## Change Made

In `src/minirepro/core.py`, line 36, changed `if rows:` to `if len(rows):`.

## Explanation

The `add_rows` method used boolean evaluation (`if rows:`) to check if the rows sequence was non-empty before adding the last row. However, numpy-like array objects raise a `ValueError` when their boolean value is evaluated if they contain more than one element (the truth value is ambiguous). The fix uses `len(rows)` instead, which explicitly checks the length of the sequence without triggering boolean evaluation. This makes `add_rows` compatible with any array-like object that implements `__len__`, including numpy arrays.

## Diff

```diff
--- a/src/minirepro/core.py
+++ b/src/minirepro/core.py
@@ -33,7 +33,7 @@ class PrettyTable:
             self.add_row(row)

         # Add the final row if any.
-        if rows:
+        if len(rows):
             self.add_row(rows[-1], divider=divider)
```

## Test Results

```
...                                                                      [100%]
3 passed in 0.02s
```
