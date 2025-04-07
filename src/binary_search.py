def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the index of a target value.

    Args:
        arr (list): A sorted list of comparable elements (ascending order)
        target: The value to search for in the array

    Returns:
        int: Index of the target if found, -1 otherwise

    Raises:
        TypeError: If input is not a list
        ValueError: If the input list is not sorted
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if list is sorted
    if any(arr[i] > arr[i+1] for i in range(len(arr)-1)):
        raise ValueError("Input list must be sorted in ascending order")
    
    # Handle empty list
    if not arr:
        return -1
    
    # Binary search implementation
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Check if target is found
        if arr[mid] == target:
            return mid
        
        # Adjust search boundaries
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    # Target not found
    return -1