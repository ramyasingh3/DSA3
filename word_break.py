"""
Word Break

Problem:
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".

Example 3:
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

Time Complexity: O(n * m * k) where n is the length of s, m is the number of words in wordDict, and k is the maximum word length
Space Complexity: O(n) for the dp array
"""

from typing import List

def word_break(s: str, wordDict: List[str]) -> bool:
    n = len(s)
    # Create a set for O(1) word lookup
    word_set = set(wordDict)
    # dp[i] represents whether s[0:i] can be segmented
    dp = [False] * (n + 1)
    dp[0] = True  # Empty string is always valid
    
    # Try all possible segmentations
    for i in range(1, n + 1):
        # Check all possible previous positions
        for j in range(i):
            # If previous position is valid and current substring is in wordDict
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    
    return dp[n]

# Test cases
def test_word_break():
    # Test case 1: Basic case
    assert word_break("leetcode", ["leet", "code"]) == True
    
    # Test case 2: Repeating words
    assert word_break("applepenapple", ["apple", "pen"]) == True
    
    # Test case 3: No valid segmentation
    assert word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False
    
    # Test case 4: Empty string
    assert word_break("", ["a", "b"]) == True
    
    # Test case 5: Single character
    assert word_break("a", ["a"]) == True
    
    # Test case 6: Word longer than string
    assert word_break("a", ["aa"]) == False
    
    # Test case 7: Multiple valid segmentations
    assert word_break("catsand", ["cat", "cats", "and", "sand"]) == True
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_word_break() 