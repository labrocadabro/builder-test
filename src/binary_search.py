def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the target element.
    
    Args:
        arr (list): A sorted list of comparable elements
        target: The element to search for
    
    Returns:
        int: Index of the FIRST occurrence of the target element if found, -1 otherwise
    
    Raises:
        TypeError: If input is not a list
        ValueError: If the input list is not sorted
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if list is sorted
    if not all(arr[i] <= arr[i+1] for i in range(len(arr)-1)):
        raise ValueError("Input list must be sorted in ascending order")
    
    # Handle empty list
    if not arr:
        return -1
    
    # Perform binary search with modification to find first occurrence
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        # If target is found, save the index but continue searching left
        if arr[mid] == target:
            result = mid
            right = mid - 1  # continue searching in the left half
        
        # Adjust search range
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result