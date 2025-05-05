def reverse_string(s: str) -> str:
    """
    Reverses the given input string.

    Args:
        s (str): The input string to be reversed.

    Returns:
        str: The reversed string.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check for valid input type
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Return the reversed string
    return s[::-1]