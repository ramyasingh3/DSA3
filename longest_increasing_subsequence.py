import bisect

class LongestIncreasingSubsequence:
    def lengthOfLIS(self, nums: list[int]) -> int:
        """
        Find the length of the longest strictly increasing subsequence.
        
        Args:
            nums: List of integers
            
        Returns:
            Length of the longest increasing subsequence
        """
        if not nums:
            return 0
            
        # dp[i] represents the length of the longest increasing subsequence
        # that ends with nums[i]
        dp = [1] * len(nums)
        
        # For each number, check all previous numbers
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                
        return max(dp)

def test_longest_increasing_subsequence():
    # Test cases
    test_cases = [
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([0, 1, 0, 3, 2, 3], 4),
        ([7, 7, 7, 7, 7, 7, 7], 1),
        ([], 0),
        ([1], 1),
        ([1, 3, 6, 7, 9, 4, 10, 5, 6], 6),
        ([3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12], 6),
    ]
    
    solver = LongestIncreasingSubsequence()
    
    for nums, expected in test_cases:
        result = solver.lengthOfLIS(nums)
        print(f"Input: nums = {nums}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print(f"Test {'passed' if result == expected else 'failed'}")
        print("-" * 50)

def length_of_lis(nums: list[int]) -> int:
    """
    Find the length of the longest strictly increasing subsequence.
    
    Args:
        nums (list[int]): List of integers
        
    Returns:
        int: Length of the longest increasing subsequence
    """
    if not nums:
        return 0
        
    n = len(nums)
    dp = [1] * n  # dp[i] represents the length of LIS ending at index i
    
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

def main():
    # Test cases
    test_cases = [
        [10, 9, 2, 5, 3, 7, 101, 18],  # Expected: 4 (subsequence: [2,5,7,101])
        [0, 1, 0, 3, 2, 3],            # Expected: 4 (subsequence: [0,1,2,3])
        [7, 7, 7, 7, 7, 7, 7],         # Expected: 1 (subsequence: [7])
        [],                            # Expected: 0
        [1],                           # Expected: 1
    ]
    
    for nums in test_cases:
        result = length_of_lis(nums)
        print(f"Input: nums = {nums}")
        print(f"Output: {result}\n")

if __name__ == "__main__":
    test_longest_increasing_subsequence()
    main() 