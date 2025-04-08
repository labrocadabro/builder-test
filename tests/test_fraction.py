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

def test_fraction_negative_signs():
    f1 = Fraction(-3, 4)
    assert f1.numerator == -3
    assert f1.denominator == 4
    
    f2 = Fraction(3, -4)
    assert f2.numerator == -3
    assert f2.denominator == 4

def test_fraction_zero_numerator():
    f = Fraction(0, 5)
    assert f.numerator == 0
    assert f.denominator == 1

def test_fraction_str_representation():
    f = Fraction(3, 4)
    assert str(f) == "3/4"

def test_fraction_repr_representation():
    f = Fraction(3, 4)
    assert repr(f) == "Fraction(3, 4)"

def test_fraction_equality():
    f1 = Fraction(3, 4)
    f2 = Fraction(6, 8)
    assert f1 == f2

def test_fraction_addition():
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 3)
    result = f1 + f2
    assert result == Fraction(5, 6)

def test_fraction_subtraction():
    f1 = Fraction(3, 4)
    f2 = Fraction(1, 4)
    result = f1 - f2
    assert result == Fraction(1, 2)

def test_fraction_multiplication():
    f1 = Fraction(2, 3)
    f2 = Fraction(3, 4)
    result = f1 * f2
    assert result == Fraction(1, 2)

def test_fraction_division():
    f1 = Fraction(3, 4)
    f2 = Fraction(2, 3)
    result = f1 / f2
    assert result == Fraction(9, 8)

def test_invalid_fraction_initialization():
    with pytest.raises(TypeError):
        Fraction("3", 4)
    
    with pytest.raises(TypeError):
        Fraction(3, "4")

def test_zero_denominator():
    with pytest.raises(ValueError):
        Fraction(1, 0)

def test_division_by_zero_fraction():
    f1 = Fraction(3, 4)
    f2 = Fraction(0, 1)
    
    with pytest.raises(ValueError):
        f1 / f2