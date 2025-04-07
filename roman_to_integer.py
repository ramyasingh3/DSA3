class Solution:
    def roman_to_int_naive(self, s: str) -> int:
        """
        Naive solution with O(n) time complexity.
        """
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        result = 0
        prev_value = 0
        
        for char in reversed(s):
            current_value = roman_map[char]
            if current_value < prev_value:
                result -= current_value
            else:
                result += current_value
            prev_value = current_value
            
        return result

    def roman_to_int_optimized(self, s: str) -> int:
        """
        Optimized solution with O(n) time complexity.
        """
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        result = 0
        i = 0
        n = len(s)
        
        while i < n:
            if i < n - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
                result += roman_map[s[i + 1]] - roman_map[s[i]]
                i += 2
            else:
                result += roman_map[s[i]]
                i += 1
                
        return result

def test_solution():
    solution = Solution()
    
    # Test Case 1: Basic conversion
    s1 = "III"
    print("Test Case 1:")
    print(f"Input: '{s1}'")
    print(f"Naive Solution: {solution.roman_to_int_naive(s1)}")
    print(f"Optimized Solution: {solution.roman_to_int_optimized(s1)}")
    print()
    
    # Test Case 2: Subtraction case
    s2 = "IV"
    print("Test Case 2:")
    print(f"Input: '{s2}'")
    print(f"Naive Solution: {solution.roman_to_int_naive(s2)}")
    print(f"Optimized Solution: {solution.roman_to_int_optimized(s2)}")
    print()
    
    # Test Case 3: Complex number
    s3 = "MCMXCIV"
    print("Test Case 3:")
    print(f"Input: '{s3}'")
    print(f"Naive Solution: {solution.roman_to_int_naive(s3)}")
    print(f"Optimized Solution: {solution.roman_to_int_optimized(s3)}")
    print()
    
    # Test Case 4: Large number
    s4 = "MMMCMXCIX"
    print("Test Case 4:")
    print(f"Input: '{s4}'")
    print(f"Naive Solution: {solution.roman_to_int_naive(s4)}")
    print(f"Optimized Solution: {solution.roman_to_int_optimized(s4)}")
    print()
    
    # Test Case 5: Single character
    s5 = "X"
    print("Test Case 5:")
    print(f"Input: '{s5}'")
    print(f"Naive Solution: {solution.roman_to_int_naive(s5)}")
    print(f"Optimized Solution: {solution.roman_to_int_optimized(s5)}")

if __name__ == "__main__":
    test_solution() 