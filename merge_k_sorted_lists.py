"""
Merge K Sorted Lists

This file contains multiple implementations for merging k sorted linked lists.

Problem Statement:
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Time Complexity: O(n log k) for optimal solution
Space Complexity: O(k) for optimal solution
"""

from typing import List, Optional
import heapq
from dataclasses import dataclass, field
from queue import PriorityQueue

class ListNode:
    """Linked List Node"""
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next
    
    def __lt__(self, other: 'ListNode') -> bool:
        """For heap comparison"""
        return self.val < other.val

@dataclass(order=True)
class PrioritizedItem:
    """Wrapper for ListNode to enable comparison in PriorityQueue"""
    priority: int
    node: ListNode = field(compare=False)

class MergeKSortedLists:
    """
    Solution class containing multiple approaches to merge k sorted lists.
    """
    
    @staticmethod
    def merge_two_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """Merge two sorted linked lists"""
        dummy = ListNode()
        current = dummy
        
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        current.next = l1 if l1 else l2
        return dummy.next
    
    @staticmethod
    def merge_k_lists_divide_conquer(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Approach 1: Divide and Conquer
        Time Complexity: O(n log k)
        Space Complexity: O(log k) for recursion stack
        """
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        
        mid = len(lists) // 2
        left = MergeKSortedLists.merge_k_lists_divide_conquer(lists[:mid])
        right = MergeKSortedLists.merge_k_lists_divide_conquer(lists[mid:])
        return MergeKSortedLists.merge_two_lists(left, right)
    
    @staticmethod
    def merge_k_lists_heap(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Approach 2: Min Heap
        Time Complexity: O(n log k)
        Space Complexity: O(k)
        """
        if not lists:
            return None
        
        # Create min heap with first node from each list
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        dummy = ListNode()
        current = dummy
        
        while heap:
            _, i, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next
    
    @staticmethod
    def merge_k_lists_priority_queue(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Approach 3: Priority Queue
        Time Complexity: O(n log k)
        Space Complexity: O(k)
        """
        if not lists:
            return None
        
        # Create priority queue with first node from each list
        pq = PriorityQueue()
        for i, node in enumerate(lists):
            if node:
                pq.put(PrioritizedItem(node.val, node))
        
        dummy = ListNode()
        current = dummy
        
        while not pq.empty():
            item = pq.get()
            node = item.node
            current.next = node
            current = current.next
            
            if node.next:
                pq.put(PrioritizedItem(node.next.val, node.next))
        
        return dummy.next
    
    @staticmethod
    def merge_k_lists_brute_force(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Approach 4: Brute Force
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        if not lists:
            return None
        
        # Collect all values
        values = []
        for head in lists:
            while head:
                values.append(head.val)
                head = head.next
        
        # Sort values
        values.sort()
        
        # Create new linked list
        dummy = ListNode()
        current = dummy
        for val in values:
            current.next = ListNode(val)
            current = current.next
        
        return dummy.next

def create_linked_list(values: List[int]) -> Optional[ListNode]:
    """Helper function to create a linked list from a list of values"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    """Helper function to convert a linked list to a list of values"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def test_merge_k_sorted_lists():
    """Test cases for Merge K Sorted Lists implementations"""
    test_cases = [
        # Test case 1: Basic case
        {
            'lists': [
                create_linked_list([1, 4, 5]),
                create_linked_list([1, 3, 4]),
                create_linked_list([2, 6])
            ],
            'expected': [1, 1, 2, 3, 4, 4, 5, 6]
        },
        # Test case 2: Empty lists
        {
            'lists': [],
            'expected': []
        },
        # Test case 3: Single list
        {
            'lists': [create_linked_list([1, 2, 3])],
            'expected': [1, 2, 3]
        },
        # Test case 4: Lists with different lengths
        {
            'lists': [
                create_linked_list([1, 2, 3]),
                create_linked_list([4, 5]),
                create_linked_list([6])
            ],
            'expected': [1, 2, 3, 4, 5, 6]
        },
        # Test case 5: Lists with duplicate values
        {
            'lists': [
                create_linked_list([1, 1, 1]),
                create_linked_list([1, 1, 1]),
                create_linked_list([1, 1, 1])
            ],
            'expected': [1, 1, 1, 1, 1, 1, 1, 1, 1]
        }
    ]
    
    for test_case in test_cases:
        lists = test_case['lists']
        expected = test_case['expected']
        
        # Test divide and conquer approach
        result1 = MergeKSortedLists.merge_k_lists_divide_conquer(lists)
        assert linked_list_to_list(result1) == expected, "Divide and conquer test failed"
        
        # Test heap approach
        result2 = MergeKSortedLists.merge_k_lists_heap(lists)
        assert linked_list_to_list(result2) == expected, "Heap test failed"
        
        # Test priority queue approach
        result3 = MergeKSortedLists.merge_k_lists_priority_queue(lists)
        assert linked_list_to_list(result3) == expected, "Priority queue test failed"
        
        # Test brute force approach
        result4 = MergeKSortedLists.merge_k_lists_brute_force(lists)
        assert linked_list_to_list(result4) == expected, "Brute force test failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    # Run test cases
    test_merge_k_sorted_lists()
    
    # Example usage
    print("\nTesting Merge K Sorted Lists with example:")
    lists = [
        create_linked_list([1, 4, 5]),
        create_linked_list([1, 3, 4]),
        create_linked_list([2, 6])
    ]
    
    print("Input lists:")
    for i, lst in enumerate(lists):
        print(f"List {i + 1}: {linked_list_to_list(lst)}")
    
    print("\nResults using different approaches:")
    
    result1 = MergeKSortedLists.merge_k_lists_divide_conquer(lists)
    print(f"Divide and Conquer: {linked_list_to_list(result1)}")
    
    result2 = MergeKSortedLists.merge_k_lists_heap(lists)
    print(f"Min Heap: {linked_list_to_list(result2)}")
    
    result3 = MergeKSortedLists.merge_k_lists_priority_queue(lists)
    print(f"Priority Queue: {linked_list_to_list(result3)}")
    
    result4 = MergeKSortedLists.merge_k_lists_brute_force(lists)
    print(f"Brute Force: {linked_list_to_list(result4)}") 