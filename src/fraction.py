from src.gcd_calculator import gcd

class Fraction:
    def __init__(self, numerator: int, denominator: int):
        """
        Initialize a Fraction object.
        
        Args:
            numerator (int): The numerator of the fraction
            denominator (int): The denominator of the fraction
        
        Raises:
            ValueError: If denominator is zero
            TypeError: If numerator or denominator is not an integer
        """
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Numerator and denominator must be integers")
        
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        
        # Determine sign
        sign = 1 if (numerator * denominator) >= 0 else -1
        
        # Use absolute values for GCD calculation
        a, b = abs(numerator), abs(denominator)
        
        # Simplify fraction
        common = gcd(a, b)
        
        self.numerator = sign * (a // common)
        self.denominator = b // common

    def __str__(self) -> str:
        """
        String representation of the fraction.
        
        Returns:
            str: Fraction in 'numerator/denominator' format
        """
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self) -> str:
        """
        Detailed string representation of the fraction.
        
        Returns:
            str: Representation showing class and fraction details
        """
        return f"Fraction({self.numerator}, {self.denominator})"

    def __eq__(self, other) -> bool:
        """
        Check equality of two fractions.
        
        Args:
            other (Fraction): Another fraction to compare
        
        Returns:
            bool: True if fractions are equal, False otherwise
        """
        if not isinstance(other, Fraction):
            return NotImplemented
        
        return (self.numerator == other.numerator and 
                self.denominator == other.denominator)

    def __add__(self, other):
        """
        Add two fractions.
        
        Args:
            other (Fraction): Fraction to add
        
        Returns:
            Fraction: Result of addition
        """
        if not isinstance(other, Fraction):
            raise TypeError("Can only add Fraction to another Fraction")
        
        new_numerator = (self.numerator * other.denominator + 
                         other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        """
        Subtract two fractions.
        
        Args:
            other (Fraction): Fraction to subtract
        
        Returns:
            Fraction: Result of subtraction
        """
        if not isinstance(other, Fraction):
            raise TypeError("Can only subtract Fraction from another Fraction")
        
        new_numerator = (self.numerator * other.denominator - 
                         other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        """
        Multiply two fractions.
        
        Args:
            other (Fraction): Fraction to multiply
        
        Returns:
            Fraction: Result of multiplication
        """
        if not isinstance(other, Fraction):
            raise TypeError("Can only multiply Fraction with another Fraction")
        
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        """
        Divide two fractions.
        
        Args:
            other (Fraction): Fraction to divide by
        
        Returns:
            Fraction: Result of division
        
        Raises:
            ValueError: If attempting to divide by zero
        """
        if not isinstance(other, Fraction):
            raise TypeError("Can only divide Fraction by another Fraction")
        
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero")
        
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        
        return Fraction(new_numerator, new_denominator)