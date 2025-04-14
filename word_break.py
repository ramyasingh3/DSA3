class WordBreak:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        """
        Check if the string can be segmented into words from the dictionary.
        
        Args:
            s: The input string
            wordDict: List of words in the dictionary
            
        Returns:
            bool: True if the string can be segmented, False otherwise
        """
        # Convert wordDict to a set for O(1) lookups
        word_set = set(wordDict)
        n = len(s)
        
        # dp[i] represents whether s[0...i-1] can be segmented
        dp = [False] * (n + 1)
        dp[0] = True  # Empty string can always be segmented
        
        for i in range(1, n + 1):
            for j in range(i):
                # Check if s[j...i-1] is in the dictionary and s[0...j-1] can be segmented
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        
        return dp[n]

def test_word_break():
    # Test cases
    test_cases = [
        ("leetcode", ["leet", "code"], True),
        ("applepenapple", ["apple", "pen"], True),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
        ("", ["a", "b"], True),  # Empty string
        ("a", [], False),  # No words in dictionary
        ("aaaaaaa", ["aaaa", "aaa"], True),  # Multiple ways to break
    ]
    
    solver = WordBreak()
    
    for s, wordDict, expected in test_cases:
        result = solver.wordBreak(s, wordDict)
        print(f"Input: s = '{s}', wordDict = {wordDict}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print(f"Test {'passed' if result == expected else 'failed'}")
        print("-" * 50)

if __name__ == "__main__":
    test_word_break() 