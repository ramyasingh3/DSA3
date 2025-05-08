from collections import Counter

def digit_count(num: str) -> bool:
    freq = Counter(num)
    for i, ch in enumerate(num):
        if freq.get(str(i), 0) != int(ch):
            return False
    return True

# Example usage
if __name__ == "__main__":
    print(digit_count("1210"))  # Output: True
    print(digit_count("030"))   # Output: False
