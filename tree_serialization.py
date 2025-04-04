class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """
        Serializes a binary tree to a string.
        Uses level-order traversal (BFS) with 'null' for empty nodes.
        
        Args:
            root: The root of the binary tree
            
        Returns:
            A string representation of the binary tree
        """
        if not root:
            return "[]"
        
        result = []
        queue = [root]
        
        while queue:
            node = queue.pop(0)
            if node:
                result.append(str(node.value))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")
                
        # Remove trailing nulls
        while result and result[-1] == "null":
            result.pop()
            
        return "[" + ",".join(result) + "]"
    
    def deserialize(self, data):
        """
        Deserializes a string to a binary tree.
        
        Args:
            data: String representation of the binary tree
            
        Returns:
            The root node of the reconstructed binary tree
        """
        if data == "[]":
            return None
            
        # Parse the string to get values
        values = data[1:-1].split(",")
        if not values:
            return None
            
        # Create root node
        root = TreeNode(int(values[0]))
        queue = [root]
        i = 1
        
        while queue and i < len(values):
            node = queue.pop(0)
            
            # Left child
            if i < len(values) and values[i] != "null":
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
            i += 1
            
            # Right child
            if i < len(values) and values[i] != "null":
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            i += 1
            
        return root

def print_tree(root, level=0, prefix="Root: "):
    """Helper function to print the tree structure"""
    if not root:
        return
    
    print("  " * level + prefix + str(root.value))
    if root.left or root.right:
        if root.left:
            print_tree(root.left, level + 1, "L--- ")
        if root.right:
            print_tree(root.right, level + 1, "R--- ")

# Test cases
if __name__ == "__main__":
    codec = Codec()
    
    # Test case 1: Simple binary tree
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    
    print("\nTest Case 1:")
    print("Original tree:")
    print_tree(root1)
    
    serialized1 = codec.serialize(root1)
    print("\nSerialized string:", serialized1)
    
    deserialized1 = codec.deserialize(serialized1)
    print("\nDeserialized tree:")
    print_tree(deserialized1)
    
    # Test case 2: Complex binary tree with null nodes
    root2 = TreeNode(5)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.right.left = TreeNode(4)
    root2.right.right = TreeNode(7)
    
    print("\nTest Case 2:")
    print("Original tree:")
    print_tree(root2)
    
    serialized2 = codec.serialize(root2)
    print("\nSerialized string:", serialized2)
    
    deserialized2 = codec.deserialize(serialized2)
    print("\nDeserialized tree:")
    print_tree(deserialized2)
    
    # Test case 3: Empty tree
    root3 = None
    
    print("\nTest Case 3:")
    print("Original tree: None")
    
    serialized3 = codec.serialize(root3)
    print("Serialized string:", serialized3)
    
    deserialized3 = codec.deserialize(serialized3)
    print("Deserialized tree: None") 