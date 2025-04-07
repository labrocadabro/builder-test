import math
from typing import Union, Tuple

class Fraction:
    """
    A comprehensive fraction class that handles various fraction operations,
    including mixed numbers, improper fractions, and comprehensive arithmetic.
    """
    
    def __init__(self, numerator: int, denominator: int = 1, whole_number: int = 0):
        """
        Initialize a Fraction with support for mixed numbers.
        
        Args:
            numerator (int): The fractional part's numerator
            denominator (int, optional): The fractional part's denominator. Defaults to 1.
            whole_number (int, optional): The whole number part. Defaults to 0.
        
        Raises:
            TypeError: If inputs are not integers
            ValueError: If denominator is zero
        """
        # Validate inputs
        if not all(isinstance(x, int) for x in [numerator, denominator, whole_number]):
            raise TypeError("All inputs must be integers")
        
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        
        # Convert mixed number to improper fraction
        total_numerator = abs(whole_number) * abs(denominator) + abs(numerator)
        
        # Determine sign
        sign = -1 if (whole_number < 0 or numerator < 0) and not (whole_number < 0 and numerator < 0) else 1
        
        # Simplify the fraction
        gcd = math.gcd(total_numerator, denominator)
        
        self.numerator = sign * (total_numerator // gcd)
        self.denominator = denominator // gcd
    
    def __str__(self) -> str:
        """
        String representation of the fraction.
        
        Returns:
            str: Fraction in 'numerator/denominator' or 'whole whole_number numerator/denominator' format
        """
        whole_number, remainder = divmod(abs(self.numerator), self.denominator)
        
        if remainder == 0:
            return str(whole_number * (1 if self.numerator >= 0 else -1))
        
        if whole_number == 0:
            return f"{self.numerator}/{self.denominator}"
        
        return f"{whole_number} {abs(remainder)}/{self.denominator}" if whole_number > 0 else f"-{whole_number} {abs(remainder)}/{self.denominator}"
    
    def __repr__(self) -> str:
        """
        Representation for debugging.
        
        Returns:
            str: Detailed representation of the Fraction
        """
        return f"Fraction({self.numerator}, {self.denominator})"
    
    @classmethod
    def from_string(cls, fraction_str: str) -> 'Fraction':
        """
        Create a Fraction from a string representation.
        
        Args:
            fraction_str (str): String representation of fraction
        
        Returns:
            Fraction: Parsed fraction
        
        Raises:
            ValueError: If string cannot be parsed
        """
        # Handle pure integers
        try:
            return cls(int(fraction_str))
        except ValueError:
            pass
        
        # Handle standard fractions
        parts = fraction_str.split('/')
        if len(parts) == 2:
            return cls(int(parts[0]), int(parts[1]))
        
        # Handle mixed numbers
        parts = fraction_str.split()
        if len(parts) == 2:
            # Whole number with fraction
            whole_number = int(parts[0])
            num, denom = map(int, parts[1].split('/'))
            return cls(num, denom, whole_number)
        
        raise ValueError(f"Cannot parse fraction from '{fraction_str}'")
    
    def _lcm(self, a: int, b: int) -> int:
        """
        Calculate Least Common Multiple.
        
        Args:
            a (int): First number
            b (int): Second number
        
        Returns:
            int: Least Common Multiple
        """
        return abs(a * b) // math.gcd(a, b)
    
    def __add__(self, other: Union['Fraction', int]) -> 'Fraction':
        """
        Add two fractions or a fraction and an integer.
        
        Args:
            other (Fraction or int): Value to add
        
        Returns:
            Fraction: Result of addition
        """
        if isinstance(other, int):
            other = Fraction(other)
        
        # Find LCM of denominators
        lcm = self._lcm(self.denominator, other.denominator)
        
        # Calculate new numerators
        new_numerator = (self.numerator * (lcm // self.denominator) + 
                         other.numerator * (lcm // other.denominator))
        
        return Fraction(new_numerator, lcm)
    
    def __sub__(self, other: Union['Fraction', int]) -> 'Fraction':
        """
        Subtract two fractions or a fraction and an integer.
        
        Args:
            other (Fraction or int): Value to subtract
        
        Returns:
            Fraction: Result of subtraction
        """
        if isinstance(other, int):
            other = Fraction(other)
        
        # Find LCM of denominators
        lcm = self._lcm(self.denominator, other.denominator)
        
        # Calculate new numerators
        new_numerator = (self.numerator * (lcm // self.denominator) - 
                         other.numerator * (lcm // other.denominator))
        
        return Fraction(new_numerator, lcm)
    
    def __mul__(self, other: Union['Fraction', int]) -> 'Fraction':
        """
        Multiply two fractions or a fraction and an integer.
        
        Args:
            other (Fraction or int): Value to multiply
        
        Returns:
            Fraction: Result of multiplication
        """
        if isinstance(other, int):
            other = Fraction(other)
        
        return Fraction(self.numerator * other.numerator, 
                        self.denominator * other.denominator)
    
    def __truediv__(self, other: Union['Fraction', int]) -> 'Fraction':
        """
        Divide two fractions or a fraction and an integer.
        
        Args:
            other (Fraction or int): Value to divide by
        
        Returns:
            Fraction: Result of division
        
        Raises:
            ValueError: If dividing by zero
        """
        if isinstance(other, int):
            other = Fraction(other)
        
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero")
        
        return Fraction(self.numerator * other.denominator, 
                        self.denominator * other.numerator)
    
    def __eq__(self, other: Union['Fraction', int]) -> bool:
        """
        Check equality of fractions.
        
        Args:
            other (Fraction or int): Value to compare
        
        Returns:
            bool: True if fractions are equivalent, False otherwise
        """
        if isinstance(other, int):
            other = Fraction(other)
        
        return (self.numerator * other.denominator == 
                other.numerator * self.denominator)
    
    def to_decimal(self) -> float:
        """
        Convert fraction to decimal.
        
        Returns:
            float: Decimal representation of the fraction
        """
        return self.numerator / self.denominator