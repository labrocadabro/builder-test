def reverse_string(s: str) -> str:
    """
    Reverses the given string manually without using slice notation or reverse().

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
    
    # Convert string to list of characters for manual reversal
    chars = list(s)
    
    # Manually reverse the list of characters
    left, right = 0, len(chars) - 1
    while left < right:
        # Swap characters from both ends moving towards the center
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    
    # Convert the list of characters back to a string
    return ''.join(chars)