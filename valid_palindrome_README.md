# Valid Palindrome

## Problem Description
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

### Examples
```
Input: "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Input: "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
```

## Approach
1. Convert the string to lowercase
2. Filter out non-alphanumeric characters
3. Compare the string with its reverse

### Key Points
- Only consider alphanumeric characters (letters and numbers)
- Case insensitive comparison
- Empty string is considered a valid palindrome

## Time Complexity
- O(n) where n is the length of the string
  - We need to traverse the string once to filter characters
  - And once more to check palindrome property

## Space Complexity
- O(n) to store the filtered string 