from typing import Optional

class ListNode:
    """
    A node in a singly linked list.
    
    Attributes:
        val: The value stored in the node
        next: Reference to the next node in the list
    """
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next 