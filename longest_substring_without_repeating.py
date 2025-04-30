"""
Longest Substring Without Repeating Characters Implementation

This file contains multiple implementations to find the length of the longest substring
without repeating characters.

Problem Statement:
Given a string s, find the length of the longest substring without repeating characters.

Time Complexity: O(n) where n is the length of the string
Space Complexity: O(min(m, n)) where m is the size of the character set
"""

def length_of_longest_substring_brute_force(s: str) -> int:
    """
    Find longest substring without repeating characters using brute force.
    Check all possible substrings.
    
    Args:
        s (str): Input string
        
    Returns:
        int: Length of longest substring without repeating characters
    """
    def has_repeating_chars(substring: str) -> bool:
        """Check if substring has repeating characters"""
        return len(substring) != len(set(substring))
    
    max_length = 0
    n = len(s)
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = s[i:j]
            if not has_repeating_chars(substring):
                max_length = max(max_length, len(substring))
    
    return max_length

def length_of_longest_substring_sliding_window(s: str) -> int:
    """
    Find longest substring without repeating characters using sliding window.
    This is the optimal solution with O(n) time complexity.
    
    Args:
        s (str): Input string
        
    Returns:
        int: Length of longest substring without repeating characters
    """
    # Dictionary to store the last position of each character
    char_positions = {}
    max_length = 0
    start = 0
    
    for end, char in enumerate(s):
        # If character is already in current window, update start
        if char in char_positions and char_positions[char] >= start:
            start = char_positions[char] + 1
        else:
            max_length = max(max_length, end - start + 1)
        
        # Update character's last position
        char_positions[char] = end
    
    return max_length

def length_of_longest_substring_set(s: str) -> int:
    """
    Find longest substring without repeating characters using a set.
    This approach uses a set to track characters in current window.
    
    Args:
        s (str): Input string
        
    Returns:
        int: Length of longest substring without repeating characters
    """
    max_length = 0
    current_chars = set()
    start = 0
    
    for end, char in enumerate(s):
        # Remove characters from start until no repeating character
        while char in current_chars:
            current_chars.remove(s[start])
            start += 1
        
        # Add current character to set
        current_chars.add(char)
        max_length = max(max_length, end - start + 1)
    
    return max_length

def length_of_longest_substring_array(s: str) -> int:
    """
    Find longest substring without repeating characters using array.
    This approach assumes ASCII characters and uses an array instead of a map.
    
    Args:
        s (str): Input string
        
    Returns:
        int: Length of longest substring without repeating characters
    """
    # Array to store last position of each ASCII character
    last_positions = [-1] * 128
    max_length = 0
    start = 0
    
    for end, char in enumerate(s):
        # If character is already in current window, update start
        if last_positions[ord(char)] >= start:
            start = last_positions[ord(char)] + 1
        else:
            max_length = max(max_length, end - start + 1)
        
        # Update character's last position
        last_positions[ord(char)] = end
    
    return max_length

def test_longest_substring():
    """Test cases for longest substring implementations"""
    test_cases = [
        ("abcabcbb", 3),      # "abc"
        ("bbbbb", 1),         # "b"
        ("pwwkew", 3),        # "wke"
        ("", 0),              # Empty string
        (" ", 1),             # Single space
        ("a", 1),             # Single character
        ("ab", 2),            # Two different characters
        ("aa", 1),            # Two same characters
        ("dvdf", 3),          # "vdf"
        ("tmmzuxt", 5),       # "mzuxt"
        ("aab", 2),           # "ab"
        ("abcabcbb", 3),      # "abc"
    ]
    
    for s, expected in test_cases:
        # Test brute force approach (only for small strings)
        if len(s) <= 10:
            assert length_of_longest_substring_brute_force(s) == expected, \
                f"Brute force test failed for '{s}'"
        
        # Test sliding window approach
        assert length_of_longest_substring_sliding_window(s) == expected, \
            f"Sliding window test failed for '{s}'"
        
        # Test set approach
        assert length_of_longest_substring_set(s) == expected, \
            f"Set test failed for '{s}'"
        
        # Test array approach
        assert length_of_longest_substring_array(s) == expected, \
            f"Array test failed for '{s}'"
    
    print("All test cases passed!")

if __name__ == "__main__":
    # Run test cases
    test_longest_substring()
    
    # Example usage
    test_strings = [
        "abcabcbb",
        "bbbbb",
        "pwwkew",
        "dvdf",
        "tmmzuxt",
        "aab"
    ]
    
    print("\nTesting various strings:")
    for s in test_strings:
        print(f"\nString: '{s}'")
        if len(s) <= 10:
            print(f"Using brute force: {length_of_longest_substring_brute_force(s)}")
        print(f"Using sliding window: {length_of_longest_substring_sliding_window(s)}")
        print(f"Using set: {length_of_longest_substring_set(s)}")
        print(f"Using array: {length_of_longest_substring_array(s)}") 