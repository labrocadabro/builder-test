import math

class Fraction:
    """
    A class representing a mathematical fraction with comprehensive operations.
    
    Attributes:
        numerator (int): The numerator of the fraction
        denominator (int): The denominator of the fraction
    """
    
    def __init__(self, numerator: int, denominator: int = 1):
        """
        Initialize a Fraction object.
        
        Args:
            numerator (int): The numerator of the fraction
            denominator (int, optional): The denominator of the fraction. Defaults to 1.
        
        Raises:
            TypeError: If numerator or denominator are not integers
            ValueError: If denominator is zero
        """
        # Validate inputs
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Numerator and denominator must be integers")
        
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        
        # Determine sign and work with absolute values
        sign = -1 if numerator * denominator < 0 else 1
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        # Simplify the fraction
        gcd = math.gcd(numerator, denominator)
        self.numerator = sign * (numerator // gcd)
        self.denominator = denominator // gcd
    
    def __str__(self) -> str:
        """
        String representation of the fraction.
        
        Returns:
            str: Fraction in 'numerator/denominator' format
        """
        return f"{self.numerator}/{self.denominator}"
    
    def __repr__(self) -> str:
        """
        Representation of the fraction for debugging.
        
        Returns:
            str: Representation of the Fraction object
        """
        return f"Fraction({self.numerator}, {self.denominator})"
    
    def __add__(self, other):
        """
        Add two fractions.
        
        Args:
            other (Fraction): Another Fraction object
        
        Returns:
            Fraction: The sum of the two fractions
        """
        if not isinstance(other, Fraction):
            other = Fraction(other)
        
        new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        
        return Fraction(new_numerator, new_denominator)
    
    def __sub__(self, other):
        """
        Subtract two fractions.
        
        Args:
            other (Fraction): Another Fraction object
        
        Returns:
            Fraction: The difference between the two fractions
        """
        if not isinstance(other, Fraction):
            other = Fraction(other)
        
        new_numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        
        return Fraction(new_numerator, new_denominator)
    
    def __mul__(self, other):
        """
        Multiply two fractions.
        
        Args:
            other (Fraction): Another Fraction object
        
        Returns:
            Fraction: The product of the two fractions
        """
        if not isinstance(other, Fraction):
            other = Fraction(other)
        
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        
        return Fraction(new_numerator, new_denominator)
    
    def __truediv__(self, other):
        """
        Divide two fractions.
        
        Args:
            other (Fraction): Another Fraction object
        
        Returns:
            Fraction: The quotient of the two fractions
        
        Raises:
            ValueError: If dividing by zero
        """
        if not isinstance(other, Fraction):
            other = Fraction(other)
        
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero")
        
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        
        return Fraction(new_numerator, new_denominator)
    
    def __eq__(self, other) -> bool:
        """
        Check if two fractions are equal.
        
        Args:
            other (Fraction): Another Fraction object
        
        Returns:
            bool: True if fractions are equal, False otherwise
        """
        if not isinstance(other, Fraction):
            other = Fraction(other)
        
        return self.numerator == other.numerator and self.denominator == other.denominator
    
    def simplify(self) -> 'Fraction':
        """
        Return a simplified version of the fraction.
        
        Returns:
            Fraction: The simplified fraction
        """
        return Fraction(self.numerator, self.denominator)