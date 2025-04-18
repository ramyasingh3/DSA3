from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def boundary_of_binary_tree(root: Optional[TreeNode]) -> List[int]:
    """
    Perform boundary traversal of a binary tree.
    The boundary includes:
    1. Left boundary (top-down)
    2. Leaf nodes (left to right)
    3. Right boundary (bottom-up)
    
    Args:
        root: Root node of the binary tree
        
    Returns:
        List of node values in boundary traversal order
    """
    if not root:
        return []
    
    result = [root.val]
    
    def left_boundary(node: TreeNode) -> None:
        if not node or (not node.left and not node.right):
            return
        result.append(node.val)
        if node.left:
            left_boundary(node.left)
        else:
            left_boundary(node.right)
    
    def right_boundary(node: TreeNode) -> None:
        if not node or (not node.left and not node.right):
            return
        if node.right:
            right_boundary(node.right)
        else:
            right_boundary(node.left)
        result.append(node.val)
    
    def leaves(node: TreeNode) -> None:
        if not node:
            return
        if not node.left and not node.right:
            result.append(node.val)
            return
        leaves(node.left)
        leaves(node.right)
    
    # Traverse left boundary (excluding root and leaves)
    left_boundary(root.left)
    
    # Traverse leaves (left to right)
    leaves(root.left)
    leaves(root.right)
    
    # Traverse right boundary (excluding root and leaves)
    right_boundary(root.right)
    
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

def test_boundary_traversal():
    """Test cases for the binary tree boundary traversal solution."""
    
    test_cases = [
        # Basic cases
        ([1, 2, 3, 4, 5, 6, 7], [1, 2, 4, 5, 6, 7, 3]),
        ([1], [1]),
        ([], []),
        # Complete binary tree
        ([1, 2, 3, 4, 5, 6, 7], [1, 2, 4, 5, 6, 7, 3]),
        # Left skewed tree
        ([1, 2, None, 3, None, 4], [1, 2, 3, 4]),
        # Right skewed tree
        ([1, None, 2, None, 3, None, 4], [1, 2, 3, 4]),
        # Complex cases
        ([5, 3, 6, 2, 4, None, None, 1], [5, 3, 2, 1, 4, 6]),
        # Large tree
        (list(range(1, 16)), [1, 2, 4, 8, 9, 10, 11, 12, 13, 14, 15, 7, 3]),
        # Edge cases
        ([1, None, None], [1]),
        ([1, 2, None], [1, 2]),
        # Mixed values
        ([10, 5, 15, 3, 7, 12, 20], [10, 5, 3, 7, 12, 20, 15])
    ]
    
    print("Testing Binary Tree Boundary Traversal Solution...")
    for tree_list, expected in test_cases:
        # Convert list to tree
        root = list_to_tree(tree_list)
        
        # Get boundary traversal
        result = boundary_of_binary_tree(root)
        
        print(f"\nInput: {tree_list}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Test {'passed' if result == expected else 'failed'}")
        print("-" * 50)

if __name__ == "__main__":
    test_boundary_traversal() 