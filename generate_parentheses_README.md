# Generate Parentheses

## Problem Description
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

## Examples
1. n = 1:
   ```
   Input: 1
   Output: ["()"]
   ```

2. n = 2:
   ```
   Input: 2
   Output: ["(())", "()()"]
   ```

3. n = 3:
   ```
   Input: 3
   Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]
   ```

4. n = 0:
   ```
   Input: 0
   Output: [""]
   ```

5. n = 4:
   ```
   Input: 4
   Output: ["(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())", "(()())()", "(())(())", "(())()()", "()((()))", "()(()())", "()(())()", "()()(())", "()()()()"]
   ```

## Solution Approaches

### 1. Brute Force (O(2^(2n)))
- Generate all possible combinations of parentheses
- Filter out invalid combinations
- Time Complexity: O(2^(2n))
- Space Complexity: O(2^(2n))

### 2. Backtracking (O(4^n/sqrt(n)))
- Only generate valid combinations by tracking open and close counts
- Time Complexity: O(4^n/sqrt(n))
- Space Complexity: O(4^n/sqrt(n))

### 3. Dynamic Programming (O(4^n/sqrt(n)))
- Build solutions from smaller subproblems
- Time Complexity: O(4^n/sqrt(n))
- Space Complexity: O(4^n/sqrt(n))

## Time Complexity
- Brute Force: O(2^(2n))
- Backtracking: O(4^n/sqrt(n))
- Dynamic Programming: O(4^n/sqrt(n))

## Space Complexity
- Brute Force: O(2^(2n))
- Backtracking: O(4^n/sqrt(n))
- Dynamic Programming: O(4^n/sqrt(n))

## Usage
```python
from generate_parentheses import Solution

solution = Solution()
n = 3

# Using brute force
result = solution.generate_parentheses_brute_force(n)
print(result)  # Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]

# Using backtracking
result = solution.generate_parentheses_backtrack(n)
print(result)  # Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]

# Using dynamic programming
result = solution.generate_parentheses_dp(n)
print(result)  # Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]
```

## Common Applications
- Generating valid expressions
- Compiler design
- Code generation
- Syntax checking
- Mathematical expression evaluation 