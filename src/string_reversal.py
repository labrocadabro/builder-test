def reverse_string(s: str) -> str:
    """
    Reverses the given input string using a manual character-by-character approach.

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
    
    # Use a list to build the reversed string
    reversed_chars = []
    
    # Iterate through the string from end to beginning
    for i in range(len(s) - 1, -1, -1):
        reversed_chars.append(s[i])
    
    # Convert the list of characters back to a string
    return ''.join(reversed_chars)