from src.prime_factorization import prime_factorization

def gcd_using_prime_factors(a, b):
    """
    Calculate the Greatest Common Divisor (GCD) using prime factorization.
    
    Args:
        a (int): First positive integer.
        b (int): Second positive integer.
    
    Returns:
        int: The Greatest Common Divisor of a and b.
    
    Raises:
        ValueError: If inputs are not positive integers.
    """
    # Validate input
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Inputs must be integers")
    
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers")
    
    # Special case: if either number is 1, return 1
    if a == 1 or b == 1:
        return 1
    
    # Get prime factorizations
    a_factors = prime_factorization(a)
    b_factors = prime_factorization(b)
    
    # Find common prime factors
    gcd_factors = []
    a_factor_counter = {}
    b_factor_counter = {}
    
    # Count occurrences of prime factors in each number
    for factor in a_factors:
        a_factor_counter[factor] = a_factor_counter.get(factor, 0) + 1
    
    for factor in b_factors:
        b_factor_counter[factor] = b_factor_counter.get(factor, 0) + 1
    
    # Find common factors with minimum count
    for factor in set(a_factor_counter.keys()) & set(b_factor_counter.keys()):
        common_count = min(a_factor_counter[factor], b_factor_counter[factor])
        gcd_factors.extend([factor] * common_count)
    
    # Calculate GCD by multiplying common prime factors
    gcd = 1
    for factor in gcd_factors:
        gcd *= factor
    
    return gcd