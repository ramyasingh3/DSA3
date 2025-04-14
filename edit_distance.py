def min_distance(word1, word2):
    """
    Find the minimum number of operations required to convert word1 to word2.
    
    Args:
        word1 (str): First input string
        word2 (str): Second input string
        
    Returns:
        int: Minimum number of operations (insertions, deletions, or substitutions)
    """
    m, n = len(word1), len(word2)
    
    # Create a DP table initialized with zeros
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize base cases
    for i in range(m + 1):
        dp[i][0] = i  # To convert word1[0...i-1] to empty string, we need i deletions
    for j in range(n + 1):
        dp[0][j] = j  # To convert empty string to word2[0...j-1], we need j insertions
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # No operation needed
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # Deletion
                    dp[i][j - 1],      # Insertion
                    dp[i - 1][j - 1]   # Replacement
                )
    
    return dp[m][n]

# Test cases
def test_min_distance():
    # Example 1
    word1 = "horse"
    word2 = "ros"
    assert min_distance(word1, word2) == 3
    
    # Example 2
    word1 = "intention"
    word2 = "execution"
    assert min_distance(word1, word2) == 5
    
    # Example 3
    word1 = ""
    word2 = "a"
    assert min_distance(word1, word2) == 1
    
    # Additional test cases
    word1 = "kitten"
    word2 = "sitting"
    assert min_distance(word1, word2) == 3
    
    word1 = "abc"
    word2 = "abc"
    assert min_distance(word1, word2) == 0
    
    word1 = "abc"
    word2 = "def"
    assert min_distance(word1, word2) == 3
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_min_distance() 