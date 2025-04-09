from typing import List

class Solution:
    def max_area_brute_force(self, height: List[int]) -> int:
        """
        Brute force approach checking all possible pairs.
        Time Complexity: O(n²)
        Space Complexity: O(1)
        """
        max_area = 0
        n = len(height)
        for i in range(n):
            for j in range(i + 1, n):
                current_area = min(height[i], height[j]) * (j - i)
                max_area = max(max_area, current_area)
        return max_area

    def max_area_two_pointers(self, height: List[int]) -> int:
        """
        Using two pointers approach.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        max_area = 0
        left, right = 0, len(height) - 1
        
        while left < right:
            current_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, current_area)
            
            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area

    def max_area_optimized(self, height: List[int]) -> int:
        """
        Optimized two pointers approach with early termination.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        max_area = 0
        left, right = 0, len(height) - 1
        
        while left < right:
            # Calculate current area
            h = min(height[left], height[right])
            current_area = h * (right - left)
            max_area = max(max_area, current_area)
            
            # Move pointers until we find a taller line
            while left < right and height[left] <= h:
                left += 1
            while left < right and height[right] <= h:
                right -= 1
                
        return max_area

def test_solution():
    solution = Solution()
    
    # Test Case 1: Basic case
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print("Test Case 1:")
    print(f"Input: {height}")
    print(f"Brute Force: {solution.max_area_brute_force(height)}")
    print(f"Two Pointers: {solution.max_area_two_pointers(height)}")
    print(f"Optimized: {solution.max_area_optimized(height)}")
    print()
    
    # Test Case 2: All same height
    height = [5, 5, 5, 5, 5]
    print("Test Case 2:")
    print(f"Input: {height}")
    print(f"Brute Force: {solution.max_area_brute_force(height)}")
    print(f"Two Pointers: {solution.max_area_two_pointers(height)}")
    print(f"Optimized: {solution.max_area_optimized(height)}")
    print()
    
    # Test Case 3: Increasing heights
    height = [1, 2, 3, 4, 5]
    print("Test Case 3:")
    print(f"Input: {height}")
    print(f"Brute Force: {solution.max_area_brute_force(height)}")
    print(f"Two Pointers: {solution.max_area_two_pointers(height)}")
    print(f"Optimized: {solution.max_area_optimized(height)}")
    print()
    
    # Test Case 4: Decreasing heights
    height = [5, 4, 3, 2, 1]
    print("Test Case 4:")
    print(f"Input: {height}")
    print(f"Brute Force: {solution.max_area_brute_force(height)}")
    print(f"Two Pointers: {solution.max_area_two_pointers(height)}")
    print(f"Optimized: {solution.max_area_optimized(height)}")
    print()
    
    # Test Case 5: Large array
    height = list(range(1000))
    print("Test Case 5:")
    print(f"Input: [0,1,2,...,999]")
    print(f"Brute Force: {solution.max_area_brute_force(height)}")
    print(f"Two Pointers: {solution.max_area_two_pointers(height)}")
    print(f"Optimized: {solution.max_area_optimized(height)}")

if __name__ == "__main__":
    test_solution() 