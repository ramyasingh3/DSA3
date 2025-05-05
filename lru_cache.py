"""
LRU Cache Implementation

This file contains multiple implementations of a Least Recently Used (LRU) cache.

Problem Statement:
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
- get(key): Get the value of the key if it exists, otherwise return -1
- put(key, value): Set or insert the value if the key is not present
- When the cache reaches its capacity, it should invalidate the least recently used item

Time Complexity: O(1) for both get and put operations
Space Complexity: O(capacity) for optimal solution
"""

from collections import OrderedDict
from typing import Optional

class Node:
    """Doubly Linked List Node"""
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None

class LRUCacheOrderedDict:
    """
    LRU Cache implementation using OrderedDict.
    Time Complexity: O(1) for both get and put
    Space Complexity: O(capacity)
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        # Move key to end (most recently used)
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Remove existing key
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            # Remove least recently used item
            self.cache.popitem(last=False)
        
        # Add new key-value pair
        self.cache[key] = value

class LRUCacheDoublyLinkedList:
    """
    LRU Cache implementation using Doubly Linked List and Hash Map.
    Time Complexity: O(1) for both get and put
    Space Complexity: O(capacity)
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node
        self.head = Node()  # Dummy head
        self.tail = Node()  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove_node(self, node: Node) -> None:
        """Remove node from its current position"""
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _add_to_front(self, node: Node) -> None:
        """Add node to front (most recently used)"""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    
    def _move_to_front(self, node: Node) -> None:
        """Move node to front (most recently used)"""
        self._remove_node(node)
        self._add_to_front(node)
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._move_to_front(node)
        return node.value
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update existing node
            node = self.cache[key]
            node.value = value
            self._move_to_front(node)
        else:
            if len(self.cache) >= self.capacity:
                # Remove least recently used node
                lru_node = self.tail.prev
                self._remove_node(lru_node)
                del self.cache[lru_node.key]
            
            # Add new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)

class LRUCacheArray:
    """
    LRU Cache implementation using arrays (for educational purposes).
    Time Complexity: O(n) for both get and put
    Space Complexity: O(capacity)
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> (value, timestamp)
        self.timestamp = 0
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        value, _ = self.cache[key]
        self.cache[key] = (value, self.timestamp)
        self.timestamp += 1
        return value
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = (value, self.timestamp)
        else:
            if len(self.cache) >= self.capacity:
                # Find least recently used key
                lru_key = min(self.cache.items(), key=lambda x: x[1][1])[0]
                del self.cache[lru_key]
            
            self.cache[key] = (value, self.timestamp)
        
        self.timestamp += 1

def test_lru_cache():
    """Test cases for LRU Cache implementations"""
    test_cases = [
        # Test case 1: Basic operations
        {
            'operations': [
                ('put', 1, 1),
                ('put', 2, 2),
                ('get', 1, 1),
                ('put', 3, 3),
                ('get', 2, -1),
                ('put', 4, 4),
                ('get', 1, -1),
                ('get', 3, 3),
                ('get', 4, 4)
            ],
            'capacity': 2
        },
        # Test case 2: Update existing key
        {
            'operations': [
                ('put', 1, 1),
                ('put', 2, 2),
                ('put', 1, 10),
                ('get', 1, 10),
                ('get', 2, 2)
            ],
            'capacity': 2
        },
        # Test case 3: Empty cache
        {
            'operations': [
                ('get', 1, -1),
                ('put', 1, 1),
                ('get', 1, 1)
            ],
            'capacity': 1
        },
        # Test case 4: Full cache
        {
            'operations': [
                ('put', 1, 1),
                ('put', 2, 2),
                ('put', 3, 3),
                ('get', 1, -1),
                ('get', 2, 2),
                ('get', 3, 3)
            ],
            'capacity': 2
        }
    ]
    
    for test_case in test_cases:
        capacity = test_case['capacity']
        operations = test_case['operations']
        
        # Test OrderedDict implementation
        cache1 = LRUCacheOrderedDict(capacity)
        for op, *args in operations:
            if op == 'get':
                result = cache1.get(args[0])
                assert result == args[1], f"OrderedDict test failed for {op} {args}"
            else:
                cache1.put(args[0], args[1])
        
        # Test DoublyLinkedList implementation
        cache2 = LRUCacheDoublyLinkedList(capacity)
        for op, *args in operations:
            if op == 'get':
                result = cache2.get(args[0])
                assert result == args[1], f"DoublyLinkedList test failed for {op} {args}"
            else:
                cache2.put(args[0], args[1])
        
        # Test Array implementation
        cache3 = LRUCacheArray(capacity)
        for op, *args in operations:
            if op == 'get':
                result = cache3.get(args[0])
                assert result == args[1], f"Array test failed for {op} {args}"
            else:
                cache3.put(args[0], args[1])
    
    print("All test cases passed!")

if __name__ == "__main__":
    # Run test cases
    test_lru_cache()
    
    # Example usage
    print("\nTesting LRU Cache with OrderedDict:")
    cache1 = LRUCacheOrderedDict(2)
    cache1.put(1, 1)
    cache1.put(2, 2)
    print(f"get(1): {cache1.get(1)}")  # returns 1
    cache1.put(3, 3)
    print(f"get(2): {cache1.get(2)}")  # returns -1
    cache1.put(4, 4)
    print(f"get(1): {cache1.get(1)}")  # returns -1
    print(f"get(3): {cache1.get(3)}")  # returns 3
    print(f"get(4): {cache1.get(4)}")  # returns 4
    
    print("\nTesting LRU Cache with DoublyLinkedList:")
    cache2 = LRUCacheDoublyLinkedList(2)
    cache2.put(1, 1)
    cache2.put(2, 2)
    print(f"get(1): {cache2.get(1)}")  # returns 1
    cache2.put(3, 3)
    print(f"get(2): {cache2.get(2)}")  # returns -1
    cache2.put(4, 4)
    print(f"get(1): {cache2.get(1)}")  # returns -1
    print(f"get(3): {cache2.get(3)}")  # returns 3
    print(f"get(4): {cache2.get(4)}")  # returns 4
    
    print("\nTesting LRU Cache with Array (slower implementation):")
    cache3 = LRUCacheArray(2)
    cache3.put(1, 1)
    cache3.put(2, 2)
    print(f"get(1): {cache3.get(1)}")  # returns 1
    cache3.put(3, 3)
    print(f"get(2): {cache3.get(2)}")  # returns -1
    cache3.put(4, 4)
    print(f"get(1): {cache3.get(1)}")  # returns -1
    print(f"get(3): {cache3.get(3)}")  # returns 3
    print(f"get(4): {cache3.get(4)}")  # returns 4 