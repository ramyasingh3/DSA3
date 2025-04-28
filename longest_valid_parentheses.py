def longest_valid_parentheses(s: str) -> int:
    """
    Find the length of the longest valid (well-formed) parentheses substring.
    
    Args:
        s (str): Input string containing only '(' and ')'
        
    Returns:
        int: Length of the longest valid parentheses substring
    """
    if not s:
        return 0
        
    n = len(s)
    dp = [0] * n  # dp[i] represents the length of valid parentheses ending at index i
    
    for i in range(1, n):
        if s[i] == ')':
            if s[i-1] == '(':
                dp[i] = (dp[i-2] if i >= 2 else 0) + 2
            elif i - dp[i-1] > 0 and s[i - dp[i-1] - 1] == '(':
                dp[i] = dp[i-1] + (dp[i - dp[i-1] - 2] if i - dp[i-1] >= 2 else 0) + 2
    
    return max(dp)

def main():
    # Test cases
    test_cases = [
        "(()",      # Expected: 2 (valid substring: "()")
        ")()())",   # Expected: 4 (valid substring: "()()")
        "",         # Expected: 0
        "()",       # Expected: 2
        "((()))",   # Expected: 6
        "()(()",    # Expected: 2
    ]
    
    for s in test_cases:
        result = longest_valid_parentheses(s)
        print(f"Input: s = '{s}'")
        print(f"Output: {result}\n")

if __name__ == "__main__":
    main() 