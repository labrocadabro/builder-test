from src.gcd_calculator import gcd_using_prime_factors

def lcm_using_gcd(a, b):
    """
    Calculate the Least Common Multiple (LCM) using the Greatest Common Divisor (GCD).
    
    The LCM is calculated using the formula: LCM(a,b) = |a * b| / GCD(a,b)
    
    Args:
        a (int): First positive integer.
        b (int): Second positive integer.
    
    Returns:
        int: The Least Common Multiple of a and b.
    
    Raises:
        ValueError: If inputs are not positive integers.
    """
    # Validate inputs
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Inputs must be integers")
    
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers")
    
    # Special case: if either number is 1, LCM is the other number
    if a == 1:
        return b
    if b == 1:
        return a
    
    # Calculate LCM using GCD formula
    gcd = gcd_using_prime_factors(a, b)
    lcm = abs(a * b) // gcd
    
    return lcm