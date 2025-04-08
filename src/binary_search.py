def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the target element.
    
    Args:
        arr (list): A sorted list of comparable elements.
        target: The element to search for in the array.
    
    Returns:
        int: The index of the target element if found, otherwise -1.
    
    Raises:
        TypeError: If the input array is not sorted or is not a list.
        ValueError: If the input array contains incomparable elements.
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if the array is sorted
    if arr != sorted(arr):
        raise TypeError("Input array must be sorted in ascending order")
    
    # Perform binary search
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Check if target is found
        if arr[mid] == target:
            return mid
        
        # If target is greater, ignore left half
        if arr[mid] < target:
            left = mid + 1
        
        # If target is smaller, ignore right half
        else:
            right = mid - 1
    
    # Target not found
    return -1