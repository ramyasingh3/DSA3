"""
Minimum Window Substring

Problem:
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window. Since the maximum frequency of 'a' in s is 1, there is no valid window.

Time Complexity: O(m + n) where m and n are the lengths of strings s and t
Space Complexity: O(k) where k is the number of unique characters in t
"""

from collections import Counter
from typing import Dict

def min_window(s: str, t: str) -> str:
    if not s or not t or len(s) < len(t):
        return ""
    
    # Create frequency counter for string t
    t_freq = Counter(t)
    required = len(t_freq)  # Number of unique characters needed
    formed = 0  # Number of unique characters formed in current window
    
    # Initialize sliding window variables
    window_freq: Dict[str, int] = {}
    left = right = 0
    min_len = float('inf')
    min_start = 0
    
    # Expand window to the right
    while right < len(s):
        char = s[right]
        window_freq[char] = window_freq.get(char, 0) + 1
        
        # If current character's frequency matches required frequency
        if char in t_freq and window_freq[char] == t_freq[char]:
            formed += 1
        
        # Try to minimize window from left
        while left <= right and formed == required:
            # Update minimum window if current window is smaller
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_start = left
            
            # Remove leftmost character from window
            char = s[left]
            window_freq[char] -= 1
            
            # If removed character was part of t and its frequency is now less than required
            if char in t_freq and window_freq[char] < t_freq[char]:
                formed -= 1
            
            left += 1
        
        right += 1
    
    return s[min_start:min_start + min_len] if min_len != float('inf') else ""

# Test cases
def test_min_window():
    # Test case 1: Basic case
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"
    
    # Test case 2: Single character
    assert min_window("a", "a") == "a"
    
    # Test case 3: No valid window
    assert min_window("a", "aa") == ""
    
    # Test case 4: Empty strings
    assert min_window("", "") == ""
    
    # Test case 5: t longer than s
    assert min_window("a", "ab") == ""
    
    # Test case 6: Multiple valid windows
    assert min_window("aab", "aab") == "aab"
    
    # Test case 7: Case sensitive
    assert min_window("aA", "Aa") == "aA"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_min_window() 