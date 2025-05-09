# Longest Substring Without Repeating Characters

## Problem Description
Given a string `s`, find the length of the longest substring without repeating characters.

## Examples

### Example 1:
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

### Example 2:
```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

### Example 3:
```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
```

## Solution Approach

The solution uses a sliding window technique with the following steps:

1. Use a dictionary to store the last position of each character
2. Maintain two pointers: start and end
3. For each character:
   - If it's already in the current window, update the start pointer
   - Otherwise, update the maximum length
   - Update the character's last position
4. Return the maximum length found

The key insight is that we can use a sliding window to efficiently track the longest substring without repeating characters:
- When we find a repeating character, we move the start pointer to the position after its last occurrence
- This ensures we always have a valid window with no repeating characters

## Time and Space Complexity

- **Time Complexity**: O(n)
  - We process each character exactly once
  - Dictionary operations are O(1) on average
  - n is the length of the input string

- **Space Complexity**: O(min(m, n))
  - m is the size of the character set (e.g., 128 for ASCII)
  - n is the length of the string
  - We store at most min(m, n) characters in the dictionary

## Edge Cases

1. Empty string
2. Single character
3. All same characters
4. No repeating characters
5. Repeating characters at the end
6. Repeating characters in the middle
7. Special characters and spaces

## Implementation Notes

- The solution uses a dictionary for O(1) lookups
- The solution handles empty strings correctly
- The solution is case-sensitive
- The solution efficiently updates the window boundaries
- The solution works with any character set

## Alternative Approaches

1. **Brute Force**:
   - Check all possible substrings
   - Time Complexity: O(n³)
   - Space Complexity: O(min(m, n))
   - Not efficient for large strings

2. **Using Set**:
   - Use a set to track characters in current window
   - Time Complexity: O(n)
   - Space Complexity: O(min(m, n))
   - Similar to the dictionary approach

3. **Using Array**:
   - Use an array for ASCII characters
   - Time Complexity: O(n)
   - Space Complexity: O(1) for fixed-size character set
   - More efficient for ASCII strings 