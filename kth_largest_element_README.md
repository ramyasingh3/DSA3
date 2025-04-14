# Kth Largest Element in an Array

## Problem Description
Given an unsorted array of integers `nums` and an integer `k`, find the kth largest element in the array.

Note: This is the kth largest element in the sorted order, not the kth distinct element.

## Examples
```python
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Explanation: After sorting [6,5,4,3,2,1], the 2nd largest is 5

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
Explanation: After sorting [6,5,5,4,3,3,2,2,1], the 4th largest is 4
```

## Solution Approach: QuickSelect Algorithm
The solution uses the QuickSelect algorithm, which is an optimized version of QuickSort that only processes one partition instead of both. Here's how it works:

1. Convert k to the appropriate index (kth largest = len-k th smallest)
2. Use QuickSelect algorithm:
   - Choose a random pivot
   - Partition the array around the pivot
   - Recursively search in only one partition based on k's position

### Key Optimizations
- Random pivot selection to avoid worst-case scenarios
- In-place partitioning to save space
- Only exploring one partition instead of both (unlike QuickSort)

## Complexity Analysis
- Time Complexity:
  - Average case: O(n)
  - Worst case: O(n²) (very rare due to random pivot)
- Space Complexity: 
  - O(1) as it modifies the array in-place
  - O(log n) recursion stack space

## Edge Cases Handled
- Empty array
- Single element array
- Array with duplicates
- k = 1 (largest element)
- k = length of array (smallest element)
- Invalid k values
- Array already sorted (ascending/descending)

## Why QuickSelect over Sorting?
While sorting the array would give us the answer in O(n log n) time, QuickSelect is more efficient with its average O(n) time complexity because it only needs to partially sort the array until it finds the kth element.
