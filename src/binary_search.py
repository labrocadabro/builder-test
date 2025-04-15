from typing import List, TypeVar, Optional

T = TypeVar('T')

def binary_search(arr: List[T], target: T) -> Optional[int]:
    """
    Perform binary search on a sorted list to find the index of the target.

    Args:
        arr (List[T]): A sorted list of elements
        target (T): The element to search for

    Returns:
        Optional[int]: The index of the target if found, None otherwise

    Raises:
        TypeError: If the input list is not sorted
    """
    # Check for empty list
    if not arr:
        return None

    # Validate that the list is sorted
    if not all(arr[i] <= arr[i+1] for i in range(len(arr)-1)):
        raise TypeError("Input list must be sorted in ascending order")

    left, right = 0, len(arr) - 1

    while left <= right:
        # Calculate middle index to avoid potential integer overflow
        mid = left + (right - left) // 2

        # Check if target is found
        if arr[mid] == target:
            return mid
        
        # If target is less than middle, search left half
        if arr[mid] > target:
            right = mid - 1
        # If target is greater than middle, search right half
        else:
            left = mid + 1

    # Target not found
    return None