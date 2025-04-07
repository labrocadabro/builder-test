def reverse_string(s: str) -> str:
    """
    Reverse a given string using a manual character-by-character approach.

    Args:
        s (str): The input string to be reversed.

    Returns:
        str: The reversed string.

    Raises:
        TypeError: If the input is not a string.
    """
    # Validate input is a string
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Manual string reversal using a list approach
    # This preserves all characters including spaces and special characters
    reversed_chars = []
    for i in range(len(s) - 1, -1, -1):
        reversed_chars.append(s[i])
    
    return ''.join(reversed_chars)