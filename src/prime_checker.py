def is_prime(number) -> bool:
    """
    Check if a given number is prime.
    
    A prime number is a natural number greater than 1 that is only divisible by 1 and itself.
    
    Args:
        number: The number to check for primality.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    
    Raises:
        ValueError: If the input is not an integer.
    """
    # Validate input type 
    try:
        # Try to convert to an integer
        num = int(number)
        
        # Ensure the conversion was exact (no floating point or non-numeric input)
        if not isinstance(number, (int, float)) or float(number) != num:
            raise ValueError("Input must be an integer")
    except (TypeError, ValueError):
        raise ValueError("Input must be an integer")
    
    # Check for non-positive numbers
    if num < 2:
        return False
    
    # Check for divisibility up to the square root of the number
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    
    return True