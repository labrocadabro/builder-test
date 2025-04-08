from src.gcd_calculator import gcd_using_prime_factors

def lcm_using_gcd(a: int, b: int) -> int:
    """
    Compute the Least Common Multiple (LCM) of two numbers using GCD.
    
    This function calculates the LCM using the formula: 
    LCM(a, b) = |a * b| / GCD(a, b)
    
    Args:
        a (int): The first positive integer.
        b (int): The second positive integer.
    
    Returns:
        int: The Least Common Multiple of a and b.
    
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
    
    # Calculate LCM using the GCD formula
    gcd = gcd_using_prime_factors(a, b)
    lcm = abs(a * b) // gcd
    
    return lcm