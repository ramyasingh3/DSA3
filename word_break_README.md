# Word Break

## Problem Description
Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

## Examples

### Example 1:
```
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
```

### Example 2:
```
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
```

### Example 3:
```
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
```

## Solution Approach

The solution uses dynamic programming with the following steps:

1. Create a set from wordDict for O(1) word lookups
2. Initialize a dp array where:
   - dp[i] represents whether s[0:i] can be segmented
   - dp[0] is True (empty string is always valid)
3. For each position i in the string:
   - Check all possible previous positions j
   - If dp[j] is True and s[j:i] is in wordDict, set dp[i] to True
4. Return dp[n] as the final result

The key insight is that we can break down the problem into smaller subproblems:
- If we can segment the string up to position j
- And the substring from j to i is a valid word
- Then we can segment the string up to position i

## Time and Space Complexity

- **Time Complexity**: O(n * m * k)
  - n is the length of string s
  - m is the number of words in wordDict
  - k is the maximum word length
  - For each position, we check all possible previous positions
  - Each substring check takes O(k) time

- **Space Complexity**: O(n)
  - We use a dp array of size n + 1
  - The word set takes O(m * k) space
  - Total space is dominated by the dp array

## Edge Cases

1. Empty string
2. Empty dictionary
3. Single character string
4. Word longer than string
5. Multiple valid segmentations
6. Repeating words
7. No valid segmentation possible

## Implementation Notes

- The solution uses a set for O(1) word lookups
- The solution handles empty strings correctly
- The solution allows word reuse
- The solution is case-sensitive
- The solution efficiently tracks valid segmentation points

## Alternative Approaches

1. **Recursive with Memoization**:
   - Use recursion to try all possible segmentations
   - Memoize results to avoid recomputation
   - Time Complexity: O(n²)
   - Space Complexity: O(n)
   - More intuitive but less efficient

2. **BFS Approach**:
   - Use BFS to find the shortest path to the end
   - Each node represents a valid segmentation point
   - Time Complexity: O(n * m * k)
   - Space Complexity: O(n)
   - Good for finding shortest segmentation

3. **Trie-based Approach**:
   - Build a trie from the dictionary
   - Use the trie to check word matches
   - Time Complexity: O(n * k)
   - Space Complexity: O(m * k)
   - More efficient for large dictionaries 