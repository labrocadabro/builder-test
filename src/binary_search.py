def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the target element.
    
    Args:
        arr (list): A sorted list of comparable elements
        target: The element to search for
    
    Returns:
        int: Index of the target element if found, otherwise -1
    
    Raises:
        TypeError: If the input is not a list
        ValueError: If the input list is not sorted
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if the list is sorted
    if arr != sorted(arr):
        raise ValueError("Input list must be sorted in ascending order")
    
    # Edge case: empty list
    if not arr:
        return -1
    
    # Binary search implementation
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Check if target is found
        if arr[mid] == target:
            return mid
        
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        
        # If target is smaller, ignore right half
        else:
            right = mid - 1
    
    # Target not found
    return -1