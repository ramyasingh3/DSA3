# Longest Increasing Path in a Matrix

## Problem Statement
Given an `m x n` integer matrix `matrix`, return the length of the longest increasing path in `matrix`.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

### Example 1:
```
Input: matrix = [[9,9,4],
                [6,6,8],
                [2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
```

### Example 2:
```
Input: matrix = [[3,4,5],
                [3,2,6],
                [2,2,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 3, 4].
```

### Example 3:
```
Input: matrix = [[1]]
Output: 1
```

## Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 200
- 0 <= matrix[i][j] <= 2^31 - 1

## Solution Approach
The solution uses dynamic programming with DFS to solve this problem efficiently:

1. Create a DP table where dp[i][j] represents the length of the longest increasing path starting from cell (i,j).

2. For each cell:
   - Use DFS to explore all four directions
   - Only move to cells with greater values
   - Cache the results in the DP table to avoid recomputation

3. Return the maximum value in the DP table

## Time and Space Complexity
- Time Complexity: O(m*n), where m and n are the dimensions of the matrix
- Space Complexity: O(m*n) for the DP table

## Implementation
The solution is implemented in Python using dynamic programming with DFS. The code includes test cases to verify the implementation. 