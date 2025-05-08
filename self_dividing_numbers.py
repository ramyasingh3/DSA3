def is_self_dividing(num: int) -> bool:
    for d in str(num):
        if d == '0' or num % int(d) != 0:
            return False
    return True

def self_dividing_numbers(left: int, right: int) -> list[int]:
    return [num for num in range(left, right + 1) if is_self_dividing(num)]

# Example usage
if __name__ == "__main__":
    print(self_dividing_numbers(1, 22))
