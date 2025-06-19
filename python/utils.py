from typing import List, Optional
from list_node import ListNode

def create_linked_list(values: List[int]) -> Optional[ListNode]:
    """
    Creates a linked list from a list of values.
    
    Args:
        values: List of integers to create the linked list from
        
    Returns:
        Head of the created linked list, or None if values is empty
    """
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head: Optional[ListNode]) -> str:
    """
    Converts a linked list to a string representation.
    
    Args:
        head: Head of the linked list to print
        
    Returns:
        String representation of the linked list
    """
    values = []
    current = head
    while current:
        values.append(str(current.val))
        current = current.next
    return " -> ".join(values) if values else "None" 