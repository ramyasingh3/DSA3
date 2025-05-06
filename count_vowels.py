def count_vowels(s: str) -> int:
    vowels = set("aeiouAEIOU")
    return sum(1 for char in s if char in vowels)

# Example usage
if __name__ == "__main__":
    print(count_vowels("hello world"))     # Output: 3
    print(count_vowels("DSA in Python"))   # Output: 4
    print(count_vowels("xyz"))             # Output: 0
