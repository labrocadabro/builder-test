from src.prime_factorization import prime_factorization

def gcd_using_prime_factors(a, b):
    """
    Calculate the Greatest Common Divisor (GCD) of two numbers using prime factorization.
    
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
    
    # Special case: if either number is 1, GCD is 1
    if a == 1 or b == 1:
        return 1
    
    # Get prime factorizations
    factors_a = prime_factorization(a)
    factors_b = prime_factorization(b)
    
    # Common factor calculation
    gcd = 1
    factor_a_counts = {}
    factor_b_counts = {}
    
    # Count occurrences of prime factors in each number
    for factor in factors_a:
        factor_a_counts[factor] = factor_a_counts.get(factor, 0) + 1
    
    for factor in factors_b:
        factor_b_counts[factor] = factor_b_counts.get(factor, 0) + 1
    
    # Find common prime factors with minimum count
    for factor, count_a in factor_a_counts.items():
        if factor in factor_b_counts:
            common_count = min(count_a, factor_b_counts[factor])
            gcd *= factor ** common_count
    
    return gcd