# Longest Increasing Subsequence

## Problem Description
Given an integer array `nums`, return the length of the longest strictly increasing subsequence. A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.

### Examples
1. Input: nums = [10,9,2,5,3,7,101,18]
   Output: 4
   Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

2. Input: nums = [0,1,0,3,2,3]
   Output: 4
   Explanation: The longest increasing subsequence is [0,1,2,3], therefore the length is 4.

3. Input: nums = [7,7,7,7,7,7,7]
   Output: 1
   Explanation: The longest increasing subsequence is [7], therefore the length is 1.

## Approach
The solution uses dynamic programming with binary search:
1. Maintain a list `tails` where `tails[i]` represents the smallest possible tail value for all increasing subsequences of length `i+1`.
2. For each number in `nums`:
   - If the number is larger than all tails, append it to the list
   - Otherwise, use binary search to find the first tail that is larger than the number and replace it
3. The length of `tails` at the end is the length of the longest increasing subsequence

## Time Complexity
- O(n log n) where n is the length of the array
- We process each number once
- For each number, we perform a binary search which takes O(log n) time

## Space Complexity
- O(n) for the `tails` array
- In the worst case, we might need to store all elements
- Overall: O(n) 