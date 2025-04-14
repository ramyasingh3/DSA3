"""
Problem: Kth Largest Element in an Array

Find the kth largest element in an unsorted array using the QuickSelect algorithm.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Explanation: The 2nd largest element is 5.

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
Explanation: The 4th largest element is 4.
"""

import random

def find_kth_largest(nums, k):
    if not nums or k < 1 or k > len(nums):
        return None
    
    # Convert k to index (kth largest = len-k th smallest)
    k = len(nums) - k
    
    def quick_select(left, right):
        if left == right:
            return nums[left]
        
        # Choose random pivot to avoid worst case scenario
        pivot_idx = random.randint(left, right)
        pivot = nums[pivot_idx]
        
        # Move pivot to end
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
        
        # Partition
        store_idx = left
        for i in range(left, right):
            if nums[i] <= pivot:
                nums[store_idx], nums[i] = nums[i], nums[store_idx]
                store_idx += 1
        
        # Move pivot to its final place
        nums[store_idx], nums[right] = nums[right], nums[store_idx]
        
        # Check if we found kth element
        if k == store_idx:
            return nums[k]
        elif k < store_idx:
            return quick_select(left, store_idx - 1)
        else:
            return quick_select(store_idx + 1, right)
    
    return quick_select(0, len(nums) - 1)

def test_kth_largest():
    test_cases = [
        ([3,2,1,5,6,4], 2, 5),
        ([3,2,3,1,2,4,5,5,6], 4, 4),
        ([1], 1, 1),
        ([1,2,3,4,5], 1, 5),
        ([1,2,3,4,5], 5, 1),
        ([3,3,3,3,3], 2, 3),
        ([6,5,4,3,2,1], 3, 4),
    ]
    
    for i, (nums, k, expected) in enumerate(test_cases, 1):
        # Make copy of array since QuickSelect modifies it
        nums_copy = nums.copy()
        result = find_kth_largest(nums_copy, k)
        
        print(f"\nTest Case {i}:")
        print(f"Array: {nums}")
        print(f"k: {k}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        
        # Verify result
        # Sort original array to double check our answer
        sorted_nums = sorted(nums, reverse=True)
        actual_kth = sorted_nums[k-1]
        
        print(f"Result: {'✓ Passed' if result == expected and result == actual_kth else '✗ Failed'}")
        print("-" * 50)

if __name__ == "__main__":
    # Set random seed for reproducibility in tests
    random.seed(42)
    test_kth_largest()
