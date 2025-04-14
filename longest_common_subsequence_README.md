# Longest Common Subsequence

## Problem Description
Given two strings `text1` and `text2`, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

## Examples

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

## Approach
The solution uses dynamic programming to solve this problem efficiently. Here's how it works:

1. Create a 2D DP table where `dp[i][j]` represents the length of the longest common subsequence of `text1[0...i-1]` and `text2[0...j-1]`
2. Initialize the base cases:
   - If either string is empty, the LCS length is 0
3. For each character in both strings:
   - If the characters match, `dp[i][j] = dp[i-1][j-1] + 1`
   - If the characters don't match, `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`
4. The value at `dp[m][n]` (where m and n are lengths of text1 and text2) gives the length of the LCS

## Time Complexity
- O(m * n), where m and n are the lengths of the two input strings
- We need to fill the DP table which has m * n cells

## Space Complexity
- O(m * n)
- We maintain a 2D DP table of size (m+1) x (n+1)

## Solution Code
The solution is implemented in `longest_common_subsequence.py`.

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
