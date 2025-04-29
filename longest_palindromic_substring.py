def longest_palindrome(s: str) -> str:
    """
    Find the longest palindromic substring in a given string.
    
    Args:
        s (str): Input string
        
    Returns:
        str: Longest palindromic substring
    """
    if not s:
        return ""
        
    n = len(s)
    # dp[i][j] will be True if the substring s[i:j+1] is a palindrome
    dp = [[False] * n for _ in range(n)]
    
    # Every single character is a palindrome
    for i in range(n):
        dp[i][i] = True
        
    start = 0
    max_length = 1
    
    # Check for substrings of length 2
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            start = i
            max_length = 2
    
    # Check for substrings of length > 2
    for length in range(3, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = True
                if length > max_length:
                    start = i
                    max_length = length
    
    return s[start:start+max_length]

def main():
    # Test cases
    test_cases = [
        "babad",    # Expected: "bab" or "aba"
        "cbbd",     # Expected: "bb"
        "a",        # Expected: "a"
        "",         # Expected: ""
        "racecar",  # Expected: "racecar"
    ]
    
    for s in test_cases:
        result = longest_palindrome(s)
        print(f"Input: s = '{s}'")
        print(f"Output: '{result}'\n")

if __name__ == "__main__":
    main() 