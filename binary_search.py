def binary_search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example usage
if __name__ == "__main__":
    print(binary_search([1, 3, 5, 7, 9], 5))  # Output: 2
    print(binary_search([1, 3, 5, 7, 9], 6))  # Output: -1
