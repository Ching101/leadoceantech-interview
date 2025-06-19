from typing import List, Optional
from list_node import ListNode

def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Merges k sorted linked lists into one sorted linked list.
    
    Args:
        lists: List of ListNode, where each ListNode is the head of a sorted linked list.
    
    Returns:
        ListNode: Head of the merged sorted linked list.
    """
    # TODO: Implement this function
    # Steps to consider:
    # 1. Handle edge cases (What cases should we consider?)
    # 2. Decide on a strategy (What strategy should we use? and Why?)
    # 3. Merge nodes while maintaining sorted order
    # 4. Update pointers to build the result list
    # 5. Return the head of the merged list
    pass

# Helper function to create a linked list from a list of values (for testing)
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print a linked list (for testing)
def print_linked_list(head):
    values = []
    current = head
    while current:
        values.append(str(current.val))
        current = current.next
    return " -> ".join(values) if values else "None"

# Test cases (for testing your implementation)
if __name__ == "__main__":
    # Test case 1: Normal case with 3 lists
    list1 = create_linked_list([1, 4, 5])
    list2 = create_linked_list([1, 3, 4])
    list3 = create_linked_list([2, 6])
    result = merge_k_lists([list1, list2, list3])
    print("Test 1:", print_linked_list(result))  # Expected: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6

    # Test case 2: Empty lists array
    result = merge_k_lists([])
    print("Test 2:", print_linked_list(result))  # Expected: None

    # Test case 3: Lists with some empty
    list1 = create_linked_list([])
    list2 = create_linked_list([1])
    result = merge_k_lists([list1, list2])
    print("Test 3:", print_linked_list(result))  # Expected: 1

    # Test case 4: Single list
    list1 = create_linked_list([1, 2, 3])
    result = merge_k_lists([list1])
    print("Test 4:", print_linked_list(result))  # Expected: 1 -> 2 -> 3