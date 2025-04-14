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

def longest_common_subsequence(text1: str, text2: str) -> tuple[int, str]:
    if not text1 or not text2:
        return 0, ""
    
    m, n = len(text1), len(text2)
    # dp[i][j] represents the length of LCS of text1[0...i-1] and text2[0...j-1]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Reconstruct the subsequence by finding the actual characters
    lcs = []
    i, j = m, n
    length = dp[m][n]
    
    # Work backwards to find characters that form the LCS
    while i > 0 and j > 0:
        # If current characters match and using them gives us optimal solution
        if text1[i-1] == text2[j-1] and dp[i][j] == dp[i-1][j-1] + 1:
            lcs.append(text1[i-1])
            i -= 1
            j -= 1
        # If not, move in direction of larger value
        elif dp[i-1][j] >= dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    # Since we built the string backwards, reverse it
    return length, ''.join(reversed(lcs))

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
        length, lcs = longest_common_subsequence(text1, text2)
        print(f"\nTest Case {i}:")
        print(f"Text1: '{text1}'")
        print(f"Text2: '{text2}'")
        print(f"Expected length: {expected_length}, Got: {length}")
        print(f"Expected LCS: '{expected_lcs}'")
        print(f"Got LCS: '{lcs}'")
        
        # Verify the result
        is_valid_lcs = True
        if length != expected_length or len(lcs) != length:
            is_valid_lcs = False
        else:
            # Verify that LCS is actually a subsequence of both strings
            def is_subsequence(s: str, t: str) -> bool:
                i = j = 0
                while i < len(s) and j < len(t):
                    if s[i] == t[j]:
                        i += 1
                    j += 1
                return i == len(s)
            
            is_valid_lcs = is_subsequence(lcs, text1) and is_subsequence(lcs, text2)
            if length == expected_length and not (lcs == expected_lcs):
                print(f"Note: Found different but valid LCS of same length")
        
        print(f"Result: {'✓ Passed' if is_valid_lcs else '✗ Failed'}")
        print("-" * 50)

if __name__ == "__main__":
    test_lcs()
