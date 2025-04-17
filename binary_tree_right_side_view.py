from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def right_side_view(root: Optional[TreeNode]) -> List[int]:
    """
    Get the right side view of a binary tree.
    
    Args:
        root: Root node of the binary tree
        
    Returns:
        List of values visible from the right side of the tree
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        
        for i in range(level_size):
            node = queue.popleft()
            
            # Only add the last node of each level (rightmost node)
            if i == level_size - 1:
                result.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return result

def list_to_tree(lst: List[Optional[int]]) -> Optional[TreeNode]:
    """Convert a list representation to a binary tree."""
    if not lst:
        return None
        
    root = TreeNode(lst[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(lst):
        node = queue.popleft()
        
        if lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)
        i += 1
        
        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)
        i += 1
    
    return root

def test_right_side_view():
    """Test cases for the binary tree right side view solution."""
    
    test_cases = [
        ([1, 2, 3, None, 5, None, 4], [1, 3, 4]),
        ([1, None, 3], [1, 3]),
        ([], []),
        ([1, 2, 3, 4], [1, 3, 4]),
        ([1, 2, 3, None, 5, None, 4, None, None, 6], [1, 3, 4, 6]),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [1, 3, 7, 11]),
        # Complex tree with multiple levels
        ([1, 2, 3, 4, 5, None, 6, None, None, 7, 8, None, None, 9, 10], 
         [1, 3, 6, 10])
    ]
    
    print("Testing Binary Tree Right Side View Solution...")
    for tree_list, expected in test_cases:
        # Convert list to tree
        root = list_to_tree(tree_list)
        
        # Get right side view
        result = right_side_view(root)
        
        print(f"\nInput: {tree_list}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Test {'passed' if result == expected else 'failed'}")
        print("-" * 50)

if __name__ == "__main__":
    test_right_side_view() 