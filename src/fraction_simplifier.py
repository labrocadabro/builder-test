import math

def simplify_fraction(numerator: int, denominator: int) -> str:
    """
    Simplify a fraction to its lowest terms.
    
    Args:
        numerator (int): The numerator of the fraction
        denominator (int): The denominator of the fraction
    
    Returns:
        str: The simplified fraction in 'numerator/denominator' format
    
    Raises:
        ValueError: If denominator is zero
        TypeError: If inputs are not integers
    """
    # Validate inputs
    if not isinstance(numerator, int) or not isinstance(denominator, int):
        raise TypeError("Numerator and denominator must be integers")
    
    # Check for division by zero
    if denominator == 0:
        raise ValueError("Denominator cannot be zero")
    
    # Handle special cases
    if numerator == 0:
        return "0/1"
    
    # Determine the sign
    sign = -1 if numerator * denominator < 0 else 1
    
    # Work with absolute values
    numerator = abs(numerator)
    denominator = abs(denominator)
    
    # Find the greatest common divisor
    gcd = math.gcd(numerator, denominator)
    
    # Simplify the fraction
    simplified_numerator = sign * (numerator // gcd)
    simplified_denominator = denominator // gcd
    
    return f"{simplified_numerator}/{simplified_denominator}"