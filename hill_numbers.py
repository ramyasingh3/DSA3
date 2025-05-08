def is_hill_number(num: int) -> bool:
    digits = list(str(num))
    n = len(digits)
    
    if n < 3:
        return False
    
    i = 1
    # strictly increasing
    while i < n and digits[i] > digits[i - 1]:
        i += 1
    
    if i == 1 or i == n:
        return False
    
    # strictly decreasing
    while i < n and digits[i] < digits[i - 1]:
        i += 1

    return i == n

def count_hill_numbers(arr: list[int]) -> int:
    return sum(is_hill_number(num) for num in arr)

# Example usage
if __name__ == "__main__":
    arr = [12321, 111, 132, 321, 1234321, 1234, 54321]
    print(count_hill_numbers(arr))  # Output: 3
