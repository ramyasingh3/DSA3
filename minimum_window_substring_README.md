# Minimum Window Substring

## Problem Description
Given two strings `s` and `t` of lengths m and n respectively, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string `""`.

## Examples

### Example 1:
```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
```

### Example 2:
```
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
```

### Example 3:
```
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window. Since the maximum frequency of 'a' in s is 1, there is no valid window.
```

## Solution Approach

The solution uses a sliding window approach with the following steps:

1. Create a frequency counter for string `t` to track required characters and their counts
2. Initialize sliding window variables:
   - `left` and `right` pointers for window boundaries
   - `window_freq` to track character frequencies in current window
   - `formed` to track how many required characters are satisfied
   - `min_len` and `min_start` to track the minimum window found

3. Expand the window by moving the `right` pointer:
   - Add new character to window frequency
   - If character frequency matches required frequency, increment `formed`

4. Contract the window by moving the `left` pointer when all required characters are found:
   - Update minimum window if current window is smaller
   - Remove leftmost character from window
   - If removed character was required, decrement `formed`

5. Return the minimum window substring or empty string if no valid window found

## Time and Space Complexity

- **Time Complexity**: O(m + n)
  - m is the length of string s
  - n is the length of string t
  - We process each character in s at most twice (once by right pointer, once by left pointer)
  - Creating frequency counter for t takes O(n)

- **Space Complexity**: O(k)
  - k is the number of unique characters in t
  - We store frequency counters for both t and the current window
  - In worst case, k could be the size of the character set (e.g., ASCII or Unicode)

## Edge Cases

1. Empty strings
2. t longer than s
3. No valid window exists
4. Multiple valid windows of same length
5. Case sensitivity
6. Duplicate characters in t
7. All characters in t are same

## Implementation Notes

- The solution uses Python's `Counter` for efficient frequency counting
- The solution is case-sensitive
- The solution handles duplicate characters in t correctly
- The solution returns the first minimum window if multiple exist
- The solution efficiently tracks required characters using a counter

## Alternative Approaches

1. **Brute Force**:
   - Check all possible substrings
   - Time Complexity: O(m² * n)
   - Space Complexity: O(k)
   - Not efficient for large strings

2. **Using Two Pointers with Hash Map**:
   - Similar to current approach but using hash map instead of Counter
   - Time Complexity: O(m + n)
   - Space Complexity: O(k)
   - More complex to implement

3. **Using Array for ASCII Characters**:
   - Use fixed-size array for ASCII characters
   - Time Complexity: O(m + n)
   - Space Complexity: O(1) for ASCII
   - Limited to ASCII character set 