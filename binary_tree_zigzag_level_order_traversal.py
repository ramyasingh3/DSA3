from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzag_level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Perform zigzag level order traversal of a binary tree.
    
    Args:
        root: Root node of the binary tree
        
    Returns:
        List of lists containing node values at each level in zigzag order
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    left_to_right = True
    
    while queue:
        level_size = len(queue)
        current_level = deque()
        
        for _ in range(level_size):
            node = queue.popleft()
            
            # Add node value to current level based on direction
            if left_to_right:
                current_level.append(node.val)
            else:
                current_level.appendleft(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(list(current_level))
        left_to_right = not left_to_right
    
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

def test_zigzag_level_order():
    """Test cases for the zigzag level order traversal solution."""
    
    test_cases = [
        ([3, 9, 20, None, None, 15, 7], [[3], [20, 9], [15, 7]]),
        ([1], [[1]]),
        ([], []),
        ([1, 2, 3, 4, 5, 6, 7], [[1], [3, 2], [4, 5, 6, 7]]),
        ([1, 2, 3, 4, None, None, 5], [[1], [3, 2], [4, 5]]),
        ([1, 2, 3, 4, 5, None, 6, None, None, 7, 8, None, None, 9, 10], 
         [[1], [3, 2], [4, 5, 6], [10, 9, 8, 7]]),
        # Complex tree with multiple levels
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
         [[1], [3, 2], [4, 5, 6, 7], [15, 14, 13, 12, 11, 10, 9, 8]])
    ]
    
    print("Testing Binary Tree Zigzag Level Order Traversal Solution...")
    for tree_list, expected in test_cases:
        # Convert list to tree
        root = list_to_tree(tree_list)
        
        # Get zigzag level order traversal
        result = zigzag_level_order(root)
        
        print(f"\nInput: {tree_list}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Test {'passed' if result == expected else 'failed'}")
        print("-" * 50)

if __name__ == "__main__":
    test_zigzag_level_order() 