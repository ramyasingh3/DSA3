from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Find two numbers in the array that sum up to the target.
    
    Args:
        nums: List of integers
        target: Target sum
        
    Returns:
        List of two indices whose values sum to target
    """
    # Dictionary to store number and its index
    num_dict = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    
    # This line should never be reached as per problem statement
    return []

def test_two_sum():
    """Test cases for the two sum solution."""
    
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([-1, -2, -3, -4, -5], -8, [2, 4]),
        ([0, 4, 3, 0], 0, [0, 3]),
        ([1, 2, 3, 4, 5], 9, [3, 4])
    ]
    
    print("Testing Two Sum Solution...")
    for nums, target, expected in test_cases:
        result = two_sum(nums, target)
        print(f"\nInput: nums = {nums}, target = {target}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Test {'passed' if result == expected else 'failed'}")
        print("-" * 50)

if __name__ == "__main__":
    test_two_sum() 