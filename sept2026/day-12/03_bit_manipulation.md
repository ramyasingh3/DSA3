# UTF-8 Validation

## Problem
Validate byte sequence as UTF-8.

## Example
```
Input: [49, 6, -20, 20, 47, -18, 41, 11, -16, 45, -19]
Output: (compute according to problem statement)
```

## Constraints
- Reasonable input sizes for interview settings (`n` up to ~10^5 unless noted)
- Aim for better than naive O(n^2) when possible

## Hint
Track remaining continuation bytes.

## Topic
Bit Manipulation
