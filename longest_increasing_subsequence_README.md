# Longest Increasing Subsequence

## Problem Statement
Given an integer array `nums`, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.

### Example 1:
```
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,5,7,101], therefore the length is 4.
```

### Example 2:
```
Input: nums = [0,1,0,3,2,3]
Output: 4
Explanation: The longest increasing subsequence is [0,1,2,3], therefore the length is 4.
```

### Example 3:
```
Input: nums = [7,7,7,7,7,7,7]
Output: 1
Explanation: The longest increasing subsequence is [7], therefore the length is 1.
```

## Constraints:
- 1 <= nums.length <= 2500
- -10^4 <= nums[i] <= 10^4

## Solution Approach
The solution uses dynamic programming to solve this problem efficiently:

1. Create a DP array where dp[i] represents the length of the longest increasing subsequence ending at index i.

2. Initialize dp array with 1's since each element is a subsequence of length 1.

3. For each element at index i:
   - Compare it with all previous elements (j < i)
   - If nums[i] > nums[j], update dp[i] = max(dp[i], dp[j] + 1)

4. Return the maximum value in the dp array

## Time and Space Complexity
- Time Complexity: O(n²), where n is the length of the input array
- Space Complexity: O(n) for the DP array

## Implementation
The solution is implemented in Python using dynamic programming. The code includes test cases to verify the implementation. 