class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> list:
        """
        Given a binary tree, return the zigzag level order traversal of its nodes' values.
        Zigzag traversal means that nodes are processed from left to right, then right to left
        for the next level, and so on.
        
        Args:
            root: Root node of the binary tree
            
        Returns:
            List of lists containing node values in zigzag order
        """
        if not root:
            return []
        
        result = []
        queue = [root]
        left_to_right = True  # Direction flag
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            # Process all nodes at current level
            for _ in range(level_size):
                node = queue.pop(0)
                current_level.append(node.value)
                
                # Add children to queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Reverse the level if needed
            if not left_to_right:
                current_level.reverse()
            
            result.append(current_level)
            left_to_right = not left_to_right  # Toggle direction
        
        return result

    def zigzagLevelOrderOptimized(self, root: TreeNode) -> list:
        """
        Optimized version of zigzag level order traversal using deque.
        More efficient for large trees as it avoids list reversal.
        
        Args:
            root: Root node of the binary tree
            
        Returns:
            List of lists containing node values in zigzag order
        """
        if not root:
            return []
        
        from collections import deque
        
        result = []
        queue = deque([root])
        left_to_right = True
        
        while queue:
            level_size = len(queue)
            current_level = deque()
            
            for _ in range(level_size):
                if left_to_right:
                    node = queue.popleft()
                    current_level.append(node.value)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                else:
                    node = queue.pop()
                    current_level.append(node.value)
                    if node.right:
                        queue.appendleft(node.right)
                    if node.left:
                        queue.appendleft(node.left)
            
            result.append(list(current_level))
            left_to_right = not left_to_right
        
        return result

def build_test_tree1():
    """
    Builds test tree 1:
         3
        / \
       9   20
          /  \
         15   7
    """
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    return root

def build_test_tree2():
    """
    Builds test tree 2:
         1
        / \
       2   3
      / \   \
     4   5   6
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    return root

def build_test_tree3():
    """
    Builds test tree 3:
         1
        /
       2
      /
     3
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    return root

def print_tree(node, level=0, prefix="Root: "):
    """Helper function to print the tree structure"""
    if not node:
        return
    print("  " * level + prefix + str(node.value))
    if node.left or node.right:
        if node.left:
            print_tree(node.left, level + 1, "L--- ")
        if node.right:
            print_tree(node.right, level + 1, "R--- ")

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    print("Test Case 1: Tree with multiple levels")
    root1 = build_test_tree1()
    print("Tree structure:")
    print_tree(root1)
    print("Zigzag level order traversal:")
    print(solution.zigzagLevelOrder(root1))  # Expected: [[3], [20, 9], [15, 7]]
    print("Optimized zigzag level order traversal:")
    print(solution.zigzagLevelOrderOptimized(root1))  # Expected: [[3], [20, 9], [15, 7]]
    
    print("\nTest Case 2: Tree with overlapping nodes")
    root2 = build_test_tree2()
    print("Tree structure:")
    print_tree(root2)
    print("Zigzag level order traversal:")
    print(solution.zigzagLevelOrder(root2))  # Expected: [[1], [3, 2], [4, 5, 6]]
    print("Optimized zigzag level order traversal:")
    print(solution.zigzagLevelOrderOptimized(root2))  # Expected: [[1], [3, 2], [4, 5, 6]]
    
    print("\nTest Case 3: Left-skewed tree")
    root3 = build_test_tree3()
    print("Tree structure:")
    print_tree(root3)
    print("Zigzag level order traversal:")
    print(solution.zigzagLevelOrder(root3))  # Expected: [[1], [2], [3]]
    print("Optimized zigzag level order traversal:")
    print(solution.zigzagLevelOrderOptimized(root3))  # Expected: [[1], [2], [3]] 