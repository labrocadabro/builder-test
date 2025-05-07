def is_prime(number):
    """
    Check if a given number is prime.
    
    Args:
        number (int): The number to check for primality.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    
    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is negative.
    """
    # Validate input
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    
    # Handle edge cases
    if number < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Special cases
    if number < 2:
        return False
    
    # Check for primality using trial division
    # Optimize by only checking up to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    
    return True