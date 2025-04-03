"""
This module provides basic arithmetic operations.

The functions support various numeric types and include error handling
for invalid inputs.
"""

def add(a, b):
    """
    Add two numbers together.
    
    Args:
        a (int or float): First number
        b (int or float): Second number
    
    Returns:
        int or float: Sum of a and b
    
    Raises:
        TypeError: If inputs are not numeric
    """
    # Check if inputs are numeric
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Inputs must be numeric")
    
    return a + b

def subtract(a, b):
    """
    Subtract the second number from the first.
    
    Args:
        a (int or float): Number to subtract from
        b (int or float): Number to subtract
    
    Returns:
        int or float: Difference between a and b
    
    Raises:
        TypeError: If inputs are not numeric
    """
    # Check if inputs are numeric
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Inputs must be numeric")
    
    return a - b

def multiply(a, b):
    """
    Multiply two numbers.
    
    Args:
        a (int or float): First number
        b (int or float): Second number
    
    Returns:
        int or float: Product of a and b
    
    Raises:
        TypeError: If inputs are not numeric
    """
    # Check if inputs are numeric
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Inputs must be numeric")
    
    return a * b

def divide(a, b):
    """
    Divide the first number by the second.
    
    Args:
        a (int or float): Dividend
        b (int or float): Divisor
    
    Returns:
        float: Result of division
    
    Raises:
        TypeError: If inputs are not numeric
        ZeroDivisionError: If divisor is zero
    """
    # Check if inputs are numeric
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Inputs must be numeric")
    
    # Check for division by zero
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    
    return a / b