from typing import List, Optional
from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def vertical_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Perform vertical order traversal of a binary tree.
    Returns a list of lists where each sublist contains nodes in a vertical line
    from top to bottom, and the vertical lines are ordered from left to right.
    
    Args:
        root: Root node of the binary tree
        
    Returns:
        List of lists containing node values in vertical order
    """
    if not root:
        return []
    
    # Dictionary to store nodes by their column index
    column_table = defaultdict(list)
    # Queue for BFS: (node, column, row)
    queue = deque([(root, 0, 0)])
    min_col = max_col = 0
    
    while queue:
        node, col, row = queue.popleft()
        
        # Update column range
        min_col = min(min_col, col)
        max_col = max(max_col, col)
        
        # Store node in its column
        column_table[col].append((row, node.val))
        
        # Add children to queue
        if node.left:
            queue.append((node.left, col - 1, row + 1))
        if node.right:
            queue.append((node.right, col + 1, row + 1))
    
    # Sort nodes in each column by row and value
    result = []
    for col in range(min_col, max_col + 1):
        # Sort by row, then by value
        column_table[col].sort()
        # Extract values in order
        result.append([val for _, val in column_table[col]])
    
    return result

def list_to_tree(lst: list) -> Optional[TreeNode]:
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

def test_vertical_order():
    """Test cases for the binary tree vertical order traversal solution."""
    
    test_cases = [
        # Basic cases
        ([3, 9, 20, None, None, 15, 7], [[9], [3, 15], [20], [7]]),
        ([1], [[1]]),
        ([], []),
        # Complete binary tree
        ([1, 2, 3, 4, 5, 6, 7], [[4], [2], [1, 5, 6], [3], [7]]),
        # Left skewed tree
        ([1, 2, None, 3, None, 4], [[4], [3], [2], [1]]),
        # Right skewed tree
        ([1, None, 2, None, 3, None, 4], [[1], [2], [3], [4]]),
        # Complex cases
        ([5, 3, 6, 2, 4, None, None, 1], [[1], [2], [3, 4], [5], [6]]),
        # Large tree
        (list(range(1, 16)), [[8], [4], [2, 9, 10], [1, 5, 6, 11, 12], [3, 7, 13, 14], [15]]),
        # Edge cases
        ([1, None, None], [[1]]),
        ([1, 2, None], [[2], [1]]),
        # Mixed values
        ([10, 5, 15, 3, 7, 12, 20], [[3], [5], [10, 7, 12], [15], [20]])
    ]
    
    print("Testing Binary Tree Vertical Order Traversal Solution...")
    for tree_list, expected in test_cases:
        # Convert list to tree
        root = list_to_tree(tree_list)
        
        # Get vertical order traversal
        result = vertical_order(root)
        
        print(f"\nInput: {tree_list}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Test {'passed' if result == expected else 'failed'}")
        print("-" * 50)

if __name__ == "__main__":
    test_vertical_order() 