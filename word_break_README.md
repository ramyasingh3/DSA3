# Word Break

## Problem Description
Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words. The same word in the dictionary may be reused multiple times in the segmentation.

### Examples
1. Input: s = "leetcode", wordDict = ["leet","code"]
   Output: true
   Explanation: "leetcode" can be segmented as "leet code".

2. Input: s = "applepenapple", wordDict = ["apple","pen"]
   Output: true
   Explanation: "applepenapple" can be segmented as "apple pen apple".

3. Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
   Output: false

## Approach
The solution uses dynamic programming to solve this problem:
1. Create a boolean array `dp` where `dp[i]` represents whether the substring `s[0...i-1]` can be segmented into dictionary words.
2. Initialize `dp[0]` as true since an empty string can always be segmented.
3. For each position `i` in the string:
   - Check all possible substrings ending at `i`
   - If any substring `s[j...i-1]` is in the dictionary and `dp[j]` is true, then `dp[i]` is true
4. The final result is stored in `dp[n]` where `n` is the length of the string.

## Time Complexity
- O(n³) where n is the length of the string
- The nested loops and substring operations contribute to the cubic time complexity

## Space Complexity
- O(n) for the dp array
- O(m) for the word dictionary (where m is the number of words)
- Overall: O(n + m) 