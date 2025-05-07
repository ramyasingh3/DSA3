def max_sum_subarray_k(nums: list[int], k: int) -> int:
    if len(nums) < k:
        return 0
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum

# Example usage
if __name__ == "__main__":
    print(max_sum_subarray_k([2, 1, 5, 1, 3, 2], 3))  # Output: 9
    print(max_sum_subarray_k([1, 9, 2, 4, 5], 2))     # Output: 11
