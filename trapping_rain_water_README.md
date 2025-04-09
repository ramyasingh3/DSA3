# Trapping Rain Water

## Problem Description
Given an array of integers `height` where each element represents the height of a bar, calculate how much water can be trapped between the bars after raining.

## Examples
1. Basic case:
   ```
   Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
   Output: 6
   Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
   In this case, 6 units of rain water (blue section) are being trapped.
   ```

2. All same height:
   ```
   Input: height = [5,5,5,5,5]
   Output: 0
   ```

3. Increasing heights:
   ```
   Input: height = [1,2,3,4,5]
   Output: 0
   ```

## Solution Approaches

### 1. Brute Force (O(n²))
- For each position, find max height to left and right
- Calculate water at current position
- Time Complexity: O(n²)
- Space Complexity: O(1)
- Best for understanding the problem

### 2. Dynamic Programming (O(n))
- Precompute left and right max arrays
- Use precomputed arrays to find water at each position
- Time Complexity: O(n)
- Space Complexity: O(n)
- Best for clarity and understanding

### 3. Two Pointers (O(n))
- Use two pointers to track left and right boundaries
- Keep track of left and right max heights
- Time Complexity: O(n)
- Space Complexity: O(1)
- Best for performance and space efficiency

## Time Complexity
- Brute Force: O(n²)
- Dynamic Programming: O(n)
- Two Pointers: O(n)

## Space Complexity
- Brute Force: O(1)
- Dynamic Programming: O(n)
- Two Pointers: O(1)

## Usage
```python
from trapping_rain_water import Solution

solution = Solution()

# Using brute force
print(solution.trap_brute_force([0,1,0,2,1,0,1,3,2,1,2,1]))  # Output: 6

# Using dynamic programming
print(solution.trap_dp([0,1,0,2,1,0,1,3,2,1,2,1]))  # Output: 6

# Using two pointers
print(solution.trap_two_pointers([0,1,0,2,1,0,1,3,2,1,2,1]))  # Output: 6
```

## Common Applications
- Water resource management
- Urban planning
- Flood prediction
- Terrain analysis
- Game development
- Data visualization 