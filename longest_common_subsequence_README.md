# Longest Common Subsequence

## Problem Statement
Given two strings `text1` and `text2`, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

### Example 1:
```
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.
```

### Example 2:
```
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
```

### Example 3:
```
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
```

## Constraints:
- 1 <= text1.length, text2.length <= 1000
- text1 and text2 consist only of lowercase English characters.

## Solution Approach
The solution uses dynamic programming to solve this problem efficiently:

1. Create a 2D DP table where dp[i][j] represents the length of the longest common subsequence of text1[0...i-1] and text2[0...j-1].

2. For each position (i,j):
   - If text1[i-1] == text2[j-1], then dp[i][j] = dp[i-1][j-1] + 1
   - Otherwise, dp[i][j] = max(dp[i-1][j], dp[i][j-1])

3. Return dp[m][n] as the result

## Time and Space Complexity
- Time Complexity: O(m*n), where m and n are the lengths of the input strings
- Space Complexity: O(m*n) for the DP table

## Implementation
The solution is implemented in Python using dynamic programming. The code includes test cases to verify the implementation.

## Edge Cases Handled
- Empty strings
- No common subsequence
- All characters same
- Completely different strings
- Partial matches
- One string being subsequence of another

## Applications
- DNA sequence alignment
- File difference comparison
- Version control systems
- Text similarity measurement
- Spell checking algorithms
