def are_anagrams(str1: str, str2: str) -> bool:
    return sorted(str1) == sorted(str2)

# Example usage
if __name__ == "__main__":
    print(are_anagrams("listen", "silent"))  # True
    print(are_anagrams("hello", "world"))    # False
    print(are_anagrams("python", "typhon"))  # True
