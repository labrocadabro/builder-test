from src.prime_factorization import prime_factorization

def gcd_using_prime_factors(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) using prime factorization.
    
    Args:
        a (int): First positive integer
        b (int): Second positive integer
    
    Returns:
        int: The Greatest Common Divisor of a and b
    
    Raises:
        ValueError: If either input is less than or equal to 0
    """
    # Validate inputs
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers")
    
    # If inputs are the same, return the input
    if a == b:
        return a
    
    # Get prime factorizations of both numbers
    a_factors = prime_factorization(a)
    b_factors = prime_factorization(b)
    
    # Find common prime factors
    gcd = 1
    for prime, count in a_factors.items():
        if prime in b_factors:
            # Take the minimum count of the common prime factor
            gcd *= prime ** min(count, b_factors[prime])
    
    return gcd