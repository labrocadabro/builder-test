from typing import List, Union, Any

def flatten_array(arr: Union[List[Any], Any]) -> List[Any]:
    """
    Recursively flatten a nested array of arbitrary depth into a single-level list.
    
    Args:
        arr (Union[List[Any], Any]): Input array or nested array to be flattened.
    
    Returns:
        List[Any]: A flattened list containing all non-list elements.
    
    Examples:
        >>> flatten_array([1, [2, 3], [4, [5, 6]]])
        [1, 2, 3, 4, 5, 6]
        >>> flatten_array([1, 2, 3])
        [1, 2, 3]
        >>> flatten_array([])
        []
    """
    # If input is not a list, return it as a single-element list
    if not isinstance(arr, list):
        return [arr]
    
    # If list is empty, return empty list
    if not arr:
        return []
    
    # Recursive flattening
    flattened = []
    for item in arr:
        # Recursively flatten each item
        flattened.extend(flatten_array(item))
    
    return flattened