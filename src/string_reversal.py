def reverse_string(s: str) -> str:
    """
    Reverses the given string manually.

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
    
    # Manual string reversal using list conversion and iteration
    reversed_chars = []
    for char in s:
        reversed_chars.insert(0, char)
    
    return ''.join(reversed_chars)