def flatten_array(arr):
    """
    Recursively flatten a nested array into a single-level array.
    
    Args:
        arr (list): A potentially nested list to be flattened.
    
    Returns:
        list: A flattened version of the input array.
    
    Raises:
        TypeError: If the input is not a list or contains non-list/non-numeric elements.
    
    Examples:
        >>> flatten_array([1, [2, 3], [4, [5, 6]]])
        [1, 2, 3, 4, 5, 6]
        >>> flatten_array([])
        []
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    flattened = []
    
    for item in arr:
        # If the item is a list, recursively flatten it
        if isinstance(item, list):
            flattened.extend(flatten_array(item))
        # If the item is a number, add it directly
        elif isinstance(item, (int, float)):
            flattened.append(item)
        else:
            # Raise an error for unsupported types
            raise TypeError(f"Unsupported item type: {type(item)}")
    
    return flattened