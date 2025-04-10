# Maximum Subarray

## Problem Description
Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

## Examples
1. Basic case:
   ```
   Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
   Output: 6
   Explanation: [4, -1, 2, 1] has the largest sum = 6
   ```

2. All negative:
   ```
   Input: nums = [-2, -1, -3, -4]
   Output: -1
   Explanation: [-1] has the largest sum = -1
   ```

3. All positive:
   ```
   Input: nums = [1, 2, 3, 4]
   Output: 10
   Explanation: The entire array has the largest sum = 10
   ```

## Solution Approaches

### 1. Kadane's Algorithm (O(n))
- Uses dynamic programming to track maximum subarray sum
- Time Complexity: O(n)
- Space Complexity: O(1)
- Best for most cases

### 2. Divide and Conquer (O(n log n))
- Divides array into halves and combines results
- Time Complexity: O(n log n)
- Space Complexity: O(log n)
- Good for understanding divide and conquer

### 3. Brute Force (O(n²))
- Checks all possible subarrays
- Time Complexity: O(n²)
- Space Complexity: O(1)
- Simple but inefficient

## Time Complexity
- Kadane's Algorithm: O(n)
- Divide and Conquer: O(n log n)
- Brute Force: O(n²)

## Space Complexity
- Kadane's Algorithm: O(1)
- Divide and Conquer: O(log n)
- Brute Force: O(1)

## Usage
```python
from maximum_subarray import Solution

solution = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# Using Kadane's Algorithm
result = solution.max_subarray_kadane(nums)
print(f"Maximum subarray sum: {result}")

# Using Divide and Conquer
result = solution.max_subarray_divide_conquer(nums)
print(f"Maximum subarray sum: {result}")

# Using Brute Force
result = solution.max_subarray_brute_force(nums)
print(f"Maximum subarray sum: {result}")
```

## Common Applications
- Stock market analysis
- Signal processing
- Image processing
- Computer vision
- Data compression
- Pattern recognition 