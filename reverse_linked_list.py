"""
Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:
- The number of nodes in the list is the range [0, 5000]
- -5000 <= Node.val <= 5000
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list_iterative(head: ListNode) -> ListNode:
    """
    Approach 1: Iterative
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    prev = None
    curr = head
    
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    
    return prev

def reverse_list_recursive(head: ListNode) -> ListNode:
    """
    Approach 2: Recursive
    Time Complexity: O(n)
    Space Complexity: O(n) due to recursion stack
    """
    if not head or not head.next:
        return head
    
    new_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    
    return new_head

def reverse_list_stack(head: ListNode) -> ListNode:
    """
    Approach 3: Using Stack
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if not head:
        return None
        
    stack = []
    curr = head
    
    # Push all nodes to stack
    while curr:
        stack.append(curr)
        curr = curr.next
    
    # Set new head
    new_head = stack.pop()
    curr = new_head
    
    # Pop nodes and reverse links
    while stack:
        curr.next = stack.pop()
        curr = curr.next
    
    curr.next = None
    return new_head

def create_linked_list(values):
    """Helper function to create a linked list from a list of values"""
    if not values:
        return None
    
    head = ListNode(values[0])
    curr = head
    
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    
    return head

def linked_list_to_list(head):
    """Helper function to convert linked list to Python list"""
    result = []
    curr = head
    
    while curr:
        result.append(curr.val)
        curr = curr.next
    
    return result

def test_reverse_linked_list():
    test_cases = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([], []),
        ([1], [1]),
        ([1, 2, 3], [3, 2, 1])
    ]
    
    for input_values, expected in test_cases:
        # Create input linked list
        head = create_linked_list(input_values)
        
        # Test iterative approach
        reversed_head = reverse_list_iterative(head)
        result = linked_list_to_list(reversed_head)
        assert result == expected, f"Iterative approach failed for {input_values}"
        
        # Test recursive approach
        head = create_linked_list(input_values)
        reversed_head = reverse_list_recursive(head)
        result = linked_list_to_list(reversed_head)
        assert result == expected, f"Recursive approach failed for {input_values}"
        
        # Test stack approach
        head = create_linked_list(input_values)
        reversed_head = reverse_list_stack(head)
        result = linked_list_to_list(reversed_head)
        assert result == expected, f"Stack approach failed for {input_values}"
        
        print(f"Test passed for input: {input_values}")

if __name__ == "__main__":
    test_reverse_linked_list()
    print("All test cases passed!") 