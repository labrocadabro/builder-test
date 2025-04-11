def reverse_string(s: str) -> str:
    """
    Manually reverse a given string while preserving all characters.

    Args:
        s (str): The input string to be reversed.

    Returns:
        str: The reversed string.

    Raises:
        TypeError: If the input is not a string.
    """
    # Type checking
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not s:
        return ""
    
    # Convert string to list of characters for manual reversal
    chars = list(s)
    
    # Manual in-place reversal using two-pointer technique
    left, right = 0, len(chars) - 1
    while left < right:
        # Swap characters
        chars[left], chars[right] = chars[right], chars[left]
        
        # Move pointers
        left += 1
        right -= 1
    
    # Convert back to string and return
    return ''.join(chars)