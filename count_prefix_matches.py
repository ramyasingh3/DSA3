def count_prefixes(words: list[str], s: str) -> int:
    count = 0
    for word in words:
        if s.startswith(word):
            count += 1
    return count

# Example usage
if __name__ == "__main__":
    words = ["a", "ap", "app", "appl", "banana"]
    s = "apple"
    print(count_prefixes(words, s))  # Output: 4
