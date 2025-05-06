from typing import List, Union, Any

def flatten_array(arr: List[Union[Any, List]]) -> List[Any]:
    """
    Recursively flatten a nested array of arbitrary depth into a single-level list.
    
    Args:
        arr (List[Union[Any, List]]): A potentially nested list to be flattened.
    
    Returns:
        List[Any]: A flattened list containing all non-list elements.
    
    Examples:
        >>> flatten_array([1, [2, 3], [4, [5, 6]]])
        [1, 2, 3, 4, 5, 6]
        >>> flatten_array([])
        []
        >>> flatten_array([1, 2, 3])
        [1, 2, 3]
    """
    flattened = []
    
    for item in arr:
        # If the item is a list, recursively flatten it
        if isinstance(item, list):
            flattened.extend(flatten_array(item))
        else:
            # If not a list, add the item directly
            flattened.append(item)
    
    return flattened