def first_unique_char(s: str) -> str | None:
    from collections import Counter
    freq = Counter(s)
    for char in s:
        if freq[char] == 1:
            return char
    return None

# Example usage
if __name__ == "__main__":
    print(first_unique_char("leetcode"))  # Output: l
    print(first_unique_char("aabbcc"))    # Output: None
    print(first_unique_char("aabbc"))     # Output: c
