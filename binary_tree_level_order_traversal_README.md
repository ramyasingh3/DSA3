# Binary Tree Level Order Traversal

## Problem Description
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

### Examples
```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Input: root = [1]
Output: [[1]]

Input: root = []
Output: []
```

## Approach
1. Breadth-First Search (BFS) using a queue:
   - Initialize queue with root node
   - While queue is not empty:
     - Process all nodes at current level
     - Add their children to queue for next level
     - Store values of current level in result

### Key Points
- Queue-based BFS implementation
- O(n) time complexity
- O(n) space complexity for queue
- Handles empty tree
- Preserves level order

## Time Complexity
- O(n) where n is the number of nodes
  - We visit each node exactly once

## Space Complexity
- O(n) in the worst case
  - Queue can hold up to n/2 nodes (last level of complete binary tree)
  - Result list stores all node values 