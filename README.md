# Serialize and Deserialize Binary Tree

## Problem Description
Design an algorithm to serialize and deserialize a binary tree. Serialization is the process of converting a data structure or object into a sequence of bits/string so that it can be stored in a file or memory buffer, or transmitted across a network connection. Deserialization is the reverse process where the string is converted back into the original data structure.

There should be no loss of information during these transformations - the deserialized tree should be identical to the original tree.

## Examples

### Example 1: Simple Binary Tree
```
Input Tree:
    1
   / \
  2   3
 /
4

Serialized String:
[1,2,3,4]

After Deserialization:
    1
   / \
  2   3
 /
4
```

### Example 2: Complex Binary Tree with Null Nodes
```
Input Tree:
    5
   / \
  2   3
     / \
    4   7

Serialized String:
[5,2,3,null,null,4,7]

After Deserialization:
    5
   / \
  2   3
     / \
    4   7
```

### Example 3: Empty Tree
```
Input Tree:
null

Serialized String:
[]

After Deserialization:
null
```

## Solution Approach

The solution uses a level-order (BFS) approach for both serialization and deserialization:

### Serialization:
1. Use a queue to perform level-order traversal
2. For each node:
   - If node exists, append its value and add children to queue
   - If node is null, append "null"
3. Remove trailing nulls for efficiency
4. Join values with commas and wrap in brackets

### Deserialization:
1. Parse the string to get array of values
2. Create root node from first value
3. Use a queue to keep track of nodes that need children
4. For each node in queue:
   - Create left child if value exists
   - Create right child if value exists
   - Add new nodes to queue

## Time Complexity
- Serialization: O(N) where N is the number of nodes
- Deserialization: O(N)
- Both operations visit each node exactly once

## Space Complexity
- Serialization: O(N) for the output string and queue
- Deserialization: O(N) for the reconstructed tree and queue
- Both operations use space proportional to the number of nodes

## Usage
```python
# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

# Create codec object
codec = Codec()

# Serialize the tree
serialized = codec.serialize(root)  # Returns "[1,2,3]"

# Deserialize back to tree
deserialized_root = codec.deserialize(serialized)
```

## Running the Tests
```bash
python tree_serialization.py
```

The program includes three test cases:
1. Simple binary tree
2. Complex binary tree with null nodes
3. Empty tree

Each test case demonstrates:
- Original tree structure
- Serialized string representation
- Deserialized tree structure (showing the transformation is lossless) 