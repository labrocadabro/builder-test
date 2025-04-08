import pytest
from src.fraction import Fraction

def test_fraction_initialization():
    f = Fraction(3, 4)
    assert f.numerator == 3
    assert f.denominator == 4

def test_fraction_simplification():
    f = Fraction(6, 8)
    assert f.numerator == 3
    assert f.denominator == 4

def test_negative_fractions():
    f1 = Fraction(-3, 4)
    assert f1.numerator == -3
    assert f1.denominator == 4

    f2 = Fraction(3, -4)
    assert f2.numerator == -3
    assert f2.denominator == 4

def test_zero_numerator():
    f = Fraction(0, 5)
    assert f.numerator == 0
    assert f.denominator == 1

def test_invalid_denominator():
    with pytest.raises(ValueError, match="Denominator cannot be zero"):
        Fraction(1, 0)

def test_invalid_type():
    with pytest.raises(TypeError, match="Numerator and denominator must be integers"):
        Fraction(1.5, 3)
    with pytest.raises(TypeError, match="Numerator and denominator must be integers"):
        Fraction(1, '3')

def test_equality():
    f1 = Fraction(1, 2)
    f2 = Fraction(2, 4)
    f3 = Fraction(3, 6)
    
    assert f1 == f2
    assert f1 == f3
    assert f2 == f3

def test_addition():
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 3)
    result = f1 + f2
    assert result == Fraction(5, 6)

def test_subtraction():
    f1 = Fraction(3, 4)
    f2 = Fraction(1, 4)
    result = f1 - f2
    assert result == Fraction(1, 2)

def test_multiplication():
    f1 = Fraction(2, 3)
    f2 = Fraction(3, 4)
    result = f1 * f2
    assert result == Fraction(1, 2)

def test_division():
    f1 = Fraction(3, 4)
    f2 = Fraction(2, 3)
    result = f1 / f2
    assert result == Fraction(9, 8)

def test_division_by_zero():
    f1 = Fraction(1, 2)
    f2 = Fraction(0, 1)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        f1 / f2

def test_str_representation():
    f = Fraction(3, 4)
    assert str(f) == "3/4"

def test_repr_representation():
    f = Fraction(3, 4)
    assert repr(f) == "Fraction(3, 4)"