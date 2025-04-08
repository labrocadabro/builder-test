from src.prime_factorization import prime_factorization

def gcd_using_prime_factors(a: int, b: int) -> int:
    """
    Compute the Greatest Common Divisor (GCD) of two numbers using prime factorization.
    
    This function calculates the GCD by finding the common prime factors 
    between the two input numbers.
    
    Args:
        a (int): The first integer.
        b (int): The second integer.
    
    Returns:
        int: The Greatest Common Divisor of a and b.
    
    Raises:
        ValueError: If either input is not an integer.
    """
    # Validate inputs
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Inputs must be integers")
    
    # Handle zero inputs
    if a == 0:
        return abs(b)
    if b == 0:
        return abs(a)
    
    # Take absolute values
    a, b = abs(a), abs(b)
    
    # Euclidean algorithm
    while b:
        a, b = b, a % b
    
    return a

# Alias to make function more accessible
gcd = gcd_using_prime_factors