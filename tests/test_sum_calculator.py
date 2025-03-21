import pytest
from src.sum_calculator import calculate_sum

def test_calculate_sum_basic():
    """Test basic functionality with a simple list."""
    assert calculate_sum([1, 2, 3]) == 8  # 0*1 + 1*2 + 2*3 = 0 + 2 + 6 = 8

def test_calculate_sum_empty_list():
    """Test with an empty list."""
    assert calculate_sum([]) == 0

def test_calculate_sum_negative_numbers():
    """Test with negative numbers."""
    assert calculate_sum([-1, -2, -3]) == -8  # 0*(-1) + 1*(-2) + 2*(-3) = 0 - 2 - 6 = -8

def test_calculate_sum_mixed_numbers():
    """Test with mixed positive and negative numbers."""
    assert calculate_sum([1, -2, 3]) == 4  # 0*1 + 1*(-2) + 2*3 = 0 - 2 + 6 = 4

def test_invalid_input_not_list():
    """Test that a TypeError is raised when input is not a list."""
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_sum("not a list")

def test_invalid_input_non_integers():
    """Test that a TypeError is raised when list contains non-integers."""
    with pytest.raises(TypeError, match="List must contain only integers"):
        calculate_sum([1, 2, "3"])
        
def test_zero_values():
    """Test a list with zero values."""
    assert calculate_sum([0, 0, 0]) == 0