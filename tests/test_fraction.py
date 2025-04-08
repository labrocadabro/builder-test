import pytest
import math
from src.fraction import Fraction

class TestFractionInitialization:
    def test_basic_fraction_creation(self):
        """Test basic fraction creation with numerator and denominator"""
        f = Fraction(3, 4)
        assert f.numerator == 3
        assert f.denominator == 4

    def test_fraction_simplification(self):
        """Test that fractions are automatically simplified"""
        f = Fraction(6, 8)
        assert f.numerator == 3
        assert f.denominator == 4

    def test_zero_numerator(self):
        """Test fraction with zero numerator"""
        f = Fraction(0, 5)
        assert f.numerator == 0
        assert f.denominator == 1

    def test_negative_fractions(self):
        """Test various combinations of negative signs"""
        # Negative numerator
        f1 = Fraction(-3, 4)
        assert f1.numerator == -3
        assert f1.denominator == 4

        # Negative denominator
        f2 = Fraction(3, -4)
        assert f2.numerator == -3
        assert f2.denominator == 4

        # Both negative
        f3 = Fraction(-3, -4)
        assert f3.numerator == 3
        assert f3.denominator == 4

    def test_invalid_fraction_creation(self):
        """Test invalid fraction creation"""
        with pytest.raises(TypeError, match="All inputs must be integers"):
            Fraction("3", 4)
        
        with pytest.raises(ValueError, match="Denominator cannot be zero"):
            Fraction(1, 0)

class TestFractionMixedNumbers:
    def test_mixed_number_creation(self):
        """Test creation of mixed numbers"""
        f = Fraction(3, 4, 2)  # 2 3/4
        assert f.numerator == 11
        assert f.denominator == 4

    def test_mixed_number_conversion(self):
        """Test converting fractions to mixed numbers"""
        f = Fraction(11, 4)
        whole, num, denom = f.to_mixed_number()
        assert whole == 2
        assert num == 3
        assert denom == 4

class TestFractionArithmetic:
    def test_addition(self):
        """Test fraction addition"""
        # Simple addition
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        result = f1 + f2
        assert result.numerator == 5
        assert result.denominator == 6

        # Mixed number addition
        f3 = Fraction(3, 4, 2)
        f4 = Fraction(1, 2)
        result = f3 + f4
        assert result.numerator == 13
        assert result.denominator == 4

    def test_subtraction(self):
        """Test fraction subtraction"""
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 4)
        result = f1 - f2
        assert result.numerator == 1
        assert result.denominator == 2

    def test_multiplication(self):
        """Test fraction multiplication"""
        f1 = Fraction(2, 3)
        f2 = Fraction(3, 4)
        result = f1 * f2
        assert result.numerator == 1
        assert result.denominator == 2

    def test_division(self):
        """Test fraction division"""
        f1 = Fraction(3, 4)
        f2 = Fraction(2, 3)
        result = f1 / f2
        assert result.numerator == 9
        assert result.denominator == 8

    def test_division_by_zero(self):
        """Test division by zero fraction"""
        f1 = Fraction(3, 4)
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            f1 / Fraction(0, 1)

class TestFractionConversions:
    def test_float_conversion(self):
        """Test converting fraction to float"""
        f = Fraction(1, 2)
        assert float(f) == 0.5
        assert math.isclose(float(Fraction(1, 3)), 1/3)

    def test_int_conversion(self):
        """Test converting fraction to integer"""
        f1 = Fraction(11, 4)
        assert int(f1) == 2

        f2 = Fraction(-11, 4)
        assert int(f2) == -2

    def test_decimal_conversion(self):
        """Test creating fraction from decimal"""
        f = Fraction.from_decimal(0.75)
        assert f.numerator == 3
        assert f.denominator == 4

        f2 = Fraction.from_decimal(1.5)
        assert f2.numerator == 3
        assert f2.denominator == 2

class TestFractionComparisons:
    def test_equality(self):
        """Test fraction equality"""
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 4)
        f3 = Fraction(3, 4)
        
        assert f1 == f2
        assert f1 != f3

    def test_less_than_greater_than(self):
        """Test fraction comparisons"""
        f1 = Fraction(1, 2)
        f2 = Fraction(3, 4)
        
        assert f1 < f2
        assert f2 > f1

class TestFractionUtilities:
    def test_absolute_value(self):
        """Test absolute value of fractions"""
        f1 = Fraction(-3, 4)
        abs_f1 = abs(f1)
        assert abs_f1.numerator == 3
        assert abs_f1.denominator == 4

    def test_string_representations(self):
        """Test string representations of fractions"""
        f = Fraction(3, 4)
        assert str(f) == "3/4"
        assert repr(f).startswith("Fraction(")
