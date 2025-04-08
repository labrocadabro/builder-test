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

def test_mixed_number_initialization():
    f = Fraction(3, 4, 2)  # 2 3/4
    assert f.numerator == 11
    assert f.denominator == 4

def test_negative_fraction():
    f = Fraction(-3, 4)
    assert f.numerator == -3
    assert f.denominator == 4

def test_zero_numerator():
    f = Fraction(0, 5)
    assert f.numerator == 0
    assert f.denominator == 1

def test_addition():
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 3)
    result = f1 + f2
    assert result.numerator == 5
    assert result.denominator == 6

def test_subtraction():
    f1 = Fraction(3, 4)
    f2 = Fraction(1, 4)
    result = f1 - f2
    assert result.numerator == 1
    assert result.denominator == 2

def test_multiplication():
    f1 = Fraction(2, 3)
    f2 = Fraction(3, 4)
    result = f1 * f2
    assert result.numerator == 1
    assert result.denominator == 2

def test_division():
    f1 = Fraction(3, 4)
    f2 = Fraction(2, 3)
    result = f1 / f2
    assert result.numerator == 9
    assert result.denominator == 8

def test_mixed_number_operations():
    f1 = Fraction(3, 4, 2)  # 2 3/4
    f2 = Fraction(1, 2)
    result = f1 + f2
    assert result.numerator == 11
    assert result.denominator == 4

def test_to_mixed_number():
    f = Fraction(11, 4)  # 2 3/4
    whole, num, denom = f.to_mixed_number()
    assert whole == 2
    assert num == 3
    assert denom == 4

def test_from_decimal():
    f = Fraction.from_decimal(0.75)
    assert f.numerator == 3
    assert f.denominator == 4

def test_comparison():
    f1 = Fraction(1, 2)
    f2 = Fraction(3, 4)
    assert f1 < f2
    assert f1 != f2

def test_float_conversion():
    f = Fraction(1, 2)
    assert float(f) == 0.5

def test_int_conversion():
    f = Fraction(11, 4)
    assert int(f) == 2

def test_absolute_value():
    f = Fraction(-3, 4)
    abs_f = abs(f)
    assert abs_f.numerator == 3
    assert abs_f.denominator == 4

def test_invalid_inputs():
    with pytest.raises(TypeError):
        Fraction("1", 2)
    
    with pytest.raises(ValueError):
        Fraction(1, 0)

def test_division_by_zero():
    f1 = Fraction(3, 4)
    
    with pytest.raises(ValueError):
        f1 / Fraction(0, 1)
