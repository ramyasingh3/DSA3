"""
Problem: Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
"""

from typing import List

def single_number(nums: List[int]) -> int:
    result = 0
    for num in nums:
        result ^= num
    return result

# Test cases
def test_single_number():
    assert single_number([2,2,1]) == 1
    assert single_number([4,1,2,1,2]) == 4
    assert single_number([1]) == 1
    assert single_number([0,1,0]) == 1
    print("All test cases passed!")

if __name__ == "__main__":
    test_single_number() 