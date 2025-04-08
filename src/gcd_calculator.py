def prime_factors(n):
    """
    Compute the prime factors of a given positive integer.
    
    Args:
        n (int): A positive integer to factorize.
    
    Returns:
        list: A list of prime factors of the input number.
    
    Raises:
        ValueError: If input is not a positive integer.
    """
    # Validate input
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive integer")
    
    factors = []
    # Handle special case of 1
    if n == 1:
        return [1]
    
    # Find prime factors
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    
    # If n is a prime number greater than 1
    if n > 1:
        factors.append(n)
    
    return factors

def gcd_using_prime_factors(a, b):
    """
    Calculate the Greatest Common Divisor (GCD) using prime factorization.
    
    Args:
        a (int): First positive integer.
        b (int): Second positive integer.
    
    Returns:
        int: The GCD of a and b.
    
    Raises:
        ValueError: If inputs are not positive integers.
    """
    # Validate inputs
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Inputs must be integers")
    
    if a < 1 or b < 1:
        raise ValueError("Inputs must be positive integers")
    
    # Special cases
    if a == 1 or b == 1:
        return 1
    
    # Get prime factors
    a_factors = prime_factors(a)
    b_factors = prime_factors(b)
    
    # Find common prime factors
    gcd = 1
    a_factor_dict = {}
    b_factor_dict = {}
    
    # Count occurrences of prime factors
    for factor in a_factors:
        a_factor_dict[factor] = a_factor_dict.get(factor, 0) + 1
    
    for factor in b_factors:
        b_factor_dict[factor] = b_factor_dict.get(factor, 0) + 1
    
    # Compute GCD using common prime factors
    for factor, count in a_factor_dict.items():
        if factor in b_factor_dict:
            gcd *= factor ** min(count, b_factor_dict[factor])
    
    return gcd