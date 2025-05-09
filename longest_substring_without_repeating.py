"""
Longest Substring Without Repeating Characters

Problem:
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.

Time Complexity: O(n) where n is the length of the string
Space Complexity: O(min(m, n)) where m is the size of the character set
"""

def length_of_longest_substring(s: str) -> int:
    if not s:
        return 0
    
    # Dictionary to store the last position of each character
    char_positions = {}
    max_length = 0
    start = 0
    
    for end, char in enumerate(s):
        # If we find a repeating character, update the start position
        if char in char_positions and char_positions[char] >= start:
            start = char_positions[char] + 1
        else:
            max_length = max(max_length, end - start + 1)
        
        # Update the last position of the current character
        char_positions[char] = end
    
    return max_length

# Test cases
def test_length_of_longest_substring():
    # Test case 1: Basic case with repeating characters
    assert length_of_longest_substring("abcabcbb") == 3
    
    # Test case 2: All same characters
    assert length_of_longest_substring("bbbbb") == 1
    
    # Test case 3: Mixed case with repeating characters
    assert length_of_longest_substring("pwwkew") == 3
    
    # Test case 4: Empty string
    assert length_of_longest_substring("") == 0
    
    # Test case 5: Single character
    assert length_of_longest_substring("a") == 1
    
    # Test case 6: No repeating characters
    assert length_of_longest_substring("abcdef") == 6
    
    # Test case 7: Repeating characters at the end
    assert length_of_longest_substring("abcabc") == 3
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_length_of_longest_substring() 