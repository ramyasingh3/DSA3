# UTF-8 Validation

## Problem
Validate byte sequence as UTF-8.

## Example
```
Input: [16, 13, -4, 10, 17, 43, 10, 9, 13]
Output: (compute according to problem statement)
```

## Constraints
- Reasonable input sizes for interview settings (`n` up to ~10^5 unless noted)
- Aim for better than naive O(n^2) when possible

## Hint
Track remaining continuation bytes.

## Topic
Bit Manipulation
