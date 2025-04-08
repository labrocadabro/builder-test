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
    # Explicitly check for various invalid input types
    if number is None or isinstance(number, (list, dict, set, tuple)) or isinstance(number, str):
        raise ValueError("Input must be an integer")
    
    # Validate integer type and value
    try:
        # Attempt to convert to int, ensuring no information loss
        num = int(number)
        if float(number) != num:
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