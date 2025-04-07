def prime_factorization(n):
    """
    Compute the prime factorization of a given positive integer.
    
    Args:
        n (int): A positive integer to factorize.
    
    Returns:
        list: A list of prime factors in ascending order.
    
    Raises:
        ValueError: If the input is less than 2.
        TypeError: If the input is not an integer.
    """
    # Check input type
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    # Check input range
    if n < 2:
        raise ValueError("Input must be greater than or equal to 2")
    
    # List to store prime factors
    factors = []
    
    # Handle 2 as a special case first
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    
    # Check for odd prime factors
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            factors.append(factor)
            n = n // factor
        factor += 2
    
    # If n is a prime number greater than 2
    if n > 2:
        factors.append(n)
    
    return factors