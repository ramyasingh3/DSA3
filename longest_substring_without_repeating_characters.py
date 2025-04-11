class Solution:
    def length_of_longest_substring_brute(self, s: str) -> int:
        """
        Brute force solution
        Time Complexity: O(n³)
        Space Complexity: O(min(n, m)) where m is the size of the charset
        """
        def all_unique(s: str) -> bool:
            return len(set(s)) == len(s)
        
        n = len(s)
        max_len = 0
        
        for i in range(n):
            for j in range(i, n):
                if all_unique(s[i:j+1]):
                    max_len = max(max_len, j - i + 1)
                    
        return max_len

    def length_of_longest_substring_sliding(self, s: str) -> int:
        """
        Sliding window solution
        Time Complexity: O(n)
        Space Complexity: O(min(n, m)) where m is the size of the charset
        """
        n = len(s)
        char_set = set()
        max_len = 0
        left = 0
        
        for right in range(n):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)
            
        return max_len

    def length_of_longest_substring_optimized(self, s: str) -> int:
        """
        Optimized sliding window solution
        Time Complexity: O(n)
        Space Complexity: O(min(n, m)) where m is the size of the charset
        """
        n = len(s)
        char_map = {}
        max_len = 0
        left = 0
        
        for right in range(n):
            if s[right] in char_map:
                left = max(left, char_map[s[right]] + 1)
            char_map[s[right]] = right
            max_len = max(max_len, right - left + 1)
            
        return max_len

def test_solution():
    solution = Solution()
    
    # Test Case 1: Basic case
    print("Test Case 1: Basic case")
    s = "abcabcbb"
    result = solution.length_of_longest_substring_brute(s)
    print(f"Input: {s}")
    print(f"Output: {result}")
    print()
    
    # Test Case 2: All same characters
    print("Test Case 2: All same characters")
    s = "bbbbb"
    result = solution.length_of_longest_substring_brute(s)
    print(f"Input: {s}")
    print(f"Output: {result}")
    print()
    
    # Test Case 3: Empty string
    print("Test Case 3: Empty string")
    s = ""
    result = solution.length_of_longest_substring_brute(s)
    print(f"Input: {s}")
    print(f"Output: {result}")
    print()
    
    # Test Case 4: Single character
    print("Test Case 4: Single character")
    s = "a"
    result = solution.length_of_longest_substring_brute(s)
    print(f"Input: {s}")
    print(f"Output: {result}")
    print()
    
    # Test Case 5: Long string
    print("Test Case 5: Long string")
    s = "abcdefghijklmnopqrstuvwxyz" * 10
    result = solution.length_of_longest_substring_brute(s)
    print(f"Input: {s[:10]}...")
    print(f"Output: {result}")
    print()
    
    # Test all methods
    print("Testing all methods:")
    s = "abcabcbb"
    print(f"Input: {s}")
    print(f"Brute force: {solution.length_of_longest_substring_brute(s)}")
    print(f"Sliding window: {solution.length_of_longest_substring_sliding(s)}")
    print(f"Optimized sliding window: {solution.length_of_longest_substring_optimized(s)}")

if __name__ == "__main__":
    test_solution() 