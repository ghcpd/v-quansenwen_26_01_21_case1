Fixed PrettyTable.add_rows to check the length before adding the final row, avoiding boolean evaluation of array-like inputs with ambiguous truth values.
This keeps add_rows working for numpy-like sequences while preserving existing behavior for normal iterables.
Verified with python -m pytest -q (3 passed).
