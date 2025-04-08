from collections import Counter
from typing import Dict

class Solution:
    def is_anagram_sort(self, s: str, t: str) -> bool:
        """
        Sorting solution with O(n log n) time complexity.
        Sorts both strings and compares them.
        """
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

    def is_anagram_counter(self, s: str, t: str) -> bool:
        """
        Counter solution with O(n) time complexity.
        Uses Counter to compare character frequencies.
        """
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)

    def is_anagram_dict(self, s: str, t: str) -> bool:
        """
        Dictionary solution with O(n) time complexity.
        Uses a dictionary to track character frequencies.
        """
        if len(s) != len(t):
            return False
            
        char_count: Dict[str, int] = {}
        
        # Count characters in s
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Subtract counts for characters in t
        for char in t:
            if char not in char_count:
                return False
            char_count[char] -= 1
            if char_count[char] == 0:
                del char_count[char]
        
        return len(char_count) == 0

def test_solution():
    solution = Solution()
    
    # Test Case 1: Basic anagram
    s1, t1 = "anagram", "nagaram"
    print("Test Case 1:")
    print(f"Input: s = {s1}, t = {t1}")
    print(f"Sort: {solution.is_anagram_sort(s1, t1)}")
    print(f"Counter: {solution.is_anagram_counter(s1, t1)}")
    print(f"Dictionary: {solution.is_anagram_dict(s1, t1)}")
    print()
    
    # Test Case 2: Not anagrams
    s2, t2 = "rat", "car"
    print("Test Case 2:")
    print(f"Input: s = {s2}, t = {t2}")
    print(f"Sort: {solution.is_anagram_sort(s2, t2)}")
    print(f"Counter: {solution.is_anagram_counter(s2, t2)}")
    print(f"Dictionary: {solution.is_anagram_dict(s2, t2)}")
    print()
    
    # Test Case 3: Different lengths
    s3, t3 = "ab", "abc"
    print("Test Case 3:")
    print(f"Input: s = {s3}, t = {t3}")
    print(f"Sort: {solution.is_anagram_sort(s3, t3)}")
    print(f"Counter: {solution.is_anagram_counter(s3, t3)}")
    print(f"Dictionary: {solution.is_anagram_dict(s3, t3)}")
    print()
    
    # Test Case 4: Empty strings
    s4, t4 = "", ""
    print("Test Case 4:")
    print(f"Input: s = {s4}, t = {t4}")
    print(f"Sort: {solution.is_anagram_sort(s4, t4)}")
    print(f"Counter: {solution.is_anagram_counter(s4, t4)}")
    print(f"Dictionary: {solution.is_anagram_dict(s4, t4)}")
    print()
    
    # Test Case 5: Same characters, different frequencies
    s5, t5 = "aaab", "aaba"
    print("Test Case 5:")
    print(f"Input: s = {s5}, t = {t5}")
    print(f"Sort: {solution.is_anagram_sort(s5, t5)}")
    print(f"Counter: {solution.is_anagram_counter(s5, t5)}")
    print(f"Dictionary: {solution.is_anagram_dict(s5, t5)}")

if __name__ == "__main__":
    test_solution() 