class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Find the lowest common ancestor (LCA) of two nodes in a binary tree.
        The LCA is the lowest node in the tree that has both p and q as descendants.
        A node can be a descendant of itself.
        
        Args:
            root: Root node of the binary tree
            p: First node to find LCA for
            q: Second node to find LCA for
            
        Returns:
            The lowest common ancestor node
        """
        # Base cases
        if not root or root == p or root == q:
            return root
        
        # Search in left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If both nodes are found in different subtrees, current node is LCA
        if left and right:
            return root
        
        # If one node is found, return that node (it might be the LCA)
        return left if left else right

    def findNode(self, root: 'TreeNode', value: int) -> 'TreeNode':
        """Helper function to find a node with given value in the tree"""
        if not root:
            return None
        if root.value == value:
            return root
        
        left = self.findNode(root.left, value)
        if left:
            return left
        return self.findNode(root.right, value)

def build_test_tree1():
    """
    Builds test tree 1:
         3
        / \
       5   1
      / \   \
     6   2   8
        / \
       7   4
    """
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    return root

def build_test_tree2():
    """
    Builds test tree 2:
         1
        / \
       2   3
      /     \
     4       5
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
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

def print_lca_result(root, p_val, q_val):
    """Helper function to print LCA result"""
    solution = Solution()
    p = solution.findNode(root, p_val)
    q = solution.findNode(root, q_val)
    if not p or not q:
        print(f"Nodes {p_val} and/or {q_val} not found in tree")
        return
    lca = solution.lowestCommonAncestor(root, p, q)
    print(f"LCA of nodes {p_val} and {q_val} is: {lca.value}")

# Test cases
if __name__ == "__main__":
    print("\nTest Case 1: Complex tree")
    root1 = build_test_tree1()
    print("Tree structure:")
    print_tree(root1)
    print("\nFinding LCAs:")
    print_lca_result(root1, 5, 1)  # Expected: 3
    print_lca_result(root1, 5, 4)  # Expected: 5
    print_lca_result(root1, 7, 4)  # Expected: 2
    
    print("\nTest Case 2: Simple tree")
    root2 = build_test_tree2()
    print("Tree structure:")
    print_tree(root2)
    print("\nFinding LCAs:")
    print_lca_result(root2, 4, 5)  # Expected: 1
    print_lca_result(root2, 2, 4)  # Expected: 2 