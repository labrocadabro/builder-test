def is_prime(number):
    """
    Check if a given number is prime.
    
    A prime number is a natural number greater than 1 that is only divisible by 1 and itself.
    
    Args:
        number (int): The number to check for primality.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    
    Raises:
        TypeError: If the input is not an integer.
    """
    # Check input type
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    
    # 1 is not a prime number by definition
    if number <= 1:
        return False
    
    # Check for primality
    # Optimization: Only check up to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    
    return True