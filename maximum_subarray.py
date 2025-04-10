from typing import List

class Solution:
    def max_subarray_kadane(self, nums: List[int]) -> int:
        """
        Kadane's algorithm
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        max_current = max_global = nums[0]
        
        for i in range(1, len(nums)):
            max_current = max(nums[i], max_current + nums[i])
            max_global = max(max_global, max_current)
            
        return max_global
        
    def max_subarray_divide_conquer(self, nums: List[int]) -> int:
        """
        Divide and conquer approach
        Time Complexity: O(n log n)
        Space Complexity: O(log n)
        """
        def helper(left: int, right: int) -> int:
            if left == right:
                return nums[left]
                
            mid = (left + right) // 2
            
            # Find max subarray in left half
            left_max = helper(left, mid)
            
            # Find max subarray in right half
            right_max = helper(mid + 1, right)
            
            # Find max subarray crossing mid
            left_sum = right_sum = float('-inf')
            current_sum = 0
            
            for i in range(mid, left - 1, -1):
                current_sum += nums[i]
                left_sum = max(left_sum, current_sum)
                
            current_sum = 0
            for i in range(mid + 1, right + 1):
                current_sum += nums[i]
                right_sum = max(right_sum, current_sum)
                
            cross_max = left_sum + right_sum
            
            return max(left_max, right_max, cross_max)
            
        return helper(0, len(nums) - 1)
        
    def max_subarray_brute_force(self, nums: List[int]) -> int:
        """
        Brute force approach
        Time Complexity: O(n²)
        Space Complexity: O(1)
        """
        max_sum = float('-inf')
        
        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                max_sum = max(max_sum, current_sum)
                
        return max_sum

def test_solution():
    solution = Solution()
    
    # Test Case 1: Basic case
    print("Test Case 1: Basic case")
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = solution.max_subarray_kadane(nums)
    print(f"Input: {nums}")
    print(f"Output: {result}")
    print()
    
    # Test Case 2: All negative
    print("Test Case 2: All negative")
    nums = [-2, -1, -3, -4]
    result = solution.max_subarray_kadane(nums)
    print(f"Input: {nums}")
    print(f"Output: {result}")
    print()
    
    # Test Case 3: All positive
    print("Test Case 3: All positive")
    nums = [1, 2, 3, 4]
    result = solution.max_subarray_kadane(nums)
    print(f"Input: {nums}")
    print(f"Output: {result}")
    print()
    
    # Test Case 4: Single element
    print("Test Case 4: Single element")
    nums = [5]
    result = solution.max_subarray_kadane(nums)
    print(f"Input: {nums}")
    print(f"Output: {result}")
    print()
    
    # Test Case 5: Large array
    print("Test Case 5: Large array")
    nums = [1, -2, 3, -4, 5, -6, 7, -8, 9]
    result = solution.max_subarray_kadane(nums)
    print(f"Input: {nums}")
    print(f"Output: {result}")
    print()
    
    # Test all methods
    print("Testing all methods:")
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    
    print("Kadane's Algorithm:")
    result = solution.max_subarray_kadane(nums)
    print(f"Result: {result}")
    
    print("Divide and Conquer:")
    result = solution.max_subarray_divide_conquer(nums)
    print(f"Result: {result}")
    
    print("Brute Force:")
    result = solution.max_subarray_brute_force(nums)
    print(f"Result: {result}")

if __name__ == "__main__":
    test_solution() 