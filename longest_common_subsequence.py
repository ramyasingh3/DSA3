"""
Longest Common Subsequence

Problem:
Given two strings text1 and text2, return the length of their longest common subsequence.
A subsequence of a string is a new string generated from the original string with some characters
(can be none) deleted without changing the relative order of the remaining characters.

Example 1:
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

Time Complexity: O(m * n) where m and n are the lengths of text1 and text2
Space Complexity: O(m * n) for the dp array
"""

def longest_common_subsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    # Create a 2D dp array initialized with zeros
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the dp array
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

# Test cases
def test_longest_common_subsequence():
    # Test case 1: Basic case
    assert longest_common_subsequence("abcde", "ace") == 3
    
    # Test case 2: Identical strings
    assert longest_common_subsequence("abc", "abc") == 3
    
    # Test case 3: No common subsequence
    assert longest_common_subsequence("abc", "def") == 0
    
    # Test case 4: Empty strings
    assert longest_common_subsequence("", "") == 0
    
    # Test case 5: One empty string
    assert longest_common_subsequence("abc", "") == 0
    
    # Test case 6: Different lengths
    assert longest_common_subsequence("abcde", "ace") == 3
    
    # Test case 7: Multiple possible subsequences
    assert longest_common_subsequence("abcabc", "abc") == 3
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_longest_common_subsequence()
