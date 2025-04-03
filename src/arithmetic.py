"""
Basic Arithmetic Operations Module

This module provides simple arithmetic operations including:
- Addition
- Subtraction
- Multiplication
- Division
- Modulo
"""

def add(a, b):
    """
    Adds two numbers and returns the result.
    
    Args:
        a (int or float): First number
        b (int or float): Second number
    
    Returns:
        int or float: Sum of a and b
    
    Raises:
        TypeError: If inputs are not numbers
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both arguments must be numbers")
    return a + b

def subtract(a, b):
    """
    Subtracts the second number from the first.
    
    Args:
        a (int or float): Number to subtract from
        b (int or float): Number to subtract
    
    Returns:
        int or float: Difference between a and b
    
    Raises:
        TypeError: If inputs are not numbers
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both arguments must be numbers")
    return a - b

def multiply(a, b):
    """
    Multiplies two numbers.
    
    Args:
        a (int or float): First number
        b (int or float): Second number
    
    Returns:
        int or float: Product of a and b
    
    Raises:
        TypeError: If inputs are not numbers
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both arguments must be numbers")
    return a * b

def divide(a, b):
    """
    Divides the first number by the second.
    
    Args:
        a (int or float): Numerator
        b (int or float): Denominator
    
    Returns:
        float: Result of a divided by b
    
    Raises:
        TypeError: If inputs are not numbers
        ZeroDivisionError: If b is zero
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both arguments must be numbers")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def modulo(a, b):
    """
    Calculates the remainder of a divided by b.
    
    Args:
        a (int or float): Dividend
        b (int or float): Divisor
    
    Returns:
        int or float: Remainder of a divided by b
    
    Raises:
        TypeError: If inputs are not numbers
        ZeroDivisionError: If b is zero
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both arguments must be numbers")
    if b == 0:
        raise ZeroDivisionError("Cannot calculate modulo with zero")
    
    # Use the definition of modulo that matches the expected behavior
    return a - (b * int(a / b))