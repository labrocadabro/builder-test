from src.fraction_simplifier import simplify_fraction
from src.lcm_calculator import lcm_using_gcd

class Fraction:
    """
    Comprehensive Fraction class supporting various mathematical operations.
    Handles mixed numbers, improper fractions, and provides robust arithmetic.
    """
    
    def __init__(self, numerator: int, denominator: int = 1, whole: int = 0):
        """
        Initialize a Fraction, supporting whole numbers and mixed number formats.
        
        Args:
            numerator (int): Numerator of the fraction part
            denominator (int, optional): Denominator of the fraction part. Defaults to 1.
            whole (int, optional): Whole number part. Defaults to 0.
        
        Raises:
            ValueError: For invalid fraction or zero denominator
            TypeError: For non-integer inputs
        """
        if not all(isinstance(x, int) for x in [numerator, denominator, whole]):
            raise TypeError("All inputs must be integers")
        
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        
        # Handle sign and convert to improper fraction
        sign = -1 if (whole < 0) ^ (numerator < 0) else 1
        
        total_numerator = abs(whole) * abs(denominator) + abs(numerator)
        total_numerator *= sign
        
        # Simplify the fraction
        self.numerator, self.denominator = simplify_fraction(total_numerator, abs(denominator))
    
    @classmethod
    def from_decimal(cls, decimal: float, max_denominator: int = 1000):
        """
        Create a Fraction from a decimal representation.
        
        Args:
            decimal (float): Decimal number to convert
            max_denominator (int, optional): Maximum denominator to use. Defaults to 1000.
        
        Returns:
            Fraction: Fractional representation of the decimal
        """
        from fractions import Fraction as StdFraction
        std_fraction = StdFraction(decimal).limit_denominator(max_denominator)
        return cls(std_fraction.numerator, std_fraction.denominator)
    
    def __str__(self) -> str:
        """String representation of the fraction."""
        return f"{self.numerator}/{self.denominator}"
    
    def __repr__(self) -> str:
        """Detailed representation for debugging."""
        return f"Fraction({self.numerator}, {self.denominator})"
    
    def __float__(self) -> float:
        """Convert fraction to float."""
        return self.numerator / self.denominator
    
    def __int__(self) -> int:
        """Convert fraction to integer (floor division)."""
        return self.numerator // self.denominator
    
    def __add__(self, other):
        """Add two fractions."""
        if not isinstance(other, Fraction):
            other = Fraction(other)
        
        # Find LCM of denominators
        lcm = lcm_using_gcd(self.denominator, other.denominator)
        
        # Scale numerators
        self_factor = lcm // self.denominator
        other_factor = lcm // other.denominator
        
        new_numerator = self.numerator * self_factor + other.numerator * other_factor
        
        return Fraction(new_numerator, lcm)
    
    def __sub__(self, other):
        """Subtract two fractions."""
        if not isinstance(other, Fraction):
            other = Fraction(other)
        
        # Find LCM of denominators
        lcm = lcm_using_gcd(self.denominator, other.denominator)
        
        # Scale numerators
        self_factor = lcm // self.denominator
        other_factor = lcm // other.denominator
        
        new_numerator = self.numerator * self_factor - other.numerator * other_factor
        
        return Fraction(new_numerator, lcm)
    
    def __mul__(self, other):
        """Multiply two fractions."""
        if not isinstance(other, Fraction):
            other = Fraction(other)
        
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        
        return Fraction(new_numerator, new_denominator)
    
    def __truediv__(self, other):
        """Divide two fractions."""
        if not isinstance(other, Fraction):
            other = Fraction(other)
        
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero")
        
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        
        return Fraction(new_numerator, new_denominator)
    
    def __eq__(self, other) -> bool:
        """Check equality of fractions."""
        if not isinstance(other, Fraction):
            other = Fraction(other)
        return self.numerator == other.numerator and self.denominator == other.denominator
    
    def __lt__(self, other) -> bool:
        """Less than comparison."""
        if not isinstance(other, Fraction):
            other = Fraction(other)
        
        # Cross multiply to compare
        return self.numerator * other.denominator < other.numerator * self.denominator
    
    def to_mixed_number(self):
        """
        Convert to mixed number representation.
        
        Returns:
            tuple: (whole_number, numerator, denominator)
        """
        whole = self.numerator // self.denominator
        remainder_numerator = abs(self.numerator % self.denominator)
        sign = 1 if self.numerator >= 0 else -1
        
        return (whole, remainder_numerator * sign, self.denominator)

    def __abs__(self):
        """Absolute value of the fraction."""
        return Fraction(abs(self.numerator), self.denominator)
