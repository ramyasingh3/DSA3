# Edit Distance

## Problem Description
Given two strings `word1` and `word2`, return the minimum number of operations required to convert `word1` to `word2`.

You have the following three operations permitted on a word:
- Insert a character
- Delete a character
- Replace a character

## Examples

### Example 1:
```
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
```

### Example 2:
```
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
```

### Example 3:
```
Input: word1 = "", word2 = "a"
Output: 1
Explanation: Insert 'a'
```

## Approach
The solution uses dynamic programming to solve this problem efficiently. Here's how it works:

1. Create a 2D DP table where `dp[i][j]` represents the minimum number of operations required to convert `word1[0...i-1]` to `word2[0...j-1]`
2. Initialize the base cases:
   - To convert an empty string to a string of length n, we need n insertions
   - To convert a string of length m to an empty string, we need m deletions
3. For each character in both strings:
   - If the characters match, `dp[i][j] = dp[i-1][j-1]` (no operation needed)
   - If the characters don't match, `dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])`
     - `dp[i-1][j]` represents deletion
     - `dp[i][j-1]` represents insertion
     - `dp[i-1][j-1]` represents replacement
4. The value at `dp[m][n]` (where m and n are lengths of word1 and word2) gives the minimum number of operations

## Time Complexity
- O(m * n), where m and n are the lengths of the two input strings
- We need to fill the DP table which has m * n cells

## Space Complexity
- O(m * n)
- We maintain a 2D DP table of size (m+1) x (n+1)

## Solution Code
The solution is implemented in `edit_distance.py`. 