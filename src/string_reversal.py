def reverse_string(s: str) -> str:
    """
    Reverse the given string using a manual character-by-character approach.

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
    
    # Use a manual reversal approach
    reversed_chars = []
    for i in range(len(s) - 1, -1, -1):
        reversed_chars.append(s[i])
    
    return ''.join(reversed_chars)