from src.prime_factorization import prime_factorization

def gcd_using_prime_factors(a, b):
    """
    Calculate the Greatest Common Divisor (GCD) using prime factorization.
    
    This function finds the GCD by comparing the prime factors of two numbers
    and multiplying the common factors.
    
    Args:
        a (int): First positive integer.
        b (int): Second positive integer.
    
    Returns:
        int: The Greatest Common Divisor of a and b.
    
    Raises:
        ValueError: If inputs are not positive integers.
    """
    # Validate inputs
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Inputs must be integers")
    
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers")
    
    # Handle special case where either number is 1
    if a == 1 or b == 1:
        return 1
    
    # Get prime factors for both numbers
    factors_a = prime_factorization(a)
    factors_b = prime_factorization(b)
    
    # Find common prime factors
    gcd_factors = []
    a_copy = factors_a.copy()
    b_copy = factors_b.copy()
    
    for factor in a_copy:
        if factor in b_copy:
            gcd_factors.append(factor)
            b_copy.remove(factor)
    
    # Calculate GCD by multiplying common prime factors
    gcd = 1
    for factor in gcd_factors:
        gcd *= factor
    
    return gcd