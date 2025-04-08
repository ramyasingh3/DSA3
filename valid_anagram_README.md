# Valid Anagram

## Problem Description
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Examples
1. Basic anagram:
   ```
   Input: s = "anagram", t = "nagaram"
   Output: true
   Explanation: Both strings use the same letters with the same frequencies
   ```

2. Not anagrams:
   ```
   Input: s = "rat", t = "car"
   Output: false
   Explanation: Different letters used
   ```

3. Different lengths:
   ```
   Input: s = "ab", t = "abc"
   Output: false
   Explanation: Different number of characters
   ```

## Solution Approaches

### 1. Sorting Solution (O(n log n))
- Sort both strings and compare
- Time Complexity: O(n log n)
- Space Complexity: O(n)
- Best for readability and simplicity

### 2. Counter Solution (O(n))
- Use Counter class to compare character frequencies
- Time Complexity: O(n)
- Space Complexity: O(1) - limited by alphabet size
- Best for concise implementation

### 3. Dictionary Solution (O(n))
- Use dictionary to track character frequencies
- Time Complexity: O(n)
- Space Complexity: O(1) - limited by alphabet size
- Best for detailed control and memory efficiency

## Time Complexity
- Sorting: O(n log n)
- Counter and Dictionary: O(n)
where n is the length of the input strings

## Space Complexity
- Sorting: O(n)
- Counter and Dictionary: O(1)
as we only store at most 26 characters (English alphabet)

## Usage
```python
from valid_anagram import Solution

solution = Solution()
s = "anagram"
t = "nagaram"

# Using sorting
result = solution.is_anagram_sort(s, t)
print(result)  # Output: True

# Using Counter
result = solution.is_anagram_counter(s, t)
print(result)  # Output: True

# Using dictionary
result = solution.is_anagram_dict(s, t)
print(result)  # Output: True
```

## Common Applications
- Word games and puzzles
- Spell checkers
- Text analysis
- Cryptography
- Natural language processing 