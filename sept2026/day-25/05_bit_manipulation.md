# Counting Bits

## Problem
Number of 1-bits for 0..n.

## Example
```
Input: [43, 6, 12, 7, 41, 10, 4, 15, 23, 21]
Output: (compute according to problem statement)
```

## Constraints
- Reasonable input sizes for interview settings (`n` up to ~10^5 unless noted)
- Aim for better than naive O(n^2) when possible

## Hint
DP: ans[i] = ans[i>>1] + (i&1).

## Topic
Bit Manipulation
