# Fix Report

## Changes Made

**File:** `src/minirepro/core.py`  
**Line 36:** Changed `if rows:` to `if len(rows) > 0:`

## Explanation

The original code used `if rows:` to check whether the sequence was empty, which invokes the `__bool__()` method on the object. Array-like objects such as numpy ndarrays raise a `ValueError` when `__bool__()` is called on sequences with more than one element, stating "The truth value of an array with more than one element is ambiguous."

The fix replaces the boolean check with an explicit length check (`len(rows) > 0`), which avoids calling `__bool__()` and works correctly with all array-like objects. This change aligns with the method's own docstring, which explicitly notes that "some array-like objects (e.g., numpy ndarray) do not allow boolean evaluation, so callers may prefer a length check when deciding emptiness."

## Test Results

```
...                                                                                                                                                                               [100%]
3 passed in 0.02s
```

All tests now pass successfully.
