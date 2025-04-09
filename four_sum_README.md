# 4Sum

## Problem Description
Given an array of integers `nums` and an integer `target`, return all unique quadruplets `[nums[i], nums[j], nums[k], nums[l]]` such that `i != j != k != l` and `nums[i] + nums[j] + nums[k] + nums[l] == target`.

## Examples
1. Basic case:
   ```
   Input: nums = [1,0,-1,0,-2,2], target = 0
   Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
   ```

2. No solution:
   ```
   Input: nums = [1,2,3,4,5], target = 20
   Output: []
   ```

3. All zeros:
   ```
   Input: nums = [0,0,0,0,0], target = 0
   Output: [[0,0,0,0]]
   ```

## Solution Approaches

### 1. Brute Force (O(n⁴))
- Check all possible quadruplets
- Time Complexity: O(n⁴)
- Space Complexity: O(1)
- Best for understanding the problem

### 2. Two Pointers (O(n³))
- Sort the array
- Use four pointers (i, j, left, right)
- Skip duplicates
- Time Complexity: O(n³)
- Space Complexity: O(1)
- Best for most practical cases

### 3. Hash Set (O(n³))
- Sort the array
- Use hash set to store pairs
- Skip duplicates
- Time Complexity: O(n³)
- Space Complexity: O(n²)
- Best when memory is not a concern

## Time Complexity
- Brute Force: O(n⁴)
- Two Pointers: O(n³)
- Hash Set: O(n³)

## Space Complexity
- Brute Force: O(1)
- Two Pointers: O(1)
- Hash Set: O(n²)

## Usage
```python
from four_sum import Solution

solution = Solution()

# Using brute force
print(solution.four_sum_brute_force([1,0,-1,0,-2,2], 0))  # Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

# Using two pointers
print(solution.four_sum_two_pointers([1,0,-1,0,-2,2], 0))  # Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

# Using hash set
print(solution.four_sum_hash([1,0,-1,0,-2,2], 0))  # Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
```

## Common Applications
- Finding quadruplets in data analysis
- Financial calculations
- Resource allocation
- Scheduling problems
- Network routing
- Database queries 