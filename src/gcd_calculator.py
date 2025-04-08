from src.prime_factorization import prime_factorization

def gcd_using_prime_factors(a: int, b: int) -> int:
    """
    Compute the Greatest Common Divisor (GCD) of two numbers using prime factorization.
    
    This function calculates the GCD by finding the common prime factors 
    between the two input numbers.
    
    Args:
        a (int): The first positive integer.
        b (int): The second positive integer.
    
    Returns:
        int: The Greatest Common Divisor of a and b.
    
    Raises:
        ValueError: If either input is not a positive integer.
    """
    # Validate inputs
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Inputs must be integers")
    
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers")
    
    # Handle special cases
    if a == b:
        return a
    
    # Get prime factorizations
    factors_a = prime_factorization(a)
    factors_b = prime_factorization(b)
    
    # Find common prime factors
    gcd_factors = []
    a_factor_copy = factors_a.copy()
    
    for factor in factors_b:
        if factor in a_factor_copy:
            gcd_factors.append(factor)
            a_factor_copy.remove(factor)
    
    # Compute GCD by multiplying common prime factors
    gcd = 1
    for factor in gcd_factors:
        gcd *= factor
    
    return gcd

# Alias to make function more accessible
gcd = gcd_using_prime_factors