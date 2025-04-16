def test_level_order():
    """Test cases for the level order traversal solution."""
    
    test_cases = [
        ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
        ([1], [[1]]),
        ([], []),
        ([1, 2, 3, 4, 5, 6, 7], [[1], [2, 3], [4, 5, 6, 7]]),
        ([1, None, 2, None, 3], [[1], [2], [3]]),
        ([1, 2, None, 3, None, 4], [[1], [2], [3], [4]]),
        # New test case: Complex tree with multiple levels
        ([1, 2, 3, 4, 5, None, 6, None, None, 7, 8, None, None, 9, 10], 
         [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]])
    ]
    
    print("Testing Binary Tree Level Order Traversal Solution...")
    for tree_list, expected in test_cases:
        # Convert list to tree
        root = list_to_tree(tree_list)
        
        # Get level order traversal
        result = level_order(root)
        
        print(f"\nInput: {tree_list}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Test {'passed' if result == expected else 'failed'}")
        print("-" * 50) 