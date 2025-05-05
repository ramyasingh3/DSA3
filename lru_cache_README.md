# LRU Cache

## Problem Description
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache. The cache should support the following operations:
- `get(key)`: Get the value of the key if it exists, otherwise return -1
- `put(key, value)`: Set or insert the value if the key is not present
- When the cache reaches its capacity, it should invalidate the least recently used item

## Examples
```
Input:
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output: [null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation:
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
```

## Constraints
- 1 <= capacity <= 3000
- 0 <= key <= 10^4
- 0 <= value <= 10^5
- At most 2 * 10^5 calls will be made to get and put

## Approach 1: OrderedDict
1. Use Python's OrderedDict to maintain insertion order
2. For get operation:
   - Return -1 if key not found
   - Move key to end (most recently used)
3. For put operation:
   - Remove key if exists
   - Remove least recently used if at capacity
   - Add new key-value pair
4. Time Complexity: O(1) for both operations
5. Space Complexity: O(capacity)

## Approach 2: Doubly Linked List + Hash Map
1. Use doubly linked list to maintain order
2. Use hash map for O(1) access
3. For get operation:
   - Return -1 if key not found
   - Move node to front (most recently used)
4. For put operation:
   - Update node if exists
   - Remove least recently used if at capacity
   - Add new node to front
5. Time Complexity: O(1) for both operations
6. Space Complexity: O(capacity)

## Approach 3: Array with Timestamps
1. Use array/hash map to store values and timestamps
2. For get operation:
   - Return -1 if key not found
   - Update timestamp
3. For put operation:
   - Update timestamp if key exists
   - Remove least recently used if at capacity
   - Add new key-value pair
4. Time Complexity: O(n) for both operations
5. Space Complexity: O(capacity)

## Time and Space Complexity Comparison
| Approach              | Time Complexity | Space Complexity | Notes                    |
|----------------------|-----------------|------------------|--------------------------|
| OrderedDict          | O(1)           | O(capacity)      | Built-in solution        |
| Doubly Linked List   | O(1)           | O(capacity)      | Custom implementation    |
| Array with Timestamps| O(n)           | O(capacity)      | Educational purpose      |

## Key Points
- This is a fundamental data structure problem
- Multiple valid approaches exist
- Edge cases to consider:
  - Empty cache
  - Single item
  - Full cache
  - Updating existing key
  - Cache eviction
- Trade-offs between approaches

## Common Applications
- Browser cache
- CPU cache
- Database caching
- Web server caching
- Memory management
- Resource allocation
- Performance optimization

## Example Walkthrough
For capacity = 2:
```
1. put(1, 1)
   Cache: {1=1}
   Order: [1]

2. put(2, 2)
   Cache: {1=1, 2=2}
   Order: [1, 2]

3. get(1)
   Cache: {1=1, 2=2}
   Order: [2, 1]  # 1 becomes most recently used

4. put(3, 3)
   Cache: {1=1, 3=3}  # 2 is evicted
   Order: [1, 3]

5. get(2)
   Returns -1 (not found)

6. put(4, 4)
   Cache: {3=3, 4=4}  # 1 is evicted
   Order: [3, 4]
```

## Follow-up Questions
1. What if we need to implement an LFU (Least Frequently Used) cache?
2. What if we need to implement a cache with time-based expiration?
3. What if we need to implement a cache with size-based eviction?
4. What if we need to implement a cache with multiple levels?
5. What if we need to implement a distributed cache?

## Optimization Tips
1. Use OrderedDict for simplicity
2. Use doubly linked list for custom implementation
3. Handle edge cases early
4. Use dummy nodes for cleaner code
5. Consider thread safety
6. Implement proper cleanup
7. Monitor cache hit ratio 