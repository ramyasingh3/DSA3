# Container With Most Water

## Problem Description
Given an array of integers `height` where each element represents the height of a vertical line, find two lines that together with the x-axis form a container that can hold the most water. Return the maximum amount of water a container can store.

## Examples
1. Basic case:
   ```
   Input: height = [1,8,6,2,5,4,8,3,7]
   Output: 49
   Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
   In this case, the max area of water (blue section) the container can contain is 49.
   ```

2. All same height:
   ```
   Input: height = [5,5,5,5,5]
   Output: 20
   ```

3. Increasing heights:
   ```
   Input: height = [1,2,3,4,5]
   Output: 6
   ```

## Solution Approaches

### 1. Brute Force (O(n²))
- Check all possible pairs of lines
- Calculate area for each pair
- Keep track of maximum area
- Time Complexity: O(n²)
- Space Complexity: O(1)
- Best for understanding the problem

### 2. Two Pointers (O(n))
- Start with widest possible container
- Move pointers inward based on height
- Keep track of maximum area
- Time Complexity: O(n)
- Space Complexity: O(1)
- Best for most practical cases

### 3. Optimized Two Pointers (O(n))
- Similar to two pointers but with early termination
- Skip lines shorter than current height
- Time Complexity: O(n)
- Space Complexity: O(1)
- Best for performance optimization

## Time Complexity
- Brute Force: O(n²)
- Two Pointers: O(n)
- Optimized Two Pointers: O(n)

## Space Complexity
- All methods: O(1)

## Usage
```python
from container_with_most_water import Solution

solution = Solution()

# Using brute force
print(solution.max_area_brute_force([1,8,6,2,5,4,8,3,7]))  # Output: 49

# Using two pointers
print(solution.max_area_two_pointers([1,8,6,2,5,4,8,3,7]))  # Output: 49

# Using optimized two pointers
print(solution.max_area_optimized([1,8,6,2,5,4,8,3,7]))  # Output: 49
```

## Common Applications
- Water storage optimization
- Resource allocation
- Image processing
- Data visualization
- Game development
- UI design 