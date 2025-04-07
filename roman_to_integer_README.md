# Roman to Integer

## Problem Description
Given a roman numeral, convert it to an integer. Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

```
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

Roman numerals are usually written largest to smallest from left to right. However, there are six instances where subtraction is used:
- I can be placed before V (5) and X (10) to make 4 and 9. 
- X can be placed before L (50) and C (100) to make 40 and 90. 
- C can be placed before D (500) and M (1000) to make 400 and 900.

## Examples
1. Basic conversion:
   ```
   Input: "III"
   Output: 3
   ```

2. Subtraction case:
   ```
   Input: "IV"
   Output: 4
   ```

3. Complex number:
   ```
   Input: "MCMXCIV"
   Output: 1994
   ```

4. Large number:
   ```
   Input: "MMMCMXCIX"
   Output: 3999
   ```

5. Single character:
   ```
   Input: "X"
   Output: 10
   ```

## Solution Approaches

### 1. Naive Solution (O(n))
- Create a mapping of Roman symbols to values
- Process the string from right to left
- Add or subtract values based on previous value
- Return the final result

### 2. Optimized Solution (O(n))
- Create a mapping of Roman symbols to values
- Process the string from left to right
- Check for subtraction cases
- Add values to result
- Return the final result

## Time Complexity
- Both solutions: O(n)

## Space Complexity
- Both solutions: O(1)

## Usage
```python
from roman_to_integer import Solution

solution = Solution()
s = "MCMXCIV"

# Using naive solution
result = solution.roman_to_int_naive(s)
print(result)  # Output: 1994

# Using optimized solution (recommended)
result = solution.roman_to_int_optimized(s)
print(result)  # Output: 1994
```

## Common Applications
- Historical data processing
- Clock face design
- Book chapter numbering
- Movie release years
- Monument inscriptions 