from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """
    Perform inorder traversal of a binary tree.
    Inorder traversal: left -> root -> right
    
    Args:
        root: Root node of the binary tree
        
    Returns:
        List of node values in inorder traversal order
    """
    result = []
    stack = []
    current = root
    
    while current or stack:
        # Reach the leftmost node of the current node
        while current:
            stack.append(current)
            current = current.left
        
        # Current must be None at this point
        current = stack.pop()
        result.append(current.val)
        
        # Visit the right subtree
        current = current.right
    
    return result

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

def test_inorder_traversal():
    """Test cases for the binary tree inorder traversal solution."""
    
    test_cases = [
        # Basic cases
        ([1, None, 2, 3], [1, 3, 2]),
        ([], []),
        ([1], [1]),
        # Complete binary tree
        ([1, 2, 3, 4, 5, 6, 7], [4, 2, 5, 1, 6, 3, 7]),
        # Left skewed tree
        ([1, 2, None, 3, None, 4], [4, 3, 2, 1]),
        # Right skewed tree
        ([1, None, 2, None, 3, None, 4], [1, 2, 3, 4]),
        # Complex cases
        ([5, 3, 6, 2, 4, None, None, 1], [1, 2, 3, 4, 5, 6]),
        # Large tree
        (list(range(1, 16)), [8, 4, 9, 2, 10, 5, 11, 1, 12, 6, 13, 3, 14, 7, 15]),
        # Edge cases
        ([1, None, None], [1]),
        ([1, 2, None], [2, 1]),
        # Mixed values
        ([10, 5, 15, 3, 7, 12, 20], [3, 5, 7, 10, 12, 15, 20])
    ]
    
    print("Testing Binary Tree Inorder Traversal Solution...")
    for tree_list, expected in test_cases:
        # Convert list to tree
        root = list_to_tree(tree_list)
        
        # Get inorder traversal
        result = inorder_traversal(root)
        
        print(f"\nInput: {tree_list}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Test {'passed' if result == expected else 'failed'}")
        print("-" * 50)

if __name__ == "__main__":
    test_inorder_traversal() 