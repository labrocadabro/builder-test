from src.gcd_calculator import gcd_using_prime_factors

def lcm_using_gcd(a: int, b: int) -> int:
    """
    Calculate the Least Common Multiple (LCM) using the GCD method.
    
    LCM(a, b) = |a * b| / GCD(a, b)
    
    Args:
        a (int): First positive integer
        b (int): Second positive integer
    
    Returns:
        int: The Least Common Multiple of a and b
    
    Raises:
        ValueError: If either input is less than or equal to 0
    """
    # Validate inputs
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers")
    
    # If either input is 0, LCM is 0
    if a == 0 or b == 0:
        return 0
    
    # Calculate LCM using the formula: LCM(a, b) = |a * b| / GCD(a, b)
    gcd = gcd_using_prime_factors(a, b)
    return abs(a * b) // gcd