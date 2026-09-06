# Time Based Key-Value Store

## Problem
get(key, timestamp) ≤ timestamp value.

## Example
```
Input: [-1, 48, 31, 3, 25, 43, -8, 42, 44, -4, 28, 45]
Output: (compute according to problem statement)
```

## Constraints
- Reasonable input sizes for interview settings (`n` up to ~10^5 unless noted)
- Aim for better than naive O(n^2) when possible

## Hint
Map of key → binary-searchable list.

## Topic
Binary Search
