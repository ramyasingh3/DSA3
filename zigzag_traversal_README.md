# Binary Tree Zigzag Level Order Traversal

## Problem Description
Given a binary tree, return the zigzag level order traversal of its nodes' values. Zigzag traversal means that nodes are processed from left to right, then right to left for the next level, and so on, alternating between directions.

## Examples

### Example 1: Tree with Multiple Levels
```
    3
   / \
  9   20
     /  \
    15   7
```
Zigzag level order traversal: [[3], [20, 9], [15, 7]]

### Example 2: Tree with Overlapping Nodes
```
    1
   / \
  2   3
 / \   \
4   5   6
```
Zigzag level order traversal: [[1], [3, 2], [4, 5, 6]]

### Example 3: Left-skewed Tree
```
    1
   /
  2
 /
3
```
Zigzag level order traversal: [[1], [2], [3]]

## Solution Approach
The solution provides two implementations:

1. **Basic Implementation**:
   - Uses BFS with a queue
   - Tracks direction with a boolean flag
   - Reverses the current level when needed
   - Time Complexity: O(N)
   - Space Complexity: O(N)

2. **Optimized Implementation**:
   - Uses deque for efficient operations
   - Changes traversal direction based on level
   - Avoids list reversal by using deque operations
   - Time Complexity: O(N)
   - Space Complexity: O(N)

## Key Features
1. **Direction Control**:
   - Alternates between left-to-right and right-to-left
   - Uses a boolean flag to track direction
   - Changes direction after each level

2. **Level Processing**:
   - Processes one level at a time
   - Maintains level order
   - Preserves node values

3. **Optimization**:
   - Uses deque for efficient operations
   - Avoids unnecessary list reversals
   - Better performance for large trees

## Usage
```python
# Create a binary tree
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)

# Create Solution instance
solution = Solution()

# Get zigzag level order traversal
zigzag_order = solution.zigzagLevelOrder(root)
print(f"Zigzag order: {zigzag_order}")

# Get optimized zigzag level order traversal
zigzag_order_opt = solution.zigzagLevelOrderOptimized(root)
print(f"Optimized zigzag order: {zigzag_order_opt}")
```

## Test Cases
The implementation includes three test cases:

1. **Tree with Multiple Levels**:
   - Tests basic zigzag traversal
   - Expected output: [[3], [20, 9], [15, 7]]

2. **Tree with Overlapping Nodes**:
   - Tests handling of multiple nodes per level
   - Expected output: [[1], [3, 2], [4, 5, 6]]

3. **Left-skewed Tree**:
   - Tests edge case with minimal branching
   - Expected output: [[1], [2], [3]]

## Running the Tests
```bash
python zigzag_traversal.py
```

## Implementation Details
The implementation includes:
1. `TreeNode` class for creating binary tree nodes
2. `Solution` class with two methods:
   - `zigzagLevelOrder`: Basic implementation
   - `zigzagLevelOrderOptimized`: Optimized implementation using deque
3. Helper functions:
   - `print_tree`: Visualizes the tree structure
   - `build_test_tree*`: Creates test trees
4. Comprehensive test cases with visual output

## Common Applications
- Tree visualization
- Level-based tree analysis
- Tree structure debugging
- UI layout optimization
- Hierarchical data representation 