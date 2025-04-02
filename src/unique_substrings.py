def find_unique_substrings(s: str) -> list[str]:
    """
    Find all unique substrings within the given input string.
    
    Args:
        s (str): The input string to find substrings from.
    
    Returns:
        list[str]: A list of unique substrings, sorted in order of first appearance.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> find_unique_substrings("abc")
        ['a', 'b', 'c', 'ab', 'bc', 'abc']
        >>> find_unique_substrings("")
        []
    """
    # Validate input
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Track unique substrings while preserving order
    unique_substrings = []
    seen = set()
    
    # Iterate through all possible substring lengths
    for length in range(1, len(s) + 1):
        for i in range(len(s) - length + 1):
            substring = s[i:i+length]
            if substring not in seen:
                unique_substrings.append(substring)
                seen.add(substring)
    
    return unique_substrings