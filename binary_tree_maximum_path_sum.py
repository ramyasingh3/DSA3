from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_path_sum(root: Optional[TreeNode]) -> int:
    """
    Find the maximum path sum in a binary tree.
    A path is defined as any sequence of nodes from some starting node to any node
    in the tree along the parent-child connections.
    
    Args:
        root: Root node of the binary tree
        
    Returns:
        Maximum path sum
    """
    def max_gain(node: Optional[TreeNode]) -> int:
        nonlocal max_sum
        if not node:
            return 0
        
        # Get maximum gain from left and right subtrees
        left_gain = max(max_gain(node.left), 0)
        right_gain = max(max_gain(node.right), 0)
        
        # Calculate the maximum path sum that includes this node
        current_path_sum = node.val + left_gain + right_gain
        
        # Update the global maximum
        max_sum = max(max_sum, current_path_sum)
        
        # Return the maximum gain if we were to continue the path
        return node.val + max(left_gain, right_gain)
    
    max_sum = float('-inf')
    max_gain(root)
    return max_sum

def list_to_tree(lst: list) -> Optional[TreeNode]:
    """Convert a list representation to a binary tree."""
    if not lst:
        return None
        
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    
    while queue and i < len(lst):
        node = queue.pop(0)
        
        if lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)
        i += 1
        
        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)
        i += 1
    
    return root

def test_max_path_sum():
    """Test cases for the binary tree maximum path sum solution."""
    
    test_cases = [
        # Basic cases
        ([1, 2, 3], 6),
        ([-10, 9, 20, None, None, 15, 7], 42),
        # Single node
        ([1], 1),
        # Negative numbers
        ([-3], -3),
        ([-2, -1], -1),
        # Complex cases
        ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 48),
        # All negative numbers
        ([-1, -2, -3], -1),
        # Large tree
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 45),
        # Edge cases
        ([], 0),
        # Mixed positive and negative
        ([10, 2, 10, 20, 1, -25, None, None, None, None, None, None, 3, 4], 42),
        # Path through root
        ([1, -2, -3, 1, 3, -2, None, -1], 3)
    ]
    
    print("Testing Binary Tree Maximum Path Sum Solution...")
    for tree_list, expected in test_cases:
        # Convert list to tree
        root = list_to_tree(tree_list)
        
        # Get maximum path sum
        result = max_path_sum(root)
        
        print(f"\nInput: {tree_list}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Test {'passed' if result == expected else 'failed'}")
        print("-" * 50)

if __name__ == "__main__":
    test_max_path_sum() 