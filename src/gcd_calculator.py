from src.prime_factorization import prime_factorization

def gcd_using_prime_factors(a, b):
    """
    Calculate the Greatest Common Divisor (GCD) using Prime Factorization method.
    
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
        raise TypeError("Inputs must be integers")
    
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers")
    
    # Special case: if either number is 1, GCD is the minimum of a and b
    if a == 1 or b == 1:
        return min(a, b)
    
    # Get prime factorizations
    a_factors = prime_factorization(a)
    b_factors = prime_factorization(b)
    
    # Find common prime factors
    gcd = 1
    a_factor_dict = {}
    b_factor_dict = {}
    
    # Count occurrences of prime factors
    for factor in a_factors:
        a_factor_dict[factor] = a_factor_dict.get(factor, 0) + 1
    
    for factor in b_factors:
        b_factor_dict[factor] = b_factor_dict.get(factor, 0) + 1
    
    # Calculate GCD by multiplying common prime factors with minimum occurrences
    for prime, count in a_factor_dict.items():
        if prime in b_factor_dict:
            common_count = min(count, b_factor_dict[prime])
            gcd *= prime ** common_count
    
    return gcd