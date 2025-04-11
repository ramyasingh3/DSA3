# Longest Substring Without Repeating Characters

## Problem Description
Given a string `s`, find the length of the longest substring without repeating characters.

## Examples
1. Basic case:
   ```
   Input: s = "abcabcbb"
   Output: 3
   Explanation: The answer is "abc", with the length of 3.
   ```

2. All same characters:
   ```
   Input: s = "bbbbb"
   Output: 1
   Explanation: The answer is "b", with the length of 1.
   ```

3. Empty string:
   ```
   Input: s = ""
   Output: 0
   ```

## Solution Approaches

### 1. Brute Force Solution (O(n³))
- Checks all possible substrings
- Time Complexity: O(n³)
- Space Complexity: O(min(n, m)) where m is the size of the charset
- Simple but inefficient
- Good for understanding the problem

### 2. Sliding Window Solution (O(n))
- Uses a sliding window to track unique characters
- Time Complexity: O(n)
- Space Complexity: O(min(n, m))
- More efficient than brute force
- Good for learning sliding window technique

### 3. Optimized Sliding Window Solution (O(n))
- Uses a hash map to store character positions
- Time Complexity: O(n)
- Space Complexity: O(min(n, m))
- Most efficient
- Good for learning optimization techniques

## Time Complexity
- Brute Force: O(n³)
- Sliding Window: O(n)
- Optimized Sliding Window: O(n)

## Space Complexity
- Brute Force: O(min(n, m))
- Sliding Window: O(min(n, m))
- Optimized Sliding Window: O(min(n, m))

## Usage
```python
from longest_substring_without_repeating_characters import Solution

solution = Solution()
s = "abcabcbb"

# Using brute force solution
result = solution.length_of_longest_substring_brute(s)
print(f"Length of longest substring: {result}")

# Using sliding window solution
result = solution.length_of_longest_substring_sliding(s)
print(f"Length of longest substring: {result}")

# Using optimized sliding window solution
result = solution.length_of_longest_substring_optimized(s)
print(f"Length of longest substring: {result}")
```

## Common Applications
- Text processing
- Pattern matching
- Data validation
- String manipulation
- Bioinformatics 