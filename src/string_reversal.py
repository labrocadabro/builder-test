def reverse_string(input_string):
    """
    Reverses the given input string manually, without using slice notation or built-in reverse methods.

    Args:
        input_string (str): The string to be reversed.

    Returns:
        str: The reversed string.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Convert string to a list of characters
    chars = list(input_string)
    
    # Reverse the list using two-pointer technique
    left, right = 0, len(chars) - 1
    while left < right:
        # Swap characters
        chars[left], chars[right] = chars[right], chars[left]
        
        # Move pointers towards the center
        left += 1
        right -= 1
    
    # Convert list back to string and return
    return ''.join(chars)