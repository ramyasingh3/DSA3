"""
Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Constraints:
- 1 <= s.length <= 10^4
- s consists of parentheses only '()[]{}'
"""

def is_valid_stack(s: str) -> bool:
    """
    Approach 1: Using Stack
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            # If stack is empty or top element doesn't match
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            stack.append(char)
    
    return len(stack) == 0

def is_valid_counter(s: str) -> bool:
    """
    Approach 2: Using Counter (Only works for single type of parentheses)
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    count = 0
    for char in s:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
            if count < 0:
                return False
    return count == 0

def is_valid_replace(s: str) -> bool:
    """
    Approach 3: Using String Replacement
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    while '()' in s or '[]' in s or '{}' in s:
        s = s.replace('()', '').replace('[]', '').replace('{}', '')
    return len(s) == 0

# Test cases
def test_valid_parentheses():
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("(((", False),
        (")))", False),
        ("({[]})", True),
        ("({[}])", False)
    ]
    
    for s, expected in test_cases:
        assert is_valid_stack(s) == expected, f"Stack approach failed for {s}"
        if all(c in '()' for c in s):  # Only test counter for single type
            assert is_valid_counter(s) == expected, f"Counter approach failed for {s}"
        assert is_valid_replace(s) == expected, f"Replace approach failed for {s}"
        print(f"Test passed for input: {s}")

if __name__ == "__main__":
    test_valid_parentheses()
    print("All test cases passed!") 