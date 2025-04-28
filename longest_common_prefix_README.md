# Longest Common Prefix

## Problem Statement
Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string `""`.

### Example 1:
```
Input: strs = ["flower","flow","flight"]
Output: "fl"
```

### Example 2:
```
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

### Example 3:
```
Input: strs = ["interspecies","interstellar","interstate"]
Output: "inters"
```

## Constraints:
- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] consists of only lowercase English letters.

## Solution Approach
The solution uses a simple approach to find the longest common prefix:

1. Find the shortest string in the array (as the common prefix cannot be longer than the shortest string)

2. For each character in the shortest string:
   - Compare it with the corresponding character in all other strings
   - If any character doesn't match, return the prefix found so far
   - If all characters match, continue to the next character

3. Return the shortest string if all characters match

## Time and Space Complexity
- Time Complexity: O(S), where S is the sum of all characters in all strings
- Space Complexity: O(1), as we only use a constant amount of extra space

## Implementation
The solution is implemented in Python. The code includes test cases to verify the implementation. 