# Longest Common Subsequence

## Problem Description
Given two strings `text1` and `text2`, return the length of their longest common subsequence. A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

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

## Solution Approach

The solution uses dynamic programming with the following steps:

1. Create a 2D dp array where dp[i][j] represents the length of LCS of text1[0:i] and text2[0:j]
2. Initialize the dp array with zeros
3. For each position (i, j):
   - If characters match: dp[i][j] = dp[i-1][j-1] + 1
   - If characters don't match: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
4. Return dp[m][n] as the final result

The key insight is that we can build the solution by considering:
- If characters match, we can extend the previous LCS
- If characters don't match, we take the maximum of:
  - LCS without the current character from text1
  - LCS without the current character from text2

## Time and Space Complexity

- **Time Complexity**: O(m * n)
  - We fill a 2D array of size (m+1) * (n+1)
  - Each cell takes O(1) time to compute
  - m and n are the lengths of text1 and text2

- **Space Complexity**: O(m * n)
  - We use a 2D dp array of size (m+1) * (n+1)
  - This is the space needed to store all intermediate results

## Edge Cases

1. Empty strings
2. Identical strings
3. No common subsequence
4. One empty string
5. Different length strings
6. Multiple possible subsequences
7. Single character strings

## Implementation Notes

- The solution uses a 2D array for dynamic programming
- The solution handles empty strings correctly
- The solution is case-sensitive
- The solution efficiently computes the LCS length
- The solution can be modified to return the actual subsequence

## Alternative Approaches

1. **Recursive with Memoization**:
   - Use recursion to try all possible subsequences
   - Memoize results to avoid recomputation
   - Time Complexity: O(m * n)
   - Space Complexity: O(m * n)
   - More intuitive but less efficient

2. **Space-Optimized DP**:
   - Use two rows instead of full 2D array
   - Time Complexity: O(m * n)
   - Space Complexity: O(min(m, n))
   - More efficient for space

3. **Suffix Tree Approach**:
   - Build a generalized suffix tree
   - Find the deepest common node
   - Time Complexity: O(m + n)
   - Space Complexity: O(m + n)
   - More complex but potentially faster

## Common Applications
- DNA sequence alignment
- File difference detection
- Plagiarism detection
- Spell checking
- Natural language processing
- Version control systems
- Bioinformatics
- Machine translation
