# Two Sum

## Problem Description
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

### Examples
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]
Explanation: Because nums[1] + nums[2] == 6, we return [1, 2].
```

## Approach
1. Use a hash map (dictionary) to store the complement of each number
2. For each number in the array:
   - Check if its complement (target - number) exists in the hash map
   - If found, return the indices
   - If not found, store the current number and its index in the hash map

### Key Points
- One-pass solution using hash map
- O(1) lookups for complements
- Handles negative numbers and zero
- Assumes exactly one solution exists

## Time Complexity
- O(n) where n is the length of the array
  - We traverse the array exactly once
  - Each hash map operation is O(1)

## Space Complexity
- O(n) to store the hash map
  - In the worst case, we might need to store all elements 