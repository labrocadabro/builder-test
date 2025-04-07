def prime_factors(n):
    """
    Calculate the prime factors of a given number.
    
    Args:
        n (int): A positive integer to factorize.
    
    Returns:
        list: A list of prime factors of the input number.
    
    Raises:
        ValueError: If input is less than or equal to 0.
    """
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
        if d * d > n:
            if n > 1:
                factors.append(n)
            break
    
    return factors

def gcd_prime_factors(a, b):
    """
    Calculate the Greatest Common Divisor (GCD) using prime factorization.
    
    Args:
        a (int): First positive integer.
        b (int): Second positive integer.
    
    Returns:
        int: The greatest common divisor of a and b.
    
    Raises:
        ValueError: If either input is less than or equal to 0.
    """
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers")
    
    # Get prime factors of both numbers
    factors_a = prime_factors(a)
    factors_b = prime_factors(b)
    
    # Find common prime factors
    gcd = 1
    a_copy = factors_a.copy()
    b_copy = factors_b.copy()
    
    for factor in set(factors_a):
        # Count occurrences in both lists and use the minimum
        a_count = a_copy.count(factor)
        b_count = b_copy.count(factor)
        
        # Remove used factors to handle multiplicity
        common_count = min(a_count, b_count)
        gcd *= factor ** common_count
        
        # Remove the used factors
        for _ in range(common_count):
            a_copy.remove(factor)
            b_copy.remove(factor)
    
    return gcd