from src.gcd_calculator import gcd_using_prime_factors

def lcm_using_gcd(a, b):
    """
    Calculate the Least Common Multiple (LCM) using the GCD method.
    
    The LCM is calculated using the formula: LCM(a, b) = |a * b| / GCD(a, b)
    
    Args:
        a (int): First positive integer.
        b (int): Second positive integer.
    
    Returns:
        int: The Least Common Multiple of a and b.
    
    Raises:
        TypeError: If inputs are not integers.
        ValueError: If inputs are not positive integers.
    """
    # Validate inputs
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Inputs must be integers")
    
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers")
    
    # Special case: if either number is 1, LCM is the maximum of a and b
    if a == 1:
        return b
    if b == 1:
        return a
    
    # Calculate LCM using GCD
    # LCM(a, b) = |a * b| / GCD(a, b)
    gcd = gcd_using_prime_factors(a, b)
    return abs(a * b) // gcd