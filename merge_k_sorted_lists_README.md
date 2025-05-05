# Merge K Sorted Lists

## Problem Description
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order. Merge all the linked-lists into one sorted linked-list and return it.

## Examples
```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
Merging them into one sorted list:
1->1->2->3->4->4->5->6

Input: lists = []
Output: []

Input: lists = [[]]
Output: []
```

## Constraints
- k == lists.length
- 0 <= k <= 10^4
- 0 <= lists[i].length <= 500
- -10^4 <= lists[i][j] <= 10^4
- lists[i] is sorted in ascending order
- The sum of lists[i].length will not exceed 10^4

## Approach 1: Divide and Conquer
1. Divide the k lists into two halves
2. Recursively merge the two halves
3. Use merge_two_lists helper function to merge two sorted lists
4. Time Complexity: O(n log k)
5. Space Complexity: O(log k) for recursion stack

## Approach 2: Min Heap
1. Create a min heap with first node from each list
2. Extract minimum node and add to result
3. Add next node from the same list to heap
4. Repeat until heap is empty
5. Time Complexity: O(n log k)
6. Space Complexity: O(k)

## Approach 3: Priority Queue
1. Similar to min heap approach
2. Use PriorityQueue instead of heapq
3. Wrap ListNode in PrioritizedItem for comparison
4. Time Complexity: O(n log k)
5. Space Complexity: O(k)

## Approach 4: Brute Force
1. Collect all values in an array
2. Sort the array
3. Create new linked list from sorted array
4. Time Complexity: O(n log n)
5. Space Complexity: O(n)

## Time and Space Complexity Comparison
| Approach          | Time Complexity | Space Complexity | Notes                    |
|------------------|-----------------|------------------|--------------------------|
| Divide and Conquer| O(n log k)     | O(log k)         | Recursive solution       |
| Min Heap         | O(n log k)     | O(k)             | Optimal solution         |
| Priority Queue   | O(n log k)     | O(k)             | Alternative to heap      |
| Brute Force      | O(n log n)     | O(n)             | Simple but less efficient|

## Key Points
- This is a fundamental linked list problem
- Multiple valid approaches exist
- Edge cases to consider:
  - Empty lists
  - Single list
  - Lists with different lengths
  - Lists with duplicate values
- Trade-offs between approaches

## Common Applications
- External sorting
- Database operations
- File merging
- Stream processing
- Distributed systems
- Big data processing
- Log aggregation

## Example Walkthrough
For lists = [[1,4,5],[1,3,4],[2,6]]:

### Min Heap Approach:
```
1. Initial heap: [(1,0,1->4->5), (1,1,1->3->4), (2,2,2->6)]
2. Extract min (1,0): result = 1->4->5
3. Add next (4,0): heap = [(1,1,1->3->4), (2,2,2->6), (4,0,4->5)]
4. Extract min (1,1): result = 1->1->3->4
5. Add next (3,1): heap = [(2,2,2->6), (3,1,3->4), (4,0,4->5)]
6. Extract min (2,2): result = 1->1->2->6
7. Add next (6,2): heap = [(3,1,3->4), (4,0,4->5), (6,2,6)]
8. Continue until heap is empty
```

## Follow-up Questions
1. What if the lists are not sorted?
2. What if we need to merge lists in descending order?
3. What if we need to merge lists with different data types?
4. What if we need to merge lists with custom comparison?
5. What if we need to merge lists in a distributed environment?

## Optimization Tips
1. Use min heap for optimal solution
2. Consider memory constraints
3. Handle edge cases early
4. Use dummy nodes for cleaner code
5. Consider thread safety
6. Implement proper cleanup
7. Monitor performance metrics 