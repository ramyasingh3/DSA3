def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Example usage
if __name__ == "__main__":
    print(factorial(5))   # Output: 120
    print(factorial(0))   # Output: 1
    print(factorial(1))   # Output: 1
