from typing import List, List[List[int]]

class Solution:
    def four_sum_brute_force(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Brute force approach checking all possible quadruplets.
        Time Complexity: O(n⁴)
        Space Complexity: O(1)
        """
        result = []
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for l in range(k + 1, n):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            quadruplet = sorted([nums[i], nums[j], nums[k], nums[l]])
                            if quadruplet not in result:
                                result.append(quadruplet)
        return result

    def four_sum_two_pointers(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Using sorting and two pointers.
        Time Complexity: O(n³)
        Space Complexity: O(1)
        """
        result = []
        nums.sort()
        n = len(nums)
        
        for i in range(n - 3):
            # Skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            for j in range(i + 1, n - 2):
                # Skip duplicates
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                    
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        # Skip duplicates
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                        
        return result

    def four_sum_hash(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Using hash set to store pairs.
        Time Complexity: O(n³)
        Space Complexity: O(n²)
        """
        result = []
        nums.sort()
        n = len(nums)
        
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                    
                seen = set()
                for k in range(j + 1, n):
                    complement = target - (nums[i] + nums[j] + nums[k])
                    if complement in seen:
                        quadruplet = [nums[i], nums[j], complement, nums[k]]
                        if quadruplet not in result:
                            result.append(quadruplet)
                    seen.add(nums[k])
                    
        return result

def test_solution():
    solution = Solution()
    
    # Test Case 1: Basic case
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print("Test Case 1:")
    print(f"Input: nums = {nums}, target = {target}")
    print("Brute Force:", solution.four_sum_brute_force(nums, target))
    print("Two Pointers:", solution.four_sum_two_pointers(nums, target))
    print("Hash Method:", solution.four_sum_hash(nums, target))
    print()
    
    # Test Case 2: No solution
    nums = [1, 2, 3, 4, 5]
    target = 20
    print("Test Case 2:")
    print(f"Input: nums = {nums}, target = {target}")
    print("Brute Force:", solution.four_sum_brute_force(nums, target))
    print("Two Pointers:", solution.four_sum_two_pointers(nums, target))
    print("Hash Method:", solution.four_sum_hash(nums, target))
    print()
    
    # Test Case 3: All zeros
    nums = [0, 0, 0, 0, 0]
    target = 0
    print("Test Case 3:")
    print(f"Input: nums = {nums}, target = {target}")
    print("Brute Force:", solution.four_sum_brute_force(nums, target))
    print("Two Pointers:", solution.four_sum_two_pointers(nums, target))
    print("Hash Method:", solution.four_sum_hash(nums, target))
    print()
    
    # Test Case 4: Large numbers
    nums = [-100, -50, -25, 0, 25, 50, 100]
    target = 0
    print("Test Case 4:")
    print(f"Input: nums = {nums}, target = {target}")
    print("Brute Force:", solution.four_sum_brute_force(nums, target))
    print("Two Pointers:", solution.four_sum_two_pointers(nums, target))
    print("Hash Method:", solution.four_sum_hash(nums, target))
    print()
    
    # Test Case 5: Empty array
    nums = []
    target = 0
    print("Test Case 5:")
    print(f"Input: nums = {nums}, target = {target}")
    print("Brute Force:", solution.four_sum_brute_force(nums, target))
    print("Two Pointers:", solution.four_sum_two_pointers(nums, target))
    print("Hash Method:", solution.four_sum_hash(nums, target))

if __name__ == "__main__":
    test_solution() 