def longest_common_prefix(strs: list[str]) -> str:
    """
    Find the longest common prefix string amongst an array of strings.
    
    Args:
        strs (list[str]): List of strings
        
    Returns:
        str: Longest common prefix
    """
    if not strs:
        return ""
        
    # Find the shortest string in the array
    shortest = min(strs, key=len)
    
    # Check each character of the shortest string
    for i, char in enumerate(shortest):
        for string in strs:
            if string[i] != char:
                return shortest[:i]
    
    return shortest

def main():
    # Test cases
    test_cases = [
        ["flower", "flow", "flight"],  # Expected: "fl"
        ["dog", "racecar", "car"],     # Expected: ""
        ["interspecies", "interstellar", "interstate"],  # Expected: "inters"
        ["", "b"],                     # Expected: ""
        ["a"],                         # Expected: "a"
        [],                            # Expected: ""
    ]
    
    for strs in test_cases:
        result = longest_common_prefix(strs)
        print(f"Input: strs = {strs}")
        print(f"Output: '{result}'\n")

if __name__ == "__main__":
    main() 