def longest_consecutive_sequence(nums: list[int]) -> int:
    """
    Find the length of the longest consecutive sequence in an array.
    
    Args:
        nums (list[int]): List of integers
        
    Returns:
        int: Length of the longest consecutive sequence
    """
    if not nums:
        return 0
        
    num_set = set(nums)
    max_length = 0
    
    for num in num_set:
        # Only check if this number is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            
            # Count the length of the sequence
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            
            max_length = max(max_length, current_length)
    
    return max_length

def main():
    # Test cases
    test_cases = [
        [100, 4, 200, 1, 3, 2],  # Expected: 4 (sequence: [1,2,3,4])
        [0, 3, 7, 2, 5, 8, 4, 6, 0, 1],  # Expected: 9 (sequence: [0,1,2,3,4,5,6,7,8])
        [],  # Expected: 0
        [1],  # Expected: 1
        [1, 1, 1, 1],  # Expected: 1
    ]
    
    for nums in test_cases:
        result = longest_consecutive_sequence(nums)
        print(f"Input: nums = {nums}")
        print(f"Output: {result}\n")

if __name__ == "__main__":
    main() 