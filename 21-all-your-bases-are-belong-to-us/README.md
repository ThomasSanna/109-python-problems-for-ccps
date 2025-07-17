# 21. All your bases are belong to us

## Problem Description

Given `n` identical coins on a table, perform the following operation repeatedly until no coins remain:

1. Arrange the coins into groups of exactly `out` coins per group (`out > 1`).
2. Take aside and record the leftover coins (`n % out`) that do not make a complete group.
3. From each complete group, place exactly `ins` coins back on the table.
4. Repeat with the new number of coins.

Return a list documenting how many coins were taken aside in each move.

This process produces the digits of `n` in base `out` (in reverse order), and works for fractional bases `out/ins` where `out > ins` and `gcd(out, ins) == 1`.

## Function Signature

```python
def group_and_skip(n, out, ins):
```

## Examples

| n         | out | ins | Expected result                   |
|-----------|-----|-----|-----------------------------------|
| 13        | 3   | 2   | [1, 2, 1, 2]                      |
| 123456789 | 10  | 1   | [9, 8, 7, 6, 5, 4, 3, 2, 1]       |
| 987654321 | 1000| 1   | [321, 654, 987]                   |
| 255       | 2   | 1   | [1, 1, 1, 1, 1, 1, 1, 1]          |
| 81        | 5   | 3   | [1, 3, 2, 0, 4, 3]                |
| 10**9     | 13  | 3   | [12, 1, 2, 0, 7, 9, 8, 11, 6, 8, 10, 5, 8, 3] |

## Notes

- The algorithm generalizes base conversion to fractional bases.
- Works for any `out > ins` and `gcd(out, ins) == 1`.