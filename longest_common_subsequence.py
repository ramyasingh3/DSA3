"""
Problem: Longest Common Subsequence

Given two strings text1 and text2, return the length of their longest common subsequence (LCS)
and the subsequence itself. A subsequence is a sequence that can be derived from another sequence
by deleting some or no elements without changing the order of the remaining elements.

Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3, "ace"
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3, "abc"
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0, ""
Explanation: There is no common subsequence, so return 0.
"""

def longest_common_subsequence(text1: str, text2: str) -> int:
    """
    Find the length of the longest common subsequence between two strings.
    
    Args:
        text1 (str): First input string
        text2 (str): Second input string
        
    Returns:
        int: Length of the longest common subsequence
    """
    if not text1 or not text2:
        return 0
        
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

def test_lcs():
    test_cases = [
        ("abcde", "ace", 3, "ace"),
        ("abc", "abc", 3, "abc"),
        ("abc", "def", 0, ""),
        ("", "abc", 0, ""),
        ("abcdef", "acf", 3, "acf"),
        ("AGGTAB", "GXTXAYB", 4, "GTAB"),
        ("hello", "world", 2, "lo"),  # Fixed: LCS is "lo" with length 2
        ("aaaaaa", "aaa", 3, "aaa"),
        ("ABCDGH", "AEDFHR", 3, "ADH"),
    ]
    
    for i, (text1, text2, expected_length, expected_lcs) in enumerate(test_cases, 1):
        length = longest_common_subsequence(text1, text2)
        print(f"\nTest Case {i}:")
        print(f"Text1: '{text1}'")
        print(f"Text2: '{text2}'")
        print(f"Expected length: {expected_length}, Got: {length}")
        print(f"Expected LCS: '{expected_lcs}'")
        
        # Verify the result
        is_valid_lcs = True
        if length != expected_length:
            is_valid_lcs = False
        
        print(f"Result: {'✓ Passed' if is_valid_lcs else '✗ Failed'}")
        print("-" * 50)

def main():
    # Test cases
    test_cases = [
        ("abcde", "ace"),  # Expected: 3 (subsequence: "ace")
        ("abc", "abc"),    # Expected: 3 (subsequence: "abc")
        ("abc", "def"),    # Expected: 0 (no common subsequence)
        ("", ""),          # Expected: 0
        ("abcde", "ace"),  # Expected: 3 (subsequence: "ace")
    ]
    
    for text1, text2 in test_cases:
        result = longest_common_subsequence(text1, text2)
        print(f"Input: text1 = '{text1}', text2 = '{text2}'")
        print(f"Output: {result}\n")

if __name__ == "__main__":
    test_lcs()
    main()
