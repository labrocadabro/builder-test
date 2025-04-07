def reverse_string(s: str) -> str:
    """
    Reverse the given string manually while preserving spaces and special characters.

    Args:
        s (str): The input string to be reversed.

    Returns:
        str: The reversed string.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Convert string to list for manual reversal
    chars = list(s)
    
    # Manually reverse the list
    left, right = 0, len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    
    # Convert back to string
    return ''.join(chars)