def is_palindrome(s: str) -> bool:
    """
    Determine if a string is a palindrome, considering only alphanumeric characters and ignoring cases.
    
    Args:
        s: Input string to check
        
    Returns:
        bool: True if the string is a palindrome, False otherwise
    """
    # Convert to lowercase and filter out non-alphanumeric characters
    filtered = ''.join(char.lower() for char in s if char.isalnum())
    
    # Compare string with its reverse
    return filtered == filtered[::-1]

def test_valid_palindrome():
    """Test cases for the valid palindrome solution."""
    
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("", True),
        (".,", True),
        ("0P", False),
        ("a.", True),
        ("ab@a", True),
        ("12321", True),
        ("Python", False),
        ("Was it a car or a cat I saw?", True)
    ]
    
    print("Testing Valid Palindrome Solution...")
    for test_str, expected in test_cases:
        result = is_palindrome(test_str)
        print(f"\nInput: {test_str}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Test {'passed' if result == expected else 'failed'}")
        print("-" * 50)

if __name__ == "__main__":
    test_valid_palindrome() 