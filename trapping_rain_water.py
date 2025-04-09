from typing import List

class Solution:
    def trap_brute_force(self, height: List[int]) -> int:
        """
        Brute force approach checking each position.
        Time Complexity: O(n²)
        Space Complexity: O(1)
        """
        total_water = 0
        n = len(height)
        
        for i in range(n):
            # Find max height to the left
            max_left = 0
            for j in range(i):
                max_left = max(max_left, height[j])
                
            # Find max height to the right
            max_right = 0
            for j in range(i + 1, n):
                max_right = max(max_right, height[j])
                
            # Calculate water at current position
            water = min(max_left, max_right) - height[i]
            if water > 0:
                total_water += water
                
        return total_water

    def trap_dp(self, height: List[int]) -> int:
        """
        Dynamic programming approach with precomputed arrays.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not height:
            return 0
            
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        
        # Compute left max array
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])
            
        # Compute right max array
        right_max[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
            
        # Calculate total water
        total_water = 0
        for i in range(n):
            water = min(left_max[i], right_max[i]) - height[i]
            if water > 0:
                total_water += water
                
        return total_water

    def trap_two_pointers(self, height: List[int]) -> int:
        """
        Two pointers approach with constant space.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not height:
            return 0
            
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        total_water = 0
        
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    total_water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    total_water += right_max - height[right]
                right -= 1
                
        return total_water

def test_solution():
    solution = Solution()
    
    # Test Case 1: Basic case
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print("Test Case 1:")
    print(f"Input: {height}")
    print(f"Brute Force: {solution.trap_brute_force(height)}")
    print(f"Dynamic Programming: {solution.trap_dp(height)}")
    print(f"Two Pointers: {solution.trap_two_pointers(height)}")
    print()
    
    # Test Case 2: All same height
    height = [5,5,5,5,5]
    print("Test Case 2:")
    print(f"Input: {height}")
    print(f"Brute Force: {solution.trap_brute_force(height)}")
    print(f"Dynamic Programming: {solution.trap_dp(height)}")
    print(f"Two Pointers: {solution.trap_two_pointers(height)}")
    print()
    
    # Test Case 3: Increasing heights
    height = [1,2,3,4,5]
    print("Test Case 3:")
    print(f"Input: {height}")
    print(f"Brute Force: {solution.trap_brute_force(height)}")
    print(f"Dynamic Programming: {solution.trap_dp(height)}")
    print(f"Two Pointers: {solution.trap_two_pointers(height)}")
    print()
    
    # Test Case 4: Decreasing heights
    height = [5,4,3,2,1]
    print("Test Case 4:")
    print(f"Input: {height}")
    print(f"Brute Force: {solution.trap_brute_force(height)}")
    print(f"Dynamic Programming: {solution.trap_dp(height)}")
    print(f"Two Pointers: {solution.trap_two_pointers(height)}")
    print()
    
    # Test Case 5: Large array
    height = [0] * 1000 + [1] + [0] * 1000
    print("Test Case 5:")
    print(f"Input: [0,0,...,0,1,0,...,0]")
    print(f"Brute Force: {solution.trap_brute_force(height)}")
    print(f"Dynamic Programming: {solution.trap_dp(height)}")
    print(f"Two Pointers: {solution.trap_two_pointers(height)}")

if __name__ == "__main__":
    test_solution() 