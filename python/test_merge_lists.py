from utils import create_linked_list, print_linked_list
from app import merge_k_lists

def run_tests():
    """Run all test cases for the merge_k_lists function."""
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

if __name__ == "__main__":
    run_tests() 