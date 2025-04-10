import pytest
from src.array_flattener import flatten_array

def test_flatten_simple_nested_array():
    """Test flattening a simple nested array."""
    assert flatten_array([1, [2, 3], [4, [5, 6]]]) == [1, 2, 3, 4, 5, 6]

def test_flatten_deeply_nested_array():
    """Test flattening a deeply nested array."""
    assert flatten_array([1, [2, [3, [4]]], 5]) == [1, 2, 3, 4, 5]

def test_flatten_empty_array():
    """Test flattening an empty array."""
    assert flatten_array([]) == []

def test_flatten_single_level_array():
    """Test flattening an already flat array."""
    assert flatten_array([1, 2, 3, 4]) == [1, 2, 3, 4]

def test_flatten_with_float_values():
    """Test flattening an array with float values."""
    assert flatten_array([1.5, [2.7, 3], 4.2]) == [1.5, 2.7, 3, 4.2]

def test_invalid_input_raises_type_error():
    """Test that non-list input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        flatten_array("not a list")

def test_nested_array_with_invalid_type_raises_error():
    """Test that an array with an unsupported type raises a TypeError."""
    with pytest.raises(TypeError, match="Unsupported item type"):
        flatten_array([1, 2, "string", [3, 4]])